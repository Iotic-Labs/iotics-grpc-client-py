import json
import threading
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import create_feed_with_meta, create_feed_value
from iotics.lib.grpc.iotics_api import IoticsApi

FEED_NAME = 'countdown'


def get_auth():
    import dotenv, os
    dotenv.load_dotenv()
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
    return auth


def create_twins(api: IoticsApi):
    followed_did = api.auth.generate_twin_did('followed')
    api.upsert_twin(followed_did, feeds=[create_feed_with_meta(FEED_NAME, True, [create_feed_value(
        'countdown', 'time remaining until liftoff', None, 'float'
    )])])
    follower_did = api.auth.generate_twin_did('follower')
    api.create_twin(follower_did)
    return follower_did, followed_did


def share_to_feed(api: IoticsApi, twin_did, feed_id):
    t = 10
    while t >= 0:
        api.share_feed_data(twin_did, feed_id, {'countdown': t})
        t -= 1
        sleep(1)


def main():
    try:
        auth = get_auth()
    except IdentityAuthError as error:
        print(error)
        return

    api = IoticsApi(auth)
    # Create two twins: One which will present a feed to be followed, and the other which will do the following.
    follower_did, followed_did = create_twins(api)
    # The followed twin shares data to its feed every 10 seconds.
    share_thread = threading.Thread(target=share_to_feed, args=(api, followed_did, FEED_NAME))
    share_thread.start()
    print('LAST STORED: ')
    # Before following the feed, we can inquire what's the last data it shared (we configured the feed to allow this)
    print(api.fetch_last_stored(follower_did, followed_did, FEED_NAME))
    # Now we follow the feed, which provides a generator that will yield a new value, when available, each time next()
    # is called
    shares = api.fetch_interests(follower_did, followed_did, FEED_NAME, fetch_last_stored=True)
    while True:
        latest = next(shares)
        data = json.loads(latest.payload.feedData.data)
        t = data['countdown']
        print("T MINUS %d!" % t)
        if t == 0:
            break
    # Clean up the space
    api.delete_twin(follower_did)
    api.delete_twin(followed_did)


if __name__ == '__main__':
    main()
