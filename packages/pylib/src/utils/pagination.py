"""Pagination helpers for SQLAlchemy queries."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session

T = TypeVar("T")


def lazyload(
    session: Session,
    stmt: Select[tuple[T]],
    page: int,
    page_size: int,
    mapper: Callable[[T], dict[str, Any]],
) -> dict[str, Any]:
    """Paginate a SQLAlchemy select statement."""
    count_stmt = select(func.count()).select_from(stmt.subquery())
    total = session.scalar(count_stmt) or 0
    rows = session.scalars(
        stmt.offset((page - 1) * page_size).limit(page_size)
    ).all()
    return {
        "items": [mapper(row) for row in rows],
        "total": total,
        "page": page,
        "page_size": page_size,
    }
