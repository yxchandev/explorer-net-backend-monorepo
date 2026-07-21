"""User database query functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.user import User
from packages.pylib.src.query.lazyload import lazyload
from packages.pylib.src.utils.db import session_scope


def lazyload_users(page: int, page_size: int) -> dict[str, Any]:
    stmt = select(User).order_by(User.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size)


def get_by_id(user_id: int) -> User | None:
    with session_scope() as session:
        return session.get(User, user_id)


def create(data: dict[str, Any]) -> User:
    with session_scope() as session:
        user = User(**data)
        session.add(user)
        session.flush()
        session.refresh(user)
        return user


def update(user_id: int, data: dict[str, Any]) -> User | None:
    with session_scope() as session:
        user = session.get(User, user_id)
        if user is None:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        session.flush()
        session.refresh(user)
        return user
