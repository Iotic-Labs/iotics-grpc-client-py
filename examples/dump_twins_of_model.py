import os
import uuid

import dotenv
import grpc._channel

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.api.common_pb2 import Scope
from iotics.api.search_pb2 import ResponseType
from iotics.lib.grpc.helpers import PROPERTY_KEY_HAS_MODEL, PROPERTY_KEY_LABEL, create_property
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
        get_twin_models(api)
    except grpc.RpcError as error:
        error: grpc._channel._MultiThreadedRendezvous
        print('Error from gRPC:', error.details())


def get_label(properties):
    for property in properties:
        if property.key == PROPERTY_KEY_LABEL:
            return property.langLiteralValue.value
    return None

def get_twin_models(api):
    client_app_id = uuid.uuid4().hex

    rdf_property_type_key = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
    # rdf_property_type_value_model = 'https://data.iotics.com/app#CollectionTwin'
    rdf_property_type_value_model = 'https://data.iotics.com/app#Model'
    payload = api.get_search_payload(properties=[
        create_property(rdf_property_type_key, rdf_property_type_value_model, is_uri=True),
    ], response_type=ResponseType.FULL)

    for response in api.search_iter(client_app_id, payload, scope=Scope.LOCAL, timeout=5):
        for twin in response.payload.twins:
            label = get_label(twin.properties)
            print(f'{label} {twin.twinId.id}')

            # if label == 'test':
            if label.startswith('Customer'):
                # delete_twins_of_model(api, twin.twinId.id)

            # if input(f'Press y to delete twins of this model {label} {twin.twinId.id}: ') == 'y':

                # if input(f'Press y to delete this model {label} {twin.twinId.id}: ') == 'y':
                describe_twins_of_model(api, twin.twinId.id)


def describe_twins_of_model(api, model_did):
    client_app_id = uuid.uuid4().hex

    payload = api.get_search_payload(properties=[
        create_property(PROPERTY_KEY_HAS_MODEL, model_did, is_uri=True),
    ], response_type=ResponseType.FULL)

    properties = []
    values = []

    for response in api.search_iter(client_app_id, payload, scope=Scope.LOCAL, timeout=5):
        for twin in response.payload.twins:
            propLine = []
            valueLine = []
            for property in twin.properties:
                propLine.append(property.key)
                if property.langLiteralValue:
                    valueLine.append(property.langLiteralValue.value)
                elif property.literalValue:
                    valueLine.append(property.literalValue.value)
                elif property.uriValue:
                    valueLine.append(property.uriValue.value)
                else:
                    valueLine.append('no value')
            
            properties.append(', '.join(propLine))
            values.append(', '.join(valueLine))

    print('properties are:')
    print(properties)
    print('values are:')
    print(values)


if __name__ == '__main__':
    main()
