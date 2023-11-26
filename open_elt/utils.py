import sys

import path

# directory reach
directory = path.Path(__file__).abspath()

# setting path
sys.path.append(directory.parent)
import json
import logging
from datetime import datetime
from json import JSONDecodeError
from typing import Dict

import boto3
from botocore.exceptions import ClientError
from customer_encoder import CustomEncoder
from errors import FileValidationError, S3ObjectNotFoundError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_date_time():
    date_time = datetime.now()
    time_id = date_time.strftime("%m%d%H%M")
    return time_id


def buildResponse(statusCode, body=None):
    response = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    }
    if body is not None:
        logger.info(json.dumps(body, cls=CustomEncoder))
        response["body"] = json.dumps(body, cls=CustomEncoder)
    return response


def get_json_data_from_s3(
    bucket: str, key: str, role_arn: str = None, external_id: str = None
) -> Dict:
    """
    Fetch data from s3 and read json data
    :param bucket: Bucket name
    :param key: File key
    :param role_arn: the role arn to access the data
    :param external_id: the external id to access the data
    :return: data dict
    """
    logger.info(f"Fetch data from bucket [{bucket}] on key [{key}]")

    data = get_s3_object(
        bucket=bucket, key=key, role_arn=role_arn, external_id=external_id
    )

    try:
        return json.loads(data)
    except JSONDecodeError as err:
        raise FileValidationError(
            f"Requested file [{key}] data unable to load as JSON"
        ) from err


def get_s3_object(
    bucket: str, key: str, role_arn: str = None, external_id: str = None
) -> bytes:
    """
    Fetch s3 object for a key from a bucket

    :param bucket: S3 bucket name
    :param key: S3 object key
    :param role_arn: the role arn to access the object
    :param external_id: the external id to access the object
    :return: The object as bytes
    """
    try:
        return (
            create_s3_client(role_arn=role_arn, external_id=external_id)
            .get_object(Bucket=bucket, Key=key)["Body"]
            .read()
        )
    except ClientError as err:
        if err.response["Error"]["Code"] == "NoSuchKey":
            raise S3ObjectNotFoundError(
                f"Unable to fetch s3 object for key [{key}] from bucket [{bucket}]"
            ) from err
        raise


def create_s3_client(role_arn: str = None, external_id: str = None):
    """
    create and cache s3 client
    :param role_arn: the role arn to assume
    :param external_id: the external id to assume the role
    :return: created s3 client
    """
    # if role_arn and external_id:
    #     return assume_role(role_arn=role_arn, external_id=external_id).create_boto_session().client("s3")
    return create_default_s3_client()


def create_default_s3_client():
    """
    Create and cache s3 client with default credentials
    :return: The created s3 client
    """
    return boto3.client("s3")
