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


from gotham._core import ApiResponse
from gotham._core import Auth
from gotham._core import ConfidentialClientAuth
from gotham._core import Config
from gotham._core import PublicClientAuth
from gotham._core import ResourceIterator
from gotham._core import StreamedApiResponse
from gotham._core import StreamingContextManager
from gotham._core import UserTokenAuth
from gotham._errors import ApiNotFoundError
from gotham._errors import BadRequestError
from gotham._errors import ConflictError
from gotham._errors import ConnectionError
from gotham._errors import ConnectTimeout
from gotham._errors import EnvironmentNotConfigured
from gotham._errors import InternalServerError
from gotham._errors import NotAuthenticated
from gotham._errors import NotFoundError
from gotham._errors import PalantirException
from gotham._errors import PalantirRPCException
from gotham._errors import PermissionDeniedError
from gotham._errors import ProxyError
from gotham._errors import RateLimitError
from gotham._errors import ReadTimeout
from gotham._errors import RequestEntityTooLargeError
from gotham._errors import SDKInternalError
from gotham._errors import StreamConsumedError
from gotham._errors import TimeoutError
from gotham._errors import UnauthorizedError
from gotham._errors import UnprocessableEntityError
from gotham._errors import WriteTimeout

# The OpenAPI document version from the spec information
# See https://swagger.io/specification/#info-object
# The SDK version
from gotham._versions import __openapi_document_version__
from gotham._versions import __version__
from gotham.v1 import GothamClient

# The OpenAPI specification version
# See https://swagger.io/specification/#versions


__all__ = [
    "__version__",
    "__openapi_document_version__",
    "Auth",
    "ConfidentialClientAuth",
    "PublicClientAuth",
    "UserTokenAuth",
    "Config",
    "PalantirException",
    "EnvironmentNotConfigured",
    "NotAuthenticated",
    "ConnectionError",
    "ProxyError",
    "PalantirRPCException",
    "BadRequestError",
    "UnauthorizedError",
    "PermissionDeniedError",
    "NotFoundError",
    "UnprocessableEntityError",
    "RateLimitError",
    "RequestEntityTooLargeError",
    "ConflictError",
    "InternalServerError",
    "SDKInternalError",
    "StreamConsumedError",
    "ConnectTimeout",
    "ReadTimeout",
    "WriteTimeout",
    "TimeoutError",
    "ApiNotFoundError",
    "GothamClient",
]
