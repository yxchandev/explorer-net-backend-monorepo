"""Consumer profile controllers."""

from packages.pylib.src.models.consumer.consumer import ConsumerIdPath, ConsumerResponse
from packages.pylib.src.services import consumer


def get_by_id(path: ConsumerIdPath) -> ConsumerResponse:
    result = consumer.get_by_id(consumer_id=path.id)
    return ConsumerResponse.model_validate(result)
