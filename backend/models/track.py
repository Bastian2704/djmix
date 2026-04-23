from typing import Optional
from pydantic import BaseModel


class TrackInfo(BaseModel):
    id: str
    youtube_id: str
    title: str
    duration: float
    file_path: str
    thumbnail: Optional[str] = None
    uploader: Optional[str] = None
    downloaded_at: str
