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
from dataclasses import dataclass

import typing_extensions

from gotham import _errors as errors
from gotham.v1.geotime import models as geotime_models
from gotham.v1.gotham import models as gotham_models


class ApiFeaturePreviewUsageOnlyParameters(typing_extensions.TypedDict):
    """
    This feature is only supported in preview mode. Please use `preview=true` in the query
    parameters to call this endpoint.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class ApiFeaturePreviewUsageOnly(errors.BadRequestError):
    name: typing.Literal["ApiFeaturePreviewUsageOnly"]
    parameters: ApiFeaturePreviewUsageOnlyParameters
    error_instance_id: str


class BasicLinkTypeNotFoundParameters(typing_extensions.TypedDict):
    """The link type is not found, or the user does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    linkType: gotham_models.LinkTypeApiName


@dataclass
class BasicLinkTypeNotFound(errors.NotFoundError):
    name: typing.Literal["BasicLinkTypeNotFound"]
    parameters: BasicLinkTypeNotFoundParameters
    error_instance_id: str


class DisallowedPropertyTypesParameters(typing_extensions.TypedDict):
    """
    At least one disallowed property type was included when creating an object, and strict validation
    was required.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    disallowedProperties: typing.List[gotham_models.PropertyApiName]


@dataclass
class DisallowedPropertyTypes(errors.BadRequestError):
    name: typing.Literal["DisallowedPropertyTypes"]
    parameters: DisallowedPropertyTypesParameters
    error_instance_id: str


class FederatedObjectUpdateNotAllowedParameters(typing_extensions.TypedDict):
    """Updating objects that exist in a federated source system is not allowed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: gotham_models.ObjectPrimaryKey


@dataclass
class FederatedObjectUpdateNotAllowed(errors.BadRequestError):
    name: typing.Literal["FederatedObjectUpdateNotAllowed"]
    parameters: FederatedObjectUpdateNotAllowedParameters
    error_instance_id: str


class FederatedSourceNotFoundParameters(typing_extensions.TypedDict):
    """The requested federated source was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    federatedSource: gotham_models.FederatedSourceName


@dataclass
class FederatedSourceNotFound(errors.NotFoundError):
    name: typing.Literal["FederatedSourceNotFound"]
    parameters: FederatedSourceNotFoundParameters
    error_instance_id: str


class InvalidClassificationPortionMarkingsParameters(typing_extensions.TypedDict):
    """The specified portion markings are not valid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    portionMarkings: typing.List[gotham_models.PortionMarking]


@dataclass
class InvalidClassificationPortionMarkings(errors.BadRequestError):
    name: typing.Literal["InvalidClassificationPortionMarkings"]
    parameters: InvalidClassificationPortionMarkingsParameters
    error_instance_id: str


class InvalidGeotimeObservationsParameters(typing_extensions.TypedDict):
    """At least one Observation was invalid, so none were written to Geotime."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidObservations: typing.List[geotime_models.InvalidObservation]


@dataclass
class InvalidGeotimeObservations(errors.BadRequestError):
    name: typing.Literal["InvalidGeotimeObservations"]
    parameters: InvalidGeotimeObservationsParameters
    error_instance_id: str


class InvalidMessagePortionMarkingsParameters(typing_extensions.TypedDict):
    """The supplied portion markings for the message security are not valid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    portionMarkings: typing.List[str]


@dataclass
class InvalidMessagePortionMarkings(errors.BadRequestError):
    name: typing.Literal["InvalidMessagePortionMarkings"]
    parameters: InvalidMessagePortionMarkingsParameters
    error_instance_id: str


class InvalidMessageRequestsParameters(typing_extensions.TypedDict):
    """
    Validation of the message request failed in Inbox.
    This commonly means that the number of recipients or message text exceeded the maximum allowed
    Inbox limits.
    Details of the failing messages and fields are given in the `inboxErrorMessage`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    inboxErrorMessage: typing_extensions.NotRequired[str]


@dataclass
class InvalidMessageRequests(errors.BadRequestError):
    name: typing.Literal["InvalidMessageRequests"]
    parameters: InvalidMessageRequestsParameters
    error_instance_id: str


class InvalidObjectRidParameters(typing_extensions.TypedDict):
    """The provided rid is not a valid ObjectRid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectRid: geotime_models.ObjectRid


