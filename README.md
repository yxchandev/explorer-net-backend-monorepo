# Explorer Net Consumer Backend API

uv workspace with FastAPI apps and a shared `pylib` package.

## Layout

```
apps/consumer/src     # Consumer FastAPI app (import: consumer.*)
apps/business/src     # Business FastAPI app (import: business.*)
packages/pylib/src    # Shared library (import: pylib.*)
```

## Setup

```powershell
uv sync
```

## Run

```powershell
# Consumer (port 8000)
uv run --package consumer consumer

# Business (port 8001)
uv run --package business business
```

Then open:
- http://127.0.0.1:8000/docs (consumer)
- http://127.0.0.1:8001/docs (business)

## Add dependencies

```powershell
# Consumer only
uv add --package consumer httpx

# Business only
uv add --package business httpx

# Shared library
uv add --package pylib pydantic
```
