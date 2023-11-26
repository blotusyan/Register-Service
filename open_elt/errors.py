"""
Global errors across Tag Service
===========================

"""
from http import HTTPStatus
from re import findall
from typing import Optional

from event_constants import JSONRPC_BAD_REQUEST


class ErrorBase(Exception):
    """Base Class For Service Errors"""

    http_code: HTTPStatus
    jsonrpc_request_id: int
    jsonrpc_status_code: int
    _code: str = None

    @property
    def code(self):
        """code returns class name by default but can be overridden"""
        if self._code:
            return self._code
        return self.__class__.__name__

    @code.setter
    def code(self, value):
        """setter to override code property"""
        self._code = value

    @property
    def title(self):
        """
        title uses the name of the base class unless the base class is ErrorBase,
        in which case it uses the name of the current class
        """
        base_class = self.__class__.__base__.__name__
        if base_class == "ErrorBase":
            code = self.code
        else:
            code = base_class
        return " ".join(findall("[A-Z][^A-Z]*", code))


class NotImplementedException(ErrorBase):
    """Exception indicating the feature for the resource is not implemented yet"""

    http_code = HTTPStatus.NOT_IMPLEMENTED

    def __init__(self, feature: str, resource: str) -> None:
        super().__init__(f"[{feature}] for [{resource}] has not been implemented yet")


class ResourceNotFound(ErrorBase):
    """Generic Not Found Error for Resources"""

    http_code = HTTPStatus.NOT_FOUND
    resource_type: str = ""

    def __init__(self, resource: Optional[str] = "UNKNOWN") -> None:
        super().__init__(f"{self.resource_type} [{resource}] Not Found")


class S3UploadFailedException(ErrorBase):
    """Exception indicating the S3 upload failed"""

    http_code = HTTPStatus.BAD_GATEWAY

    def __init__(self) -> None:
        super().__init__("Failed to upload data to S3 bucket")


class DatabaseException(ErrorBase):
    """Exception indicating a database error"""

    http_code = HTTPStatus.BAD_GATEWAY

    def __init__(self, message: Optional[str] = None) -> None:
        if not message:
            message = "An unspecified database error occurred"
        super().__init__(message)


class ClientBadRequest(ErrorBase):
    """
    Generic error for client's mistakes
    """

    http_code = HTTPStatus.BAD_REQUEST
    jsonrpc_status_code = JSONRPC_BAD_REQUEST


class TenantNotFound(ClientBadRequest):
    """
    Raised when tenant id is not found in the sns topic tag list
    """


class FileStoreIdNotFound(ClientBadRequest):
    """
    Raised when file store id is not found in the sns topic tag list
    """


class FileValidationError(ClientBadRequest):
    """
    Raised when provided files fail JSON Schema Validation
    """


class S3ObjectNotFoundError(ClientBadRequest):
    """
    Raised when content service unable fetch s3 object
    """