@dataclass
class InvalidObjectRid(errors.BadRequestError):
    name: typing.Literal["InvalidObjectRid"]
    parameters: InvalidObjectRidParameters
    error_instance_id: str


class InvalidOntologyTypesParameters(typing_extensions.TypedDict):
    """At least one specified ontology type was invalid (property type, link type, object type)."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidPropertyTypes: typing.List[gotham_models.PropertyApiName]
    invalidObjectTypes: typing.List[gotham_models.ObjectTypeApiName]
    invalidLinkTypes: typing.List[gotham_models.LinkTypeApiName]


@dataclass
class InvalidOntologyTypes(errors.BadRequestError):
    name: typing.Literal["InvalidOntologyTypes"]
    parameters: InvalidOntologyTypesParameters
    error_instance_id: str


class InvalidPageSizeParameters(typing_extensions.TypedDict):
    """The provided page size was zero or negative. Page sizes must be greater than zero."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageSize: gotham_models.PageSize


@dataclass
class InvalidPageSize(errors.BadRequestError):
    name: typing.Literal["InvalidPageSize"]
    parameters: InvalidPageSizeParameters
    error_instance_id: str


class InvalidPageTokenParameters(typing_extensions.TypedDict):
    """The provided page token could not be used to retrieve the next page of results."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    pageToken: gotham_models.PageToken


@dataclass
class InvalidPageToken(errors.BadRequestError):
    name: typing.Literal["InvalidPageToken"]
    parameters: InvalidPageTokenParameters
    error_instance_id: str


class InvalidPermissionsParameters(typing_extensions.TypedDict):
    """The listed groups specified in the permissions do not exist, or an unknown permission type was specified."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupNames: typing.List[gotham_models.GroupName]


@dataclass
class InvalidPermissions(errors.BadRequestError):
    name: typing.Literal["InvalidPermissions"]
    parameters: InvalidPermissionsParameters
    error_instance_id: str


class InvalidPropertyValueParameters(typing_extensions.TypedDict):
    """
    At least one disallowed property type was included when creating an object, and strict validation
    was required.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    propertyType: gotham_models.PropertyApiName
    propertyValue: gotham_models.PropertyValue
    reason: str


@dataclass
class InvalidPropertyValue(errors.BadRequestError):
    name: typing.Literal["InvalidPropertyValue"]
    parameters: InvalidPropertyValueParameters
    error_instance_id: str


class InvalidSidcParameters(typing_extensions.TypedDict):
    """The specified symbol identification code (SIDC) was not valid based on MIL-STD-2525C specification"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    invalidSidc: str


@dataclass
class InvalidSidc(errors.BadRequestError):
    name: typing.Literal["InvalidSidc"]
    parameters: InvalidSidcParameters
    error_instance_id: str


class InvalidTrackRidParameters(typing_extensions.TypedDict):
    """The provided rid is not a valid Track rid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trackRid: geotime_models.TrackRid


@dataclass
class InvalidTrackRid(errors.BadRequestError):
    name: typing.Literal["InvalidTrackRid"]
    parameters: InvalidTrackRidParameters
    error_instance_id: str


class MalformedObjectPrimaryKeysParameters(typing_extensions.TypedDict):
    """The requested object primary key or keys are malformed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKeys: typing.List[gotham_models.ObjectPrimaryKey]


@dataclass
class MalformedObjectPrimaryKeys(errors.BadRequestError):
    name: typing.Literal["MalformedObjectPrimaryKeys"]
    parameters: MalformedObjectPrimaryKeysParameters
    error_instance_id: str


