"""Page service functions."""

from __future__ import annotations

from typing import Any

from packages.pylib.src.orm.page import Page
from packages.pylib.src.query import page as page_query


def _serialize_page(page: Page) -> dict[str, Any]:
    return {
        "id": page.id,
        "outlet_id": page.outlet_id,
        "html": page.html,
        "created_at": page.created_at,
        "updated_at": page.updated_at,
    }


def lazyload_pages(page_num: int, page_size: int) -> dict[str, Any]:
    result = page_query.lazyload_pages(page_num, page_size)
    return {
        **result,
        "items": [_serialize_page(page) for page in result["items"]],
    }


def get_by_id(page_id: int) -> dict[str, Any] | None:
    page = page_query.get_by_id(page_id)
    if page is None:
        return None
    return _serialize_page(page)


def create(data: dict[str, Any]) -> dict[str, Any]:
    page = page_query.create(data)
    return _serialize_page(page)


def update(page_id: int, data: dict[str, Any]) -> dict[str, Any] | None:
    page = page_query.update(page_id, data)
    if page is None:
        return None
    return _serialize_page(page)
