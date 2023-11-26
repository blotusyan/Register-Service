# PYTHON_ARGCOMPLETE_OK
"""
pytest: unit and functional testing with Python.
"""
from _pytest import __version__
from _pytest.assertion import register_assert_rewrite
from _pytest.config import UsageError, cmdline, hookimpl, hookspec, main
from _pytest.debugging import pytestPDB as __pytestPDB
from _pytest.fixtures import fillfixtures as _fillfuncargs
from _pytest.fixtures import fixture, yield_fixture
from _pytest.freeze_support import freeze_includes
from _pytest.main import ExitCode, Session
from _pytest.mark import MARK_GEN as mark
from _pytest.mark import param
from _pytest.nodes import Collector, File, Item
from _pytest.outcomes import exit, fail, importorskip, skip, xfail
from _pytest.python import Class, Function, Instance, Module, Package
from _pytest.python_api import approx, raises
from _pytest.recwarn import deprecated_call, warns
from _pytest.warning_types import (
    PytestAssertRewriteWarning,
    PytestCacheWarning,
    PytestCollectionWarning,
    PytestConfigWarning,
    PytestDeprecationWarning,
    PytestExperimentalApiWarning,
    PytestUnhandledCoroutineWarning,
    PytestUnknownMarkWarning,
    PytestWarning,
)

set_trace = __pytestPDB.set_trace

__all__ = [
    "__version__",
    "_fillfuncargs",
    "approx",
    "Class",
    "cmdline",
    "Collector",
    "deprecated_call",
    "exit",
    "ExitCode",
    "fail",
    "File",
    "fixture",
    "freeze_includes",
    "Function",
    "hookimpl",
    "hookspec",
    "importorskip",
    "Instance",
    "Item",
    "main",
    "mark",
    "Module",
    "Package",
    "param",
    "PytestAssertRewriteWarning",
    "PytestCacheWarning",
    "PytestCollectionWarning",
    "PytestConfigWarning",
    "PytestDeprecationWarning",
    "PytestExperimentalApiWarning",
    "PytestUnhandledCoroutineWarning",
    "PytestUnknownMarkWarning",
    "PytestWarning",
    "raises",
    "register_assert_rewrite",
    "Session",
    "set_trace",
    "skip",
    "UsageError",
    "warns",
    "xfail",
    "yield_fixture",
]

if __name__ == "__main__":
    # if run as a script or by 'python -m pytest'
    # we trigger the below "else" condition by the following import
    import pytest

    raise SystemExit(pytest.main())
else:
    from _pytest.compat import _setup_collect_fakemodule

    _setup_collect_fakemodule()
