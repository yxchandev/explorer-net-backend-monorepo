# Explorer Net Consumer Backend API

uv workspace with a FastAPI app and a shared `pylib` package.

## Layout

```
apps/api          # FastAPI application
packages/pylib    # Shared library (workspace member)
```

## Setup

```powershell
uv sync
```

## Run the API

```powershell
uv run api
# or
uv run uvicorn api.main:app --reload
```

Then open http://127.0.0.1:8000/docs

- `GET /health` — liveness check
- `GET /hello?name=Ada` — uses `pylib.greet`

## Add dependencies

```powershell
# API only
uv add --package api httpx

# Shared library
uv add --package pylib pydantic
```
