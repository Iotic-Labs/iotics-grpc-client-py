import os
import uuid

import dotenv
import grpc._channel

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.iotics_api import IoticsApi
from iotics.lib.grpc.helpers import PER_PAGE_LIMIT


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
        list_local_twins(api)
    except grpc.RpcError as error:
        error: grpc._channel._MultiThreadedRendezvous
        print('Error from gRPC:', error.details())


def list_local_twins(api):

    #limit > 100 throws an grpc param error
    twins_total_count=PER_PAGE_LIMIT
    all_twin_count = 0
    page_num=0
    while twins_total_count==PER_PAGE_LIMIT :
        twin_list = api.list_twins(page=page_num)
        twins_total_count = len(twin_list.payload.twins)
        all_twin_count+=twins_total_count
        print(f'Got replies from page #{page_num} and found {twins_total_count} twins on this page.')
        page_num+=1

    print(f'found {all_twin_count} twins in total.')

if __name__ == '__main__':
    main()
