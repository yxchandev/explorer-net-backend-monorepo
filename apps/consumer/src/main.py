from fastapi import FastAPI

from apps.consumer.src.routes.authentication import router as authentication_router
from apps.consumer.src.routes.consumer import router as consumer_router
from apps.consumer.src.routes.discovery import router as discovery_router
from apps.consumer.src.routes.user import router as user_router

app = FastAPI(title="Explorer Net Consumer API", version="0.1.0")

app.include_router(authentication_router)
app.include_router(discovery_router)
app.include_router(consumer_router)
app.include_router(user_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
