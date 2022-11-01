import json
import sys
import threading
import uuid
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.api.common_pb2 import Scope
from iotics.lib.grpc.helpers import create_input_with_meta, create_value, create_property
from iotics.lib.grpc.iotics_api import IoticsApi


VALUE_NAME = 'state'


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
    twins = set()
    twins_total_count = 0
    for response in api.search_iter(client_app_id, payload, scope=Scope.GLOBAL, timeout=5):
        hostId = response.payload.hostId
        status = response.payload.status.message or 'OK'
        page = int(response.headers.clientRef.split('_page')[1]) + 1
        twins_count = len(response.payload.twins)
        if twins_count > 0:
            for twin in response.payload.twins:
                twins.add(twin.twinId.id)
        print(f'Host: {hostId:>53} Twins: {twins_count:>3} Page: {page:>2} Status: {status}')
        hosts.add(hostId)
        twins_total_count += twins_count

    print(f'Got replies from {len(hosts)} hosts and found {twins_total_count} twins in total.')
    return twins

    
def follow_feed(api: IoticsApi, follower_did, tl_twin_did, feed_name):
    shares = api.fetch_interests(follower_did, tl_twin_did, feed_name, fetch_last_stored=True)

    while True:
        latest = next(shares)
        data = json.loads(latest.payload.feedData.data)
        t = data[VALUE_NAME]
        print("\nReceived message: %s" % t)


def main():
    try:
        auth = get_auth()
    except IdentityAuthError as error:
        print(error)
        return
    
    api = IoticsApi(auth)
    # Create the follower / controller twin
    print('Creating twin...')
    follower_did = api.auth.generate_twin_did('follower')
    api.create_twin(follower_did)

    print('Searching for traffic lights...')
    twins = search_traffic_lights(api)

    if len(twins) == 0:
        print('No twins found. Cleaning space...')
        api.delete_twin(follower_did)
        print('Exiting...')
        sys.exit(1)

    print('Describing found traffic lights...')
    for twin in twins:
        tl_twin_did = twin
        description = api.describe_twin(twin)
        print(description)
        for feed in description.payload.result.feeds:
            feed_id = feed.feedId
        for control in description.payload.result.inputs:
            input_id = control.inputId
        print(feed_id)
        print(input_id)
        break

    receiver_thread = threading.Thread(target=follow_feed, args=(api, follower_did, tl_twin_did, feed_id.id))
    receiver_thread.start()

    try:
        while True:
            # receive input from command line
            text = input("press enter to change traffic light state")
            api.send_input_message({VALUE_NAME: ""}, follower_did, tl_twin_did, input_id.id)
            # send control message
    except KeyboardInterrupt:
        print('\nExiting')
    finally:
        print('Cleaning space...')
        api.delete_twin(follower_did)
        print('Done!')


if __name__ == '__main__':
    main()
