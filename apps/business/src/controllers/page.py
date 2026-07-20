"""Business page controllers."""

from fastapi import HTTPException, status

from packages.pylib.src.models.business.page import (
    PageCreateRequest,
    PageIdPath,
    PageListResponse,
    PageResponse,
    PageUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery
from packages.pylib.src.services import page


def get_pages(query: PaginationQuery) -> PageListResponse:
    result = page.lazyload_pages(page_num=query.page, page_size=query.page_size)
    return PageListResponse.model_validate(result)


def get_page(path: PageIdPath) -> PageResponse:
    result = page.get_by_id(path.id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not found")
    return PageResponse.model_validate(result)


def create_page(body: PageCreateRequest) -> PageResponse:
    result = page.create(body.model_dump())
    return PageResponse.model_validate(result)


def update_page(path: PageIdPath, body: PageUpdateRequest) -> PageResponse:
    result = page.update(path.id, body.model_dump(exclude_unset=True))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not found")
    return PageResponse.model_validate(result)
