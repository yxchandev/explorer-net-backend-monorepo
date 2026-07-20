"""Business page routes."""

from fastapi import APIRouter, Depends

from apps.business.src.controllers import page
from packages.pylib.src.models.business.page import (
    PageCreateRequest,
    PageIdPath,
    PageListResponse,
    PageResponse,
    PageUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery

router = APIRouter(tags=["page"])


@router.get("/pages", response_model=PageListResponse)
def get_pages(query: PaginationQuery = Depends()) -> PageListResponse:
    return page.get_pages(query)


@router.get("/page/{id}", response_model=PageResponse)
def get_page(id: int) -> PageResponse:
    return page.get_page(PageIdPath(id=id))


@router.put("/page/{id}", response_model=PageResponse)
def update_page(id: int, body: PageUpdateRequest) -> PageResponse:
    return page.update_page(PageIdPath(id=id), body)


@router.post("/page", response_model=PageResponse, status_code=201)
def create_page(body: PageCreateRequest) -> PageResponse:
    return page.create_page(body)
