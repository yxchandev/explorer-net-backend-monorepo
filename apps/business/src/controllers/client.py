"""Business client controllers."""

from fastapi import HTTPException, status

from packages.pylib.src.models.business.client import (
    ClientCreateRequest,
    ClientIdPath,
    ClientListResponse,
    ClientResponse,
    ClientUpdateRequest,
)
from packages.pylib.src.models.common.pagination import PaginationQuery
from packages.pylib.src.services import client


def get_clients(query: PaginationQuery) -> ClientListResponse:
    result = client.lazyload_clients(page=query.page, page_size=query.page_size)
    return ClientListResponse.model_validate(result)


def get_client(path: ClientIdPath) -> ClientResponse:
    result = client.get_by_id(path.id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return ClientResponse.model_validate(result)


def create_client(body: ClientCreateRequest) -> ClientResponse:
    result = client.create(body.model_dump())
    return ClientResponse.model_validate(result)


def update_client(path: ClientIdPath, body: ClientUpdateRequest) -> ClientResponse:
    result = client.update(path.id, body.model_dump(exclude_unset=True))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
    return ClientResponse.model_validate(result)
