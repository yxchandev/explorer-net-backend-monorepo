"""Outlet service functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.outlet import Outlet
from packages.pylib.src.utils.db import session_scope
from packages.pylib.src.utils.pagination import lazyload


def _serialize_outlet(outlet: Outlet) -> dict[str, Any]:
    return {
        "id": outlet.id,
        "country": outlet.country,
        "unit": outlet.unit,
        "address1": outlet.address1,
        "address2": outlet.address2,
        "postcode": outlet.postcode,
        "latitude": outlet.latitude,
        "longitude": outlet.longitude,
        "phone_number": outlet.phone_number,
        "description": outlet.description,
        "client_id": outlet.client_id,
        "created_at": outlet.created_at,
        "updated_at": outlet.updated_at,
    }


def lazyload_outlets(page: int, page_size: int) -> dict[str, Any]:
    stmt = select(Outlet).order_by(Outlet.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size, _serialize_outlet)


def get_by_id(outlet_id: int) -> dict[str, Any] | None:
    with session_scope() as session:
        outlet = session.get(Outlet, outlet_id)
        if outlet is None:
            return None
        return _serialize_outlet(outlet)


def create(data: dict[str, Any]) -> dict[str, Any]:
    with session_scope() as session:
        outlet = Outlet(**data)
        session.add(outlet)
        session.flush()
        session.refresh(outlet)
        return _serialize_outlet(outlet)


def update(outlet_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    with session_scope() as session:
        outlet = session.get(Outlet, outlet_id)
        if outlet is None:
            return None
        for key, value in data.items():
            setattr(outlet, key, value)
        session.flush()
        session.refresh(outlet)
        return _serialize_outlet(outlet)
