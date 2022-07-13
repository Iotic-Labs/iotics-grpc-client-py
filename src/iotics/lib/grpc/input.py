# Copyright © 2022 IOTIC LABS LTD. info@iotics.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/Iotic-Labs/iotics-grpc-client-py/blob/main/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing

import grpc
import grpc._channel
from google.protobuf.wrappers_pb2 import BoolValue

from .base import ApiBase
from .helpers import create_headers
from iotics.api import input_pb2_grpc
from iotics.api import input_pb2
from iotics.api import feed_pb2
from iotics.api import common_pb2


class InputApi(ApiBase):
    stub_class = input_pb2_grpc.InputAPIStub
    stub: input_pb2_grpc.InputAPIStub

    def describe_input(
        self,
        twin_id: str,
        input_id: str,
        remote_host_id: typing.Optional[str] = None,
        headers: typing.Optional[common_pb2.Headers] = None,
    ) -> input_pb2.DescribeInputResponse:
        """Describes an input (local and remote).

        Args:
            twin_id:
            input_id:
            remote_host_id:
            headers:

        Returns: A response object describing the input.
        """
        request = input_pb2.DescribeInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.DescribeInputRequest.Arguments(
                input=self.build_input(twin_id, input_id),
                remoteHostId=self.build_host_id(remote_host_id),
            )
        )
        return self.stub.DescribeInput(request)

    def delete_input(
        self,
        twin_id: str,
        input_id: str,
        headers: typing.Optional[common_pb2.Headers] = None,
    ) -> input_pb2.DeleteInputResponse:
        """Deletes an input (idempotent).

        Args:
            twin_id:
            input_id:
            headers:

        Returns: A response object with a payload containing the deleted input.

        """
        request = input_pb2.DeleteInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.DeleteInputRequest.Arguments(input=self.build_input(twin_id, input_id)),
        )
        return self.stub.DeleteInput(request)

    def receive_input_message(self, twin_id, input_id) -> typing.Iterator[input_pb2.ReceiveInputMessageResponse]:
    # def get_input_listener(self, client_app_id: str, timeout: int):

        """Initialises an iterator that listens for input messages for a given Twin ID and Input ID.

        Note: This function must be called before `InterestApi.send_input_message` otherwise messages may be lost.

        Args:
            twin_id:
            input_id:

        Returns: Response iterator with extra blocking (e.g. `time_remaining`) and non-blocking (e.g. `code`) methods.
        """
        # TODO(Adrian): Not sure if/what headers are needed for. Do we need them to get correct responses like in search?
        # sub_headers = common_pb2.SubscriptionHeaders(clientAppId=client_app_id, transactionRef=[client_app_id])
        headers = None
        args = input_pb2.ReceiveInputMessageRequest.Arguments(input=self.build_input(twin_id, input_id))
        request = input_pb2.ReceiveInputMessageRequest(headers=headers, args=args)
        # TODO(Adrian): Not sure how to gracefully exit, hence do we need timeout?
        # input_pb2.ReceiveInputMessageResponse.Payload.input
        # input_pb2.ReceiveInputMessageResponse.Payload.message

        # Define type here to avoid: `TypeError: 'ABCMeta' object is not subscriptable`.
        # input_responses: grpc._channel._MultiThreadedRendezvous[input_pb2.ReceiveInputMessageResponse] = \
        return self.stub.ReceiveInputMessages(request, timeout=None)
