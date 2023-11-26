import logging

import boto3
from boto3.dynamodb.conditions import Attr, Key
from client_model import InputClient, PracticeSession
from client_schema import DB_CLIENT_SCHEMA, INPUT_CLIENT_SCHEMA, OUTPUT_CLIENT_SCHEMA
from config import DYNAMODB_TABLE
from utils import buildResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamoDB = DYNAMODB_TABLE
client = boto3.resource("dynamodb")
table = client.Table(dynamoDB)


def save_client_db(my_client: InputClient) -> dict:
    """
    Save client info entry into DB
    :param my_client: the deserialized client object
    :return: Dict of response received after storing entry
    """
    my_pk = my_client.userId
    my_sk_1 = my_client.userId
    db_serialized_client = DB_CLIENT_SCHEMA.dump(my_client)
    output_serialized_client = OUTPUT_CLIENT_SCHEMA.dump(my_client)
    item = {
        "pk": my_pk,
        "sk-1": my_sk_1,
        "data": db_serialized_client,
    }
    table.put_item(Item=item)
    body = {"Operation": "Save", "Message": "Success", "Item": output_serialized_client}
    return buildResponse(200, body)


def get_items_db(hash_value, range_value=None) -> dict:
    """
    Get input data ready before sending to DB layer
    :param hash_value: hash_value as pk
    :param range_value: range_value as sk-1
    :return: Dict of response received after retrieving entry
    """
    hash_key = Key("pk")
    range_key = Key("sk-1")

    key_condition_expression = (
        hash_key.eq(hash_value)
        if not range_value
        else hash_key.eq(hash_value) & range_key.eq(hash_value)
    )
    kwargs = {"KeyConditionExpression": key_condition_expression}

    response = table.query(**kwargs)
    if response["Items"]:
        if range_value:
            return buildResponse(200, response["Items"][0])
        else:
            return buildResponse(200, response["Items"])
    else:
        return buildResponse(404, {"Message": "id: %s not found" % input})
