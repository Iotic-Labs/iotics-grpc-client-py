# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iotics/api/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17iotics/api/common.proto\x12\niotics.api\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1d\n\x05Limit\x12\x14\n\x05value\x18\x01 \x01(\rR\x05value\"\x1e\n\x06Offset\x12\x14\n\x05value\x18\x01 \x01(\rR\x05value\"\\\n\x05Range\x12\'\n\x05limit\x18\x01 \x01(\x0b\x32\x11.iotics.api.LimitR\x05limit\x12*\n\x06offset\x18\x02 \x01(\x0b\x32\x12.iotics.api.OffsetR\x06offset\"7\n\x0bLangLiteral\x12\x12\n\x04lang\x18\x01 \x01(\tR\x04lang\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"%\n\rStringLiteral\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\";\n\x07Literal\x12\x1a\n\x08\x64\x61taType\x18\x01 \x01(\tR\x08\x64\x61taType\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\x1b\n\x03Uri\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\xa3\x02\n\x08Property\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x39\n\x0cliteralValue\x18\x02 \x01(\x0b\x32\x13.iotics.api.LiteralH\x00R\x0cliteralValue\x12\x45\n\x10langLiteralValue\x18\x03 \x01(\x0b\x32\x17.iotics.api.LangLiteralH\x00R\x10langLiteralValue\x12K\n\x12stringLiteralValue\x18\x04 \x01(\x0b\x32\x19.iotics.api.StringLiteralH\x00R\x12stringLiteralValue\x12-\n\x08uriValue\x18\x05 \x01(\x0b\x32\x0f.iotics.api.UriH\x00R\x08uriValueB\x07\n\x05value\"1\n\x0bGeoLocation\x12\x10\n\x03lat\x18\x01 \x01(\x01R\x03lat\x12\x10\n\x03lon\x18\x02 \x01(\x01R\x03lon\"\\\n\tGeoCircle\x12\x33\n\x08location\x18\x01 \x01(\x0b\x32\x17.iotics.api.GeoLocationR\x08location\x12\x1a\n\x08radiusKm\x18\x02 \x01(\x01R\x08radiusKm\"\xf9\x01\n\x07Headers\x12\x1c\n\tclientRef\x18\x01 \x01(\tR\tclientRef\x12 \n\x0b\x63lientAppId\x18\x02 \x01(\tR\x0b\x63lientAppId\x12&\n\x0etransactionRef\x18\x03 \x03(\tR\x0etransactionRef\x12\x42\n\rconsumerGroup\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\rconsumerGroup\x12\x42\n\x0erequestTimeout\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0erequestTimeout\"\xa3\x01\n\x13SubscriptionHeaders\x12 \n\x0b\x63lientAppId\x18\x01 \x01(\tR\x0b\x63lientAppId\x12&\n\x0etransactionRef\x18\x02 \x03(\tR\x0etransactionRef\x12\x42\n\rconsumerGroup\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\rconsumerGroup\"\x1e\n\x06HostID\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\x1e\n\x06TwinID\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\x1e\n\x06\x46\x65\x65\x64ID\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\x1f\n\x07InputID\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"g\n\x05Value\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\x12\x12\n\x04unit\x18\x03 \x01(\tR\x04unit\x12\x1a\n\x08\x64\x61taType\x18\x04 \x01(\tR\x08\x64\x61taType\"Y\n\x06Values\x12\'\n\x05\x61\x64\x64\x65\x64\x18\x01 \x03(\x0b\x32\x11.iotics.api.ValueR\x05\x61\x64\x64\x65\x64\x12&\n\x0e\x64\x65letedByLabel\x18\x02 \x03(\tR\x0e\x64\x65letedByLabel\"n\n\x08\x46\x65\x65\x64\x44\x61ta\x12:\n\noccurredAt\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\noccurredAt\x12\x12\n\x04mime\x18\x03 \x01(\tR\x04mime\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\x0cR\x04\x64\x61ta\"\xb0\x01\n\x0ePropertyUpdate\x12\x1e\n\nclearedAll\x18\x01 \x01(\x08R\nclearedAll\x12.\n\x07\x64\x65leted\x18\x02 \x03(\x0b\x32\x14.iotics.api.PropertyR\x07\x64\x65leted\x12\"\n\x0c\x64\x65letedByKey\x18\x03 \x03(\tR\x0c\x64\x65letedByKey\x12*\n\x05\x61\x64\x64\x65\x64\x18\x04 \x03(\x0b\x32\x14.iotics.api.PropertyR\x05\x61\x64\x64\x65\x64*%\n\nVisibility\x12\x0b\n\x07PRIVATE\x10\x00\x12\n\n\x06PUBLIC\x10\x01*\x1e\n\x05Scope\x12\n\n\x06GLOBAL\x10\x00\x12\t\n\x05LOCAL\x10\x01\x42\x7f\n\x0e\x63om.iotics.apiB\x0b\x43ommonProtoP\x01Z>github.com/Iotic-Labs/iotic-go-proto-qapi/iotics/api;ioticsapi\xa2\x02\x03IAX\xaa\x02\nIotics.Api\xca\x02\nIotics\\Apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iotics.api.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.iotics.apiB\013CommonProtoP\001Z>github.com/Iotic-Labs/iotic-go-proto-qapi/iotics/api;ioticsapi\242\002\003IAX\252\002\nIotics.Api\312\002\nIotics\\Api'
  _VISIBILITY._serialized_start=1920
  _VISIBILITY._serialized_end=1957
  _SCOPE._serialized_start=1959
  _SCOPE._serialized_end=1989
  _LIMIT._serialized_start=104
  _LIMIT._serialized_end=133
  _OFFSET._serialized_start=135
  _OFFSET._serialized_end=165
  _RANGE._serialized_start=167
  _RANGE._serialized_end=259
  _LANGLITERAL._serialized_start=261
  _LANGLITERAL._serialized_end=316
  _STRINGLITERAL._serialized_start=318
  _STRINGLITERAL._serialized_end=355
  _LITERAL._serialized_start=357
  _LITERAL._serialized_end=416
  _URI._serialized_start=418
  _URI._serialized_end=445
  _PROPERTY._serialized_start=448
  _PROPERTY._serialized_end=739
  _GEOLOCATION._serialized_start=741
  _GEOLOCATION._serialized_end=790
  _GEOCIRCLE._serialized_start=792
  _GEOCIRCLE._serialized_end=884
  _HEADERS._serialized_start=887
  _HEADERS._serialized_end=1136
  _SUBSCRIPTIONHEADERS._serialized_start=1139
  _SUBSCRIPTIONHEADERS._serialized_end=1302
  _HOSTID._serialized_start=1304
  _HOSTID._serialized_end=1334
  _TWINID._serialized_start=1336
  _TWINID._serialized_end=1366
  _FEEDID._serialized_start=1368
  _FEEDID._serialized_end=1398
  _INPUTID._serialized_start=1400
  _INPUTID._serialized_end=1431
  _VALUE._serialized_start=1433
  _VALUE._serialized_end=1536
  _VALUES._serialized_start=1538
  _VALUES._serialized_end=1627
  _FEEDDATA._serialized_start=1629
  _FEEDDATA._serialized_end=1739
  _PROPERTYUPDATE._serialized_start=1742
  _PROPERTYUPDATE._serialized_end=1918
# @@protoc_insertion_point(module_scope)
