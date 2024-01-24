"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (search)
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import google.rpc.status_pb2
import iotics.api.common_pb2
import iotics.api.feed_pb2
import iotics.api.input_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ResponseType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ResponseTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResponseType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FULL: _ResponseType.ValueType  # 0
    LOCATED: _ResponseType.ValueType  # 1
    MINIMAL: _ResponseType.ValueType  # 2

class ResponseType(_ResponseType, metaclass=_ResponseTypeEnumTypeWrapper):
    """ResponseType describes the type of the search response.
    - FULL - Returns full responses including twins, feeds and inputs identifiers, properties and location
    - LOCATED - Returns located responses including twins identifier, location and label (for the provided language or default)
    - MINIMAL - Returns minimal responses including twins identifier only
    """

FULL: ResponseType.ValueType  # 0
LOCATED: ResponseType.ValueType  # 1
MINIMAL: ResponseType.ValueType  # 2
global___ResponseType = ResponseType

@typing_extensions.final
class SearchRequest(google.protobuf.message.Message):
    """SearchRequest describes a search request used for both synchronous and asynchronous search."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """Search request payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class Filter(google.protobuf.message.Message):
            """Search request filters, any of these can be used in combination or on their own."""

            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            TEXT_FIELD_NUMBER: builtins.int
            LOCATION_FIELD_NUMBER: builtins.int
            PROPERTIES_FIELD_NUMBER: builtins.int
            @property
            def text(self) -> google.protobuf.wrappers_pb2.StringValue:
                """Text filtering. One or more keywords which must match text from twin properties. Note that any (rather than all)
                of the keywords will produce a match.
                """
            @property
            def location(self) -> iotics.api.common_pb2.GeoCircle:
                """Location filtering: area within which twins must be located"""
            @property
            def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
                """Properties filtering: one or more exact properties, all of which twins must have."""
            def __init__(
                self,
                *,
                text: google.protobuf.wrappers_pb2.StringValue | None = ...,
                location: iotics.api.common_pb2.GeoCircle | None = ...,
                properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["location", b"location", "text", b"text"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "properties", b"properties", "text", b"text"]) -> None: ...

        RESPONSETYPE_FIELD_NUMBER: builtins.int
        EXPIRYTIMEOUT_FIELD_NUMBER: builtins.int
        FILTER_FIELD_NUMBER: builtins.int
        responseType: global___ResponseType.ValueType
        """Expected response type"""
        @property
        def expiryTimeout(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """UTC time (millis from epoch / unix time) when this search request has to be considered expired."""
        @property
        def filter(self) -> global___SearchRequest.Payload.Filter:
            """Search Request filters"""
        def __init__(
            self,
            *,
            responseType: global___ResponseType.ValueType = ...,
            expiryTimeout: google.protobuf.timestamp_pb2.Timestamp | None = ...,
            filter: global___SearchRequest.Payload.Filter | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["expiryTimeout", b"expiryTimeout", "filter", b"filter"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["expiryTimeout", b"expiryTimeout", "filter", b"filter", "responseType", b"responseType"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    LANG_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Search request headers"""
    scope: iotics.api.common_pb2.Scope.ValueType
    """Search request scope"""
    @property
    def lang(self) -> google.protobuf.wrappers_pb2.StringValue:
        """Search request language, applicable to text filtering. If not specified, text search will match any language."""
    @property
    def payload(self) -> global___SearchRequest.Payload:
        """Search request payload"""
    @property
    def range(self) -> iotics.api.common_pb2.Range:
        """Search request range"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        scope: iotics.api.common_pb2.Scope.ValueType = ...,
        lang: google.protobuf.wrappers_pb2.StringValue | None = ...,
        payload: global___SearchRequest.Payload | None = ...,
        range: iotics.api.common_pb2.Range | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "lang", b"lang", "payload", b"payload", "range", b"range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "lang", b"lang", "payload", b"payload", "range", b"range", "scope", b"scope"]) -> None: ...

global___SearchRequest = SearchRequest

@typing_extensions.final
class AdvancedSearchRequest(google.protobuf.message.Message):
    """AdvancedSearchRequest describes a search request with more filtering possibilities than SearchRequest. It returns
    formatted details about the twins matched by the supplied filter.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """Search request payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RESPONSETYPE_FIELD_NUMBER: builtins.int
        FILTER_FIELD_NUMBER: builtins.int
        responseType: global___ResponseType.ValueType
        """Expected response type"""
        filter: builtins.str
        """The search filter, expressed as a JSON-encoded AST (in JSONLogic style)"""
        def __init__(
            self,
            *,
            responseType: global___ResponseType.ValueType = ...,
            filter: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "responseType", b"responseType"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Search request headers"""
    scope: iotics.api.common_pb2.Scope.ValueType
    """Search request scope"""
    @property
    def payload(self) -> global___AdvancedSearchRequest.Payload:
        """Search request payload"""
    @property
    def range(self) -> iotics.api.common_pb2.Range:
        """Search request range"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        scope: iotics.api.common_pb2.Scope.ValueType = ...,
        payload: global___AdvancedSearchRequest.Payload | None = ...,
        range: iotics.api.common_pb2.Range | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload", "range", b"range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload", "range", b"range", "scope", b"scope"]) -> None: ...

global___AdvancedSearchRequest = AdvancedSearchRequest

@typing_extensions.final
class SearchResponse(google.protobuf.message.Message):
    """---------------------------------------------------------------------------------------------------------------------

    SearchResponse describes a result associated to a search request.
    It contains all the matching twins/feeds/inputs according to the request scope/range/lang/filters in the expected response type format.
    In the decentralised iotics operating environment, each node in the network generates a response and the client is expected to
    receive a stream of response messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class FeedDetails(google.protobuf.message.Message):
        """Search response feed details. Included with response type: FULL."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        STORELAST_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> iotics.api.feed_pb2.FeedID:
            """Feed"""
        storeLast: builtins.bool
        """whether offers the ability to store last received value"""
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Feed custom properties."""
        def __init__(
            self,
            *,
            feedId: iotics.api.feed_pb2.FeedID | None = ...,
            storeLast: builtins.bool = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId", "properties", b"properties", "storeLast", b"storeLast"]) -> None: ...

    @typing_extensions.final
    class InputDetails(google.protobuf.message.Message):
        """Search response input details. Included with response type: FULL."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        INPUTID_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def inputId(self) -> iotics.api.input_pb2.InputID:
            """Input"""
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Input custom properties."""
        def __init__(
            self,
            *,
            inputId: iotics.api.input_pb2.InputID | None = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["inputId", b"inputId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["inputId", b"inputId", "properties", b"properties"]) -> None: ...

    @typing_extensions.final
    class TwinDetails(google.protobuf.message.Message):
        """Search response twin details."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        LOCATION_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        FEEDS_FIELD_NUMBER: builtins.int
        INPUTS_FIELD_NUMBER: builtins.int
        UPDATEDAT_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Twin identifier. Included with response type: FULL, LOCATED and MINIMAL"""
        @property
        def location(self) -> iotics.api.common_pb2.GeoLocation:
            """Twin location (if set). Included with response type: FULL and LOCATED"""
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Twin custom properties."""
        @property
        def feeds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SearchResponse.FeedDetails]:
            """Feed details. Included with response type: FULL"""
        @property
        def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SearchResponse.InputDetails]:
            """Input details. Included with response type: FULL"""
        @property
        def updatedAt(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Twin updatedAt timestamp."""
        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
            location: iotics.api.common_pb2.GeoLocation | None = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
            feeds: collections.abc.Iterable[global___SearchResponse.FeedDetails] | None = ...,
            inputs: collections.abc.Iterable[global___SearchResponse.InputDetails] | None = ...,
            updatedAt: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["location", b"location", "twinId", b"twinId", "updatedAt", b"updatedAt"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feeds", b"feeds", "inputs", b"inputs", "location", b"location", "properties", b"properties", "twinId", b"twinId", "updatedAt", b"updatedAt"]) -> None: ...

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """Search Response Payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RESPONSETYPE_FIELD_NUMBER: builtins.int
        STATUS_FIELD_NUMBER: builtins.int
        HOSTID_FIELD_NUMBER: builtins.int
        TWINS_FIELD_NUMBER: builtins.int
        responseType: global___ResponseType.ValueType
        """Type of the response."""
        @property
        def status(self) -> google.rpc.status_pb2.Status:
            """Response status - if present indicates that this response is invalid"""
        hostId: builtins.str
        """Host identifier string representation"""
        @property
        def twins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SearchResponse.TwinDetails]:
            """Matching twins"""
        def __init__(
            self,
            *,
            responseType: global___ResponseType.ValueType = ...,
            status: google.rpc.status_pb2.Status | None = ...,
            hostId: builtins.str = ...,
            twins: collections.abc.Iterable[global___SearchResponse.TwinDetails] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["status", b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["hostId", b"hostId", "responseType", b"responseType", "status", b"status", "twins", b"twins"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers: ...
    @property
    def payload(self) -> global___SearchResponse.Payload:
        """Search response payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___SearchResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___SearchResponse = SearchResponse

@typing_extensions.final
class DispatchSearchResponse(google.protobuf.message.Message):
    """---------------------------------------------------------------------------------------------------------------------

    Dispatch Search Response message.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DispatchSearchResponse = DispatchSearchResponse
