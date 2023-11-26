import json
import logging
import sys

import path

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent.parent)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from client_model import InputClient, PracticeSession
from client_schema import INPUT_CLIENT_SCHEMA
from service import getSessionbyId, getUserbyId, saveClient

ID_PATH = "id"
KEYWORD_PATH = "keyword"
# client table: pk: user_id sk-1: user_id
# session table: pk: user_id sk-1: session_id


def register_input_handler(event, context) -> dict:
    """
    Handle Gateway POST request
    :param event: the event body received
    :return: Dict of response received after storing entry
    """
    logger.info(event["body"])  # string: string
    my_client: InputClient = INPUT_CLIENT_SCHEMA.loads(event["body"])
    return saveClient(my_client)


def retrieve_by_user_id_handler(event, context) -> dict:
    """
    Handle Gateway GET request based on user_id
    :param event: the event body received
    :return: Dict of response received after retrieving entry
    """
    user_id = event["requestContext"]["userId"]
    return getUserbyId(user_id)


def retrieve_by_session_id_handler(event, context) -> dict:
    """
    Handle Gateway GET request based on session_id
    :param event: the event body received
    :return: Dict of response received after retrieving entry
    """
    sessionId = event["requestContext"]["sessionId"]
    return getSessionbyId(sessionId)
