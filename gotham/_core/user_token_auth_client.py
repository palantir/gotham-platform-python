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


import os
from typing import Callable
from typing import TypeVar

import httpx

from gotham._core.auth_utils import Auth
from gotham._core.auth_utils import Token
from gotham._core.utils import assert_non_empty_string
from gotham._errors.environment_not_configured import EnvironmentNotConfigured
from gotham._errors.not_authenticated import NotAuthenticated

T = TypeVar("T")


class _UserToken(Token):

    def __init__(self, token: str) -> None:
        self._token = token

    @property
    def access_token(self) -> str:
        return self._token


class UserTokenAuth(Auth):
    def __init__(self, token: str) -> None:
        assert_non_empty_string(token, "token")
        self._token = _UserToken(token)

    def get_token(self) -> Token:
        if self._token is None:
            raise NotAuthenticated("Client has not been authenticated.")
        return self._token

    def execute_with_token(self, func: Callable[[Token], httpx.Response]) -> httpx.Response:
        return func(self.get_token())

    def run_with_token(self, func: Callable[[Token], httpx.Response]) -> None:
        func(self.get_token())
