"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (twins)
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import iotics.api.common_pb2
import iotics.api.feed_pb2
import iotics.api.input_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListAllTwinsRequest(google.protobuf.message.Message):
    """List all twins."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADERS_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers: ...
    @property
    def range(self) -> iotics.api.common_pb2.Range:
        """Listing result range"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        range: iotics.api.common_pb2.Range | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "range", b"range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "range", b"range"]) -> None: ...

global___ListAllTwinsRequest = ListAllTwinsRequest

@typing.final
class ListAllTwinsResponse(google.protobuf.message.Message):
    """Response of the list all twins request.
    Note this is useful for sync responses. In case there are too many twins (millions)
    this request may fail. Better opt for async behaviour via stomp/websocket.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TwinDetails(google.protobuf.message.Message):
        """ListAllTwinsResponse twin details."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        LOCATION_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        UPDATEDAT_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Twin identifier."""

        @property
        def location(self) -> iotics.api.common_pb2.GeoLocation:
            """Twin location (if set)."""

        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Twin custom properties."""

        @property
        def updatedAt(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Twin updatedAt timestamp."""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
            location: iotics.api.common_pb2.GeoLocation | None = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
            updatedAt: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["location", b"location", "twinId", b"twinId", "updatedAt", b"updatedAt"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["location", b"location", "properties", b"properties", "twinId", b"twinId", "updatedAt", b"updatedAt"]) -> None: ...

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Payload of listed twins."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINS_FIELD_NUMBER: builtins.int
        @property
        def twins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ListAllTwinsResponse.TwinDetails]: ...
        def __init__(
            self,
            *,
            twins: collections.abc.Iterable[global___ListAllTwinsResponse.TwinDetails] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["twins", b"twins"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers: ...
    @property
    def payload(self) -> global___ListAllTwinsResponse.Payload: ...
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___ListAllTwinsResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___ListAllTwinsResponse = ListAllTwinsResponse

@typing.final
class CreateTwinRequest(google.protobuf.message.Message):
    """CreateTwinRequest is made to create a twin (idempotent)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Arguments identifies the twin to create."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        id: builtins.str
        """Twin identifier string representation (simple string)"""
        def __init__(
            self,
            *,
            id: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Common headers"""

    @property
    def payload(self) -> global___CreateTwinRequest.Payload:
        """Request-specific payload"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___CreateTwinRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___CreateTwinRequest = CreateTwinRequest

@typing.final
class CreateTwinResponse(google.protobuf.message.Message):
    """CreateTwinResponse is received when a twin has been created."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Payload identifies the twin which was created."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to delete"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Common headers"""

    @property
    def payload(self) -> global___CreateTwinResponse.Payload:
        """Request-specific payload"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___CreateTwinResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___CreateTwinResponse = CreateTwinResponse

@typing.final
class DeleteTwinRequest(google.protobuf.message.Message):
    """---------------------------------------

    DeleteRequest is made to delete a particular twin.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Arguments(google.protobuf.message.Message):
        """Arguments identifies the twin to delete."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to delete"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Common headers"""

    @property
    def args(self) -> global___DeleteTwinRequest.Arguments:
        """Request-specific arguments"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___DeleteTwinRequest.Arguments | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["args", b"args", "headers", b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["args", b"args", "headers", b"headers"]) -> None: ...

global___DeleteTwinRequest = DeleteTwinRequest

@typing.final
class DeleteTwinResponse(google.protobuf.message.Message):
    """Deleted is received when a twin has been deleted."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Payload identifies the twin which was deleted."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to delete"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Common headers"""

    @property
    def payload(self) -> global___DeleteTwinResponse.Payload:
        """Request-specific response"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___DeleteTwinResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___DeleteTwinResponse = DeleteTwinResponse

@typing.final
class DescribeTwinRequest(google.protobuf.message.Message):
    """Description of twin: Provides public metadata lookup for individual resources."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Arguments(google.protobuf.message.Message):
        """Only one action argument is necessary."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to describe"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers: ...
    @property
    def args(self) -> global___DescribeTwinRequest.Arguments: ...
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___DescribeTwinRequest.Arguments | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["args", b"args", "headers", b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["args", b"args", "headers", b"headers"]) -> None: ...

global___DescribeTwinRequest = DescribeTwinRequest

@typing.final
class FeedMeta(google.protobuf.message.Message):
    """Metadata message for this Feed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEEDID_FIELD_NUMBER: builtins.int
    STORELAST_FIELD_NUMBER: builtins.int
    storeLast: builtins.bool
    @property
    def feedId(self) -> iotics.api.feed_pb2.FeedID: ...
    def __init__(
        self,
        *,
        feedId: iotics.api.feed_pb2.FeedID | None = ...,
        storeLast: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["feedId", b"feedId"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["feedId", b"feedId", "storeLast", b"storeLast"]) -> None: ...

global___FeedMeta = FeedMeta

@typing.final
class InputMeta(google.protobuf.message.Message):
    """Metadata message for this input."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUTID_FIELD_NUMBER: builtins.int
    @property
    def inputId(self) -> iotics.api.input_pb2.InputID: ...
    def __init__(
        self,
        *,
        inputId: iotics.api.input_pb2.InputID | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["inputId", b"inputId"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["inputId", b"inputId"]) -> None: ...

global___InputMeta = InputMeta

@typing.final
class DescribeTwinResponse(google.protobuf.message.Message):
    """The response for a description request on this twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class MetaResult(google.protobuf.message.Message):
        """Metadata result data bag for this feed."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LOCATION_FIELD_NUMBER: builtins.int
        FEEDS_FIELD_NUMBER: builtins.int
        INPUTS_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        UPDATEDAT_FIELD_NUMBER: builtins.int
        @property
        def location(self) -> iotics.api.common_pb2.GeoLocation: ...
        @property
        def feeds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeedMeta]: ...
        @property
        def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InputMeta]: ...
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Custom properties associated with this twin."""

        @property
        def updatedAt(self) -> google.protobuf.timestamp_pb2.Timestamp:
            """Twin updatedAt timestamp."""

        def __init__(
            self,
            *,
            location: iotics.api.common_pb2.GeoLocation | None = ...,
            feeds: collections.abc.Iterable[global___FeedMeta] | None = ...,
            inputs: collections.abc.Iterable[global___InputMeta] | None = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
            updatedAt: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["location", b"location", "updatedAt", b"updatedAt"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["feeds", b"feeds", "inputs", b"inputs", "location", b"location", "properties", b"properties", "updatedAt", b"updatedAt"]) -> None: ...

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Payload of described twins."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        RESULT_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """the twin"""

        @property
        def result(self) -> global___DescribeTwinResponse.MetaResult:
            """the description details"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
            result: global___DescribeTwinResponse.MetaResult | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["result", b"result", "twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["result", b"result", "twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers: ...
    @property
    def payload(self) -> global___DescribeTwinResponse.Payload: ...
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___DescribeTwinResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___DescribeTwinResponse = DescribeTwinResponse

@typing.final
class GeoLocationUpdate(google.protobuf.message.Message):
    """---------------------------------------

    GeoLocationUpdate describes the update of a twin location.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_FIELD_NUMBER: builtins.int
    @property
    def location(self) -> iotics.api.common_pb2.GeoLocation:
        """New location of the twin. If unset, the previously set location will be removed"""

    def __init__(
        self,
        *,
        location: iotics.api.common_pb2.GeoLocation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["location", b"location"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["location", b"location"]) -> None: ...

global___GeoLocationUpdate = GeoLocationUpdate

@typing.final
class UpdateTwinRequest(google.protobuf.message.Message):
    """UpdateTwinRequest is used to update attributes (including metadata) of a given twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Arguments(google.protobuf.message.Message):
        """UpdateTwinRequest mandatory arguments."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to update"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    @typing.final
    class Payload(google.protobuf.message.Message):
        """UpdateTwinRequest payload. One or more fields can be provided, depending on what needs to be updated.
        Note that the specified metadata changes are applied in the following order:
        tags, properties, labels, comments, location
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PROPERTIES_FIELD_NUMBER: builtins.int
        LOCATION_FIELD_NUMBER: builtins.int
        @property
        def properties(self) -> iotics.api.common_pb2.PropertyUpdate:
            """Custom properties to add/remove. Internal properties (such as location) cannot be modified here."""

        @property
        def location(self) -> global___GeoLocationUpdate:
            """Location to be set/unset"""

        def __init__(
            self,
            *,
            properties: iotics.api.common_pb2.PropertyUpdate | None = ...,
            location: global___GeoLocationUpdate | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["location", b"location", "properties", b"properties"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["location", b"location", "properties", b"properties"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """UpdateTwinRequest headers"""

    @property
    def args(self) -> global___UpdateTwinRequest.Arguments:
        """UpdateTwinRequest arguments"""

    @property
    def payload(self) -> global___UpdateTwinRequest.Payload:
        """UpdateTwinRequest payload"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___UpdateTwinRequest.Arguments | None = ...,
        payload: global___UpdateTwinRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> None: ...

global___UpdateTwinRequest = UpdateTwinRequest

@typing.final
class UpdateTwinResponse(google.protobuf.message.Message):
    """UpdateTwinResponse describes an updated twin. It is received when the update operation is successful."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """UpdateTwinResponse payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to delete"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """UpdateTwinResponse headers"""

    @property
    def payload(self) -> global___UpdateTwinResponse.Payload:
        """UpdateTwinResponse payload"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___UpdateTwinResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___UpdateTwinResponse = UpdateTwinResponse

@typing.final
class UpsertTwinRequest(google.protobuf.message.Message):
    """UpsertTwinRequest describes the full state of a twin + its feeds and inputs to create or update (full update)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """UpsertTwinRequest payload. This state will be applied to the twin, feeds and inputs"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        LOCATION_FIELD_NUMBER: builtins.int
        FEEDS_FIELD_NUMBER: builtins.int
        INPUTS_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the twin to create/update"""

        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Twin Properties to set"""

        @property
        def location(self) -> iotics.api.common_pb2.GeoLocation:
            """Twin location to set. If not set the Twin will have no location"""

        @property
        def feeds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.feed_pb2.UpsertFeedWithMeta]:
            """Feeds with metadata to set for the twin"""

        @property
        def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.input_pb2.UpsertInputWithMeta]:
            """Inputs with metadata to set for the twin"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
            location: iotics.api.common_pb2.GeoLocation | None = ...,
            feeds: collections.abc.Iterable[iotics.api.feed_pb2.UpsertFeedWithMeta] | None = ...,
            inputs: collections.abc.Iterable[iotics.api.input_pb2.UpsertInputWithMeta] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["location", b"location", "twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["feeds", b"feeds", "inputs", b"inputs", "location", b"location", "properties", b"properties", "twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """UpdateTwinRequest headers"""

    @property
    def payload(self) -> global___UpsertTwinRequest.Payload:
        """UpdateTwinRequest payload"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___UpsertTwinRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___UpsertTwinRequest = UpsertTwinRequest

@typing.final
class UpsertTwinResponse(google.protobuf.message.Message):
    """UpsertTwinResponse is received when a twin and its feeds and inputs have been created/updated."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Payload identifies the twin which was created."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Unique ID of the created/updated twin"""

        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Common headers"""

    @property
    def payload(self) -> global___UpsertTwinResponse.Payload:
        """Request-specific payload"""

    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___UpsertTwinResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___UpsertTwinResponse = UpsertTwinResponse
