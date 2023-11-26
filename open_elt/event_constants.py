"""
Event constant values
======================

"""
DEFAULT_RESPONSE_CONTENT_TYPE = "application/vnd.api+json"
FILTER_KEY = "filter"
LINKS_KEY = "links"
TENANT_ID_KEY = "tenant_id"
ITEM_TYPE_KEY = "item_type"
ITEM_ID_KEY = "item_id"
BATCH_QUERY_FOLDER = "batch-query"

TENANT_ID_TAG_NAME = "tenant_id"
FILE_STORE_ID_TAG_NAME = "file_store_id"

# EventBridge
DATA_KEY = "data"
DETAIL_KEY = "detail"
ID_KEY = "id"
DETAIL_TYPE_KEY = "detail-type"

TOPIC_TAG_KEY = "Key"
TOPIC_TAG_VALUE = "Value"
TOPIC_TAG_RESPONSE_KEY = "Tags"
TENANT_ID_TAG_NAME = "tenant_id"
FILE_STORE_ID_TAG_NAME = "file_store_id"

EVENT_SOURCE = "aws:s3"
PUT_EVENT_NAME = "ObjectCreated:Put"
COPY_EVENT_NAME = "ObjectCreated:Copy"
POST_EVENT_NAME = "ObjectCreated:Post"
MULTIPART_UPLOAD_EVENT_NAME = "ObjectCreated:CompleteMultipartUpload"
ACCEPTABLE_EVENT_NAMES = [
    PUT_EVENT_NAME,
    COPY_EVENT_NAME,
    POST_EVENT_NAME,
    MULTIPART_UPLOAD_EVENT_NAME,
]

# JSONRPC 2.0
JSONRPC_BAD_REQUEST = -32600
JSONRPC_BAD_METHOD = -32601
