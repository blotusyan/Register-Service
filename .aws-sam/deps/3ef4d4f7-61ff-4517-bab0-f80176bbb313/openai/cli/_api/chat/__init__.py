from __future__ import annotations

from argparse import ArgumentParser
from typing import TYPE_CHECKING

from . import completions

if TYPE_CHECKING:
    from argparse import _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    completions.register(subparser)
