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

ArtifactGid = core.RID
"""The globally unique identifier of an artifact."""


class ArtifactSecurity(pydantic.BaseModel):
    """
    Security mutation details for a target, target board, or hptl.
    Specifying security overrides the system's default security when creating and updating data.
    This model may evolve over time for other security features.
    """

    portion_markings: typing.List[PortionMarking] = pydantic.Field(alias=str("portionMarkings"))  # type: ignore[literal-required]
    """
    Collection of classification portion markings; markings are validated against the system's Classification
    Based Access Control (CBAC) rules; if invalid, an error is raised.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


BBox = typing.List["Coordinate"]
"""
A GeoJSON object MAY have a member named "bbox" to include
information on the coordinate range for its Geometries, Features, or
FeatureCollections. The value of the bbox member MUST be an array of
length 2*n where n is the number of dimensions represented in the
contained geometries, with all axes of the most southwesterly point
followed by all axes of the more northeasterly point. The axes order
of a bbox follows the axes order of geometries.
"""


class ChatMessageId(pydantic.BaseModel):
    """ChatMessageId"""

    chat_channel_gid: ObjectPrimaryKey = pydantic.Field(alias=str("chatChannelGid"))  # type: ignore[literal-required]
    matrix_event_id: str = pydantic.Field(alias=str("matrixEventId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


Coordinate = float
"""Coordinate"""


class CreateHighPriorityTargetListResponseV2(pydantic.BaseModel):
    """Response with the RID of the created High Priority Target List"""

    high_priority_target_list_rid: HighPriorityTargetListRid = pydantic.Field(alias=str("highPriorityTargetListRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CreateTargetBoardResponseV2(pydantic.BaseModel):
    """Response with the ID of the created Target Board"""

    target_board_rid: TargetBoardRid = pydantic.Field(alias=str("targetBoardRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class CreateTargetResponseV2(pydantic.BaseModel):
    """The RID of the Target that was created."""

    target_rid: TargetRid = pydantic.Field(alias=str("targetRid"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


CustomTargetIdentifer = str
"""Custom identifier for targets"""


class ElevationWithError(pydantic.BaseModel):
    """An object including the elevation and the linear error, both in meters"""

    elevation_in_meters: float = pydantic.Field(alias=str("elevationInMeters"))  # type: ignore[literal-required]
    linear_error_in_meters: typing.Optional[float] = pydantic.Field(alias=str("linearErrorInMeters"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class EmptySuccessResponse(pydantic.BaseModel):
    """An empty response object indicating the request was successful."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Feature(pydantic.BaseModel):
    """GeoJSON 'Feature' object"""

    geometry: typing.Optional[Geometry] = None
    properties: typing.Dict[FeaturePropertyKey, typing.Any]
    """
    A `Feature` object has a member with the name "properties".  The
    value of the properties member is an object (any JSON object or a
    JSON null value).
    """

    id: typing.Optional[typing.Any] = None
    """
    If a `Feature` has a commonly used identifier, that identifier
    SHOULD be included as a member of the Feature object with the name
    "id", and the value of this member is either a JSON string or
    number.
    """

    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Feature"] = "Feature"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FeatureCollection(pydantic.BaseModel):
    """GeoJSON 'FeatureCollection' object"""

    features: typing.List[FeatureCollectionTypes]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["FeatureCollection"] = "FeatureCollection"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FeaturePropertyKey = str
"""FeaturePropertyKey"""


class FederatedAndQuery(pydantic.BaseModel):
    """Returns objects where every query is satisfied."""

    value: typing.List[FederatedSearchJsonQuery]
    type: typing.Literal["and"] = "and"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FederatedNotQuery(pydantic.BaseModel):
    """Returns objects where the query is not satisfied."""

    value: FederatedSearchJsonQuery
    type: typing.Literal["not"] = "not"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class FederatedOrQuery(pydantic.BaseModel):
    """Returns objects where at least 1 query is satisfied."""

    value: typing.List[FederatedSearchJsonQuery]
    type: typing.Literal["or"] = "or"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FederatedSearchJsonQuery = typing_extensions.Annotated[
    typing.Union[FederatedNotQuery, FederatedOrQuery, FederatedAndQuery, "FederatedTermQuery"],
    pydantic.Field(discriminator="type"),
]
"""FederatedSearchJsonQuery"""


class FederatedSource(pydantic.BaseModel):
    """Represents a federated source that is available for use in the system."""

    name: FederatedSourceName
    display_name: typing.Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    """The display name of the federated source."""

    namespaces: typing.List[Namespace]
    """The namespaces of the federated source."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


FederatedSourceName = str
"""The name of a federated source."""


class FederatedTermQuery(pydantic.BaseModel):
    """
    Returns objects where the specified field matches the value. The exact kind of matching depends on the data
    source.
    """

    field: str
    value: PropertyValue
    type: typing.Literal["term"] = "term"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeoCircle(pydantic.BaseModel):
    """A circle representing the area a target is located."""

    center: GeoPoint
    radius: float
    """The radius of the geo circle (meters)"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GeoJsonObject = typing_extensions.Annotated[
    typing.Union[
        "MultiPoint",
        "GeometryCollection",
        "MultiLineString",
        FeatureCollection,
        "LineString",
        "MultiPolygon",
        "Point",
        "Polygon",
        Feature,
    ],
    pydantic.Field(discriminator="type"),
]
"""
GeoJSON object

The coordinate reference system for all GeoJSON coordinates is a
geographic coordinate reference system, using the World Geodetic System
1984 (WGS 84) datum, with longitude and latitude units of decimal
degrees.
This is equivalent to the coordinate reference system identified by the
Open Geospatial Consortium (OGC) URN
An OPTIONAL third-position element SHALL be the height in meters above
or below the WGS 84 reference ellipsoid.
In the absence of elevation values, applications sensitive to height or
depth SHOULD interpret positions as being at local ground or sea level.
"""


