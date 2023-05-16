# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: iotics/api/twin.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.timestamp_pb2
import iotics.api.common_pb2
import iotics.api.feed_pb2
import iotics.api.input_pb2
import iotics.api.twin_pb2


class TwinAPIBase(abc.ABC):

    @abc.abstractmethod
    async def CreateTwin(self, stream: 'grpclib.server.Stream[iotics.api.twin_pb2.CreateTwinRequest, iotics.api.twin_pb2.CreateTwinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpsertTwin(self, stream: 'grpclib.server.Stream[iotics.api.twin_pb2.UpsertTwinRequest, iotics.api.twin_pb2.UpsertTwinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTwin(self, stream: 'grpclib.server.Stream[iotics.api.twin_pb2.DeleteTwinRequest, iotics.api.twin_pb2.DeleteTwinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTwin(self, stream: 'grpclib.server.Stream[iotics.api.twin_pb2.UpdateTwinRequest, iotics.api.twin_pb2.UpdateTwinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DescribeTwin(self, stream: 'grpclib.server.Stream[iotics.api.twin_pb2.DescribeTwinRequest, iotics.api.twin_pb2.DescribeTwinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListAllTwins(self, stream: 'grpclib.server.Stream[iotics.api.twin_pb2.ListAllTwinsRequest, iotics.api.twin_pb2.ListAllTwinsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/iotics.api.TwinAPI/CreateTwin': grpclib.const.Handler(
                self.CreateTwin,
                grpclib.const.Cardinality.UNARY_UNARY,
                iotics.api.twin_pb2.CreateTwinRequest,
                iotics.api.twin_pb2.CreateTwinResponse,
            ),
            '/iotics.api.TwinAPI/UpsertTwin': grpclib.const.Handler(
                self.UpsertTwin,
                grpclib.const.Cardinality.UNARY_UNARY,
                iotics.api.twin_pb2.UpsertTwinRequest,
                iotics.api.twin_pb2.UpsertTwinResponse,
            ),
            '/iotics.api.TwinAPI/DeleteTwin': grpclib.const.Handler(
                self.DeleteTwin,
                grpclib.const.Cardinality.UNARY_UNARY,
                iotics.api.twin_pb2.DeleteTwinRequest,
                iotics.api.twin_pb2.DeleteTwinResponse,
            ),
            '/iotics.api.TwinAPI/UpdateTwin': grpclib.const.Handler(
                self.UpdateTwin,
                grpclib.const.Cardinality.UNARY_UNARY,
                iotics.api.twin_pb2.UpdateTwinRequest,
                iotics.api.twin_pb2.UpdateTwinResponse,
            ),
            '/iotics.api.TwinAPI/DescribeTwin': grpclib.const.Handler(
                self.DescribeTwin,
                grpclib.const.Cardinality.UNARY_UNARY,
                iotics.api.twin_pb2.DescribeTwinRequest,
                iotics.api.twin_pb2.DescribeTwinResponse,
            ),
            '/iotics.api.TwinAPI/ListAllTwins': grpclib.const.Handler(
                self.ListAllTwins,
                grpclib.const.Cardinality.UNARY_UNARY,
                iotics.api.twin_pb2.ListAllTwinsRequest,
                iotics.api.twin_pb2.ListAllTwinsResponse,
            ),
        }


class TwinAPIStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateTwin = grpclib.client.UnaryUnaryMethod(
            channel,
            '/iotics.api.TwinAPI/CreateTwin',
            iotics.api.twin_pb2.CreateTwinRequest,
            iotics.api.twin_pb2.CreateTwinResponse,
        )
        self.UpsertTwin = grpclib.client.UnaryUnaryMethod(
            channel,
            '/iotics.api.TwinAPI/UpsertTwin',
            iotics.api.twin_pb2.UpsertTwinRequest,
            iotics.api.twin_pb2.UpsertTwinResponse,
        )
        self.DeleteTwin = grpclib.client.UnaryUnaryMethod(
            channel,
            '/iotics.api.TwinAPI/DeleteTwin',
            iotics.api.twin_pb2.DeleteTwinRequest,
            iotics.api.twin_pb2.DeleteTwinResponse,
        )
        self.UpdateTwin = grpclib.client.UnaryUnaryMethod(
            channel,
            '/iotics.api.TwinAPI/UpdateTwin',
            iotics.api.twin_pb2.UpdateTwinRequest,
            iotics.api.twin_pb2.UpdateTwinResponse,
        )
        self.DescribeTwin = grpclib.client.UnaryUnaryMethod(
            channel,
            '/iotics.api.TwinAPI/DescribeTwin',
            iotics.api.twin_pb2.DescribeTwinRequest,
            iotics.api.twin_pb2.DescribeTwinResponse,
        )
        self.ListAllTwins = grpclib.client.UnaryUnaryMethod(
            channel,
            '/iotics.api.TwinAPI/ListAllTwins',
            iotics.api.twin_pb2.ListAllTwinsRequest,
            iotics.api.twin_pb2.ListAllTwinsResponse,
        )
