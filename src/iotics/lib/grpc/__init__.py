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

from iotics.api.common_pb2 import Scope, Visibility
from iotics.api.feed_pb2 import CreateFeedResponse, DeleteFeedResponse, DescribeFeedResponse, ListAllFeedsResponse, \
    ShareFeedDataResponse, UpdateFeedResponse
from iotics.api.interest_pb2 import FetchInterestResponse
from iotics.api.search_pb2 import SearchRequest, SearchResponse
from iotics.api.meta_pb2 import SparqlQueryResponse, SparqlResultType, SparqlUpdateResponse
from iotics.api.twin_pb2 import CreateTwinResponse, DeleteTwinResponse, DescribeTwinResponse, ListAllTwinsResponse, \
    UpdateTwinResponse, UpsertTwinResponse
from iotics.lib.grpc.iotics_api import IoticsApi
from iotics.lib.grpc.feeds import FeedApi
from iotics.lib.grpc.interest import InterestApi
from iotics.lib.grpc.search import SearchApi
from iotics.lib.grpc.sparql import SparqlApi
from iotics.lib.grpc.twins import TwinApi
from iotics.lib.grpc.helpers import *

del globals()['get_channel']
