import json
import dotenv, os
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import create_feed_with_meta, create_value
from iotics.lib.grpc.iotics_api import IoticsApi


def get_auth():
    dotenv.load_dotenv()
    auth = IdentityAuth(
        os.environ['SPACE'],
        os.getenv('DID_RESOLVER_URL'),
        os.environ['USER_DID'],
        os.environ['AGENT_DID'],
        os.environ['AGENT_KEY_NAME'],
        os.environ['AGENT_NAME'],
        os.environ['AGENT_SECRET'],
        os.getenv('TOKEN_TTL'),
    )
    return auth


def main():
    try:
        auth = get_auth()
    except IdentityAuthError as error:
        print(error)
        return

    twin_did = os.getenv('TWIN_DID')
    print(twin_did)
    feed_name = os.getenv('FEED_NAME')
    print(feed_name)
    remote_host_id = os.getenv('REMOTE_HOST_ID')

    api = IoticsApi(auth)
    print('LAST STORED: ')
    # fetching last stored works in both spaces B and C
    print(api.fetch_last_stored(twin_did, twin_did, feed_name, remote_host_id))

    shares = api.fetch_interests(twin_did, twin_did, feed_name, remote_host_id, fetch_last_stored=True)
    while True:
        latest = next(shares)
        data = json.loads(latest.payload.feedData.data)
        # the last store value gets printed out for space B but not space C
        t = data['Message ID']
        print("%d" % t)
        if t == 0:
            break

if __name__ == '__main__':
    main()
