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


from __future__ import annotations

import dataclasses
import io
import json
import os
import typing
from datetime import datetime

import click

import gotham.v1


@dataclasses.dataclass
class _Context:
    obj: gotham.v1.FoundryClient


def get_from_environ(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise gotham.EnvironmentNotConfigured(f"Please set {key} using `export {key}=<{key}>`")

    return value


@click.group()  # type: ignore
@click.pass_context  # type: ignore
def cli(ctx: _Context):
    "An experimental CLI for the Foundry API"
    ctx.obj = gotham.v1.FoundryClient(
        auth=gotham.UserTokenAuth(token=get_from_environ("FOUNDRY_TOKEN")),
        hostname=get_from_environ("FOUNDRY_HOSTNAME"),
    )


@cli.group("federated_sources")
def federated_sources():
    pass


@federated_sources.group("federated_source")
def federated_sources_federated_source():
    pass


@federated_sources_federated_source.command("list")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def federated_sources_federated_source_list(
    client: gotham.v1.FoundryClient,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Get a list of all federated sources.

    """
    result = client.federated_sources.FederatedSource.list(
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("foundry")
def foundry():
    pass


@cli.group("gaia")
def gaia():
    pass


@gaia.group("map")
def gaia_map():
    pass


@gaia_map.command("add_artifacts")
@click.argument("map_rid", type=str, required=True)
@click.option(
    "--artifact_gids",
    type=str,
    required=True,
    help="""The GIDs of the artifacts to be added to the map.
""",
)
@click.option(
    "--label",
    type=str,
    required=True,
    help="""The name of the layer to be created
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_add_artifacts(
    client: gotham.v1.FoundryClient,
    map_rid: str,
    artifact_gids: str,
    label: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Add artifacts to a map. Currently only target collection artifacts may be added. If unknown artifacts
    or artifacts that don't satisfy the security requirements are provided, the entire request will fail.
    For each request, a new layer is created for each artifact, thus not idempotent.
    Returns the IDs of the layers created.

    """
    result = client.gaia.Map.add_artifacts(
        map_rid=map_rid,
        artifact_gids=json.loads(artifact_gids),
        label=label,
        preview=preview,
    )
    click.echo(repr(result))


@gaia_map.command("add_enterprise_map_layers")
@click.argument("map_rid", type=str, required=True)
@click.option(
    "--eml_ids",
    type=str,
    required=True,
    help="""The IDs of the enterprise map layers to be added to the map.
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_add_enterprise_map_layers(
    client: gotham.v1.FoundryClient,
    map_rid: str,
    eml_ids: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Add enterprise map layers to a map. If unknown enterprise map layers or enterprise map layers that don't
    satisfy the security requirements are provided, the entire request will fail. For each request, a new layer
    is created for each enterprise map layer provided, thus not idempotent.
    Returns the IDs of the layers created.

    """
    result = client.gaia.Map.add_enterprise_map_layers(
        map_rid=map_rid,
        eml_ids=json.loads(eml_ids),
        preview=preview,
    )
    click.echo(repr(result))


@gaia_map.command("add_objects")
@click.argument("map_rid", type=str, required=True)
@click.option(
    "--label",
    type=str,
    required=True,
    help="""The name of the layer to be created
""",
)
@click.option("--object_rids", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_add_objects(
    client: gotham.v1.FoundryClient,
    map_rid: str,
    label: str,
    object_rids: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Add objects to a map. Currently only Foundry-managed object types may be added. If unknown objects
    or objects that don't satisfy the security requirements are provided, the entire request will fail.
    This creates a new layer that includes all the provided objects per request, thus not idempotent.
    Returns the ID of the layer created.

    """
    result = client.gaia.Map.add_objects(
        map_rid=map_rid,
        label=label,
        object_rids=json.loads(object_rids),
        preview=preview,
    )
    click.echo(repr(result))


@gaia_map.command("export_kmz")
@click.argument("map_id", type=str, required=True)
@click.option(
    "--name",
    type=str,
    required=False,
    help="""The name of the exported file. Defaults to 'palantir-export'.
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_export_kmz(
    client: gotham.v1.FoundryClient,
    map_id: str,
    name: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Export all map elements from a Gaia map to a KMZ file suitable for rendering in external applications, such as Google Earth. There are no schema compatibility guarantees provided for internal KMZ content exported by this endpoint.
    Only local map elements will be exported i.e. no elements from linked maps.

    """
    result = client.gaia.Map.export_kmz(
        map_id=map_id,
        name=name,
        preview=preview,
    )
    click.echo(result)


@gaia_map.command("load")
@click.argument("map_gid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_load(
    client: gotham.v1.FoundryClient,
    map_gid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Loads the structure and basic metadata of a Gaia map, given a map GID. Metadata includes the map's title and
    layer labels.

    The response contains a mapping of all layers contained in the map. The map's layer hierarchy can be recreated
    by using the `rootLayerIds` in the response along with the `subLayerIds` field in the layer's metadata.

    """
    result = client.gaia.Map.load(
        map_gid=map_gid,
        preview=preview,
    )
    click.echo(repr(result))


@gaia_map.command("load_layers")
@click.argument("map_gid", type=str, required=True)
@click.option(
    "--layer_ids",
    type=str,
    required=True,
    help="""The set of layer IDs to load from a Gaia map.
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_load_layers(
    client: gotham.v1.FoundryClient,
    map_gid: str,
    layer_ids: str,
    preview: typing.Optional[bool],
):
    """
    Loads the elements contained in the requested layers of a Gaia map. The response includes the geometries
    associated with the elements.

    """
    result = client.gaia.Map.load_layers(
        map_gid=map_gid,
        layer_ids=json.loads(layer_ids),
        preview=preview,
    )
    click.echo(repr(result))


@gaia_map.command("render_symbol")
@click.argument("gaia_symbol", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_render_symbol(
    client: gotham.v1.FoundryClient,
    gaia_symbol: str,
    preview: typing.Optional[bool],
):
    """
    Fetches the PNG for the given symbol identifier

    """
    result = client.gaia.Map.render_symbol(
        gaia_symbol=json.loads(gaia_symbol),
        preview=preview,
    )
    click.echo(result)


@gaia_map.command("search")
@click.option(
    "--map_name",
    type=str,
    required=True,
    help="""The name of the map(s) to be queried.
""",
)
@click.option(
    "--page_size",
    type=int,
    required=False,
    help="""The maximum number of matching Gaia maps to return. Defaults to 50.
""",
)
@click.option(
    "--page_token",
    type=str,
    required=False,
    help="""The page token indicates where to start paging. This should be omitted from the first page's request.
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def gaia_map_search(
    client: gotham.v1.FoundryClient,
    map_name: str,
    page_size: typing.Optional[int],
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Retrieves all published maps containing the mapName (does not have to be exact).

    """
    result = client.gaia.Map.search(
        map_name=map_name,
        page_size=page_size,
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("geotime")
def geotime():
    pass


@geotime.group("geotime")
def geotime_geotime():
    pass


@geotime_geotime.command("link_track_and_object")
@click.option("--object_rid", type=str, required=True, help="""""")
@click.option("--track_rid", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_link_track_and_object(
    client: gotham.v1.FoundryClient,
    object_rid: str,
    track_rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Links a Geotime Track with an Object, by ensuring that the Track has a "pointer"
    to its Object, and vice versa.

    """
    result = client.geotime.Geotime.link_track_and_object(
        object_rid=object_rid,
        track_rid=track_rid,
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("link_tracks")
@click.option("--other_track_rid", type=str, required=True, help="""""")
@click.option("--track_rid", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_link_tracks(
    client: gotham.v1.FoundryClient,
    other_track_rid: str,
    track_rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Links a Geotime Track with another Track, by ensuring that the Tracks have "pointers" to each other.

    """
    result = client.geotime.Geotime.link_tracks(
        other_track_rid=other_track_rid,
        track_rid=track_rid,
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("put_convolution_metadata")
@click.option("--convolutions", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_put_convolution_metadata(
    client: gotham.v1.FoundryClient,
    convolutions: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Stores metadata about a convolved ellipse.

    """
    result = client.geotime.Geotime.put_convolution_metadata(
        convolutions=json.loads(convolutions),
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("search_latest_observations")
@click.argument("observation_spec_id", type=str, required=True)
@click.option("--query", type=str, required=True, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_search_latest_observations(
    client: gotham.v1.FoundryClient,
    observation_spec_id: str,
    query: str,
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Gets the latest Observation along each Geotime Track matching the supplied query. Only returns Observations
    conforming to the given Observation Spec.

    """
    result = client.geotime.Geotime.search_latest_observations(
        observation_spec_id=observation_spec_id,
        query=json.loads(query),
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("search_observation_histories")
@click.argument("observation_spec_id", type=str, required=True)
@click.option("--query", type=str, required=True, help="""""")
@click.option("--history_window", type=str, required=False, help="""""")
@click.option("--page_token", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_search_observation_histories(
    client: gotham.v1.FoundryClient,
    observation_spec_id: str,
    query: str,
    history_window: typing.Optional[str],
    page_token: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Gets clipped Observation histories along each Geotime Track matching the supplied query. Histories are clipped
    based on the supplied history window. If no history window is supplied, a default history window of the past
    7 days is used. Only returns Observations conforming to the given Observation Spec.

    """
    result = client.geotime.Geotime.search_observation_histories(
        observation_spec_id=observation_spec_id,
        query=json.loads(query),
        history_window=None if history_window is None else json.loads(history_window),
        page_token=page_token,
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("unlink_track_and_object")
@click.option("--object_rid", type=str, required=True, help="""""")
@click.option("--track_rid", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_unlink_track_and_object(
    client: gotham.v1.FoundryClient,
    object_rid: str,
    track_rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Unlinks a Geotime Track from an Object, by ensuring that we remove any "pointers" between the Track and Object

    """
    result = client.geotime.Geotime.unlink_track_and_object(
        object_rid=object_rid,
        track_rid=track_rid,
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("unlink_tracks")
@click.option("--other_track_rid", type=str, required=True, help="""""")
@click.option("--track_rid", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_unlink_tracks(
    client: gotham.v1.FoundryClient,
    other_track_rid: str,
    track_rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Unlinks a Geotime Track from another Track, removing any "pointers" between the Tracks.

    """
    result = client.geotime.Geotime.unlink_tracks(
        other_track_rid=other_track_rid,
        track_rid=track_rid,
        preview=preview,
    )
    click.echo(repr(result))


@geotime_geotime.command("write_observations")
@click.argument("write_observations_request", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def geotime_geotime_write_observations(
    client: gotham.v1.FoundryClient,
    write_observations_request: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Writes Observations directly to Geotime. Returns the Observations that could not be written to Geotime with the
    reason for why they could not be written. Any Observations not in the response are guaranteed to have been
    written successfully to Geotime's backing data store.

    """
    result = client.geotime.Geotime.write_observations(
        write_observations_request=json.loads(write_observations_request),
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("gotham")
def gotham():
    pass


@cli.group("inbox")
def inbox():
    pass


@inbox.group("messages")
def inbox_messages():
    pass


@inbox_messages.command("send")
@click.option("--messages", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def inbox_messages_send(
    client: gotham.v1.FoundryClient,
    messages: str,
    preview: typing.Optional[bool],
):
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

    """
    result = client.inbox.Messages.send(
        messages=json.loads(messages),
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("map_rendering")
def map_rendering():
    pass


@map_rendering.group("map_rendering")
def map_rendering_map_rendering():
    pass


@map_rendering_map_rendering.command("load_generic_symbol")
@click.argument("id", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.option(
    "--size",
    type=int,
    required=False,
    help="""Resize the icon so that its reference size matches this value. The actually returned image may be larger or smaller than this value.
""",
)
@click.pass_obj
def map_rendering_map_rendering_load_generic_symbol(
    client: gotham.v1.FoundryClient,
    id: str,
    preview: typing.Optional[bool],
    size: typing.Optional[int],
):
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

    """
    result = client.map_rendering.MapRendering.load_generic_symbol(
        id=id,
        preview=preview,
        size=size,
    )
    click.echo(result)


@map_rendering_map_rendering.command("load_resource_tile")
@click.argument("tileset", type=str, required=True)
@click.argument("zoom", type=int, required=True)
@click.argument("x_coordinate", type=int, required=True)
@click.argument("y_coordinate", type=int, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def map_rendering_map_rendering_load_resource_tile(
    client: gotham.v1.FoundryClient,
    tileset: str,
    zoom: int,
    x_coordinate: int,
    y_coordinate: int,
    preview: typing.Optional[bool],
):
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

    """
    result = client.map_rendering.MapRendering.load_resource_tile(
        tileset=tileset,
        zoom=zoom,
        x_coordinate=x_coordinate,
        y_coordinate=y_coordinate,
        preview=preview,
    )
    click.echo(result)


@map_rendering_map_rendering.command("render_objects")
@click.option("--capabilities", type=str, required=True, help="""""")
@click.option("--invocations", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def map_rendering_map_rendering_render_objects(
    client: gotham.v1.FoundryClient,
    capabilities: str,
    invocations: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Stateless api to fetch a snapshot of renderables for a given object set. Only includes initial renderable values
    in snapshot, does not reflect changes made while rendering.

    """
    result = client.map_rendering.MapRendering.render_objects(
        capabilities=json.loads(capabilities),
        invocations=json.loads(invocations),
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("media")
def media():
    pass


@media.group("media")
def media_media():
    pass


@media_media.command("get_media_content")
@click.argument("media_rid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def media_media_get_media_content(
    client: gotham.v1.FoundryClient,
    media_rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Get the content of media.

    """
    result = client.media.Media.get_media_content(
        media_rid=media_rid,
        preview=preview,
    )
    click.echo(result)


@media_media.command("get_object_media")
@click.argument("primary_key", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def media_media_get_object_media(
    client: gotham.v1.FoundryClient,
    primary_key: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Get media metadata for object. Media metadata contains an identifier and other
    attributes suitable for display/download, such as content type and title.

    """
    result = client.media.Media.get_object_media(
        primary_key=primary_key,
        preview=preview,
    )
    click.echo(repr(result))


@cli.group("target_workbench")
def target_workbench():
    pass


@target_workbench.group("targets")
def target_workbench_targets():
    pass


@target_workbench_targets.command("create")
@click.option("--aimpoints", type=str, required=True, help="""""")
@click.option("--column", type=str, required=True, help="""""")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--security", type=str, required=True, help="""""")
@click.option("--target_board", type=str, required=True, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option("--entity_rid", type=str, required=False, help="""""")
@click.option("--high_priority_target_list_target_subtype", type=str, required=False, help="""""")
@click.option("--location", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.option(
    "--sidc", type=str, required=False, help="""MIL-STD 2525C Symbol Identification Code"""
)
@click.option("--target_identifier", type=str, required=False, help="""""")
@click.option(
    "--target_type",
    type=str,
    required=False,
    help="""The resource type of the target.
Example: Building
""",
)
@click.pass_obj
def target_workbench_targets_create(
    client: gotham.v1.FoundryClient,
    aimpoints: str,
    column: str,
    name: str,
    security: str,
    target_board: str,
    description: typing.Optional[str],
    entity_rid: typing.Optional[str],
    high_priority_target_list_target_subtype: typing.Optional[str],
    location: typing.Optional[str],
    preview: typing.Optional[bool],
    sidc: typing.Optional[str],
    target_identifier: typing.Optional[str],
    target_type: typing.Optional[str],
):
    """
    Create a Target.
    Returns the RID of the created Target.

    If `sidc` field is specified and invalid according to MIL-STD-2525C specification,
    an `InvalidSidc` error is thrown.

    """
    result = client.target_workbench.Targets.create(
        aimpoints=json.loads(aimpoints),
        column=column,
        name=name,
        security=json.loads(security),
        target_board=target_board,
        description=description,
        entity_rid=entity_rid,
        high_priority_target_list_target_subtype=high_priority_target_list_target_subtype,
        location=None if location is None else json.loads(location),
        preview=preview,
        sidc=sidc,
        target_identifier=None if target_identifier is None else json.loads(target_identifier),
        target_type=target_type,
    )
    click.echo(repr(result))


@target_workbench_targets.command("create_intel")
@click.argument("rid", type=str, required=True)
@click.option(
    "--domain",
    type=click.Choice(
        ["SIGINT", "OSINT", "IMINT", "ELINT", "HUMINT", "OTHER", "ALL_SOURCE", "GEOINT"]
    ),
    required=True,
    help="""""",
)
@click.option("--id", type=str, required=True, help="""""")
@click.option("--intel_type", type=str, required=True, help="""""")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--valid_time", type=click.DateTime(), required=True, help="""""")
@click.option("--confidence", type=float, required=False, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option("--location", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.option("--source", type=str, required=False, help="""""")
@click.pass_obj
def target_workbench_targets_create_intel(
    client: gotham.v1.FoundryClient,
    rid: str,
    domain: typing.Literal[
        "SIGINT", "OSINT", "IMINT", "ELINT", "HUMINT", "OTHER", "ALL_SOURCE", "GEOINT"
    ],
    id: str,
    intel_type: str,
    name: str,
    valid_time: datetime,
    confidence: typing.Optional[float],
    description: typing.Optional[str],
    location: typing.Optional[str],
    preview: typing.Optional[bool],
    source: typing.Optional[str],
):
    """
    Create Intel on Target by RID

    """
    result = client.target_workbench.Targets.create_intel(
        rid=rid,
        domain=domain,
        id=id,
        intel_type=json.loads(intel_type),
        name=name,
        valid_time=valid_time,
        confidence=confidence,
        description=description,
        location=None if location is None else json.loads(location),
        preview=preview,
        source=source,
    )
    click.echo(repr(result))


@target_workbench_targets.command("delete")
@click.argument("rid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_targets_delete(
    client: gotham.v1.FoundryClient,
    rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Archive a Target by RID.
    The user is required to have OWN permissions on the target.

    """
    result = client.target_workbench.Targets.delete(
        rid=rid,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_targets.command("get")
@click.argument("rid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_targets_get(
    client: gotham.v1.FoundryClient,
    rid: str,
    preview: typing.Optional[bool],
):
    """
    Load a Target by RID.

    """
    result = client.target_workbench.Targets.get(
        rid=rid,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_targets.command("remove_intel")
@click.argument("rid", type=str, required=True)
@click.option("--id", type=str, required=True, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_targets_remove_intel(
    client: gotham.v1.FoundryClient,
    rid: str,
    id: str,
    preview: typing.Optional[bool],
):
    """
    Remove Intel on Target by RID

    """
    result = client.target_workbench.Targets.remove_intel(
        rid=rid,
        id=id,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_targets.command("update")
@click.argument("rid", type=str, required=True)
@click.option("--aimpoints", type=str, required=True, help="""""")
@click.option(
    "--base_revision_id",
    type=int,
    required=True,
    help="""The version of the Target to be modified.
The modifying operations will be transformed against any concurrent operations
made since this version. 

If the supplied version is outdated, the server will respond back with RevisionTooOld exception and
the client must resend the request with the updated baseRevisionId.
""",
)
@click.option("--name", type=str, required=True, help="""""")
@click.option(
    "--client_id",
    type=str,
    required=False,
    help="""The client id is used to identify conflicting edits made by the same client,
typically due to retries, and discard them. Clients should choose an arbitrary random
identifier to distinguish themselves. There is no need persist and re-use the same
client id over multiple sessions.

The client id is also used to avoid broadcasting operations to the client who
submitted them.
""",
)
@click.option("--description", type=str, required=False, help="""""")
@click.option("--entity_rid", type=str, required=False, help="""""")
@click.option("--high_priority_target_list_target_subtype", type=str, required=False, help="""""")
@click.option("--location", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.option(
    "--sidc", type=str, required=False, help="""MIL-STD 2525C Symbol Identification Code"""
)
@click.option("--target_identifier", type=str, required=False, help="""""")
@click.option(
    "--target_type",
    type=str,
    required=False,
    help="""The resource type of the target.
Example: Building
""",
)
@click.pass_obj
def target_workbench_targets_update(
    client: gotham.v1.FoundryClient,
    rid: str,
    aimpoints: str,
    base_revision_id: int,
    name: str,
    client_id: typing.Optional[str],
    description: typing.Optional[str],
    entity_rid: typing.Optional[str],
    high_priority_target_list_target_subtype: typing.Optional[str],
    location: typing.Optional[str],
    preview: typing.Optional[bool],
    sidc: typing.Optional[str],
    target_identifier: typing.Optional[str],
    target_type: typing.Optional[str],
):
    """
    Set current state of Target by RID.

    If `sidc` field is specified and invalid according to MIL-STD-2525C specification,
    an `InvalidSidc` error is thrown.

    """
    result = client.target_workbench.Targets.update(
        rid=rid,
        aimpoints=json.loads(aimpoints),
        base_revision_id=base_revision_id,
        name=name,
        client_id=client_id,
        description=description,
        entity_rid=entity_rid,
        high_priority_target_list_target_subtype=high_priority_target_list_target_subtype,
        location=None if location is None else json.loads(location),
        preview=preview,
        sidc=sidc,
        target_identifier=None if target_identifier is None else json.loads(target_identifier),
        target_type=target_type,
    )
    click.echo(repr(result))


@target_workbench.group("target_boards")
def target_workbench_target_boards():
    pass


@target_workbench_target_boards.command("create")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--security", type=str, required=True, help="""""")
@click.option("--configuration", type=str, required=False, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option("--high_priority_target_list", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_target_boards_create(
    client: gotham.v1.FoundryClient,
    name: str,
    security: str,
    configuration: typing.Optional[str],
    description: typing.Optional[str],
    high_priority_target_list: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    By default, create a TargetBoard with default columns: IDENTIFIED TARGET, PRIORITIZED TARGET, IN COORDINATION, IN EXECUTION, COMPLETE.
    Returns the RID of the created TargetBoard.

    """
    result = client.target_workbench.TargetBoards.create(
        name=name,
        security=json.loads(security),
        configuration=None if configuration is None else json.loads(configuration),
        description=description,
        high_priority_target_list=high_priority_target_list,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_target_boards.command("delete")
@click.argument("rid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_target_boards_delete(
    client: gotham.v1.FoundryClient,
    rid: str,
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::

    Archive a Collection by RID.

    """
    result = client.target_workbench.TargetBoards.delete(
        rid=rid,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_target_boards.command("get")
@click.argument("rid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_target_boards_get(
    client: gotham.v1.FoundryClient,
    rid: str,
    preview: typing.Optional[bool],
):
    """
    Load Target Board by RID.

    """
    result = client.target_workbench.TargetBoards.get(
        rid=rid,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_target_boards.command("load_target_pucks")
@click.argument("rid", type=str, required=True)
@click.option(
    "--load_level",
    type=str,
    required=True,
    help="""Determines the set of information to load for a given target puck.
""",
)
@click.option(
    "--allow_stale_loads",
    type=bool,
    required=False,
    help="""If set to true, will potentially load "stale" data associated with the target puck. Defaults to false. Note
that even if the returned data is stale, the data will be stale in the order of minutes or less. Setting
this option to true will yield better performance, especially for consumers that wish to poll this endpoint
at a frequent interval.
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_target_boards_load_target_pucks(
    client: gotham.v1.FoundryClient,
    rid: str,
    load_level: str,
    allow_stale_loads: typing.Optional[bool],
    preview: typing.Optional[bool],
):
    """
    :::callout{theme=warning title=Warning}
    This endpoint is in preview and may be modified or removed at any time.
    To use this endpoint, add `preview=true` to the request query parameters.
    :::
    Loads target pucks contained in a target board. The response may include the puck's associated location and
    board status metadata, depending on the load levels specified in the request.

    """
    result = client.target_workbench.TargetBoards.load_target_pucks(
        rid=rid,
        load_level=json.loads(load_level),
        allow_stale_loads=allow_stale_loads,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_target_boards.command("update")
@click.argument("rid", type=str, required=True)
@click.option(
    "--base_revision_id",
    type=int,
    required=True,
    help="""The current version of the Target Board to be modified.
The archive operation will be transformed against any concurrent operations
made since this version. If there are any conflicting edits that result in changes to
these operations when they're applied, that will be noted in the response.
""",
)
@click.option("--name", type=str, required=True, help="""""")
@click.option("--configuration", type=str, required=False, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option("--high_priority_target_list", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_target_boards_update(
    client: gotham.v1.FoundryClient,
    rid: str,
    base_revision_id: int,
    name: str,
    configuration: typing.Optional[str],
    description: typing.Optional[str],
    high_priority_target_list: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Modify a Target Board by RID.

    """
    result = client.target_workbench.TargetBoards.update(
        rid=rid,
        base_revision_id=base_revision_id,
        name=name,
        configuration=None if configuration is None else json.loads(configuration),
        description=description,
        high_priority_target_list=high_priority_target_list,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_target_boards.command("update_target_column")
@click.argument("target_rid", type=str, required=True)
@click.option(
    "--base_revision_id",
    type=int,
    required=True,
    help="""The version of Target Board you are working with.
The set operation will be transformed against any concurrent operations
made since this version. If there are any conflicting edits that result in changes to
these operations when they're applied, that will be noted in the response.
""",
)
@click.option("--board_rid", type=str, required=True, help="""""")
@click.option("--new_column_id", type=str, required=True, help="""""")
@click.option(
    "--client_id",
    type=str,
    required=False,
    help="""The client id is used to identify conflicting edits made by the same client,
typically due to retries, and discard them. Clients should choose an arbitrary random
identifier to distinguish themselves. There is no need persist and re-use the same
client id over multiple sessions.

The client id is also used to avoid broadcasting operations to the client who
submitted them.
""",
)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_target_boards_update_target_column(
    client: gotham.v1.FoundryClient,
    target_rid: str,
    base_revision_id: int,
    board_rid: str,
    new_column_id: str,
    client_id: typing.Optional[str],
    preview: typing.Optional[bool],
):
    """
    Move a Target into a TargetBoardColumn from an old column.

    """
    result = client.target_workbench.TargetBoards.update_target_column(
        target_rid=target_rid,
        base_revision_id=base_revision_id,
        board_rid=board_rid,
        new_column_id=new_column_id,
        client_id=client_id,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench.group("high_priority_target_lists")
def target_workbench_high_priority_target_lists():
    pass


@target_workbench_high_priority_target_lists.command("create")
@click.option("--name", type=str, required=True, help="""""")
@click.option("--security", type=str, required=True, help="""""")
@click.option("--target_aois", type=str, required=True, help="""""")
@click.option(
    "--targets", type=str, required=True, help="""A list of HighPriorityTargetListTargets"""
)
@click.option("--area_geo", type=str, required=False, help="""""")
@click.option("--area_object_rid", type=str, required=False, help="""""")
@click.option("--description", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.option("--target_board", type=str, required=False, help="""""")
@click.pass_obj
def target_workbench_high_priority_target_lists_create(
    client: gotham.v1.FoundryClient,
    name: str,
    security: str,
    target_aois: str,
    targets: str,
    area_geo: typing.Optional[str],
    area_object_rid: typing.Optional[str],
    description: typing.Optional[str],
    preview: typing.Optional[bool],
    target_board: typing.Optional[str],
):
    """
    Create a High Priority Target List.
    Returns the RID of the created High Priority Target List.

    """
    result = client.target_workbench.HighPriorityTargetLists.create(
        name=name,
        security=json.loads(security),
        target_aois=json.loads(target_aois),
        targets=json.loads(targets),
        area_geo=None if area_geo is None else json.loads(area_geo),
        area_object_rid=area_object_rid,
        description=description,
        preview=preview,
        target_board=target_board,
    )
    click.echo(repr(result))


@target_workbench_high_priority_target_lists.command("get")
@click.argument("rid", type=str, required=True)
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.pass_obj
def target_workbench_high_priority_target_lists_get(
    client: gotham.v1.FoundryClient,
    rid: str,
    preview: typing.Optional[bool],
):
    """
    Load a High Priority Target List by RID.

    """
    result = client.target_workbench.HighPriorityTargetLists.get(
        rid=rid,
        preview=preview,
    )
    click.echo(repr(result))


@target_workbench_high_priority_target_lists.command("update")
@click.argument("rid", type=str, required=True)
@click.option(
    "--base_revision_id",
    type=int,
    required=True,
    help="""The current version of the HighPriorityTargetList to be modified.
Any modifying operations should be accompanied by this version to avoid concurrent operations
made since this version. If there are any conflicting edits that result in changes to
these operations when they're applied, that will be noted in the response.
""",
)
@click.option("--target_aois", type=str, required=True, help="""""")
@click.option(
    "--targets", type=str, required=True, help="""A list of HighPriorityTargetListTargets"""
)
@click.option("--area_geo", type=str, required=False, help="""""")
@click.option("--area_object_rid", type=str, required=False, help="""""")
@click.option(
    "--preview",
    type=bool,
    required=False,
    help="""Represents a boolean value that restricts an endpoint to preview mode when set to true.
""",
)
@click.option("--target_board", type=str, required=False, help="""""")
@click.pass_obj
def target_workbench_high_priority_target_lists_update(
    client: gotham.v1.FoundryClient,
    rid: str,
    base_revision_id: int,
    target_aois: str,
    targets: str,
    area_geo: typing.Optional[str],
    area_object_rid: typing.Optional[str],
    preview: typing.Optional[bool],
    target_board: typing.Optional[str],
):
    """
    Modify a High Priority Target List by RID.

    """
    result = client.target_workbench.HighPriorityTargetLists.update(
        rid=rid,
        base_revision_id=base_revision_id,
        target_aois=json.loads(target_aois),
        targets=json.loads(targets),
        area_geo=None if area_geo is None else json.loads(area_geo),
        area_object_rid=area_object_rid,
        preview=preview,
        target_board=target_board,
    )
    click.echo(repr(result))


if __name__ == "__main__":
    cli()