class MalformedPropertyFiltersParameters(typing_extensions.TypedDict):
    """At least one of requested filters are malformed. Please look at the documentation of `SearchObjectsRequest`."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore


@dataclass
class MalformedPropertyFilters(errors.BadRequestError):
    name: typing.Literal["MalformedPropertyFilters"]
    parameters: MalformedPropertyFiltersParameters
    error_instance_id: str


class MalformedUnresolveRequestParameters(typing_extensions.TypedDict):
    """
    The unresolve request was malformed, either because no objects would be unresolved or because the primary object
    would be unresolved from itself. Please look at the documentation of `UnresolveObjects`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    safeErrorMessage: str


@dataclass
class MalformedUnresolveRequest(errors.BadRequestError):
    name: typing.Literal["MalformedUnresolveRequest"]
    parameters: MalformedUnresolveRequestParameters
    error_instance_id: str


class MediaNotFoundParameters(typing_extensions.TypedDict):
    """The requested media was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    mediaId: gotham_models.MediaRid


@dataclass
class MediaNotFound(errors.NotFoundError):
    name: typing.Literal["MediaNotFound"]
    parameters: MediaNotFoundParameters
    error_instance_id: str


class MissingRepresentativePropertyTypesParameters(typing_extensions.TypedDict):
    """
    At least one representative property type was not included when creating an object, and strict validation
    was required.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    missingRepresentativeProperties: typing.List[gotham_models.PropertyApiName]


@dataclass
class MissingRepresentativePropertyTypes(errors.BadRequestError):
    name: typing.Literal["MissingRepresentativePropertyTypes"]
    parameters: MissingRepresentativePropertyTypesParameters
    error_instance_id: str


class NamespaceNotFoundParameters(typing_extensions.TypedDict):
    """The requested namespace was not found in the given federated source."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    federatedSource: gotham_models.FederatedSourceName
    namespace: gotham_models.NamespaceName


@dataclass
class NamespaceNotFound(errors.NotFoundError):
    name: typing.Literal["NamespaceNotFound"]
    parameters: NamespaceNotFoundParameters
    error_instance_id: str


class NoLocatorFoundForRidParameters(typing_extensions.TypedDict):
    """Could not find the locator for the given Object rid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectRid: geotime_models.ObjectRid


@dataclass
class NoLocatorFoundForRid(errors.BadRequestError):
    name: typing.Literal["NoLocatorFoundForRid"]
    parameters: NoLocatorFoundForRidParameters
    error_instance_id: str


class ObjectNotFoundParameters(typing_extensions.TypedDict):
    """The requested object was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKeys: typing.List[gotham_models.ObjectPrimaryKey]


@dataclass
class ObjectNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectNotFound"]
    parameters: ObjectNotFoundParameters
    error_instance_id: str


class ObjectTypeNotFoundParameters(typing_extensions.TypedDict):
    """The requested object type is not found, or the client token does not have access to it."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: gotham_models.ObjectTypeApiName


@dataclass
class ObjectTypeNotFound(errors.NotFoundError):
    name: typing.Literal["ObjectTypeNotFound"]
    parameters: ObjectTypeNotFoundParameters
    error_instance_id: str


class PropertiesNotFoundParameters(typing_extensions.TypedDict):
    """The requested properties are not found on the object type."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectType: gotham_models.ObjectTypeApiName
    properties: typing.List[gotham_models.PropertyApiName]


@dataclass
class PropertiesNotFound(errors.NotFoundError):
    name: typing.Literal["PropertiesNotFound"]
    parameters: PropertiesNotFoundParameters
    error_instance_id: str


class PropertyNotFoundParameters(typing_extensions.TypedDict):
    """The requested property was not found on the object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: gotham_models.ObjectPrimaryKey
    propertyId: gotham_models.PropertyId


@dataclass
class PropertyNotFound(errors.NotFoundError):
    name: typing.Literal["PropertyNotFound"]
    parameters: PropertyNotFoundParameters
    error_instance_id: str


