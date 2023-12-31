from __future__ import annotations

import builtins
import contextlib
import os
import sys
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
from types import ModuleType, TracebackType
from typing import (
    IO,
    Any,
    AnyStr,
    BinaryIO,
    Callable,
    Generator,
    Iterable,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
    overload,
)

from _typeshed import (
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
    Self,
)
from typing_extensions import Literal

from . import classes

# Type for the match argument for several methods
_Match = Optional[Union[str, Callable[[str], bool], Callable[[Path], bool]]]

class TreeWalkWarning(Warning):
    pass

class Traversal:
    follow: Callable[[Path], bool]
    def __init__(self, follow: Callable[[Path], bool]): ...
    def __call__(
        self,
        walker: Generator[Path, Optional[Callable[[], bool]], None],
    ) -> Iterator[Path]: ...

class Path(str):
    module: Any
    def __init__(self, other: Any = ...) -> None: ...
    @classmethod
    def using_module(cls, module: ModuleType) -> Type[Path]: ...
    @classes.ClassProperty
    @classmethod
    def _next_class(cls: Type[Self]) -> Type[Self]: ...
    def __repr__(self) -> str: ...
    def __add__(self: Self, more: str) -> Self: ...
    def __radd__(self: Self, other: str) -> Self: ...
    def __div__(self: Self, rel: str) -> Self: ...
    def __truediv__(self: Self, rel: str) -> Self: ...
    def __rdiv__(self: Self, rel: str) -> Self: ...
    def __rtruediv__(self: Self, rel: str) -> Self: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...
    @classmethod
    def getcwd(cls: Type[Self]) -> Self: ...
    def abspath(self: Self) -> Self: ...
    def normcase(self: Self) -> Self: ...
    def normpath(self: Self) -> Self: ...
    def realpath(self: Self) -> Self: ...
    def expanduser(self: Self) -> Self: ...
    def expandvars(self: Self) -> Self: ...
    def dirname(self: Self) -> Self: ...
    def basename(self: Self) -> Self: ...
    def expand(self: Self) -> Self: ...
    @property
    def stem(self) -> str: ...
    @property
    def ext(self) -> str: ...
    def with_suffix(self: Self, suffix: str) -> Self: ...
    @property
    def drive(self: Self) -> Self: ...
    @property
    def parent(self: Self) -> Self: ...
    @property
    def name(self: Self) -> Self: ...
    def splitpath(self: Self) -> Tuple[Self, str]: ...
    def splitdrive(self: Self) -> Tuple[Self, Self]: ...
    def splitext(self: Self) -> Tuple[Self, str]: ...
    def stripext(self: Self) -> Self: ...
    @classes.multimethod
    def joinpath(cls: Self, first: str, *others: str) -> Self: ...
    def splitall(self: Self) -> List[Union[Self, str]]: ...
    def parts(self: Self) -> Tuple[Union[Self, str], ...]: ...
    def _parts(self: Self) -> Iterator[Union[Self, str]]: ...
    def _parts_iter(self: Self) -> Iterator[Union[Self, str]]: ...
    def relpath(self: Self, start: str = ...) -> Self: ...
    def relpathto(self: Self, dest: str) -> Self: ...
    # --- Listing, searching, walking, and matching
    def listdir(self: Self, match: _Match = ...) -> List[Self]: ...
    def dirs(self: Self, match: _Match = ...) -> List[Self]: ...
    def files(self: Self, match: _Match = ...) -> List[Self]: ...
    def walk(
        self: Self,
        match: _Match = ...,
        errors: str = ...,
    ) -> Generator[Self, Optional[Callable[[], bool]], None]: ...
    def walkdirs(
        self: Self,
        match: _Match = ...,
        errors: str = ...,
    ) -> Iterator[Self]: ...
    def walkfiles(
        self: Self,
        match: _Match = ...,
        errors: str = ...,
    ) -> Iterator[Self]: ...
    def fnmatch(
        self,
        pattern: Union[Path, str],
        normcase: Optional[Callable[[str], str]] = ...,
    ) -> bool: ...
    def glob(self: Self, pattern: str) -> List[Self]: ...
    def iglob(self: Self, pattern: str) -> Iterator[Self]: ...
    @overload
    def open(
        self,
        mode: OpenTextMode = ...,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Optional[Callable[[str, int], int]] = ...,
    ) -> TextIOWrapper: ...
    @overload
    def open(
        self,
        mode: OpenBinaryMode,
        buffering: Literal[0],
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Callable[[str, int], int] = ...,
    ) -> FileIO: ...
    @overload
    def open(
        self,
        mode: OpenBinaryModeUpdating,
        buffering: Literal[-1, 1] = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Callable[[str, int], int] = ...,
    ) -> BufferedRandom: ...
    @overload
    def open(
        self,
        mode: OpenBinaryModeReading,
        buffering: Literal[-1, 1] = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Callable[[str, int], int] = ...,
    ) -> BufferedReader: ...
    @overload
    def open(
        self,
        mode: OpenBinaryModeWriting,
        buffering: Literal[-1, 1] = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Callable[[str, int], int] = ...,
    ) -> BufferedWriter: ...
    @overload
    def open(
        self,
        mode: OpenBinaryMode,
        buffering: int,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Callable[[str, int], int] = ...,
    ) -> BinaryIO: ...
    @overload
    def open(
        self,
        mode: str,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Callable[[str, int], int] = ...,
    ) -> IO[Any]: ...
    def bytes(self) -> builtins.bytes: ...
    @overload
    def chunks(
        self,
        size: int,
        mode: OpenTextMode = ...,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Optional[Callable[[str, int], int]] = ...,
    ) -> Iterator[str]: ...
    @overload
    def chunks(
        self,
        size: int,
        mode: OpenBinaryMode,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Optional[Callable[[str, int], int]] = ...,
    ) -> Iterator[builtins.bytes]: ...
    @overload
    def chunks(
        self,
        size: int,
        mode: str,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        closefd: bool = ...,
        opener: Optional[Callable[[str, int], int]] = ...,
    ) -> Iterator[Union[str, builtins.bytes]]: ...
    def write_bytes(self, bytes: builtins.bytes, append: bool = ...) -> None: ...
    def read_text(
        self, encoding: Optional[str] = ..., errors: Optional[str] = ...
    ) -> str: ...
    def read_bytes(self) -> builtins.bytes: ...
    def text(self, encoding: Optional[str] = ..., errors: str = ...) -> str: ...
    @overload
    def write_text(
        self,
        text: str,
        encoding: Optional[str] = ...,
        errors: str = ...,
        linesep: Optional[str] = ...,
        append: bool = ...,
    ) -> None: ...
    @overload
    def write_text(
        self,
        text: builtins.bytes,
        encoding: None = ...,
        errors: str = ...,
        linesep: Optional[str] = ...,
        append: bool = ...,
    ) -> None: ...
    def lines(
        self,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        retain: bool = ...,
    ) -> List[str]: ...
    def write_lines(
        self,
        lines: List[str],
        encoding: Optional[str] = ...,
        errors: str = ...,
        linesep: Optional[str] = ...,
        append: bool = ...,
    ) -> None: ...
    def read_md5(self) -> builtins.bytes: ...
    def read_hash(self, hash_name: str) -> builtins.bytes: ...
    def read_hexhash(self, hash_name: str) -> str: ...
    def isabs(self) -> bool: ...
    def exists(self) -> bool: ...
    def isdir(self) -> bool: ...
    def isfile(self) -> bool: ...
    def islink(self) -> bool: ...
    def ismount(self) -> bool: ...
    def samefile(self, other: str) -> bool: ...
    def getatime(self) -> float: ...
    @property
    def atime(self) -> float: ...
    def getmtime(self) -> float: ...
    @property
    def mtime(self) -> float: ...
    def getctime(self) -> float: ...
    @property
    def ctime(self) -> float: ...
    def getsize(self) -> int: ...
    @property
    def size(self) -> int: ...
    def access(
        self,
        mode: int,
        *,
        dir_fd: Optional[int] = ...,
        effective_ids: bool = ...,
        follow_symlinks: bool = ...,
    ) -> bool: ...
    def stat(self) -> os.stat_result: ...
    def lstat(self) -> os.stat_result: ...
    def get_owner(self) -> str: ...
    @property
    def owner(self) -> str: ...
    if sys.platform != "win32":
        def statvfs(self) -> os.statvfs_result: ...
        def pathconf(self, name: Union[str, int]) -> int: ...

    def utime(
        self,
        times: Union[Tuple[int, int], Tuple[float, float], None] = ...,
        *,
        ns: Tuple[int, int] = ...,
        dir_fd: Optional[int] = ...,
        follow_symlinks: bool = ...,
    ) -> Path: ...
    def chmod(self: Self, mode: Union[str, int]) -> Self: ...
    if sys.platform != "win32":
        def chown(
            self: Self, uid: Union[int, str] = ..., gid: Union[int, str] = ...
        ) -> Self: ...

    def rename(self: Self, new: str) -> Self: ...
    def renames(self: Self, new: str) -> Self: ...
    def mkdir(self: Self, mode: int = ...) -> Self: ...
    def mkdir_p(self: Self, mode: int = ...) -> Self: ...
    def makedirs(self: Self, mode: int = ...) -> Self: ...
    def makedirs_p(self: Self, mode: int = ...) -> Self: ...
    def rmdir(self: Self) -> Self: ...
    def rmdir_p(self: Self) -> Self: ...
    def removedirs(self: Self) -> Self: ...
    def removedirs_p(self: Self) -> Self: ...
    def touch(self: Self) -> Self: ...
    def remove(self: Self) -> Self: ...
    def remove_p(self: Self) -> Self: ...
    def unlink(self: Self) -> Self: ...
    def unlink_p(self: Self) -> Self: ...
    def link(self: Self, newpath: str) -> Self: ...
    def symlink(self: Self, newlink: Optional[str] = ...) -> Self: ...
    def readlink(self: Self) -> Self: ...
    def readlinkabs(self: Self) -> Self: ...
    def copyfile(self, dst: str, *, follow_symlinks: bool = ...) -> str: ...
    def copymode(self, dst: str, *, follow_symlinks: bool = ...) -> None: ...
    def copystat(self, dst: str, *, follow_symlinks: bool = ...) -> None: ...
    def copy(self, dst: str, *, follow_symlinks: bool = ...) -> Any: ...
    def copy2(self, dst: str, *, follow_symlinks: bool = ...) -> Any: ...
    def copytree(
        self,
        dst: str,
        symlinks: bool = ...,
        ignore: Optional[Callable[[str, list[str]], Iterable[str]]] = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
        dirs_exist_ok: bool = ...,
    ) -> Any: ...
    def move(
        self, dst: str, copy_function: Callable[[str, str], None] = ...
    ) -> Any: ...
    def rmtree(
        self,
        ignore_errors: bool = ...,
        onerror: Optional[Callable[[Any, Any, Any], Any]] = ...,
    ) -> None: ...
    def rmtree_p(self: Self) -> Self: ...
    def chdir(self) -> None: ...
    def cd(self) -> None: ...
    def merge_tree(
        self,
        dst: str,
        symlinks: bool = ...,
        *,
        copy_function: Callable[[str, str], None] = ...,
        ignore: Callable[[Any, List[str]], Union[List[str], Set[str]]] = ...,
    ) -> None: ...
    if sys.platform != "win32":
        def chroot(self) -> None: ...
    if sys.platform == "win32":
        def startfile(self: Self, operation: Optional[str] = ...) -> Self: ...

    @contextlib.contextmanager
    def in_place(
        self,
        mode: str = ...,
        buffering: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        backup_extension: Optional[str] = ...,
    ) -> Iterator[Tuple[IO[Any], IO[Any]]]: ...
    @classes.ClassProperty
    @classmethod
    def special(cls) -> Callable[[Optional[str]], SpecialResolver]: ...

