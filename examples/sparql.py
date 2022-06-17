from typing import Dict

import grpc
from identity_auth import IdentityAuth, IdentityAuthError
from iotics.lib.grpc.iotics_api import IoticsApi
from iotics.api.meta_pb2 import SparqlQueryResponse


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


def do_query(query, api):
    # Map of responses per sequence number (remove potential duplication) per host
    chunks_per_host: Dict[str, Dict[int, SparqlQueryResponse]] = {}
    stream = api.sparql_query(query)
    try:
        for response in stream:
            # Chunk processing per host per seq number
            host_id = response.payload.remoteHostId.value or 'localhost'
            chunks = chunks_per_host.setdefault(host_id, {})
            chunks[response.payload.seqNum] = response
    # Exit the loop based on the timeout error (normal case)
    # Or any other GRPCError (anomaly)
    except grpc.RpcError as err:
        if err.code() != grpc.StatusCode.DEADLINE_EXCEEDED:
            raise err
        print("timeout occurred")

    for host_id, chunks in chunks_per_host.items():
        sorted_chunks = sorted(chunks.values(), key=lambda r: r.payload.seqNum)
        last_chunk = sorted_chunks[-1]

        if not last_chunk.payload.last or len(chunks) != last_chunk.payload.seqNum + 1:
            print(f'Incomplete response from {host_id} - skip')
            continue

        resp = ''.join([c.payload.resultChunk.decode() for c in sorted_chunks])
        print('%s chunks received' % len(sorted_chunks))
        print(f'Response from host: {host_id}')
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
    print('RE-QUERY (bindings should be empty)')
    do_query(query, api)


if __name__ == '__main__':
    main()
