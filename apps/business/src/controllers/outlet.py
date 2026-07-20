"""Business outlet controllers."""

from fastapi import HTTPException, status

from packages.pylib.src.models.business.outlet import (
    OutletCreateRequest,
    OutletIdPath,
    OutletListResponse,
    OutletResponse,
    OutletUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery
from packages.pylib.src.services import outlet


def get_outlets(query: PaginationQuery) -> OutletListResponse:
    result = outlet.lazyload_outlets(page=query.page, page_size=query.page_size)
    return OutletListResponse.model_validate(result)


def get_outlet(path: OutletIdPath) -> OutletResponse:
    result = outlet.get_by_id(path.id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Outlet not found")
    return OutletResponse.model_validate(result)


def create_outlet(body: OutletCreateRequest) -> OutletResponse:
    result = outlet.create(body.model_dump())
    return OutletResponse.model_validate(result)


def update_outlet(path: OutletIdPath, body: OutletUpdateRequest) -> OutletResponse:
    result = outlet.update(path.id, body.model_dump(exclude_unset=True))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Outlet not found")
    return OutletResponse.model_validate(result)
