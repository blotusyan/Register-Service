import unittest
from test.test_data import (
    SAMPLE_ISO_TIMESTAMP,
    SAMPLE_USER_ID,
    good_input,
    good_output,
    input_with_problem_in_age,
    input_with_problem_in_gender,
    session_input,
)

import pytest
from freezegun import freeze_time
from marshmallow import ValidationError

from open_elt.client_schema import (
    DB_CLIENT_SCHEMA,
    INPUT_CLIENT_SCHEMA,
    OUTPUT_CLIENT_SCHEMA,
    PRACTICE_SESSION_SCHEMA,
)


def test_input_client_schema_encode_decode():
    my_client = INPUT_CLIENT_SCHEMA.load(good_input)
    serialized = INPUT_CLIENT_SCHEMA.dump(my_client)
    assert good_input == serialized


def test_input_client_schema_raise_age_validation_error():
    with pytest.raises(ValidationError) as err:
        my_client = INPUT_CLIENT_SCHEMA.load(input_with_problem_in_age)
    assert "age" in err.value.args[0]


def test_input_client_schema_raise_gender_validation_error():
    with pytest.raises(ValidationError) as err:
        my_client = INPUT_CLIENT_SCHEMA.load(input_with_problem_in_gender)
    assert "gender" in err.value.args[0]


def test_output_client_schema_encode_decode():
    my_client = OUTPUT_CLIENT_SCHEMA.load(good_output)
    serialized = OUTPUT_CLIENT_SCHEMA.dump(my_client)
    assert good_output == serialized


def test_input_to_db_client_schema():
    my_client = INPUT_CLIENT_SCHEMA.load(good_input)
    serialized = DB_CLIENT_SCHEMA.dump(my_client)
    assert serialized["trialList"] == []


def test_input_to_output_client_schema():
    my_client = INPUT_CLIENT_SCHEMA.load(good_input)
    serialized = OUTPUT_CLIENT_SCHEMA.dump(my_client)
    assert serialized["userId"] == SAMPLE_USER_ID


@freeze_time(SAMPLE_ISO_TIMESTAMP)
def test_practice_session_schema_encode_decode():
    my_session = PRACTICE_SESSION_SCHEMA.load(session_input)
    my_session.set_userId(SAMPLE_USER_ID)
    serialized = PRACTICE_SESSION_SCHEMA.dump(my_session)
    assert session_input == serialized
