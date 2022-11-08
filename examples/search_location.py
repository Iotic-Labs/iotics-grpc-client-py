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
    try:
        get_twins_in_cambridge(api)
    except grpc.RpcError as error:
        error: grpc._channel._MultiThreadedRendezvous
        print('Error from gRPC:', error.details())


def get_twins_in_cambridge(api):
    client_app_id = uuid.uuid4().hex

    cambridge = 52.1951, 0.1313, 5  # latitude, longitude, radius in km
    payload = api.get_search_payload(location=cambridge, response_type=ResponseType.FULL)

    local_host_id = api.get_local_host_id()

    host_count = 0
    twins_total_count = 0
    for response in api.search_iter(client_app_id, payload, scope=Scope.GLOBAL, timeout=5):
        hostId = response.payload.hostId
        status = response.payload.status
        if status.code:
            print(f'Host: {hostId:>53}: {status.message}')
            return

        twins = [
            f'- {twin.twinId.id} ({prop.langLiteralValue.lang}): {prop.langLiteralValue.value}'
            for twin in response.payload.twins
            for prop in twin.properties
            if prop.key == 'http://www.w3.org/2000/01/rdf-schema#label'
        ]

        host_count += 1

        print(f'{hostId}{"(local host)" if not hostId or local_host_id == hostId else ""}:\n' + '\n'.join(twins))

        twins_total_count += len(response.payload.twins)

    print(f'Got replies from {host_count} hosts and found {twins_total_count} twins in total.')


if __name__ == '__main__':
    main()
