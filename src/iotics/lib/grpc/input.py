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

    def create_input(
            self, twin_did: str,
            input_id: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> input_pb2.CreateInputResponse:
        """Create a input on the given twin
        Args:
            twin_did: Decentralized Identifier of the twin on which a input should be created
            input_id: A string identifying this input that is unique to this twin
            headers: optional request headers
        Returns: Response object confirming the input's details (ie, the two IDs that were given)
        """
        req = input_pb2.CreateInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.CreateInputRequest.Arguments(twinId=common_pb2.TwinID(id=twin_did)),
            payload=input_pb2.CreateInputRequest.Payload(id=input_id)
        )
        return self.stub.CreateInput(req)

    def update_input(
            self,
            twin_did: str,
            input_id: str,
            values_added: typing.Optional[list] = None,
            values_deleted: typing.Optional[list] = None,
            props_added: typing.Optional[list] = None,
            props_deleted: typing.Optional[list] = None,
            props_keys_deleted: typing.Optional[list] = None,
            clear_all_props: bool = False,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> input_pb2.UpdateInputResponse:
        """Update the details of the given input. Any arguments omitted will have their values unchanged
        Args:
            twin_did: Decentralized Identifier of the twin providing this input
            input_id: A string identifying this input that is unique to this twin
            values_added: A list of Value objects (metadata describing the structure of shared data) to be added to the
                input. These may be created via the create_value helper
            values_deleted: A list of Value objects to be removed from the input
            props_added: A list of semantic properties to be added to the input
            props_deleted: A list of semantic properties to be removed from the input
            props_keys_deleted: A list of any property keys for which all values should be removed from the input
            clear_all_props: Whether or not to remove all semantic properties from the input
            headers: optional request headers
        Returns: Response object confirming the IDs of the twin and input being updated
        """
        req = input_pb2.UpdateInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.UpdateInputRequest.Arguments(
                inputId=input_pb2.InputID(id=input_id, twinId=twin_did)
            ),
            payload=input_pb2.UpdateInputRequest.Payload(
                values=common_pb2.Values(added=values_added, deletedByLabel=values_deleted),
                properties=common_pb2.PropertyUpdate(
                    added=props_added, deleted=props_deleted, deletedByKey=props_keys_deleted,
                    clearedAll=clear_all_props
                )
            )
        )
        return self.stub.UpdateInput(req)


    def describe_input(
        self,
        twin_did: str,
        input_id: str,
        remote_host_id: typing.Optional[str] = None,
        headers: typing.Optional[common_pb2.Headers] = None,
    ) -> input_pb2.DescribeInputResponse:
        """Describes an input (local and remote).

        Args:
            twin_did: The twin whose input will be described
            input_id: The ID of the input to be described
            remote_host_id: The remote host on which the twin is found -- None if twin is local
            headers: optional request headers

        Returns: A response object describing the input.
        """
        request = input_pb2.DescribeInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.DescribeInputRequest.Arguments(
                inputId=InputID(id=input_id, twinId=twin_did, hostId=remote_host_id),
            )
        )
        return self.stub.DescribeInput(request)

    def delete_input(
        self,
        twin_did: str,
        input_id: str,
        headers: typing.Optional[common_pb2.Headers] = None,
    ) -> input_pb2.DeleteInputResponse:
        """Deletes an input (idempotent).

        Args:
            twin_did: The twin whose input will be deleted
            input_id: The ID of the input to be deleted
            headers: optional request headers

        Returns: A response object with a payload containing the deleted input.

        """
        request = input_pb2.DeleteInputRequest(
            headers=headers or create_headers(),
            args=input_pb2.DeleteInputRequest.Arguments(inputId=InputID(id=input_id, twinId=twin_did)),
        )
        return self.stub.DeleteInput(request)

    def receive_input_messages(
            self,
            twin_did: str,
            input_id: str,
            timeout: typing.Optional[int] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> typing.Iterator[input_pb2.ReceiveInputMessageResponse]:
        """Initialises an iterator that listens for input messages for a given Twin ID and Input ID.

        Note: This function must be called before `InterestApi.send_input_message` otherwise messages may be lost.

        Args:
            twin_did: The twin offering the input to receive messages on
            input_id: The input that will receive the messages
            timeout: How long before the input stops listening
            headers: optional request headers

        Returns: Response iterator with extra blocking (e.g. `time_remaining`) and non-blocking (e.g. `code`) methods.
        """
        args = input_pb2.ReceiveInputMessageRequest.Arguments(inputId=InputID(id=input_id, twinId=twin_did))
        request = input_pb2.ReceiveInputMessageRequest(headers=headers or create_headers(), args=args)

        # Define type here to avoid: `TypeError: 'ABCMeta' object is not subscriptable`.
        input_responses: grpc._channel._MultiThreadedRendezvous[input_pb2.ReceiveInputMessageResponse] = \
            self.stub.ReceiveInputMessages(request, timeout=timeout)
        return input_responses
