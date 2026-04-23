import json
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

DOWNLOADS_DIR = Path("/app/music/downloads")


@router.get("/")
async def list_tracks():
    if not DOWNLOADS_DIR.exists():
        return {"tracks": []}
    tracks = [
        json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(DOWNLOADS_DIR.glob("*.json"))
    ]
    return {"tracks": tracks}


@router.get("/{track_id}/audio")
async def get_track_audio(track_id: str):
    mp3 = DOWNLOADS_DIR / f"{track_id}.mp3"
    if not mp3.exists():
        raise HTTPException(status_code=404, detail="Track not found")
    return FileResponse(mp3, media_type="audio/mpeg", filename=mp3.name)


@router.get("/{track_id}")
async def get_track(track_id: str):
    meta = DOWNLOADS_DIR / f"{track_id}.json"
    if not meta.exists():
        raise HTTPException(status_code=404, detail="Track not found")
    return json.loads(meta.read_text(encoding="utf-8"))


@router.delete("/{track_id}")
async def delete_track(track_id: str):
    meta = DOWNLOADS_DIR / f"{track_id}.json"
    if not meta.exists():
        raise HTTPException(status_code=404, detail="Track not found")
    meta.unlink(missing_ok=True)
    (DOWNLOADS_DIR / f"{track_id}.mp3").unlink(missing_ok=True)
    return {"deleted": track_id}
