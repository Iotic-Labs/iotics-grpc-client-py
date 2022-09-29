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
import json
import typing

import grpc
import grpc._channel
from google.protobuf.wrappers_pb2 import BoolValue

from iotics.api import common_pb2
from iotics.api import feed_pb2
from iotics.api import input_pb2
from iotics.api import interest_pb2
from iotics.api import interest_pb2_grpc
from iotics.api.common_pb2 import TwinID
from iotics.api.feed_pb2 import FeedID
from iotics.api.input_pb2 import InputID
from iotics.api.interest_pb2 import Interest
from .base import ApiBase
from .helpers import create_headers, create_timestamp


class InterestApi(ApiBase):
    stub_class = interest_pb2_grpc.InterestAPIStub
    stub: interest_pb2_grpc.InterestAPIStub

    @staticmethod
    def _build_interest(follower_twin_did, followed_twin_did, followed_feed_id, remote_host_id=None):
        return interest_pb2.Interest(
            followerTwinId=common_pb2.TwinID(value=follower_twin_did),
            followedFeed=interest_pb2.Interest.FollowedFeed(
                feed=feed_pb2.Feed(
                    id=common_pb2.FeedID(value=followed_feed_id),
                    twinId=common_pb2.TwinID(value=followed_twin_did)
                ),
                hostId=common_pb2.HostID(value=remote_host_id) if remote_host_id else None
            )
        )

    def fetch_interests(
            self,
            follower_twin_did: str,
            followed_twin_did: str,
            followed_feed_id: str,
            remote_host_id: typing.Optional[str] = None,
            fetch_last_stored: bool = True,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> interest_pb2.FetchInterestResponse:
        """Receive streaming data as it is shared to a feed

        Args:
            follower_twin_did: Decentralized identifier of the twin seeking data
            followed_twin_did: Decentralized identifier of the twin providing data
            followed_feed_id: Identifier (unique per-twin) of the feed providing data
            remote_host_id: Remote host on which the followed twin is found (None if local)
            fetch_last_stored: Whether to return the data most recently shared to the feed immediately, rather than
                waiting for a new feed share to return any data
            headers: optional request headers

        Returns: Iterator of Response objects, streamed as data is shared to the feed, with an "interest" attribute
        recapitulating the submitted parameters, and a "feedData" attribute with the following attributes:
            occurredAt: Timestamp for the shared data, expressed in seconds since the epoch
            mime: MIME type of the shared data
            data: The data shared to the feed
        """
        req = interest_pb2.FetchInterestRequest(
            headers=headers or create_headers(),
            args=interest_pb2.FetchInterestRequest.Arguments(
                interest=Interest(followerTwinId=TwinID(id=follower_twin_did), followedFeedId=FeedID(
                    id=followed_feed_id, twinId=followed_twin_did, hostId=remote_host_id))
            ),
            fetchLastStored=BoolValue(value=fetch_last_stored)
        )
        # Define type here to avoid: `TypeError: 'ABCMeta' object is not subscriptable`.
        interests: grpc._channel._MultiThreadedRendezvous[interest_pb2.FetchInterestResponse] = \
            self.stub.FetchInterests(req)
        return interests

    def fetch_last_stored(
            self,
            follower_twin_did: str,
            followed_twin_did: str,
            followed_feed_id: str,
            remote_host_id: typing.Optional[str] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> interest_pb2.FetchInterestResponse:
        """Retrieve the data most recently shared to a given feed

        Args:
            follower_twin_did: Decentralized identifier of the twin seeking data
            followed_twin_did: Decentralized identifier of the twin providing data
            followed_feed_id: Identifier (unique per-twin) of the feed providing data
            remote_host_id: Remote host on which the followed twin is found (None if local)
            headers: optional request headers

        Returns: Response object with an "interest" attribute recapitulating the submitted parameters, and a "feedData"
        attribute with the following attributes:
            occurredAt: Timestamp for the shared data, expressed in seconds since the epoch
            mime: MIME type of the shared data
            data: The data shared to the feed
        """
        req = interest_pb2.FetchLastStoredRequest(
            headers=headers or create_headers(),
            args=interest_pb2.FetchLastStoredRequest.Arguments(
                interest=Interest(followerTwinId=TwinID(id=follower_twin_did), followedFeedId=FeedID(
                    id=followed_feed_id, twinId=followed_twin_did, hostId=remote_host_id))
            )
        )
        return self.stub.FetchLastStored(req)

    def send_input_message(
        self,
        message: typing.Any,
        sender_twin_id: str,
        receiver_twin_id: str,
        input_id: str,
        remote_host_id: typing.Optional[str] = None,
        headers: typing.Optional[common_pb2.Headers] = None,
    ) -> interest_pb2.SendInputMessageResponse:
        """Sends a message to the input of a local or remote twin.

        Args:
            message: What to send the remote twin, usually in the form of a dict with keys matching the input's Values
            sender_twin_id: The twin sending the message
            receiver_twin_id: The twin receiving the message
            input_id: The ID of the input where the message will be sent
            remote_host_id: If the receiver twin is remote, its host ID (None if local)
            headers: optional request headers

        Returns: Response object indicating success

        """
        input_interest = interest_pb2.InputInterest(
            senderTwinId=common_pb2.TwinID(id=sender_twin_id),
            destInputId=InputID(id=input_id, twinId=receiver_twin_id, hostId=remote_host_id),
        )
        input_message = input_pb2.InputMessage(
            occurredAt=create_timestamp(),
            mime='application/json',
            data=json.dumps(message).encode(),
        )
        request = interest_pb2.SendInputMessageRequest(
            headers=headers or create_headers(),
            args=interest_pb2.SendInputMessageRequest.Arguments(interest=input_interest),
            payload=interest_pb2.SendInputMessageRequest.Payload(message=input_message),
        )
        return self.stub.SendInputMessage(request=request)
