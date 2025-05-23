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


from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import Optional

import httpx

from gotham._core.config import Config


class Token(ABC):

    @property
    @abstractmethod
    def access_token(self) -> str:
        pass


class Auth(ABC):
    @abstractmethod
    def get_token(self) -> "Token":
        pass

    def _parameterize(self, hostname: str, config: Optional[Config]) -> None:
        pass

    @abstractmethod
    def execute_with_token(self, func: Callable[["Token"], httpx.Response]) -> httpx.Response:
        pass

    @abstractmethod
    def run_with_token(self, func: Callable[["Token"], httpx.Response]) -> None:
        pass
