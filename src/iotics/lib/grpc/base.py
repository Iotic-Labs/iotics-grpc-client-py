import grpc


class ApiBase:
    stub_class = None

    def __init__(self, address, token):
        self.stub = self.stub_class(self._create_channel(address, token))
        self.address = address
        self.token = token

    def _create_channel(self, address, token):
        call_credentials = grpc.access_token_call_credentials(token)
        channel_credentials = grpc.ssl_channel_credentials()
        composite_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
        return grpc.secure_channel(f"{address}:10001", credentials=composite_credentials)