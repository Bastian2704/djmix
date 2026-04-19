from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import playlist, tracks, mix

app = FastAPI(title="DJMix API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(playlist.router, prefix="/api/playlist", tags=["playlist"])
app.include_router(tracks.router,   prefix="/api/tracks",   tags=["tracks"])
app.include_router(mix.router,      prefix="/api/mix",      tags=["mix"])

@app.get("/api/health")
def health():
    return {"status": "ok"}
