from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class PlaylistImportRequest(BaseModel):
    url: str


@router.post("/import", status_code=202)
async def import_playlist(body: PlaylistImportRequest):
    from workers.celery_app import download_playlist
    task = download_playlist.delay(body.url)
    return {"job_id": task.id, "status": "enqueued"}


@router.get("/status/{job_id}")
async def playlist_status(job_id: str):
    from celery.result import AsyncResult
    from workers.celery_app import celery

    result = AsyncResult(job_id, app=celery)
    state = result.state

    if state == "PENDING":
        return {"job_id": job_id, "status": "pending"}

    if state == "PROGRESS":
        info = result.info or {}
        return {
            "job_id": job_id,
            "status": "progress",
            "current": info.get("current", 0),
            "total": info.get("total", 0),
            "track": info.get("track", ""),
            "percent": info.get("percent", 0.0),
        }

    if state == "SUCCESS":
        return {"job_id": job_id, "status": "done", "tracks": result.result}

    if state == "FAILURE":
        raise HTTPException(status_code=500, detail=str(result.result))

    return {"job_id": job_id, "status": state.lower()}
