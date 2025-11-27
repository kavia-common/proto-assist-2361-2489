#!/usr/bin/env python3
"""
PUBLIC_INTERFACE
Entrypoint script to launch the FastAPI application with Uvicorn.

This script ensures the correct module path is used so Uvicorn can import
the ASGI application object. It starts the server on port 3001 by default.

Environment variables:
- HOST: The host interface to bind to (default: 0.0.0.0)
- PORT: The port to listen on (default: 3001)
- RELOAD: Enable auto-reload in development when set to "true" (default: False)

Usage:
    python run.py
    HOST=127.0.0.1 PORT=3001 RELOAD=true python run.py
"""
import os
import uvicorn


# PUBLIC_INTERFACE
def main():
    """Start the Uvicorn server pointing to the FastAPI app."""
    host = os.getenv("HOST", "0.0.0.0")
    port_str = os.getenv("PORT", "3001")
    try:
        port = int(port_str)
    except ValueError:
        # Fallback with a sensible default if invalid env provided
        port = 3001

    reload_env = os.getenv("RELOAD", "false").lower() == "true"

    # Use the correct module path to the FastAPI app
    # Package structure: src/api/main.py with 'app' defined
    uvicorn.run(
        "src.api.main:app",
        host=host,
        port=port,
        reload=reload_env,
        factory=False,
    )


if __name__ == "__main__":
    main()
