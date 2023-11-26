import os
from os import environ, getenv

OPENAI_API_KEY = "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"

DYNAMODB_TABLE = getenv(
    "DYNAMODB_TABLE",
    "open-IELTS-syan-DynamoDB-1TS2W4W0CKBH5-OpenIELTSTable-9AA7HVQRRA6U",
)
