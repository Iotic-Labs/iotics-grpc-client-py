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

import grpc

from iotics.api import common_pb2, input_pb2
from iotics.lib.grpc.auth import AuthInterface
from iotics.lib.grpc.helpers import get_channel


class ApiBase:
    stub_class = None

    def __init__(self, auth: AuthInterface, channel: typing.Optional[grpc.Channel] = None):
        channel = channel or get_channel(auth)
        self.stub = self.stub_class(channel)
        self.address = auth.get_host()
        self.token = auth.get_token()
