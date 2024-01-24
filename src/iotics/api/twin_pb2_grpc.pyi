"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (twins)
"""
import abc
import collections.abc
import grpc
import grpc.aio
import iotics.api.twin_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class TwinAPIStub:
    """---------------------------------------------------------------------------------------------------------------------

    TwinAPI enables creation and management of Iotics twins.
    Services only affect local resources, unless stated otherwise.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    CreateTwin: grpc.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.CreateTwinRequest,
        iotics.api.twin_pb2.CreateTwinResponse,
    ]
    """CreateTwin creates a twin."""
    UpsertTwin: grpc.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.UpsertTwinRequest,
        iotics.api.twin_pb2.UpsertTwinResponse,
    ]
    """UpsertTwin creates or update a twin with its metadata + the twin feeds and inputs with their metadata.
    The full state is applied (ie. if the operation succeeds the state of the twin, feeds and inputs will be the one
    described in the payload)
    """
    DeleteTwin: grpc.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.DeleteTwinRequest,
        iotics.api.twin_pb2.DeleteTwinResponse,
    ]
    """DeleteTwin deletes a twin."""
    UpdateTwin: grpc.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.UpdateTwinRequest,
        iotics.api.twin_pb2.UpdateTwinResponse,
    ]
    """UpdateTwin updates a twin (partial update)."""
    DescribeTwin: grpc.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.DescribeTwinRequest,
        iotics.api.twin_pb2.DescribeTwinResponse,
    ]
    """Describes a twin. (local and remote)"""
    ListAllTwins: grpc.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.ListAllTwinsRequest,
        iotics.api.twin_pb2.ListAllTwinsResponse,
    ]
    """List all twins."""

class TwinAPIAsyncStub:
    """---------------------------------------------------------------------------------------------------------------------

    TwinAPI enables creation and management of Iotics twins.
    Services only affect local resources, unless stated otherwise.
    """

    CreateTwin: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.CreateTwinRequest,
        iotics.api.twin_pb2.CreateTwinResponse,
    ]
    """CreateTwin creates a twin."""
    UpsertTwin: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.UpsertTwinRequest,
        iotics.api.twin_pb2.UpsertTwinResponse,
    ]
    """UpsertTwin creates or update a twin with its metadata + the twin feeds and inputs with their metadata.
    The full state is applied (ie. if the operation succeeds the state of the twin, feeds and inputs will be the one
    described in the payload)
    """
    DeleteTwin: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.DeleteTwinRequest,
        iotics.api.twin_pb2.DeleteTwinResponse,
    ]
    """DeleteTwin deletes a twin."""
    UpdateTwin: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.UpdateTwinRequest,
        iotics.api.twin_pb2.UpdateTwinResponse,
    ]
    """UpdateTwin updates a twin (partial update)."""
    DescribeTwin: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.DescribeTwinRequest,
        iotics.api.twin_pb2.DescribeTwinResponse,
    ]
    """Describes a twin. (local and remote)"""
    ListAllTwins: grpc.aio.UnaryUnaryMultiCallable[
        iotics.api.twin_pb2.ListAllTwinsRequest,
        iotics.api.twin_pb2.ListAllTwinsResponse,
    ]
    """List all twins."""

class TwinAPIServicer(metaclass=abc.ABCMeta):
    """---------------------------------------------------------------------------------------------------------------------

    TwinAPI enables creation and management of Iotics twins.
    Services only affect local resources, unless stated otherwise.
    """

    @abc.abstractmethod
    def CreateTwin(
        self,
        request: iotics.api.twin_pb2.CreateTwinRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.twin_pb2.CreateTwinResponse, collections.abc.Awaitable[iotics.api.twin_pb2.CreateTwinResponse]]:
        """CreateTwin creates a twin."""
    @abc.abstractmethod
    def UpsertTwin(
        self,
        request: iotics.api.twin_pb2.UpsertTwinRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.twin_pb2.UpsertTwinResponse, collections.abc.Awaitable[iotics.api.twin_pb2.UpsertTwinResponse]]:
        """UpsertTwin creates or update a twin with its metadata + the twin feeds and inputs with their metadata.
        The full state is applied (ie. if the operation succeeds the state of the twin, feeds and inputs will be the one
        described in the payload)
        """
    @abc.abstractmethod
    def DeleteTwin(
        self,
        request: iotics.api.twin_pb2.DeleteTwinRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.twin_pb2.DeleteTwinResponse, collections.abc.Awaitable[iotics.api.twin_pb2.DeleteTwinResponse]]:
        """DeleteTwin deletes a twin."""
    @abc.abstractmethod
    def UpdateTwin(
        self,
        request: iotics.api.twin_pb2.UpdateTwinRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.twin_pb2.UpdateTwinResponse, collections.abc.Awaitable[iotics.api.twin_pb2.UpdateTwinResponse]]:
        """UpdateTwin updates a twin (partial update)."""
    @abc.abstractmethod
    def DescribeTwin(
        self,
        request: iotics.api.twin_pb2.DescribeTwinRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.twin_pb2.DescribeTwinResponse, collections.abc.Awaitable[iotics.api.twin_pb2.DescribeTwinResponse]]:
        """Describes a twin. (local and remote)"""
    @abc.abstractmethod
    def ListAllTwins(
        self,
        request: iotics.api.twin_pb2.ListAllTwinsRequest,
        context: _ServicerContext,
    ) -> typing.Union[iotics.api.twin_pb2.ListAllTwinsResponse, collections.abc.Awaitable[iotics.api.twin_pb2.ListAllTwinsResponse]]:
        """List all twins."""

def add_TwinAPIServicer_to_server(servicer: TwinAPIServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
