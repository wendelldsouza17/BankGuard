from fastapi import FastAPI

from backend.app.config import settings


app = FastAPI(title=settings.app_name)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": settings.app_name,
    }