# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing_extensions import Literal

from .._models import BaseModel
from .embedding import Embedding

__all__ = ["CreateEmbeddingResponse", "Usage"]


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens used by the prompt."""

    total_tokens: int
    """The total number of tokens used by the request."""


class CreateEmbeddingResponse(BaseModel):
    data: List[Embedding]
    """The list of embeddings generated by the model."""

    model: str
    """The name of the model used to generate the embedding."""

    object: Literal["list"]
    """The object type, which is always "list"."""

    usage: Usage
    """The usage information for the request."""
