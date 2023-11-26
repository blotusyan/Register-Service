import json
import os
import sys
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Iterable,
    Mapping,
    Tuple,
    Union,
)

from multidict import CIMultiDict, CIMultiDictProxy, MultiDict, MultiDictProxy, istr
from yarl import URL

# These are for other modules to use (to avoid repeating the conditional import).
if sys.version_info >= (3, 8):
    from typing import Final as Final
    from typing import Protocol as Protocol
    from typing import TypedDict as TypedDict
else:
    from typing_extensions import Final
    from typing_extensions import Protocol as Protocol  # noqa: F401
    from typing_extensions import TypedDict as TypedDict

DEFAULT_JSON_ENCODER = json.dumps
DEFAULT_JSON_DECODER = json.loads

if TYPE_CHECKING:  # pragma: no cover
    _CIMultiDict = CIMultiDict[str]
    _CIMultiDictProxy = CIMultiDictProxy[str]
    _MultiDict = MultiDict[str]
    _MultiDictProxy = MultiDictProxy[str]
    from http.cookies import BaseCookie, Morsel

    from .web import Request, StreamResponse
else:
    _CIMultiDict = CIMultiDict
    _CIMultiDictProxy = CIMultiDictProxy
    _MultiDict = MultiDict
    _MultiDictProxy = MultiDictProxy

Byteish = Union[bytes, bytearray, memoryview]
JSONEncoder = Callable[[Any], str]
JSONDecoder = Callable[[str], Any]
LooseHeaders = Union[Mapping[Union[str, istr], str], _CIMultiDict, _CIMultiDictProxy]
RawHeaders = Tuple[Tuple[bytes, bytes], ...]
StrOrURL = Union[str, URL]

LooseCookiesMappings = Mapping[str, Union[str, "BaseCookie[str]", "Morsel[Any]"]]
LooseCookiesIterables = Iterable[
    Tuple[str, Union[str, "BaseCookie[str]", "Morsel[Any]"]]
]
LooseCookies = Union[
    LooseCookiesMappings,
    LooseCookiesIterables,
    "BaseCookie[str]",
]

Handler = Callable[["Request"], Awaitable["StreamResponse"]]

PathLike = Union[str, "os.PathLike[str]"]