class DirectoryNotEmpty(OSError):
    @staticmethod
    def translate() -> Iterator[None]: ...

def only_newer(copy_func: Callable[[str, str], None]) -> Callable[[str, str], None]: ...

class ExtantPath(Path):
    def _validate(self) -> None: ...

class ExtantFile(Path):
    def _validate(self) -> None: ...

class SpecialResolver:
    class ResolverScope:
        def __init__(self, paths: SpecialResolver, scope: str) -> None: ...
        def __getattr__(self, class_: str) -> MultiPathType: ...

    def __init__(
        self,
        path_class: type,
        appname: Optional[str] = ...,
        appauthor: Optional[str] = ...,
        version: Optional[str] = ...,
        roaming: bool = ...,
        multipath: bool = ...,
    ): ...
    def __getattr__(self, scope: str) -> ResolverScope: ...
    def get_dir(self, scope: str, class_: str) -> MultiPathType: ...

class Multi:
    @classmethod
    def for_class(cls, path_cls: type) -> Type[MultiPathType]: ...
    @classmethod
    def detect(cls, input: str) -> MultiPathType: ...
    def __iter__(self) -> Iterator[Path]: ...
    @classes.ClassProperty
    @classmethod
    def _next_class(cls) -> Type[Path]: ...

class MultiPathType(Multi, Path):
    pass

class TempDir(Path):
    @classes.ClassProperty
    @classmethod
    def _next_class(cls) -> Type[Path]: ...
    def __new__(
        cls: Type[Self],
        suffix: Optional[AnyStr] = ...,
        prefix: Optional[AnyStr] = ...,
        dir: Optional[Union[AnyStr, os.PathLike[AnyStr]]] = ...,
    ) -> Self: ...
    def __init__(self) -> None: ...
    def __enter__(self) -> Path: ...  # type: ignore
    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

class Handlers:
    @classmethod
    def _resolve(
        cls, param: Union[str, Callable[[str], None]]
    ) -> Callable[[str], None]: ...
