from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import create_location, create_property, create_feed_with_meta, create_feed_value
    # PROPERTY_KEY_LABEL, PROPERTY_KEY_COMMENT, PROPERTY_KEY_HAS_MODEL
from iotics.lib.grpc.iotics_api import IoticsApi

FEED_NAME = 'myFeed'
CAMBRIDGE = create_location(52.2, 0.1)
LONDON = create_location(51.5, -0.1)
PROPERTY_KEY_LABEL='http://www.w3.org/2000/01/rdf-schema#label'
PROPERTY_KEY_COMMENT='http://www.w3.org/2000/01/rdf-schema#comment'
TWIN_NAME='ZTEST008-1155'

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
    twin_did = auth.generate_twin_did(TWIN_NAME)

    # You can now use this DID to create a twin.
    api.upsert_twin(twin_did, properties=[
        create_property(key=PROPERTY_KEY_LABEL, value=TWIN_NAME),
        create_property(key=PROPERTY_KEY_COMMENT, value='foo'),
        # create_property(key=PROPERTY_KEY_HAS_MODEL, value='did:iotics:iotGT9SKuoPaW4ZawWRv77HxonZbM5uUNDvh',
        #                 is_uri=True),
        create_property(key='http://example.com/foo', value='bar'),
        create_property(key='https://schema.org/Text', value='through the api'),
        create_property(key='https://schema.org/description', value='through the api desc'),
        create_property(key='https://data.iotics.com/app#createdBy', value='zoltaniotics')
        
        
    ], feeds=[
        create_feed_with_meta('feed1', properties=[
            create_property(key=PROPERTY_KEY_LABEL, value='My feed'),
            create_property(key=PROPERTY_KEY_COMMENT, value='It\'s super awesome')
        ], values=[
            create_feed_value('Awesomeness', 'how much awesome', 'http://qudt.org/vocab/unit/KiloPA', 'integer'),
            create_feed_value('Temperature', 'In celsius', 'https://qudt.org/vocab/unit/DEG_C', 'integer'),
        ])
    ])
    print('Created', twin_did)
    print(api.describe_twin(twin_did))


if __name__ == '__main__':
    main()
