import os
from os import environ, getenv

OPENAI_API_KEY = getenv("OPENAI_API_KEY", "NULL")

DYNAMODB_TABLE = getenv(
    "DYNAMODB_TABLE",
    "NULL",
)
