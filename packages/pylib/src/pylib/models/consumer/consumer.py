"""Consumer profile request/response models."""

from pydantic import BaseModel, Field


class ConsumerIdPath(BaseModel):
    id: str = Field(min_length=1)


class ConsumerResponse(BaseModel):
    status: str
    message: str
    id: str
