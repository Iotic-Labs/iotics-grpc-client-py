from time import sleep
from typing import Dict

import grpc
from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.iotics_api import IoticsApi
from iotics.api.meta_pb2 import SparqlQueryResponse


def get_auth():
    import dotenv
    import os
    dotenv.load_dotenv()
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
    return auth


def do_query(query, api):
    # Map of responses per sequence number (remove potential duplication)
    chunks: Dict[int, SparqlQueryResponse] = {}
    stream = api.sparql_query(query)
    try:
        for response in stream:
            # Chunk processing per seq number
            chunks[response.payload.seqNum] = response
            print(f'Chunk {response.payload.seqNum} received: {response.payload.resultChunk.decode()}')
    # Exit the loop based on the timeout error (normal case)
    # Or any other GRPCError (anomaly)
    except grpc.RpcError as err:
        if err.code() != grpc.StatusCode.DEADLINE_EXCEEDED:
            raise err
        print("timeout occurred")

    sorted_chunks = sorted(chunks.values(), key=lambda r: r.payload.seqNum)
    last_chunk = sorted_chunks[-1]

    if not last_chunk.payload.last or len(chunks) != last_chunk.payload.seqNum + 1:
        print(f'Incomplete response')

    resp = ''.join([c.payload.resultChunk.decode() for c in sorted_chunks])
    print('%s chunks received' % len(sorted_chunks))
    print(resp)


def main():
    try:
        api = IoticsApi(get_auth())
    except IdentityAuthError as error:
        print(error)
        return

    update = '''
    PREFIX iotg: <http://data.iotics.com/graph#>
    INSERT DATA {
        GRAPH iotg:custom-public {
            <http://myontology.com/foo> a <http://myontology.com/bar> .
        }
    }'''
    print("DOING UPDATE")
    api.sparql_update(update)
    # Wait for the update to be processed before querying
    sleep(5)
    print("DOING QUERY")
    query = '''
    PREFIX iotg: <http://data.iotics.com/graph#>
    SELECT ?s ?p ?o
    FROM iotg:custom-public
    WHERE {
        ?s ?p ?o
    }'''
    do_query(query, api)
    print('CLEANUP')
    update = '''
    PREFIX iotg: <http://data.iotics.com/graph#>
    DELETE DATA {
        GRAPH iotg:custom-public {
            <http://myontology.com/foo> a <http://myontology.com/bar> .
        }
    }'''
    api.sparql_update(update)
    # Wait for the update to be processed before querying
    sleep(5)
    print('RE-QUERY (bindings should be empty)')
    do_query(query, api)


if __name__ == '__main__':
    main()
