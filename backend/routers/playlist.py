from fastapi import APIRouter

router = APIRouter()

@router.post("/import")
async def import_playlist(data: dict):
    """Recibe URL de playlist de YouTube y encola descarga."""
    # TODO: llamar a downloader.py
    return {"status": "enqueued", "url": data.get("url")}
