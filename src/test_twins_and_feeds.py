import asyncio
from iotics.lib.grpc.helpers import create_location, create_property, create_feed_with_meta, create_feed_value
from iotics.lib.grpc.feeds import FeedApi
from iotics.lib.grpc.twins import TwinApi

TWIN_ID = 'did:iotics:iotHc4PJCmmJ8UytVp25D4wuVUbzkzYTBpYq'
FEED_NAME = 'myFeed'
CAMBRIDGE = create_location(52.2, 0.1)
LONDON = create_location(51.5, -0.1)


def main():
    space = input('What space? ') or 'ganymede.iotics.space'
    token = input('What token? ') or 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJkaWQ6aW90aWNzOmlvdEZnek5VWlRqRHppSFI2OFY3WEg0eEJmSDl5TVlOdlphUSNwb3J0YWwtYWdlbnQtMCIsImF1ZCI6ImRlZmF1bHQiLCJzdWIiOiJkaWQ6aW90aWNzOmlvdFhlMzkzOXlEMnJLckxBWTNrb1VVZUVTelNvV3M5QjRYdCIsImlhdCI6MTY1MjMzOTg2MywiZXhwIjoxNjUyMzQwNDkzfQ.cKVeqquFQxwtxnIDEs0Ng-WVswf2f8XuQV9UxjRzEwD2v1Frb0RdM0UyYhYreGt1QjiwSRtJhovTLuSJbzKFKQ'
    twin_api = TwinApi(space, token)
    feed_api = FeedApi(space, token)
    # result = api.list_twins()
    # did = result.payload.twins[0].id.value
    print('CREATING TWIN:')
    twin_api.create_twin(TWIN_ID)
    print('UPDATING TWIN:')
    twin_api.update_twin(TWIN_ID, location=CAMBRIDGE, visibility='PUBLIC', props_added=[
        create_property(key='http://test-ontology.com/test#key', value='12', datatype='integer')
    ])
    print('RESULT:')
    print(twin_api.describe_twin(TWIN_ID))
    print('ADDING FEED:')
    feed_api.create_feed(TWIN_ID, FEED_NAME)
    print('RESULT:')
    print(twin_api.describe_twin(TWIN_ID))
    print('UPDATING FEED:')
    feed_api.update_feed(TWIN_ID, FEED_NAME, store_last=False, values_added=[
        create_feed_value('temp', 'temperature in Celsius', 'http://purl.obolibrary.org/obo/UO_0000027', 'float')
    ], props_added=[create_property(key='http://test-ontology.com/test#feedIs', value='great')])
    print('RESULT:')
    print(feed_api.describe_feed(TWIN_ID, FEED_NAME))
    print('SHARING DATA:')
    feed_api.share_feed_data(TWIN_ID, FEED_NAME, {'temp': 42})
    print('UPSERTING TWIN:')
    twin_api.upsert_twin(TWIN_ID, location=LONDON, visibility='PRIVATE', properties=[
        create_property(key='http://test-ontology.com/test#key', value='hi', language='en')
    ], feeds=[create_feed_with_meta('foo', values=[create_feed_value(
        'speed', 'speed in m/s', 'http://purl.obolibrary.org/obo/UO_0000094', 'float'
    )], properties=[create_property(key='http://test-ontology.com/test#feedIs', value='terrible')])])
    print('RESULT:')
    print(twin_api.describe_twin(TWIN_ID))
    print('WITH FEED:')
    print(feed_api.describe_feed(TWIN_ID, 'foo'))
    print('DELETE FEED:')
    feed_api.delete_feed(TWIN_ID, 'foo')
    print('NEW FEED LIST:')
    print(feed_api.list_feeds(TWIN_ID))
    print('DELETING TWIN:')
    twin_api.delete_twin(TWIN_ID)
    try:
        twin_api.describe_twin(TWIN_ID)
    except:
        print('SUCCESS')
    else:
        raise Exception("Didn't delete twin")


if __name__ == '__main__':
    main()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