class PutConvolutionMetadataErrorParameters(typing_extensions.TypedDict):
    """Could not store metadata for convolved ellipses"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    convolvedEllipses: typing.List[gotham_models.GeotimeSeriesExternalReference]


@dataclass
class PutConvolutionMetadataError(errors.InternalServerError):
    name: typing.Literal["PutConvolutionMetadataError"]
    parameters: PutConvolutionMetadataErrorParameters
    error_instance_id: str


class ResolvedObjectComponentsNotFoundParameters(typing_extensions.TypedDict):
    """The requested object primary keys to unresolve are not found in the given resolved object."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    missingPrimaryKeys: typing.List[gotham_models.ObjectPrimaryKey]


@dataclass
class ResolvedObjectComponentsNotFound(errors.NotFoundError):
    name: typing.Literal["ResolvedObjectComponentsNotFound"]
    parameters: ResolvedObjectComponentsNotFoundParameters
    error_instance_id: str


class ServiceNotConfiguredParameters(typing_extensions.TypedDict):
    """The service necessary to complete this request is not installed on the stack"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    serviceName: gotham_models.ServiceName


@dataclass
class ServiceNotConfigured(errors.NotFoundError):
    name: typing.Literal["ServiceNotConfigured"]
    parameters: ServiceNotConfiguredParameters
    error_instance_id: str


class TargetNotOnTargetBoardParameters(typing_extensions.TypedDict):
    """Target must be located on the request target board."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    targetRid: gotham_models.TargetRid
    boardRid: gotham_models.TargetBoardRid


@dataclass
class TargetNotOnTargetBoard(errors.BadRequestError):
    name: typing.Literal["TargetNotOnTargetBoard"]
    parameters: TargetNotOnTargetBoardParameters
    error_instance_id: str


class TrackToObjectLinkageFailureParameters(typing_extensions.TypedDict):
    """Could not link the given Track and Object"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trackRid: geotime_models.TrackRid
    targetRid: geotime_models.ObjectRid


@dataclass
class TrackToObjectLinkageFailure(errors.InternalServerError):
    name: typing.Literal["TrackToObjectLinkageFailure"]
    parameters: TrackToObjectLinkageFailureParameters
    error_instance_id: str


class TrackToObjectUnlinkageFailureParameters(typing_extensions.TypedDict):
    """Could not unlink the given Track and Object"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trackRid: geotime_models.TrackRid
    objectRid: geotime_models.ObjectRid


@dataclass
class TrackToObjectUnlinkageFailure(errors.InternalServerError):
    name: typing.Literal["TrackToObjectUnlinkageFailure"]
    parameters: TrackToObjectUnlinkageFailureParameters
    error_instance_id: str


class TrackToTrackLinkageFailureParameters(typing_extensions.TypedDict):
    """Could not link the given Tracks"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trackRid: geotime_models.TrackRid
    otherTrackRid: geotime_models.TrackRid


@dataclass
class TrackToTrackLinkageFailure(errors.InternalServerError):
    name: typing.Literal["TrackToTrackLinkageFailure"]
    parameters: TrackToTrackLinkageFailureParameters
    error_instance_id: str


class TrackToTrackUnlinkageFailureParameters(typing_extensions.TypedDict):
    """Could not unlink the given Tracks"""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trackRid: geotime_models.TrackRid
    otherTrackRid: geotime_models.TrackRid


@dataclass
class TrackToTrackUnlinkageFailure(errors.InternalServerError):
    name: typing.Literal["TrackToTrackUnlinkageFailure"]
    parameters: TrackToTrackUnlinkageFailureParameters
    error_instance_id: str


class UnclearGeotimeSeriesReferenceParameters(typing_extensions.TypedDict):
    """One of GeotimeTrackRid or GeotimeSeriesExternalReference may be specified, but not both."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    geotimeTrack: gotham_models.GeotimeTrackRid
    geotimeSeriesExternalReference: gotham_models.GeotimeSeriesExternalReference


