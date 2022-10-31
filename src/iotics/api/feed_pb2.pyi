"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (feed)
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import iotics.api.common_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FeedID(google.protobuf.message.Message):
    """A feed representation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TWINID_FIELD_NUMBER: builtins.int
    HOSTID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Feed identifier string representation (simple string) (unique within the scope of a twin identifier's feed set)"""
    twinId: builtins.str
    """Twin identifier string representation (simple string) (twin to which the feed belongs)"""
    hostId: builtins.str
    """Host identifier string representation (simple string) (Host to which the twin belongs)"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        twinId: builtins.str = ...,
        hostId: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hostId", b"hostId", "id", b"id", "twinId", b"twinId"]) -> None: ...

global___FeedID = FeedID

@typing_extensions.final
class CreateFeedRequest(google.protobuf.message.Message):
    """CreateFeedRequestCreate is used to create a new feed in a given twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """Payload describes the data needed to create a feed."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        id: builtins.str
        """Feed identifier string representation (simple string) (unique within the scope of a twin identifier's feed set)"""
        def __init__(
            self,
            *,
            id: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

    @typing_extensions.final
    class Arguments(google.protobuf.message.Message):
        """Arguments describes the mandatory arguments to identify the twin the feed belongs to."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Identifier of the twin owning this feed"""
        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """CreateFeedRequest headers"""
    @property
    def args(self) -> global___CreateFeedRequest.Arguments:
        """CreateFeedRequest mandatory arguments"""
    @property
    def payload(self) -> global___CreateFeedRequest.Payload:
        """CreateFeedRequest payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___CreateFeedRequest.Arguments | None = ...,
        payload: global___CreateFeedRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> None: ...

global___CreateFeedRequest = CreateFeedRequest

@typing_extensions.final
class CreateFeedResponse(google.protobuf.message.Message):
    """CreateFeedResponse describes a created feed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """CreateFeedResponse payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """The created feed"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """CreateFeedResponse headers"""
    @property
    def payload(self) -> global___CreateFeedResponse.Payload:
        """CreateFeedResponse payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___CreateFeedResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___CreateFeedResponse = CreateFeedResponse

@typing_extensions.final
class DeleteFeedRequest(google.protobuf.message.Message):
    """DeleteFeedRequest is used to delete a feed from a given twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Arguments(google.protobuf.message.Message):
        """DeleteFeedRequest arguments."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """Feed to delete"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DeleteFeedRequest headers"""
    @property
    def args(self) -> global___DeleteFeedRequest.Arguments:
        """DeleteFeedRequest mandatory arguments"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___DeleteFeedRequest.Arguments | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers"]) -> None: ...

global___DeleteFeedRequest = DeleteFeedRequest

@typing_extensions.final
class DeleteFeedResponse(google.protobuf.message.Message):
    """DeleteFeedResponse describes a deleted feed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """DeleteFeedResponse payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """Deleted feed"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DeleteFeedResponse headers"""
    @property
    def payload(self) -> global___DeleteFeedResponse.Payload:
        """DeleteFeedResponse payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___DeleteFeedResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___DeleteFeedResponse = DeleteFeedResponse

@typing_extensions.final
class UpdateFeedRequest(google.protobuf.message.Message):
    """UpdateFeedRequest is used to update attributes (including metadata) of a given feed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """UpdateFeedRequest payload. One or more fields can be provided, depending on what needs to be updated.
        Note that the specified metadata changes are applied in the following order:
        tags, values, labels, comments
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        STORELAST_FIELD_NUMBER: builtins.int
        VALUES_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def storeLast(self) -> google.protobuf.wrappers_pb2.BoolValue:
            """StoreLast dictates whether to store the last shared sample of a feed."""
        @property
        def values(self) -> iotics.api.common_pb2.Values:
            """Values are descriptive individual data items to add/remove."""
        @property
        def properties(self) -> iotics.api.common_pb2.PropertyUpdate:
            """Custom properties to add/remove. Internal properties (such as location) cannot be modified here."""
        def __init__(
            self,
            *,
            storeLast: google.protobuf.wrappers_pb2.BoolValue | None = ...,
            values: iotics.api.common_pb2.Values | None = ...,
            properties: iotics.api.common_pb2.PropertyUpdate | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["properties", b"properties", "storeLast", b"storeLast", "values", b"values"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["properties", b"properties", "storeLast", b"storeLast", "values", b"values"]) -> None: ...

    @typing_extensions.final
    class Arguments(google.protobuf.message.Message):
        """UpdateFeedRequest arguments."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID: ...
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """UpdateFeedRequest headers"""
    @property
    def args(self) -> global___UpdateFeedRequest.Arguments:
        """UpdateFeedRequest arguments"""
    @property
    def payload(self) -> global___UpdateFeedRequest.Payload:
        """UpdateFeedRequest payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___UpdateFeedRequest.Arguments | None = ...,
        payload: global___UpdateFeedRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> None: ...

global___UpdateFeedRequest = UpdateFeedRequest

@typing_extensions.final
class UpdateFeedResponse(google.protobuf.message.Message):
    """UpdateFeedResponse is used to indicate a successful update."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """UpdateFeedResponse payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """Updated feed"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """UpdateFeedResponse headers"""
    @property
    def payload(self) -> global___UpdateFeedResponse.Payload:
        """UpdateFeedResponse payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___UpdateFeedResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___UpdateFeedResponse = UpdateFeedResponse

@typing_extensions.final
class ShareFeedDataRequest(google.protobuf.message.Message):
    """ShareFeedDataRequest is used to share a new sample of data for the given feed."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """ShareFeedDataRequest payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SAMPLE_FIELD_NUMBER: builtins.int
        @property
        def sample(self) -> iotics.api.common_pb2.FeedData:
            """Sample to share"""
        def __init__(
            self,
            *,
            sample: iotics.api.common_pb2.FeedData | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["sample", b"sample"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["sample", b"sample"]) -> None: ...

    @typing_extensions.final
    class Arguments(google.protobuf.message.Message):
        """ShareFeedDataRequest arguments."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """Feed sharing the sample"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """ShareFeedDataRequest headers"""
    @property
    def args(self) -> global___ShareFeedDataRequest.Arguments:
        """ShareFeedDataRequest arguments"""
    @property
    def payload(self) -> global___ShareFeedDataRequest.Payload:
        """ShareFeedDataRequest payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___ShareFeedDataRequest.Arguments | None = ...,
        payload: global___ShareFeedDataRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "payload", b"payload"]) -> None: ...

global___ShareFeedDataRequest = ShareFeedDataRequest

@typing_extensions.final
class ShareFeedDataResponse(google.protobuf.message.Message):
    """ShareFeedDataResponse is used to indicate a successful feed share."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADERS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """ShareFeedDataResponse headers"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers"]) -> None: ...

