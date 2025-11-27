# proto-assist-2361-2489

## BackendAPI - Run Instructions

The FastAPI app lives at `BackendAPI/src/api/main.py` and the ASGI application object is `app`.

To run the server on port 3001 with the correct module path:

Option 1: Use the provided entrypoint script
```bash
cd BackendAPI
python run.py
```

Environment overrides:
```bash
HOST=127.0.0.1 PORT=3001 RELOAD=true python run.py
```

Option 2: Run uvicorn directly (ensure current working directory is `BackendAPI`)
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 3001
```