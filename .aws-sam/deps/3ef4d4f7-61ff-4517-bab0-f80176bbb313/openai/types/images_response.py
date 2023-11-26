# File generated from our OpenAPI spec by Stainless.

from typing import List

from .._models import BaseModel
from .image import Image

__all__ = ["ImagesResponse"]


class ImagesResponse(BaseModel):
    created: int

    data: List[Image]