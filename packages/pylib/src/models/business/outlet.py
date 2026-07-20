"""Business outlet Pydantic models."""

from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from packages.pylib.src.models.common.pagination import PaginatedResponse
from packages.pylib.src.models.enums import Country


class OutletResponse(BaseModel):
    id: int
    country: Country
    unit: str
    address1: str
    address2: str | None
    postcode: str
    latitude: Decimal
    longitude: Decimal
    phone_number: int
    description: str | None
    client_id: int
    created_at: datetime
    updated_at: datetime


class OutletCreateRequest(BaseModel):
    country: Country
    unit: str = Field(min_length=1)
    address1: str = Field(min_length=1)
    address2: str | None = None
    postcode: str = Field(min_length=1)
    latitude: Decimal
    longitude: Decimal
    phone_number: int
    description: str | None = None
    client_id: int = Field(gt=0)


class OutletUpdateRequest(BaseModel):
    country: Country | None = None
    unit: str | None = Field(default=None, min_length=1)
    address1: str | None = Field(default=None, min_length=1)
    address2: str | None = None
    postcode: str | None = Field(default=None, min_length=1)
    latitude: Decimal | None = None
    longitude: Decimal | None = None
    phone_number: int | None = None
    description: str | None = None
    client_id: int | None = Field(default=None, gt=0)


class OutletIdPath(BaseModel):
    id: int = Field(gt=0)


class OutletListResponse(PaginatedResponse[OutletResponse]):
    pass
