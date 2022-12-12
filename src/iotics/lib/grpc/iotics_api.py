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
from iotics.lib.grpc.input import InputApi
from iotics.lib.grpc.interest import InterestApi
from iotics.lib.grpc.search import SearchApi
from iotics.lib.grpc.sparql import SparqlApi
from iotics.lib.grpc.twins import TwinApi
from iotics.lib.grpc.host import HostApi


class IoticsApi:
    def __init__(self, auth, channel=None):
        self._auth: AuthInterface = auth
        self._channel: typing.Optional[grpc.Channel] = channel
        self._twin_api: typing.Optional[TwinApi] = None
        self._feed_api: typing.Optional[FeedApi] = None
        self._input_api: typing.Optional[InputApi] = None
        self._search_api: typing.Optional[SearchApi] = None
        self._interest_api: typing.Optional[InterestApi] = None
        self._sparql_api: typing.Optional[SparqlApi] = None
        self._host_api: typing.Optional[HostApi] = None
        self._local_host_id: str = None

        self._initialise_twin_api()
        self._initialise_feed_api()
        self._initialise_input_api()
        self._initialise_interest_api()
        self._initialise_search_api()
        self._initialise_sparql_api()
        self._initialise_host_api()

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
            self._initialise_twin_api()
        return self._twin_api

    @property
    def feed_api(self) -> FeedApi:
        if not self._feed_api:
            self._initialise_feed_api()
        return self._feed_api

    @property
    def input_api(self) -> InputApi:
        if not self._input_api:
            self._initialise_input_api()
        return self._input_api

    @property
    def interest_api(self) -> InterestApi:
        if not self._interest_api:
            self._initialise_interest_api()
        return self._interest_api

    @property
    def search_api(self) -> SearchApi:
        if not self._search_api:
            self._initialise_search_api()
        return self._search_api

    @property
    def sparql_api(self) -> SparqlApi:
        if not self._sparql_api:
            self._initialise_sparql_api()
        return self._sparql_api

    @property
    def host_api(self) -> HostApi:
        if not self._host_api:
            self._initialise_host_api()
        return self._host_api

    def update_auth(self, auth, channel=None):
        self._auth = auth
        self.update_channel(channel)

    def update_channel(self, channel: typing.Optional[grpc.Channel] = None):
        self._channel = channel or get_channel(self._auth)
        for api in self._apis():
            if api:
                self._update_api(api)

    def _update_api(self, api: ApiBase):
        if isinstance(api, TwinApi):
            self._initialise_twin_api()
        elif isinstance(api, FeedApi):
            self._initialise_feed_api()
        elif isinstance(api, InputApi):
            self._initialise_input_api()
        elif isinstance(api, InterestApi):
            self._initialise_interest_api()
        elif isinstance(api, SearchApi):
            self._initialise_search_api()
        elif isinstance(api, SparqlApi):
            self._initialise_sparql_api()
        elif isinstance(api, HostApi):
            self._initialise_host_api()

    def _initialise_twin_api(self):
        self._twin_api = TwinApi(self._auth, self._channel)
        self.create_twin = self.twin_api.create_twin
        self.describe_twin = self.twin_api.describe_twin
        self.delete_twin = self.twin_api.delete_twin
        self.list_twins = self.twin_api.list_twins
        self.update_twin = self.twin_api.update_twin
        self.upsert_twin = self.twin_api.upsert_twin

    def _initialise_feed_api(self):
        self._feed_api = FeedApi(self._auth, self._channel)
        self.create_feed = self.feed_api.create_feed
        self.delete_feed = self.feed_api.delete_feed
        self.update_feed = self.feed_api.update_feed
        self.share_feed_data = self.feed_api.share_feed_data
        self.list_all_feeds = self.feed_api.list_all_feeds
        self.describe_feed = self.feed_api.describe_feed

    def _initialise_input_api(self):
        self._input_api = InputApi(self._auth, self._channel)
        self.describe_input = self.input_api.describe_input
        self.delete_input = self.input_api.delete_input
        self.receive_input_messages = self.input_api.receive_input_messages

    def _initialise_interest_api(self):
        self._interest_api = InterestApi(self._auth, self._channel)
        self.send_input_message = self.interest_api.send_input_message
        self.fetch_interests = self.interest_api.fetch_interests
        self.fetch_last_stored = self.interest_api.fetch_last_stored

    def _initialise_search_api(self):
        self._search_api = SearchApi(self._auth, self._channel)
        self.get_search_payload = self.search_api.get_search_payload
        self.search_iter = self.search_api.search_iter

    def _initialise_sparql_api(self):
        self._sparql_api = SparqlApi(self._auth, self._channel)
        self.sparql_query = self.sparql_api.sparql_query
        self.sparql_update = self.sparql_api.sparql_update

    def _initialise_host_api(self):
        self._host_api = HostApi(self._auth, self._channel)
        self.get_local_host_id = self.host_api.get_local_host_id

    def _apis(self):
        return [
            self._twin_api,
            self._feed_api,
            self._input_api,
            self._search_api,
            self._interest_api,
            self._sparql_api,
            self._host_api,
        ]
