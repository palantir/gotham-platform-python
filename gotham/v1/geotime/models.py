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
from gotham.v1.gotham import models as gotham_models

CollectionId = str
"""Identifier for the specific data source within the source system for this Observation data. This is a mandatory qualifier in addition to the Source System ID, and is unique within the source system. To extend the above example, this would identify a specific table within the database."""


class ConvolvedComponentMetadata(pydantic.BaseModel):
    """Metadata representing an input ellipse used to create a convolved ellipse."""

    ellipse_id: gotham_models.GeotimeSeriesExternalReference = pydantic.Field(alias=str("ellipseId"))  # type: ignore[literal-required]
    convolution_timestamp: core.AwareDatetime = pydantic.Field(alias=str("convolutionTimestamp"))  # type: ignore[literal-required]
    user_id: str = pydantic.Field(alias=str("userId"))  # type: ignore[literal-required]
    """The user ID of the user which performed this convolution."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ConvolvedMetadata(pydantic.BaseModel):
    """Metadata representing a convolved ellipse and the input ellipses used to create it."""

    convolved_ellipse_id: gotham_models.GeotimeSeriesExternalReference = pydantic.Field(alias=str("convolvedEllipseId"))  # type: ignore[literal-required]
    components: typing.List[ConvolvedComponentMetadata]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeometryStyle(pydantic.BaseModel):
    """Describes styling information to control the appearance of observation geometry."""

    stroke_width: typing.Optional[float] = pydantic.Field(alias=str("strokeWidth"), default=None)  # type: ignore[literal-required]
    stroke_color: typing.Optional[str] = pydantic.Field(alias=str("strokeColor"), default=None)  # type: ignore[literal-required]
    """
    A 6 character hexadecimal string describing the color of the border on all geometry. Default is
    "#FDFF00". The leading # is required.
    """

    fill_color: typing.Optional[str] = pydantic.Field(alias=str("fillColor"), default=None)  # type: ignore[literal-required]
    """
    A 6 character hexadecimal string describing the color to fill all geometry. The leading # is required.
    By default, the geometry will not be filled and will instead appear "hollow". If you want to fill a
    geometry, you must specify both fillColor and fillOpacity for this to have any effect.
    """

    fill_opacity: typing.Optional[float] = pydantic.Field(alias=str("fillOpacity"), default=None)  # type: ignore[literal-required]
    """
    A number between 0 and 1 (inclusive) which controls the opacity of the fill of all geometry. By default,
    this is 0. If you want to fill a geometry, you must specify both fillColor and fillOpacity for this to
    have any effect.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IconSymbologyIdentifier(pydantic.BaseModel):
    """
    A built-in generic icon identifier. The color properties, if specified, must be a 6-character hexadecimal string
    describing the color to use for the icon. The leading # is required.
    """

    code: str
    """The code of an icon allowed on a given deployment."""

    fill_color: typing.Optional[str] = pydantic.Field(alias=str("fillColor"), default=None)  # type: ignore[literal-required]
    """
    A 6-character hexadecimal string describing the color to use to fill the icon (if supported). The leading #
    is required.
    """

    stroke_color: typing.Optional[str] = pydantic.Field(alias=str("strokeColor"), default=None)  # type: ignore[literal-required]
    """
    A 6-character hexadecimal string describing the color to use for the icon's stroke (if supported). The
    leading # is required.
    """

    type: typing.Literal["iconSym"] = "iconSym"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class InvalidObservation(pydantic.BaseModel):
    """InvalidObservation"""

    observation: Observation
    reason: str
    """The reason the Observation that failed to be written failed."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MilSymbologyIdentifier(pydantic.BaseModel):
    """A builtin set of identifiers that are built-in and follow the MIL-STD-2525 specification."""

    code: str
    type: typing.Literal["milSym"] = "milSym"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectRid = str
"""Globally unique identifier for an Object Rid."""


class Observation(pydantic.BaseModel):
    """A geotemporal object along a Geotime Track (SSID, CID, SpecID, TrackID quadruplet)."""

    source_system_id: SourceSystemId = pydantic.Field(alias=str("sourceSystemId"))  # type: ignore[literal-required]
    collection_id: CollectionId = pydantic.Field(alias=str("collectionId"))  # type: ignore[literal-required]
    observation_spec_id: ObservationSpecId = pydantic.Field(alias=str("observationSpecId"))  # type: ignore[literal-required]
    track_id: str = pydantic.Field(alias=str("trackId"))  # type: ignore[literal-required]
    """The ID of a series of location points. This is a shared ID between Observations which forms a Track. These IDs are typically derived from the integrated data. For example, a flight identifier used to distinguish a unique voyage by a plane."""

    position: gotham_models.GeoPoint
    timestamp: core.AwareDatetime
    name: typing.Optional[str] = None
    """The name of the entity associated with the Observation. For example, 'My Plane' or 'Air Force One'."""

    static_properties: typing.List[ObservationField] = pydantic.Field(alias=str("staticProperties"))  # type: ignore[literal-required]
    """Properties that are expected to remain constant along a Geotime Track. E.g. A plane's tail number."""

    live_properties: typing.List[ObservationField] = pydantic.Field(alias=str("liveProperties"))  # type: ignore[literal-required]
    """Properties that are expected to be updated frequently along a Geotime Track. E.g. A plane's heading."""

    style: typing.Optional[ObservationStyle] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObservationField(pydantic.BaseModel):
    """A dynamic field that must match a field defined in the Observation's associated ObservationSpec."""

    property_type: str = pydantic.Field(alias=str("propertyType"))  # type: ignore[literal-required]
    value: typing.Any
    """A string that can represent a plain string, GeoJson string, or numeric value."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class ObservationQuery(pydantic.BaseModel):
    """The query to match to Geotime Tracks."""

    time: typing.Optional[TimeQuery] = None
    location: typing.Optional[ObservationWithinQuery] = None
    property: typing.Optional[PropertyValuesQuery] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObservationSpecId = str
"""Globally unique identifier for the Observation Specification. Observation Specs are schemas used to define the shape of an Observation. These schemas contain mandatory fields such as timestamp, position and Track ID, as well as dynamically defined fields exposed as static and live properties."""


class ObservationStyle(pydantic.BaseModel):
    """Describes styling information about how an individual observation should be displayed on the frontend."""

    blueprint_icon_name: typing.Optional[str] = pydantic.Field(alias=str("blueprintIconName"), default=None)  # type: ignore[literal-required]
    """
    The name of an icon from the open source project "blueprint" to be used in the baseball card view of an
    observation.
    """

    symbology: typing.Optional[SymbologyIdentifier] = None
    geometry_style: typing.Optional[GeometryStyle] = pydantic.Field(alias=str("geometryStyle"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObservationWithinQuery = typing.List[gotham_models.GeoPoint]
"""
The polygon within which to search for Geotime Tracks.
The polygon must be structured in the following manner:
1. It must be closed. That is, the first and last point in the list of points must be the same.
2. There must be a minimum of 4 points including the equal first and last points.
3. The points must be listed in a counter-clockwise manner.
"""


class PropertyValuesQuery(pydantic.BaseModel):
    """Matches observations which have any of the values specified for this property."""

    property: str
    """The name of the property in the observation schema"""

    values: typing.List[gotham_models.PropertyValue]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SearchLatestObservationsResponse(pydantic.BaseModel):
    """The list of latest Observations corresponding to the Tracks that matched the ObservationQuery used to search."""

    data: typing.List[Observation]
    next_page_token: typing.Optional[gotham_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SearchObservationHistoryResponse(pydantic.BaseModel):
    """The list of latest Observations corresponding to the Tracks that matched the ObservationQuery used to search."""

    data: typing.List[Track]
    next_page_token: typing.Optional[gotham_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SourceSystemId = str
"""Globally unique identifier for the system from which this Observation data is sourced. An example might be the name of a database."""


SymbologyIdentifier = typing_extensions.Annotated[
    typing.Union[IconSymbologyIdentifier, MilSymbologyIdentifier],
    pydantic.Field(discriminator="type"),
]
"""An identifier for a symbology icon to use for display on a map."""


class TimeQuery(pydantic.BaseModel):
    """
    The time range over which Geotime Tracks with most recent Observations with timestamps falling within
    this inclusive range will be matched to.
    """

    start: core.AwareDatetime
    end: core.AwareDatetime
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Track(pydantic.BaseModel):
    """A series of timestamped Observations."""

    track_rid: typing.Optional[TrackRid] = pydantic.Field(alias=str("TrackRid"), default=None)  # type: ignore[literal-required]
    observations: typing.List[Observation]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TrackRid = str
"""Globally unique identifier for a Geotime Track. This is synonymous with a Gotham Identifier and contains information like SourceSystemId, CollectionId, SpecId and TrackId."""


WriteObservationsRequest = typing.List[Observation]
"""The list of Observations to write to Geotime."""


WriteObservationsResponse = typing.List[InvalidObservation]
"""The list of Observations that failed to write to Geotime, if any."""


core.resolve_forward_references(ObservationWithinQuery, globalns=globals(), localns=locals())
core.resolve_forward_references(SymbologyIdentifier, globalns=globals(), localns=locals())
core.resolve_forward_references(WriteObservationsRequest, globalns=globals(), localns=locals())
core.resolve_forward_references(WriteObservationsResponse, globalns=globals(), localns=locals())

__all__ = [
    "CollectionId",
    "ConvolvedComponentMetadata",
    "ConvolvedMetadata",
    "GeometryStyle",
    "IconSymbologyIdentifier",
    "InvalidObservation",
    "MilSymbologyIdentifier",
    "ObjectRid",
    "Observation",
    "ObservationField",
    "ObservationQuery",
    "ObservationSpecId",
    "ObservationStyle",
    "ObservationWithinQuery",
    "PropertyValuesQuery",
    "SearchLatestObservationsResponse",
    "SearchObservationHistoryResponse",
    "SourceSystemId",
    "SymbologyIdentifier",
    "TimeQuery",
    "Track",
    "TrackRid",
    "WriteObservationsRequest",
    "WriteObservationsResponse",
]
