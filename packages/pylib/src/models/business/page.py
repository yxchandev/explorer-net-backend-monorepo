"""Business page Pydantic models."""

from datetime import datetime

from pydantic import BaseModel, Field

from packages.pylib.src.models.common.pagination import PaginatedResponse


class PageResponse(BaseModel):
    id: int
    outlet_id: int
    html: str
    created_at: datetime
    updated_at: datetime


class PageCreateRequest(BaseModel):
    outlet_id: int = Field(gt=0)
    html: str = Field(min_length=1)


class PageUpdateRequest(BaseModel):
    outlet_id: int | None = Field(default=None, gt=0)
    html: str | None = Field(default=None, min_length=1)


class PageIdPath(BaseModel):
    id: int = Field(gt=0)


class PageListResponse(PaginatedResponse[PageResponse]):
    pass
