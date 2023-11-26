"""
Modification Info Schema
"""
from marshmallow import fields

from open_elt.helper_schema import CamelCaseSchema, SimpleTypeSchema
from open_elt.modification_info_model import ModificationInfo


class ModificationInfoSchema(SimpleTypeSchema, CamelCaseSchema):
    """Schema for ModificationInfo"""

    OBJ_CLS = ModificationInfo

    created = fields.DateTime(required=True, format="iso")
    last_modified = fields.DateTime(required=True, format="iso")
    created_by = fields.String(required=False, load_default=None)
    last_modified_by = fields.String(required=False, load_default=None)
