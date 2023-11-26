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
logger.info("before importing")

from client_model import InputClient, PracticeSession
from client_schema import INPUT_CLIENT_SCHEMA
from service import getSessionbyId, getUserbyId, saveClient



ID_PATH = "id"
KEYWORD_PATH = "keyword"
# client table: pk: user_id sk-1: user_id
# session table: pk: user_id sk-1: session_id


def register_input_handler(event, context):
    logger.info(event["body"])  # string: string
    my_client: InputClient = INPUT_CLIENT_SCHEMA.loads(event["body"])
    return saveClient(my_client)


def retrieve_by_user_id_handler(event, context):
    user_id = event["requestContext"]["userId"]
    return getUserbyId(user_id)


def retrieve_by_session_id_handler(event, context):
    sessionId = event["requestContext"]["sessionId"]
    return getSessionbyId(sessionId)


# dict = {'resource': '/hello', 'path': '/hello', 'httpMethod': 'POST', 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-ASN': '577', 'CloudFront-Viewer-Country': 'CA', 'Content-Type': 'application/json', 'Host': 'imroou7if7.execute-api.us-east-1.amazonaws.com', 'Postman-Token': '496567a8-b809-4ef3-aac4-056dbb307440', 'User-Agent': 'PostmanRuntime/7.31.1', 'Via': '1.1 fe2c65104051140806cad998f531e478.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'GyuJE1-DuWpDsZmtRKfmeciC1zkLnjnFL2WY2hoa2AFItRRtwk7XJQ==', 'X-Amzn-Trace-Id': 'Root=1-6413e2c2-7c9349ae69452f89110552b5', 'X-Forwarded-For': '76.68.101.130, 130.176.130.75', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-ASN': ['577'], 'CloudFront-Viewer-Country': ['CA'], 'Content-Type': ['application/json'], 'Host': ['imroou7if7.execute-api.us-east-1.amazonaws.com'], 'Postman-Token': ['496567a8-b809-4ef3-aac4-056dbb307440'], 'User-Agent': ['PostmanRuntime/7.31.1'], 'Via': ['1.1 fe2c65104051140806cad998f531e478.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['GyuJE1-DuWpDsZmtRKfmeciC1zkLnjnFL2WY2hoa2AFItRRtwk7XJQ=='], 'X-Amzn-Trace-Id': ['Root=1-6413e2c2-7c9349ae69452f89110552b5'], 'X-Forwarded-For': ['76.68.101.130, 130.176.130.75'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'amt2ok', 'resourcePath': '/hello', 'httpMethod': 'POST', 'extendedRequestId': 'B6BecEa1oAMFS5A=', 'requestTime': '17/Mar/2023:03:47:14 +0000', 'path': '/Prod/hello', 'accountId': '544025597035', 'protocol': 'HTTP/1.1', 'stage': 'Prod', 'domainPrefix': 'imroou7if7', 'requestTimeEpoch': 1679024834589, 'requestId': '1b7c509c-1a07-4399-8c52-946e14cfe8cb', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '76.68.101.130', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'PostmanRuntime/7.31.1', 'user': None}, 'domainName': 'imroou7if7.execute-api.us-east-1.amazonaws.com', 'apiId': 'imroou7if7'}, 'body': '{\n    "question": "说1个张国荣成名曲"\n}', 'isBase64Encoded': False}
# print(dict["requestContext"]["accountId"])
