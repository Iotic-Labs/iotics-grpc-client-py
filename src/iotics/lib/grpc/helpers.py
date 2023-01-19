# Copyright © 2022 IOTIC LABS LTD. info@iotics.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/Iotic-Labs/iotics-grpc-client-py/blob/main/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime
import uuid

import grpc
from google.protobuf.timestamp_pb2 import Timestamp

from iotics.api.common_pb2 import GeoLocation, Headers, LangLiteral, Literal, Property, StringLiteral, Uri, Value
from iotics.api.feed_pb2 import UpsertFeedWithMeta
from iotics.lib.grpc.auth import AuthInterface
from iotics.api.input_pb2 import UpsertInputWithMeta


def get_channel(auth: AuthInterface) -> grpc.Channel:
    """Creates a gRPC channel to IOTICSpace and instantiates API stub.

    Args:
        auth: Required to get a space host name and authentication token.

    Returns: gRPC channel.
    """
    # note: for testing against a local server without ssl
    # you can use 'grpc.local_channel_credentials()' here instead
    channel_credentials = grpc.ssl_channel_credentials()
    call_credentials = grpc.access_token_call_credentials(auth.get_token())
    composite_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
    return grpc.secure_channel(auth.get_host(), composite_credentials)


def create_property(key, value, language=None, datatype=None, is_uri=False):
    value = _create_property_value(value, language, datatype, is_uri)
    if isinstance(value, Uri):
        return Property(key=key, uriValue=value)
    if isinstance(value, Literal):
        return Property(key=key, literalValue=value)
    if isinstance(value, StringLiteral):
        return Property(key=key, stringLiteralValue=value)
    if isinstance(value, LangLiteral):
        return Property(key=key, langLiteralValue=value)


def _create_property_value(value, language=None, datatype=None, is_uri=False):
    if is_uri:
        return Uri(value=value)
    if language:
        return LangLiteral(value=value, lang=language)
    if datatype:
        return Literal(value=value, dataType=datatype)
    return StringLiteral(value=value)


def create_location(lat, lon):
    return GeoLocation(lat=lat, lon=lon)


def create_feed_with_meta(feed_id, store_last=True, values=None, properties=None):
    return UpsertFeedWithMeta(
        id=feed_id,
        storeLast=store_last,
        values=values,
        properties=properties
    )


def create_input_with_meta(input_id, values=None, properties=None):
    return UpsertInputWithMeta(
        id=input_id,
        values=values,
        properties=properties
    )


def create_value(label, comment=None, unit=None, data_type=None):
    return Value(label=label, comment=comment, unit=unit, dataType=data_type)


def create_headers(client_ref=None, client_app_id=None, transaction_ref=None, consumer_group=None,
                   request_timeout=None):
    client_app_id = client_app_id or uuid.uuid4().hex
    return Headers(
        clientRef=client_ref or 'IOTICS GRPC Python client',
        clientAppId=client_app_id,
        transactionRef=transaction_ref or [client_app_id],
        consumerGroup=consumer_group,
        requestTimeout=request_timeout
    )


def create_timestamp() -> Timestamp:
    """Create a Google protobuf timestamp with current time in UTC."""
    timestamp = Timestamp()
    timestamp.FromDatetime(datetime.datetime.now(datetime.timezone.utc))
    return timestamp


PROPERTY_IS_DIGITAL_TWIN = Property(
    key='http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
    uriValue=Uri(value='http://data.iotics.com/iotics#DigitalTwin')
)
PROPERTY_IS_MODEL = Property(
    key='http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
    uriValue=Uri(value='https://data.iotics.com/app#Model')
)
PROPERTY_CREATED_BY_MODEL = Property(
    key='http://data.iotics.com/app#CreationMeans',
    uriValue=Uri(value='http://data.iotics.com/app#ByModel')
)
PROPERTY_ALLOW_ALL = Property(
    key='http://data.iotics.com/public#hostAllowList',
    uriValue=Uri(value='http://data.iotics.com/public#all')
)
PROPERTY_ALLOW_NONE = Property(
    key='http://data.iotics.com/public#hostAllowList',
    uriValue=Uri(value='http://data.iotics.com/public#none')
)
PROPERTY_KEY_HAS_MODEL = 'https://data.iotics.com/app#model'
PROPERTY_KEY_COLOR = 'https://data.iotics.com/app#color'
PROPERTY_KEY_CREATED_AT = 'https://data.iotics.com/app#createdAt'
PROPERTY_KEY_CREATED_BY = 'https://data.iotics.com/app#createdBy'
PROPERTY_KEY_UPDATED_AT = 'https://data.iotics.com/app#updatedAt'
PROPERTY_KEY_UPDATED_BY = 'https://data.iotics.com/app#updatedBy'
PROPERTY_KEY_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"
PROPERTY_KEY_COMMENT = "http://www.w3.org/2000/01/rdf-schema#comment"
