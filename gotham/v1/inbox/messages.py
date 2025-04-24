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

import pydantic
import typing_extensions

from gotham import _core as core
from gotham import _errors as errors
from gotham.v1.gotham import models as gotham_models


class MessagesClient:
    """
    The API client for the Messages Resource.

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
        self._api_client = core.ApiClient(auth=auth, hostname=hostname, config=config)

        self.with_streaming_response = _MessagesClientStreaming(self)
        self.with_raw_response = _MessagesClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def send(
        self,
        *,
        messages: typing.List[gotham_models.SendMessageRequest],
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.SendMessagesResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Send messages in Global Inbox.

        Validation failure for any message will cause the entire request to throw before any messages are sent.

        The response reports all messages which were successfully sent, and any messages which failed to
        be sent due to a conflict with an existing message.

        Callers must be added to the internal "External Inbox Alert Producers" group in Gotham Security (multipass).

        Note that the recipient `realm` must be specified if the caller's `realm` is not identical. For
        example, to send to the "Everyone" group in the "palantir-internal-realm" realm, the caller must either specify the realm or already be
        in "palantir-internal-realm".

        :param messages:
        :type messages: List[SendMessageRequest]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.SendMessagesResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/inbox/messages",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "messages": messages,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "messages": typing.List[gotham_models.SendMessageRequest],
                    },
                ),
                response_type=gotham_models.SendMessagesResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MessagesClientRaw:
    def __init__(self, client: MessagesClient) -> None:
        def send(_: gotham_models.SendMessagesResponse): ...

        self.send = core.with_raw_response(send, client.send)


class _MessagesClientStreaming:
    def __init__(self, client: MessagesClient) -> None:
        def send(_: gotham_models.SendMessagesResponse): ...

        self.send = core.with_streaming_response(send, client.send)
