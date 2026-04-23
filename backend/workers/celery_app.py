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
