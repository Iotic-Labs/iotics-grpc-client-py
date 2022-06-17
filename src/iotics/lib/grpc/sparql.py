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

from .base import ApiBase
from .helpers import create_headers
from iotics.api.meta_pb2_grpc import MetaAPIStub as SparqlApiStub
from iotics.api import meta_pb2
from iotics.api import common_pb2


class SparqlApi(ApiBase):
    stub_class = SparqlApiStub
    stub: SparqlApiStub

    def sparql_query(
            self,
            query: str,
            result_content_type: meta_pb2.SparqlResultType = meta_pb2.SparqlResultType.SPARQL_JSON,
            scope: common_pb2.Scope = common_pb2.Scope.LOCAL,
            timeout: int = 5,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> meta_pb2.SparqlQueryResponse:
        """Submit a SPARQL query to the network of IOTIC Hosts and receive a chunked stream of responses

        Args:
            query: the SPARQL query to submit
            result_content_type: Choice of response type among SPARQL_JSON, SPARQL_XML, SPARQL_CSV, RDF_TURTLE, RDF_XML,
                and RDF_NTRIPLES
            scope: GLOBAL or LOCAL, whether to submit this query to only the local host or all hosts on the network
            timeout: How long to wait for responses, in seconds
            headers: optional request headers

        Returns: A result chunk with details of what host it came from, where it is in that host's sequence, and whether
        it is the last chunk
        """
        req = meta_pb2.SparqlQueryRequest(
            headers=headers or create_headers(),
            payload=meta_pb2.SparqlQueryRequest.Payload(
                query=query.encode('utf-8'),
                resultContentType=result_content_type
            ), scope=scope
        )
        # Define type here to avoid: `TypeError: 'ABCMeta' object is not subscriptable`.
        chunks: grpc._channel._MultiThreadedRendezvous[meta_pb2.SparqlQueryResponse] = \
            self.stub.SparqlQuery(req, timeout=timeout)
        return chunks

    def sparql_update(
            self,
            update: str,
            headers: typing.Optional[common_pb2.Headers] = None
    ) -> meta_pb2.SparqlUpdateResponse:
        """Add triples to the custom-public graph of the Fuseki database on the local host.

        Args:
            update: the update written in SPARQL
            headers: optional request headers

        Returns: Response object
        """
        req = meta_pb2.SparqlUpdateRequest(
            headers=headers or create_headers(),
            payload=meta_pb2.SparqlUpdateRequest.Payload(update=update.encode('utf-8'))
        )
        return self.stub.SparqlUpdate(req)
