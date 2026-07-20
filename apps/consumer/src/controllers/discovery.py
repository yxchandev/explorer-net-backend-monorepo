"""Consumer discovery controllers."""

from packages.pylib.src.models.consumer.discovery import SearchRequest, SearchResponse
from packages.pylib.src.services import discovery


def search(body: SearchRequest) -> SearchResponse:
    result = discovery.search(query=body.query)
    return SearchResponse.model_validate(result)
