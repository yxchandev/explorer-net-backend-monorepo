"""Business menu routes."""

from fastapi import APIRouter, Depends

from apps.business.src.controllers import menu
from packages.pylib.src.models.business.menu import (
    MenuCreateRequest,
    MenuIdPath,
    MenuListResponse,
    MenuResponse,
    MenuUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery

router = APIRouter(tags=["menu"])


@router.get("/menus", response_model=MenuListResponse)
def get_menus(query: PaginationQuery = Depends()) -> MenuListResponse:
    return menu.get_menus(query)


@router.get("/menu/{id}", response_model=MenuResponse)
def get_menu(id: int) -> MenuResponse:
    return menu.get_menu(MenuIdPath(id=id))


@router.put("/menu/{id}", response_model=MenuResponse)
def update_menu(id: int, body: MenuUpdateRequest) -> MenuResponse:
    return menu.update_menu(MenuIdPath(id=id), body)


@router.post("/menu", response_model=MenuResponse, status_code=201)
def create_menu(body: MenuCreateRequest) -> MenuResponse:
    return menu.create_menu(body)
