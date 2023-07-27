from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.iotics_api import IoticsApi


def main():
    import dotenv
    import os
    dotenv.load_dotenv()
    try:
        auth = IdentityAuth(
            os.environ['SPACE'],
            os.getenv('DID_RESOLVER_URL'),
            os.environ['USER_DID'],
            os.environ['AGENT_DID'],
            os.environ['AGENT_KEY_NAME'],
            os.environ['AGENT_NAME'],
            os.environ['AGENT_SECRET'],
            os.getenv('TOKEN_TTL')
        )
    except IdentityAuthError as error:
        print(error)
        return

    api = IoticsApi(auth)

    twin_did = os.getenv('TWIN_DID')
    if not twin_did:
        print('TWIN_DID not set')
        return

    print(api.describe_twin(twin_did))

    feed_id = os.getenv('FEED_ID')
    if feed_id:
        print(api.describe_feed(twin_did, feed_id))


if __name__ == '__main__':
    main()
