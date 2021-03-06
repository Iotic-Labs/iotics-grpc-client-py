"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import iotics.api.interest_pb2
import typing

class InterestAPIStub:
    """---------------------------------------------------------------------------------------------------------------------

    InterestAPI enables creation and management of interests between a twin and a feed.
    """
    def __init__(self, channel: grpc.Channel) -> None: ...
    FetchInterests: grpc.UnaryStreamMultiCallable[
        iotics.api.interest_pb2.FetchInterestRequest,
        iotics.api.interest_pb2.FetchInterestResponse]
    """Fetch feed data for this interest. (local and remote)"""

    FetchLastStored: grpc.UnaryUnaryMultiCallable[
        iotics.api.interest_pb2.FetchLastStoredRequest,
        iotics.api.interest_pb2.FetchInterestResponse]
    """Fetch last data shared on this interest. (local and remote)"""

    ListAllInterests: grpc.UnaryUnaryMultiCallable[
        iotics.api.interest_pb2.ListAllInterestsRequest,
        iotics.api.interest_pb2.ListAllInterestsResponse]
    """List all interests associated to a given follower twin (Not implemented yet)."""

    CreateInterest: grpc.UnaryUnaryMultiCallable[
        iotics.api.interest_pb2.CreateInterestRequest,
        iotics.api.interest_pb2.CreateInterestResponse]
    """Create an interest between a follower twin and a followed feed. (Not implemented yet)."""

    DeleteInterest: grpc.UnaryUnaryMultiCallable[
        iotics.api.interest_pb2.DeleteInterestRequest,
        iotics.api.interest_pb2.DeleteInterestResponse]
    """Delete an existing interest. (Not implemented yet)."""

    SendInputMessage: grpc.UnaryUnaryMultiCallable[
        iotics.api.interest_pb2.SendInputMessageRequest,
        iotics.api.interest_pb2.SendInputMessageResponse]
    """Send a message to an input. (local and remote)"""


class InterestAPIServicer(metaclass=abc.ABCMeta):
    """---------------------------------------------------------------------------------------------------------------------

    InterestAPI enables creation and management of interests between a twin and a feed.
    """
    @abc.abstractmethod
    def FetchInterests(self,
        request: iotics.api.interest_pb2.FetchInterestRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[iotics.api.interest_pb2.FetchInterestResponse]:
        """Fetch feed data for this interest. (local and remote)"""
        pass

    @abc.abstractmethod
    def FetchLastStored(self,
        request: iotics.api.interest_pb2.FetchLastStoredRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.interest_pb2.FetchInterestResponse:
        """Fetch last data shared on this interest. (local and remote)"""
        pass

    @abc.abstractmethod
    def ListAllInterests(self,
        request: iotics.api.interest_pb2.ListAllInterestsRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.interest_pb2.ListAllInterestsResponse:
        """List all interests associated to a given follower twin (Not implemented yet)."""
        pass

    @abc.abstractmethod
    def CreateInterest(self,
        request: iotics.api.interest_pb2.CreateInterestRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.interest_pb2.CreateInterestResponse:
        """Create an interest between a follower twin and a followed feed. (Not implemented yet)."""
        pass

    @abc.abstractmethod
    def DeleteInterest(self,
        request: iotics.api.interest_pb2.DeleteInterestRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.interest_pb2.DeleteInterestResponse:
        """Delete an existing interest. (Not implemented yet)."""
        pass

    @abc.abstractmethod
    def SendInputMessage(self,
        request: iotics.api.interest_pb2.SendInputMessageRequest,
        context: grpc.ServicerContext,
    ) -> iotics.api.interest_pb2.SendInputMessageResponse:
        """Send a message to an input. (local and remote)"""
        pass


def add_InterestAPIServicer_to_server(servicer: InterestAPIServicer, server: grpc.Server) -> None: ...
