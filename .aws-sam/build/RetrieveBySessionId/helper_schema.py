import marshmallow
from marshmallow import Schema, fields, post_load, pre_dump, validate


def camelcase(snake_case_string) -> str:
    """
    Convert snake_case to camelCase
    """
    parts = iter(snake_case_string.split("_"))
    # ARN word in the s3 event is uppercase
    return next(parts) + "".join(i.title() if i != "arn" else i.upper() for i in parts)


class CamelCaseSchema(Schema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)


class SimpleTypeSchema(Schema):
    """
    The class simplifies creating schema that upon load convert data into object defined by OBJ_CLS class.
    It registered post_load hook. The class does not support more complex scenarios, since the order of calling
    to hook is not defined
    """

    # pylint: disable= no-member, unused-argument
    @post_load
    def make_object(self, data, many=False, **_):
        """
        The function converts deserialized dictionary into object.
        :param data: dictionary representation of the parsed data
        :param many:
        :param _:
        :return: new object of type OBJ_CLS
        """
        return self.OBJ_CLS(**data)


def pascalcase(pascal_case_string: str):
    """
    Convert a string from snake_case to PascalCase
    """
    parts = iter(pascal_case_string.split("_"))
    # URL word in the s3 event is uppercase
    return "".join(i.title() if i != "url" else i.upper() for i in parts)


class PascalCaseSchema(Schema):
    """
    Schema that uses pascal-case for its external representation
    and snake-case for its internal representation.
    """

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = pascalcase(field_obj.data_key or field_name)
