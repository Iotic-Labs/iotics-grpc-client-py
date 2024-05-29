"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (input)
"""

import abc
import collections.abc
import grpc
import grpc.aio
import iotics.api.input_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class InputAPIStub:
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    DeleteInput: grpc.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.DeleteInputRequest,
        iotics.api.input_pb2.DeleteInputResponse,
    ]
    """Deletes an input. (Idempotent)"""

    DescribeInput: grpc.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.DescribeInputRequest,
        iotics.api.input_pb2.DescribeInputResponse,
    ]
    """Describes an input. (local and remote)"""

    ReceiveInputMessages: grpc.UnaryStreamMultiCallable[
        iotics.api.input_pb2.ReceiveInputMessageRequest,
        iotics.api.input_pb2.ReceiveInputMessageResponse,
    ]
    """Receives input messages for a specific input."""

    CreateInput: grpc.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.CreateInputRequest,
        iotics.api.input_pb2.CreateInputResponse,
    ]
    """Creates an input owned by a twin. (Idempotent)"""

    UpdateInput: grpc.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.UpdateInputRequest,
        iotics.api.input_pb2.UpdateInputResponse,
    ]
    """Updates attributes of an input, including its metadata."""

class InputAPIAsyncStub:
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """

    DeleteInput: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.DeleteInputRequest,
        iotics.api.input_pb2.DeleteInputResponse,
    ]
    """Deletes an input. (Idempotent)"""

    DescribeInput: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.DescribeInputRequest,
        iotics.api.input_pb2.DescribeInputResponse,
    ]
    """Describes an input. (local and remote)"""

    ReceiveInputMessages: grpc.aio.UnaryStreamMultiCallable[
        iotics.api.input_pb2.ReceiveInputMessageRequest,
        iotics.api.input_pb2.ReceiveInputMessageResponse,
    ]
    """Receives input messages for a specific input."""

    CreateInput: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.CreateInputRequest,
        iotics.api.input_pb2.CreateInputResponse,
    ]
    """Creates an input owned by a twin. (Idempotent)"""

    UpdateInput: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.UpdateInputRequest,
        iotics.api.input_pb2.UpdateInputResponse,
    ]
    """Updates attributes of an input, including its metadata."""

class InputAPIServicer(metaclass=abc.ABCMeta):
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """

    @abc.abstractmethod
    def DeleteInput(
        self,
        request: iotics.api.input_pb2.DeleteInputRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.input_pb2.DeleteInputResponse, collections.abc.Awaitable[iotics.api.input_pb2.DeleteInputResponse]]:
        """Deletes an input. (Idempotent)"""

    @abc.abstractmethod
    def DescribeInput(
        self,
        request: iotics.api.input_pb2.DescribeInputRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.input_pb2.DescribeInputResponse, collections.abc.Awaitable[iotics.api.input_pb2.DescribeInputResponse]]:
        """Describes an input. (local and remote)"""

    @abc.abstractmethod
    def ReceiveInputMessages(
        self,
        request: iotics.api.input_pb2.ReceiveInputMessageRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[iotics.api.input_pb2.ReceiveInputMessageResponse], collections.abc.AsyncIterator[iotics.api.input_pb2.ReceiveInputMessageResponse]]:
        """Receives input messages for a specific input."""

    @abc.abstractmethod
    def CreateInput(
        self,
        request: iotics.api.input_pb2.CreateInputRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.input_pb2.CreateInputResponse, collections.abc.Awaitable[iotics.api.input_pb2.CreateInputResponse]]:
        """Creates an input owned by a twin. (Idempotent)"""

    @abc.abstractmethod
    def UpdateInput(
        self,
        request: iotics.api.input_pb2.UpdateInputRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.input_pb2.UpdateInputResponse, collections.abc.Awaitable[iotics.api.input_pb2.UpdateInputResponse]]:
        """Updates attributes of an input, including its metadata."""

def add_InputAPIServicer_to_server(servicer: InputAPIServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
