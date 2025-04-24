#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import typing

from gotham import _core as core


class GothamClient:
    """
    The Foundry V1 API client.

    :param auth: Your auth configuration.
    :param hostname: Your Foundry hostname (for example, "myfoundry.palantirfoundry.com"). This can also include your API gateway service URI.
    :param config: Optionally specify the configuration for the HTTP session.
    """

    def __init__(
        self,
        auth: core.Auth,
        hostname: str,
        config: typing.Optional[core.Config] = None,
    ):
        from gotham.v1.federated_sources._client import FederatedSourcesClient
        from gotham.v1.gaia._client import GaiaClient
        from gotham.v1.geotime._client import GeotimeClient
        from gotham.v1.inbox._client import InboxClient
        from gotham.v1.map_rendering._client import MapRenderingClient
        from gotham.v1.media._client import MediaClient
        from gotham.v1.target_workbench._client import TargetWorkbenchClient

        self.federated_sources = FederatedSourcesClient(auth=auth, hostname=hostname, config=config)
        self.gaia = GaiaClient(auth=auth, hostname=hostname, config=config)
        self.geotime = GeotimeClient(auth=auth, hostname=hostname, config=config)
        self.inbox = InboxClient(auth=auth, hostname=hostname, config=config)
        self.map_rendering = MapRenderingClient(auth=auth, hostname=hostname, config=config)
        self.media = MediaClient(auth=auth, hostname=hostname, config=config)
        self.target_workbench = TargetWorkbenchClient(auth=auth, hostname=hostname, config=config)
