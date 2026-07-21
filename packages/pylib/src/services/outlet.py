"""Outlet service functions."""

from __future__ import annotations

from typing import Any

from packages.pylib.src.orm.outlet import Outlet
from packages.pylib.src.query import outlet as outlet_query


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
    result = outlet_query.lazyload_outlets(page, page_size)
    return {
        **result,
        "items": [_serialize_outlet(outlet) for outlet in result["items"]],
    }


def get_by_id(outlet_id: int) -> dict[str, Any] | None:
    outlet = outlet_query.get_by_id(outlet_id)
    if outlet is None:
        return None
    return _serialize_outlet(outlet)


def create(data: dict[str, Any]) -> dict[str, Any]:
    outlet = outlet_query.create(data)
    return _serialize_outlet(outlet)


def update(outlet_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    outlet = outlet_query.update(outlet_id, data)
    if outlet is None:
        return None
    return _serialize_outlet(outlet)
