import json
import time
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import BoolValue
from .base import ApiBase
from iotics.api.feed_pb2_grpc import FeedAPIStub
from iotics.api.feed_pb2 import CreateFeedRequest, DeleteFeedRequest, UpdateFeedRequest, ShareFeedDataRequest, \
    ListAllFeedsRequest, DescribeFeedRequest, Feed
from iotics.api.common_pb2 import Headers, TwinID, HostID, FeedID, PropertyUpdate, Values, FeedData


class FeedApi(ApiBase):
    stub_class = FeedAPIStub

    def create_feed(self, twin_id, feed_id):
        req = CreateFeedRequest(
            headers=Headers(),
            args=CreateFeedRequest.Arguments(twinId=TwinID(value=twin_id)),
            payload=CreateFeedRequest.Payload(feedId=FeedID(value=feed_id))
        )
        return self.stub.CreateFeed(req)

    def delete_feed(self, twin_id, feed_id):
        req = DeleteFeedRequest(
            headers=Headers(),
            args=DeleteFeedRequest.Arguments(feed=Feed(id=FeedID(value=feed_id), twinId=TwinID(value=twin_id))),
        )
        return self.stub.DeleteFeed(req)

    def update_feed(self, twin_id, feed_id, store_last=True, values_added=None, values_deleted=None, props_added=None,
                    props_deleted=None, props_keys_deleted=None, clear_all_props=False):
        req = UpdateFeedRequest(
            headers=Headers(),
            args=UpdateFeedRequest.Arguments(feed=Feed(id=FeedID(value=feed_id), twinId=TwinID(value=twin_id))),
            payload=UpdateFeedRequest.Payload(
                storeLast=BoolValue(value=store_last),
                values=Values(added=values_added, deletedByLabel=values_deleted),
                properties=PropertyUpdate(added=props_added, deleted=props_deleted, deletedByKey=props_keys_deleted,
                                          clearedAll=clear_all_props)
            )
        )
        return self.stub.UpdateFeed(req)

    def share_feed_data(self, twin_id, feed_id, data):
        req = ShareFeedDataRequest(
            headers=Headers(),
            args=ShareFeedDataRequest.Arguments(feed=Feed(id=FeedID(value=feed_id), twinId=TwinID(value=twin_id))),
            payload=ShareFeedDataRequest.Payload(sample=FeedData(
                occurredAt=Timestamp(seconds=int(time.time())),
                mime="text/json",
                data=bytes(json.dumps(data), 'utf-8'))),
        )
        return self.stub.ShareFeedData(req)

    def list_feeds(self, twin_id):
        req = ListAllFeedsRequest(
            headers=Headers(),
            args=ListAllFeedsRequest.Arguments(twinId=TwinID(value=twin_id))
        )
        return self.stub.ListAllFeeds(req)

    def describe_feed(self, twin_id, feed_id, remote_host_id=None):
        req = DescribeFeedRequest(
            headers=Headers(),
            args=DescribeFeedRequest.Arguments(
                feed=Feed(id=FeedID(value=feed_id), twinId=TwinID(value=twin_id)),
                remoteHostId=HostID(value=remote_host_id) if remote_host_id else None)
        )
        return self.stub.DescribeFeed(req)