global___ShareFeedDataResponse = ShareFeedDataResponse

@typing_extensions.final
class ListAllFeedsRequest(google.protobuf.message.Message):
    """ListAllFeedsRequest is used to list all the feeds owned by a given twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Arguments(google.protobuf.message.Message):
        """ListAllFeedsRequest mandatory arguments."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TWINID_FIELD_NUMBER: builtins.int
        @property
        def twinId(self) -> iotics.api.common_pb2.TwinID:
            """Identifier of the twin owning this feed"""
        def __init__(
            self,
            *,
            twinId: iotics.api.common_pb2.TwinID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["twinId", b"twinId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["twinId", b"twinId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    RANGE_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """ListAllFeedsRequest headers"""
    @property
    def args(self) -> global___ListAllFeedsRequest.Arguments:
        """ListAllFeedsRequest arguments"""
    @property
    def range(self) -> iotics.api.common_pb2.Range:
        """Limit the results according to the value
        (optional: when not supplied, assume no default limits required - See https://ioticlabs.atlassian.net/browse/FO-1362)
        """
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___ListAllFeedsRequest.Arguments | None = ...,
        range: iotics.api.common_pb2.Range | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "range", b"range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers", "range", b"range"]) -> None: ...

global___ListAllFeedsRequest = ListAllFeedsRequest

