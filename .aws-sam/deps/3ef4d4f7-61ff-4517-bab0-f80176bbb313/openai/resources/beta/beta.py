# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import AsyncAPIResource, SyncAPIResource
from .assistants import (
    Assistants,
    AssistantsWithRawResponse,
    AsyncAssistants,
    AsyncAssistantsWithRawResponse,
)
from .threads import (
    AsyncThreads,
    AsyncThreadsWithRawResponse,
    Threads,
    ThreadsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import AsyncOpenAI, OpenAI

__all__ = ["Beta", "AsyncBeta"]


class Beta(SyncAPIResource):
    assistants: Assistants
    threads: Threads
    with_raw_response: BetaWithRawResponse

    def __init__(self, client: OpenAI) -> None:
        super().__init__(client)
        self.assistants = Assistants(client)
        self.threads = Threads(client)
        self.with_raw_response = BetaWithRawResponse(self)


class AsyncBeta(AsyncAPIResource):
    assistants: AsyncAssistants
    threads: AsyncThreads
    with_raw_response: AsyncBetaWithRawResponse

    def __init__(self, client: AsyncOpenAI) -> None:
        super().__init__(client)
        self.assistants = AsyncAssistants(client)
        self.threads = AsyncThreads(client)
        self.with_raw_response = AsyncBetaWithRawResponse(self)


class BetaWithRawResponse:
    def __init__(self, beta: Beta) -> None:
        self.assistants = AssistantsWithRawResponse(beta.assistants)
        self.threads = ThreadsWithRawResponse(beta.threads)


class AsyncBetaWithRawResponse:
    def __init__(self, beta: AsyncBeta) -> None:
        self.assistants = AsyncAssistantsWithRawResponse(beta.assistants)
        self.threads = AsyncThreadsWithRawResponse(beta.threads)
