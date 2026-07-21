"""Outlet database query functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.outlet import Outlet
from packages.pylib.src.query.lazyload import lazyload
from packages.pylib.src.utils.db import session_scope


def lazyload_outlets(page: int, page_size: int) -> dict[str, Any]:
    stmt = select(Outlet).order_by(Outlet.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size)


def get_by_id(outlet_id: int) -> Outlet | None:
    with session_scope() as session:
        return session.get(Outlet, outlet_id)


def create(data: dict[str, Any]) -> Outlet:
    with session_scope() as session:
        outlet = Outlet(**data)
        session.add(outlet)
        session.flush()
        session.refresh(outlet)
        return outlet


def update(outlet_id: int, data: dict[str, Any]) -> Outlet | None:
    with session_scope() as session:
        outlet = session.get(Outlet, outlet_id)
        if outlet is None:
            return None
        for key, value in data.items():
            setattr(outlet, key, value)
        session.flush()
        session.refresh(outlet)
        return outlet