class GeoPoint(pydantic.BaseModel):
    """GeoPoint"""

    longitude: float
    latitude: float
    elevation: typing.Optional[float] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeoPolygon(pydantic.BaseModel):
    """A Polygon representing the area where this High Priority Target List is applicable. If areaObjectRid exists, that field will be preferred."""

    points: typing.List[GeoPoint]
    """Points defining the polygon in lat, lng, and altitude (meters)."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


Geometry = typing_extensions.Annotated[
    typing.Union[
        "MultiPoint",
        "GeometryCollection",
        "MultiLineString",
        "LineString",
        "MultiPolygon",
        "Point",
        "Polygon",
    ],
    pydantic.Field(discriminator="type"),
]
"""Abstract type for all GeoJSON object except Feature and FeatureCollection"""


class GeometryCollection(pydantic.BaseModel):
    """
    GeoJSON geometry collection

    GeometryCollections composed of a single part or a number of parts of a
    single type SHOULD be avoided when that single part or a single object
    of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could
    be used instead.
    """

    geometries: typing.List[Geometry]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["GeometryCollection"] = "GeometryCollection"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GeotimeSeriesExternalReference(pydantic.BaseModel):
    """
    Reference to a geotime series suitable for external usage.
    Series ID (also referred to as Track ID) is a per-series/track-level attribute, such
    as a flight, manifest or voyage number.

    Observation Spec / Source System and Collection uniquely define a "collection" of observations in a given
    source system adhering to a specific shape.

    See [Observation basics](https://palantir.com/docs/gotham/api/geotime-resources/observations/observation-basics) for more
    information about geotime observations.
    """

    source_system_spec_id: str = pydantic.Field(alias=str("sourceSystemSpecId"))  # type: ignore[literal-required]
    collection_id: str = pydantic.Field(alias=str("collectionId"))  # type: ignore[literal-required]
    observation_spec_id: str = pydantic.Field(alias=str("observationSpecId"))  # type: ignore[literal-required]
    series_id: str = pydantic.Field(alias=str("seriesId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


GeotimeTrackRid = str
"""A resource identifier (RID) of a Geotime Track tracking the target."""


class GetFederatedSourceResponse(pydantic.BaseModel):
    """GetFederatedSourceResponse"""

    next_page_token: typing.Optional[PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[FederatedSource]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GetMediaResponse(pydantic.BaseModel):
    """GetMediaResponse"""

    media: typing.List[Media]
    security_details: typing.Dict[SecurityKey, ObjectComponentSecurity] = pydantic.Field(alias=str("securityDetails"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GroupName(pydantic.BaseModel):
    """
    A qualified group name as used when defining permissions. A group contains a name, and optionally a realm. The
    realm is required for external groups.
    """

    name: str
    """The base name of the group."""

    realm: typing.Optional[str] = None
    """The realm of the group. Empty for internal groups."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class GroupRecipient(pydantic.BaseModel):
    """GroupRecipient"""

    name: str
    """The name for the group in Gotham Security (multipass)."""

    realm: typing.Optional[str] = None
    """The name for the realm for this group. If no realm is specified, the caller's realm is used instead."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class HighPriorityTargetListAgm(pydantic.BaseModel):
    """The Attack Guidance Matrix on a Target on an High Priority Target List."""

    agm_id: HighPriorityTargetListAgmId = pydantic.Field(alias=str("agmId"))  # type: ignore[literal-required]
    effector_type: typing.Optional[HighPriorityTargetListEffectType] = pydantic.Field(alias=str("effectorType"), default=None)  # type: ignore[literal-required]
    effector: typing.Optional[str] = None
    """Example: F-16C"""

    effector_priority: typing.Optional[int] = pydantic.Field(alias=str("effectorPriority"), default=None)  # type: ignore[literal-required]
    """Priority between 1 (highest priority) to 8 of this Effector for the High Priority Target List Target."""

    timeliness_in_minutes: typing.Optional[float] = pydantic.Field(alias=str("timelinessInMinutes"), default=None)  # type: ignore[literal-required]
    accuracy_in_meters: typing.Optional[float] = pydantic.Field(alias=str("accuracyInMeters"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


HighPriorityTargetListAgmId = str
"""HighPriorityTargetListAgmId"""


HighPriorityTargetListEffectType = typing.Literal[
    "DESTROY",
    "JAMMING",
    "NEUTRALIZE",
    "SUPPRESS",
    "K_KILL",
    "COG_KILL",
    "F_KILL",
    "G_KILL",
    "MSN_KILL",
    "M_KILL",
    "M_SLASH_F_KILL",
    "M_SLASH_MSN_KILL",
    "M_SLASH_P_KILL",
    "P_KILL",
    "PM_KILL",
    "PTO_KILL",
    "TOA_KILL",
]
"""The action that should be taken on a Target in a High Priority Target List."""


HighPriorityTargetListRid = str
"""HighPriorityTargetListRid"""


HighPriorityTargetListTargetId = str
"""HighPriorityTargetListTargetId"""


class HighPriorityTargetListTargetV2(pydantic.BaseModel):
    """The target on an High Priority Target List."""

    high_priority_target_list_target_id: HighPriorityTargetListTargetId = pydantic.Field(alias=str("highPriorityTargetListTargetId"))  # type: ignore[literal-required]
    aoi_id: typing.Optional[HptlTargetAoiId] = pydantic.Field(alias=str("aoiId"), default=None)  # type: ignore[literal-required]
    target_type: str = pydantic.Field(alias=str("targetType"))  # type: ignore[literal-required]
    """
    The type of object of this High Priority Target List Target.
    Example: Car
    """

    target_subtypes: typing.List[HptlTargetSubtype] = pydantic.Field(alias=str("targetSubtypes"))  # type: ignore[literal-required]
    """
    A target's subtype will be matched for membership against this set of subtypes in order to determine
    priority, subpriority, and AGM. An empty set of targetSubtypes indicates that this HptlTarget can be
    matched against ANY target subtype.
    """

    priority: int
    """Priority between 1 (highest priority) to 10 of this High Priority Target List Target."""

    sub_priority: typing.Optional[int] = pydantic.Field(alias=str("subPriority"), default=None)  # type: ignore[literal-required]
    """Further categorization of a HptlTarget's priority."""

    category: typing.Optional[str] = None
    """
    The object class appearing on HighPriorityTargetList.
    Example: Airplane
    """

    elnots: typing.List[HptlTargetElnot]
    """ELINT Notations (ELNOTs) associated with the HPTL target type"""

    when: HighPriorityTargetListWhen
    agm: typing.Dict[HighPriorityTargetListAgmId, HighPriorityTargetListAgm]
    """A map of HighPriorityTargetListAgmId to HighPriorityTargetListAgm"""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class HighPriorityTargetListV2(pydantic.BaseModel):
    """The High Priority Target List object."""

    rid: HighPriorityTargetListRid
    description: typing.Optional[str] = None
    targets: typing.List[HighPriorityTargetListTargetV2]
    target_aois: typing.List[HptlTargetAoi] = pydantic.Field(alias=str("targetAois"))  # type: ignore[literal-required]
    area_object_id: typing.Optional[ObjectPrimaryKey] = pydantic.Field(alias=str("areaObjectId"), default=None)  # type: ignore[literal-required]
    area_geo: typing.Optional[GeoPolygon] = pydantic.Field(alias=str("areaGeo"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


HighPriorityTargetListWhen = typing.Literal["ACQUIRED", "IMMEDIATE", "PLANNED", "NONE"]
"""A category representing when to action the Target on a High Priority Target List."""


class HptlTargetAoi(pydantic.BaseModel):
    """HptlTargetAoi"""

    id: HptlTargetAoiId
    name: typing.Optional[str] = None
    data: HptlTargetAoiUnion
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


HptlTargetAoiId = core.UUID
"""HptlTargetAoiId"""


HptlTargetAoiUnion = typing_extensions.Annotated[
    typing.Union["HptlTargetGeoAoi", "HptlTargetEntityAoi"], pydantic.Field(discriminator="type")
]
"""HptlTargetAoiUnion"""


HptlTargetElnot = str
"""HptlTargetElnot"""


class HptlTargetEntityAoi(pydantic.BaseModel):
    """HptlTargetEntityAoi"""

    entity: ObjectPrimaryKey
    type: typing.Literal["entity"] = "entity"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class HptlTargetGeoAoi(pydantic.BaseModel):
    """HptlTargetGeoAoi"""

    geo: GeoPolygon
    type: typing.Literal["geo"] = "geo"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


HptlTargetSubtype = str
"""
This subtype will be matched against the subType stored on HptlTarget in order to determine a target's
subPriority, as well as priority in addition to priority and AGM.
"""


class IntelChatMessage(pydantic.BaseModel):
    """IntelChatMessage"""

    chat_message_id: ChatMessageId = pydantic.Field(alias=str("chatMessageId"))  # type: ignore[literal-required]
    type: typing.Literal["chatMessage"] = "chatMessage"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


IntelDomain = typing.Literal[
    "SIGINT", "OSINT", "IMINT", "ELINT", "HUMINT", "OTHER", "ALL_SOURCE", "GEOINT"
]
"""IntelDomain"""


class IntelDossier(pydantic.BaseModel):
    """IntelDossier"""

    dossier_gid: ObjectPrimaryKey = pydantic.Field(alias=str("dossierGid"))  # type: ignore[literal-required]
    type: typing.Literal["dossier"] = "dossier"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IntelFoundryObject(pydantic.BaseModel):
    """IntelFoundryObject"""

    foundry_object_rid: str = pydantic.Field(alias=str("foundryObjectRid"))  # type: ignore[literal-required]
    type: typing.Literal["foundryObject"] = "foundryObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IntelFreeText(pydantic.BaseModel):
    """Freetext is stored in the Intel `description` field."""

    type: typing.Literal["freetext"] = "freetext"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IntelGeotimeObservation(pydantic.BaseModel):
    """IntelGeotimeObservation"""

    geotime_track: GeotimeTrackRid = pydantic.Field(alias=str("geotimeTrack"))  # type: ignore[literal-required]
    type: typing.Literal["geotimeObservation"] = "geotimeObservation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


IntelId = str
"""IntelId"""


class IntelMedia(pydantic.BaseModel):
    """IntelMedia"""

    file_gid: ObjectPrimaryKey = pydantic.Field(alias=str("fileGid"))  # type: ignore[literal-required]
    type: typing.Literal["media"] = "media"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class IntelPgObject(pydantic.BaseModel):
    """IntelPgObject"""

    object_rid: ObjectPrimaryKey = pydantic.Field(alias=str("objectRid"))  # type: ignore[literal-required]
    type: typing.Literal["pgObject"] = "pgObject"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


IntelUnion = typing_extensions.Annotated[
    typing.Union[
        IntelGeotimeObservation,
        IntelFoundryObject,
        IntelFreeText,
        IntelDossier,
        IntelMedia,
        IntelPgObject,
        IntelChatMessage,
    ],
    pydantic.Field(discriminator="type"),
]
"""IntelUnion"""


JpdiId = str
"""JpdiId"""


class LineString(pydantic.BaseModel):
    """LineString"""

    coordinates: typing.Optional[LineStringCoordinates] = None
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["LineString"] = "LineString"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


LineStringCoordinates = typing_extensions.Annotated[
    typing.List["Position"], annotated_types.Len(min_length=2)
]
"""GeoJSON fundamental geometry construct, array of two or more positions."""


LinearRing = typing_extensions.Annotated[typing.List["Position"], annotated_types.Len(min_length=4)]
"""
A linear ring is a closed LineString with four or more positions.

The first and last positions are equivalent, and they MUST contain
identical values; their representation SHOULD also be identical.

A linear ring is the boundary of a surface or the boundary of a hole in
a surface.

A linear ring MUST follow the right-hand rule with respect to the area
it bounds, i.e., exterior rings are counterclockwise, and holes are
clockwise.
"""


LinkTypeApiName = str
"""The name of the link in the API - also called the Link Type URI."""


class LoadHighPriorityTargetListResponseV2(pydantic.BaseModel):
    """The response body returned when loading a High Priority Target List."""

    high_priority_target_list: HighPriorityTargetListV2 = pydantic.Field(alias=str("highPriorityTargetList"))  # type: ignore[literal-required]
    base_revision_id: int = pydantic.Field(alias=str("baseRevisionId"))  # type: ignore[literal-required]
    """
    The current version of the HighPriorityTargetList retrieved.
    Any modifying operations should be accompanied by this version to avoid concurrent operations
    made since this version. If there are any conflicting edits that result in changes to
    these operations when they're applied, that will be noted in the response.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadTargetBoardResponseV2(pydantic.BaseModel):
    """The response body returned when loading a Target Board."""

    target_board: TargetBoard = pydantic.Field(alias=str("targetBoard"))  # type: ignore[literal-required]
    base_revision_id: core.Long = pydantic.Field(alias=str("baseRevisionId"))  # type: ignore[literal-required]
    """
    The current version of the Collection retrieved.
    Any modifying operations should be accompanied by this version to avoid concurrent operations
    made since this version. If there are any conflicting edits that result in changes to
    these operations when they're applied, that will be noted in the response.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadTargetPuckResponse(pydantic.BaseModel):
    """LoadTargetPuckResponse"""

    location: typing.Optional[TargetLocation] = None
    status: TargetPuckStatus
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadTargetPucksResponse(pydantic.BaseModel):
    """LoadTargetPucksResponse"""

    responses: typing.Dict[TargetPuckId, LoadTargetPuckResponse]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LoadTargetResponseV2(pydantic.BaseModel):
    """The response body returned when loading a Target. The objectRid is the RID of the object being targeted."""

    target: TargetV2
    base_revision_id: core.Long = pydantic.Field(alias=str("baseRevisionId"))  # type: ignore[literal-required]
    """
    The current version of the Target retrieved.
    Any modifying operations should be accompanied by this version to avoid concurrent operations
    made since this version. If there are any conflicting edits that result in changes to
    these operations when they're applied, that will be noted in the response.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Location3dWithError(pydantic.BaseModel):
    """Location object that contains the latitude, longitude, and elevation"""

    lat: float
    lng: float
    circular_error_in_meters: typing.Optional[float] = pydantic.Field(alias=str("circularErrorInMeters"), default=None)  # type: ignore[literal-required]
    hae: typing.Optional[ElevationWithError] = None
    msl: typing.Optional[ElevationWithError] = None
    agl: typing.Optional[ElevationWithError] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class LocationSource(pydantic.BaseModel):
    """
    An object containing the location source for a target.
    This can either be a Location3dWithError and/or a geotimeTrack.
    """

    manual_location: typing.Optional[Location3dWithError] = pydantic.Field(alias=str("manualLocation"), default=None)  # type: ignore[literal-required]
    geotime_track: typing.Optional[GeotimeTrackRid] = pydantic.Field(alias=str("geotimeTrack"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Media(pydantic.BaseModel):
    """
    The representation of a media reference attached to an Object.
    To download media contents, pass the Media RID to the [get media content](https://palantir.com/docs/gotham/api/revdb-resources/media/get-media-content) operation.
    """

    rid: MediaRid
    title: str
    """The user-friendly title of a of media, suitable for displaying to users."""

    description: typing.Optional[str] = None
    """The user-friendly description of a of media, suitable for displaying to users. May not be present for all media."""

    size_bytes: typing.Optional[SizeBytes] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    media_type: MediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    security: typing.List[SecurityKey]
    """
    The ID of the security details for this media. There can be multiple associated with a single media. If a
    user has he security markings or groups of any of them, they will have the associated permission.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MediaRid = core.RID
"""The unique resource identifier of a media component."""


MediaType = str
"""
The [media type](https://www.iana.org/assignments/media-types/media-types.xhtml) of the media.
Examples: `application/json`, `application/pdf`, `application/octet-stream`, `image/jpeg`
"""


class MensurationData(pydantic.BaseModel):
    """MensurationData"""

    mensuration_method: typing.Optional[str] = pydantic.Field(alias=str("mensurationMethod"), default=None)  # type: ignore[literal-required]
    height_method: typing.Optional[str] = pydantic.Field(alias=str("heightMethod"), default=None)  # type: ignore[literal-required]
    elevation_source: typing.Optional[str] = pydantic.Field(alias=str("elevationSource"), default=None)  # type: ignore[literal-required]
    unit_id: typing.Optional[str] = pydantic.Field(alias=str("unitId"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MessageSecurity(pydantic.BaseModel):
    """MessageSecurity"""

    portion_markings: typing.List[PortionMarking] = pydantic.Field(alias=str("portionMarkings"))  # type: ignore[literal-required]
    """
    Collection of classification portion markings; markings are validated against the system's Classification
    Based Access Control (CBAC) rules; if invalid, an error is raised.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MessageSender(pydantic.BaseModel):
    """
    Static text details to display for the message sender.
    Content is secured using the message-level security.
    """

    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


MessageSourceId = core.UUID
"""The unique identifier assigned to the Global Inbox message."""


class MultiLineString(pydantic.BaseModel):
    """MultiLineString"""

    coordinates: typing.List[LineStringCoordinates]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["MultiLineString"] = "MultiLineString"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MultiPoint(pydantic.BaseModel):
    """MultiPoint"""

    coordinates: typing.List[Position]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["MultiPoint"] = "MultiPoint"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class MultiPolygon(pydantic.BaseModel):
    """MultiPolygon"""

    coordinates: typing.List[typing.List[LinearRing]]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["MultiPolygon"] = "MultiPolygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Namespace(pydantic.BaseModel):
    """Represents a namespace of a federated source."""

    name: NamespaceName
    display_name: str = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The properties of a namespace of a federated source."""

    query_shape: typing.Optional[FederatedSearchJsonQuery] = pydantic.Field(alias=str("queryShape"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


NamespaceName = str
"""A identity/name of a namespace of a federated source."""


class ObjectComponentSecurity(pydantic.BaseModel):
    """
    Security mutation details for a component of an object - property, media, link.
    Specifying security overrides the system's default security when creating and updating data.
    If portion markings are specified, permissions *may* be specified. If portion markings are not specified,
    permissions *must* be specified.

    This model may evolve over time for other security features.
    """

    portion_markings: typing.List[PortionMarking] = pydantic.Field(alias=str("portionMarkings"))  # type: ignore[literal-required]
    """
    Collection of classification portion markings; markings are validated against the system's Classification
    Based Access Control (CBAC) rules.

    If invalid, an [InvalidClassificationPortionMarkings](https://palantir.com/docs/gotham/api/general/overview/errors#security-errors) error will be thrown.

    If not specified, no markings will be applied.
    """

    permissions: typing.List[PermissionItem]
    """
    An optional mapping of groups to permissions allowed for the group. If not specified, the system's default
    is for the Everyone group to have WRITE permission, and the Administrators group to have OWNER permission.

    A user will get the highest permission of any of the group they belong to. If portion markings are specified,
    the user must have access to all the markings specified before these permissions are applied.
    """

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ObjectPrimaryKey = str
"""The primary key/unique identifier of an object, useful for interacting with Gotham APIs to load and mutate objects."""


ObjectTypeApiName = str
"""The name of the object in the API - also called the Object Type URI."""


PageSize = int
"""The page size to use for the endpoint."""


PageToken = str
"""
The page token indicates where to start paging. This should be omitted from the first page's request.
To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response
and populate the next request's `pageToken` field with it.
"""


Permission = typing.Literal["READ", "WRITE", "OWNER"]
"""
A permission, one of READ, WRITE, or OWNER. Each successive permission implies the previous ones, so WRITE
implies READ, and OWNER implies READ and WRITE.
"""


class PermissionItem(pydantic.BaseModel):
    """A mapping of a group to a permission."""

    group: GroupName
    permission: Permission
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Point(pydantic.BaseModel):
    """Point"""

    coordinates: Position
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Point"] = "Point"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class Polygon(pydantic.BaseModel):
    """Polygon"""

    coordinates: typing.List[LinearRing]
    bbox: typing.Optional[BBox] = None
    type: typing.Literal["Polygon"] = "Polygon"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


PortionMarking = str
"""
Security markings represent the level of access control that applies to a specific piece of information (e.g., object property, object title).
Security markings are required upon creating a new object, and upon adding a new property to an existing object.
To access information with one or more markings, the user must have access to the markings associated with that information as defined by
your organization's defined security rules. Only users with the correct permissions can get, update, or delete a property
with security markings.

In particular, if a user creates an object and adds a property of type with highly restricted markings, it is possible
that subsequent calls to the get object properties endpoint may fail to display the highly restricted property.

Contact your Palantir administrator for more information on the markings that your organization uses.
"""


Position = typing_extensions.Annotated[
    typing.List[Coordinate], annotated_types.Len(min_length=2, max_length=3)
]
"""
GeoJSON fundamental geometry construct.

A position is an array of numbers. There MUST be two or more elements.
The first two elements are longitude and latitude, precisely in that order and using decimal numbers.
Altitude or elevation MAY be included as an optional third element.

Implementations SHOULD NOT extend positions beyond three elements
because the semantics of extra elements are unspecified and ambiguous.
Historically, some implementations have used a fourth element to carry
a linear referencing measure (sometimes denoted as "M") or a numerical
timestamp, but in most situations a parser will not be able to properly
interpret these values. The interpretation and meaning of additional
elements is beyond the scope of this specification, and additional
elements MAY be ignored by parsers.
"""


PreviewMode = bool
"""Represents a boolean value that restricts an endpoint to preview mode when set to true."""


PropertyApiName = str
"""The name of the property in the API - also called the Property Type URI."""


PropertyId = str
"""
The unique identifier of the property to be updated. This is not to be confused with `propertyType`,
which refers to the property's semantic name (e.g. `com.palantir.property.employeeid`).

`propertyId` can be obtained by calling the [get object properties](https://palantir.com/docs/gotham/api/revdb-resources/objects/get-object-properties/) for an object.
"""


PropertyValue = typing.Any
"""
Represents the value of a property. The following table provides expected representations of scalar data types:

| Type      | JSON encoding                                         | Example                         |
|-----------|-------------------------------------------------------|---------------------------------|
| Date      | ISO 8601 extended local date string                   | `"2021-05-01"`                  |
| Decimal   | string                                                | `"2.718281828"`                 |
| Double    | number                                                | `3.14159265`                    |
| Integer   | number                                                | `238940`                        |
| Long      | string                                                | `"58319870951433"`              |
| String    | string                                                | `"Call me Ishmael"`             |
| Timestamp | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`        |
"""


class SecureTextBody(pydantic.BaseModel):
    """
    A static text body for the message.
    Content is secured using the message-level security.
    """

    value: str
    format_style: TextFormatStyle = pydantic.Field(alias=str("formatStyle"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SecureTextTitle(pydantic.BaseModel):
    """
    A static text title for the message.
    Content is secured using the message-level security.
    """

    value: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SecurityKey = core.Long
"""
The unique identifier of the object component security for an object component. This key is only meant for
deduplication and lookup in the security details included in a single response. It has no guarantees or meaning
outside a single response.
"""


class SendMessageFailure(pydantic.BaseModel):
    """SendMessageFailure"""

    source_id: MessageSourceId = pydantic.Field(alias=str("sourceId"))  # type: ignore[literal-required]
    reason: SendMessageFailureReason
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


SendMessageFailureReason = typing.Literal["CONFLICTING_SOURCE_ID", "UNKNOWN"]
"""
The reason for a failure to send an Inbox message:
  * `CONFLICTING_SOURCE_ID`: A message with the same `MessageSourceId` already exists.
  * `UNKNOWN`: The message failed to send due to an unknown conflict.
"""


class SendMessageRequest(pydantic.BaseModel):
    """SendMessageRequest"""

    group_recipients: typing.List[GroupRecipient] = pydantic.Field(alias=str("groupRecipients"))  # type: ignore[literal-required]
    """The groups of users to send this message to."""

    sender: MessageSender
    title: SecureTextTitle
    body: typing.Optional[SecureTextBody] = None
    security: MessageSecurity
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SendMessageResponse(pydantic.BaseModel):
    """SendMessageResponse"""

    source_id: MessageSourceId = pydantic.Field(alias=str("sourceId"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class SendMessagesResponse(pydantic.BaseModel):
    """SendMessagesResponse"""

    responses: typing.List[SendMessageResponse]
    """
    The list of messages which were sent successfully.
    Messages are returned in the order in which they were sent in the request.
    """

    failures: typing.List[SendMessageFailure]
    """The list of messages which failed to be sent in Inbox due to conflicts with existing messages."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


ServiceName = str
"""The name of the service that is not set-up"""


SizeBytes = core.Long
"""The size of media in bytes."""


TargetAimpointId = str
"""A global unique id of a Target Aimpoint."""


class TargetAimpointV2(pydantic.BaseModel):
    """An aimpoint of a Target if there are multiple locations associated with a Target."""

    id: TargetAimpointId
    name: typing.Optional[str] = None
    location: typing.Optional[Location3dWithError] = None
    geotime_track: typing.Optional[GeotimeTrackRid] = pydantic.Field(alias=str("geotimeTrack"), default=None)  # type: ignore[literal-required]
    entity_rid: typing.Optional[ObjectPrimaryKey] = pydantic.Field(alias=str("entityRid"), default=None)  # type: ignore[literal-required]
    jpdi_id: typing.Optional[JpdiId] = pydantic.Field(alias=str("jpdiId"), default=None)  # type: ignore[literal-required]
    mensuration: typing.Optional[MensurationData] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TargetBoard(pydantic.BaseModel):
    """TargetBoard"""

    rid: TargetBoardRid
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    targets: typing.List[TargetBranchId]
    target_column_ids: typing.Dict[TargetBranchId, TargetDetails] = pydantic.Field(alias=str("targetColumnIds"))  # type: ignore[literal-required]
    high_priority_target_list: typing.Optional[HighPriorityTargetListRid] = pydantic.Field(alias=str("highPriorityTargetList"), default=None)  # type: ignore[literal-required]
    configuration: typing.Optional[TargetBoardConfiguration] = None
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TargetBoardColumnConfiguration(pydantic.BaseModel):
    """TargetBoardColumnConfiguration"""

    id: TargetBoardColumnConfigurationId
    name: str
    color: str
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TargetBoardColumnConfigurationId = str
"""TargetBoardColumnConfigurationId"""


TargetBoardColumnId = str
"""
Equivalent to a collection column ID. The ID of a TargetCollectionColumn, default values are:
DRAFT (Identified target), PLAN_DEVELOPMENT (Prioritized target), PLANNED (In coordination), EXECUTION (In execution), CLOSED (Complete).
"""


class TargetBoardConfiguration(pydantic.BaseModel):
    """Configuration for the target board. If present, must have at least one column"""

    columns: typing.List[TargetBoardColumnConfiguration]
    target_identifiers: typing.List[TargetIdentifierEnum] = pydantic.Field(alias=str("targetIdentifiers"))  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TargetBoardRid = str
"""The unique resource identifier of a Target Board. This is equivalent to a collection RID."""


TargetBranchId = str
"""Identifier of a target and branch. Requires a '*' between the branch ID and target ID."""


class TargetDetails(pydantic.BaseModel):
    """TargetDetails"""

    column_id: typing.Optional[TargetBoardColumnConfigurationId] = pydantic.Field(alias=str("columnId"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


class TargetIdentifier(pydantic.BaseModel):
    """Target identifier object for different identifier types"""

    custom_target_identifier: typing.Optional[CustomTargetIdentifer] = pydantic.Field(alias=str("customTargetIdentifier"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TargetIdentifierEnum = typing.Literal["CUSTOM"]
"""TargetIdentifierEnum"""


class TargetObservation(pydantic.BaseModel):
    """TargetObservation"""

    latest_location: GeoPoint = pydantic.Field(alias=str("latestLocation"))  # type: ignore[literal-required]
    timestamp: typing.Optional[core.AwareDatetime] = None
    """
    Timestamp associated with the target's observation. Timestamp may be absent if the location source does
    not provide them.
    """

    type: typing.Literal["TargetObservation"] = "TargetObservation"
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TargetPuckId = str
"""TargetPuckId"""


TargetPuckLoadLevel = typing.Literal["LOCATION", "BOARD_STATUS"]
"""TargetPuckLoadLevel"""


class TargetPuckStatus(pydantic.BaseModel):
    """TargetPuckStatus"""

    board_rid: TargetBoardRid = pydantic.Field(alias=str("boardRid"))  # type: ignore[literal-required]
    column: TargetBoardColumnId
    column_name: str = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    """Name of the column containing this target puck."""

    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TargetRid = str
"""TargetRid"""


class TargetV2(pydantic.BaseModel):
    """The Target object."""

    rid: TargetRid
    name: str
    description: typing.Optional[str] = None
    target_boards: typing.List[TargetBoardRid] = pydantic.Field(alias=str("targetBoards"))  # type: ignore[literal-required]
    location: typing.Optional[LocationSource] = None
    target_type: typing.Optional[str] = pydantic.Field(alias=str("targetType"), default=None)  # type: ignore[literal-required]
    """
    This is used for effector pairing and determination around HPTL category and time sensitivity
    Example: Building
    """

    entity_rid: typing.Optional[ObjectPrimaryKey] = pydantic.Field(alias=str("entityRid"), default=None)  # type: ignore[literal-required]
    sidc: typing.Optional[str] = None
    """MIL-STD 2525C Symbol Identification Code"""

    aimpoints: typing.List[TargetAimpointV2]
    target_identifier: typing.Optional[TargetIdentifier] = pydantic.Field(alias=str("targetIdentifier"), default=None)  # type: ignore[literal-required]
    high_priority_target_list_target_subtype: typing.Optional[HptlTargetSubtype] = pydantic.Field(alias=str("highPriorityTargetListTargetSubtype"), default=None)  # type: ignore[literal-required]
    model_config = {"extra": "allow", "populate_by_name": True}

    def to_dict(self) -> typing.Dict[str, typing.Any]:
        """Return the dictionary representation of the model using the field aliases."""
        return self.model_dump(by_alias=True, exclude_none=True)


TextFormatStyle = typing.Literal["UNFORMATTED", "PREFORMATTED", "MARKDOWN"]
"""
The formatting style to apply to text when rendering:
  * `UNFORMATTED`: Should be rendered as a simple string, no extra formatting is applied.
  * `PREFORMATTED`: Whitespace is maintained and the content is rendered in a monospace font.
  * `MARKDOWN`: Markdown rendering should be applied.
"""


FeatureCollectionTypes = Feature
"""FeatureCollectionTypes"""


TargetLocation = TargetObservation
"""TargetLocation"""


core.resolve_forward_references(BBox, globalns=globals(), localns=locals())
core.resolve_forward_references(FederatedSearchJsonQuery, globalns=globals(), localns=locals())
core.resolve_forward_references(GeoJsonObject, globalns=globals(), localns=locals())
core.resolve_forward_references(Geometry, globalns=globals(), localns=locals())
core.resolve_forward_references(HptlTargetAoiUnion, globalns=globals(), localns=locals())
core.resolve_forward_references(IntelUnion, globalns=globals(), localns=locals())
core.resolve_forward_references(LineStringCoordinates, globalns=globals(), localns=locals())
core.resolve_forward_references(LinearRing, globalns=globals(), localns=locals())
core.resolve_forward_references(Position, globalns=globals(), localns=locals())

__all__ = [
    "ArtifactGid",
    "ArtifactSecurity",
    "BBox",
    "ChatMessageId",
    "Coordinate",
    "CreateHighPriorityTargetListResponseV2",
    "CreateTargetBoardResponseV2",
    "CreateTargetResponseV2",
    "CustomTargetIdentifer",
    "ElevationWithError",
    "EmptySuccessResponse",
    "Feature",
    "FeatureCollection",
    "FeatureCollectionTypes",
    "FeaturePropertyKey",
    "FederatedAndQuery",
    "FederatedNotQuery",
    "FederatedOrQuery",
    "FederatedSearchJsonQuery",
    "FederatedSource",
    "FederatedSourceName",
    "FederatedTermQuery",
    "GeoCircle",
    "GeoJsonObject",
    "GeoPoint",
    "GeoPolygon",
    "Geometry",
    "GeometryCollection",
    "GeotimeSeriesExternalReference",
    "GeotimeTrackRid",
    "GetFederatedSourceResponse",
    "GetMediaResponse",
    "GroupName",
    "GroupRecipient",
    "HighPriorityTargetListAgm",
    "HighPriorityTargetListAgmId",
    "HighPriorityTargetListEffectType",
    "HighPriorityTargetListRid",
    "HighPriorityTargetListTargetId",
    "HighPriorityTargetListTargetV2",
    "HighPriorityTargetListV2",
    "HighPriorityTargetListWhen",
    "HptlTargetAoi",
    "HptlTargetAoiId",
    "HptlTargetAoiUnion",
    "HptlTargetElnot",
    "HptlTargetEntityAoi",
    "HptlTargetGeoAoi",
    "HptlTargetSubtype",
    "IntelChatMessage",
    "IntelDomain",
    "IntelDossier",
    "IntelFoundryObject",
    "IntelFreeText",
    "IntelGeotimeObservation",
    "IntelId",
    "IntelMedia",
    "IntelPgObject",
    "IntelUnion",
    "JpdiId",
    "LineString",
    "LineStringCoordinates",
    "LinearRing",
    "LinkTypeApiName",
    "LoadHighPriorityTargetListResponseV2",
    "LoadTargetBoardResponseV2",
    "LoadTargetPuckResponse",
    "LoadTargetPucksResponse",
    "LoadTargetResponseV2",
    "Location3dWithError",
    "LocationSource",
    "Media",
    "MediaRid",
    "MediaType",
    "MensurationData",
    "MessageSecurity",
    "MessageSender",
    "MessageSourceId",
    "MultiLineString",
    "MultiPoint",
    "MultiPolygon",
    "Namespace",
    "NamespaceName",
    "ObjectComponentSecurity",
    "ObjectPrimaryKey",
    "ObjectTypeApiName",
    "PageSize",
    "PageToken",
    "Permission",
    "PermissionItem",
    "Point",
    "Polygon",
    "PortionMarking",
    "Position",
    "PreviewMode",
    "PropertyApiName",
    "PropertyId",
    "PropertyValue",
    "SecureTextBody",
    "SecureTextTitle",
    "SecurityKey",
    "SendMessageFailure",
    "SendMessageFailureReason",
    "SendMessageRequest",
    "SendMessageResponse",
    "SendMessagesResponse",
    "ServiceName",
    "SizeBytes",
    "TargetAimpointId",
    "TargetAimpointV2",
    "TargetBoard",
    "TargetBoardColumnConfiguration",
    "TargetBoardColumnConfigurationId",
    "TargetBoardColumnId",
    "TargetBoardConfiguration",
    "TargetBoardRid",
    "TargetBranchId",
    "TargetDetails",
    "TargetIdentifier",
    "TargetIdentifierEnum",
    "TargetLocation",
    "TargetObservation",
    "TargetPuckId",
    "TargetPuckLoadLevel",
    "TargetPuckStatus",
    "TargetRid",
    "TargetV2",
    "TextFormatStyle",
]
