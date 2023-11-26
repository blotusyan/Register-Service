from typing import ClassVar, Generic, Iterable, Text, Type, Union

from typing_extensions import Final

class raw:
    uniobj: Final[Text]
    def __init__(self, uniobj: Text) -> None: ...

class _NamespaceMetaclass(type):
    def __getattr__(self, name: str) -> Type[Tag]: ...

class Namespace(metaclass=_NamespaceMetaclass): ...

class Tag(list):
    class Attr:
        def __getattr__(self, attr: str) -> Text: ...
    attr: Final[Attr]
    def __init__(
        self, *args: Union[Text, raw, Tag, Iterable[Tag]], **kwargs: Union[Text, raw]
    ) -> None: ...
    def unicode(self, indent: int = ...) -> Text: ...

class html(Namespace):
    class Style:
        def __init__(self, **kw: Union[str, Text]) -> None: ...
    style: ClassVar[Style]

def escape(ustring: Union[str, Text]) -> Text: ...
