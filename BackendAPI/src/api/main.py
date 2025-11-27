from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app with minimal metadata and tags to support /openapi.json generation
app = FastAPI(
    title="Proto Assistant Backend API",
    description="Minimal FastAPI app exposing a health endpoint for service availability checks.",
    version="0.1.0",
    openapi_tags=[
        {"name": "health", "description": "Service health and readiness endpoints"}
    ],
)

# Enable permissive CORS for now (can be restricted later via env configuration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get(
    "/",
    tags=["health"],
    summary="Health Check",
    description="Returns a simple confirmation that the API service is healthy and reachable.",
    operation_id="health_check",
)
def health_check():
    """
    Health check endpoint.

    Returns:
        dict: A simple JSON payload confirming the service is healthy.
    """
    return {"status": "ok"}
