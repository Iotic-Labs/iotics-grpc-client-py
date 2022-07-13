from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import create_location, create_property, create_feed_with_meta, create_feed_value
from iotics.lib.grpc.iotics_api import IoticsApi

FEED_NAME = 'myFeed'
CAMBRIDGE = create_location(52.2, 0.1)
LONDON = create_location(51.5, -0.1)


def main():
    import dotenv, os
    dotenv.load_dotenv()
    try:
        auth = IdentityAuth(
            os.environ['SPACE'],
            os.getenv('DID_RESOLVER_URL'),
            os.environ['USER_SEED'],
            os.environ['USER_KEY_NAME'],
            os.getenv('USER_NAME'),
            os.environ['AGENT_SEED'],
            os.environ['AGENT_KEY_NAME'],
            os.getenv('AGENT_NAME'),
        )
    except IdentityAuthError as error:
        print(error)
        return

    api = IoticsApi(auth)

    # Use your auth class to generate a decentralized identifier (DID) that will refer to your twin.
    twin_did = auth.generate_twin_did('test-twin')

    # You can now use this DID to create a twin.
    api.create_twin(twin_did)
    # Make the twin findable by providing some metadata, such as its location and a semantic property.
    # TODO(Adrian): Does visibility work as expected? Shouldn't be: `common_pb2.Visibility.PUBLIC`?
    api.update_twin(twin_did, location=CAMBRIDGE, visibility='PUBLIC', props_added=[
        create_property(key='http://test-ontology.com/test#key', value='12', datatype='integer')
    ])
    # IOTICS Twins can provide real-time streams of data using Feeds. Create a feed, making sure the name you provide
    # isn't already used by another feed on the same twin.
    api.create_feed(twin_did, FEED_NAME)
    # Feed metadata helps us understand what sort of data it shares. Feed shares take the form of key-value pairs, and
    # the Value objects tell us what sort of value is found at each key (the value's Label, the first argument). Feeds
    # may also be given semantic properties just like twins.
    api.update_feed(twin_did, FEED_NAME, store_last=False, values_added=[
        create_feed_value('temp', 'temperature in Celsius', 'http://purl.obolibrary.org/obo/UO_0000027', 'float')
    ], props_added=[create_property(key='http://test-ontology.com/test#feedIs', value='great')])
    # Our twin and feed are fully decorated! Let's see how it looks:
    print('BEFORE UPSERT:')
    print(api.describe_twin(twin_did))
    print(api.describe_feed(twin_did, FEED_NAME))
    print('SHARING DATA:')
    api.share_feed_data(twin_did, FEED_NAME, {'temp': 42})
    # Using the upsert command we can replace twin and feed metadata at the same time, creating any that weren't already
    # present.
    # TODO(Adrian): Does visibility work as expected? Shouldn't be: `common_pb2.Visibility.PRIVATE`?
    api.upsert_twin(twin_did, location=LONDON, visibility='PRIVATE', properties=[
        create_property(key='http://test-ontology.com/test#key', value='hi', language='en')
    ], feeds=[create_feed_with_meta('foo', values=[create_feed_value(
        'speed', 'speed in m/s', 'http://purl.obolibrary.org/obo/UO_0000094', 'float'
    )], properties=[create_property(key='http://test-ontology.com/test#feedIs', value='terrible')])])
    print('AFTER UPSERT:')
    print(api.describe_twin(twin_did))
    print(api.describe_feed(twin_did, 'foo'))
    # Upserts obliterate any preexisting twin configuration: the old FEED_NAME feed will no longer be present, and
    # deleting the new 'foo' feed leaves none left.
    api.delete_feed(twin_did, 'foo')
    print('EMPTY FEED LIST:')
    print(api.list_all_feeds(twin_did))
    print('DELETING TWIN:')
    api.delete_twin(twin_did)
    # After deleting a twin, the DID no longer refers to anything, and attempting to describe a twin there will cause an
    # error.
    try:
        api.describe_twin(twin_did)
    except:
        print('SUCCESS')
    else:
        raise Exception("Didn't delete twin")


if __name__ == '__main__':
    main()
