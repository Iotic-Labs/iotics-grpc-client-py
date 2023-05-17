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

from iotics.api.input_pb2 import InputID

from .base import ApiBase
from .helpers import create_headers
from iotics.api import input_pb2_grpc
from iotics.api import input_pb2
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
            twin_id: The twin whose input will be described
            input_id: The ID of the input to be described
            remote_host_id: The remote host on which the twin is found -- None if twin is local
            headers: optional request headers

        Returns: A response object describing the input.
        """
        request = input_pb2.DescribeInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.DescribeInputRequest.Arguments(
                inputId=InputID(id=input_id, twinId=twin_id, hostId=remote_host_id),
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
            twin_id: The twin whose input will be deleted
            input_id: The ID of the input to be deleted
            headers: optional request headers

        Returns: A response object with a payload containing the deleted input.

        """
        request = input_pb2.DeleteInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.DeleteInputRequest.Arguments(inputId=InputID(id=input_id, twinId=twin_id)),
        )
        return self.stub.DeleteInput(request)

    def receive_input_messages(
            self,
            twin_id: str,
            input_id: str,
            timeout: typing.Optional[int] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> typing.Iterator[input_pb2.ReceiveInputMessageResponse]:
        """Initialises an iterator that listens for input messages for a given Twin ID and Input ID.

        Note: This function must be called before `InterestApi.send_input_message` otherwise messages may be lost.

        Args:
            twin_id: The twin offering the input to receive messages on
            input_id: The input that will receive the messages
            timeout: How long before the input stops listening
            headers: optional request headers

        Returns: Response iterator with extra blocking (e.g. `time_remaining`) and non-blocking (e.g. `code`) methods.
        """
        args = input_pb2.ReceiveInputMessageRequest.Arguments(inputId=InputID(id=input_id, twinId=twin_id))
        request = input_pb2.ReceiveInputMessageRequest(headers=headers or create_headers(), args=args)

        # Define type here to avoid: `TypeError: 'ABCMeta' object is not subscriptable`.
        input_responses: grpc._channel._MultiThreadedRendezvous[input_pb2.ReceiveInputMessageResponse] = \
            self.stub.ReceiveInputMessages(request, timeout=timeout)
        return input_responses
