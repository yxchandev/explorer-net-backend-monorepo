"""Consumer user routes."""

from fastapi import APIRouter, Depends

from apps.consumer.src.controllers import user
from packages.pylib.src.models.common.pagination import PaginationQuery
from packages.pylib.src.models.consumer.user import (
    UserCreateRequest,
    UserIdPath,
    UserListResponse,
    UserResponse,
    UserUpdateRequest,
)

router = APIRouter(tags=["user"])


@router.get("/users", response_model=UserListResponse)
def get_users(query: PaginationQuery = Depends()) -> UserListResponse:
    return user.get_users(query)


@router.get("/user/{id}", response_model=UserResponse)
def get_user(id: int) -> UserResponse:
    return user.get_user(UserIdPath(id=id))


@router.put("/user/{id}", response_model=UserResponse)
def update_user(id: int, body: UserUpdateRequest) -> UserResponse:
    return user.update_user(UserIdPath(id=id), body)


@router.post("/user", response_model=UserResponse, status_code=201)
def create_user(body: UserCreateRequest) -> UserResponse:
    return user.create_user(body)
