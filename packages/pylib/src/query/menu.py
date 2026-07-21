"""Menu database query functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.menu import Menu
from packages.pylib.src.query.lazyload import lazyload
from packages.pylib.src.utils.db import session_scope


def lazyload_menus(page: int, page_size: int) -> dict[str, Any]:
    stmt = select(Menu).order_by(Menu.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size)


def get_by_id(menu_id: int) -> Menu | None:
    with session_scope() as session:
        return session.get(Menu, menu_id)


def create(data: dict[str, Any]) -> Menu:
    with session_scope() as session:
        menu = Menu(**data)
        session.add(menu)
        session.flush()
        session.refresh(menu)
        return menu


def update(menu_id: int, data: dict[str, Any]) -> Menu | None:
    with session_scope() as session:
        menu = session.get(Menu, menu_id)
        if menu is None:
            return None
        for key, value in data.items():
            setattr(menu, key, value)
        session.flush()
        session.refresh(menu)
        return menu
