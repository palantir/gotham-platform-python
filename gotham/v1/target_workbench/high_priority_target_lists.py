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


class HighPriorityTargetListsClient:
    """
    The API client for the HighPriorityTargetLists Resource.

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

        self.with_streaming_response = _HighPriorityTargetListsClientStreaming(self)
        self.with_raw_response = _HighPriorityTargetListsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        name: str,
        security: gotham_models.ArtifactSecurity,
        target_aois: typing.List[gotham_models.HptlTargetAoi],
        targets: typing.List[gotham_models.HighPriorityTargetListTargetV2],
        area_geo: typing.Optional[gotham_models.GeoPolygon] = None,
        area_object_rid: typing.Optional[gotham_models.ObjectPrimaryKey] = None,
        description: typing.Optional[str] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        target_board: typing.Optional[gotham_models.TargetBoardRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.CreateHighPriorityTargetListResponseV2:
        """
        Create a High Priority Target List.
        Returns the RID of the created High Priority Target List.

        :param name:
        :type name: str
        :param security:
        :type security: ArtifactSecurity
        :param target_aois:
        :type target_aois: List[HptlTargetAoi]
        :param targets: A list of HighPriorityTargetListTargets
        :type targets: List[HighPriorityTargetListTargetV2]
        :param area_geo:
        :type area_geo: Optional[GeoPolygon]
        :param area_object_rid:
        :type area_object_rid: Optional[ObjectPrimaryKey]
        :param description:
        :type description: Optional[str]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param target_board:
        :type target_board: Optional[TargetBoardRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.CreateHighPriorityTargetListResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/twb/highPriorityTargetList",
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
                    "targetBoard": target_board,
                    "targets": targets,
                    "areaObjectRid": area_object_rid,
                    "areaGeo": area_geo,
                    "targetAois": target_aois,
                    "security": security,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": str,
                        "description": typing.Optional[str],
                        "targetBoard": typing.Optional[gotham_models.TargetBoardRid],
                        "targets": typing.List[gotham_models.HighPriorityTargetListTargetV2],
                        "areaObjectRid": typing.Optional[gotham_models.ObjectPrimaryKey],
                        "areaGeo": typing.Optional[gotham_models.GeoPolygon],
                        "targetAois": typing.List[gotham_models.HptlTargetAoi],
                        "security": gotham_models.ArtifactSecurity,
                    },
                ),
                response_type=gotham_models.CreateHighPriorityTargetListResponseV2,
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
        rid: gotham_models.HighPriorityTargetListRid,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.LoadHighPriorityTargetListResponseV2:
        """
        Load a High Priority Target List by RID.

        :param rid: High Priority Target List RID
        :type rid: HighPriorityTargetListRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.LoadHighPriorityTargetListResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/twb/highPriorityTargetList/{rid}",
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
                response_type=gotham_models.LoadHighPriorityTargetListResponseV2,
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
        rid: gotham_models.HighPriorityTargetListRid,
        *,
        base_revision_id: int,
        target_aois: typing.List[gotham_models.HptlTargetAoi],
        targets: typing.List[gotham_models.HighPriorityTargetListTargetV2],
        area_geo: typing.Optional[gotham_models.GeoPolygon] = None,
        area_object_rid: typing.Optional[gotham_models.ObjectPrimaryKey] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        target_board: typing.Optional[gotham_models.TargetBoardRid] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        Modify a High Priority Target List by RID.

        :param rid: High Priority Target List RID
        :type rid: HighPriorityTargetListRid
        :param base_revision_id: The current version of the HighPriorityTargetList to be modified. Any modifying operations should be accompanied by this version to avoid concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.
        :type base_revision_id: int
        :param target_aois:
        :type target_aois: List[HptlTargetAoi]
        :param targets: A list of HighPriorityTargetListTargets
        :type targets: List[HighPriorityTargetListTargetV2]
        :param area_geo:
        :type area_geo: Optional[GeoPolygon]
        :param area_object_rid:
        :type area_object_rid: Optional[ObjectPrimaryKey]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param target_board:
        :type target_board: Optional[TargetBoardRid]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/highPriorityTargetList/{rid}",
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
                    "targetBoard": target_board,
                    "targets": targets,
                    "areaObjectRid": area_object_rid,
                    "areaGeo": area_geo,
                    "targetAois": target_aois,
                    "baseRevisionId": base_revision_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "targetBoard": typing.Optional[gotham_models.TargetBoardRid],
                        "targets": typing.List[gotham_models.HighPriorityTargetListTargetV2],
                        "areaObjectRid": typing.Optional[gotham_models.ObjectPrimaryKey],
                        "areaGeo": typing.Optional[gotham_models.GeoPolygon],
                        "targetAois": typing.List[gotham_models.HptlTargetAoi],
                        "baseRevisionId": int,
                    },
                ),
                response_type=gotham_models.EmptySuccessResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _HighPriorityTargetListsClientRaw:
    def __init__(self, client: HighPriorityTargetListsClient) -> None:
        def create(_: gotham_models.CreateHighPriorityTargetListResponseV2): ...
        def get(_: gotham_models.LoadHighPriorityTargetListResponseV2): ...
        def update(_: gotham_models.EmptySuccessResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.get = core.with_raw_response(get, client.get)
        self.update = core.with_raw_response(update, client.update)


class _HighPriorityTargetListsClientStreaming:
    def __init__(self, client: HighPriorityTargetListsClient) -> None:
        def create(_: gotham_models.CreateHighPriorityTargetListResponseV2): ...
        def get(_: gotham_models.LoadHighPriorityTargetListResponseV2): ...
        def update(_: gotham_models.EmptySuccessResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.get = core.with_streaming_response(get, client.get)
        self.update = core.with_streaming_response(update, client.update)
