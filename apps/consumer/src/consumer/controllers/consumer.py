"""Consumer profile controllers."""

from pylib.models.consumer.consumer import ConsumerIdPath, ConsumerResponse
from pylib.services import consumer as consumer_service


def get_by_id(path: ConsumerIdPath) -> ConsumerResponse:
    result = consumer_service.get_by_id(consumer_id=path.id)
    return ConsumerResponse.model_validate(result)
