"""Business menu controllers."""

from fastapi import HTTPException, status

from packages.pylib.src.models.business.menu import (
    MenuCreateRequest,
    MenuIdPath,
    MenuListResponse,
    MenuResponse,
    MenuUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery
from packages.pylib.src.services import menu


def get_menus(query: PaginationQuery) -> MenuListResponse:
    result = menu.lazyload_menus(page=query.page, page_size=query.page_size)
    return MenuListResponse.model_validate(result)


def get_menu(path: MenuIdPath) -> MenuResponse:
    result = menu.get_by_id(path.id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found")
    return MenuResponse.model_validate(result)


def create_menu(body: MenuCreateRequest) -> MenuResponse:
    result = menu.create(body.model_dump())
    return MenuResponse.model_validate(result)


def update_menu(path: MenuIdPath, body: MenuUpdateRequest) -> MenuResponse:
    result = menu.update(path.id, body.model_dump(exclude_unset=True))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found")
    return MenuResponse.model_validate(result)
