import json
import logging
import sys

import path

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)
from client_model import InputClient, PracticeSession
from client_schema import (INPUT_CLIENT_SCHEMA, OUTPUT_CLIENT_SCHEMA,
                           DBClientSchema)
from customer_encoder import CustomEncoder
from db import get_items_db, save_client_db

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def saveClient(my_client: InputClient) -> dict:
    try:
        logger.info("CREATING CLIENT")
        return save_client_db(my_client)
    except:
        logger.exception("Do cutom exception")


def getUserbyId(userId: str):
    try:
        logger.info("FINDING CLIENT [{userId}].")
        return get_items_db(userId)
    except:
        logger.exception("Do cutom exception")


def getSessionbyId(sessionId: str):
    try:
        return get_items_db(sessionId)
    except:
        logger.exception("Do cutom exception")
