# Copyright © 2024 IOTIC LABS LTD. info@iotics.com
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

from iotics.api import common_pb2
from iotics.api import circle_pb2
from iotics.api import circle_pb2_grpc
from .base import ApiBase
from .helpers import create_headers, PER_PAGE_LIMIT


class CircleAPI(ApiBase):
    stub_class = circle_pb2_grpc.CircleAPIStub
    stub: circle_pb2_grpc.CircleAPIStub

    def describe_circle(
            self,
            circle_did: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> circle_pb2.DescribeCircleResponse:
        """Describes the circle with the given DID, listing its properties

        Args:
            circle_did: Decentralized Identifier uniquely specifying the circle
            headers: optional request headers

        Returns: Response object describing the circle
        """

        req = circle_pb2.DescribeCircleRequest(
            headers=headers or create_headers(),
            args=circle_pb2.DescribeCircleRequest.Arguments(
                circleId=circle_pb2.CircleID(id=circle_did)),
        )
        return self.stub.DescribeCircle(req)

    def delete_circle(
            self,
            circle_did: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> circle_pb2.DeleteCircleResponse:
        """Deletes the circle with the given DID

        Args:
            circle_did: Decentralized Identifier uniquely specifying the circle
            headers: optional request headers

        Returns: Response object confirming the DID of the deleted circle
        """

        req = circle_pb2.DeleteCircleRequest(
            headers=headers or create_headers(),
            args=circle_pb2.DeleteCircleRequest.Arguments(circleId=circle_pb2.CircleID(id=circle_did)))
        return self.stub.DeleteCircle(req)

    def list_circles(self,
                   page:int = 0,
                   headers: typing.Optional[common_pb2.Headers] = None
    ) -> circle_pb2.ListAllCirclesResponse:
        """Lists all local circles visible to the user making the request

        Args:
            page: Used to request offsetted results, as responses contain only up to `PER_PAGE_LIMIT` results per request.
            headers: optional request headers

        Returns: Response object listing circles with their location and properties
        """
        
        req = circle_pb2.ListAllCirclesRequest(
            range=common_pb2.Range(
                limit=common_pb2.Limit(value=PER_PAGE_LIMIT),
                offset=common_pb2.Offset(value=PER_PAGE_LIMIT * page)
            ),
            headers=headers or create_headers())
        return self.stub.ListAllCircles(req)

    def upsert_circle(
            self,
            circle_did: str,
            properties: typing.Optional[typing.Iterable[common_pb2.Property]] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> circle_pb2.UpsertCircleResponse:
        """Upserts a circle with the given details, ie, the given ID will specify a circle with these details regardless of
        whether a circle previously existed with this ID. Any arguments omitted will become absent or given default values

        Args:
            circle_did: Decentralized Identifier of the circle to upsert
            properties: A list of semantic properties providing further information about the circle, created using the
                create_property helper
            headers: optional request headers

        Returns: Response object confirming the ID of the circle that was upserted
        """

        req = circle_pb2.UpsertCircleRequest(
            headers=headers or create_headers(),
            payload=circle_pb2.UpsertCircleRequest.Payload(
                circleId=circle_pb2.CircleID(id=circle_did),
                properties=properties,
            )
        )
        return self.stub.UpsertCircle(req)
