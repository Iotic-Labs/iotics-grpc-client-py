import typing

import requests
from iotics.lib.identity import make_identifier, get_rest_high_level_identity_api, get_rest_identity_api,\
    HighLevelIdentityApi, KeyPairSecretsHelper, RegisteredIdentity, SeedMethod

from iotics.lib.grpc.auth import AuthInterface


class IdentityAuthError(Exception):
    """Raised when `IdentityAuth` cannot be instantiated correctly."""


class IdentityAuth(AuthInterface):
    agent: RegisteredIdentity = None
    api: HighLevelIdentityApi = None
    grpc_url: str = None
    token_ttl: int = 30
    user_did: str = None

    def __init__(
        self,
        space: str,
        resolver_url: typing.Optional[str],
        user_did: str,
        agent_did: str,
        agent_key_name: str,
        agent_name: str,
        agent_secret: str,
        token_ttl: typing.Optional[str]
    ):
        split_url = space.partition('://')
        space = split_url[2] or split_url[0]
        self.grpc_url = space + ':10001'
        if not resolver_url:
            index_url = f'https://{space}/index.json'
            try:
                resolver_url = requests.get(index_url).json()['resolver']
            except requests.exceptions.ConnectionError:
                raise IdentityAuthError(f'Could not fetch resolver URL from `{index_url}`.')
        if token_ttl:
            self.token_ttl = int(token_ttl)
        if not agent_name.startswith('#'):
            agent_name = '#' + agent_name
        self.agent = self._get_agent(
            resolver_url,
            agent_did,
            agent_key_name,
            agent_name,
            agent_secret
        )
        self.api = get_rest_high_level_identity_api(resolver_url=resolver_url)
        self.grpc_token = self.api.create_agent_auth_token(
            self.agent, user_did, self.token_ttl
        )

    def get_host(self) -> str:
        return self.grpc_url

    def get_token(self, ttl: typing.Optional[int] = None) -> str:
        if self.grpc_token:
            return self.grpc_token

        self.refresh_token(ttl or self.token_ttl)
        return self.grpc_token

    def refresh_token(self, ttl: typing.Optional[int] = None):
        self.api.create_agent_auth_token(self.agent, self.user_did, ttl or self.token_ttl)

    def generate_twin_did(self, twin_name) -> str:
        # Reuse the agent secret seed for simplicity and ease of twin maintenance.
        seed = self.agent.key_pair_secrets.seed
        twin_registered_identity = self.api.create_twin_with_control_delegation(
            seed, twin_name, self.agent, '#AuthorityDelegation')
        return twin_registered_identity.did

    @staticmethod
    def _get_agent(resolver_url: str, agent_did: str, agent_key_name: str, agent_name: str, agent_secret: str):
        # Gets an agent identity using the provided credentials, taking into account that the agent DID may have been
        # generated using either of two SeedMethods
        agent_secret = bytes.fromhex(agent_secret)
        api = get_rest_identity_api(resolver_url)
        agent = api.get_agent_identity(
            agent_secret,
            agent_key_name,
            agent_did,
            agent_name
        )
        did_from_keys = make_identifier(KeyPairSecretsHelper.get_key_pair(agent.key_pair_secrets).public_bytes)
        if did_from_keys == agent_did:
            return agent
        return api.get_agent_identity(
            agent_secret,
            agent_key_name,
            agent_did,
            agent_name,
            SeedMethod.SEED_METHOD_NONE
        )
