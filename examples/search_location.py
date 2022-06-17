import os
import uuid

import dotenv
import grpc._channel

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.api.common_pb2 import Scope
from iotics.api.search_pb2 import ResponseType
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
        get_twins_in_cambridge(api)
    except grpc.RpcError as error:
        error: grpc._channel._MultiThreadedRendezvous
        print('Error from gRPC:', error.details())


def get_twins_in_cambridge(api):
    client_app_id = uuid.uuid4().hex

    cambridge = 52.1951, 0.1313, 5  # latitude, longitude, radius in km
    payload = api.get_search_payload(location=cambridge, response_type=ResponseType.FULL)

    hosts = set()
    twins_total_count = 0
    for response in api.search_iter(client_app_id, payload, scope=Scope.GLOBAL, timeout=5):
        hostId = response.payload.remoteHostId.value or 'local'
        status = response.payload.status
        if status.code:
            print(f'Host: {hostId:>53}: {status.message}')
            return

        twins = [
            f'- {twin.id.value} ({prop.langLiteralValue.lang}): {prop.langLiteralValue.value}'
            for twin in response.payload.twins
            for prop in twin.properties
            if prop.key == 'http://www.w3.org/2000/01/rdf-schema#label'
        ]
        if twins:
            print(f'{hostId}:\n' + '\n'.join(twins))

        hosts.add(hostId)
        twins_total_count += len(response.payload.twins)

    print(f'Got replies from {len(hosts)} hosts and found {twins_total_count} twins in total.')


if __name__ == '__main__':
    main()
