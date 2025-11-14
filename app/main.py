from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title="FinSight API",
    version="0.1.0",
    description="Backend API for the FinSight AI-powered personal finance dashboard."
)


@app.get("/")
def read_root():
    """
    Simple health check endpoint to verify that the API is running.
    """
    return {
        "message": "FinSight API is running",
        "environment": settings.APP_ENV,
    }
