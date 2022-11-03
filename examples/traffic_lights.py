import json
from threading import Thread, Event
from time import sleep

from identity_auth import IdentityAuth, IdentityAuthError
from iotics.api.common_pb2 import Visibility
from iotics.lib.grpc.helpers import create_input_with_meta, create_value, create_location, create_property, create_feed_with_meta
from iotics.lib.grpc.iotics_api import IoticsApi

import pibrella

CAMBRIDGE = create_location(52.2, 0.1)
KEGS = create_location(52.2509719,0.7012496)
INPUT_NAME = 'countdown'
VALUE_NAME = 'countdown'
FEED_NAME = 'tl_state'
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


def create_twin(api: IoticsApi):
    receiver_did = api.auth.generate_twin_did('receiver')
    api.upsert_twin(receiver_did, inputs=[create_input_with_meta(INPUT_NAME, [create_value(
        VALUE_NAME, 'next state', None, 'string'
    )])])

    # Make the twin findable by providing some metadata, such as its location and a semantic property.
    rdf_property_type_key = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
    rdf_property_type_value_tl = 'http://www.productontology.org/id/Traffic_light'
    rdf_property_label_key = 'http://www.w3.org/2000/01/rdf-schema#label'
    rdf_property_label_value_tl = 'Demo pibrella traffic lights'
    rdf_property_sdo_city = 'https://schema.org/City'
    rdf_property_wd_cambridge = 'https://www.wikidata.org/wiki/Q350'

    api.update_twin(receiver_did, location=KEGS, visibility=Visibility.PUBLIC, props_added=[
        create_property(rdf_property_type_key, rdf_property_type_value_tl, is_uri=True),
        create_property(rdf_property_label_key, rdf_property_label_value_tl, is_uri=False),
        create_property(rdf_property_sdo_city, rdf_property_wd_cambridge, is_uri=True)
    ])
    # IOTICS Twins can provide real-time streams of data using Feeds. Create a feed, making sure the name you provide
    # isn't already used by another feed on the same twin.
    api.create_feed(receiver_did, FEED_NAME)
    # Feed metadata helps us understand what sort of data it shares. Feed shares take the form of key-value pairs, and
    # the Value objects tell us what sort of value is found at each key (the value's Label, the first argument). Feeds
    # may also be given semantic properties just like twins.
    api.update_feed(receiver_did, FEED_NAME, store_last=True, 
        values_added=[create_value('state', 'traffic lights state', None, 'string'),],
        props_added=[create_property(key=rdf_property_label_key, value='Traffic light state', is_uri=False)]
        )

    return receiver_did


def receive_messages(api: IoticsApi, twin_did, input_name, tl, stop_threads):
    # Here we tell the receiver to begin allowing messages on its input, and get back a generator which will return the
    # messages that are shared to it.
    shares = api.receive_input_messages(twin_did, input_name)

    while True:
        latest = next(shares)
        if  stop_threads.is_set():
            break
        data = json.loads(latest.payload.message.data)
        t = data[VALUE_NAME]
        print("Received message: %s" % t)
        next_state = next(tl.state)
        api.share_feed_data(twin_did, FEED_NAME, {'state': next_state})
        print("traffic state: %s" % next_state)


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

    api = IoticsApi(auth)
    # Create twin: which presents an input will receive state change messages
    print('Creating twin...')
    receiver_did = create_twin(api)
    print('Preparing to receive messages...')
    stop_threads = Event()
    receiver_thread = Thread(target=receive_messages, args=(api, receiver_did, INPUT_NAME, tl, stop_threads))
    receiver_thread.start()

    # pibrella stuff
    def button_changed(pin):
        if pin.read() == 1:
            next_state = next(tl.state)
            # twin_did.share next_state
            print("traffic state: %s" % next_state)
            api.share_feed_data(receiver_did, FEED_NAME, {'state': next_state})
    pibrella.button.changed(button_changed) 

    # We send this message one letter at a time to the ourselves, with messages one second apart. Just to show things are working
    print('Sending messages...')
    message = 'HELLO'
    for char in message:
        api.send_input_message({VALUE_NAME: char}, receiver_did, receiver_did, INPUT_NAME)
        sleep(1)

    try:
        pibrella.pause()
    except KeyboardInterrupt:
        pass
    finally:
        print('Cleaning space...')
        stop_threads.set() # set the stop_threads flag and then send ourselves a message to ensure the loop runs
        api.send_input_message({VALUE_NAME: ""}, receiver_did, receiver_did, INPUT_NAME)
        api.delete_twin(receiver_did)
        print('Done!')

        pibrella.light.off() # turn off all the lights before we leave


if __name__ == '__main__':
    main()
