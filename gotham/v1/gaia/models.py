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

import annotated_types
import pydantic
import typing_extensions

from gotham import _core as core
from gotham.v1.gotham import models as gotham_models


class AddArtifactsToMapResponse(pydantic.BaseModel):
    """The response body to add artifacts to a map, containing the ID of the created layer."""

    data_layer_ids: typing.List[GaiaLayerId] = pydantic.Field(alias=str("dataLayerIds"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AddEnterpriseMapLayersToMapResponse(pydantic.BaseModel):
    """The response body to add enterprise map layers to a map, containing the IDs of the created layers."""

    data_layer_ids: typing.List[GaiaLayerId] = pydantic.Field(alias=str("dataLayerIds"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class AddObjectsToMapResponse(pydantic.BaseModel):
    """The response body to add objects to a map, containing the ID of the created layer."""

    data_layer_ids: typing.List[GaiaLayerId] = pydantic.Field(alias=str("dataLayerIds"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


EmlId = str
"""The ID of a enterprise map layer"""


class FillStyle(pydantic.BaseModel):
    """FillStyle"""

    opacity: typing.Optional[float] = None
    """The opacity of the polygon, if applicable, between 0 and 1."""

    color: typing.Optional[str] = None
    """
    A 6 character hexadecimal string describing the color filling the geometry. The leading # is required, 
    e.g. "#FF00FF"
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GaiaCoordinate(pydantic.BaseModel):
    """A conjured coordinate that is NOT geojson and has an actual structure instead of a [lon, lat] array."""

    lon: float
    lat: float
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GaiaElement(pydantic.BaseModel):
    """
    A representation of an element in a Gaia map. An element can be thought as a leaf node in the structure of a
    map. It contains information such as the geometry of a feature. An element has one or more features.

    Each element has an ID unique within the context of its parent layer; the ID is not guaranteed to be unique
    within the context of a map.
    """

    id: GaiaElementId
    parent_id: GaiaLayerId = pydantic.Field(alias=str("parentId"))  # type: ignore[literal-required]
    features: typing_extensions.Annotated[
        typing.List[GaiaFeature], annotated_types.Len(min_length=1)
    ]
    label: str
    properties: typing.Optional[GaiaProperties] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GaiaElementId = str
"""The ID of an element in a map."""


class GaiaFeature(pydantic.BaseModel):
    """Features are the objects you see on a Gaia map. This includes information such as geometry."""

    geometry: gotham_models.GeoJsonObject
    style: typing.Optional[GaiaStyle] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GaiaLayer(pydantic.BaseModel):
    """
    A representation of a layer in a Gaia map. A layer can contain multiple sub-layers and elements. Each layer has
    a unique ID within the context of a map.
    """

    id: GaiaLayerId
    elements: typing.List[GaiaElement]
    """A list of elements contained within the layer."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GaiaLayerId = str
"""The ID of a layer in a Gaia map."""


class GaiaLayerMetadata(pydantic.BaseModel):
    """GaiaLayerMetadata"""

    id: GaiaLayerId
    sub_layer_ids: typing.List[GaiaLayerId] = pydantic.Field(alias=str("subLayerIds"))  # type: ignore[literal-required]
    """A list of layer IDs nested under this layer."""

    label: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GaiaMapGid = str
"""The GID of a Gaia map"""


GaiaMapId = str
"""The locator (value after the last period) of a Gaia Map RID."""


class GaiaMapMetadata(pydantic.BaseModel):
    """GaiaMapMetadata"""

    map_rid: GaiaMapRid = pydantic.Field(alias=str("mapRid"))  # type: ignore[literal-required]
    map_gid: GaiaMapGid = pydantic.Field(alias=str("mapGid"))  # type: ignore[literal-required]
    name: str
    created_at: core.AwareDatetime = pydantic.Field(alias=str("createdAt"))  # type: ignore[literal-required]
    """The time when the map was first created, based on UTC timezone."""

    last_modified: core.AwareDatetime = pydantic.Field(alias=str("lastModified"))  # type: ignore[literal-required]
    """The last time the map was modified, based on UTC timezone."""

    num_layers: typing.Optional[int] = pydantic.Field(alias=str("numLayers"), default=None)  # type: ignore[literal-required]
    """The number of layers on the map."""

    num_elements: typing.Optional[int] = pydantic.Field(alias=str("numElements"), default=None)  # type: ignore[literal-required]
    """The number of elements on the map."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GaiaMapName = str
"""The name of the Gaia map."""


GaiaMapRid = str
"""The RID of a Gaia Map."""


class GaiaProperties(pydantic.BaseModel):
    """
    Strongly-typed properties associated with a Gaia element. We provide API guarantees over fields in this class;
    consumers may use these properties programmatically. Note that the fields in this class are not guaranteed
    to be populated; we populate these fields on a best effort basis.
    """

    tactical_graphic_properties: typing.Optional[TacticalGraphicProperties] = pydantic.Field(alias=str("tacticalGraphicProperties"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GaiaStyle(pydantic.BaseModel):
    """GaiaStyle"""

    symbol: typing.Optional[SymbolStyle] = None
    fill: typing.Optional[FillStyle] = None
    stroke: typing.Optional[StrokeStyle] = None
    label: typing.Optional[LabelStyle] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GaiaSymbol = typing_extensions.Annotated[
    typing.Union["MilsymSymbol", "IconSymbol"], pydantic.Field(discriminator="type")
]
"""GaiaSymbol"""


class IconFillStyle(pydantic.BaseModel):
    """IconFillStyle"""

    color: typing.Optional[str] = None
    """
    A 6 character hexadecimal string describing the color filling the icon, if applicable. The leading # is required, 
    e.g. "#FF00FF"
    """

    opacity: typing.Optional[float] = None
    """The opacity of the icon between 0 and 1, if applicable."""

    text: typing.Optional[str] = None
    """The icon fill text, if applicable"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IconStrokeStyle(pydantic.BaseModel):
    """IconStrokeStyle"""

    color: typing.Optional[str] = None
    """
    A 6 character hexadecimal string describing the color outlining the icon, if applicable. The leading # is required, 
    e.g. "#FF00FF"
    """

    width: typing.Optional[float] = None
    """The width of the outline in pixels, if applicable."""

    opacity: typing.Optional[float] = None
    """The opacity of the outline between 0 and 1, if applicable."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IconSymbol(pydantic.BaseModel):
    """IconSymbol"""

    id: str
    """The symbol identifier"""

    stroke: typing.Optional[IconStrokeStyle] = None
    fill: typing.Optional[IconFillStyle] = None
    type: typing.Literal["IconSymbol"] = "IconSymbol"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LabelStyle(pydantic.BaseModel):
    """
    Styling properties for rendering labels on a map. Right now, this will always be attached to a Point geometry.
    The "text" field should be drawn with the given visibility/opacity/color. The Y-coordinate of the point
    geometry represents the vertical midpoint of the rendered text and the X-coordinate of the point geometry
    should line up with either the leftmost, center, or rightmost part of the rendered text as determined by the
    textAlignment field. Then, the text should be rotated clockwise about this point geometry as determined by the
    rotation field.
    """

    text: typing.Optional[str] = None
    """The text to render on the feature"""

    text_rotation: typing.Optional[float] = pydantic.Field(alias=str("textRotation"), default=None)  # type: ignore[literal-required]
    """How many degrees (clockwise) to rotate the rendered text about the point provided in the geometry field"""

    text_color: typing.Optional[str] = pydantic.Field(alias=str("textColor"), default=None)  # type: ignore[literal-required]
    """
    A 6 character hexadecimal string describing the text color, if applicable. The leading # is required, 
    e.g. "#FF00FF"
    """

    text_alignment: typing.Optional[TextAlignment] = pydantic.Field(alias=str("textAlignment"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadLayersResponse(pydantic.BaseModel):
    """LoadLayersResponse"""

    layers: typing.Dict[GaiaLayerId, GaiaLayer]
    """A mapping of the requested layer IDs to a Gaia layer. Any invalid layer IDs will be omitted from this field."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadMapResponse(pydantic.BaseModel):
    """Contains information related to a Gaia map's structure and basic metadata."""

    title: str
    """The title of the loaded Gaia map."""

    root_layer_ids: typing.List[GaiaLayerId] = pydantic.Field(alias=str("rootLayerIds"))  # type: ignore[literal-required]
    """
    The **root** layers of the loaded Gaia map. This does not include sub-layers, i.e. layers nested within a parent
    layer in a Gaia map.
    """

    layers: typing.Dict[GaiaLayerId, GaiaLayerMetadata]
    """A mapping of **all** the layers contained in the Gaia map. Includes layers nested under the root layers."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MilSymModifiers(pydantic.BaseModel):
    """MilSymModifiers"""

    a_m: typing.List[float] = pydantic.Field(alias=str("aM"))  # type: ignore[literal-required]
    a_n: typing.List[float] = pydantic.Field(alias=str("aN"))  # type: ignore[literal-required]
    x: typing.List[float]
    x1: typing.Optional[float] = None
    a: typing.Optional[str] = None
    b: typing.Optional[str] = None
    c: typing.Optional[str] = None
    g: typing.Optional[str] = None
    f: typing.Optional[str] = None
    h: typing.Optional[str] = None
    h1: typing.Optional[str] = None
    h2: typing.Optional[str] = None
    n: typing.Optional[str] = None
    j: typing.Optional[str] = None
    k: typing.Optional[str] = None
    l: typing.Optional[str] = None
    m: typing.Optional[str] = None
    p: typing.Optional[str] = None
    q: typing.Optional[str] = None
    r: typing.Optional[str] = None
    s: typing.Optional[str] = None
    t: typing.Optional[str] = None
    t1: typing.Optional[str] = None
    v: typing.Optional[str] = None
    w: typing.Optional[str] = None
    w1: typing.Optional[str] = None
    y: typing.Optional[str] = None
    z: typing.Optional[str] = None
    a_a: typing.Optional[str] = pydantic.Field(alias=str("aA"), default=None)  # type: ignore[literal-required]
    a_f: typing.Optional[str] = pydantic.Field(alias=str("aF"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MilsymSymbol(pydantic.BaseModel):
    """MilsymSymbol"""

    sidc: str
    """The SIDC of the MIL-2525-C symbol."""

    type: typing.Literal["MilsymSymbol"] = "MilsymSymbol"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SearchMapsResponse(pydantic.BaseModel):
    """The response body containing the queried Gaia maps"""

    results: typing.List[GaiaMapMetadata]
    next_page_token: typing.Optional[gotham_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class StrokeStyle(pydantic.BaseModel):
    """StrokeStyle"""

    width: typing.Optional[int] = None
    """The width of the outline in pixels."""

    opacity: typing.Optional[float] = None
    """The opacity of the outline between 0 and 1."""

    color: typing.Optional[str] = None
    """
    A 6 character hexadecimal string describing the color outlining the geometry. The leading # is required, 
    e.g. "#FF00FF"
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SymbolStyle(pydantic.BaseModel):
    """SymbolStyle"""

    symbol: GaiaSymbol
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TacticalGraphicProperties(pydantic.BaseModel):
    """The unique properties (WGS84 control points, modifiers, and the SIDC) required to create a tactical graphic."""

    sidc: MilsymSymbol
    control_points: typing.List[GaiaCoordinate] = pydantic.Field(alias=str("controlPoints"))  # type: ignore[literal-required]
    modifiers: MilSymModifiers
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TextAlignment = typing.Literal["CENTER", "RIGHT", "LEFT"]
"""TextAlignment"""


core.resolve_forward_references(GaiaSymbol, globalns=globals(), localns=locals())

__all__ = [
    "AddArtifactsToMapResponse",
    "AddEnterpriseMapLayersToMapResponse",
    "AddObjectsToMapResponse",
    "EmlId",
    "FillStyle",
    "GaiaCoordinate",
    "GaiaElement",
    "GaiaElementId",
    "GaiaFeature",
    "GaiaLayer",
    "GaiaLayerId",
    "GaiaLayerMetadata",
    "GaiaMapGid",
    "GaiaMapId",
    "GaiaMapMetadata",
    "GaiaMapName",
    "GaiaMapRid",
    "GaiaProperties",
    "GaiaStyle",
    "GaiaSymbol",
    "IconFillStyle",
    "IconStrokeStyle",
    "IconSymbol",
    "LabelStyle",
    "LoadLayersResponse",
    "LoadMapResponse",
    "MilSymModifiers",
    "MilsymSymbol",
    "SearchMapsResponse",
    "StrokeStyle",
    "SymbolStyle",
    "TacticalGraphicProperties",
    "TextAlignment",
]
