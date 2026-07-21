"""Page database query functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.page import Page
from packages.pylib.src.query.lazyload import lazyload
from packages.pylib.src.utils.db import session_scope


def lazyload_pages(page_num: int, page_size: int) -> dict[str, Any]:
    stmt = select(Page).order_by(Page.id)
    with session_scope() as session:
        return lazyload(session, stmt, page_num, page_size)


def get_by_id(page_id: int) -> Page | None:
    with session_scope() as session:
        return session.get(Page, page_id)


def create(data: dict[str, Any]) -> Page:
    with session_scope() as session:
        page = Page(**data)
        session.add(page)
        session.flush()
        session.refresh(page)
        return page


def update(page_id: int, data: dict[str, Any]) -> Page | None:
    with session_scope() as session:
        page = session.get(Page, page_id)
        if page is None:
            return None
        for key, value in data.items():
            setattr(page, key, value)
        session.flush()
        session.refresh(page)
        return page
