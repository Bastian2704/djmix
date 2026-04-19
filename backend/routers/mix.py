from fastapi import APIRouter

router = APIRouter()

@router.post("/render")
async def render_mix(data: dict):
    """Recibe configuración completa del mix y encola procesamiento."""
    # TODO: llamar a audio.py via Celery
    return {"status": "enqueued"}

@router.get("/status/{job_id}")
async def mix_status(job_id: str):
    """Consulta el estado del job de Celery."""
    # TODO: consultar Celery result backend
    return {"job_id": job_id, "status": "pending"}

@router.get("/download/{job_id}")
async def download_mix(job_id: str):
    """Devuelve el ZIP del mix exportado."""
    # TODO: devolver FileResponse
    return {"job_id": job_id}
