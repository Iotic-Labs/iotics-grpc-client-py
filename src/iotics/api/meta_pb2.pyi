"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2019-2022 Iotic Labs Ltd. All rights reserved.

Iotics Web protocol definitions (meta)
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.rpc.status_pb2
import iotics.api.common_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SparqlResultType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SparqlResultTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SparqlResultType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SPARQL_JSON: _SparqlResultType.ValueType  # 0
    """Applicable to SELECT/ASK (SPARQL 1.1 Query Results JSON Format)"""
    SPARQL_XML: _SparqlResultType.ValueType  # 1
    """Applicable to SELECT/ASK (SPARQL 1.1 Query Results XML Format)"""
    SPARQL_CSV: _SparqlResultType.ValueType  # 2
    """Applicable to SELECT/ASK (SPARQL 1.1. Query Results CSV Format)"""
    RDF_TURTLE: _SparqlResultType.ValueType  # 3
    """Applicable to CONSTRUCT/DESCRIBE (Terse RDF Triple Language)"""
    RDF_XML: _SparqlResultType.ValueType  # 4
    """Applicable to CONSTRUCT/DESCRIBE (RDF 1.1 XML)"""
    RDF_NTRIPLES: _SparqlResultType.ValueType  # 5
    """Applicable to CONSTRUCT/DESCRIBE (RDF 1.1 N-Triples)"""

class SparqlResultType(_SparqlResultType, metaclass=_SparqlResultTypeEnumTypeWrapper):
    """SparqlResultType defines the result content types for SPARQL requests. Note that applicable content types depend on
    the type of query.
    """

SPARQL_JSON: SparqlResultType.ValueType  # 0
"""Applicable to SELECT/ASK (SPARQL 1.1 Query Results JSON Format)"""
SPARQL_XML: SparqlResultType.ValueType  # 1
"""Applicable to SELECT/ASK (SPARQL 1.1 Query Results XML Format)"""
SPARQL_CSV: SparqlResultType.ValueType  # 2
"""Applicable to SELECT/ASK (SPARQL 1.1. Query Results CSV Format)"""
RDF_TURTLE: SparqlResultType.ValueType  # 3
"""Applicable to CONSTRUCT/DESCRIBE (Terse RDF Triple Language)"""
RDF_XML: SparqlResultType.ValueType  # 4
"""Applicable to CONSTRUCT/DESCRIBE (RDF 1.1 XML)"""
RDF_NTRIPLES: SparqlResultType.ValueType  # 5
"""Applicable to CONSTRUCT/DESCRIBE (RDF 1.1 N-Triples)"""
global___SparqlResultType = SparqlResultType

