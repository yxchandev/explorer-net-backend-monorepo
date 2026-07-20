"""Business outlet routes."""

from fastapi import APIRouter, Depends

from apps.business.src.controllers import outlet
from packages.pylib.src.models.business.outlet import (
    OutletCreateRequest,
    OutletIdPath,
    OutletListResponse,
    OutletResponse,
    OutletUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery

router = APIRouter(tags=["outlet"])


@router.get("/outlets", response_model=OutletListResponse)
def get_outlets(query: PaginationQuery = Depends()) -> OutletListResponse:
    return outlet.get_outlets(query)


@router.get("/outlet/{id}", response_model=OutletResponse)
def get_outlet(id: int) -> OutletResponse:
    return outlet.get_outlet(OutletIdPath(id=id))


@router.put("/outlet/{id}", response_model=OutletResponse)
def update_outlet(id: int, body: OutletUpdateRequest) -> OutletResponse:
    return outlet.update_outlet(OutletIdPath(id=id), body)


@router.post("/outlet", response_model=OutletResponse, status_code=201)
def create_outlet(body: OutletCreateRequest) -> OutletResponse:
    return outlet.create_outlet(body)
