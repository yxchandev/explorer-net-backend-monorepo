from fastapi import FastAPI

from consumer.routes.authentication import router as authentication_router
from consumer.routes.consumer import router as consumer_router
from consumer.routes.discovery import router as discovery_router

app = FastAPI(title="Explorer Net Consumer API", version="0.1.0")

app.include_router(authentication_router)
app.include_router(discovery_router)
app.include_router(consumer_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
