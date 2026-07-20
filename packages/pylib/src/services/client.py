"""Client service functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.client import Client
from packages.pylib.src.utils.db import session_scope
from packages.pylib.src.utils.pagination import lazyload


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
    stmt = select(Client).order_by(Client.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size, _serialize_client)


def get_by_id(client_id: int) -> dict[str, Any] | None:
    with session_scope() as session:
        client = session.get(Client, client_id)
        if client is None:
            return None
        return _serialize_client(client)


def create(data: dict[str, Any]) -> dict[str, Any]:
    with session_scope() as session:
        client = Client(**data)
        session.add(client)
        session.flush()
        session.refresh(client)
        return _serialize_client(client)


def update(client_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    with session_scope() as session:
        client = session.get(Client, client_id)
        if client is None:
            return None
        for key, value in data.items():
            setattr(client, key, value)
        session.flush()
        session.refresh(client)
        return _serialize_client(client)
