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

from iotics.api import common_pb2
from iotics.api import feed_pb2
from iotics.api import input_pb2
from iotics.api import twin_pb2
from iotics.api import twin_pb2_grpc
from .base import ApiBase
from .helpers import create_headers, PER_PAGE_LIMIT


class TwinApi(ApiBase):
    stub_class = twin_pb2_grpc.TwinAPIStub
    stub: twin_pb2_grpc.TwinAPIStub

    def create_twin(
            self,
            twin_did: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> twin_pb2.CreateTwinResponse:
        """Creates a twin with the given DID, which should be created using the get_did method of your chosen
        authenticator

        Args:
            twin_did: Decentralized Identifier uniquely specifying the twin
            headers: optional request headers

        Returns: Response object confirming the Twin ID
        """
        req = twin_pb2.CreateTwinRequest(
            headers=headers or create_headers(),
            payload=twin_pb2.CreateTwinRequest.Payload(id=twin_did)
        )
        return self.stub.CreateTwin(req)

    def describe_twin(
            self,
            twin_did: str,
            remote_host_id: typing.Optional[str] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> twin_pb2.DescribeTwinResponse:
        """Describes the twin with the given DID, listing its location, properties, and feeds

        Args:
            twin_did: Decentralized Identifier uniquely specifying the twin
            remote_host_id: ID of the remote host on which the twin can be found (None if local)
            headers: optional request headers

        Returns: Response object describing the twin
        """

        req = twin_pb2.DescribeTwinRequest(
            headers=headers or create_headers(),
            args=twin_pb2.DescribeTwinRequest.Arguments(
                twinId=common_pb2.TwinID(id=twin_did, hostId=remote_host_id)),
        )
        return self.stub.DescribeTwin(req)

    def delete_twin(
            self,
            twin_did: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> twin_pb2.DeleteTwinResponse:
        """Deletes the twin with the given DID

        Args:
            twin_did: Decentralized Identifier uniquely specifying the twin
            headers: optional request headers

        Returns: Response object confirming the DID of the deleted twin
        """

        req = twin_pb2.DeleteTwinRequest(
            headers=headers or create_headers(),
            args=twin_pb2.DeleteTwinRequest.Arguments(twinId=common_pb2.TwinID(id=twin_did)))
        return self.stub.DeleteTwin(req)

    def list_twins(self, 
                   page:int = 0,
                   headers: typing.Optional[common_pb2.Headers] = None
    ) -> twin_pb2.ListAllTwinsResponse:
        """Lists all local twins visible to the user making the request

        Args:
            page: Used to request offsetted results, as responses contain only up to `PER_PAGE_LIMIT` results per request.
            headers: optional request headers

        Returns: Response object listing twins with their location and properties
        """
        
        req = twin_pb2.ListAllTwinsRequest(
            range=common_pb2.Range(
                limit=common_pb2.Limit(value=PER_PAGE_LIMIT),
                offset=common_pb2.Offset(value=PER_PAGE_LIMIT * page)
            ),
            headers=headers or create_headers())
        return self.stub.ListAllTwins(req)

    def update_twin(
            self,
            twin_did: str,
            location: typing.Optional[common_pb2.GeoLocation] = None,
            props_added: typing.Optional[list] = None,
            props_deleted: typing.Optional[list] = None,
            props_keys_deleted: typing.Optional[list] = None,
            props_clear_all: bool = False,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> twin_pb2.UpdateTwinResponse:
        """Update a twin to have the given location, and/or properties. Arguments omitted will not have
        their values updated
        Args:
            twin_did: Decentralized Identifier of the twin to update
            location: The new GeoLocation for the twin, created from lat/lon values using the create_location helper
            props_added: A list of semantic properties to be added to the twin, created using the create_property helper
            props_deleted: A list of semantic properties to be removed from the twin
            props_keys_deleted: A list of any property keys for which all values should be removed from the twin
            props_clear_all: Whether or not to clear all properties from the twin
            headers: optional request headers

        Returns: Response object confirming the ID of the twin that was updated
        """

        req = twin_pb2.UpdateTwinRequest(
            headers=headers or create_headers(),
            args=twin_pb2.UpdateTwinRequest.Arguments(twinId=common_pb2.TwinID(id=twin_did)),
            payload=twin_pb2.UpdateTwinRequest.Payload(
                location=twin_pb2.GeoLocationUpdate(location=location) if location else None,
                properties=common_pb2.PropertyUpdate(
                    added=props_added,
                    deleted=props_deleted,
                    deletedByKey=props_keys_deleted,
                    clearedAll=props_clear_all
                )
            ))
        return self.stub.UpdateTwin(req)

    def upsert_twin(
            self,
            twin_did: str,
            location: typing.Optional[common_pb2.GeoLocation] = None,
            properties: typing.Optional[typing.Iterable[common_pb2.Property]] = None,
            feeds: typing.Optional[typing.Iterable[feed_pb2.UpsertFeedWithMeta]] = None,
            inputs: typing.Optional[typing.Iterable[input_pb2.UpsertInputWithMeta]] = None,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> twin_pb2.UpsertTwinResponse:
        """Upserts a twin with the given details, ie, the given ID will specify a twin with these details regardless of
        whether a twin previously existed with this ID. Any arguments omitted will become absent or given default values

        Args:
            twin_did: Decentralized Identifier of the twin to upsert
            location: The GeoLocation for the twin, created from lat/lon values using the create_location helper
            properties: A list of semantic properties providing further information about the twin, created using the
                create_property helper
            feeds: A list of feeds on which the twin may share real-time data, created using the create_feed_with_meta
                helper
            inputs: A list of inputs on which the twin may receive messages
            headers: optional request headers

        Returns: Response object confirming the ID of the twin that was upserted
        """

        req = twin_pb2.UpsertTwinRequest(
            headers=headers or create_headers(),
            payload=twin_pb2.UpsertTwinRequest.Payload(
                twinId=common_pb2.TwinID(id=twin_did),
                location=location,
                properties=properties,
                feeds=feeds,
                inputs=inputs,
            )
        )
        return self.stub.UpsertTwin(req)
