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

import typing

import pydantic
import typing_extensions

from gotham import _core as core
from gotham.v1.foundry import models as foundry_models
from gotham.v1.gotham import models as gotham_models


class ClientCapabilities(pydantic.BaseModel):
    """
    The render capability of the client. Renderables will be returned in the best possible format that's supported
    by the client.
    """

    supported_renderable_content: typing.List[RenderableContentType] = pydantic.Field(alias=str("supportedRenderableContent"))  # type: ignore[literal-required]
    """
    Supported renderable content types. Unsupported types will be converted to supported ones. More advanced
    renderable content types may suffer lower performance or fidelity when being transcoded into the base
    geometry type. The base geometry type must always be supported.
    Refer to [RenderableContent](https://palantir.com/#/components/schemas/RenderableContent) for the shape of the renderable contents.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FoundryObjectPropertyValueUntyped = typing.Any
"""The value of a Foundry object's property. The type of the property value is not preserved."""


class GeometryRenderableContent(pydantic.BaseModel):
    """Renderable content represented with GeoJson geometry."""

    geometry: gotham_models.GeoJsonObject
    style: MrsGeometryStyle
    type: typing.Literal["geometry"] = "geometry"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Invocation(pydantic.BaseModel):
    """
    Represents a request to render a set of Foundry objects. This includes information on how the objects should be
    rendered.
    """

    id: InvocationId
    sourcing_only: typing.Optional[bool] = pydantic.Field(alias=str("sourcingOnly"), default=None)  # type: ignore[literal-required]
    """
    Set to only receive sourcing information with no renderables. This is useful for rendering a list view
    without displaying renderables, such as in the case of a layer with visibility toggled off.
    """

    objects: ObjectsReference
    renderer: RendererReference
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


InvocationId = str
"""Client supplied session-unique identifier for a specific invocation of a render function."""


MrsAlpha = int
"""Alpha value of the color in the [0, 255] range."""


class MrsColor(pydantic.BaseModel):
    """MrsColor"""

    rgb: MrsRgb
    alpha: MrsAlpha
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MrsFillStyle(pydantic.BaseModel):
    """The RID of an object set."""

    color: MrsColor
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MrsGenericSymbol(pydantic.BaseModel):
    """Base generic symbol. Clients should always support rendering this symbol type."""

    id: MrsGenericSymbolId
    type: typing.Literal["generic"] = "generic"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MrsGenericSymbolId = str
"""
Unique identifier for a symbol that can be used to fetch the symbol as a PNG using loadGenericSymbol endpoint.
The ID is opaque and not meant to be parsed in any way.
"""


