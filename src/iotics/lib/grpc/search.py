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
from google.protobuf.wrappers_pb2 import StringValue

from iotics.api import common_pb2
from iotics.api import search_pb2
from iotics.api import search_pb2_grpc
from iotics.lib.grpc.helpers import create_headers
from iotics.lib.grpc.base import ApiBase

PER_PAGE_LIMIT = 100


class SearchApi(ApiBase):
    stub_class = search_pb2_grpc.SearchAPIStub
    stub: search_pb2_grpc.SearchAPIStub

    @staticmethod
    def get_search_payload(
        text: typing.Optional[str] = None,
        location: typing.Optional[typing.Tuple[float, float, float]] = None,
        properties: typing.Optional[list] = None,
        response_type: search_pb2.ResponseType = search_pb2.ResponseType.MINIMAL
    ) -> search_pb2.SearchRequest.Payload:
        """Provides a correctly instantiated search request payload.

        Args:
            text: Filter results by text.
            location: Filter results for given geographic coordinates and radius.
            properties: Filter results for given metadata properties.
            response_type: Used for results in search responses.

        Returns: Payload object.
        """
        text = text and StringValue(value=text)
        location = location and common_pb2.GeoCircle(
            location=common_pb2.GeoLocation(lat=location[0], lon=location[1]),
            radiusKm=location[2]
        )
        payload = search_pb2.SearchRequest.Payload(
            responseType=response_type,
            filter=search_pb2.SearchRequest.Payload.Filter(text=text, location=location, properties=properties),
        )
        return payload

    def search_iter(
        self,
        client_app_id: str,
        payload: search_pb2.SearchRequest.Payload,
        scope: common_pb2.Scope = common_pb2.Scope.LOCAL,
        lang: typing.Optional[str] = None,
        timeout=3,
    ) -> typing.Iterator[search_pb2.SearchResponse]:
        """Searches IOTICSpace using an iterator.

        Args:
            client_app_id: Used to bind together and identify search requests and responses.
            payload: Contains filters, used to narrow results.
            scope: Used to filter search responses either to local IOTICSpace only or all visible IOTICSpaces.
            lang: The language to conduct text searches in
            timeout: Time after which the search iterator will stop blocking and listening for more replies.

        Returns: Search responses with results.
        """
        response_listener = self.get_response_listener(client_app_id, timeout=timeout)
        self.dispatch_request(client_app_id, payload, scope, lang)
        last_requested_page = 0
        try:
            for response in response_listener:
                current_page = int(response.headers.clientRef.split('_page')[1])
                if len(response.payload.twins) >= PER_PAGE_LIMIT and current_page >= last_requested_page:
                    last_requested_page += 1
                    self.dispatch_request(client_app_id, payload, scope, lang, page=current_page + 1)
                # Do not yield redundant responses if paginated search is called with global scope.
                if response.payload.twins or current_page == 0:
                    yield response
        except grpc._channel._MultiThreadedRendezvous as err:
            if err.code() != grpc.StatusCode.DEADLINE_EXCEEDED:
                raise

    def get_response_listener(self, client_app_id: str, timeout: int):
        """Initialises an iterator that listens for search request replies.

        Note: This function must be called before `dispatch_request` otherwise search responses may be lost.

        Args:
            client: Used to open a stream to receive search replies from IOTICSpace.
            client_app_id: A value that must match with the search request dispatched value.
            timeout: Time after which blocking operations on the response listener will be cancelled.

        Returns: Search results iterator with extra blocking (e.g. `time_remaining`) and non-blocking (e.g. `code`)
        methods.
        """
        sub_headers = common_pb2.SubscriptionHeaders(clientAppId=client_app_id, transactionRef=[client_app_id])
        # Define type here to avoid: `TypeError: 'ABCMeta' object is not subscriptable`.
        search_responses: grpc._channel._MultiThreadedRendezvous[search_pb2.SearchResponse] = \
            self.stub.ReceiveAllSearchResponses(sub_headers, timeout=timeout)
        return search_responses

    def dispatch_request(
        self,
        client_app_id: str,
        payload: search_pb2.SearchRequest.Payload,
        scope: common_pb2.Scope = common_pb2.Scope.LOCAL,
        lang: typing.Optional[str] = None,
        page: int = 0
    ) -> None:
        """Sends a (paginated) search request.

        Note: This function must be called after `get_response_listener` otherwise search responses may be lost.

        Args:
            client_app_id: A value used to identify replies for given search.
            payload: Contains filters, used to narrow results.
            scope: Used to filter search responses either to local IOTICSpace only or all visible IOTICSpaces.
            lang: The language to conduct text searches in
            page: Used to request offsetted results, as responses contain only up to `PER_PAGE_LIMIT` results per a
            request.
        """
        client_ref = f'{client_app_id}_page{page}'
        headers = create_headers(client_ref=client_ref, client_app_id=client_app_id)
        result_range = common_pb2.Range(
            limit=common_pb2.Limit(value=PER_PAGE_LIMIT),
            offset=common_pb2.Offset(value=PER_PAGE_LIMIT * page)
        )
        if lang:
            lang = StringValue(value=lang)
        request = search_pb2.SearchRequest(headers=headers, scope=scope, lang=lang, payload=payload, range=result_range)
        self.stub.DispatchSearchRequest(request)
