from __future__ import annotations

from argparse import ArgumentParser
from typing import TYPE_CHECKING

from . import fine_tunes, migrate

if TYPE_CHECKING:
    from argparse import _SubParsersAction


def register_commands(
    parser: ArgumentParser, subparser: _SubParsersAction[ArgumentParser]
) -> None:
    migrate.register(subparser)

    namespaced = parser.add_subparsers(
        title="Tools", help="Convenience client side tools"
    )

    fine_tunes.register(namespaced)
