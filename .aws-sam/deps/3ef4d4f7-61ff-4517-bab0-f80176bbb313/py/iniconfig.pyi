from typing import Callable, Iterator, Mapping, Optional, Tuple, TypeVar, Union

from typing_extensions import Final

_D = TypeVar("_D")
_T = TypeVar("_T")

class ParseError(Exception):
    # Private __init__.
    path: Final[str]
    lineno: Final[int]
    msg: Final[str]

class SectionWrapper:
    # Private __init__.
    config: Final[IniConfig]
    name: Final[str]
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> Iterator[str]: ...
    def get(
        self, key: str, default: _D = ..., convert: Callable[[str], _T] = ...
    ) -> Union[_T, _D]: ...
    def items(self) -> Iterator[Tuple[str, str]]: ...
    def lineof(self, name: str) -> Optional[int]: ...

class IniConfig:
    path: Final[str]
    sections: Final[Mapping[str, Mapping[str, str]]]
    def __init__(self, path: str, data: Optional[str] = None): ...
    def __contains__(self, arg: str) -> bool: ...
    def __getitem__(self, name: str) -> SectionWrapper: ...
    def __iter__(self) -> Iterator[SectionWrapper]: ...
    def get(
        self,
        section: str,
        name: str,
        default: _D = ...,
        convert: Callable[[str], _T] = ...,
    ) -> Union[_T, _D]: ...
    def lineof(self, section: str, name: Optional[str] = ...) -> Optional[int]: ...
