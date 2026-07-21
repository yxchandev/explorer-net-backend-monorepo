"""Client database query functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.client import Client
from packages.pylib.src.query.lazyload import lazyload
from packages.pylib.src.utils.db import session_scope


def lazyload_clients(page: int, page_size: int) -> dict[str, Any]:
    stmt = select(Client).order_by(Client.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size)


def get_by_id(client_id: int) -> Client | None:
    with session_scope() as session:
        return session.get(Client, client_id)


def create(data: dict[str, Any]) -> Client:
    with session_scope() as session:
        client = Client(**data)
        session.add(client)
        session.flush()
        session.refresh(client)
        return client


def update(client_id: int, data: dict[str, Any]) -> Client | None:
    with session_scope() as session:
        client = session.get(Client, client_id)
        if client is None:
            return None
        for key, value in data.items():
            setattr(client, key, value)
        session.flush()
        session.refresh(client)
        return client
