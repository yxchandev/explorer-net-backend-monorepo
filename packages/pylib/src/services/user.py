"""User service functions."""

from __future__ import annotations

from typing import Any

from packages.pylib.src.orm.user import User
from packages.pylib.src.query import user as user_query


def _serialize_user(user: User) -> dict[str, Any]:
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "telephone": user.telephone,
        "email": user.email,
        "country_code": user.country_code,
        "reset_password": user.reset_password,
        "remark": user.remark,
        "verified": user.verified,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }


def lazyload_users(page: int, page_size: int) -> dict[str, Any]:
    result = user_query.lazyload_users(page, page_size)
    return {
        **result,
        "items": [_serialize_user(user) for user in result["items"]],
    }


def get_by_id(user_id: int) -> dict[str, Any] | None:
    user = user_query.get_by_id(user_id)
    if user is None:
        return None
    return _serialize_user(user)


def create(data: dict[str, Any]) -> dict[str, Any]:
    user = user_query.create(data)
    return _serialize_user(user)


def update(user_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    user = user_query.update(user_id, data)
    if user is None:
        return None
    return _serialize_user(user)
