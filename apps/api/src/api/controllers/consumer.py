"""Consumer controllers with Pydantic request/response models."""

from pydantic import BaseModel, Field

from pylib.services import consumer as consumer_service


class ConsumerIdPath(BaseModel):
    id: str = Field(min_length=1)


class ConsumerResponse(BaseModel):
    status: str
    message: str
    id: str


def get_by_id(path: ConsumerIdPath) -> ConsumerResponse:
    result = consumer_service.get_by_id(consumer_id=path.id)
    return ConsumerResponse.model_validate(result)
