# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from iotics.api import twin_pb2 as iotics_dot_api_dot_twin__pb2


class TwinAPIStub(object):
    """---------------------------------------------------------------------------------------------------------------------

    TwinAPI enables creation and management of Iotics twins.
    Services only affect local resources, unless stated otherwise.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTwin = channel.unary_unary(
                '/iotics.api.TwinAPI/CreateTwin',
                request_serializer=iotics_dot_api_dot_twin__pb2.CreateTwinRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_twin__pb2.CreateTwinResponse.FromString,
                )
        self.UpsertTwin = channel.unary_unary(
                '/iotics.api.TwinAPI/UpsertTwin',
                request_serializer=iotics_dot_api_dot_twin__pb2.UpsertTwinRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_twin__pb2.UpsertTwinResponse.FromString,
                )
        self.DeleteTwin = channel.unary_unary(
                '/iotics.api.TwinAPI/DeleteTwin',
                request_serializer=iotics_dot_api_dot_twin__pb2.DeleteTwinRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_twin__pb2.DeleteTwinResponse.FromString,
                )
        self.UpdateTwin = channel.unary_unary(
                '/iotics.api.TwinAPI/UpdateTwin',
                request_serializer=iotics_dot_api_dot_twin__pb2.UpdateTwinRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_twin__pb2.UpdateTwinResponse.FromString,
                )
        self.DescribeTwin = channel.unary_unary(
                '/iotics.api.TwinAPI/DescribeTwin',
                request_serializer=iotics_dot_api_dot_twin__pb2.DescribeTwinRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_twin__pb2.DescribeTwinResponse.FromString,
                )
        self.ListAllTwins = channel.unary_unary(
                '/iotics.api.TwinAPI/ListAllTwins',
                request_serializer=iotics_dot_api_dot_twin__pb2.ListAllTwinsRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_twin__pb2.ListAllTwinsResponse.FromString,
                )


class TwinAPIServicer(object):
    """---------------------------------------------------------------------------------------------------------------------

    TwinAPI enables creation and management of Iotics twins.
    Services only affect local resources, unless stated otherwise.
    """

    def CreateTwin(self, request, context):
        """CreateTwin creates a twin.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpsertTwin(self, request, context):
        """UpsertTwin creates or update a twin with its metadata + the twin feeds and inputs with their metadata.
        The full state is applied (ie. if the operation succeeds the state of the twin, feeds and inputs will be the one
        described in the payload)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTwin(self, request, context):
        """DeleteTwin deletes a twin.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTwin(self, request, context):
        """UpdateTwin updates a twin (partial update).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeTwin(self, request, context):
        """Describes a twin. (local and remote)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAllTwins(self, request, context):
        """List all twins.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TwinAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTwin': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTwin,
                    request_deserializer=iotics_dot_api_dot_twin__pb2.CreateTwinRequest.FromString,
                    response_serializer=iotics_dot_api_dot_twin__pb2.CreateTwinResponse.SerializeToString,
            ),
            'UpsertTwin': grpc.unary_unary_rpc_method_handler(
                    servicer.UpsertTwin,
                    request_deserializer=iotics_dot_api_dot_twin__pb2.UpsertTwinRequest.FromString,
                    response_serializer=iotics_dot_api_dot_twin__pb2.UpsertTwinResponse.SerializeToString,
            ),
            'DeleteTwin': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTwin,
                    request_deserializer=iotics_dot_api_dot_twin__pb2.DeleteTwinRequest.FromString,
                    response_serializer=iotics_dot_api_dot_twin__pb2.DeleteTwinResponse.SerializeToString,
            ),
            'UpdateTwin': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTwin,
                    request_deserializer=iotics_dot_api_dot_twin__pb2.UpdateTwinRequest.FromString,
                    response_serializer=iotics_dot_api_dot_twin__pb2.UpdateTwinResponse.SerializeToString,
            ),
            'DescribeTwin': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeTwin,
                    request_deserializer=iotics_dot_api_dot_twin__pb2.DescribeTwinRequest.FromString,
                    response_serializer=iotics_dot_api_dot_twin__pb2.DescribeTwinResponse.SerializeToString,
            ),
            'ListAllTwins': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAllTwins,
                    request_deserializer=iotics_dot_api_dot_twin__pb2.ListAllTwinsRequest.FromString,
                    response_serializer=iotics_dot_api_dot_twin__pb2.ListAllTwinsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iotics.api.TwinAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TwinAPI(object):
    """---------------------------------------------------------------------------------------------------------------------

    TwinAPI enables creation and management of Iotics twins.
    Services only affect local resources, unless stated otherwise.
    """

    @staticmethod
    def CreateTwin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.TwinAPI/CreateTwin',
            iotics_dot_api_dot_twin__pb2.CreateTwinRequest.SerializeToString,
            iotics_dot_api_dot_twin__pb2.CreateTwinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpsertTwin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.TwinAPI/UpsertTwin',
            iotics_dot_api_dot_twin__pb2.UpsertTwinRequest.SerializeToString,
            iotics_dot_api_dot_twin__pb2.UpsertTwinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTwin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.TwinAPI/DeleteTwin',
            iotics_dot_api_dot_twin__pb2.DeleteTwinRequest.SerializeToString,
            iotics_dot_api_dot_twin__pb2.DeleteTwinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTwin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.TwinAPI/UpdateTwin',
            iotics_dot_api_dot_twin__pb2.UpdateTwinRequest.SerializeToString,
            iotics_dot_api_dot_twin__pb2.UpdateTwinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeTwin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.TwinAPI/DescribeTwin',
            iotics_dot_api_dot_twin__pb2.DescribeTwinRequest.SerializeToString,
            iotics_dot_api_dot_twin__pb2.DescribeTwinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAllTwins(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.TwinAPI/ListAllTwins',
            iotics_dot_api_dot_twin__pb2.ListAllTwinsRequest.SerializeToString,
            iotics_dot_api_dot_twin__pb2.ListAllTwinsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
