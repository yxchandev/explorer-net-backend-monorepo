"""Consumer user controllers."""

from fastapi import HTTPException, status

from packages.pylib.src.models.common.pagination import PaginationQuery
from packages.pylib.src.models.consumer.user import (
    UserCreateRequest,
    UserIdPath,
    UserListResponse,
    UserResponse,
    UserUpdateRequest,
)
from packages.pylib.src.services import user


def get_users(query: PaginationQuery) -> UserListResponse:
    result = user.lazyload_users(page=query.page, page_size=query.page_size)
    return UserListResponse.model_validate(result)


def get_user(path: UserIdPath) -> UserResponse:
    result = user.get_by_id(path.id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserResponse.model_validate(result)


def create_user(body: UserCreateRequest) -> UserResponse:
    result = user.create(body.model_dump())
    return UserResponse.model_validate(result)


def update_user(path: UserIdPath, body: UserUpdateRequest) -> UserResponse:
    result = user.update(path.id, body.model_dump(exclude_unset=True))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserResponse.model_validate(result)
