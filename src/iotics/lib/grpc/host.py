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
from iotics.api import common_pb2
from iotics.api import host_pb2
from iotics.api import host_pb2_grpc
from iotics.lib.grpc.base import ApiBase
from iotics.lib.grpc.helpers import create_headers


class HostApi(ApiBase):
    stub_class = host_pb2_grpc.HostAPIStub
    stub: host_pb2_grpc.HostAPIStub

    def get_local_host_id(self, headers: typing.Optional[common_pb2.Headers] = None) -> host_pb2.GetHostIDResponse:
        """ get the id of the local host
        """
        request = host_pb2.GetHostIDRequest(
            headers=headers or create_headers(),
        )

        resp = self.stub.GetHostID(request)

        return resp
