"""Business client Pydantic models."""

from datetime import datetime

from pydantic import BaseModel, Field

from packages.pylib.src.models.common.pagination import PaginatedResponse


class ClientResponse(BaseModel):
    id: int
    email: str
    business_name: str
    country_code: int
    telephone: int
    remark: str | None
    verified: bool
    reset_password: bool
    created_at: datetime
    updated_at: datetime


class ClientCreateRequest(BaseModel):
    email: str = Field(min_length=1)
    business_name: str = Field(min_length=1)
    country_code: int
    telephone: int
    password: str = Field(min_length=8)
    remark: str | None = None
    verified: bool = False
    reset_password: bool = False


class ClientUpdateRequest(BaseModel):
    email: str | None = Field(default=None, min_length=1)
    business_name: str | None = Field(default=None, min_length=1)
    country_code: int | None = None
    telephone: int | None = None
    password: str | None = Field(default=None, min_length=8)
    remark: str | None = None
    verified: bool | None = None
    reset_password: bool | None = None


class ClientIdPath(BaseModel):
    id: int = Field(gt=0)


class ClientListResponse(PaginatedResponse[ClientResponse]):
    pass
