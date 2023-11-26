from open_elt.client_model import PracticeSession, InputClient
from freezegun import freeze_time
from test.test_data import (
    SAMPLE_ISO_TIMESTAMP,
    SAMPLE_USER_ID,
    good_input,
    good_output,
    input_with_problem_in_age,
    input_with_problem_in_gender,
    session_input,
    SAMPLE_TEST_FEEDBACK,
    SAMPLE_ISO_TIMESTAMP_OBJECT,
    DEFAULT_SESSION_ID,
    SAMPLE_SESSION_ID,
)


@freeze_time(SAMPLE_ISO_TIMESTAMP)
def test_InputClient_Object_Creation():
    my_client = InputClient(
        fname="Weiheng",
        lname="Yan",
        age=18,
        gender="Male",
        country="China",
        attempted=3,
        catagory="General",
        lastAttempted=6.5,
        target=7,
    )
    assert my_client.modificationInfo.created_by == SAMPLE_USER_ID
    assert my_client.modificationInfo.last_modified_by == SAMPLE_USER_ID


@freeze_time(SAMPLE_ISO_TIMESTAMP)
def test_PracticeSession_Object_Creation():
    my_session = PracticeSession(mark=7, feedback=SAMPLE_TEST_FEEDBACK)
    assert my_session.time == SAMPLE_ISO_TIMESTAMP_OBJECT


@freeze_time(SAMPLE_ISO_TIMESTAMP)
def test_PracticeSession_Set_SessionId():
    my_session = PracticeSession(mark=7, feedback=SAMPLE_TEST_FEEDBACK)
    assert my_session.sessionId == DEFAULT_SESSION_ID
    my_session.set_sessionId(user_id=SAMPLE_USER_ID)
    assert my_session.sessionId == SAMPLE_SESSION_ID


@freeze_time(SAMPLE_ISO_TIMESTAMP)
def test_PracticeSession_Set_UserId():
    my_session = PracticeSession(mark=7, feedback=SAMPLE_TEST_FEEDBACK)
    assert my_session.modificationInfo.created_by == None
    my_session.set_userId(user_id=SAMPLE_USER_ID)
    assert my_session.modificationInfo.created_by == SAMPLE_USER_ID
    assert my_session.modificationInfo.last_modified_by == SAMPLE_USER_ID
    assert my_session.modificationInfo.created == SAMPLE_ISO_TIMESTAMP_OBJECT
