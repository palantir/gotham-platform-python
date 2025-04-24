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


class TargetsClient:
    """
    The API client for the Targets Resource.

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

        self.with_streaming_response = _TargetsClientStreaming(self)
        self.with_raw_response = _TargetsClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create(
        self,
        *,
        aimpoints: typing.List[gotham_models.TargetAimpointV2],
        column: gotham_models.TargetBoardColumnId,
        name: str,
        security: gotham_models.ArtifactSecurity,
        target_board: gotham_models.TargetBoardRid,
        description: typing.Optional[str] = None,
        entity_rid: typing.Optional[gotham_models.ObjectPrimaryKey] = None,
        high_priority_target_list_target_subtype: typing.Optional[
            gotham_models.HptlTargetSubtype
        ] = None,
        location: typing.Optional[gotham_models.LocationSource] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        sidc: typing.Optional[str] = None,
        target_identifier: typing.Optional[gotham_models.TargetIdentifier] = None,
        target_type: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.CreateTargetResponseV2:
        """
        Create a Target.
        Returns the RID of the created Target.

        If `sidc` field is specified and invalid according to MIL-STD-2525C specification,
        an `InvalidSidc` error is thrown.

        :param aimpoints:
        :type aimpoints: List[TargetAimpointV2]
        :param column:
        :type column: TargetBoardColumnId
        :param name:
        :type name: str
        :param security:
        :type security: ArtifactSecurity
        :param target_board:
        :type target_board: TargetBoardRid
        :param description:
        :type description: Optional[str]
        :param entity_rid:
        :type entity_rid: Optional[ObjectPrimaryKey]
        :param high_priority_target_list_target_subtype:
        :type high_priority_target_list_target_subtype: Optional[HptlTargetSubtype]
        :param location:
        :type location: Optional[LocationSource]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param sidc: MIL-STD 2525C Symbol Identification Code
        :type sidc: Optional[str]
        :param target_identifier:
        :type target_identifier: Optional[TargetIdentifier]
        :param target_type: The resource type of the target. Example: Building
        :type target_type: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.CreateTargetResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/twb/target",
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
                    "column": column,
                    "targetType": target_type,
                    "entityRid": entity_rid,
                    "sidc": sidc,
                    "targetIdentifier": target_identifier,
                    "location": location,
                    "highPriorityTargetListTargetSubtype": high_priority_target_list_target_subtype,
                    "aimpoints": aimpoints,
                    "security": security,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": str,
                        "description": typing.Optional[str],
                        "targetBoard": gotham_models.TargetBoardRid,
                        "column": gotham_models.TargetBoardColumnId,
                        "targetType": typing.Optional[str],
                        "entityRid": typing.Optional[gotham_models.ObjectPrimaryKey],
                        "sidc": typing.Optional[str],
                        "targetIdentifier": typing.Optional[gotham_models.TargetIdentifier],
                        "location": typing.Optional[gotham_models.LocationSource],
                        "highPriorityTargetListTargetSubtype": typing.Optional[
                            gotham_models.HptlTargetSubtype
                        ],
                        "aimpoints": typing.List[gotham_models.TargetAimpointV2],
                        "security": gotham_models.ArtifactSecurity,
                    },
                ),
                response_type=gotham_models.CreateTargetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def create_intel(
        self,
        rid: gotham_models.TargetRid,
        *,
        domain: gotham_models.IntelDomain,
        id: gotham_models.IntelId,
        intel_type: gotham_models.IntelUnion,
        name: str,
        valid_time: core.AwareDatetime,
        confidence: typing.Optional[float] = None,
        description: typing.Optional[str] = None,
        location: typing.Optional[gotham_models.GeoCircle] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        source: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        Create Intel on Target by RID

        :param rid: Target RID
        :type rid: TargetRid
        :param domain:
        :type domain: IntelDomain
        :param id:
        :type id: IntelId
        :param intel_type:
        :type intel_type: IntelUnion
        :param name:
        :type name: str
        :param valid_time:
        :type valid_time: datetime
        :param confidence:
        :type confidence: Optional[float]
        :param description:
        :type description: Optional[str]
        :param location:
        :type location: Optional[GeoCircle]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param source:
        :type source: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/createTargetIntel/{rid}",
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
                    "id": id,
                    "name": name,
                    "description": description,
                    "domain": domain,
                    "validTime": valid_time,
                    "location": location,
                    "confidence": confidence,
                    "intelType": intel_type,
                    "source": source,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "id": gotham_models.IntelId,
                        "name": str,
                        "description": typing.Optional[str],
                        "domain": gotham_models.IntelDomain,
                        "validTime": core.AwareDatetime,
                        "location": typing.Optional[gotham_models.GeoCircle],
                        "confidence": typing.Optional[float],
                        "intelType": gotham_models.IntelUnion,
                        "source": typing.Optional[str],
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
    def delete(
        self,
        rid: gotham_models.TargetRid,
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

        Archive a Target by RID.
        The user is required to have OWN permissions on the target.

        :param rid: Target RID
        :type rid: TargetRid
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
                resource_path="/gotham/v1/twb/target/{rid}/archive",
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
        rid: gotham_models.TargetRid,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.LoadTargetResponseV2:
        """
        Load a Target by RID.

        :param rid: Target RID
        :type rid: TargetRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.LoadTargetResponseV2
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/twb/target/{rid}",
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
                response_type=gotham_models.LoadTargetResponseV2,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def remove_intel(
        self,
        rid: gotham_models.TargetRid,
        *,
        id: gotham_models.IntelId,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        Remove Intel on Target by RID

        :param rid: Target RID
        :type rid: TargetRid
        :param id:
        :type id: IntelId
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
                resource_path="/gotham/v1/twb/removeTargetIntel/{rid}",
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
                    "id": id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "id": gotham_models.IntelId,
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
    def update(
        self,
        rid: gotham_models.TargetRid,
        *,
        aimpoints: typing.List[gotham_models.TargetAimpointV2],
        base_revision_id: core.Long,
        name: str,
        client_id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        entity_rid: typing.Optional[gotham_models.ObjectPrimaryKey] = None,
        high_priority_target_list_target_subtype: typing.Optional[
            gotham_models.HptlTargetSubtype
        ] = None,
        location: typing.Optional[gotham_models.LocationSource] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        sidc: typing.Optional[str] = None,
        target_identifier: typing.Optional[gotham_models.TargetIdentifier] = None,
        target_type: typing.Optional[str] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        Set current state of Target by RID.

        If `sidc` field is specified and invalid according to MIL-STD-2525C specification,
        an `InvalidSidc` error is thrown.

        :param rid: Target RID
        :type rid: TargetRid
        :param aimpoints:
        :type aimpoints: List[TargetAimpointV2]
        :param base_revision_id: The version of the Target to be modified. The modifying operations will be transformed against any concurrent operations made since this version.   If the supplied version is outdated, the server will respond back with RevisionTooOld exception and the client must resend the request with the updated baseRevisionId.
        :type base_revision_id: Long
        :param name:
        :type name: str
        :param client_id: The client id is used to identify conflicting edits made by the same client, typically due to retries, and discard them. Clients should choose an arbitrary random identifier to distinguish themselves. There is no need persist and re-use the same client id over multiple sessions.  The client id is also used to avoid broadcasting operations to the client who submitted them.
        :type client_id: Optional[str]
        :param description:
        :type description: Optional[str]
        :param entity_rid:
        :type entity_rid: Optional[ObjectPrimaryKey]
        :param high_priority_target_list_target_subtype:
        :type high_priority_target_list_target_subtype: Optional[HptlTargetSubtype]
        :param location:
        :type location: Optional[LocationSource]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param sidc: MIL-STD 2525C Symbol Identification Code
        :type sidc: Optional[str]
        :param target_identifier:
        :type target_identifier: Optional[TargetIdentifier]
        :param target_type: The resource type of the target. Example: Building
        :type target_type: Optional[str]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/twb/target/{rid}",
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
                    "targetType": target_type,
                    "entityRid": entity_rid,
                    "sidc": sidc,
                    "targetIdentifier": target_identifier,
                    "location": location,
                    "highPriorityTargetListTargetSubtype": high_priority_target_list_target_subtype,
                    "aimpoints": aimpoints,
                    "baseRevisionId": base_revision_id,
                    "clientId": client_id,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": str,
                        "description": typing.Optional[str],
                        "targetType": typing.Optional[str],
                        "entityRid": typing.Optional[gotham_models.ObjectPrimaryKey],
                        "sidc": typing.Optional[str],
                        "targetIdentifier": typing.Optional[gotham_models.TargetIdentifier],
                        "location": typing.Optional[gotham_models.LocationSource],
                        "highPriorityTargetListTargetSubtype": typing.Optional[
                            gotham_models.HptlTargetSubtype
                        ],
                        "aimpoints": typing.List[gotham_models.TargetAimpointV2],
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


class _TargetsClientRaw:
    def __init__(self, client: TargetsClient) -> None:
        def create(_: gotham_models.CreateTargetResponseV2): ...
        def create_intel(_: gotham_models.EmptySuccessResponse): ...
        def delete(_: gotham_models.EmptySuccessResponse): ...
        def get(_: gotham_models.LoadTargetResponseV2): ...
        def remove_intel(_: gotham_models.EmptySuccessResponse): ...
        def update(_: gotham_models.EmptySuccessResponse): ...

        self.create = core.with_raw_response(create, client.create)
        self.create_intel = core.with_raw_response(create_intel, client.create_intel)
        self.delete = core.with_raw_response(delete, client.delete)
        self.get = core.with_raw_response(get, client.get)
        self.remove_intel = core.with_raw_response(remove_intel, client.remove_intel)
        self.update = core.with_raw_response(update, client.update)


class _TargetsClientStreaming:
    def __init__(self, client: TargetsClient) -> None:
        def create(_: gotham_models.CreateTargetResponseV2): ...
        def create_intel(_: gotham_models.EmptySuccessResponse): ...
        def delete(_: gotham_models.EmptySuccessResponse): ...
        def get(_: gotham_models.LoadTargetResponseV2): ...
        def remove_intel(_: gotham_models.EmptySuccessResponse): ...
        def update(_: gotham_models.EmptySuccessResponse): ...

        self.create = core.with_streaming_response(create, client.create)
        self.create_intel = core.with_streaming_response(create_intel, client.create_intel)
        self.delete = core.with_streaming_response(delete, client.delete)
        self.get = core.with_streaming_response(get, client.get)
        self.remove_intel = core.with_streaming_response(remove_intel, client.remove_intel)
        self.update = core.with_streaming_response(update, client.update)
