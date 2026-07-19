"""Discovery controllers with Pydantic request/response models."""

from pydantic import BaseModel, Field

from pylib.services import discovery as discovery_service


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)


class SearchResponse(BaseModel):
    status: str
    message: str
    query: str
    results: list[dict[str, object]] = Field(default_factory=list)


def search(body: SearchRequest) -> SearchResponse:
    result = discovery_service.search(query=body.query)
    return SearchResponse.model_validate(result)
