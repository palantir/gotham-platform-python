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
from functools import cached_property

from gotham import _core as core


class TargetWorkbenchClient:
    """
    The API client for the TargetWorkbench Namespace.

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
        self._auth = auth
        self._hostname = hostname
        self._config = config

    @cached_property
    def HighPriorityTargetLists(self):
        from gotham.v1.target_workbench.high_priority_target_lists import (
            HighPriorityTargetListsClient,
        )  # NOQA

        return HighPriorityTargetListsClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def TargetBoards(self):
        from gotham.v1.target_workbench.target_boards import TargetBoardsClient

        return TargetBoardsClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )

    @cached_property
    def Targets(self):
        from gotham.v1.target_workbench.targets import TargetsClient

        return TargetsClient(
            auth=self._auth,
            hostname=self._hostname,
            config=self._config,
        )
