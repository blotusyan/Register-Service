# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionFunctionMessageParam"]


class ChatCompletionFunctionMessageParam(TypedDict, total=False):
    content: Required[Optional[str]]
    """The return value from the function call, to return to the model."""

    name: Required[str]
    """The name of the function to call."""

    role: Required[Literal["function"]]
    """The role of the messages author, in this case `function`."""