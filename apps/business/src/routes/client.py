"""Business client routes."""

from fastapi import APIRouter, Depends

from apps.business.src.controllers import client
from packages.pylib.src.models.business.client import (
    ClientCreateRequest,
    ClientIdPath,
    ClientListResponse,
    ClientResponse,
    ClientUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery

router = APIRouter(tags=["client"])


@router.get("/clients", response_model=ClientListResponse)
def get_clients(query: PaginationQuery = Depends()) -> ClientListResponse:
    return client.get_clients(query)


@router.get("/client/{id}", response_model=ClientResponse)
def get_client(id: int) -> ClientResponse:
    return client.get_client(ClientIdPath(id=id))


@router.put("/client/{id}", response_model=ClientResponse)
def update_client(id: int, body: ClientUpdateRequest) -> ClientResponse:
    return client.update_client(ClientIdPath(id=id), body)


@router.post("/client", response_model=ClientResponse, status_code=201)
def create_client(body: ClientCreateRequest) -> ClientResponse:
    return client.create_client(body)
