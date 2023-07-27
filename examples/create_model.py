from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import METADATA_ALLOW_ALL, PROPERTY_IS_MODEL, PROPERTY_KEY_HAS_MODEL, PROPERTY_KEY_LABEL, create_location, create_property, create_feed_with_meta, create_value
from iotics.lib.grpc.iotics_api import IoticsApi

FEED_NAME = 'feed1'
CAMBRIDGE = create_location(52.2, 0.1)


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

    for i in range (1, 2):
        create_model(api, auth, f'model {i}')
        print(f'created model {i}')


def create_model(api, auth, model_name):
    # Use your auth class to generate a decentralized identifier (DID) that will refer to your twin.
    twin_did = auth.generate_twin_did(model_name)

    api.upsert_twin(twin_did, location=CAMBRIDGE, properties=[
        create_property(key=PROPERTY_KEY_LABEL, value=model_name, language='en'),
        PROPERTY_IS_MODEL
    ], feeds=[create_feed_with_meta(FEED_NAME, values=[create_value(
        'fd1', 'field 1', 'http://qudt.org/vocab/unit/DEG_C', 'float'
    )], properties=[create_property(key=PROPERTY_KEY_LABEL, value='feed 1', language='en')])])

    for i in range (1, 51):
        create_twin(api, auth, f'twin {i}', model_name, twin_did)

    # print(api.describe_twin(twin_did))


def create_twin(api, auth, twin_name, model_name, model_did):
    twin_did = auth.generate_twin_did(f'{model_name}-{twin_name}')

    api.upsert_twin(twin_did, location=CAMBRIDGE, properties=[
        create_property(key=PROPERTY_KEY_LABEL, value=f'{model_name}-{twin_name}', language='en'),
        create_property(key=PROPERTY_KEY_HAS_MODEL, value=model_did, is_uri=True)
    ], feeds=[create_feed_with_meta(FEED_NAME, values=[create_value(
        'fd1', 'field 1', 'http://qudt.org/vocab/unit/DEG_C', 'float'
    )], properties=[create_property(key=PROPERTY_KEY_LABEL, value='feed 1', language='en')])])

    print(f'created twin {model_name}-{twin_name}')


if __name__ == '__main__':
    main()
