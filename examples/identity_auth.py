import typing

import requests
from iotics.lib.identity import get_rest_high_level_identity_api

from iotics.lib.grpc.auth import AuthInterface


class IdentityAuthError(Exception):
    """Raised when `IdentityAuth` cannot be instantiated correctly."""


class IdentityAuth(AuthInterface):
    def __init__(
        self,
        space: str,
        resolver_url: typing.Optional[str],
        user_seed: str,
        user_key_name: str,
        user_name: typing.Optional[str],
        agent_seed: str,
        agent_key_name: str,
        agent_name: typing.Optional[str],
        token_ttl: int = 30
    ):
        try:
            int(user_seed, 16)
            int(agent_seed, 16)
            if len(user_seed) != 64 or len(agent_seed) != 64:
                raise
        except:
            raise IdentityAuthError(
                'Please provide values for USER_SEED and AGENT_SEED that are 64-character hexadecimal strings.'
            )
        split_url = space.partition('://')
        space = split_url[2] or split_url[0]
        self.grpc_url = space + ':10001'
        if not resolver_url:
            index_url = f'https://{space}/index.json'
            try:
                resolver_url = requests.get(index_url).json()['resolver']
            except requests.exceptions.ConnectionError:
                raise IdentityAuthError(f'Could not fetch resolver URL from `{index_url}`.')

        self.high_level_api = api = get_rest_high_level_identity_api(resolver_url=resolver_url)
        user_registered_id, self.agent_registered_id = api.create_user_and_agent_with_auth_delegation(
            user_seed=bytearray.fromhex(user_seed),
            user_key_name=user_key_name,
            agent_seed=bytearray.fromhex(agent_seed),
            agent_key_name=agent_key_name,
            user_name=user_name,
            agent_name=agent_name,
        )
        print(f'User DID: {user_registered_id.did}')
        print(f'Agent DID: {self.agent_registered_id.did}')
        self.grpc_token = api.create_agent_auth_token(self.agent_registered_id, user_registered_id.did, token_ttl)

    def get_host(self) -> str:
        return self.grpc_url

    def get_token(self) -> str:
        return self.grpc_token

    def generate_twin_did(self, twin_name) -> str:
        # Reuse the agent secret seed for simplicity and ease of twin maintenance.
        seed = self.agent_registered_id.key_pair_secrets.seed
        # To keep your twins secure, you should ensure that the twin key name is secret and not easy to guess,
        # Optionally you can use password to make it more secure (defaults to none).
        key_name = twin_name
        twin_name = '#' + twin_name
        twin_registered_identity = self.high_level_api.create_twin_with_control_delegation(
            seed, key_name, self.agent_registered_id, '#AuthorityDelegation', twin_name)
        return twin_registered_identity.did
