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


class TargetBoardsClient:
    """
    The API client for the TargetBoards Resource.

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

        self.with_streaming_response = _TargetBoardsClientStreaming(self)
        self.with_raw_response = _TargetBoardsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: str,
        security: gotham_models.ArtifactSecurity,
        configuration: typing.Optional[gotham_models.TargetBoardConfiguration] = None,
        description: typing.Optional[str] = None,
        high_priority_target_list: typing.Optional[gotham_models.HighPriorityTargetListRid] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.CreateTargetBoardResponseV2:
        """
        By default, create a TargetBoard with default columns: IDENTIFIED TARGET, PRIORITIZED TARGET, IN COORDINATION, IN EXECUTION, COMPLETE.
        Returns the RID of the created TargetBoard.

        :param name:
        :type name: str
        :param security:
        :type security: ArtifactSecurity
        :param configuration:
        :type configuration: Optional[TargetBoardConfiguration]
        :param description:
        :type description: Optional[str]
        :param high_priority_target_list:
        :type high_priority_target_list: Optional[HighPriorityTargetListRid]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.CreateTargetBoardResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/twb/targetBoard",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "description": description,
                    "highPriorityTargetList": high_priority_target_list,
                    "configuration": configuration,
                    "security": security,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": str,
                        "description": typing.Optional[str],
                        "highPriorityTargetList": typing.Optional[
                            gotham_models.HighPriorityTargetListRid
                        ],
                        "configuration": typing.Optional[gotham_models.TargetBoardConfiguration],
                        "security": gotham_models.ArtifactSecurity,
                    },
                ),
                response_type=gotham_models.CreateTargetBoardResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def delete(
        self,
        rid: gotham_models.TargetBoardRid,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Archive a Collection by RID.

        :param rid: Target Board RID
        :type rid: TargetBoardRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/targetBoard/{rid}/archive",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "rid": rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=gotham_models.EmptySuccessResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def get(
        self,
        rid: gotham_models.TargetBoardRid,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.LoadTargetBoardResponseV2:
        """
        Load Target Board by RID.

        :param rid: Target Board RID
        :type rid: TargetBoardRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.LoadTargetBoardResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/twb/targetBoard/{rid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "rid": rid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=gotham_models.LoadTargetBoardResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_target_pucks(
        self,
        rid: gotham_models.TargetBoardRid,
        *,
        load_level: typing.List[gotham_models.TargetPuckLoadLevel],
        allow_stale_loads: typing.Optional[bool] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.LoadTargetPucksResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::
        Loads target pucks contained in a target board. The response may include the puck's associated location and
        board status metadata, depending on the load levels specified in the request.

        :param rid: Target Board RID to load target pucks from.
        :type rid: TargetBoardRid
        :param load_level: Determines the set of information to load for a given target puck.
        :type load_level: List[TargetPuckLoadLevel]
        :param allow_stale_loads: If set to true, will potentially load "stale" data associated with the target puck. Defaults to false. Note that even if the returned data is stale, the data will be stale in the order of minutes or less. Setting this option to true will yield better performance, especially for consumers that wish to poll this endpoint at a frequent interval.
        :type allow_stale_loads: Optional[bool]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.LoadTargetPucksResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/board/{rid}/loadTargetPucks",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "rid": rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "loadLevel": load_level,
                    "allowStaleLoads": allow_stale_loads,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "loadLevel": typing.List[gotham_models.TargetPuckLoadLevel],
                        "allowStaleLoads": typing.Optional[bool],
                    },
                ),
                response_type=gotham_models.LoadTargetPucksResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update(
        self,
        rid: gotham_models.TargetBoardRid,
        *,
        base_revision_id: core.Long,
        name: str,
        configuration: typing.Optional[gotham_models.TargetBoardConfiguration] = None,
        description: typing.Optional[str] = None,
        high_priority_target_list: typing.Optional[gotham_models.HighPriorityTargetListRid] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        Modify a Target Board by RID.

        :param rid: TargetBoard RID
        :type rid: TargetBoardRid
        :param base_revision_id: The current version of the Target Board to be modified. The archive operation will be transformed against any concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.
        :type base_revision_id: Long
        :param name:
        :type name: str
        :param configuration:
        :type configuration: Optional[TargetBoardConfiguration]
        :param description:
        :type description: Optional[str]
        :param high_priority_target_list:
        :type high_priority_target_list: Optional[HighPriorityTargetListRid]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/targetBoard/{rid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "rid": rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "name": name,
                    "description": description,
                    "highPriorityTargetList": high_priority_target_list,
                    "configuration": configuration,
                    "baseRevisionId": base_revision_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": str,
                        "description": typing.Optional[str],
                        "highPriorityTargetList": typing.Optional[
                            gotham_models.HighPriorityTargetListRid
                        ],
                        "configuration": typing.Optional[gotham_models.TargetBoardConfiguration],
                        "baseRevisionId": core.Long,
                    },
                ),
                response_type=gotham_models.EmptySuccessResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def update_target_column(
        self,
        target_rid: gotham_models.TargetRid,
        *,
        base_revision_id: core.Long,
        board_rid: gotham_models.TargetBoardRid,
        new_column_id: gotham_models.TargetBoardColumnId,
        client_id: typing.Optional[str] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        Move a Target into a TargetBoardColumn from an old column.

        :param target_rid:
        :type target_rid: TargetRid
        :param base_revision_id: The version of Target Board you are working with. The set operation will be transformed against any concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.
        :type base_revision_id: Long
        :param board_rid:
        :type board_rid: TargetBoardRid
        :param new_column_id:
        :type new_column_id: TargetBoardColumnId
        :param client_id: The client id is used to identify conflicting edits made by the same client, typically due to retries, and discard them. Clients should choose an arbitrary random identifier to distinguish themselves. There is no need persist and re-use the same client id over multiple sessions.  The client id is also used to avoid broadcasting operations to the client who submitted them.
        :type client_id: Optional[str]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/setTargetColumn/{targetRid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "targetRid": target_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "boardRid": board_rid,
                    "newColumnId": new_column_id,
                    "baseRevisionId": base_revision_id,
                    "clientId": client_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "boardRid": gotham_models.TargetBoardRid,
                        "newColumnId": gotham_models.TargetBoardColumnId,
                        "baseRevisionId": core.Long,
                        "clientId": typing.Optional[str],
                    },
                ),
                response_type=gotham_models.EmptySuccessResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _TargetBoardsClientRaw:
    def __init__(self, client: TargetBoardsClient) -> None:
        def create(_: gotham_models.CreateTargetBoardResponseV2): ...
        def delete(_: gotham_models.EmptySuccessResponse): ...
        def get(_: gotham_models.LoadTargetBoardResponseV2): ...
        def load_target_pucks(_: gotham_models.LoadTargetPucksResponse): ...
        def update(_: gotham_models.EmptySuccessResponse): ...
        def update_target_column(_: gotham_models.EmptySuccessResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.load_target_pucks = core.with_raw_response(load_target_pucks, client.load_target_pucks)
        self.update = core.with_raw_response(update, client.update)
        self.update_target_column = core.with_raw_response(
            update_target_column, client.update_target_column
        )


class _TargetBoardsClientStreaming:
    def __init__(self, client: TargetBoardsClient) -> None:
        def create(_: gotham_models.CreateTargetBoardResponseV2): ...
        def delete(_: gotham_models.EmptySuccessResponse): ...
        def get(_: gotham_models.LoadTargetBoardResponseV2): ...
        def load_target_pucks(_: gotham_models.LoadTargetPucksResponse): ...
        def update(_: gotham_models.EmptySuccessResponse): ...
        def update_target_column(_: gotham_models.EmptySuccessResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.delete = core.with_streaming_response(delete, client.delete)
        self.get = core.with_streaming_response(get, client.get)
        self.load_target_pucks = core.with_streaming_response(
            load_target_pucks, client.load_target_pucks
        )
        self.update = core.with_streaming_response(update, client.update)
        self.update_target_column = core.with_streaming_response(
            update_target_column, client.update_target_column
        )
