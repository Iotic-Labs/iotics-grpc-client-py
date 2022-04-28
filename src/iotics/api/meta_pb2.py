# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iotics/api/meta.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from iotics.api import common_pb2 as iotics_dot_api_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='iotics/api/meta.proto',
  package='iotics.api',
  syntax='proto3',
  serialized_options=b'\n\016com.iotics.apiB\tMetaProtoP\001Z>github.com/Iotic-Labs/iotic-go-proto-qapi/iotics/api;ioticsapi\242\002\003IAX\252\002\nIotics.Api\312\002\nIotics\\Api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15iotics/api/meta.proto\x12\niotics.api\x1a\x17google/rpc/status.proto\x1a\x17iotics/api/common.proto\"\x9b\x02\n\x12SparqlQueryRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12\'\n\x05scope\x18\x02 \x01(\x0e\x32\x11.iotics.api.ScopeR\x05scope\x12@\n\x07payload\x18\x03 \x01(\x0b\x32&.iotics.api.SparqlQueryRequest.PayloadR\x07payload\x1ak\n\x07Payload\x12J\n\x11resultContentType\x18\x01 \x01(\x0e\x32\x1c.iotics.api.SparqlResultTypeR\x11resultContentType\x12\x14\n\x05query\x18\x02 \x01(\x0cR\x05query\"\x85\x03\n\x13SparqlQueryResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12\x41\n\x07payload\x18\x02 \x01(\x0b\x32\'.iotics.api.SparqlQueryResponse.PayloadR\x07payload\x1a\xfb\x01\n\x07Payload\x12\x36\n\x0cremoteHostId\x18\x01 \x01(\x0b\x32\x12.iotics.api.HostIDR\x0cremoteHostId\x12\x16\n\x06seqNum\x18\x02 \x01(\x04R\x06seqNum\x12\x12\n\x04last\x18\x03 \x01(\x08R\x04last\x12*\n\x06status\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\x12>\n\x0b\x63ontentType\x18\x05 \x01(\x0e\x32\x1c.iotics.api.SparqlResultTypeR\x0b\x63ontentType\x12 \n\x0bresultChunk\x18\x06 \x01(\x0cR\x0bresultChunk*r\n\x10SparqlResultType\x12\x0f\n\x0bSPARQL_JSON\x10\x00\x12\x0e\n\nSPARQL_XML\x10\x01\x12\x0e\n\nSPARQL_CSV\x10\x02\x12\x0e\n\nRDF_TURTLE\x10\x03\x12\x0b\n\x07RDF_XML\x10\x04\x12\x10\n\x0cRDF_NTRIPLES\x10\x05\x32]\n\x07MetaAPI\x12R\n\x0bSparqlQuery\x12\x1e.iotics.api.SparqlQueryRequest\x1a\x1f.iotics.api.SparqlQueryResponse\"\x00\x30\x01\x42}\n\x0e\x63om.iotics.apiB\tMetaProtoP\x01Z>github.com/Iotic-Labs/iotic-go-proto-qapi/iotics/api;ioticsapi\xa2\x02\x03IAX\xaa\x02\nIotics.Api\xca\x02\nIotics\\Apib\x06proto3'
  ,
  dependencies=[google_dot_rpc_dot_status__pb2.DESCRIPTOR,iotics_dot_api_dot_common__pb2.DESCRIPTOR,])

_SPARQLRESULTTYPE = _descriptor.EnumDescriptor(
  name='SparqlResultType',
  full_name='iotics.api.SparqlResultType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPARQL_JSON', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARQL_XML', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARQL_CSV', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RDF_TURTLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RDF_XML', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RDF_NTRIPLES', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=765,
  serialized_end=879,
)
_sym_db.RegisterEnumDescriptor(_SPARQLRESULTTYPE)

SparqlResultType = enum_type_wrapper.EnumTypeWrapper(_SPARQLRESULTTYPE)
SPARQL_JSON = 0
SPARQL_XML = 1
SPARQL_CSV = 2
RDF_TURTLE = 3
RDF_XML = 4
RDF_NTRIPLES = 5



_SPARQLQUERYREQUEST_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='iotics.api.SparqlQueryRequest.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultContentType', full_name='iotics.api.SparqlQueryRequest.Payload.resultContentType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resultContentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='iotics.api.SparqlQueryRequest.Payload.query', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='query', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=371,
)

_SPARQLQUERYREQUEST = _descriptor.Descriptor(
  name='SparqlQueryRequest',
  full_name='iotics.api.SparqlQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='iotics.api.SparqlQueryRequest.headers', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='headers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='iotics.api.SparqlQueryRequest.scope', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scope', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='iotics.api.SparqlQueryRequest.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SPARQLQUERYREQUEST_PAYLOAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=371,
)


