"""Discovery service functions."""


def search(query: str) -> dict[str, object]:
    return {
        "status": "ok",
        "message": "Search completed",
        "query": query,
        "results": [],
    }
