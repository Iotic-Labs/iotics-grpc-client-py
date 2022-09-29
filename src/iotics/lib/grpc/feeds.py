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
import time
import typing

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import BoolValue

from .base import ApiBase
from .helpers import create_headers
from iotics.api import feed_pb2_grpc
from iotics.api import feed_pb2
from iotics.api import common_pb2


class FeedApi(ApiBase):
    stub_class = feed_pb2_grpc.FeedAPIStub
    stub: feed_pb2_grpc.FeedAPIStub

    def create_feed(
            self, twin_did: str,
            feed_id: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> feed_pb2.CreateFeedResponse:
        """Create a feed on the given twin

        Args:
            twin_did: Decentralized Identifier of the twin on which a feed should be created
            feed_id: A string identifying this feed that is unique to this twin
            headers: optional request headers

        Returns: Response object confirming the feed's details (ie, the two IDs that were given)
        """
        req = feed_pb2.CreateFeedRequest(
            headers=headers or create_headers(),
            args=feed_pb2.CreateFeedRequest.Arguments(twinId=common_pb2.TwinID(id=twin_did)),
            payload=feed_pb2.CreateFeedRequest.Payload(id=feed_id)
        )
        return self.stub.CreateFeed(req)

    def delete_feed(
            self,
            twin_did: str,
            feed_id: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> feed_pb2.DeleteFeedResponse:
        """Delete a feed from the given twin

        Args:
            twin_did: Decentralized Identifier of the twin on which a feed should be created
            feed_id: A string identifying this feed that is unique to this twin
            headers: optional request headers

        Returns: Response object confirming the feed's details (ie, the two IDs that were given)
        """
        req = feed_pb2.DeleteFeedRequest(
            headers=headers or create_headers(),
            args=feed_pb2.DeleteFeedRequest.Arguments(feedId=feed_pb2.FeedID(id=feed_id, twinId=twin_did))
        )
        return self.stub.DeleteFeed(req)

    def update_feed(
            self,
            twin_did: str,
            feed_id: str,
            store_last: bool = True,
            values_added: typing.Optional[list] = None,
            values_deleted: typing.Optional[list] = None,
            props_added: typing.Optional[list] = None,
            props_deleted: typing.Optional[list] = None,
            props_keys_deleted: typing.Optional[list] = None,
            clear_all_props: bool = False,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> feed_pb2.UpdateFeedResponse:
        """Update the details of the given feed. Any arguments omitted will have their values unchanged

        Args:
            twin_did: Decentralized Identifier of the twin providing this feed
            feed_id: A string identifying this feed that is unique to this twin
            store_last: Whether the data last shared to this feed should be stored for retrieval via the Interest API,
                or only available to its subscribers at the moment it was shared
            values_added: A list of Value objects (metadata describing the structure of shared data) to be added to the
                feed. These may be created via the create_value helper
            values_deleted: A list of Value objects to be removed from the feed
            props_added: A list of semantic properties to be added to the feed
            props_deleted: A list of semantic properties to be removed from the feed
            props_keys_deleted: A list of any property keys for which all values should be removed from the feed
            clear_all_props: Whether or not to remove all semantic properties from the feed
            headers: optional request headers

        Returns: Response object confirming the IDs of the twin and feed being updated
        """
        req = feed_pb2.UpdateFeedRequest(
            headers=headers or create_headers(),
            args=feed_pb2.UpdateFeedRequest.Arguments(
                feedId=feed_pb2.FeedID(id=feed_id, twinId=twin_did)
            ),
            payload=feed_pb2.UpdateFeedRequest.Payload(
                storeLast=BoolValue(value=store_last),
                values=common_pb2.Values(added=values_added, deletedByLabel=values_deleted),
                properties=common_pb2.PropertyUpdate(
                    added=props_added, deleted=props_deleted, deletedByKey=props_keys_deleted,
                    clearedAll=clear_all_props
                )
            )
        )
        return self.stub.UpdateFeed(req)

    def share_feed_data(
            self,
            twin_did: str,
            feed_id: str,
            data: dict,
            occurred_at: typing.Optional[int] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> feed_pb2.ShareFeedDataResponse:
        """Share data to a feed

        Args:
            twin_did: Decentralized Identifier of the twin providing the feed
            feed_id: A string identifying the feed that is unique to its twin
            data: A dictionary with keys matching labels of the metadata Value objects associated with this feed,
            and values representing their status at the given time
            occurred_at: The time at which this data was captured in seconds since the epoch, defaulting to now
            headers: optional request headers

        Returns: Response object bearing no payload
        """
        req = feed_pb2.ShareFeedDataRequest(
            headers=headers or create_headers(),
            args=feed_pb2.ShareFeedDataRequest.Arguments(
                feedId=feed_pb2.FeedID(id=feed_id, twinId=twin_did)
            ),
            payload=feed_pb2.ShareFeedDataRequest.Payload(sample=common_pb2.FeedData(
                occurredAt=Timestamp(seconds=occurred_at if occurred_at else int(time.time())),
                mime="text/json",
                data=bytes(json.dumps(data), 'utf-8'))),
        )
        return self.stub.ShareFeedData(req)

    def list_all_feeds(
            self,
            twin_did: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> feed_pb2.ListAllFeedsResponse:
        """List all feeds provided by a given twin

        Args:
            twin_did: Decentralized Identifier for the twin whose feeds are to be listed
            headers: optional request headers

        Returns: Response object with attribute 'feeds', a list of Feed objects with id and twinId attributes
        """
        req = feed_pb2.ListAllFeedsRequest(
            headers=headers or create_headers(),
            args=feed_pb2.ListAllFeedsRequest.Arguments(twinId=common_pb2.TwinID(id=twin_did))
        )
        return self.stub.ListAllFeeds(req)

    def describe_feed(
            self,
            twin_did: str,
            feed_id: str,
            remote_host_id: typing.Optional[str] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> feed_pb2.DescribeFeedResponse:
        """
        Describes the feed identified by the given twin and feed IDs, listing its values, properties, and whether its
            last shared data is stored
        Args:
            twin_did: Decentralized Identifier for the twin exposing the feed in question
            feed_id: A string identifying the feed that is unique to its twin
            remote_host_id: ID of the remote host on which the twin can be found (None if local)
            headers: optional request headers

        Returns: Response object describing the feed
        """
        req = feed_pb2.DescribeFeedRequest(
            headers=headers or create_headers(),
            args=feed_pb2.DescribeFeedRequest.Arguments(
                feedId=feed_pb2.FeedID(id=feed_id, twinId=twin_did, hostId=remote_host_id)),
        )
        return self.stub.DescribeFeed(req)
