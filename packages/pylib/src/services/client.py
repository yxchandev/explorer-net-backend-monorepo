"""Client service functions."""

from __future__ import annotations

from typing import Any

from packages.pylib.src.orm.client import Client
from packages.pylib.src.query import client as client_query


def _serialize_client(client: Client) -> dict[str, Any]:
    return {
        "id": client.id,
        "email": client.email,
        "business_name": client.business_name,
        "country_code": client.country_code,
        "telephone": client.telephone,
        "remark": client.remark,
        "verified": client.verified,
        "reset_password": client.reset_password,
        "created_at": client.created_at,
        "updated_at": client.updated_at,
    }


def lazyload_clients(page: int, page_size: int) -> dict[str, Any]:
    result = client_query.lazyload_clients(page, page_size)
    return {
        **result,
        "items": [_serialize_client(client) for client in result["items"]],
    }


def get_by_id(client_id: int) -> dict[str, Any] | None:
    client = client_query.get_by_id(client_id)
    if client is None:
        return None
    return _serialize_client(client)


def create(data: dict[str, Any]) -> dict[str, Any]:
    client = client_query.create(data)
    return _serialize_client(client)


def update(client_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    client = client_query.update(client_id, data)
    if client is None:
        return None
    return _serialize_client(client)
