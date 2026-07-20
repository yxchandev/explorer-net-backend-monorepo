"""Consumer routes."""

from fastapi import APIRouter

from apps.consumer.src.controllers import consumer
from packages.pylib.src.models.consumer.consumer import ConsumerIdPath, ConsumerResponse

router = APIRouter(prefix="/consumer", tags=["consumer"])


@router.get("/{id}", response_model=ConsumerResponse)
def get_consumer(id: str) -> ConsumerResponse:
    return consumer.get_by_id(ConsumerIdPath(id=id))
