import marshmallow
from open_elt.helper_schema import CamelCaseSchema, SimpleTypeSchema
from marshmallow import Schema, fields, post_load, pre_dump, validate
from open_elt.modification_info_schema import ModificationInfoSchema

from open_elt.client_model import InputClient, PracticeSession


class InputClientSchema(SimpleTypeSchema, CamelCaseSchema):
    """Schema for InputMusic"""

    OBJ_CLS = InputClient

    fname = fields.String(
        required=True,
        validate=[validate.Length(0, 50)],
        metadata={
            "description": "first name",
            "example": "Weiheng",
        },
    )
    lname = fields.String(
        required=True,
        validate=[validate.Length(0, 50)],
        metadata={
            "description": "last name",
            "example": "Yan",
        },
    )
    age = fields.Integer(
        required=True,
        validate=validate.Range(min=0, max=120),
        metadata={
            "description": "age",
            "example": 18,
        },
    )
    gender = fields.String(
        required=True,
        validate=validate.OneOf(["Male", "Female"]),
        metadata={
            "description": "gender",
            "example": "Male",
        },
    )
    country = fields.String(
        required=True,
        validate=[validate.Length(0, 15)],
        metadata={
            "description": "country",
            "example": "China",
        },
    )
    attempted = fields.Integer(
        required=True,
        metadata={
            "description": "attempted",
            "example": "2",
        },
    )
    catagory = fields.String(
        required=True,
        validate=validate.OneOf(["General", "Academic"]),
        metadata={
            "description": "type",
            "example": "G",
        },
    )
    lastAttempted = fields.Float(
        validate=validate.Range(min=1, max=9),
        metadata={
            "description": "last score",
            "example": "6.5",
        },
    )
    target = fields.Float(
        validate=validate.Range(min=1, max=9),
        required=True,
        metadata={
            "description": "target score",
            "example": "7.5",
        },
    )


class OutputClientSchema(InputClientSchema):
    OBJ_CLS = InputClient

    userId = fields.String(
        required=True,
        validate=[validate.Length(1, 64)],
        metadata={"description": "unique id of the client", "example": "syan0729"},
    )


class PracticeSessionSchema(SimpleTypeSchema, CamelCaseSchema):
    OBJ_CLS = PracticeSession

    modificationInfo = fields.Nested(
        ModificationInfoSchema,
        required=True,
        metadata={"description": "modification info of a music object"},
    )
    mark = fields.Integer(
        required=True,
        validate=validate.Range(min=0, max=9),
        metadata={
            "description": "mark",
            "example": "6.5",
        },
    )
    feedback = fields.String(
        required=True,
        validate=[validate.Length(1, 200)],
        metadata={"description": "unique id of the client", "example": "syan0729"},
    )
    # archive = fields.List(
    #     fields.Dict(
    #         load_default=[], metadata={"description": "a list of Music item dict"}
    #     )
    # )
    time = fields.DateTime(required=True, format="iso")
    sessionId = fields.String(
        required=True,
        validate=[validate.Length(1, 20)],
        metadata={"description": "unique id of the client", "example": "syan0729"},
    )


class DBClientSchema(OutputClientSchema):
    OBJ_CLS = InputClient

    modificationInfo = fields.Nested(
        ModificationInfoSchema,
        required=True,
        metadata={"description": "modification info of a music object"},
    )
    trialList = fields.List(
        fields.Nested(
            PracticeSessionSchema,
            required=True,
            metadata={"description": "list of previous attempts"},
        )
    )


INPUT_CLIENT_SCHEMA = InputClientSchema()
OUTPUT_CLIENT_SCHEMA = OutputClientSchema()
DB_CLIENT_SCHEMA = DBClientSchema()
PRACTICE_SESSION_SCHEMA = PracticeSessionSchema()
