"""Consumer service functions."""


def get_by_id(consumer_id: str) -> dict[str, str]:
    return {
        "status": "ok",
        "message": "Consumer retrieved",
        "id": consumer_id,
    }
