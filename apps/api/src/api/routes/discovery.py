"""Discovery routes."""

from fastapi import APIRouter

from api.controllers import discovery as discovery_controller
from api.controllers.discovery import SearchRequest, SearchResponse

router = APIRouter(prefix="/discovery", tags=["discovery"])


@router.post("/search", response_model=SearchResponse)
def search(body: SearchRequest) -> SearchResponse:
    return discovery_controller.search(body)
