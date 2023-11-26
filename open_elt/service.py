import json
import logging
import sys

import path

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)
from client_model import InputClient, PracticeSession
from client_schema import INPUT_CLIENT_SCHEMA, OUTPUT_CLIENT_SCHEMA, DBClientSchema
from customer_encoder import CustomEncoder
from db import get_items_db, save_client_db

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def saveClient(my_client: InputClient) -> dict:
    """
    Get input data ready before sending to DB layer
    :param my_client: the deserialized client object
    :return: Dict of response received after storing entry
    """
    try:
        logger.info("CREATING CLIENT")
        return save_client_db(my_client)
    except:
        logger.exception("Do cutom exception")


def getUserbyId(userId: str) -> dict:
    """
    Get ready for retrieving userId from DB layer
    :param userId: target id of the user
    :return: Dict of response received after retrieving entry
    """
    try:
        logger.info("FINDING CLIENT [{userId}].")
        return get_items_db(userId)
    except:
        logger.exception("Do cutom exception")


def getSessionbyId(sessionId: str) -> dict:
    """
    Get ready for retrieving sessionId from DB layer
    :param sessionId: target id of the session 
    :return: Dict of response received after retrieving entry
    """
    try:
        return get_items_db(sessionId)
    except:
        logger.exception("Do cutom exception")
