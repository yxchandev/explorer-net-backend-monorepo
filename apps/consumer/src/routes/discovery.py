"""Discovery routes."""

from fastapi import APIRouter

from apps.consumer.src.controllers import discovery
from packages.pylib.src.models.consumer.discovery import SearchRequest, SearchResponse

router = APIRouter(prefix="/discovery", tags=["discovery"])


@router.post("/search", response_model=SearchResponse)
def search(body: SearchRequest) -> SearchResponse:
    return discovery.search(body)
