"""
Modification Info
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class ModificationInfo:
    """Properties for recent modification history info for an entry"""

    created: datetime
    last_modified: datetime
    created_by: str = None
    last_modified_by: str = None
