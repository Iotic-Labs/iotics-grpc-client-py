import json
import threading
import uuid
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.api.common_pb2 import Scope
from iotics.lib.grpc.helpers import create_input_with_meta, create_value, create_property
from iotics.lib.grpc.iotics_api import IoticsApi


INPUT_NAME = 'countdown'
VALUE_NAME = 'countdown'


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

def search_traffic_lights(api):
    client_app_id = uuid.uuid4().hex
    input = None

    rdf_property_type_key = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
    rdf_property_type_value_tl = 'http://www.productontology.org/id/Traffic_light'
    payload = api.get_search_payload(properties=[
        create_property(rdf_property_type_key, rdf_property_type_value_tl, is_uri=True),
    ])

    hosts = set()
    twins_total_count = 0
    for response in api.search_iter(client_app_id, payload, scope=Scope.GLOBAL, timeout=5):
        hostId = response.payload.remoteHostId.value or 'local'
        status = response.payload.status.message or 'OK'
        page = int(response.headers.clientRef.split('_page')[1]) + 1
        twins_count = len(response.payload.twins)
        print(f'Host: {hostId:>53} Twins: {twins_count:>3} Page: {page:>2} Status: {status}')
        hosts.add(hostId)
        twins_total_count += twins_count

    print(f'Got replies from {len(hosts)} hosts and found {twins_total_count} twins in total.')


def main():
    try:
        auth = get_auth()
    except IdentityAuthError as error:
        print(error)
        return
    
    api = IoticsApi(auth)
    # Create two twins: One which will send messages, and another which presents an input which will receive them.
    print('Creating twins...')
    follower_did = api.auth.generate_twin_did('follower')
    api.create_twin(follower_did)

    print('Searching for traffic lights...')
    input_did = search_traffic_lights(api)

    try:
        while True:
            # receive input
            text = input("press enter to change traffic light state")
            # send control message
    except KeyboardInterrupt:
        print('\n')
    finally:
        print('Cleaning space...')
        api.delete_twin(follower_did)
        print('Done!')


if __name__ == '__main__':
    main()