@dataclass
class UnclearGeotimeSeriesReference(errors.BadRequestError):
    name: typing.Literal["UnclearGeotimeSeriesReference"]
    parameters: UnclearGeotimeSeriesReferenceParameters
    error_instance_id: str


class UnclearMultiSourcePropertyUpdateRequestParameters(typing_extensions.TypedDict):
    """
    The update to a component from multiple sources is unclear. This commonly means that
    a component subject to update has multiple sources and the caller did not specify whether to
    apply to all or a specific source.  Adjust request and try again.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    primaryKey: gotham_models.ObjectPrimaryKey
    propertyId: gotham_models.PropertyId


@dataclass
class UnclearMultiSourcePropertyUpdateRequest(errors.BadRequestError):
    name: typing.Literal["UnclearMultiSourcePropertyUpdateRequest"]
    parameters: UnclearMultiSourcePropertyUpdateRequestParameters
    error_instance_id: str


class UnknownRecipientsParameters(typing_extensions.TypedDict):
    """
    The supplied message recipients are not valid.
    Please ensure the group names supplied are valid, and belong to their supplied realm,
    or belong to the caller's realm if no realm was specified.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupRecipients: typing.List[gotham_models.GroupRecipient]


@dataclass
class UnknownRecipients(errors.BadRequestError):
    name: typing.Literal["UnknownRecipients"]
    parameters: UnknownRecipientsParameters
    error_instance_id: str


class UserHasNoOwnerPermsParameters(typing_extensions.TypedDict):
    """The user is required to have owner permissions on the artifact."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    artifactId: str


@dataclass
class UserHasNoOwnerPerms(errors.BadRequestError):
    name: typing.Literal["UserHasNoOwnerPerms"]
    parameters: UserHasNoOwnerPermsParameters
    error_instance_id: str


class WriteGeotimeObservationSizeLimitParameters(typing_extensions.TypedDict):
    """The write request contained too many observations, so none were written to Geotime."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    requestSize: int
    maxSize: int


@dataclass
class WriteGeotimeObservationSizeLimit(errors.BadRequestError):
    name: typing.Literal["WriteGeotimeObservationSizeLimit"]
    parameters: WriteGeotimeObservationSizeLimitParameters
    error_instance_id: str


__all__ = [
    "ApiFeaturePreviewUsageOnly",
    "BasicLinkTypeNotFound",
    "DisallowedPropertyTypes",
    "FederatedObjectUpdateNotAllowed",
    "FederatedSourceNotFound",
    "InvalidClassificationPortionMarkings",
    "InvalidGeotimeObservations",
    "InvalidMessagePortionMarkings",
    "InvalidMessageRequests",
    "InvalidObjectRid",
    "InvalidOntologyTypes",
    "InvalidPageSize",
    "InvalidPageToken",
    "InvalidPermissions",
    "InvalidPropertyValue",
    "InvalidSidc",
    "InvalidTrackRid",
    "MalformedObjectPrimaryKeys",
    "MalformedPropertyFilters",
    "MalformedUnresolveRequest",
    "MediaNotFound",
    "MissingRepresentativePropertyTypes",
    "NamespaceNotFound",
    "NoLocatorFoundForRid",
    "ObjectNotFound",
    "ObjectTypeNotFound",
    "PropertiesNotFound",
    "PropertyNotFound",
    "PutConvolutionMetadataError",
    "ResolvedObjectComponentsNotFound",
    "ServiceNotConfigured",
    "TargetNotOnTargetBoard",
    "TrackToObjectLinkageFailure",
    "TrackToObjectUnlinkageFailure",
    "TrackToTrackLinkageFailure",
    "TrackToTrackUnlinkageFailure",
    "UnclearGeotimeSeriesReference",
    "UnclearMultiSourcePropertyUpdateRequest",
    "UnknownRecipients",
    "UserHasNoOwnerPerms",
    "WriteGeotimeObservationSizeLimit",
]