class MrsGeometryStyle(pydantic.BaseModel):
    """Styling information for GeoJson geometry objects."""

    symbol_style: typing.Optional[MrsSymbolStyle] = pydantic.Field(alias=str("symbolStyle"), default=None)  # type: ignore[literal-required]
    stroke_style: typing.Optional[MrsStrokeStyle] = pydantic.Field(alias=str("strokeStyle"), default=None)  # type: ignore[literal-required]
    fill_style: typing.Optional[MrsFillStyle] = pydantic.Field(alias=str("fillStyle"), default=None)  # type: ignore[literal-required]
    label_style: typing.Optional[MrsLabelStyle] = pydantic.Field(alias=str("labelStyle"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MrsLabelStyle(pydantic.BaseModel):
    """The RID of an object set."""

    color: MrsColor
    text: str
    size: MrsVirtualPixels
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MrsRasterStyle(pydantic.BaseModel):
    """Styling information for raster tiles."""

    opacity: MrsAlpha
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MrsRgb = str
"""RGB values of the color encoded in hex as '#RRGGBB'"""


class MrsStrokeStyle(pydantic.BaseModel):
    """The RID of an object set."""

    color: MrsColor
    width: MrsVirtualPixels
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MrsSymbolStyle(pydantic.BaseModel):
    """MrsSymbolStyle"""

    symbol: MrsSymbol
    size: MrsVirtualPixels
    opacity: MrsAlpha
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MrsVirtualPixels = float
"""
Size in virtual pixels, accounting for high DPI displays. For browser applications these are CSS pixels or
devicePixelRatio.
"""


class ObjectSourcingContent(pydantic.BaseModel):
    """Information that could be used to identify an unique Foundry object."""

    object_type: foundry_models.FoundryObjectTypeRid = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    primary_key: typing.Dict[foundry_models.FoundryObjectPropertyTypeRid, FoundryObjectPropertyValueUntyped] = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    """The primary key of an object."""

    type: typing.Literal["object"] = "object"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObjectsReferenceObjectSet(pydantic.BaseModel):
    """Reference to a Foundry object set. Versioned object sets are currently not supported."""

    object_set_rid: foundry_models.FoundryObjectSetRid = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    type: typing.Literal["objectSet"] = "objectSet"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class RasterTilesRenderableContent(pydantic.BaseModel):
    """
    Renderable content represented with raster tiles in the Web Mercator (EPSG:3857) projection, laid out with the
    single root tile, (z=0, x=0, y=0), covering the whole world. Construct the url using the url template supplied
    to load the raster tile.
    See https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames.
    """

    url: str
    """URL template to use to fetch image tiles in the slippy layout. Example '.../{z}/{x}/{y}'"""

    tile_display_resolution: MrsVirtualPixels = pydantic.Field(alias=str("tileDisplayResolution"))  # type: ignore[literal-required]
    covering_geometry: gotham_models.GeoJsonObject = pydantic.Field(alias=str("coveringGeometry"))  # type: ignore[literal-required]
    style: MrsRasterStyle
    type: typing.Literal["rasterTilesWebMercator"] = "rasterTilesWebMercator"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class RenderObjectsResponse(pydantic.BaseModel):
    """RenderObjectsResponse"""

    renderables: typing.List[Renderable]
    sourcings: typing.List[Sourcing]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Renderable(pydantic.BaseModel):
    """A set of RenderableContent that represents a property of a Foundry object (i.e. the sourcing) for an invocation."""

    id: RenderableId
    invocation: InvocationId
    sourcing: SourcingId
    content: typing.Dict[RenderablePartId, RenderableContent]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


RenderableContent = typing_extensions.Annotated[
    typing.Union[GeometryRenderableContent, RasterTilesRenderableContent],
    pydantic.Field(discriminator="type"),
]
"""Represents a set of geopositioned geometries and their corresponding style to be rendered on to a map."""


RenderableContentType = typing.Literal["GEOMETRY", "RASTER_TILES_WEB_MERCATOR"]
"""
Available renderable content types:
- `GEOMETRY`: Base geometry type.
  Corresponds to [GeometryRenderableContent](https://palantir.com/#/components/schemas/GeometryRenderableContent).
- `RASTER_TILES_WEB_MERCATOR`: Web Mercator (EPSG:3857) projection raster tiles.
  Corresponds to [RasterTilesRenderableContent](https://palantir.com/#/components/schemas/RasterTilesRenderableContent).
"""


RenderableId = str
"""Globally unique ID for a renderable within a session. The ID is opaque and not meant to be parsed in any way."""


RenderablePartId = str
"""Locally unique identifier for a part of a renderable."""


class Sourcing(pydantic.BaseModel):
    """A reference to an individual unit of data Renderables were derived from."""

    id: SourcingId
    content: SourcingContent
    title: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SourcingId = str
"""Globally unique ID for the sourcing within a session. The ID is opaque and not meant to be parsed in any way."""


class StandardRendererReference(pydantic.BaseModel):
    """
    The standard built in renderer. Renders the objects with service defined default styling derived from the object
    type icon set in ontology manager.
    """

    type: typing.Literal["standard"] = "standard"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TilesetId = str
"""
Unique identifier for a tileset that can be used to fetch slippy tiles. The ID is opaque and not meant to be
parsed in any way.
"""


MrsSymbol = MrsGenericSymbol
"""MrsSymbol"""


ObjectsReference = ObjectsReferenceObjectSet
"""Reference to a set of Foundry objects."""


RendererReference = StandardRendererReference
"""
Reference that can be resolved into a renderer object. The renderer object includes configuration settings for
rendering the objects.
"""


SourcingContent = ObjectSourcingContent
"""SourcingContent"""


core.resolve_forward_references(RenderableContent, globalns=globals(), localns=locals())

__all__ = [
    "ClientCapabilities",
    "FoundryObjectPropertyValueUntyped",
    "GeometryRenderableContent",
    "Invocation",
    "InvocationId",
    "MrsAlpha",
    "MrsColor",
    "MrsFillStyle",
    "MrsGenericSymbol",
    "MrsGenericSymbolId",
    "MrsGeometryStyle",
    "MrsLabelStyle",
    "MrsRasterStyle",
    "MrsRgb",
    "MrsStrokeStyle",
    "MrsSymbol",
    "MrsSymbolStyle",
    "MrsVirtualPixels",
    "ObjectSourcingContent",
    "ObjectsReference",
    "ObjectsReferenceObjectSet",
    "RasterTilesRenderableContent",
    "RenderObjectsResponse",
    "Renderable",
    "RenderableContent",
    "RenderableContentType",
    "RenderableId",
    "RenderablePartId",
    "RendererReference",
    "Sourcing",
    "SourcingContent",
    "SourcingId",
    "StandardRendererReference",
    "TilesetId",
]
