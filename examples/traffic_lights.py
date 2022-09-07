import json
import threading
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.helpers import create_input_with_meta, create_value
from iotics.lib.grpc.iotics_api import IoticsApi

import pibrella

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


def create_twins(api: IoticsApi):
    receiver_did = api.auth.generate_twin_did('receiver')
    api.upsert_twin(receiver_did, inputs=[create_input_with_meta(INPUT_NAME, [create_value(
        VALUE_NAME, 'time remaining until liftoff', None, 'float'
    )])])
    sender_did = api.auth.generate_twin_did('sender')
    api.create_twin(sender_did)
    return sender_did, receiver_did


def receive_messages(api: IoticsApi, twin_did, input_name, tl):
    # Here we tell the receiver to begin allowing messages on its input, and get back a generator which will return the
    # messages that are shared to it.
    shares = api.receive_input_messages(twin_did, input_name)

    while True:
        latest = next(shares)
        data = json.loads(latest.payload.message.data)
        t = data[VALUE_NAME]
        print("Received message: %s" % t)
        print("traffic state: %s" % next(tl.state))
        if t == '!':
            # We know the message, so stop listening for input messages once we get the last character.
            break

class TrafficLights():
    def __init__(self):
        self.__state = self.__traffic_state()

    @property
    def state(self):
        return self.__state

    def __traffic_state(self):

        while True:
            pibrella.light.red.on()
            yield("red")

            pibrella.light.yellow.on()
            yield("red and amber")

            pibrella.light.red.off()
            pibrella.light.yellow.off()
            pibrella.light.green.on()
            yield("green")

            pibrella.light.green.off()
            pibrella.light.yellow.on()
            yield("amber")

            pibrella.light.yellow.off()
        

def main():
    try:
        auth = get_auth()
    except IdentityAuthError as error:
        print(error)
        return
    
    tl = TrafficLights()
    def button_changed(pin):
        if pin.read() == 1:
            print("traffic state: %s" % next(tl.state))
    pibrella.button.changed(button_changed) 

    api = IoticsApi(auth)
    # Create two twins: One which will send messages, and another which presents an input which will receive them.
    print('Creating twins...')
    sender_did, receiver_did = create_twins(api)
    print('Preparing to receive messages...')
    receiver_thread = threading.Thread(target=receive_messages, args=(api, receiver_did, INPUT_NAME, tl))
    receiver_thread.start()
    # The sender twin sends this message one letter at a time to the receiver, with messages one second apart.
    print('Sending messages...')
    message = 'HELLO, IOTICS!'
    for char in message:
        api.send_input_message({VALUE_NAME: char}, sender_did, receiver_did, INPUT_NAME)
        sleep(1)

    try:
        pibrella.pause()
    except KeyboardInterrupt:
        pass
    finally:
        print('Cleaning space...')
        api.delete_twin(sender_did)
        api.delete_twin(receiver_did)
        print('Done!')

        pibrella.light.off() # turn off all the lights before we leave

if __name__ == '__main__':
    main()
