import os
import uuid

import dotenv
import grpc._channel

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.api.common_pb2 import Scope
from iotics.lib.grpc.helpers import create_property
from iotics.lib.grpc.iotics_api import IoticsApi


def main():
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
    try:
        get_twin_models(api)
    except grpc.RpcError as error:
        error: grpc._channel._MultiThreadedRendezvous
        print('Error from gRPC:', error.details())


def get_twin_models(api):
    client_app_id = uuid.uuid4().hex

    rdf_property_type_key = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
    rdf_property_type_value_model = 'https://data.iotics.com/app#Model'
    payload = api.get_search_payload(properties=[
        create_property(rdf_property_type_key, rdf_property_type_value_model, is_uri=True),
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


if __name__ == '__main__':
    main()