@typing_extensions.final
class ExplorerRequest(google.protobuf.message.Message):
    """ExplorerRequest - Deprecated. Use SparqlQueryRequest instead."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """Explorer request payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RESULTCONTENTTYPE_FIELD_NUMBER: builtins.int
        KEYWORD_FIELD_NUMBER: builtins.int
        resultContentType: global___SparqlResultType.ValueType
        """The desired result content type. Note that choosing an invalid result type for the type of query will result in
        an error status reported in the response. (See SparqlResultType for valid content-query type combinations.)
        """
        keyword: builtins.str
        """keyword defines the search term associated to the explorer request."""
        def __init__(
            self,
            *,
            resultContentType: global___SparqlResultType.ValueType = ...,
            keyword: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["keyword", b"keyword", "resultContentType", b"resultContentType"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Explorer request headers"""
    scope: iotics.api.common_pb2.Scope.ValueType
    """Explorer request scope"""
    @property
    def payload(self) -> global___ExplorerRequest.Payload:
        """Explorer request payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        scope: iotics.api.common_pb2.Scope.ValueType = ...,
        payload: global___ExplorerRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload", "scope", b"scope"]) -> None: ...

global___ExplorerRequest = ExplorerRequest

@typing_extensions.final
class SparqlQueryRequest(google.protobuf.message.Message):
    """SparqlQueryRequest describes a SPARQL query."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """SPARQL query request payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RESULTCONTENTTYPE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        resultContentType: global___SparqlResultType.ValueType
        """The desired result content type. Note that choosing an invalid result type for the type of query will result in
        an error status reported in the response. (See SparqlResultType for valid content-query type combinations.)
        """
        query: builtins.bytes
        """A UTF8-encoded SPARQL 1.1 query"""
        def __init__(
            self,
            *,
            resultContentType: global___SparqlResultType.ValueType = ...,
            query: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["query", b"query", "resultContentType", b"resultContentType"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    SCOPE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """SPARQL query request headers"""
    scope: iotics.api.common_pb2.Scope.ValueType
    """SPARQL query request scope"""
    @property
    def payload(self) -> global___SparqlQueryRequest.Payload:
        """SPARQL query request payload"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        scope: iotics.api.common_pb2.Scope.ValueType = ...,
        payload: global___SparqlQueryRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload", "scope", b"scope"]) -> None: ...

global___SparqlQueryRequest = SparqlQueryRequest

@typing_extensions.final
class SparqlQueryResponse(google.protobuf.message.Message):
    """SparqlQueryResponse is a part of a result for a SPARQL query request. Multiple chunks form a complete result. Related
    chunks can be identified by a combination of:
    - The hostId
    - Client reference (in headers, set by caller)
    - Chunk sequence number
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """Payload of the query result chunk"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        HOSTID_FIELD_NUMBER: builtins.int
        SEQNUM_FIELD_NUMBER: builtins.int
        LAST_FIELD_NUMBER: builtins.int
        STATUS_FIELD_NUMBER: builtins.int
        CONTENTTYPE_FIELD_NUMBER: builtins.int
        RESULTCHUNK_FIELD_NUMBER: builtins.int
        hostId: builtins.str
        """Result host identifier. Indicates from which host this result chunk came from. For a local result, this field
        will be unset.
        """
        seqNum: builtins.int
        """Position of a chunk in result from a given host (and request). The first chunk has a sequence number of 0."""
        last: builtins.bool
        """Indicates whether this is the last chunk from a given host, for a specific request. Results for different
        requests can be identified by setting a unique clientRef in the request headers.
        """
        @property
        def status(self) -> google.rpc.status_pb2.Status:
            """Result error status (only applicable to local results). If set, this will
            indicate a problem with running the query (e.g. invalid syntax or content type) as opposed to a more general
            issue (in which case the standard gRPC error mechanism will be used and the stream terminated).
            """
        contentType: global___SparqlResultType.ValueType
        """Content type of the result."""
        resultChunk: builtins.bytes
        """Query result chunk, encoded according to actualType.
        Note that:
        - The maximum size of each chunk is host-specific.
        """
        def __init__(
            self,
            *,
            hostId: builtins.str = ...,
            seqNum: builtins.int = ...,
            last: builtins.bool = ...,
            status: google.rpc.status_pb2.Status | None = ...,
            contentType: global___SparqlResultType.ValueType = ...,
            resultChunk: builtins.bytes = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["status", b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["contentType", b"contentType", "hostId", b"hostId", "last", b"last", "resultChunk", b"resultChunk", "seqNum", b"seqNum", "status", b"status"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """Headers for the query result. clientRef within can be used to identify which query the result applies to."""
    @property
    def payload(self) -> global___SparqlQueryResponse.Payload:
        """SPARQL query result chunk payload."""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___SparqlQueryResponse.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___SparqlQueryResponse = SparqlQueryResponse

@typing_extensions.final
class SparqlUpdateRequest(google.protobuf.message.Message):
    """Performs a SPARQL update against custom metadata only."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Payload(google.protobuf.message.Message):
        """SPARQL update request payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        UPDATE_FIELD_NUMBER: builtins.int
        update: builtins.bytes
        """A UTF8-encoded SPARQL 1.1 update"""
        def __init__(
            self,
            *,
            update: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["update", b"update"]) -> None: ...

    HEADERS_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """SPARQL update request headers"""
    @property
    def payload(self) -> global___SparqlUpdateRequest.Payload:
        """SPARQL update request payload."""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
        payload: global___SparqlUpdateRequest.Payload | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers", "payload", b"payload"]) -> None: ...

global___SparqlUpdateRequest = SparqlUpdateRequest

@typing_extensions.final
class SparqlUpdateResponse(google.protobuf.message.Message):
    """Response of the SPARQL update request."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADERS_FIELD_NUMBER: builtins.int
    @property
    def headers(self) -> iotics.api.common_pb2.Headers:
        """SPARQL update response headers"""
    def __init__(
        self,
        *,
        headers: iotics.api.common_pb2.Headers | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["headers", b"headers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["headers", b"headers"]) -> None: ...

global___SparqlUpdateResponse = SparqlUpdateResponse
