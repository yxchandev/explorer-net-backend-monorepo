"""User service functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.user import User
from packages.pylib.src.utils.db import session_scope
from packages.pylib.src.utils.pagination import lazyload


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
    stmt = select(User).order_by(User.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size, _serialize_user)


def get_by_id(user_id: int) -> dict[str, Any] | None:
    with session_scope() as session:
        user = session.get(User, user_id)
        if user is None:
            return None
        return _serialize_user(user)


def create(data: dict[str, Any]) -> dict[str, Any]:
    with session_scope() as session:
        user = User(**data)
        session.add(user)
        session.flush()
        session.refresh(user)
        return _serialize_user(user)


def update(user_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    with session_scope() as session:
        user = session.get(User, user_id)
        if user is None:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        session.flush()
        session.refresh(user)
        return _serialize_user(user)
