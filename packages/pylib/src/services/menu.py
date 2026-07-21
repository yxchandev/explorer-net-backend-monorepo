"""Menu service functions."""

from __future__ import annotations

from typing import Any

from packages.pylib.src.orm.menu import Menu
from packages.pylib.src.query import menu as menu_query


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
    result = menu_query.lazyload_menus(page, page_size)
    return {
        **result,
        "items": [_serialize_menu(menu) for menu in result["items"]],
    }


def get_by_id(menu_id: int) -> dict[str, Any] | None:
    menu = menu_query.get_by_id(menu_id)
    if menu is None:
        return None
    return _serialize_menu(menu)


def create(data: dict[str, Any]) -> dict[str, Any]:
    menu = menu_query.create(data)
    return _serialize_menu(menu)


def update(menu_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    menu = menu_query.update(menu_id, data)
    if menu is None:
        return None
    return _serialize_menu(menu)