_SPARQLQUERYRESPONSE_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='iotics.api.SparqlQueryResponse.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='remoteHostId', full_name='iotics.api.SparqlQueryResponse.Payload.remoteHostId', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remoteHostId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='iotics.api.SparqlQueryResponse.Payload.seqNum', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='seqNum', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last', full_name='iotics.api.SparqlQueryResponse.Payload.last', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='last', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='iotics.api.SparqlQueryResponse.Payload.status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contentType', full_name='iotics.api.SparqlQueryResponse.Payload.contentType', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultChunk', full_name='iotics.api.SparqlQueryResponse.Payload.resultChunk', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resultChunk', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=763,
)

_SPARQLQUERYRESPONSE = _descriptor.Descriptor(
  name='SparqlQueryResponse',
  full_name='iotics.api.SparqlQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='iotics.api.SparqlQueryResponse.headers', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='headers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='iotics.api.SparqlQueryResponse.payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payload', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SPARQLQUERYRESPONSE_PAYLOAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=763,
)

_SPARQLQUERYREQUEST_PAYLOAD.fields_by_name['resultContentType'].enum_type = _SPARQLRESULTTYPE
_SPARQLQUERYREQUEST_PAYLOAD.containing_type = _SPARQLQUERYREQUEST
_SPARQLQUERYREQUEST.fields_by_name['headers'].message_type = iotics_dot_api_dot_common__pb2._HEADERS
_SPARQLQUERYREQUEST.fields_by_name['scope'].enum_type = iotics_dot_api_dot_common__pb2._SCOPE
_SPARQLQUERYREQUEST.fields_by_name['payload'].message_type = _SPARQLQUERYREQUEST_PAYLOAD
_SPARQLQUERYRESPONSE_PAYLOAD.fields_by_name['remoteHostId'].message_type = iotics_dot_api_dot_common__pb2._HOSTID
_SPARQLQUERYRESPONSE_PAYLOAD.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_SPARQLQUERYRESPONSE_PAYLOAD.fields_by_name['contentType'].enum_type = _SPARQLRESULTTYPE
_SPARQLQUERYRESPONSE_PAYLOAD.containing_type = _SPARQLQUERYRESPONSE
_SPARQLQUERYRESPONSE.fields_by_name['headers'].message_type = iotics_dot_api_dot_common__pb2._HEADERS
_SPARQLQUERYRESPONSE.fields_by_name['payload'].message_type = _SPARQLQUERYRESPONSE_PAYLOAD
DESCRIPTOR.message_types_by_name['SparqlQueryRequest'] = _SPARQLQUERYREQUEST
DESCRIPTOR.message_types_by_name['SparqlQueryResponse'] = _SPARQLQUERYRESPONSE
DESCRIPTOR.enum_types_by_name['SparqlResultType'] = _SPARQLRESULTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SparqlQueryRequest = _reflection.GeneratedProtocolMessageType('SparqlQueryRequest', (_message.Message,), {

  'Payload' : _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
    'DESCRIPTOR' : _SPARQLQUERYREQUEST_PAYLOAD,
    '__module__' : 'iotics.api.meta_pb2'
    # @@protoc_insertion_point(class_scope:iotics.api.SparqlQueryRequest.Payload)
    })
  ,
  'DESCRIPTOR' : _SPARQLQUERYREQUEST,
  '__module__' : 'iotics.api.meta_pb2'
  # @@protoc_insertion_point(class_scope:iotics.api.SparqlQueryRequest)
  })
_sym_db.RegisterMessage(SparqlQueryRequest)
_sym_db.RegisterMessage(SparqlQueryRequest.Payload)

SparqlQueryResponse = _reflection.GeneratedProtocolMessageType('SparqlQueryResponse', (_message.Message,), {

  'Payload' : _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
    'DESCRIPTOR' : _SPARQLQUERYRESPONSE_PAYLOAD,
    '__module__' : 'iotics.api.meta_pb2'
    # @@protoc_insertion_point(class_scope:iotics.api.SparqlQueryResponse.Payload)
    })
  ,
  'DESCRIPTOR' : _SPARQLQUERYRESPONSE,
  '__module__' : 'iotics.api.meta_pb2'
  # @@protoc_insertion_point(class_scope:iotics.api.SparqlQueryResponse)
  })
_sym_db.RegisterMessage(SparqlQueryResponse)
_sym_db.RegisterMessage(SparqlQueryResponse.Payload)


DESCRIPTOR._options = None

_METAAPI = _descriptor.ServiceDescriptor(
  name='MetaAPI',
  full_name='iotics.api.MetaAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=881,
  serialized_end=974,
  methods=[
  _descriptor.MethodDescriptor(
    name='SparqlQuery',
    full_name='iotics.api.MetaAPI.SparqlQuery',
    index=0,
    containing_service=None,
    input_type=_SPARQLQUERYREQUEST,
    output_type=_SPARQLQUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METAAPI)

DESCRIPTOR.services_by_name['MetaAPI'] = _METAAPI

# @@protoc_insertion_point(module_scope)
