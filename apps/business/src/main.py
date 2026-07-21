from fastapi import APIRouter, FastAPI

from apps.business.src.routes.client import router as client_router
from apps.business.src.routes.menu import router as menu_router
from apps.business.src.routes.outlet import router as outlet_router
from apps.business.src.routes.page import router as page_router

app = FastAPI(title="Explorer Net Business API", version="0.1.0")

api = APIRouter(prefix="/api")
api.include_router(client_router)
api.include_router(outlet_router)
api.include_router(menu_router)
api.include_router(page_router)
app.include_router(api)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
