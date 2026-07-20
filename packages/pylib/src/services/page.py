"""Page service functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.page import Page
from packages.pylib.src.utils.db import session_scope
from packages.pylib.src.utils.pagination import lazyload


def _serialize_page(page: Page) -> dict[str, Any]:
    return {
        "id": page.id,
        "outlet_id": page.outlet_id,
        "html": page.html,
        "created_at": page.created_at,
        "updated_at": page.updated_at,
    }


def lazyload_pages(page_num: int, page_size: int) -> dict[str, Any]:
    stmt = select(Page).order_by(Page.id)
    with session_scope() as session:
        return lazyload(session, stmt, page_num, page_size, _serialize_page)


def get_by_id(page_id: int) -> dict[str, Any] | None:
    with session_scope() as session:
        page = session.get(Page, page_id)
        if page is None:
            return None
        return _serialize_page(page)


def create(data: dict[str, Any]) -> dict[str, Any]:
    with session_scope() as session:
        page = Page(**data)
        session.add(page)
        session.flush()
        session.refresh(page)
        return _serialize_page(page)


def update(page_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    with session_scope() as session:
        page = session.get(Page, page_id)
        if page is None:
            return None
        for key, value in data.items():
            setattr(page, key, value)
        session.flush()
        session.refresh(page)
        return _serialize_page(page)
