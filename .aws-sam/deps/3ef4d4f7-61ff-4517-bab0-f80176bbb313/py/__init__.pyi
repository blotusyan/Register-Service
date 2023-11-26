from typing import Any

# py allows to use e.g. py.path.local even without importing py.path.
# So import implicitly.
from . import error, iniconfig, io, path, xml

__version__: str

# Untyped modules below here.
std: Any
test: Any
process: Any
apipkg: Any
code: Any
builtin: Any
log: Any
