# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: iotics/api/feed.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'iotics/api/feed.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from iotics.api import common_pb2 as iotics_dot_api_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15iotics/api/feed.proto\x12\niotics.api\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17iotics/api/common.proto\"H\n\x06\x46\x65\x65\x64ID\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06twinId\x18\x02 \x01(\tR\x06twinId\x12\x16\n\x06hostId\x18\x03 \x01(\tR\x06hostId\"\x94\x02\n\x11\x43reateFeedRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12;\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\'.iotics.api.CreateFeedRequest.ArgumentsR\x04\x61rgs\x12?\n\x07payload\x18\x03 \x01(\x0b\x32%.iotics.api.CreateFeedRequest.PayloadR\x07payload\x1a\x19\n\x07Payload\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x1a\x37\n\tArguments\x12*\n\x06twinId\x18\x01 \x01(\x0b\x32\x12.iotics.api.TwinIDR\x06twinId\"\xbc\x01\n\x12\x43reateFeedResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12@\n\x07payload\x18\x02 \x01(\x0b\x32&.iotics.api.CreateFeedResponse.PayloadR\x07payload\x1a\x35\n\x07Payload\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"\xb8\x01\n\x11\x44\x65leteFeedRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12;\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\'.iotics.api.DeleteFeedRequest.ArgumentsR\x04\x61rgs\x1a\x37\n\tArguments\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"\xbc\x01\n\x12\x44\x65leteFeedResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12@\n\x07payload\x18\x02 \x01(\x0b\x32&.iotics.api.DeleteFeedResponse.PayloadR\x07payload\x1a\x35\n\x07Payload\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"\xa7\x03\n\x11UpdateFeedRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12;\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\'.iotics.api.UpdateFeedRequest.ArgumentsR\x04\x61rgs\x12?\n\x07payload\x18\x03 \x01(\x0b\x32%.iotics.api.UpdateFeedRequest.PayloadR\x07payload\x1a\xab\x01\n\x07Payload\x12\x38\n\tstoreLast\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\tstoreLast\x12*\n\x06values\x18\x03 \x01(\x0b\x32\x12.iotics.api.ValuesR\x06values\x12:\n\nproperties\x18\x06 \x01(\x0b\x32\x1a.iotics.api.PropertyUpdateR\nproperties\x1a\x37\n\tArguments\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"\xbc\x01\n\x12UpdateFeedResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12@\n\x07payload\x18\x02 \x01(\x0b\x32&.iotics.api.UpdateFeedResponse.PayloadR\x07payload\x1a\x35\n\x07Payload\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"\xbb\x02\n\x14ShareFeedDataRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12>\n\x04\x61rgs\x18\x02 \x01(\x0b\x32*.iotics.api.ShareFeedDataRequest.ArgumentsR\x04\x61rgs\x12\x42\n\x07payload\x18\x03 \x01(\x0b\x32(.iotics.api.ShareFeedDataRequest.PayloadR\x07payload\x1a\x37\n\x07Payload\x12,\n\x06sample\x18\x01 \x01(\x0b\x32\x14.iotics.api.FeedDataR\x06sample\x1a\x37\n\tArguments\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"F\n\x15ShareFeedDataResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\"\xe5\x01\n\x13ListAllFeedsRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12=\n\x04\x61rgs\x18\x02 \x01(\x0b\x32).iotics.api.ListAllFeedsRequest.ArgumentsR\x04\x61rgs\x12\'\n\x05range\x18\x03 \x01(\x0b\x32\x11.iotics.api.RangeR\x05range\x1a\x37\n\tArguments\x12*\n\x06twinId\x18\x01 \x01(\x0b\x32\x12.iotics.api.TwinIDR\x06twinId\"\xc2\x01\n\x14ListAllFeedsResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12\x42\n\x07payload\x18\x02 \x01(\x0b\x32(.iotics.api.ListAllFeedsResponse.PayloadR\x07payload\x1a\x37\n\x07Payload\x12,\n\x07\x66\x65\x65\x64Ids\x18\x01 \x03(\x0b\x32\x12.iotics.api.FeedIDR\x07\x66\x65\x65\x64Ids\"\xbc\x01\n\x13\x44\x65scribeFeedRequest\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12=\n\x04\x61rgs\x18\x03 \x01(\x0b\x32).iotics.api.DescribeFeedRequest.ArgumentsR\x04\x61rgs\x1a\x37\n\tArguments\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\"\x93\x03\n\x14\x44\x65scribeFeedResponse\x12-\n\x07headers\x18\x01 \x01(\x0b\x32\x13.iotics.api.HeadersR\x07headers\x12\x42\n\x07payload\x18\x02 \x01(\x0b\x32(.iotics.api.DescribeFeedResponse.PayloadR\x07payload\x1a\x8b\x01\n\nMetaResult\x12)\n\x06values\x18\x02 \x03(\x0b\x32\x11.iotics.api.ValueR\x06values\x12\x1c\n\tstoreLast\x18\x05 \x01(\x08R\tstoreLast\x12\x34\n\nproperties\x18\x06 \x03(\x0b\x32\x14.iotics.api.PropertyR\nproperties\x1az\n\x07Payload\x12*\n\x06\x66\x65\x65\x64Id\x18\x01 \x01(\x0b\x32\x12.iotics.api.FeedIDR\x06\x66\x65\x65\x64Id\x12\x43\n\x06result\x18\x02 \x01(\x0b\x32+.iotics.api.DescribeFeedResponse.MetaResultR\x06result\"\xa3\x01\n\x12UpsertFeedWithMeta\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1c\n\tstoreLast\x18\x04 \x01(\x08R\tstoreLast\x12)\n\x06values\x18\x05 \x03(\x0b\x32\x11.iotics.api.ValueR\x06values\x12\x34\n\nproperties\x18\x06 \x03(\x0b\x32\x14.iotics.api.PropertyR\nproperties2\xd3\x04\n\x07\x46\x65\x65\x64\x41PI\x12M\n\nCreateFeed\x12\x1d.iotics.api.CreateFeedRequest\x1a\x1e.iotics.api.CreateFeedResponse\"\x00\x12M\n\nDeleteFeed\x12\x1d.iotics.api.DeleteFeedRequest\x1a\x1e.iotics.api.DeleteFeedResponse\"\x00\x12M\n\nUpdateFeed\x12\x1d.iotics.api.UpdateFeedRequest\x1a\x1e.iotics.api.UpdateFeedResponse\"\x00\x12V\n\rShareFeedData\x12 .iotics.api.ShareFeedDataRequest\x1a!.iotics.api.ShareFeedDataResponse\"\x00\x12Y\n\x0eStreamFeedData\x12 .iotics.api.ShareFeedDataRequest\x1a!.iotics.api.ShareFeedDataResponse\"\x00(\x01\x12S\n\x0cListAllFeeds\x12\x1f.iotics.api.ListAllFeedsRequest\x1a .iotics.api.ListAllFeedsResponse\"\x00\x12S\n\x0c\x44\x65scribeFeed\x12\x1f.iotics.api.DescribeFeedRequest\x1a .iotics.api.DescribeFeedResponse\"\x00\x42}\n\x0e\x63om.iotics.apiB\tFeedProtoP\x01Z>github.com/Iotic-Labs/iotic-go-proto-qapi/iotics/api;ioticsapi\xa2\x02\x03IAX\xaa\x02\nIotics.Api\xca\x02\nIotics\\Apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iotics.api.feed_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016com.iotics.apiB\tFeedProtoP\001Z>github.com/Iotic-Labs/iotic-go-proto-qapi/iotics/api;ioticsapi\242\002\003IAX\252\002\nIotics.Api\312\002\nIotics\\Api'
  _globals['_FEEDID']._serialized_start=94
  _globals['_FEEDID']._serialized_end=166
  _globals['_CREATEFEEDREQUEST']._serialized_start=169
  _globals['_CREATEFEEDREQUEST']._serialized_end=445
  _globals['_CREATEFEEDREQUEST_PAYLOAD']._serialized_start=363
  _globals['_CREATEFEEDREQUEST_PAYLOAD']._serialized_end=388
  _globals['_CREATEFEEDREQUEST_ARGUMENTS']._serialized_start=390
  _globals['_CREATEFEEDREQUEST_ARGUMENTS']._serialized_end=445
  _globals['_CREATEFEEDRESPONSE']._serialized_start=448
  _globals['_CREATEFEEDRESPONSE']._serialized_end=636
  _globals['_CREATEFEEDRESPONSE_PAYLOAD']._serialized_start=583
  _globals['_CREATEFEEDRESPONSE_PAYLOAD']._serialized_end=636
  _globals['_DELETEFEEDREQUEST']._serialized_start=639
  _globals['_DELETEFEEDREQUEST']._serialized_end=823
  _globals['_DELETEFEEDREQUEST_ARGUMENTS']._serialized_start=768
  _globals['_DELETEFEEDREQUEST_ARGUMENTS']._serialized_end=823
  _globals['_DELETEFEEDRESPONSE']._serialized_start=826
  _globals['_DELETEFEEDRESPONSE']._serialized_end=1014
  _globals['_DELETEFEEDRESPONSE_PAYLOAD']._serialized_start=583
  _globals['_DELETEFEEDRESPONSE_PAYLOAD']._serialized_end=636
  _globals['_UPDATEFEEDREQUEST']._serialized_start=1017
  _globals['_UPDATEFEEDREQUEST']._serialized_end=1440
  _globals['_UPDATEFEEDREQUEST_PAYLOAD']._serialized_start=1212
  _globals['_UPDATEFEEDREQUEST_PAYLOAD']._serialized_end=1383
  _globals['_UPDATEFEEDREQUEST_ARGUMENTS']._serialized_start=768
  _globals['_UPDATEFEEDREQUEST_ARGUMENTS']._serialized_end=823
  _globals['_UPDATEFEEDRESPONSE']._serialized_start=1443
  _globals['_UPDATEFEEDRESPONSE']._serialized_end=1631
  _globals['_UPDATEFEEDRESPONSE_PAYLOAD']._serialized_start=583
  _globals['_UPDATEFEEDRESPONSE_PAYLOAD']._serialized_end=636
  _globals['_SHAREFEEDDATAREQUEST']._serialized_start=1634
  _globals['_SHAREFEEDDATAREQUEST']._serialized_end=1949
  _globals['_SHAREFEEDDATAREQUEST_PAYLOAD']._serialized_start=1837
  _globals['_SHAREFEEDDATAREQUEST_PAYLOAD']._serialized_end=1892
  _globals['_SHAREFEEDDATAREQUEST_ARGUMENTS']._serialized_start=768
  _globals['_SHAREFEEDDATAREQUEST_ARGUMENTS']._serialized_end=823
  _globals['_SHAREFEEDDATARESPONSE']._serialized_start=1951
  _globals['_SHAREFEEDDATARESPONSE']._serialized_end=2021
  _globals['_LISTALLFEEDSREQUEST']._serialized_start=2024
  _globals['_LISTALLFEEDSREQUEST']._serialized_end=2253
  _globals['_LISTALLFEEDSREQUEST_ARGUMENTS']._serialized_start=390
  _globals['_LISTALLFEEDSREQUEST_ARGUMENTS']._serialized_end=445
  _globals['_LISTALLFEEDSRESPONSE']._serialized_start=2256
  _globals['_LISTALLFEEDSRESPONSE']._serialized_end=2450
  _globals['_LISTALLFEEDSRESPONSE_PAYLOAD']._serialized_start=2395
  _globals['_LISTALLFEEDSRESPONSE_PAYLOAD']._serialized_end=2450
  _globals['_DESCRIBEFEEDREQUEST']._serialized_start=2453
  _globals['_DESCRIBEFEEDREQUEST']._serialized_end=2641
  _globals['_DESCRIBEFEEDREQUEST_ARGUMENTS']._serialized_start=768
  _globals['_DESCRIBEFEEDREQUEST_ARGUMENTS']._serialized_end=823
  _globals['_DESCRIBEFEEDRESPONSE']._serialized_start=2644
  _globals['_DESCRIBEFEEDRESPONSE']._serialized_end=3047
  _globals['_DESCRIBEFEEDRESPONSE_METARESULT']._serialized_start=2784
  _globals['_DESCRIBEFEEDRESPONSE_METARESULT']._serialized_end=2923
  _globals['_DESCRIBEFEEDRESPONSE_PAYLOAD']._serialized_start=2925
  _globals['_DESCRIBEFEEDRESPONSE_PAYLOAD']._serialized_end=3047
  _globals['_UPSERTFEEDWITHMETA']._serialized_start=3050
  _globals['_UPSERTFEEDWITHMETA']._serialized_end=3213
  _globals['_FEEDAPI']._serialized_start=3216
  _globals['_FEEDAPI']._serialized_end=3811
# @@protoc_insertion_point(module_scope)
