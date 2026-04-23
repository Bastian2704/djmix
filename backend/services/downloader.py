import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Optional

import yt_dlp

DOWNLOADS_DIR = Path("/app/music/downloads")


_EXTRACTOR_ARGS = {"youtube": {"player_client": ["ios", "web"]}}


def _ydl_opts(hooks: list) -> dict:
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    return {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": str(DOWNLOADS_DIR / "%(id)s.%(ext)s"),
        "ignoreerrors": True,
        "quiet": True,
        "no_warnings": True,
        "progress_hooks": hooks,
        "extractor_args": _EXTRACTOR_ARGS,
    }


def get_playlist_entries(url: str) -> list[dict]:
    """Extract playlist entry list without downloading (fast)."""
    opts = {
        "extract_flat": True,
        "quiet": True,
        "ignoreerrors": True,
        "extractor_args": _EXTRACTOR_ARGS,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    if not info:
        return []
    entries = info.get("entries") or [info]
    return [
        {
            "id": e["id"],
            "title": e.get("title") or e["id"],
            "duration": e.get("duration") or 0,
        }
        for e in entries
        if e and e.get("id")
    ]


def download_playlist(
    url: str,
    progress_callback: Optional[Callable[[int, int, str, float], None]] = None,
) -> list[dict]:
    """
    Download all tracks from a YouTube playlist (or single video) as MP3.
    Skips tracks already present on disk.
    Returns list of track metadata dicts.
    """
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    entries = get_playlist_entries(url)
    total = len(entries)
    results: list[dict] = []

    for i, entry in enumerate(entries, start=1):
        youtube_id = entry["id"]
        meta_path = DOWNLOADS_DIR / f"{youtube_id}.json"

        if meta_path.exists():
            with open(meta_path) as f:
                results.append(json.load(f))
            if progress_callback:
                progress_callback(i, total, entry["title"], 100.0)
            continue

        def _hook(d, _id=youtube_id, _title=entry["title"], _i=i):
            if d["status"] == "downloading" and progress_callback:
                raw = d.get("_percent_str", "0%").strip().replace("%", "")
                try:
                    pct = float(raw)
                except ValueError:
                    pct = 0.0
                progress_callback(_i, total, _title, pct)

        with yt_dlp.YoutubeDL(_ydl_opts([_hook])) as ydl:
            info = ydl.extract_info(
                f"https://www.youtube.com/watch?v={youtube_id}", download=True
            )

        if not info:
            continue

        meta: dict = {
            "id": youtube_id,
            "youtube_id": youtube_id,
            "title": info.get("title") or entry["title"],
            "duration": float(info.get("duration") or 0),
            "file_path": str(DOWNLOADS_DIR / f"{youtube_id}.mp3"),
            "thumbnail": info.get("thumbnail"),
            "uploader": info.get("uploader"),
            "downloaded_at": datetime.now(timezone.utc).isoformat(),
        }

        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)

        results.append(meta)
        if progress_callback:
            progress_callback(i, total, meta["title"], 100.0)

    return results
