import json
import logging
import random
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import path  # change dir hierachy

from open_elt.modification_info_model import ModificationInfo

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)
from open_elt.utils import create_date_time

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@dataclass
class PracticeSession:
    """Properties for PracticeSession"""

    mark: int
    feedback: str
    # archive: list(dict) = []
    modificationInfo: ModificationInfo
    time: datetime
    sessionId: str = "DEFAULT_SESSION_ID"

    def __init__(self, mark, feedback, **kwargs):
        self.mark = mark
        self.feedback = feedback
        self.modificationInfo = ModificationInfo(
            created=datetime.now(), last_modified=datetime.now()
        )
        self.time = datetime.now()

    def set_sessionId(self, user_id: str, **kwargs):
        self.sessionId = user_id + "-session-" + create_date_time()

    def set_userId(self, user_id: str, **kwargs) -> None:
        self.modificationInfo.created_by = user_id
        self.modificationInfo.last_modified_by = user_id


@dataclass
class InputClient:
    """Properties for Client"""

    fname: str
    lname: str
    age: int
    gender: str
    country: str
    attempted: int
    catagory: str
    lastAttempted: float
    target: float
    modificationInfo: ModificationInfo
    userId: str
    trialList: list[PracticeSession]

    def __init__(self, **kwargs):
        logger.info("kwargs are: \n")
        logger.info(kwargs)
        self.fname = kwargs.get("fname")
        self.lname = kwargs.get("lname")
        self.age = kwargs.get("age")
        self.gender = kwargs.get("gender")  # need to consider LGBTQ+
        self.country = kwargs.get("country")
        self.attempted = kwargs.get(
            "attempted"
        )  # can check if it is a int or string in kwargs
        self.catagory = kwargs.get("catagory")
        self.lastAttempted = kwargs.get("lastAttempted")
        self.target = kwargs.get("target")
        self.userId = self.fname[0] + self.lname + str(2023 - self.age)
        self.modificationInfo = ModificationInfo(
            created=datetime.now(),
            last_modified=datetime.now(),
            created_by=self.userId,
            last_modified_by=self.userId,
        )
        self.trialList = []

    def add_session(self, session: PracticeSession, **kwargs):
        self.trialList.append(session)
        logger.info("add new session to user [{self.userId}]")
