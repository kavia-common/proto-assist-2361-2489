from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

# PUBLIC_INTERFACE
app = FastAPI(
    title="Proto Assistant Backend API",
    description=(
        "Core service layer for Proto Assistant. This service handles health checks and "
        "serves as the ASGI application entrypoint for Uvicorn."
    ),
    version="1.0.0",
)

# Configure permissive CORS for now; refine for production environments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production via env
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get("/", summary="Health Check", tags=["Health"])
def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify the API is running.

    Returns:
        A JSON object with a simple status message.
    """
    return {"message": "Healthy"}
