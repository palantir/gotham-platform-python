# Geotime

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**link_track_and_object**](#link_track_and_object) | **POST** /gotham/v1/tracks/linkToObject | Stable |
[**link_tracks**](#link_tracks) | **POST** /gotham/v1/tracks/linkTracks | Stable |
[**put_convolution_metadata**](#put_convolution_metadata) | **PUT** /gotham/v1/convolution/metadata | Stable |
[**search_latest_observations**](#search_latest_observations) | **POST** /gotham/v1/observations/latest/{observationSpecId}/search | Stable |
[**search_observation_histories**](#search_observation_histories) | **POST** /gotham/v1/observations/history/{observationSpecId}/search | Stable |
[**unlink_track_and_object**](#unlink_track_and_object) | **POST** /gotham/v1/tracks/unlinkFromObject | Stable |
[**unlink_tracks**](#unlink_tracks) | **POST** /gotham/v1/tracks/unlinkTracks | Stable |
[**write_observations**](#write_observations) | **POST** /gotham/v1/observations | Stable |

# **link_track_and_object**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Links a Geotime Track with an Object, by ensuring that the Track has a "pointer"
to its Object, and vice versa.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**object_rid** | ObjectRid |  |  |
**track_rid** | TrackRid |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ObjectRid
object_rid = "ri.gotham.1-1.object.someString"
# TrackRid
track_rid = "ri.gotham.1-1.geotime-track.foo.bar.baz.track0"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.link_track_and_object(
        object_rid=object_rid, track_rid=track_rid, preview=preview
    )
    print("The link_track_and_object response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.link_track_and_object: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | A successful response means that the Track has been linked to the Object. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **link_tracks**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Links a Geotime Track with another Track, by ensuring that the Tracks have "pointers" to each other.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**other_track_rid** | TrackRid |  |  |
**track_rid** | TrackRid |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TrackRid
other_track_rid = "ri.gotham.1-1.geotime-track.foo.bar.baz.track1"
# TrackRid
track_rid = "ri.gotham.1-1.geotime-track.foo.bar.baz.track0"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.link_tracks(
        other_track_rid=other_track_rid, track_rid=track_rid, preview=preview
    )
    print("The link_tracks response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.link_tracks: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | A successful response means that the Tracks have been linked. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **put_convolution_metadata**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Stores metadata about a convolved ellipse.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**convolutions** | List[ConvolvedMetadata] |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[ConvolvedMetadata]
convolutions = [
    {
        "convolvedEllipseId": {
            "seriesId": "convolved-ellipse-1",
            "observationSpecId": "obs-1",
            "sourceSystemSpecId": "sys-1",
            "collectionId": "col-1",
        },
        "components": [
            {
                "ellipseId": {
                    "seriesId": "ellipse-1",
                    "observationSpecId": "obs-2",
                    "sourceSystemSpecId": "sys-2",
                    "collectionId": "col-2",
                },
                "convolutionTimestamp": "2022-01-01T00:00:00Z",
                "userId": "user-1",
            },
            {
                "ellipseId": {
                    "seriesId": "ellipse-2",
                    "observationSpecId": "obs-3",
                    "sourceSystemSpecId": "sys-3",
                    "collectionId": "col-3",
                },
                "convolutionTimestamp": "2022-01-02T00:00:00Z",
                "userId": "user-2",
            },
        ],
    }
]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.put_convolution_metadata(
        convolutions=convolutions, preview=preview
    )
    print("The put_convolution_metadata response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.put_convolution_metadata: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | A successful response means that the Tracks have been unlinked. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **search_latest_observations**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Gets the latest Observation along each Geotime Track matching the supplied query. Only returns Observations
conforming to the given Observation Spec.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**observation_spec_id** | ObservationSpecId | Search results will be constrained to Observations conforming to this Observation Spec.  |  |
**query** | ObservationQuery |  |  |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**SearchLatestObservationsResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ObservationSpecId | Search results will be constrained to Observations conforming to this Observation Spec.
observation_spec_id = "baz"
# ObservationQuery
query = {"time": {"start": "2023-01-01T12:00:00Z", "end": "2023-03-07T12:10:00Z"}}
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.search_latest_observations(
        observation_spec_id, query=query, page_token=page_token, preview=preview
    )
    print("The search_latest_observations response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.search_latest_observations: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchLatestObservationsResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **search_observation_histories**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Gets clipped Observation histories along each Geotime Track matching the supplied query. Histories are clipped
based on the supplied history window. If no history window is supplied, a default history window of the past 
7 days is used. Only returns Observations conforming to the given Observation Spec.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**observation_spec_id** | ObservationSpecId | Search results will be constrained to Observations conforming to this Observation Spec.  |  |
**query** | ObservationQuery |  |  |
**history_window** | Optional[TimeQuery] |  | [optional] |
**page_token** | Optional[PageToken] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**SearchObservationHistoryResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ObservationSpecId | Search results will be constrained to Observations conforming to this Observation Spec.
observation_spec_id = "baz"
# ObservationQuery
query = {
    "time": {"start": "2023-01-01T12:00:00Z", "end": "2023-03-07T12:10:00Z"},
    "historyWindow": {"start": "2023-03-07T12:00:00Z", "end": "2023-03-07T12:10:00Z"},
}
# Optional[TimeQuery]
history_window = None
# Optional[PageToken]
page_token = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.search_observation_histories(
        observation_spec_id,
        query=query,
        history_window=history_window,
        page_token=page_token,
        preview=preview,
    )
    print("The search_observation_histories response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.search_observation_histories: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchObservationHistoryResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **unlink_track_and_object**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Unlinks a Geotime Track from an Object, by ensuring that we remove any "pointers" between the Track and Object


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**object_rid** | ObjectRid |  |  |
**track_rid** | TrackRid |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ObjectRid
object_rid = "ri.gotham.1-1.object.someString"
# TrackRid
track_rid = "ri.gotham.1-1.geotime-track.foo.bar.baz.track0"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.unlink_track_and_object(
        object_rid=object_rid, track_rid=track_rid, preview=preview
    )
    print("The unlink_track_and_object response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.unlink_track_and_object: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | A successful response means that the Track has been unlinked from the Object. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **unlink_tracks**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Unlinks a Geotime Track from another Track, removing any "pointers" between the Tracks.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**other_track_rid** | TrackRid |  |  |
**track_rid** | TrackRid |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TrackRid
other_track_rid = "ri.gotham.1-1.geotime-track.foo.bar.baz.track1"
# TrackRid
track_rid = "ri.gotham.1-1.geotime-track.foo.bar.baz.track0"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.unlink_tracks(
        other_track_rid=other_track_rid, track_rid=track_rid, preview=preview
    )
    print("The unlink_tracks response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.unlink_tracks: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | A successful response means that the Tracks have been unlinked. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **write_observations**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Writes Observations directly to Geotime. Returns the Observations that could not be written to Geotime with the
reason for why they could not be written. Any Observations not in the response are guaranteed to have been
written successfully to Geotime's backing data store.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**write_observations_request** | WriteObservationsRequest | Body of the request |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**WriteObservationsResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# WriteObservationsRequest | Body of the request
write_observations_request = [
    {
        "sourceSystemId": "foo",
        "collectionId": "bar",
        "observationSpecId": "baz",
        "trackId": "track0",
        "position": {"longitude": -122.16219, "latitude": 37.44274},
        "timestamp": "2023-01-01T22:00:00Z",
        "name": "name0",
        "staticProperties": [],
        "liveProperties": [],
    },
    {
        "sourceSystemId": "foo",
        "collectionId": "bar",
        "observationSpecId": "baz",
        "trackId": "track1",
        "position": {"longitude": -122.16165, "latitude": 37.44215},
        "timestamp": "fakeInvalidTimestamp",
        "name": "name1",
        "staticProperties": [],
        "liveProperties": [],
    },
]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.geotime.Geotime.write_observations(
        write_observations_request, preview=preview
    )
    print("The write_observations response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Geotime.write_observations: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | WriteObservationsResponse  | Response with information about any Observations that failed to be written. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

