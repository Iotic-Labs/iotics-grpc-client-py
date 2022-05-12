from iotics.api.common_pb2 import GeoLocation, Property, Uri, StringLiteral, Literal, LangLiteral, Value
from iotics.api.feed_pb2 import UpsertFeedWithMeta


def create_property(key, value, language=None, datatype=None, is_uri=False):
    value = _create_property_value(value, language, datatype, is_uri)
    if isinstance(value, Uri):
        return Property(key=key, uriValue=value)
    if isinstance(value, Literal):
        return Property(key=key, literalValue=value)
    if isinstance(value, StringLiteral):
        return Property(key=key, stringLiteralValue=value)
    if isinstance(value, LangLiteral):
        return Property(key=key, langLiteralValue=value)


def _create_property_value(value, language=None, datatype=None, is_uri=False):
    if is_uri:
        return Uri(value=value)
    if language:
        return LangLiteral(value=value, lang=language)
    if datatype:
        return Literal(value=value, dataType=datatype)
    return StringLiteral(value=value)


def create_location(lat, lon):
    return GeoLocation(lat=lat, lon=lon)


def create_feed_with_meta(feed_id, store_last=True, values=None, properties=None):
    return UpsertFeedWithMeta(
        id=feed_id,
        storeLast=store_last,
        values=values,
        properties=properties
    )


def create_feed_value(label, comment=None, unit=None, data_type=None):
    return Value(label=label, comment=comment, unit=unit, dataType=data_type)
