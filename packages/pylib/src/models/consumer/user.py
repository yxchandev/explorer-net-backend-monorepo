"""Consumer user Pydantic models."""

from datetime import datetime

from pydantic import BaseModel, Field

from packages.pylib.src.models.common.pagination import PaginatedResponse


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    telephone: int
    email: str
    country_code: int
    reset_password: bool
    remark: str | None
    verified: bool
    created_at: datetime
    updated_at: datetime


class UserCreateRequest(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str = Field(min_length=8)
    telephone: int
    email: str = Field(min_length=1)
    country_code: int
    remark: str | None = None
    verified: bool = False
    reset_password: bool = False


class UserUpdateRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=1)
    last_name: str | None = Field(default=None, min_length=1)
    password: str | None = Field(default=None, min_length=8)
    telephone: int | None = None
    email: str | None = Field(default=None, min_length=1)
    country_code: int | None = None
    remark: str | None = None
    verified: bool | None = None
    reset_password: bool | None = None


class UserIdPath(BaseModel):
    id: int = Field(gt=0)


class UserListResponse(PaginatedResponse[UserResponse]):
    pass
