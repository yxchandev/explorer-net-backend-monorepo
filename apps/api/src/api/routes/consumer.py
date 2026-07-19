"""Consumer routes."""

from fastapi import APIRouter

from api.controllers import consumer as consumer_controller
from api.controllers.consumer import ConsumerIdPath, ConsumerResponse

router = APIRouter(prefix="/consumer", tags=["consumer"])


@router.get("/{id}", response_model=ConsumerResponse)
def get_consumer(id: str) -> ConsumerResponse:
    return consumer_controller.get_by_id(ConsumerIdPath(id=id))