@typing_extensions.final
class ListAllFeedsResponse(google.protobuf.message.Message):
    """ListAllFeedsResponse describes the list of the feeds owned by a twin."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """ListAllFeedsResponse payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDIDS_FIELD_NUMBER: builtins.int
        @property
        def feedIds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeedID]:
            """List of the feeds owned by the twin"""
        def __init__(
            self,
            *,
            feedIds: collections.abc.Iterable[global___FeedID] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedIds", b"feedIds"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """ListAllFeedsResponse headers"""
    @property
    def payload(self) -> global___ListAllFeedsResponse.Payload:
        """ListAllFeedsResponse payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___ListAllFeedsResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___ListAllFeedsResponse = ListAllFeedsResponse

@typing_extensions.final
class DescribeFeedRequest(google.protobuf.message.Message):
    """Description of twin: Provides public metadata lookup for individual resources."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Arguments(google.protobuf.message.Message):
        """DescribeFeedRequest arguments."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """Feed to describe"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DescribeFeedRequest headers"""
    @property
    def args(self) -> global___DescribeFeedRequest.Arguments:
        """DescribeFeedRequest mandatory arguments"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        args: global___DescribeFeedRequest.Arguments | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "headers", b"headers"]) -> None: ...

global___DescribeFeedRequest = DescribeFeedRequest

@typing_extensions.final
class DescribeFeedResponse(google.protobuf.message.Message):
    """Describe feed response."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MetaResult(google.protobuf.message.Message):
        """Metadata result databag."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUES_FIELD_NUMBER: builtins.int
        STORELAST_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Value]:
            """Values semantically describing the share payload of Feed"""
        storeLast: builtins.bool
        """Whether this feed might have its most recent data sample stored. If so, it can be retrieved via FetchLastStored
        request. (See interest API)
        """
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Custom properties associated with this feed."""
        def __init__(
            self,
            *,
            values: collections.abc.Iterable[iotics.api.common_pb2.Value] | None = ...,
            storeLast: builtins.bool = ...,
            properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["properties", b"properties", "storeLast", b"storeLast", "values", b"values"]) -> None: ...

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """DescribeFeedResponse payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FEEDID_FIELD_NUMBER: builtins.int
        RESULT_FIELD_NUMBER: builtins.int
        @property
        def feedId(self) -> global___FeedID:
            """Described feed"""
        @property
        def result(self) -> global___DescribeFeedResponse.MetaResult:
            """Metadata result"""
        def __init__(
            self,
            *,
            feedId: global___FeedID | None = ...,
            result: global___DescribeFeedResponse.MetaResult | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["feedId", b"feedId", "result", b"result"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["feedId", b"feedId", "result", b"result"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DescribeFeedResponse headers"""
    @property
    def payload(self) -> global___DescribeFeedResponse.Payload:
        """DescribeFeedResponse payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___DescribeFeedResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___DescribeFeedResponse = DescribeFeedResponse

@typing_extensions.final
class UpsertFeedWithMeta(google.protobuf.message.Message):
    """UpsertFeedWithMeta is used to describe the full feed state. Used in UpsertTwinRequest."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    STORELAST_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Feed identifier string representation (simple string) (unique within the scope of a twin identifier's feed set)"""
    storeLast: builtins.bool
    """StoreLast dictates whether to store the last shared sample of the feed. Default 'False'"""
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Value]:
        """Values to set"""
    @property
    def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
        """Feed properties to set"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        storeLast: builtins.bool = ...,
        values: collections.abc.Iterable[iotics.api.common_pb2.Value] | None = ...,
        properties: collections.abc.Iterable[iotics.api.common_pb2.Property] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "properties", b"properties", "storeLast", b"storeLast", "values", b"values"]) -> None: ...

global___UpsertFeedWithMeta = UpsertFeedWithMeta
