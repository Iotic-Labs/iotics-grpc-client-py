# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from iotics.api import input_pb2 as iotics_dot_api_dot_input__pb2


class InputAPIStub(object):
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeleteInput = channel.unary_unary(
                '/iotics.api.InputAPI/DeleteInput',
                request_serializer=iotics_dot_api_dot_input__pb2.DeleteInputRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_input__pb2.DeleteInputResponse.FromString,
                )
        self.DescribeInput = channel.unary_unary(
                '/iotics.api.InputAPI/DescribeInput',
                request_serializer=iotics_dot_api_dot_input__pb2.DescribeInputRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_input__pb2.DescribeInputResponse.FromString,
                )
        self.ReceiveInputMessages = channel.unary_stream(
                '/iotics.api.InputAPI/ReceiveInputMessages',
                request_serializer=iotics_dot_api_dot_input__pb2.ReceiveInputMessageRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_input__pb2.ReceiveInputMessageResponse.FromString,
                )
        self.CreateInput = channel.unary_unary(
                '/iotics.api.InputAPI/CreateInput',
                request_serializer=iotics_dot_api_dot_input__pb2.CreateInputRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_input__pb2.CreateInputResponse.FromString,
                )
        self.UpdateInput = channel.unary_unary(
                '/iotics.api.InputAPI/UpdateInput',
                request_serializer=iotics_dot_api_dot_input__pb2.UpdateInputRequest.SerializeToString,
                response_deserializer=iotics_dot_api_dot_input__pb2.UpdateInputResponse.FromString,
                )


class InputAPIServicer(object):
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """

    def DeleteInput(self, request, context):
        """Deletes an input. (Idempotent)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeInput(self, request, context):
        """Describes an input. (local and remote)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveInputMessages(self, request, context):
        """Receives input messages for a specific input.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInput(self, request, context):
        """Creates an input owned by a twin. (Idempotent)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInput(self, request, context):
        """Updates attributes of an input, including its metadata.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InputAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeleteInput': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteInput,
                    request_deserializer=iotics_dot_api_dot_input__pb2.DeleteInputRequest.FromString,
                    response_serializer=iotics_dot_api_dot_input__pb2.DeleteInputResponse.SerializeToString,
            ),
            'DescribeInput': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeInput,
                    request_deserializer=iotics_dot_api_dot_input__pb2.DescribeInputRequest.FromString,
                    response_serializer=iotics_dot_api_dot_input__pb2.DescribeInputResponse.SerializeToString,
            ),
            'ReceiveInputMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.ReceiveInputMessages,
                    request_deserializer=iotics_dot_api_dot_input__pb2.ReceiveInputMessageRequest.FromString,
                    response_serializer=iotics_dot_api_dot_input__pb2.ReceiveInputMessageResponse.SerializeToString,
            ),
            'CreateInput': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateInput,
                    request_deserializer=iotics_dot_api_dot_input__pb2.CreateInputRequest.FromString,
                    response_serializer=iotics_dot_api_dot_input__pb2.CreateInputResponse.SerializeToString,
            ),
            'UpdateInput': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateInput,
                    request_deserializer=iotics_dot_api_dot_input__pb2.UpdateInputRequest.FromString,
                    response_serializer=iotics_dot_api_dot_input__pb2.UpdateInputResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iotics.api.InputAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InputAPI(object):
    """---------------------------------------------------------------------------------------------------------------------

    Input API groups all the actions link to a twin input.
    Services only affect local resources, unless stated otherwise.
    """

    @staticmethod
    def DeleteInput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.InputAPI/DeleteInput',
            iotics_dot_api_dot_input__pb2.DeleteInputRequest.SerializeToString,
            iotics_dot_api_dot_input__pb2.DeleteInputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeInput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.InputAPI/DescribeInput',
            iotics_dot_api_dot_input__pb2.DescribeInputRequest.SerializeToString,
            iotics_dot_api_dot_input__pb2.DescribeInputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveInputMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/iotics.api.InputAPI/ReceiveInputMessages',
            iotics_dot_api_dot_input__pb2.ReceiveInputMessageRequest.SerializeToString,
            iotics_dot_api_dot_input__pb2.ReceiveInputMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateInput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.InputAPI/CreateInput',
            iotics_dot_api_dot_input__pb2.CreateInputRequest.SerializeToString,
            iotics_dot_api_dot_input__pb2.CreateInputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateInput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iotics.api.InputAPI/UpdateInput',
            iotics_dot_api_dot_input__pb2.UpdateInputRequest.SerializeToString,
            iotics_dot_api_dot_input__pb2.UpdateInputResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
