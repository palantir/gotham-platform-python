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


from gotham._errors.api_not_found import ApiNotFoundError
from gotham._errors.connection_error import ConnectionError
from gotham._errors.connection_error import ProxyError
from gotham._errors.environment_not_configured import EnvironmentNotConfigured
from gotham._errors.not_authenticated import NotAuthenticated
from gotham._errors.palantir_exception import PalantirException
from gotham._errors.palantir_rpc_exception import BadRequestError
from gotham._errors.palantir_rpc_exception import ConflictError
from gotham._errors.palantir_rpc_exception import InternalServerError
from gotham._errors.palantir_rpc_exception import NotFoundError
from gotham._errors.palantir_rpc_exception import PalantirRPCException
from gotham._errors.palantir_rpc_exception import PermissionDeniedError
from gotham._errors.palantir_rpc_exception import RateLimitError
from gotham._errors.palantir_rpc_exception import RequestEntityTooLargeError
from gotham._errors.palantir_rpc_exception import UnauthorizedError
from gotham._errors.palantir_rpc_exception import UnprocessableEntityError
from gotham._errors.sdk_internal_error import SDKInternalError
from gotham._errors.sdk_internal_error import handle_unexpected
from gotham._errors.stream_error import StreamConsumedError
from gotham._errors.timeout_error import ConnectTimeout
from gotham._errors.timeout_error import ReadTimeout
from gotham._errors.timeout_error import TimeoutError
from gotham._errors.timeout_error import WriteTimeout
from gotham._errors.utils import deserialize_error
