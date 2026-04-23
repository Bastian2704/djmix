import os
from celery import Celery

celery = Celery(
    "djmix",
    broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0"),
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
)


@celery.task(bind=True, name="workers.celery_app.download_playlist")
def download_playlist(self, url: str) -> list[dict]:
    from services.downloader import download_playlist as _download

    def on_progress(current: int, total: int, title: str, percent: float) -> None:
        self.update_state(
            state="PROGRESS",
            meta={
                "current": current,
                "total": total,
                "track": title,
                "percent": round(percent, 1),
            },
        )

    return _download(url, progress_callback=on_progress)
