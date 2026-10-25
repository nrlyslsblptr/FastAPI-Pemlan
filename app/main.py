
from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="MediTrack API",
    description=(
        "API untuk pencatatan jadwal obat dan catatan "
        "kesehatan harian. Bukan alat diagnosis medis."
    ),
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "MediTrack API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
