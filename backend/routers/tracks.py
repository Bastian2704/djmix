import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1

router = APIRouter()

DOWNLOADS_DIR = Path("/app/music/downloads")


def _read_mp3_meta(path: Path, track_id: str, original_name: str) -> dict:
    duration = 0.0
    title = Path(original_name).stem
    artist = ""
    try:
        audio = MP3(str(path))
        duration = round(audio.info.length, 3)
    except Exception:
        pass
    try:
        tags = ID3(str(path))
        if tags.get("TIT2"):
            title = str(tags["TIT2"])
        if tags.get("TPE1"):
            artist = str(tags["TPE1"])
    except Exception:
        pass
    return {
        "id": track_id,
        "title": title,
        "artist": artist,
        "duration": duration,
        "file_path": str(path),
        "original_name": original_name,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
    }


@router.post("/upload", status_code=201)
async def upload_track(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".mp3"):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos MP3")

    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    track_id = uuid.uuid4().hex
    mp3_path = DOWNLOADS_DIR / f"{track_id}.mp3"
    meta_path = DOWNLOADS_DIR / f"{track_id}.json"

    content = await file.read()
    mp3_path.write_bytes(content)

    meta = _read_mp3_meta(mp3_path, track_id, file.filename)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    return meta


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
