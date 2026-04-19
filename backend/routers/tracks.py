from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_tracks():
    """Lista todas las canciones descargadas."""
    # TODO: leer desde music/downloads
    return {"tracks": []}

@router.get("/{track_id}")
async def get_track(track_id: str):
    """Devuelve info de una canción."""
    # TODO: buscar por id
    return {"track_id": track_id}

@router.delete("/{track_id}")
async def delete_track(track_id: str):
    """Elimina una canción."""
    # TODO: borrar archivo
    return {"deleted": track_id}
