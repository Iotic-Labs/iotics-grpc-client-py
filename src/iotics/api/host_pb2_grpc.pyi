"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (hosts)
"""

import abc
import collections.abc
import grpc
import grpc.aio
import iotics.api.host_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class HostAPIStub:
    """---------------------------------------------------------------------------------------------------------------------

    HostAPI enables management of Iotics host twins.
    Services only affect local resources, unless stated otherwise.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetHostID: grpc.UnaryUnaryMultiCallable[
        iotics.api.host_pb2.GetHostIDRequest,
        iotics.api.host_pb2.GetHostIDResponse,
    ]
    """GetHostID gets the ID of the host twin."""

class HostAPIAsyncStub:
    """---------------------------------------------------------------------------------------------------------------------

    HostAPI enables management of Iotics host twins.
    Services only affect local resources, unless stated otherwise.
    """

    GetHostID: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.host_pb2.GetHostIDRequest,
        iotics.api.host_pb2.GetHostIDResponse,
    ]
    """GetHostID gets the ID of the host twin."""

class HostAPIServicer(metaclass=abc.ABCMeta):
    """---------------------------------------------------------------------------------------------------------------------

    HostAPI enables management of Iotics host twins.
    Services only affect local resources, unless stated otherwise.
    """

    @abc.abstractmethod
    def GetHostID(
        self,
        request: iotics.api.host_pb2.GetHostIDRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.host_pb2.GetHostIDResponse, collections.abc.Awaitable[iotics.api.host_pb2.GetHostIDResponse]]:
        """GetHostID gets the ID of the host twin."""

def add_HostAPIServicer_to_server(servicer: HostAPIServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
