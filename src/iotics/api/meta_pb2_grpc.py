# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from iotics.api import meta_pb2 as iotics_dot_api_dot_meta__pb2


class MetaAPIStub(object):
    """---------------------------------------------------------------------------------------------------------------------

    MetaAPI enables querying of metadata associated with Twins and Feeds.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SparqlQuery = channel.unary_stream(
                '/iotics.api.MetaAPI/SparqlQuery',
                request_serializer=iotics_dot_api_dot_meta__pb2.SparqlQueryRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_meta__pb2.SparqlQueryResponse.FromString,
                )


class MetaAPIServicer(object):
    """---------------------------------------------------------------------------------------------------------------------

    MetaAPI enables querying of metadata associated with Twins and Feeds.
    """

    def SparqlQuery(self, request, context):
        """SparqlQuery performs a SPARQL 1.1 query and returns one or more results, each as a sequence of chunks. Note that:
        - Chunks for a particular result will arrive in-order though they might be interleaved with chunks from other
        results (when performing a non-local query). See scope parameter in SparqlQueryRequest.
        - The call will only complete once the (specified or host default) request timeout has been reached. The client can
        choose to end the stream early once they have received enough results. (E.g. in the case of Scope.LOCAL this
        would be after the one and only sequence of chunks has been received.)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetaAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SparqlQuery': grpc.unary_stream_rpc_method_handler(
                    servicer.SparqlQuery,
                    request_deserializer=iotics_dot_api_dot_meta__pb2.SparqlQueryRequest.FromString,
                    response_serializer=iotics_dot_api_dot_meta__pb2.SparqlQueryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iotics.api.MetaAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetaAPI(object):
    """---------------------------------------------------------------------------------------------------------------------

    MetaAPI enables querying of metadata associated with Twins and Feeds.
    """

    @staticmethod
    def SparqlQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/iotics.api.MetaAPI/SparqlQuery',
            iotics_dot_api_dot_meta__pb2.SparqlQueryRequest.SerializeToString,
            iotics_dot_api_dot_meta__pb2.SparqlQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
