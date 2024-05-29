"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (common)
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Scope:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ScopeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Scope.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    GLOBAL: _Scope.ValueType  # 0
    LOCAL: _Scope.ValueType  # 1

class Scope(_Scope, metaclass=_ScopeEnumTypeWrapper):
    """Scope is a request parameter used to apply a scope to a given request.
    GLOBAL - go over the network/target the public Twin
    LOCAL - restrain the request to the local host
    """

GLOBAL: Scope.ValueType  # 0
LOCAL: Scope.ValueType  # 1
global___Scope = Scope

@typing.final
class Limit(google.protobuf.message.Message):
    """---------------------------------------------------------------------------------------------------------------------

    Limit is a request parameter to limit the number of results.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    """Max number of results (under configuration max limit constraint)"""
    def __init__(
        self,
        *,
        value: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___Limit = Limit

@typing.final
class Offset(google.protobuf.message.Message):
    """Offset is a request parameter applicable in conjunction with the "Limit"
    request parameter to start returning results from the given offset.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    """Result number to start from"""
    def __init__(
        self,
        *,
        value: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___Offset = Offset

@typing.final
class Range(google.protobuf.message.Message):
    """Range is the combination of the "Limit" and "Offset" is a request parameters. It is
    used to return a specific range of results. Default value is applied if no limit is specified.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    @property
    def limit(self) -> global___Limit: ...
    @property
    def offset(self) -> global___Offset: ...
    def __init__(
        self,
        *,
        limit: global___Limit | None = ...,
        offset: global___Offset | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["limit", b"limit", "offset", b"offset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["limit", b"limit", "offset", b"offset"]) -> None: ...

global___Range = Range

@typing.final
class LangLiteral(google.protobuf.message.Message):
    """LangLiteral is a metadata property type describing a string with a given language (implicit datatype: rdf:langString)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LANG_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    lang: builtins.str
    """2-character language code"""
    value: builtins.str
    """String representation of the value"""
    def __init__(
        self,
        *,
        lang: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lang", b"lang", "value", b"value"]) -> None: ...

global___LangLiteral = LangLiteral

@typing.final
class StringLiteral(google.protobuf.message.Message):
    """StringLiteral is a metadata property type describing a string without a language (implicit datatype: rdf:string)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.str
    """String representation of the value"""
    def __init__(
        self,
        *,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___StringLiteral = StringLiteral

@typing.final
class Literal(google.protobuf.message.Message):
    """Literal is a metadata property type describing a literal with the given datatype (implicit datatype: rdfs:Literal)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATATYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    dataType: builtins.str
    """XSD data type (e.g. double) without its namespace prefix (http://www.w3.org/2001/XMLSchema#). The following types
    are currently supported:
    dateTime, time, date, boolean, integer, decimal, float, double, nonPositiveInteger, negativeInteger,
    nonNegativeInteger, positiveInteger, long, unsignedLong, int, unsignedInt, short, unsignedShort, byte,
    unsignedByte, base64Binary, anyURI
    """
    value: builtins.str
    """String representation of the value according to XSD datatype specification"""
    def __init__(
        self,
        *,
        dataType: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dataType", b"dataType", "value", b"value"]) -> None: ...

global___Literal = Literal

@typing.final
class Uri(google.protobuf.message.Message):
    """Uri is a metadata property type describing a Uri."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.str
    """String representation of the value"""
    def __init__(
        self,
        *,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___Uri = Uri

@typing.final
class Property(google.protobuf.message.Message):
    """Property is a metadata property with a single value.
    Multiple instances are used to represent a key (predicate) with multiple values.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    LITERALVALUE_FIELD_NUMBER: builtins.int
    LANGLITERALVALUE_FIELD_NUMBER: builtins.int
    STRINGLITERALVALUE_FIELD_NUMBER: builtins.int
    URIVALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    """The key (predicate) of the property"""
    @property
    def literalValue(self) -> global___Literal: ...
    @property
    def langLiteralValue(self) -> global___LangLiteral: ...
    @property
    def stringLiteralValue(self) -> global___StringLiteral: ...
    @property
    def uriValue(self) -> global___Uri: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        literalValue: global___Literal | None = ...,
        langLiteralValue: global___LangLiteral | None = ...,
        stringLiteralValue: global___StringLiteral | None = ...,
        uriValue: global___Uri | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["langLiteralValue", b"langLiteralValue", "literalValue", b"literalValue", "stringLiteralValue", b"stringLiteralValue", "uriValue", b"uriValue", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "langLiteralValue", b"langLiteralValue", "literalValue", b"literalValue", "stringLiteralValue", b"stringLiteralValue", "uriValue", b"uriValue", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["value", b"value"]) -> typing.Literal["literalValue", "langLiteralValue", "stringLiteralValue", "uriValue"] | None: ...

global___Property = Property

@typing.final
class GeoLocation(google.protobuf.message.Message):
    """GeoLocation is the geographic location of a Twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAT_FIELD_NUMBER: builtins.int
    LON_FIELD_NUMBER: builtins.int
    lat: builtins.float
    """Latitude"""
    lon: builtins.float
    """Longitude"""
    def __init__(
        self,
        *,
        lat: builtins.float = ...,
        lon: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lat", b"lat", "lon", b"lon"]) -> None: ...

global___GeoLocation = GeoLocation

@typing.final
class GeoCircle(google.protobuf.message.Message):
    """GeoCircle is an approximate geographic location."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_FIELD_NUMBER: builtins.int
    RADIUSKM_FIELD_NUMBER: builtins.int
    radiusKm: builtins.float
    """Radius (Km) relative to the geolocation"""
    @property
    def location(self) -> global___GeoLocation: ...
    def __init__(
        self,
        *,
        location: global___GeoLocation | None = ...,
        radiusKm: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["location", b"location"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["location", b"location", "radiusKm", b"radiusKm"]) -> None: ...

global___GeoCircle = GeoCircle

@typing.final
class RequestInfo(google.protobuf.message.Message):
    """RequestInfo is a request parameter used to provide additional information about the request.
    It will also be included in the response.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TraceCtxEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    STARTTIME_FIELD_NUMBER: builtins.int
    TRACECTX_FIELD_NUMBER: builtins.int
    @property
    def startTime(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start timestamp of the request, from the perspective of the host (server). Values supplied by the client will be
        ignored
        """

    @property
    def traceCtx(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Headers for tracing support (W3C Trace Context / Baggage). If no valid context is provided by the client, the host
        (server) will initialise one.
        """

    def __init__(
        self,
        *,
        startTime: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        traceCtx: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["startTime", b"startTime"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["startTime", b"startTime", "traceCtx", b"traceCtx"]) -> None: ...

global___RequestInfo = RequestInfo

@typing.final
class Headers(google.protobuf.message.Message):
    """Headers describes the common headers applicable to all the API requests
    (except for Search subscribe: see SubscriptionHeaders).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENTREF_FIELD_NUMBER: builtins.int
    CLIENTAPPID_FIELD_NUMBER: builtins.int
    TRANSACTIONREF_FIELD_NUMBER: builtins.int
    CONSUMERGROUP_FIELD_NUMBER: builtins.int
    REQUESTTIMEOUT_FIELD_NUMBER: builtins.int
    REQUESTINFO_FIELD_NUMBER: builtins.int
    clientRef: builtins.str
    """Optional client reference. Any responses associated with the request will include this reference."""
    clientAppId: builtins.str
    """User namespace used to group all the requests/responses"""
    @property
    def transactionRef(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Used to loosely link requests/responses in a distributed environment
        each layer can add its own id to the list. Transaction ref is limited to
        a max of 16 elements per list and, for each list item, a max length of 36
        characters
        """

    @property
    def consumerGroup(self) -> google.protobuf.wrappers_pb2.StringValue:
        """Used for group listener, optional - Not implemented yet"""

    @property
    def requestTimeout(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Client request timeout used to stop the request processing once the timeout is reached"""

    @property
    def requestInfo(self) -> global___RequestInfo: ...
    def __init__(
        self,
        *,
        clientRef: builtins.str = ...,
        clientAppId: builtins.str = ...,
        transactionRef: collections.abc.Iterable[builtins.str] | None = ...,
        consumerGroup: google.protobuf.wrappers_pb2.StringValue | None = ...,
        requestTimeout: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        requestInfo: global___RequestInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["consumerGroup", b"consumerGroup", "requestInfo", b"requestInfo", "requestTimeout", b"requestTimeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["clientAppId", b"clientAppId", "clientRef", b"clientRef", "consumerGroup", b"consumerGroup", "requestInfo", b"requestInfo", "requestTimeout", b"requestTimeout", "transactionRef", b"transactionRef"]) -> None: ...

global___Headers = Headers

@typing.final
class SubscriptionHeaders(google.protobuf.message.Message):
    """SubscriptionHeaders describes a Search subscribe header. (Will be DEPRECATED with the client-ref from Headers)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENTAPPID_FIELD_NUMBER: builtins.int
    TRANSACTIONREF_FIELD_NUMBER: builtins.int
    CONSUMERGROUP_FIELD_NUMBER: builtins.int
    clientAppId: builtins.str
    """User namespace used to group all the requests/responses"""
    @property
    def transactionRef(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Used to loosely link requests/responses in a distributed environment
        each layer can add its own id to the list. Transaction ref is limited to
        a max of 16 elements per list and, for each list item, a max length of 36
        characters
        """

    @property
    def consumerGroup(self) -> google.protobuf.wrappers_pb2.StringValue:
        """consumer group (for group listener, optional) - Not implemented yet"""

    def __init__(
        self,
        *,
        clientAppId: builtins.str = ...,
        transactionRef: collections.abc.Iterable[builtins.str] | None = ...,
        consumerGroup: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["consumerGroup", b"consumerGroup"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["clientAppId", b"clientAppId", "consumerGroup", b"consumerGroup", "transactionRef", b"transactionRef"]) -> None: ...

global___SubscriptionHeaders = SubscriptionHeaders

@typing.final
class TwinID(google.protobuf.message.Message):
    """TwinID is the virtual representation of a (physical, purely virtual or hybrid) device,
    is only ever located in the host it was created.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    HOSTID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Twin Identifier (using DID format)"""
    hostId: builtins.str
    """Host Identifier (using DID format)"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        hostId: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["hostId", b"hostId", "id", b"id"]) -> None: ...

global___TwinID = TwinID

@typing.final
class Value(google.protobuf.message.Message):
    """Value is the definition of an individual piece of data within a Feed share or an Input send. Values are purely descriptive, e.g. a
    follower should expect data to match the values associated with said Feed/Input but must be able to recover where this
    is not the case.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LABEL_FIELD_NUMBER: builtins.int
    COMMENT_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    DATATYPE_FIELD_NUMBER: builtins.int
    label: builtins.str
    """label is the unique identifier of the value. It is language-neutral. E.g.: "t" / "temp" / "temperature"."""
    comment: builtins.str
    """comment is the (optional) human-readable description of the value. It is language-specific. E.g.: "Engine oil temperature" """
    unit: builtins.str
    """unit is the (optional) fully qualified ontology string URI of the unit, e.g. http://purl.obolibrary.org/obo/UO_0000027"""
    dataType: builtins.str
    """dataType is the xsd type in shorthand notation.
    Currently supported types are: base64Binary, decimal, float, double, dateTime, time, date, boolean, integer,
    nonPositiveInteger, negativeInteger, nonNegativeInteger, positiveInteger, long, unsignedLong, int, unsignedInt,
    short, unsignedShort, byte, unsignedByte
    """
    def __init__(
        self,
        *,
        label: builtins.str = ...,
        comment: builtins.str = ...,
        unit: builtins.str = ...,
        dataType: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["comment", b"comment", "dataType", b"dataType", "label", b"label", "unit", b"unit"]) -> None: ...

global___Value = Value

@typing.final
class Values(google.protobuf.message.Message):
    """Values defines a set of values to be added and/or deleted."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDED_FIELD_NUMBER: builtins.int
    DELETEDBYLABEL_FIELD_NUMBER: builtins.int
    @property
    def added(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Value]:
        """added is the list of values to be added. Note that deletedByLabel takes precedence over this, i.e. if both added
        and deletedByLabel contain the same value, the value will be deleted.
        """

    @property
    def deletedByLabel(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """deletedByLabel is the list of labels of values to be deleted."""

    def __init__(
        self,
        *,
        added: collections.abc.Iterable[global___Value] | None = ...,
        deletedByLabel: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["added", b"added", "deletedByLabel", b"deletedByLabel"]) -> None: ...

global___Values = Values

@typing.final
class FeedData(google.protobuf.message.Message):
    """FeedData is set of datapoints shared via a Feed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OCCURREDAT_FIELD_NUMBER: builtins.int
    MIME_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    mime: builtins.str
    """mime is the mime type of the encoded data."""
    data: builtins.bytes
    """data is the actual set of datapoints, encoded according the the mime type. The data should follow the Feed's
    value definitions but that is not enforced. (See also Value)
    """
    @property
    def occurredAt(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """occurredAt is the UTC timestamp of the sample. Typically this is either the time at which an application shared
        this sample or the time applicable to the sample itself (such as an hourly weather observation).
        (Optional: set to host time if not provided)
        """

    def __init__(
        self,
        *,
        occurredAt: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        mime: builtins.str = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["occurredAt", b"occurredAt"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "mime", b"mime", "occurredAt", b"occurredAt"]) -> None: ...

global___FeedData = FeedData

@typing.final
class PropertyUpdate(google.protobuf.message.Message):
    """PropertyUpdate describes the update of resource's underlying properties.
    Can be used to add, replace, or delete properties. The order of operations is:
    clearedAll (if True), deleted, deletedByKey, added.
    Note that internal properties (such as location) cannot be modified here.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLEAREDALL_FIELD_NUMBER: builtins.int
    DELETED_FIELD_NUMBER: builtins.int
    DELETEDBYKEY_FIELD_NUMBER: builtins.int
    ADDED_FIELD_NUMBER: builtins.int
    clearedAll: builtins.bool
    """Delete all properties currently set on the resource."""
    @property
    def deleted(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Property]:
        """Delete specific exact properties (by key and value). This operation is ignored if clearAll is True."""

    @property
    def deletedByKey(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Delete any properties with the given keys (predicates). This operation is ignored if clearAll is True."""

    @property
    def added(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Property]:
        """Adds the given properties"""

    def __init__(
        self,
        *,
        clearedAll: builtins.bool = ...,
        deleted: collections.abc.Iterable[global___Property] | None = ...,
        deletedByKey: collections.abc.Iterable[builtins.str] | None = ...,
        added: collections.abc.Iterable[global___Property] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["added", b"added", "clearedAll", b"clearedAll", "deleted", b"deleted", "deletedByKey", b"deletedByKey"]) -> None: ...

global___PropertyUpdate = PropertyUpdate
