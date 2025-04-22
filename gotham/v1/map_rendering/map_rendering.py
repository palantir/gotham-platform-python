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
from gotham.v1.map_rendering import models as map_rendering_models


class MapRenderingClient:
    """
    The API client for the MapRendering Resource.

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

        self.with_streaming_response = _MapRenderingClientStreaming(self)
        self.with_raw_response = _MapRenderingClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_generic_symbol(
        self,
        id: map_rendering_models.MrsGenericSymbolId,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        size: typing.Optional[int] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Loads a PNG format icon with the provided ID, resizing it if requested.
        This endpoint has the following features that make it more easily usable from browsers:
        - Respects the If-None-Match etag header, returning 304 if the icon is unchanged.
        - Will use a PALANTIR_TOKEN cookie if no authorization header was provided.
        - Returns Cache-Control and Content-Type headers.

        :param id: The generic symbol ID returned by the service that uniquely identifies a symbol.
        :type id: MrsGenericSymbolId
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param size: Resize the icon so that its reference size matches this value. The actually returned image may be larger or smaller than this value.
        :type size: Optional[int]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/maprendering/symbols/generic/{id}",
                query_params={
                    "preview": preview,
                    "size": size,
                },
                path_params={
                    "id": id,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def load_resource_tile(
        self,
        tileset: map_rendering_models.TilesetId,
        zoom: int,
        x_coordinate: int,
        y_coordinate: int,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> bytes:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Loads a tile from the provided tileset at the provided coordinates.
        This endpoint has the following features that make it more easily usable from browsers:
        - Respects the If-None-Match etag header, returning 304 if the tile is unchanged.
        - Will use a PALANTIR_TOKEN cookie if no authorization header was provided.
        - Returns Cache-Control and Content-Type headers.

        :param tileset:
        :type tileset: TilesetId
        :param zoom:
        :type zoom: int
        :param x_coordinate:
        :type x_coordinate: int
        :param y_coordinate:
        :type y_coordinate: int
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: bytes
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="GET",
                resource_path="/gotham/v1/maprendering/resources/tiles/{tileset}/{zoom}/{xCoordinate}/{yCoordinate}",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "tileset": tileset,
                    "zoom": zoom,
                    "xCoordinate": x_coordinate,
                    "yCoordinate": y_coordinate,
                },
                header_params={
                    "Accept": "*/*",
                },
                body=None,
                body_type=None,
                response_type=bytes,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def render_objects(
        self,
        *,
        capabilities: map_rendering_models.ClientCapabilities,
        invocations: typing.List[map_rendering_models.Invocation],
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> map_rendering_models.RenderObjectsResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Stateless api to fetch a snapshot of renderables for a given object set. Only includes initial renderable values
        in snapshot, does not reflect changes made while rendering.

        :param capabilities:
        :type capabilities: ClientCapabilities
        :param invocations:
        :type invocations: List[Invocation]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: map_rendering_models.RenderObjectsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="PUT",
                resource_path="/gotham/v1/maprendering/render",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "capabilities": capabilities,
                    "invocations": invocations,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "capabilities": map_rendering_models.ClientCapabilities,
                        "invocations": typing.List[map_rendering_models.Invocation],
                    },
                ),
                response_type=map_rendering_models.RenderObjectsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _MapRenderingClientRaw:
    def __init__(self, client: MapRenderingClient) -> None:
        def load_generic_symbol(_: bytes): ...
        def load_resource_tile(_: bytes): ...
        def render_objects(_: map_rendering_models.RenderObjectsResponse): ...

        self.load_generic_symbol = core.with_raw_response(
            load_generic_symbol, client.load_generic_symbol
        )
        self.load_resource_tile = core.with_raw_response(
            load_resource_tile, client.load_resource_tile
        )
        self.render_objects = core.with_raw_response(render_objects, client.render_objects)


class _MapRenderingClientStreaming:
    def __init__(self, client: MapRenderingClient) -> None:
        def load_generic_symbol(_: bytes): ...
        def load_resource_tile(_: bytes): ...
        def render_objects(_: map_rendering_models.RenderObjectsResponse): ...

        self.load_generic_symbol = core.with_streaming_response(
            load_generic_symbol, client.load_generic_symbol
        )
        self.load_resource_tile = core.with_streaming_response(
            load_resource_tile, client.load_resource_tile
        )
        self.render_objects = core.with_streaming_response(render_objects, client.render_objects)
