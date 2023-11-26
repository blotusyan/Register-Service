# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import AsyncAPIResource, SyncAPIResource
from .completions import (
    AsyncCompletions,
    AsyncCompletionsWithRawResponse,
    Completions,
    CompletionsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import AsyncOpenAI, OpenAI

__all__ = ["Chat", "AsyncChat"]


class Chat(SyncAPIResource):
    completions: Completions
    with_raw_response: ChatWithRawResponse

    def __init__(self, client: OpenAI) -> None:
        super().__init__(client)
        self.completions = Completions(client)
        self.with_raw_response = ChatWithRawResponse(self)


class AsyncChat(AsyncAPIResource):
    completions: AsyncCompletions
    with_raw_response: AsyncChatWithRawResponse

    def __init__(self, client: AsyncOpenAI) -> None:
        super().__init__(client)
        self.completions = AsyncCompletions(client)
        self.with_raw_response = AsyncChatWithRawResponse(self)


class ChatWithRawResponse:
    def __init__(self, chat: Chat) -> None:
        self.completions = CompletionsWithRawResponse(chat.completions)


class AsyncChatWithRawResponse:
    def __init__(self, chat: AsyncChat) -> None:
        self.completions = AsyncCompletionsWithRawResponse(chat.completions)
