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
from gotham.v1.geotime import models as geotime_models
from gotham.v1.gotham import models as gotham_models


class GeotimeClient:
    """
    The API client for the Geotime Resource.

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

        self.with_streaming_response = _GeotimeClientStreaming(self)
        self.with_raw_response = _GeotimeClientRaw(self)

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def link_track_and_object(
        self,
        *,
        object_rid: geotime_models.ObjectRid,
        track_rid: geotime_models.TrackRid,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Links a Geotime Track with an Object, by ensuring that the Track has a "pointer"
        to its Object, and vice versa.

        :param object_rid:
        :type object_rid: ObjectRid
        :param track_rid:
        :type track_rid: TrackRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/tracks/linkToObject",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "trackRid": track_rid,
                    "objectRid": object_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "trackRid": geotime_models.TrackRid,
                        "objectRid": geotime_models.ObjectRid,
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
    def link_tracks(
        self,
        *,
        other_track_rid: geotime_models.TrackRid,
        track_rid: geotime_models.TrackRid,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Links a Geotime Track with another Track, by ensuring that the Tracks have "pointers" to each other.

        :param other_track_rid:
        :type other_track_rid: TrackRid
        :param track_rid:
        :type track_rid: TrackRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/tracks/linkTracks",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "trackRid": track_rid,
                    "otherTrackRid": other_track_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "trackRid": geotime_models.TrackRid,
                        "otherTrackRid": geotime_models.TrackRid,
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
    def put_convolution_metadata(
        self,
        *,
        convolutions: typing.List[geotime_models.ConvolvedMetadata],
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Stores metadata about a convolved ellipse.

        :param convolutions:
        :type convolutions: List[ConvolvedMetadata]
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
                resource_path="/gotham/v1/convolution/metadata",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "convolutions": convolutions,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "convolutions": typing.List[geotime_models.ConvolvedMetadata],
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
    def search_latest_observations(
        self,
        observation_spec_id: geotime_models.ObservationSpecId,
        *,
        query: geotime_models.ObservationQuery,
        page_token: typing.Optional[gotham_models.PageToken] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> geotime_models.SearchLatestObservationsResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Gets the latest Observation along each Geotime Track matching the supplied query. Only returns Observations
        conforming to the given Observation Spec.

        :param observation_spec_id: Search results will be constrained to Observations conforming to this Observation Spec.
        :type observation_spec_id: ObservationSpecId
        :param query:
        :type query: ObservationQuery
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: geotime_models.SearchLatestObservationsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/observations/latest/{observationSpecId}/search",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "observationSpecId": observation_spec_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": geotime_models.ObservationQuery,
                        "pageToken": typing.Optional[gotham_models.PageToken],
                    },
                ),
                response_type=geotime_models.SearchLatestObservationsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search_observation_histories(
        self,
        observation_spec_id: geotime_models.ObservationSpecId,
        *,
        query: geotime_models.ObservationQuery,
        history_window: typing.Optional[geotime_models.TimeQuery] = None,
        page_token: typing.Optional[gotham_models.PageToken] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> geotime_models.SearchObservationHistoryResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Gets clipped Observation histories along each Geotime Track matching the supplied query. Histories are clipped
        based on the supplied history window. If no history window is supplied, a default history window of the past
        7 days is used. Only returns Observations conforming to the given Observation Spec.

        :param observation_spec_id: Search results will be constrained to Observations conforming to this Observation Spec.
        :type observation_spec_id: ObservationSpecId
        :param query:
        :type query: ObservationQuery
        :param history_window:
        :type history_window: Optional[TimeQuery]
        :param page_token:
        :type page_token: Optional[PageToken]
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: geotime_models.SearchObservationHistoryResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/observations/history/{observationSpecId}/search",
                query_params={
                    "preview": preview,
                },
                path_params={
                    "observationSpecId": observation_spec_id,
                },
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "query": query,
                    "historyWindow": history_window,
                    "pageToken": page_token,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "query": geotime_models.ObservationQuery,
                        "historyWindow": typing.Optional[geotime_models.TimeQuery],
                        "pageToken": typing.Optional[gotham_models.PageToken],
                    },
                ),
                response_type=geotime_models.SearchObservationHistoryResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )

    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def unlink_track_and_object(
        self,
        *,
        object_rid: geotime_models.ObjectRid,
        track_rid: geotime_models.TrackRid,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Unlinks a Geotime Track from an Object, by ensuring that we remove any "pointers" between the Track and Object

        :param object_rid:
        :type object_rid: ObjectRid
        :param track_rid:
        :type track_rid: TrackRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/tracks/unlinkFromObject",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "trackRid": track_rid,
                    "objectRid": object_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "trackRid": geotime_models.TrackRid,
                        "objectRid": geotime_models.ObjectRid,
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
    def unlink_tracks(
        self,
        *,
        other_track_rid: geotime_models.TrackRid,
        track_rid: geotime_models.TrackRid,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> gotham_models.EmptySuccessResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Unlinks a Geotime Track from another Track, removing any "pointers" between the Tracks.

        :param other_track_rid:
        :type other_track_rid: TrackRid
        :param track_rid:
        :type track_rid: TrackRid
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: gotham_models.EmptySuccessResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/tracks/unlinkTracks",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body={
                    "trackRid": track_rid,
                    "otherTrackRid": other_track_rid,
                },
                body_type=typing_extensions.TypedDict(
                    "Body",
                    {  # type: ignore
                        "trackRid": geotime_models.TrackRid,
                        "otherTrackRid": geotime_models.TrackRid,
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
    def write_observations(
        self,
        write_observations_request: geotime_models.WriteObservationsRequest,
        *,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> geotime_models.WriteObservationsResponse:
        """
        :::callout{theme=warning title=Warning}
        This endpoint is in preview and may be modified or removed at any time.
        To use this endpoint, add `preview=true` to the request query parameters.
        :::

        Writes Observations directly to Geotime. Returns the Observations that could not be written to Geotime with the
        reason for why they could not be written. Any Observations not in the response are guaranteed to have been
        written successfully to Geotime's backing data store.

        :param write_observations_request: Body of the request
        :type write_observations_request: WriteObservationsRequest
        :param preview: Represents a boolean value that restricts an endpoint to preview mode when set to true.
        :type preview: Optional[PreviewMode]
        :param request_timeout: timeout setting for this request in seconds.
        :type request_timeout: Optional[int]
        :return: Returns the result object.
        :rtype: geotime_models.WriteObservationsResponse
        """

        return self._api_client.call_api(
            core.RequestInfo(
                method="POST",
                resource_path="/gotham/v1/observations",
                query_params={
                    "preview": preview,
                },
                path_params={},
                header_params={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body=write_observations_request,
                body_type=geotime_models.WriteObservationsRequest,
                response_type=geotime_models.WriteObservationsResponse,
                request_timeout=request_timeout,
                throwable_errors={},
                response_mode=_sdk_internal.get("response_mode"),
            ),
        )


class _GeotimeClientRaw:
    def __init__(self, client: GeotimeClient) -> None:
        def link_track_and_object(_: gotham_models.EmptySuccessResponse): ...
        def link_tracks(_: gotham_models.EmptySuccessResponse): ...
        def put_convolution_metadata(_: gotham_models.EmptySuccessResponse): ...
        def search_latest_observations(_: geotime_models.SearchLatestObservationsResponse): ...
        def search_observation_histories(_: geotime_models.SearchObservationHistoryResponse): ...
        def unlink_track_and_object(_: gotham_models.EmptySuccessResponse): ...
        def unlink_tracks(_: gotham_models.EmptySuccessResponse): ...
        def write_observations(_: geotime_models.WriteObservationsResponse): ...

        self.link_track_and_object = core.with_raw_response(
            link_track_and_object, client.link_track_and_object
        )
        self.link_tracks = core.with_raw_response(link_tracks, client.link_tracks)
        self.put_convolution_metadata = core.with_raw_response(
            put_convolution_metadata, client.put_convolution_metadata
        )
        self.search_latest_observations = core.with_raw_response(
            search_latest_observations, client.search_latest_observations
        )
        self.search_observation_histories = core.with_raw_response(
            search_observation_histories, client.search_observation_histories
        )
        self.unlink_track_and_object = core.with_raw_response(
            unlink_track_and_object, client.unlink_track_and_object
        )
        self.unlink_tracks = core.with_raw_response(unlink_tracks, client.unlink_tracks)
        self.write_observations = core.with_raw_response(
            write_observations, client.write_observations
        )


class _GeotimeClientStreaming:
    def __init__(self, client: GeotimeClient) -> None:
        def link_track_and_object(_: gotham_models.EmptySuccessResponse): ...
        def link_tracks(_: gotham_models.EmptySuccessResponse): ...
        def put_convolution_metadata(_: gotham_models.EmptySuccessResponse): ...
        def search_latest_observations(_: geotime_models.SearchLatestObservationsResponse): ...
        def search_observation_histories(_: geotime_models.SearchObservationHistoryResponse): ...
        def unlink_track_and_object(_: gotham_models.EmptySuccessResponse): ...
        def unlink_tracks(_: gotham_models.EmptySuccessResponse): ...
        def write_observations(_: geotime_models.WriteObservationsResponse): ...

        self.link_track_and_object = core.with_streaming_response(
            link_track_and_object, client.link_track_and_object
        )
        self.link_tracks = core.with_streaming_response(link_tracks, client.link_tracks)
        self.put_convolution_metadata = core.with_streaming_response(
            put_convolution_metadata, client.put_convolution_metadata
        )
        self.search_latest_observations = core.with_streaming_response(
            search_latest_observations, client.search_latest_observations
        )
        self.search_observation_histories = core.with_streaming_response(
            search_observation_histories, client.search_observation_histories
        )
        self.unlink_track_and_object = core.with_streaming_response(
            unlink_track_and_object, client.unlink_track_and_object
        )
        self.unlink_tracks = core.with_streaming_response(unlink_tracks, client.unlink_tracks)
        self.write_observations = core.with_streaming_response(
            write_observations, client.write_observations
        )
