"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import iotics.api.common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Input(google.protobuf.message.Message):
    """Representation of an input."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    TWINID_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> iotics.api.common_pb2.InputID:
        """Input identifier (unique within the scope of a twin identifier's input set)"""
        pass
    @property
    def twinId(self) -> iotics.api.common_pb2.TwinID:
        """Twin unique identifier (twin to which the input belongs)"""
        pass
    def __init__(self,
        *,
        id: typing.Optional[iotics.api.common_pb2.InputID] = ...,
        twinId: typing.Optional[iotics.api.common_pb2.TwinID] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id",b"id","twinId",b"twinId"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","twinId",b"twinId"]) -> None: ...
global___Input = Input

class DeleteInputRequest(google.protobuf.message.Message):
    """DeleteInputRequest is used to delete an input from a given twin."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Arguments(google.protobuf.message.Message):
        """DeleteInputRequest arguments."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INPUT_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> global___Input:
            """Input to delete"""
            pass
        def __init__(self,
            *,
            input: typing.Optional[global___Input] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["input",b"input"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["input",b"input"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DeleteInputRequest headers"""
        pass
    @property
    def args(self) -> global___DeleteInputRequest.Arguments:
        """DeleteInputRequest mandatory arguments"""
        pass
    def __init__(self,
        *,
        headers: typing.Optional[iotics.api.common_pb2.Headers] = ...,
        args: typing.Optional[global___DeleteInputRequest.Arguments] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args",b"args","headers",b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","headers",b"headers"]) -> None: ...
global___DeleteInputRequest = DeleteInputRequest

class DeleteInputResponse(google.protobuf.message.Message):
    """DeleteInputResponse describes a deleted input."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Payload(google.protobuf.message.Message):
        """DeleteInputResponse payload."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INPUT_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> global___Input:
            """Deleted input"""
            pass
        def __init__(self,
            *,
            input: typing.Optional[global___Input] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["input",b"input"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["input",b"input"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DeleteInputResponse headers"""
        pass
    @property
    def payload(self) -> global___DeleteInputResponse.Payload:
        """DeleteInputResponse payload"""
        pass
    def __init__(self,
        *,
        headers: typing.Optional[iotics.api.common_pb2.Headers] = ...,
        payload: typing.Optional[global___DeleteInputResponse.Payload] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers",b"headers","payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers",b"headers","payload",b"payload"]) -> None: ...
global___DeleteInputResponse = DeleteInputResponse

class DescribeInputRequest(google.protobuf.message.Message):
    """DescribeInputRequest is used to request the input metadata."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Arguments(google.protobuf.message.Message):
        """DescribeInputRequest arguments."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INPUT_FIELD_NUMBER: builtins.int
        REMOTEHOSTID_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> global___Input:
            """Input to describe"""
            pass
        @property
        def remoteHostId(self) -> iotics.api.common_pb2.HostID:
            """HostID to describe a remote input (Optional, keep empty if input is local)"""
            pass
        def __init__(self,
            *,
            input: typing.Optional[global___Input] = ...,
            remoteHostId: typing.Optional[iotics.api.common_pb2.HostID] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["input",b"input","remoteHostId",b"remoteHostId"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["input",b"input","remoteHostId",b"remoteHostId"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DescribeInputRequest headers"""
        pass
    @property
    def args(self) -> global___DescribeInputRequest.Arguments:
        """DescribeInputRequest mandatory arguments"""
        pass
    def __init__(self,
        *,
        headers: typing.Optional[iotics.api.common_pb2.Headers] = ...,
        args: typing.Optional[global___DescribeInputRequest.Arguments] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args",b"args","headers",b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","headers",b"headers"]) -> None: ...
global___DescribeInputRequest = DescribeInputRequest

class DescribeInputResponse(google.protobuf.message.Message):
    """DescribeInputResponse provides metadata lookup for individual input resources."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MetaResult(google.protobuf.message.Message):
        """DescribeInputResponse metadata result."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        VALUES_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Value]:
            """Values semantically describing the Input messages"""
            pass
        @property
        def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
            """Custom properties associated with this input."""
            pass
        def __init__(self,
            *,
            values: typing.Optional[typing.Iterable[iotics.api.common_pb2.Value]] = ...,
            properties: typing.Optional[typing.Iterable[iotics.api.common_pb2.Property]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["properties",b"properties","values",b"values"]) -> None: ...

    class Payload(google.protobuf.message.Message):
        """DescribeInputResponse payload."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INPUT_FIELD_NUMBER: builtins.int
        RESULT_FIELD_NUMBER: builtins.int
        REMOTEHOSTID_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> global___Input:
            """Described input"""
            pass
        @property
        def result(self) -> global___DescribeInputResponse.MetaResult:
            """Metadata result"""
            pass
        @property
        def remoteHostId(self) -> iotics.api.common_pb2.HostID:
            """HostID of the described input. (Optional, empty if input is local)"""
            pass
        def __init__(self,
            *,
            input: typing.Optional[global___Input] = ...,
            result: typing.Optional[global___DescribeInputResponse.MetaResult] = ...,
            remoteHostId: typing.Optional[iotics.api.common_pb2.HostID] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["input",b"input","remoteHostId",b"remoteHostId","result",b"result"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["input",b"input","remoteHostId",b"remoteHostId","result",b"result"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """DescribeInputResponse headers"""
        pass
    @property
    def payload(self) -> global___DescribeInputResponse.Payload:
        """DescribeInputResponse payload"""
        pass
    def __init__(self,
        *,
        headers: typing.Optional[iotics.api.common_pb2.Headers] = ...,
        payload: typing.Optional[global___DescribeInputResponse.Payload] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers",b"headers","payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers",b"headers","payload",b"payload"]) -> None: ...
global___DescribeInputResponse = DescribeInputResponse

class UpsertInputWithMeta(google.protobuf.message.Message):
    """UpsertInputWithMeta is used to describe the full input state. Used in UpsertTwinRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    PROPERTIES_FIELD_NUMBER: builtins.int
    id: typing.Text
    """Id of the input to create/update"""

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Value]:
        """Values to set"""
        pass
    @property
    def properties(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[iotics.api.common_pb2.Property]:
        """Properties to set"""
        pass
    def __init__(self,
        *,
        id: typing.Text = ...,
        values: typing.Optional[typing.Iterable[iotics.api.common_pb2.Value]] = ...,
        properties: typing.Optional[typing.Iterable[iotics.api.common_pb2.Property]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","properties",b"properties","values",b"values"]) -> None: ...
global___UpsertInputWithMeta = UpsertInputWithMeta

class InputMessage(google.protobuf.message.Message):
    """InputMessage describe a message that can be sent to an input"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OCCURREDAT_FIELD_NUMBER: builtins.int
    MIME_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def occurredAt(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """OccurredAt is the UTC timestamp of the message.
        Typically this is either the time at which an application sent this message
        or the time applicable to the message itself. (Optional: set to host time if not provided)
        """
        pass
    mime: typing.Text
    """Mime is the mime type of the encoded data."""

    data: builtins.bytes
    """Data is the actual message, encoded according the the mime type. The data should follow the Input's
    value definitions but that is not enforced. (See also Value)
    """

    def __init__(self,
        *,
        occurredAt: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        mime: typing.Text = ...,
        data: builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["occurredAt",b"occurredAt"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data",b"data","mime",b"mime","occurredAt",b"occurredAt"]) -> None: ...
global___InputMessage = InputMessage

class ReceiveInputMessageRequest(google.protobuf.message.Message):
    """ReceiveInputMessageRequest is used to receive messages sent to a given Input."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Arguments(google.protobuf.message.Message):
        """ReceiveInputMessageRequest arguments."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INPUT_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> global___Input:
            """Input to listen messages from"""
            pass
        def __init__(self,
            *,
            input: typing.Optional[global___Input] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["input",b"input"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["input",b"input"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """ReceiveInputMessageRequest headers"""
        pass
    @property
    def args(self) -> global___ReceiveInputMessageRequest.Arguments:
        """ReceiveInputMessageRequest mandatory arguments"""
        pass
    def __init__(self,
        *,
        headers: typing.Optional[iotics.api.common_pb2.Headers] = ...,
        args: typing.Optional[global___ReceiveInputMessageRequest.Arguments] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["args",b"args","headers",b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","headers",b"headers"]) -> None: ...
global___ReceiveInputMessageRequest = ReceiveInputMessageRequest

class ReceiveInputMessageResponse(google.protobuf.message.Message):
    """ReceiveInputMessageResponse contains a message sent to the Input."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Payload(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        INPUT_FIELD_NUMBER: builtins.int
        MESSAGE_FIELD_NUMBER: builtins.int
        @property
        def input(self) -> global___Input:
            """Input the message has been sent to"""
            pass
        @property
        def message(self) -> global___InputMessage:
            """Input message"""
            pass
        def __init__(self,
            *,
            input: typing.Optional[global___Input] = ...,
            message: typing.Optional[global___InputMessage] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["input",b"input","message",b"message"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["input",b"input","message",b"message"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """ReceiveInputMessageResponse headers"""
        pass
    @property
    def payload(self) -> global___ReceiveInputMessageResponse.Payload:
        """ReceiveInputMessageResponse payload"""
        pass
    def __init__(self,
        *,
        headers: typing.Optional[iotics.api.common_pb2.Headers] = ...,
        payload: typing.Optional[global___ReceiveInputMessageResponse.Payload] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers",b"headers","payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers",b"headers","payload",b"payload"]) -> None: ...
global___ReceiveInputMessageResponse = ReceiveInputMessageResponse
