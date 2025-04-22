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
from gotham.v1.gaia import models as gaia_models
from gotham.v1.gotham import models as gotham_models


class MapClient:
    """
    The API client for the Map Resource.

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

        self.with_streaming_response = _MapClientStreaming(self)
        self.with_raw_response = _MapClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_artifacts(
        self,
        map_rid: gaia_models.GaiaMapRid,
        *,
        artifact_gids: typing.List[gotham_models.ArtifactGid],
        label: str,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gaia_models.AddArtifactsToMapResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Add artifacts to a map. Currently only target collection artifacts may be added. If unknown artifacts
        or artifacts that don't satisfy the security requirements are provided, the entire request will fail.
        For each request, a new layer is created for each artifact, thus not idempotent.
        Returns the IDs of the layers created.

        :param map_rid: The RID of the Gaia map that you wish to add artifacts to.
        :type map_rid: GaiaMapRid
        :param artifact_gids: The GIDs of the artifacts to be added to the map.
        :type artifact_gids: List[ArtifactGid]
        :param label: The name of the layer to be created
        :type label: str
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gaia_models.AddArtifactsToMapResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/maps/{mapRid}/layers/artifacts",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mapRid": map_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "artifactGids": artifact_gids,
                    "label": label,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "artifactGids": typing.List[gotham_models.ArtifactGid],
                        "label": str,
                    },
                ),
                response_type=gaia_models.AddArtifactsToMapResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_enterprise_map_layers(
        self,
        map_rid: gaia_models.GaiaMapRid,
        *,
        eml_ids: typing.List[gaia_models.EmlId],
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gaia_models.AddEnterpriseMapLayersToMapResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Add enterprise map layers to a map. If unknown enterprise map layers or enterprise map layers that don't
        satisfy the security requirements are provided, the entire request will fail. For each request, a new layer
        is created for each enterprise map layer provided, thus not idempotent.
        Returns the IDs of the layers created.

        :param map_rid: The RID of the Gaia map that you wish to add objects to.
        :type map_rid: GaiaMapRid
        :param eml_ids: The IDs of the enterprise map layers to be added to the map.
        :type eml_ids: List[EmlId]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gaia_models.AddEnterpriseMapLayersToMapResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/maps/{mapRid}/layers/emls",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mapRid": map_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "emlIds": eml_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "emlIds": typing.List[gaia_models.EmlId],
                    },
                ),
                response_type=gaia_models.AddEnterpriseMapLayersToMapResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def add_objects(
        self,
        map_rid: gaia_models.GaiaMapRid,
        *,
        label: str,
        object_rids: typing.List[core.RID],
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gaia_models.AddObjectsToMapResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Add objects to a map. Currently only Foundry-managed object types may be added. If unknown objects
        or objects that don't satisfy the security requirements are provided, the entire request will fail.
        This creates a new layer that includes all the provided objects per request, thus not idempotent.
        Returns the ID of the layer created.

        :param map_rid: The RID of the Gaia map that you wish to add objects to.
        :type map_rid: GaiaMapRid
        :param label: The name of the layer to be created
        :type label: str
        :param object_rids:
        :type object_rids: List[RID]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gaia_models.AddObjectsToMapResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/maps/{mapRid}/layers/objects",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mapRid": map_rid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "objectRids": object_rids,
                    "label": label,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "objectRids": typing.List[core.RID],
                        "label": str,
                    },
                ),
                response_type=gaia_models.AddObjectsToMapResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def export_kmz(
        self,
        map_id: gaia_models.GaiaMapId,
        *,
        name: typing.Optional[str] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Export all map elements from a Gaia map to a KMZ file suitable for rendering in external applications, such as Google Earth. There are no schema compatibility guarantees provided for internal KMZ content exported by this endpoint.
        Only local map elements will be exported i.e. no elements from linked maps.

        :param map_id: The artifact identifier of the Gaia map being exported, which can be copied via **Help** > **Developer** > **Copy id**. The export call will download all elements in the referenced map.
        :type map_id: GaiaMapId
        :param name: The name of the exported file. Defaults to 'palantir-export'.
        :type name: Optional[str]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/maps/{mapId}/kmz",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mapId": map_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body={
                    "name": name,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "name": typing.Optional[str],
                    },
                ),
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load(
        self,
        map_gid: gaia_models.GaiaMapGid,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gaia_models.LoadMapResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Loads the structure and basic metadata of a Gaia map, given a map GID. Metadata includes the map's title and
        layer labels.

        The response contains a mapping of all layers contained in the map. The map's layer hierarchy can be recreated
        by using the `rootLayerIds` in the response along with the `subLayerIds` field in the layer's metadata.

        :param map_gid: The GID of the map to be loaded.
        :type map_gid: GaiaMapGid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gaia_models.LoadMapResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/maps/load/{mapGid}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mapGid": map_gid,
                },
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=gaia_models.LoadMapResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_layers(
        self,
        map_gid: gaia_models.GaiaMapGid,
        *,
        layer_ids: typing.List[gaia_models.GaiaLayerId],
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gaia_models.LoadLayersResponse:
        """
        Loads the elements contained in the requested layers of a Gaia map. The response includes the geometries
        associated with the elements.

        :param map_gid: The GID of the map containing the layers to be loaded.
        :type map_gid: GaiaMapGid
        :param layer_ids: The set of layer IDs to load from a Gaia map.
        :type layer_ids: List[GaiaLayerId]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gaia_models.LoadLayersResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/maps/load/{mapGid}/layers",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "mapGid": map_gid,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "layerIds": layer_ids,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "layerIds": typing.List[gaia_models.GaiaLayerId],
                    },
                ),
                response_type=gaia_models.LoadLayersResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def render_symbol(
        self,
        gaia_symbol: gaia_models.GaiaSymbol,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        Fetches the PNG for the given symbol identifier

        :param gaia_symbol: Body of the request
        :type gaia_symbol: GaiaSymbol
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/maps/rendering/symbol",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body=gaia_symbol,
                body_type=gaia_models.GaiaSymbol,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search(
        self,
        *,
        map_name: gaia_models.GaiaMapName,
        page_size: typing.Optional[gotham_models.PageSize] = None,
        page_token: typing.Optional[gotham_models.PageToken] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gaia_models.SearchMapsResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Retrieves all published maps containing the mapName (does not have to be exact).

        :param map_name: The name of the map(s) to be queried.
        :type map_name: GaiaMapName
        :param page_size: The maximum number of matching Gaia maps to return. Defaults to 50.
        :type page_size: Optional[PageSize]
        :param page_token: The page token indicates where to start paging. This should be omitted from the first page's request.
        :type page_token: Optional[PageToken]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gaia_models.SearchMapsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/maps",
                query_params={
                    "mapName": map_name,
                    "pageSize": page_size,
                    "pageToken": page_token,
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Accept": "application/json",
                },
                body=None,
                body_type=None,
                response_type=gaia_models.SearchMapsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MapClientRaw:
    def __init__(self, client: MapClient) -> None:
        def add_artifacts(_: gaia_models.AddArtifactsToMapResponse): ...
        def add_enterprise_map_layers(_: gaia_models.AddEnterpriseMapLayersToMapResponse): ...
        def add_objects(_: gaia_models.AddObjectsToMapResponse): ...
        def export_kmz(_: bytes): ...
        def load(_: gaia_models.LoadMapResponse): ...
        def load_layers(_: gaia_models.LoadLayersResponse): ...
        def render_symbol(_: bytes): ...
        def search(_: gaia_models.SearchMapsResponse): ...

        self.add_artifacts = core.with_raw_response(add_artifacts, client.add_artifacts)
        self.add_enterprise_map_layers = core.with_raw_response(
            add_enterprise_map_layers, client.add_enterprise_map_layers
        )
        self.add_objects = core.with_raw_response(add_objects, client.add_objects)
        self.export_kmz = core.with_raw_response(export_kmz, client.export_kmz)
        self.load = core.with_raw_response(load, client.load)
        self.load_layers = core.with_raw_response(load_layers, client.load_layers)
        self.render_symbol = core.with_raw_response(render_symbol, client.render_symbol)
        self.search = core.with_raw_response(search, client.search)


class _MapClientStreaming:
    def __init__(self, client: MapClient) -> None:
        def add_artifacts(_: gaia_models.AddArtifactsToMapResponse): ...
        def add_enterprise_map_layers(_: gaia_models.AddEnterpriseMapLayersToMapResponse): ...
        def add_objects(_: gaia_models.AddObjectsToMapResponse): ...
        def export_kmz(_: bytes): ...
        def load(_: gaia_models.LoadMapResponse): ...
        def load_layers(_: gaia_models.LoadLayersResponse): ...
        def render_symbol(_: bytes): ...
        def search(_: gaia_models.SearchMapsResponse): ...

        self.add_artifacts = core.with_streaming_response(add_artifacts, client.add_artifacts)
        self.add_enterprise_map_layers = core.with_streaming_response(
            add_enterprise_map_layers, client.add_enterprise_map_layers
        )
        self.add_objects = core.with_streaming_response(add_objects, client.add_objects)
        self.export_kmz = core.with_streaming_response(export_kmz, client.export_kmz)
        self.load = core.with_streaming_response(load, client.load)
        self.load_layers = core.with_streaming_response(load_layers, client.load_layers)
        self.render_symbol = core.with_streaming_response(render_symbol, client.render_symbol)
        self.search = core.with_streaming_response(search, client.search)
