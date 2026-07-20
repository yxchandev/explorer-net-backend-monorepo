"""Menu service functions."""

from __future__ import annotations

from typing import Any

from sqlalchemy import select

from packages.pylib.src.orm.menu import Menu
from packages.pylib.src.utils.db import session_scope
from packages.pylib.src.utils.pagination import lazyload


def _serialize_menu(menu: Menu) -> dict[str, Any]:
    return {
        "id": menu.id,
        "outlet_id": menu.outlet_id,
        "name": menu.name,
        "price": menu.price,
        "currency": menu.currency,
        "category": menu.category,
        "created_at": menu.created_at,
        "updated_at": menu.updated_at,
    }


def lazyload_menus(page: int, page_size: int) -> dict[str, Any]:
    stmt = select(Menu).order_by(Menu.id)
    with session_scope() as session:
        return lazyload(session, stmt, page, page_size, _serialize_menu)


def get_by_id(menu_id: int) -> dict[str, Any] | None:
    with session_scope() as session:
        menu = session.get(Menu, menu_id)
        if menu is None:
            return None
        return _serialize_menu(menu)


def create(data: dict[str, Any]) -> dict[str, Any]:
    with session_scope() as session:
        menu = Menu(**data)
        session.add(menu)
        session.flush()
        session.refresh(menu)
        return _serialize_menu(menu)


def update(menu_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    with session_scope() as session:
        menu = session.get(Menu, menu_id)
        if menu is None:
            return None
        for key, value in data.items():
            setattr(menu, key, value)
        session.flush()
        session.refresh(menu)
        return _serialize_menu(menu)
