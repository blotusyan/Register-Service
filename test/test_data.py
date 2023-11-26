from datetime import datetime
from open_elt.utils import create_date_time
from freezegun import freeze_time

SAMPLE_USER_ID = "WYan2005"
SAMPLE_SESSION_ID = "WYan2005-20231124"
DEFAULT_SESSION_ID = "DEFAULT_SESSION_ID"
SAMPLE_ISO_TIMESTAMP = "2022-11-24T02:09:54"
SAMPLE_ISO_TIMESTAMP_OBJECT = datetime.strptime(
    SAMPLE_ISO_TIMESTAMP, "%Y-%m-%dT%H:%M:%S"
)
DEFAULT_SESSION_ID = "DEFAULT_SESSION_ID"


@freeze_time(SAMPLE_ISO_TIMESTAMP)
def create_frozen_time():
    return create_date_time()


SAMPLE_SESSION_ID = SAMPLE_USER_ID + "-session-" + create_frozen_time()

good_input = {
    "fname": "Weiheng",
    "lname": "Yan",
    "age": 18,
    "gender": "Male",
    "country": "China",
    "attempted": 5,
    "catagory": "General",
    "lastAttempted": 7.5,
    "target": 8.0,
}

input_with_problem_in_age = {
    "fname": "Weiheng",
    "lname": "Yan",
    "age": -5,
    "gender": "Male",
    "country": "China",
    "attempted": 5,
    "catagory": "General",
    "lastAttempted": 7.0,
    "target": 8.0,
}

input_with_problem_in_gender = {
    "fname": "Weiheng",
    "lname": "Yan",
    "age": -5,
    "gender": "Boy",
    "country": "China",
    "attempted": 5,
    "catagory": "General",
    "lastAttempted": 7,
    "target": 8.0,
}

good_output = {
    "fname": "Weiheng",
    "lname": "Yan",
    "age": 18,
    "gender": "Male",
    "country": "China",
    "attempted": 5,
    "catagory": "General",
    "lastAttempted": 7.5,
    "target": 8.0,
    "userId": SAMPLE_USER_ID,
}

session_input = {
    "modificationInfo": {
        "created": SAMPLE_ISO_TIMESTAMP,
        "createdBy": SAMPLE_USER_ID,
        "lastModified": SAMPLE_ISO_TIMESTAMP,
        "lastModifiedBy": SAMPLE_USER_ID,
    },
    "mark": 7,
    "feedback": "I like your speech",
    "time": SAMPLE_ISO_TIMESTAMP,
    "sessionId": DEFAULT_SESSION_ID,
}


SAMPLE_TEST_FEEDBACK = "You are perfect"
