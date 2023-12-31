from __future__ import annotations

from typing import TYPE_CHECKING

from typing_extensions import override

from .._exceptions import OpenAIError
from .._utils import LazyProxy

INSTRUCTIONS = """

You tried to access openai.{symbol}, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742
"""


class APIRemovedInV1(OpenAIError):
    def __init__(self, *, symbol: str) -> None:
        super().__init__(INSTRUCTIONS.format(symbol=symbol))


class APIRemovedInV1Proxy(LazyProxy[None]):
    def __init__(self, *, symbol: str) -> None:
        super().__init__()
        self._symbol = symbol

    @override
    def __load__(self) -> None:
        raise APIRemovedInV1(symbol=self._symbol)


SYMBOLS = [
    "Edit",
    "File",
    "Audio",
    "Image",
    "Model",
    "Engine",
    "Customer",
    "FineTune",
    "Embedding",
    "Completion",
    "Deployment",
    "Moderation",
    "ErrorObject",
    "FineTuningJob",
    "ChatCompletion",
]

# we explicitly tell type checkers that nothing is exported
# from this file so that when we re-export the old symbols
# in `openai/__init__.py` they aren't added to the auto-complete
# suggestions given by editors
if TYPE_CHECKING:
    __all__: list[str] = []
else:
    __all__ = SYMBOLS


__locals = locals()
for symbol in SYMBOLS:
    __locals[symbol] = APIRemovedInV1Proxy(symbol=symbol)
