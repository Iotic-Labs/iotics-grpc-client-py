# Copyright © 2022 IOTIC LABS LTD. info@iotics.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/Iotic-Labs/iotics-grpc-client-py/blob/main/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import typing


class AuthInterface:
    """Authenticator for gRPC requests to IOTICSpace."""

    def get_host(self) -> str:
        """Provides a host name of an IOTICSpace.

        Returns: IOTICSpace host name and gRPC port.
        """
        raise NotImplementedError

    def get_token(self, ttl: typing.Optional[int]) -> str:
        """Provides an authentication token for a gRPC requests.
        Once generated, will return the same one until refresh_token is called.

        Returns: Encoded JSON Web Token.
        """
        raise NotImplementedError

    def refresh_token(self, ttl: typing.Optional[int]) -> str:
        """Provides a new authentication token for a gRPC requests.

        Returns: Encoded JSON Web Token.
        """
        raise NotImplementedError
