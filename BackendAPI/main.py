"""
FastAPI application entrypoint for uvicorn.

This module re-exports the app instance from the internal package path
so that 'uvicorn main:app' works when started from the BackendAPI root.
"""

# PUBLIC_INTERFACE
from src.api.main import app  # noqa: F401

__all__ = ["app"]
