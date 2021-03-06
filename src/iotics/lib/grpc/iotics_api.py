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

from iotics.lib.grpc.auth import AuthInterface
from iotics.lib.grpc.base import ApiBase
from iotics.lib.grpc.feeds import FeedApi
from iotics.lib.grpc.helpers import get_channel
from iotics.lib.grpc.interest import InterestApi
from iotics.lib.grpc.search import SearchApi
from iotics.lib.grpc.sparql import SparqlApi
from iotics.lib.grpc.twins import TwinApi


class IoticsApi:
    def __init__(self, auth, channel=None):
        self._auth: AuthInterface = auth
        self._channel: typing.Optional[grpc.Channel] = channel
        self._twin_api: typing.Optional[TwinApi] = None
        self._feed_api: typing.Optional[FeedApi] = None
        self._search_api: typing.Optional[SearchApi] = None
        self._interest_api: typing.Optional[InterestApi] = None
        self._sparql_api: typing.Optional[SparqlApi] = None

        self.create_feed = self.feed_api.create_feed
        self.delete_feed = self.feed_api.delete_feed
        self.update_feed = self.feed_api.update_feed
        self.share_feed_data = self.feed_api.share_feed_data
        self.list_all_feeds = self.feed_api.list_all_feeds
        self.describe_feed = self.feed_api.describe_feed
        self.fetch_interests = self.interest_api.fetch_interests
        self.fetch_last_stored = self.interest_api.fetch_last_stored
        self.get_search_payload = self.search_api.get_search_payload
        self.search_iter = self.search_api.search_iter
        self.sparql_query = self.sparql_api.sparql_query
        self.sparql_update = self.sparql_api.sparql_update
        self.create_twin = self.twin_api.create_twin
        self.describe_twin = self.twin_api.describe_twin
        self.delete_twin = self.twin_api.delete_twin
        self.list_twins = self.twin_api.list_twins
        self.update_twin = self.twin_api.update_twin
        self.upsert_twin = self.twin_api.upsert_twin

    @property
    def auth(self) -> AuthInterface:
        return self._auth

    @property
    def channel(self) -> grpc.Channel:
        if not self._channel:
            self._channel = get_channel(self._auth)
        return self._channel

    @property
    def twin_api(self) -> TwinApi:
        if not self._twin_api:
            self._twin_api = TwinApi(self._auth, self.channel)
        return self._twin_api

    @property
    def feed_api(self) -> FeedApi:
        if not self._feed_api:
            self._feed_api = FeedApi(self._auth, self.channel)
        return self._feed_api

    @property
    def interest_api(self) -> InterestApi:
        if not self._interest_api:
            self._interest_api = InterestApi(self._auth, self.channel)
        return self._interest_api

    @property
    def search_api(self) -> SearchApi:
        if not self._search_api:
            self._search_api = SearchApi(self._auth, self.channel)
        return self._search_api

    @property
    def sparql_api(self) -> SparqlApi:
        if not self._sparql_api:
            self._sparql_api = SparqlApi(self._auth, self.channel)
        return self._sparql_api

    def update_auth(self, auth, channel=None):
        self._auth = auth
        self.update_channel(channel)

    def update_channel(self, channel: typing.Optional[grpc.Channel] = None):
        self._channel = channel or get_channel(self._auth)
        for api in self._apis():
            if api:
                self._update_api(api, channel)

    def _update_api(self, api: ApiBase, channel: grpc.Channel):
        if isinstance(api, TwinApi):
            self._twin_api = TwinApi(self._auth, channel)
        elif isinstance(api, FeedApi):
            self._feed_api = FeedApi(self._auth, channel)
        elif isinstance(api, InterestApi):
            self._interest_api = InterestApi(self._auth, channel)
        elif isinstance(api, SearchApi):
            self._search_api = SearchApi(self._auth, channel)
        elif isinstance(api, SparqlApi):
            self._sparql_api = SparqlApi(self._auth, channel)

    def _apis(self):
        return [
            self._twin_api,
            self._feed_api,
            self._search_api,
            self._interest_api,
            self._sparql_api
        ]
