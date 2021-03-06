"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import iotics.api.input_pb2
import typing

class InputAPIStub:
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """
    def __init__(self, channel: grpc.Channel) -> None: ...
    DeleteInput: grpc.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.DeleteInputRequest,
        iotics.api.input_pb2.DeleteInputResponse]
    """Deletes an input. (Idempotent)"""

    DescribeInput: grpc.UnaryUnaryMultiCallable[
        iotics.api.input_pb2.DescribeInputRequest,
        iotics.api.input_pb2.DescribeInputResponse]
    """Describes an input. (local and remote)"""

    ReceiveInputMessages: grpc.UnaryStreamMultiCallable[
        iotics.api.input_pb2.ReceiveInputMessageRequest,
        iotics.api.input_pb2.ReceiveInputMessageResponse]
    """Receives input messages for a specific input."""


class InputAPIServicer(metaclass=abc.ABCMeta):
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """
    @abc.abstractmethod
    def DeleteInput(self,
        request: iotics.api.input_pb2.DeleteInputRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.input_pb2.DeleteInputResponse:
        """Deletes an input. (Idempotent)"""
        pass

    @abc.abstractmethod
    def DescribeInput(self,
        request: iotics.api.input_pb2.DescribeInputRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.input_pb2.DescribeInputResponse:
        """Describes an input. (local and remote)"""
        pass

    @abc.abstractmethod
    def ReceiveInputMessages(self,
        request: iotics.api.input_pb2.ReceiveInputMessageRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[iotics.api.input_pb2.ReceiveInputMessageResponse]:
        """Receives input messages for a specific input."""
        pass


def add_InputAPIServicer_to_server(servicer: InputAPIServicer, server: grpc.Server) -> None: ...
