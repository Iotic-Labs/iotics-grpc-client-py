import json
import threading
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import create_property
from iotics.lib.grpc.iotics_api import IoticsApi

INPUT_NAME = 'countdown'
VALUE_NAME = 'countdown'

def parse_inputs(api: IoticsApi, twin_did, input_name):
    # Here we tell the receiver to begin allowing messages on its input, and get back a generator which will return the
    # messages that are shared to it.
    shares = api.receive_input_messages(twin_did, input_name)
    while True:
        latest = next(shares)
        data = json.loads(latest.payload.message.data)
        t = data[VALUE_NAME]
        print("Received message: %s" % t)
        if t == '!':
            # We know the message, so stop listening for input messages once we get the last character.
            break

def build_auth() -> IdentityAuth:
    import dotenv
    import os
    dotenv.load_dotenv()

    return IdentityAuth(
        os.environ['SPACE'],
        os.getenv('DID_RESOLVER_URL'),
        os.environ['USER_DID'],
        os.environ['AGENT_DID'],
        os.environ['AGENT_KEY_NAME'],
        os.environ['AGENT_NAME'],
        os.environ['AGENT_SECRET'],
        os.getenv('TOKEN_TTL')
    )

def main():
    try:
        auth = build_auth()
    except IdentityAuthError as error:
        print(error)
        return

    print('Auth built successfully')
    api = IoticsApi(auth)

    # Use your auth class to generate a decentralized identifier (DID) that will refer to your twin.
    twin_did = auth.generate_twin_did('test-twin')
    sender_did = auth.generate_twin_did('test-twin-sender')

    print('Creating twin...')
    # You can now use this DID to create a twin.
    api.create_twin(twin_did)
    api.create_twin(sender_did)

    print('Creating input...')
    # Create an input for the twin. This will allow other twins to share data with it.
    api.create_input(twin_did, INPUT_NAME)

    # Spawn a thread to listen to the input.
    print('Preparing to receive messages...')
    receiver_thread = threading.Thread(target=parse_inputs, args=(api, twin_did, INPUT_NAME))
    receiver_thread.start()

    # Send messages to the input.
    print('Sending messages...')
    message = 'HELLO, IOTICS!'
    for char in message:
        api.send_input_message({VALUE_NAME: char}, sender_did, twin_did, INPUT_NAME)

        # Wait a second between each message.
        sleep(0.2)
    print('updating input...')
    api.update_input(twin_did, INPUT_NAME, props_added=[create_property(key='http://test-ontology.com/test#inputIs', value='great')])
    print('Cleaning space...')
    api.delete_twin(sender_did)
    api.delete_twin(twin_did)
    print('Done!')
    # After deleting a twin, the DID no longer refers to anything, and attempting to describe a twin there will cause an
    # error.
    try:
        api.describe_twin(twin_did)
    except:
        print('SUCCESS')
    else:
        raise Exception("Didn't delete twin")

if __name__ == '__main__':
    main()
