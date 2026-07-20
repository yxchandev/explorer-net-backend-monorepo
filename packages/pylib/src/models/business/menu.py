"""Business menu Pydantic models."""

from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from packages.pylib.src.models.common.pagination import PaginatedResponse
from packages.pylib.src.models.enums import Currency


class MenuResponse(BaseModel):
    id: int
    outlet_id: int
    name: str
    price: Decimal
    currency: Currency
    category: str
    created_at: datetime
    updated_at: datetime


class MenuCreateRequest(BaseModel):
    outlet_id: int = Field(gt=0)
    name: str = Field(min_length=1)
    price: Decimal = Field(gt=0)
    currency: Currency
    category: str = Field(min_length=1)


class MenuUpdateRequest(BaseModel):
    outlet_id: int | None = Field(default=None, gt=0)
    name: str | None = Field(default=None, min_length=1)
    price: Decimal | None = Field(default=None, gt=0)
    currency: Currency | None = None
    category: str | None = Field(default=None, min_length=1)


class MenuIdPath(BaseModel):
    id: int = Field(gt=0)


class MenuListResponse(PaginatedResponse[MenuResponse]):
    pass
