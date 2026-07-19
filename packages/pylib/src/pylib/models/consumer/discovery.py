"""Consumer discovery request/response models."""

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)


class SearchResponse(BaseModel):
    status: str
    message: str
    query: str
    results: list[dict[str, object]] = Field(default_factory=list)
