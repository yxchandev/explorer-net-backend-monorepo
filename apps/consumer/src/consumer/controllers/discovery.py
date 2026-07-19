"""Consumer discovery controllers."""

from pylib.models.consumer.discovery import SearchRequest, SearchResponse
from pylib.services import discovery as discovery_service


def search(body: SearchRequest) -> SearchResponse:
    result = discovery_service.search(query=body.query)
    return SearchResponse.model_validate(result)
