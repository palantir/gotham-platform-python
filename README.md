# Gotham Platform SDK

![Supported Python Versions](https://img.shields.io/pypi/pyversions/gotham-platform-python)
[![PyPI Version](https://img.shields.io/pypi/v/gotham-platform-python)](https://pypi.org/project/gotham-platform-python/)
[![License](https://img.shields.io/badge/License-Apache%202.0-lightgrey.svg)](https://opensource.org/licenses/Apache-2.0)

> [!WARNING]
> This SDK is incubating and subject to change.

The Gotham Platform SDK is a Python SDK built on top of the Gotham API.
Review [Gotham API documentation](https://www.palantir.com/docs/gotham/api/) for more details.

> [!NOTE]
> This Python package is automatically generated based on the Gotham API specification.


<a id="sdk-vs-sdk"></a>
## Gotham Platform SDK vs. Foundry Platform SDK vs. Ontology SDK
Palantir provides two platform APIs for interacting with the Gotham and Foundry platforms. Each has a corresponding Software Development Kit (SDK). There is also the OSDK for interacting with Foundry ontologies. Make sure to choose the correct SDK for your use case. As a general rule of thumb, any applications which leverage the Ontology should use the Ontology SDK over the Foundry platform SDK for a superior development experience.

> [!IMPORTANT]
> Make sure to understand the difference between the Foundry, Gotham, and Ontology SDKs. Review this section before continuing with the installation of this library.

### Ontology SDK
The Ontology SDK allows you to access the full power of the Ontology directly from your development environment. You can generate the Ontology SDK using the Developer Console, a portal for creating and managing applications using Palantir APIs. Review the [Ontology SDK documentation](https://www.palantir.com/docs/foundry/ontology-sdk) for more information.

### Foundry Platform SDK
The Foundry Platform Software Development Kit (SDK) is generated from the Foundry API specification
file. The intention of this SDK is to encompass endpoints related to interacting
with the Foundry platform itself. Although there are Ontology services included by this SDK, this SDK surfaces endpoints
for interacting with Ontological resources such as object types, link types, and action types. In contrast, the OSDK allows you to interact with objects, links and Actions (for example, querying your objects, applying an action).

### Gotham Platform SDK
The Gotham Platform Software Development Kit (SDK) is generated from the Gotham API specification
file. The intention of this SDK is to encompass endpoints related to interacting
with the Gotham platform itself. This includes Gotham apps and data, such as Gaia, Target Workbench, and geotemporal data.

<a id="installation"></a>
## Installation
You can install the Python package using `pip`:

```sh
pip install gotham-platform-python
```

<a id="major-version-link"></a>
## API Versioning
Every endpoint of the Gotham API is versioned using a version number that appears in the URL. For example,
v1 endpoints look like this:

```
https://<hostname>/api/v1/...
```

This SDK exposes several clients, one for each major version of the API. The latest major version of the
SDK is **v1** and is exposed using the `GothamClient` located in the
`gotham` package.

```python
from gotham import GothamClient
```

For other major versions, you must import that specific client from a submodule. For example, to
import the **v1** client from a sub-module you would import it like this:

```python
from gotham.v1 import GothamClient
```

More information about how the API is versioned can be found [here](https://www.palantir.com/docs/gotham/api/general/overview/versioning/).

<a id="authorization"></a>
## Authorization and client initalization
There are two options for authorizing the SDK.

### User token
> [!WARNING]
> User tokens are associated with your personal user account and must not be used in
> production applications or committed to shared or public code repositories. We recommend
> you store test API tokens as environment variables during development. For authorizing
> production applications, you should register an OAuth2 application (see
> [OAuth2 Client](#oauth2-client) below for more details).

You can pass in a user token as an arguments when initializing the `UserTokenAuth`:

```python
import gotham

client = gotham.GothamClient(
    auth=gotham.UserTokenAuth(os.environ["BEARER_TOKEN"]),
    hostname="example.palantirfoundry.com",
)

```

<a id="oauth2-client"></a>
### OAuth2 Client
OAuth2 clients are the recommended way to connect to Gotham in production applications. Currently, this SDK
natively supports the [client credentials grant flow](https://www.palantir.com/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant).
The token obtained by this grant can be used to access resources on behalf of the created service user. To use this
authentication method, you will first need to register a third-party application in Foundry by following [the guide on third-party application registration](https://www.palantir.com/docs/foundry/platform-security-third-party/register-3pa).

To use the confidential client functionality, you first need to construct a
`ConfidentialClientAuth` object. As these service user tokens have a short
lifespan (one hour), we automatically retry all operations one time if a `401`
(Unauthorized) error is thrown after refreshing the token.

```python
import gotham

auth = gotham.ConfidentialClientAuth(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    scopes=[...],  # optional list of scopes
)

```

> [!IMPORTANT]
> Make sure to select the appropriate scopes when initializating the `ConfidentialClientAuth`. You can find the relevant scopes
> in the [endpoint documentation](#apis-link).

After creating the `ConfidentialClientAuth` object, pass it in to the `GothamClient`,

```python
import gotham

client = gotham.GothamClient(auth=auth, hostname="example.palantirfoundry.com")

```

> [!TIP]
> If you want to use the `ConfidentialClientAuth` class independently of the `GothamClient`, you can
> use the `get_token()` method to get the token. You will have to provide a `hostname` when
> instantiating the `ConfidentialClientAuth` object, for example
> `ConfidentialClientAuth(..., hostname="example.palantirfoundry.com")`.

## Quickstart

Follow the [installation procedure](#installation) and determine which [authentication method](#authorization) is
best suited for your instance before following this example. For simplicity, the `UserTokenAuth` class will be used for demonstration
purposes.

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

Want to learn more about this Foundry SDK library? Review the following sections.

↳ [Error handling](#errors): Learn more about HTTP & data validation error handling  
↳ [Pagination](#pagination): Learn how to work with paginated endpoints in the SDK  
↳ [Streaming](#binary-streaming): Learn how to stream binary data from Foundry  
↳ [Static type analysis](#static-types): Learn about the static type analysis capabilities of this library  
↳ [HTTP Session Configuration](#session-config): Learn how to configure the HTTP session.  

<a id="errors"></a>
## Error handling
### Data validation
The SDK employs [Pydantic](https://docs.pydantic.dev/latest/) for runtime validation
of arguments. In the example below, we are passing in a number to `high_priority_target_list`
which should actually be a string type:

```python
client.target_workbench.TargetBoards.create(
	name=name, 
	security=security, 
	configuration=configuration, 
	description=description, 
	high_priority_target_list=123, 
	preview=preview)
```

If you did this, you would receive an error that looks something like:

```python
pydantic_core._pydantic_core.ValidationError: 1 validation error for create
high_priority_target_list
  Input should be a valid string [type=string_type, input_value=123, input_type=int]
    For further information visit https://errors.pydantic.dev/2.5/v/string_type

```

To handle these errors, you can catch `pydantic.ValidationError`. To learn more, see
the [Pydantic error documentation](https://docs.pydantic.dev/latest/errors/errors/).

> [!TIP]
> Pydantic works with static type checkers such as
[pyright](https://github.com/microsoft/pyright) for an improved developer
experience. See [Static Type Analysis](#static-types) below for more information.

### HTTP exceptions
Each operation includes a list of possible exceptions that can be thrown which can be thrown by the server, all of which inherit from `PalantirRPCException`. For example, an operation that interacts with target tracks might throw an `InvalidTrackRid` error, which is defined as follows:

```python
class InvalidTrackRidParameters(typing_extensions.TypedDict):
    """The provided rid is not a valid Track rid."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    trackRid: geotime_models.TrackRid


@dataclass
class InvalidTrackRid(errors.BadRequestError):
    name: typing.Literal["InvalidTrackRid"]
    parameters: InvalidTrackRidParameters
    error_instance_id: str

```
As a user, you can catch this exception and handle it accordingly.

```python
from gotham.v1.gotham._errors.errors import InvalidTrackRid

try:
    response = client.geotime.Geotime.link_tracks(
        other_track_rid=other_track_rid, track_rid=track_rid, preview=preview
    )
    ...
except InvalidTrackRid as e:
    print("Track rid has an incorrect format", e.parameters[...])

```

You can refer to the method documentation to see which exceptions can be thrown. It is also possible to
catch a generic subclass of `PalantirRPCException` such as `BadRequestError` or `NotFoundError`.


| Status Code | Error Class                  |
| ----------- | ---------------------------- |
| 400         | `BadRequestError`            |
| 401         | `UnauthorizedError`          |
| 403         | `PermissionDeniedError`      |
| 404         | `NotFoundError`              |
| 413         | `RequestEntityTooLargeError` |
| 422         | `UnprocessableEntityError`   |
| 429         | `RateLimitError`             |
| >=500,<600  | `InternalServerError`        |
| Other       | `PalantirRPCException`       |

```python
from gotham._errors import PalantirRPCException
from gotham.v1.gotham.errors import BadRequestError

try:
    api_response = client.geotime.Geotime.link_tracks(
        other_track_rid=other_track_rid, track_rid=track_rid, preview=preview
    )
    ...
except BadRequestError as e:
    print("Track rid has an incorrect format", e)
except PalantirRPCException as e:
    print("Another HTTP exception occurred", e)

```

All HTTP exceptions will have the following properties. See the [Gotham API docs](https://www.palantir.com/docs/gotham/api/general/overview/errors) for details about the Gotham error information.

| Property          | Type                   | Description                                                                                                                                                       |
| ----------------- | -----------------------| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name              | str                    | The Palantir error name. See the [Gotham API docs](https://www.palantir.com/docs/gotham/api/general/overview/errors).        |
| error_instance_id | str                    | The Palantir error instance ID. See the [Gotham API docs](https://www.palantir.com/docs/gotham/api/general/overview/errors). |
| parameters        | Dict[str, Any]         | The Palantir error parameters. See the [Gotham API docs](https://www.palantir.com/docs/gotham/api/general/overview/errors).  |

### Other exceptions
There are a handful of other exception classes that could be thrown when instantiating or using a client.

| ErrorClass                 | Thrown Directly | Description                                                                                                                       |
| -------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------- |     
| NotAuthenticated           | Yes             | You used either `ConfidentialClientAuth` or `PublicClientAuth` to make an API call without going through the OAuth process first. |           
| ConnectionError            | Yes             | An issue occurred when connecting to the server. This also catches `ProxyError`.                                                  |
| ProxyError                 | Yes             | An issue occurred when connecting to or authenticating with a proxy server.                                                       |
| TimeoutError               | No              | The request timed out. This catches both `ConnectTimeout`, `ReadTimeout` and `WriteTimeout`.                                      |
| ConnectTimeout             | Yes             | The request timed out when attempting to connect to the server.                                                                   |
| ReadTimeout                | Yes             | The server did not send any data in the allotted amount of time.                                                                  |
| WriteTimeout               | Yes             | There was a timeout when writing data to the server.                                                                              |
| StreamConsumedError        | Yes             | The content of the given stream has already been consumed.                                                                        |
| RequestEntityTooLargeError | Yes             | The request entity is too large.                                                                                                  |
| ConflictError              | Yes             | There was a conflict with another request.                                                                                        |
| SDKInternalError           | Yes             | An unexpected issue occurred and should be reported.                                                                              |

<a id="pagination"></a>
## Pagination
When calling any iterator endpoints, we return a `ResourceIterator` class designed to simplify the process of working
with paginated API endpoints. This class provides a convenient way to fetch, iterate over, and manage pages
of data, while handling the underlying pagination logic.

To iterate over all items, you can simply create a `ResourceIterator` instance and use it in a for loop, like this:

```python
for item in client.geotime.Geotime.search_observation_histories(
    observation_spec_id, query=query, history_window=history_window, preview=preview
):
    print(item)

```

This will automatically fetch and iterate through all the pages of data from the specified API endpoint. For more granular control, you can manually fetch each page using the `next_page_token`.

```python
page = client.geotime.Geotime.search_observation_histories(
    observation_spec_id, query=query, history_window=history_window, preview=preview
)

while page.next_page_token:
    for branch in page.data:
        print(branch)

    page = client.geotime.Geotime.search_observation_histories(
        observation_spec_id,
        query=query,
        history_window=history_window,
        page_token=page.next_page_token,
        preview=preview,
    )

```


<a id="binary-streaming"></a>
## Streaming
This SDK supports streaming binary data using a separate streaming client accessible under
`with_streaming_response` on each Resource. To ensure the stream is closed, you need to use a context
manager when making a request with this client.

```python
# Non-streaming response
with open("result.png", "wb") as f:
    f.write(client.map_rendering.MapRendering.load_generic_symbol(id, preview=preview, size=size))

# Streaming response
with open("result.png", "wb") as f:
    with client.map_rendering.MapRendering.with_streaming_response.load_generic_symbol(
        id, preview=preview, size=size
    ) as response:
        for chunk in response.iter_bytes():
            f.write(chunk)

```

<a id="static-types"></a>
## Static type analysis
This library uses [Pydantic](https://docs.pydantic.dev) for creating and validating data models which you will see in the
method definitions (see [Documentation for Models](#models-link) below for a full list of models). All request parameters with nested
fields are typed as a `Union` between a Pydantic [BaseModel](https://docs.pydantic.dev/latest/api/base_model/) class and a [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict) whereas responses use `Pydantic`
class. For example, here is how `Geotime.search_latest_observations` method is defined in the `Geotime` namespace:

```python
    @core.maybe_ignore_preview
    @pydantic.validate_call
    @errors.handle_unexpected
    def search_latest_observations(
        self,
        observation_spec_id: geotime_models.ObservationSpecId,
        *,
        query: typing.Union[geotime_models.ObservationQuery, geotime_models.ObservationQueryDict],
        page_token: typing.Optional[gotham_models.PageToken] = None,
        preview: typing.Optional[gotham_models.PreviewMode] = None,
        request_timeout: typing.Optional[core.Timeout] = None,
        _sdk_internal: core.SdkInternal = {},
    ) -> geotime_models.SearchLatestObservationsResponse:
        ...

```

In this example, `ObservationQuery` is a `BaseModel` class and `ObservationQueryDict` is a `TypedDict` class. When calling this method,
you can choose whether to pass in a class instance or a dict.

```python
import gotham
from gotham.geotime.models import ObservationQuery, PropertyValuesQuery

client = gotham.GothamClient(...)

# Class instance
result = client.geotime.Geotime.search_latest_observations(
    observation_spec_id=observationSpecId,
    query=ObservationQuery(
        property=PropertyValuesQuery(property="property1", values=["value1", "value2"])
    ),
    preview=True,
)

# Dict
result = client.geotime.Geotime.search_latest_observations(
    observation_spec_id=observationSpecId,
    query={"property": {"property": "property1", "values": ["value1", "value2"]}},
    preview=True,
)

```

> [!TIP]
> A `Pydantic` model can be converted into its `TypedDict` representation using the `to_dict` method. For example, if you handle
> a variable of type `PropertyValuesQuery` and you called `to_dict()` on that variable you would receive a `PropertyValuesQueryDict`
> variable.

If you are using a static type checker (for example, [mypy](https://mypy-lang.org), [pyright](https://github.com/microsoft/pyright)), you
get static type analysis for the arguments you provide to the function and with the response. For example, if you pass an `int`
to `map_name` but `map_name` expects a string or if you try to access `mapName` on the returned [`Map`](docs/Map.md) object (the
property is actually called `name`), you will get the following errors:


```python
maps = gotham_client.gaia.Map.search(
    # ERROR: "Literal[123]" is incompatible with "GaiaMapName"
    map_name=123,
    preview=True,
)

# ERROR: Cannot access member "mapName" for type "GaiaMapMetadata"
print(maps.results[0].mapName)

```

<a id="session-config"></a>
## HTTP Session Configuration
You can configure various parts of the HTTP session using the `Config` class.

```python
from gotham import Config
from gotham import UserTokenAuth
from gotham import GothamClient

client = GothamClient(
    auth=UserTokenAuth(...),
    hostname="example.palantirfoundry.com",
    config=Config(
        # Set the default headers for every request
        default_headers={"Foo": "Bar"},
        # Default to a 60 second timeout
        timeout=60,
        # Create a proxy for the https protocol
        proxies={"https": "https://10.10.1.10:1080"},
    ),
)

```

The full list of options can be found below.

- `default_headers` (dict[str, str]): HTTP headers to include with all requests.
- `proxies` (dict["http" | "https", str]): Proxies to use for HTTP and HTTPS requests.
- `timeout` (int | float): The default timeout for all requests in seconds.
- `verify` (bool | str): SSL verification, can be a boolean or a path to a CA bundle. Defaults to `True`.
- `default_params` (dict[str, Any]): URL query parameters to include with all requests.
- `scheme` ("http" | "https"): URL scheme to use ('http' or 'https'). Defaults to 'https'.

### SSL Certificate Verification

In addition to the `Config` class, the SSL certificate file used for verification can be set using
the following environment variables (in order of precedence):
- **`REQUESTS_CA_BUNDLE`**
- **`SSL_CERT_FILE`**

The SDK will only check for the presence of these environment variables if the `verify` option is set to
`True` (the default value). If `verify` is set to False, the environment variables will be ignored.

> [!IMPORTANT]
> If you are using an HTTPS proxy server, the `verify` value will be passed to the proxy's
> SSL context as well.

## Common errors
This section will document any user-related errors with information on how you may be able to resolve them.

### ApiFeaturePreviewUsageOnly
This error indicates you are trying to use an endpoint in public preview and have not set `preview=True` when
calling the endpoint. Before doing so, note that this endpoint is
in preview state and breaking changes may occur at any time.

During the first phase of an endpoint's lifecycle, it may be in `Public Preview`
state. This indicates that the endpoint is in development and is not intended for
production use. 

## Input should have timezone info

```python
# Example error
pydantic_core._pydantic_core.ValidationError: 1 validation error for Model
datetype
  Input should have timezone info [type=timezone_aware, input_value=datetime.datetime(2025, 2, 5, 20, 57, 57, 511182), input_type=datetime]
```

This error indicates that you are passing a `datetime` object without timezone information to an
endpoint that requires it. To resolve this error, you should pass in a `datetime` object with timezone
information. For example, you can use the `timezone` class in the `datetime` package:

```python
from datetime import datetime
from datetime import timezone

datetime_with_tz = datetime(2025, 2, 5, 20, 57, 57, 511182, tzinfo=timezone.utc)
```

<a id="apis-link"></a>
<a id="apis-v1-link"></a>
## Documentation for V1 API endpoints

Namespace | Resource | Operation | HTTP request |
------------ | ------------- | ------------- | ------------- |
**FederatedSources** | FederatedSource | [**list**](docs/v1/FederatedSources/FederatedSource.md#list) | **GET** /gotham/v1/federatedSources |
**Gaia** | Map | [**add_artifacts**](docs/v1/Gaia/Map.md#add_artifacts) | **POST** /gotham/v1/maps/{mapRid}/layers/artifacts |
**Gaia** | Map | [**add_enterprise_map_layers**](docs/v1/Gaia/Map.md#add_enterprise_map_layers) | **POST** /gotham/v1/maps/{mapRid}/layers/emls |
**Gaia** | Map | [**add_objects**](docs/v1/Gaia/Map.md#add_objects) | **POST** /gotham/v1/maps/{mapRid}/layers/objects |
**Gaia** | Map | [**export_kmz**](docs/v1/Gaia/Map.md#export_kmz) | **POST** /gotham/v1/maps/{mapId}/kmz |
**Gaia** | Map | [**load**](docs/v1/Gaia/Map.md#load) | **GET** /gotham/v1/maps/load/{mapGid} |
**Gaia** | Map | [**load_layers**](docs/v1/Gaia/Map.md#load_layers) | **PUT** /gotham/v1/maps/load/{mapGid}/layers |
**Gaia** | Map | [**render_symbol**](docs/v1/Gaia/Map.md#render_symbol) | **PUT** /gotham/v1/maps/rendering/symbol |
**Gaia** | Map | [**search**](docs/v1/Gaia/Map.md#search) | **GET** /gotham/v1/maps |
**Geotime** | Geotime | [**link_track_and_object**](docs/v1/Geotime/Geotime.md#link_track_and_object) | **POST** /gotham/v1/tracks/linkToObject |
**Geotime** | Geotime | [**link_tracks**](docs/v1/Geotime/Geotime.md#link_tracks) | **POST** /gotham/v1/tracks/linkTracks |
**Geotime** | Geotime | [**put_convolution_metadata**](docs/v1/Geotime/Geotime.md#put_convolution_metadata) | **PUT** /gotham/v1/convolution/metadata |
**Geotime** | Geotime | [**search_latest_observations**](docs/v1/Geotime/Geotime.md#search_latest_observations) | **POST** /gotham/v1/observations/latest/{observationSpecId}/search |
**Geotime** | Geotime | [**search_observation_histories**](docs/v1/Geotime/Geotime.md#search_observation_histories) | **POST** /gotham/v1/observations/history/{observationSpecId}/search |
**Geotime** | Geotime | [**unlink_track_and_object**](docs/v1/Geotime/Geotime.md#unlink_track_and_object) | **POST** /gotham/v1/tracks/unlinkFromObject |
**Geotime** | Geotime | [**unlink_tracks**](docs/v1/Geotime/Geotime.md#unlink_tracks) | **POST** /gotham/v1/tracks/unlinkTracks |
**Geotime** | Geotime | [**write_observations**](docs/v1/Geotime/Geotime.md#write_observations) | **POST** /gotham/v1/observations |
**Inbox** | Messages | [**send**](docs/v1/Inbox/Messages.md#send) | **POST** /gotham/v1/inbox/messages |
**MapRendering** | MapRendering | [**load_generic_symbol**](docs/v1/MapRendering/MapRendering.md#load_generic_symbol) | **GET** /gotham/v1/maprendering/symbols/generic/{id} |
**MapRendering** | MapRendering | [**load_resource_tile**](docs/v1/MapRendering/MapRendering.md#load_resource_tile) | **GET** /gotham/v1/maprendering/resources/tiles/{tileset}/{zoom}/{xCoordinate}/{yCoordinate} |
**MapRendering** | MapRendering | [**render_objects**](docs/v1/MapRendering/MapRendering.md#render_objects) | **PUT** /gotham/v1/maprendering/render |
**Media** | Media | [**get_media_content**](docs/v1/Media/Media.md#get_media_content) | **GET** /gotham/v1/media/{mediaRid}/content |
**Media** | Media | [**get_object_media**](docs/v1/Media/Media.md#get_object_media) | **GET** /gotham/v1/objects/{primaryKey}/media |
**TargetWorkbench** | HighPriorityTargetLists | [**create**](docs/v1/TargetWorkbench/HighPriorityTargetLists.md#create) | **POST** /gotham/v1/twb/highPriorityTargetList |
**TargetWorkbench** | HighPriorityTargetLists | [**get**](docs/v1/TargetWorkbench/HighPriorityTargetLists.md#get) | **GET** /gotham/v1/twb/highPriorityTargetList/{rid} |
**TargetWorkbench** | HighPriorityTargetLists | [**update**](docs/v1/TargetWorkbench/HighPriorityTargetLists.md#update) | **PUT** /gotham/v1/twb/highPriorityTargetList/{rid} |
**TargetWorkbench** | TargetBoards | [**create**](docs/v1/TargetWorkbench/TargetBoards.md#create) | **POST** /gotham/v1/twb/targetBoard |
**TargetWorkbench** | TargetBoards | [**delete**](docs/v1/TargetWorkbench/TargetBoards.md#delete) | **PUT** /gotham/v1/twb/targetBoard/{rid}/archive |
**TargetWorkbench** | TargetBoards | [**get**](docs/v1/TargetWorkbench/TargetBoards.md#get) | **GET** /gotham/v1/twb/targetBoard/{rid} |
**TargetWorkbench** | TargetBoards | [**load_target_pucks**](docs/v1/TargetWorkbench/TargetBoards.md#load_target_pucks) | **PUT** /gotham/v1/twb/board/{rid}/loadTargetPucks |
**TargetWorkbench** | TargetBoards | [**update**](docs/v1/TargetWorkbench/TargetBoards.md#update) | **PUT** /gotham/v1/twb/targetBoard/{rid} |
**TargetWorkbench** | TargetBoards | [**update_target_column**](docs/v1/TargetWorkbench/TargetBoards.md#update_target_column) | **PUT** /gotham/v1/twb/setTargetColumn/{targetRid} |
**TargetWorkbench** | Targets | [**create**](docs/v1/TargetWorkbench/Targets.md#create) | **POST** /gotham/v1/twb/target |
**TargetWorkbench** | Targets | [**create_intel**](docs/v1/TargetWorkbench/Targets.md#create_intel) | **PUT** /gotham/v1/twb/createTargetIntel/{rid} |
**TargetWorkbench** | Targets | [**delete**](docs/v1/TargetWorkbench/Targets.md#delete) | **PUT** /gotham/v1/twb/target/{rid}/archive |
**TargetWorkbench** | Targets | [**get**](docs/v1/TargetWorkbench/Targets.md#get) | **GET** /gotham/v1/twb/target/{rid} |
**TargetWorkbench** | Targets | [**remove_intel**](docs/v1/TargetWorkbench/Targets.md#remove_intel) | **PUT** /gotham/v1/twb/removeTargetIntel/{rid} |
**TargetWorkbench** | Targets | [**update**](docs/v1/TargetWorkbench/Targets.md#update) | **PUT** /gotham/v1/twb/target/{rid} |


<a id="models-link"></a>
<a id="models-v1-link"></a>
## Documentation for V1 models

Namespace | Name | Import |
--------- | ---- | ------ |
**Foundry** | [FoundryObjectPropertyTypeRid](docs/v1/Foundry/models/FoundryObjectPropertyTypeRid.md) | `from gotham.v1.foundry.models import FoundryObjectPropertyTypeRid` |
**Foundry** | [FoundryObjectSetRid](docs/v1/Foundry/models/FoundryObjectSetRid.md) | `from gotham.v1.foundry.models import FoundryObjectSetRid` |
**Foundry** | [FoundryObjectTypeRid](docs/v1/Foundry/models/FoundryObjectTypeRid.md) | `from gotham.v1.foundry.models import FoundryObjectTypeRid` |
**Gaia** | [AddArtifactsToMapResponse](docs/v1/Gaia/models/AddArtifactsToMapResponse.md) | `from gotham.v1.gaia.models import AddArtifactsToMapResponse` |
**Gaia** | [AddEnterpriseMapLayersToMapResponse](docs/v1/Gaia/models/AddEnterpriseMapLayersToMapResponse.md) | `from gotham.v1.gaia.models import AddEnterpriseMapLayersToMapResponse` |
**Gaia** | [AddObjectsToMapResponse](docs/v1/Gaia/models/AddObjectsToMapResponse.md) | `from gotham.v1.gaia.models import AddObjectsToMapResponse` |
**Gaia** | [EmlId](docs/v1/Gaia/models/EmlId.md) | `from gotham.v1.gaia.models import EmlId` |
**Gaia** | [FillStyle](docs/v1/Gaia/models/FillStyle.md) | `from gotham.v1.gaia.models import FillStyle` |
**Gaia** | [GaiaCoordinate](docs/v1/Gaia/models/GaiaCoordinate.md) | `from gotham.v1.gaia.models import GaiaCoordinate` |
**Gaia** | [GaiaElement](docs/v1/Gaia/models/GaiaElement.md) | `from gotham.v1.gaia.models import GaiaElement` |
**Gaia** | [GaiaElementId](docs/v1/Gaia/models/GaiaElementId.md) | `from gotham.v1.gaia.models import GaiaElementId` |
**Gaia** | [GaiaFeature](docs/v1/Gaia/models/GaiaFeature.md) | `from gotham.v1.gaia.models import GaiaFeature` |
**Gaia** | [GaiaLayer](docs/v1/Gaia/models/GaiaLayer.md) | `from gotham.v1.gaia.models import GaiaLayer` |
**Gaia** | [GaiaLayerId](docs/v1/Gaia/models/GaiaLayerId.md) | `from gotham.v1.gaia.models import GaiaLayerId` |
**Gaia** | [GaiaLayerMetadata](docs/v1/Gaia/models/GaiaLayerMetadata.md) | `from gotham.v1.gaia.models import GaiaLayerMetadata` |
**Gaia** | [GaiaMapGid](docs/v1/Gaia/models/GaiaMapGid.md) | `from gotham.v1.gaia.models import GaiaMapGid` |
**Gaia** | [GaiaMapId](docs/v1/Gaia/models/GaiaMapId.md) | `from gotham.v1.gaia.models import GaiaMapId` |
**Gaia** | [GaiaMapMetadata](docs/v1/Gaia/models/GaiaMapMetadata.md) | `from gotham.v1.gaia.models import GaiaMapMetadata` |
**Gaia** | [GaiaMapName](docs/v1/Gaia/models/GaiaMapName.md) | `from gotham.v1.gaia.models import GaiaMapName` |
**Gaia** | [GaiaMapRid](docs/v1/Gaia/models/GaiaMapRid.md) | `from gotham.v1.gaia.models import GaiaMapRid` |
**Gaia** | [GaiaProperties](docs/v1/Gaia/models/GaiaProperties.md) | `from gotham.v1.gaia.models import GaiaProperties` |
**Gaia** | [GaiaStyle](docs/v1/Gaia/models/GaiaStyle.md) | `from gotham.v1.gaia.models import GaiaStyle` |
**Gaia** | [GaiaSymbol](docs/v1/Gaia/models/GaiaSymbol.md) | `from gotham.v1.gaia.models import GaiaSymbol` |
**Gaia** | [IconFillStyle](docs/v1/Gaia/models/IconFillStyle.md) | `from gotham.v1.gaia.models import IconFillStyle` |
**Gaia** | [IconStrokeStyle](docs/v1/Gaia/models/IconStrokeStyle.md) | `from gotham.v1.gaia.models import IconStrokeStyle` |
**Gaia** | [IconSymbol](docs/v1/Gaia/models/IconSymbol.md) | `from gotham.v1.gaia.models import IconSymbol` |
**Gaia** | [LabelStyle](docs/v1/Gaia/models/LabelStyle.md) | `from gotham.v1.gaia.models import LabelStyle` |
**Gaia** | [LoadLayersResponse](docs/v1/Gaia/models/LoadLayersResponse.md) | `from gotham.v1.gaia.models import LoadLayersResponse` |
**Gaia** | [LoadMapResponse](docs/v1/Gaia/models/LoadMapResponse.md) | `from gotham.v1.gaia.models import LoadMapResponse` |
**Gaia** | [MilSymModifiers](docs/v1/Gaia/models/MilSymModifiers.md) | `from gotham.v1.gaia.models import MilSymModifiers` |
**Gaia** | [MilsymSymbol](docs/v1/Gaia/models/MilsymSymbol.md) | `from gotham.v1.gaia.models import MilsymSymbol` |
**Gaia** | [SearchMapsResponse](docs/v1/Gaia/models/SearchMapsResponse.md) | `from gotham.v1.gaia.models import SearchMapsResponse` |
**Gaia** | [StrokeStyle](docs/v1/Gaia/models/StrokeStyle.md) | `from gotham.v1.gaia.models import StrokeStyle` |
**Gaia** | [SymbolStyle](docs/v1/Gaia/models/SymbolStyle.md) | `from gotham.v1.gaia.models import SymbolStyle` |
**Gaia** | [TacticalGraphicProperties](docs/v1/Gaia/models/TacticalGraphicProperties.md) | `from gotham.v1.gaia.models import TacticalGraphicProperties` |
**Gaia** | [TextAlignment](docs/v1/Gaia/models/TextAlignment.md) | `from gotham.v1.gaia.models import TextAlignment` |
**Geotime** | [CollectionId](docs/v1/Geotime/models/CollectionId.md) | `from gotham.v1.geotime.models import CollectionId` |
**Geotime** | [ConvolvedComponentMetadata](docs/v1/Geotime/models/ConvolvedComponentMetadata.md) | `from gotham.v1.geotime.models import ConvolvedComponentMetadata` |
**Geotime** | [ConvolvedMetadata](docs/v1/Geotime/models/ConvolvedMetadata.md) | `from gotham.v1.geotime.models import ConvolvedMetadata` |
**Geotime** | [GeometryStyle](docs/v1/Geotime/models/GeometryStyle.md) | `from gotham.v1.geotime.models import GeometryStyle` |
**Geotime** | [IconSymbologyIdentifier](docs/v1/Geotime/models/IconSymbologyIdentifier.md) | `from gotham.v1.geotime.models import IconSymbologyIdentifier` |
**Geotime** | [InvalidObservation](docs/v1/Geotime/models/InvalidObservation.md) | `from gotham.v1.geotime.models import InvalidObservation` |
**Geotime** | [MilSymbologyIdentifier](docs/v1/Geotime/models/MilSymbologyIdentifier.md) | `from gotham.v1.geotime.models import MilSymbologyIdentifier` |
**Geotime** | [ObjectRid](docs/v1/Geotime/models/ObjectRid.md) | `from gotham.v1.geotime.models import ObjectRid` |
**Geotime** | [Observation](docs/v1/Geotime/models/Observation.md) | `from gotham.v1.geotime.models import Observation` |
**Geotime** | [ObservationField](docs/v1/Geotime/models/ObservationField.md) | `from gotham.v1.geotime.models import ObservationField` |
**Geotime** | [ObservationQuery](docs/v1/Geotime/models/ObservationQuery.md) | `from gotham.v1.geotime.models import ObservationQuery` |
**Geotime** | [ObservationSpecId](docs/v1/Geotime/models/ObservationSpecId.md) | `from gotham.v1.geotime.models import ObservationSpecId` |
**Geotime** | [ObservationStyle](docs/v1/Geotime/models/ObservationStyle.md) | `from gotham.v1.geotime.models import ObservationStyle` |
**Geotime** | [ObservationWithinQuery](docs/v1/Geotime/models/ObservationWithinQuery.md) | `from gotham.v1.geotime.models import ObservationWithinQuery` |
**Geotime** | [PropertyValuesQuery](docs/v1/Geotime/models/PropertyValuesQuery.md) | `from gotham.v1.geotime.models import PropertyValuesQuery` |
**Geotime** | [SearchLatestObservationsResponse](docs/v1/Geotime/models/SearchLatestObservationsResponse.md) | `from gotham.v1.geotime.models import SearchLatestObservationsResponse` |
**Geotime** | [SearchObservationHistoryResponse](docs/v1/Geotime/models/SearchObservationHistoryResponse.md) | `from gotham.v1.geotime.models import SearchObservationHistoryResponse` |
**Geotime** | [SourceSystemId](docs/v1/Geotime/models/SourceSystemId.md) | `from gotham.v1.geotime.models import SourceSystemId` |
**Geotime** | [SymbologyIdentifier](docs/v1/Geotime/models/SymbologyIdentifier.md) | `from gotham.v1.geotime.models import SymbologyIdentifier` |
**Geotime** | [TimeQuery](docs/v1/Geotime/models/TimeQuery.md) | `from gotham.v1.geotime.models import TimeQuery` |
**Geotime** | [Track](docs/v1/Geotime/models/Track.md) | `from gotham.v1.geotime.models import Track` |
**Geotime** | [TrackRid](docs/v1/Geotime/models/TrackRid.md) | `from gotham.v1.geotime.models import TrackRid` |
**Geotime** | [WriteObservationsRequest](docs/v1/Geotime/models/WriteObservationsRequest.md) | `from gotham.v1.geotime.models import WriteObservationsRequest` |
**Geotime** | [WriteObservationsResponse](docs/v1/Geotime/models/WriteObservationsResponse.md) | `from gotham.v1.geotime.models import WriteObservationsResponse` |
**Gotham** | [ArtifactGid](docs/v1/Gotham/models/ArtifactGid.md) | `from gotham.v1.gotham.models import ArtifactGid` |
**Gotham** | [ArtifactSecurity](docs/v1/Gotham/models/ArtifactSecurity.md) | `from gotham.v1.gotham.models import ArtifactSecurity` |
**Gotham** | [BBox](docs/v1/Gotham/models/BBox.md) | `from gotham.v1.gotham.models import BBox` |
**Gotham** | [ChatMessageId](docs/v1/Gotham/models/ChatMessageId.md) | `from gotham.v1.gotham.models import ChatMessageId` |
**Gotham** | [Coordinate](docs/v1/Gotham/models/Coordinate.md) | `from gotham.v1.gotham.models import Coordinate` |
**Gotham** | [CreateHighPriorityTargetListResponseV2](docs/v1/Gotham/models/CreateHighPriorityTargetListResponseV2.md) | `from gotham.v1.gotham.models import CreateHighPriorityTargetListResponseV2` |
**Gotham** | [CreateTargetBoardResponseV2](docs/v1/Gotham/models/CreateTargetBoardResponseV2.md) | `from gotham.v1.gotham.models import CreateTargetBoardResponseV2` |
**Gotham** | [CreateTargetResponseV2](docs/v1/Gotham/models/CreateTargetResponseV2.md) | `from gotham.v1.gotham.models import CreateTargetResponseV2` |
**Gotham** | [CustomTargetIdentifer](docs/v1/Gotham/models/CustomTargetIdentifer.md) | `from gotham.v1.gotham.models import CustomTargetIdentifer` |
**Gotham** | [ElevationWithError](docs/v1/Gotham/models/ElevationWithError.md) | `from gotham.v1.gotham.models import ElevationWithError` |
**Gotham** | [EmptySuccessResponse](docs/v1/Gotham/models/EmptySuccessResponse.md) | `from gotham.v1.gotham.models import EmptySuccessResponse` |
**Gotham** | [Feature](docs/v1/Gotham/models/Feature.md) | `from gotham.v1.gotham.models import Feature` |
**Gotham** | [FeatureCollection](docs/v1/Gotham/models/FeatureCollection.md) | `from gotham.v1.gotham.models import FeatureCollection` |
**Gotham** | [FeatureCollectionTypes](docs/v1/Gotham/models/FeatureCollectionTypes.md) | `from gotham.v1.gotham.models import FeatureCollectionTypes` |
**Gotham** | [FeaturePropertyKey](docs/v1/Gotham/models/FeaturePropertyKey.md) | `from gotham.v1.gotham.models import FeaturePropertyKey` |
**Gotham** | [FederatedAndQuery](docs/v1/Gotham/models/FederatedAndQuery.md) | `from gotham.v1.gotham.models import FederatedAndQuery` |
**Gotham** | [FederatedNotQuery](docs/v1/Gotham/models/FederatedNotQuery.md) | `from gotham.v1.gotham.models import FederatedNotQuery` |
**Gotham** | [FederatedOrQuery](docs/v1/Gotham/models/FederatedOrQuery.md) | `from gotham.v1.gotham.models import FederatedOrQuery` |
**Gotham** | [FederatedSearchJsonQuery](docs/v1/Gotham/models/FederatedSearchJsonQuery.md) | `from gotham.v1.gotham.models import FederatedSearchJsonQuery` |
**Gotham** | [FederatedSource](docs/v1/Gotham/models/FederatedSource.md) | `from gotham.v1.gotham.models import FederatedSource` |
**Gotham** | [FederatedSourceName](docs/v1/Gotham/models/FederatedSourceName.md) | `from gotham.v1.gotham.models import FederatedSourceName` |
**Gotham** | [FederatedTermQuery](docs/v1/Gotham/models/FederatedTermQuery.md) | `from gotham.v1.gotham.models import FederatedTermQuery` |
**Gotham** | [GeoCircle](docs/v1/Gotham/models/GeoCircle.md) | `from gotham.v1.gotham.models import GeoCircle` |
**Gotham** | [GeoJsonObject](docs/v1/Gotham/models/GeoJsonObject.md) | `from gotham.v1.gotham.models import GeoJsonObject` |
**Gotham** | [Geometry](docs/v1/Gotham/models/Geometry.md) | `from gotham.v1.gotham.models import Geometry` |
**Gotham** | [GeometryCollection](docs/v1/Gotham/models/GeometryCollection.md) | `from gotham.v1.gotham.models import GeometryCollection` |
**Gotham** | [GeoPoint](docs/v1/Gotham/models/GeoPoint.md) | `from gotham.v1.gotham.models import GeoPoint` |
**Gotham** | [GeoPolygon](docs/v1/Gotham/models/GeoPolygon.md) | `from gotham.v1.gotham.models import GeoPolygon` |
**Gotham** | [GeotimeSeriesExternalReference](docs/v1/Gotham/models/GeotimeSeriesExternalReference.md) | `from gotham.v1.gotham.models import GeotimeSeriesExternalReference` |
**Gotham** | [GeotimeTrackRid](docs/v1/Gotham/models/GeotimeTrackRid.md) | `from gotham.v1.gotham.models import GeotimeTrackRid` |
**Gotham** | [GetFederatedSourceResponse](docs/v1/Gotham/models/GetFederatedSourceResponse.md) | `from gotham.v1.gotham.models import GetFederatedSourceResponse` |
**Gotham** | [GetMediaResponse](docs/v1/Gotham/models/GetMediaResponse.md) | `from gotham.v1.gotham.models import GetMediaResponse` |
**Gotham** | [GroupName](docs/v1/Gotham/models/GroupName.md) | `from gotham.v1.gotham.models import GroupName` |
**Gotham** | [GroupRecipient](docs/v1/Gotham/models/GroupRecipient.md) | `from gotham.v1.gotham.models import GroupRecipient` |
**Gotham** | [HighPriorityTargetListAgm](docs/v1/Gotham/models/HighPriorityTargetListAgm.md) | `from gotham.v1.gotham.models import HighPriorityTargetListAgm` |
**Gotham** | [HighPriorityTargetListAgmId](docs/v1/Gotham/models/HighPriorityTargetListAgmId.md) | `from gotham.v1.gotham.models import HighPriorityTargetListAgmId` |
**Gotham** | [HighPriorityTargetListEffectType](docs/v1/Gotham/models/HighPriorityTargetListEffectType.md) | `from gotham.v1.gotham.models import HighPriorityTargetListEffectType` |
**Gotham** | [HighPriorityTargetListRid](docs/v1/Gotham/models/HighPriorityTargetListRid.md) | `from gotham.v1.gotham.models import HighPriorityTargetListRid` |
**Gotham** | [HighPriorityTargetListTargetId](docs/v1/Gotham/models/HighPriorityTargetListTargetId.md) | `from gotham.v1.gotham.models import HighPriorityTargetListTargetId` |
**Gotham** | [HighPriorityTargetListTargetV2](docs/v1/Gotham/models/HighPriorityTargetListTargetV2.md) | `from gotham.v1.gotham.models import HighPriorityTargetListTargetV2` |
**Gotham** | [HighPriorityTargetListV2](docs/v1/Gotham/models/HighPriorityTargetListV2.md) | `from gotham.v1.gotham.models import HighPriorityTargetListV2` |
**Gotham** | [HighPriorityTargetListWhen](docs/v1/Gotham/models/HighPriorityTargetListWhen.md) | `from gotham.v1.gotham.models import HighPriorityTargetListWhen` |
**Gotham** | [HptlTargetAoi](docs/v1/Gotham/models/HptlTargetAoi.md) | `from gotham.v1.gotham.models import HptlTargetAoi` |
**Gotham** | [HptlTargetAoiId](docs/v1/Gotham/models/HptlTargetAoiId.md) | `from gotham.v1.gotham.models import HptlTargetAoiId` |
**Gotham** | [HptlTargetAoiUnion](docs/v1/Gotham/models/HptlTargetAoiUnion.md) | `from gotham.v1.gotham.models import HptlTargetAoiUnion` |
**Gotham** | [HptlTargetElnot](docs/v1/Gotham/models/HptlTargetElnot.md) | `from gotham.v1.gotham.models import HptlTargetElnot` |
**Gotham** | [HptlTargetEntityAoi](docs/v1/Gotham/models/HptlTargetEntityAoi.md) | `from gotham.v1.gotham.models import HptlTargetEntityAoi` |
**Gotham** | [HptlTargetGeoAoi](docs/v1/Gotham/models/HptlTargetGeoAoi.md) | `from gotham.v1.gotham.models import HptlTargetGeoAoi` |
**Gotham** | [HptlTargetSubtype](docs/v1/Gotham/models/HptlTargetSubtype.md) | `from gotham.v1.gotham.models import HptlTargetSubtype` |
**Gotham** | [IntelChatMessage](docs/v1/Gotham/models/IntelChatMessage.md) | `from gotham.v1.gotham.models import IntelChatMessage` |
**Gotham** | [IntelDomain](docs/v1/Gotham/models/IntelDomain.md) | `from gotham.v1.gotham.models import IntelDomain` |
**Gotham** | [IntelDossier](docs/v1/Gotham/models/IntelDossier.md) | `from gotham.v1.gotham.models import IntelDossier` |
**Gotham** | [IntelFoundryObject](docs/v1/Gotham/models/IntelFoundryObject.md) | `from gotham.v1.gotham.models import IntelFoundryObject` |
**Gotham** | [IntelFreeText](docs/v1/Gotham/models/IntelFreeText.md) | `from gotham.v1.gotham.models import IntelFreeText` |
**Gotham** | [IntelGeotimeObservation](docs/v1/Gotham/models/IntelGeotimeObservation.md) | `from gotham.v1.gotham.models import IntelGeotimeObservation` |
**Gotham** | [IntelId](docs/v1/Gotham/models/IntelId.md) | `from gotham.v1.gotham.models import IntelId` |
**Gotham** | [IntelMedia](docs/v1/Gotham/models/IntelMedia.md) | `from gotham.v1.gotham.models import IntelMedia` |
**Gotham** | [IntelPgObject](docs/v1/Gotham/models/IntelPgObject.md) | `from gotham.v1.gotham.models import IntelPgObject` |
**Gotham** | [IntelUnion](docs/v1/Gotham/models/IntelUnion.md) | `from gotham.v1.gotham.models import IntelUnion` |
**Gotham** | [JpdiId](docs/v1/Gotham/models/JpdiId.md) | `from gotham.v1.gotham.models import JpdiId` |
**Gotham** | [LinearRing](docs/v1/Gotham/models/LinearRing.md) | `from gotham.v1.gotham.models import LinearRing` |
**Gotham** | [LineString](docs/v1/Gotham/models/LineString.md) | `from gotham.v1.gotham.models import LineString` |
**Gotham** | [LineStringCoordinates](docs/v1/Gotham/models/LineStringCoordinates.md) | `from gotham.v1.gotham.models import LineStringCoordinates` |
**Gotham** | [LinkTypeApiName](docs/v1/Gotham/models/LinkTypeApiName.md) | `from gotham.v1.gotham.models import LinkTypeApiName` |
**Gotham** | [LoadHighPriorityTargetListResponseV2](docs/v1/Gotham/models/LoadHighPriorityTargetListResponseV2.md) | `from gotham.v1.gotham.models import LoadHighPriorityTargetListResponseV2` |
**Gotham** | [LoadTargetBoardResponseV2](docs/v1/Gotham/models/LoadTargetBoardResponseV2.md) | `from gotham.v1.gotham.models import LoadTargetBoardResponseV2` |
**Gotham** | [LoadTargetPuckResponse](docs/v1/Gotham/models/LoadTargetPuckResponse.md) | `from gotham.v1.gotham.models import LoadTargetPuckResponse` |
**Gotham** | [LoadTargetPucksResponse](docs/v1/Gotham/models/LoadTargetPucksResponse.md) | `from gotham.v1.gotham.models import LoadTargetPucksResponse` |
**Gotham** | [LoadTargetResponseV2](docs/v1/Gotham/models/LoadTargetResponseV2.md) | `from gotham.v1.gotham.models import LoadTargetResponseV2` |
**Gotham** | [Location3dWithError](docs/v1/Gotham/models/Location3dWithError.md) | `from gotham.v1.gotham.models import Location3dWithError` |
**Gotham** | [LocationSource](docs/v1/Gotham/models/LocationSource.md) | `from gotham.v1.gotham.models import LocationSource` |
**Gotham** | [Media](docs/v1/Gotham/models/Media.md) | `from gotham.v1.gotham.models import Media` |
**Gotham** | [MediaRid](docs/v1/Gotham/models/MediaRid.md) | `from gotham.v1.gotham.models import MediaRid` |
**Gotham** | [MediaType](docs/v1/Gotham/models/MediaType.md) | `from gotham.v1.gotham.models import MediaType` |
**Gotham** | [MensurationData](docs/v1/Gotham/models/MensurationData.md) | `from gotham.v1.gotham.models import MensurationData` |
**Gotham** | [MessageSecurity](docs/v1/Gotham/models/MessageSecurity.md) | `from gotham.v1.gotham.models import MessageSecurity` |
**Gotham** | [MessageSender](docs/v1/Gotham/models/MessageSender.md) | `from gotham.v1.gotham.models import MessageSender` |
**Gotham** | [MessageSourceId](docs/v1/Gotham/models/MessageSourceId.md) | `from gotham.v1.gotham.models import MessageSourceId` |
**Gotham** | [MultiLineString](docs/v1/Gotham/models/MultiLineString.md) | `from gotham.v1.gotham.models import MultiLineString` |
**Gotham** | [MultiPoint](docs/v1/Gotham/models/MultiPoint.md) | `from gotham.v1.gotham.models import MultiPoint` |
**Gotham** | [MultiPolygon](docs/v1/Gotham/models/MultiPolygon.md) | `from gotham.v1.gotham.models import MultiPolygon` |
**Gotham** | [Namespace](docs/v1/Gotham/models/Namespace.md) | `from gotham.v1.gotham.models import Namespace` |
**Gotham** | [NamespaceName](docs/v1/Gotham/models/NamespaceName.md) | `from gotham.v1.gotham.models import NamespaceName` |
**Gotham** | [ObjectComponentSecurity](docs/v1/Gotham/models/ObjectComponentSecurity.md) | `from gotham.v1.gotham.models import ObjectComponentSecurity` |
**Gotham** | [ObjectPrimaryKey](docs/v1/Gotham/models/ObjectPrimaryKey.md) | `from gotham.v1.gotham.models import ObjectPrimaryKey` |
**Gotham** | [ObjectTypeApiName](docs/v1/Gotham/models/ObjectTypeApiName.md) | `from gotham.v1.gotham.models import ObjectTypeApiName` |
**Gotham** | [PageSize](docs/v1/Gotham/models/PageSize.md) | `from gotham.v1.gotham.models import PageSize` |
**Gotham** | [PageToken](docs/v1/Gotham/models/PageToken.md) | `from gotham.v1.gotham.models import PageToken` |
**Gotham** | [Permission](docs/v1/Gotham/models/Permission.md) | `from gotham.v1.gotham.models import Permission` |
**Gotham** | [PermissionItem](docs/v1/Gotham/models/PermissionItem.md) | `from gotham.v1.gotham.models import PermissionItem` |
**Gotham** | [Point](docs/v1/Gotham/models/Point.md) | `from gotham.v1.gotham.models import Point` |
**Gotham** | [Polygon](docs/v1/Gotham/models/Polygon.md) | `from gotham.v1.gotham.models import Polygon` |
**Gotham** | [PortionMarking](docs/v1/Gotham/models/PortionMarking.md) | `from gotham.v1.gotham.models import PortionMarking` |
**Gotham** | [Position](docs/v1/Gotham/models/Position.md) | `from gotham.v1.gotham.models import Position` |
**Gotham** | [PreviewMode](docs/v1/Gotham/models/PreviewMode.md) | `from gotham.v1.gotham.models import PreviewMode` |
**Gotham** | [PropertyApiName](docs/v1/Gotham/models/PropertyApiName.md) | `from gotham.v1.gotham.models import PropertyApiName` |
**Gotham** | [PropertyId](docs/v1/Gotham/models/PropertyId.md) | `from gotham.v1.gotham.models import PropertyId` |
**Gotham** | [PropertyValue](docs/v1/Gotham/models/PropertyValue.md) | `from gotham.v1.gotham.models import PropertyValue` |
**Gotham** | [SecureTextBody](docs/v1/Gotham/models/SecureTextBody.md) | `from gotham.v1.gotham.models import SecureTextBody` |
**Gotham** | [SecureTextTitle](docs/v1/Gotham/models/SecureTextTitle.md) | `from gotham.v1.gotham.models import SecureTextTitle` |
**Gotham** | [SecurityKey](docs/v1/Gotham/models/SecurityKey.md) | `from gotham.v1.gotham.models import SecurityKey` |
**Gotham** | [SendMessageFailure](docs/v1/Gotham/models/SendMessageFailure.md) | `from gotham.v1.gotham.models import SendMessageFailure` |
**Gotham** | [SendMessageFailureReason](docs/v1/Gotham/models/SendMessageFailureReason.md) | `from gotham.v1.gotham.models import SendMessageFailureReason` |
**Gotham** | [SendMessageRequest](docs/v1/Gotham/models/SendMessageRequest.md) | `from gotham.v1.gotham.models import SendMessageRequest` |
**Gotham** | [SendMessageResponse](docs/v1/Gotham/models/SendMessageResponse.md) | `from gotham.v1.gotham.models import SendMessageResponse` |
**Gotham** | [SendMessagesResponse](docs/v1/Gotham/models/SendMessagesResponse.md) | `from gotham.v1.gotham.models import SendMessagesResponse` |
**Gotham** | [ServiceName](docs/v1/Gotham/models/ServiceName.md) | `from gotham.v1.gotham.models import ServiceName` |
**Gotham** | [SizeBytes](docs/v1/Gotham/models/SizeBytes.md) | `from gotham.v1.gotham.models import SizeBytes` |
**Gotham** | [TargetAimpointId](docs/v1/Gotham/models/TargetAimpointId.md) | `from gotham.v1.gotham.models import TargetAimpointId` |
**Gotham** | [TargetAimpointV2](docs/v1/Gotham/models/TargetAimpointV2.md) | `from gotham.v1.gotham.models import TargetAimpointV2` |
**Gotham** | [TargetBoard](docs/v1/Gotham/models/TargetBoard.md) | `from gotham.v1.gotham.models import TargetBoard` |
**Gotham** | [TargetBoardColumnConfiguration](docs/v1/Gotham/models/TargetBoardColumnConfiguration.md) | `from gotham.v1.gotham.models import TargetBoardColumnConfiguration` |
**Gotham** | [TargetBoardColumnConfigurationId](docs/v1/Gotham/models/TargetBoardColumnConfigurationId.md) | `from gotham.v1.gotham.models import TargetBoardColumnConfigurationId` |
**Gotham** | [TargetBoardColumnId](docs/v1/Gotham/models/TargetBoardColumnId.md) | `from gotham.v1.gotham.models import TargetBoardColumnId` |
**Gotham** | [TargetBoardConfiguration](docs/v1/Gotham/models/TargetBoardConfiguration.md) | `from gotham.v1.gotham.models import TargetBoardConfiguration` |
**Gotham** | [TargetBoardRid](docs/v1/Gotham/models/TargetBoardRid.md) | `from gotham.v1.gotham.models import TargetBoardRid` |
**Gotham** | [TargetBranchId](docs/v1/Gotham/models/TargetBranchId.md) | `from gotham.v1.gotham.models import TargetBranchId` |
**Gotham** | [TargetDetails](docs/v1/Gotham/models/TargetDetails.md) | `from gotham.v1.gotham.models import TargetDetails` |
**Gotham** | [TargetIdentifier](docs/v1/Gotham/models/TargetIdentifier.md) | `from gotham.v1.gotham.models import TargetIdentifier` |
**Gotham** | [TargetIdentifierEnum](docs/v1/Gotham/models/TargetIdentifierEnum.md) | `from gotham.v1.gotham.models import TargetIdentifierEnum` |
**Gotham** | [TargetLocation](docs/v1/Gotham/models/TargetLocation.md) | `from gotham.v1.gotham.models import TargetLocation` |
**Gotham** | [TargetObservation](docs/v1/Gotham/models/TargetObservation.md) | `from gotham.v1.gotham.models import TargetObservation` |
**Gotham** | [TargetPuckId](docs/v1/Gotham/models/TargetPuckId.md) | `from gotham.v1.gotham.models import TargetPuckId` |
**Gotham** | [TargetPuckLoadLevel](docs/v1/Gotham/models/TargetPuckLoadLevel.md) | `from gotham.v1.gotham.models import TargetPuckLoadLevel` |
**Gotham** | [TargetPuckStatus](docs/v1/Gotham/models/TargetPuckStatus.md) | `from gotham.v1.gotham.models import TargetPuckStatus` |
**Gotham** | [TargetRid](docs/v1/Gotham/models/TargetRid.md) | `from gotham.v1.gotham.models import TargetRid` |
**Gotham** | [TargetV2](docs/v1/Gotham/models/TargetV2.md) | `from gotham.v1.gotham.models import TargetV2` |
**Gotham** | [TextFormatStyle](docs/v1/Gotham/models/TextFormatStyle.md) | `from gotham.v1.gotham.models import TextFormatStyle` |
**MapRendering** | [ClientCapabilities](docs/v1/MapRendering/models/ClientCapabilities.md) | `from gotham.v1.map_rendering.models import ClientCapabilities` |
**MapRendering** | [FoundryObjectPropertyValueUntyped](docs/v1/MapRendering/models/FoundryObjectPropertyValueUntyped.md) | `from gotham.v1.map_rendering.models import FoundryObjectPropertyValueUntyped` |
**MapRendering** | [GeometryRenderableContent](docs/v1/MapRendering/models/GeometryRenderableContent.md) | `from gotham.v1.map_rendering.models import GeometryRenderableContent` |
**MapRendering** | [Invocation](docs/v1/MapRendering/models/Invocation.md) | `from gotham.v1.map_rendering.models import Invocation` |
**MapRendering** | [InvocationId](docs/v1/MapRendering/models/InvocationId.md) | `from gotham.v1.map_rendering.models import InvocationId` |
**MapRendering** | [MrsAlpha](docs/v1/MapRendering/models/MrsAlpha.md) | `from gotham.v1.map_rendering.models import MrsAlpha` |
**MapRendering** | [MrsColor](docs/v1/MapRendering/models/MrsColor.md) | `from gotham.v1.map_rendering.models import MrsColor` |
**MapRendering** | [MrsFillStyle](docs/v1/MapRendering/models/MrsFillStyle.md) | `from gotham.v1.map_rendering.models import MrsFillStyle` |
**MapRendering** | [MrsGenericSymbol](docs/v1/MapRendering/models/MrsGenericSymbol.md) | `from gotham.v1.map_rendering.models import MrsGenericSymbol` |
**MapRendering** | [MrsGenericSymbolId](docs/v1/MapRendering/models/MrsGenericSymbolId.md) | `from gotham.v1.map_rendering.models import MrsGenericSymbolId` |
**MapRendering** | [MrsGeometryStyle](docs/v1/MapRendering/models/MrsGeometryStyle.md) | `from gotham.v1.map_rendering.models import MrsGeometryStyle` |
**MapRendering** | [MrsLabelStyle](docs/v1/MapRendering/models/MrsLabelStyle.md) | `from gotham.v1.map_rendering.models import MrsLabelStyle` |
**MapRendering** | [MrsRasterStyle](docs/v1/MapRendering/models/MrsRasterStyle.md) | `from gotham.v1.map_rendering.models import MrsRasterStyle` |
**MapRendering** | [MrsRgb](docs/v1/MapRendering/models/MrsRgb.md) | `from gotham.v1.map_rendering.models import MrsRgb` |
**MapRendering** | [MrsStrokeStyle](docs/v1/MapRendering/models/MrsStrokeStyle.md) | `from gotham.v1.map_rendering.models import MrsStrokeStyle` |
**MapRendering** | [MrsSymbol](docs/v1/MapRendering/models/MrsSymbol.md) | `from gotham.v1.map_rendering.models import MrsSymbol` |
**MapRendering** | [MrsSymbolStyle](docs/v1/MapRendering/models/MrsSymbolStyle.md) | `from gotham.v1.map_rendering.models import MrsSymbolStyle` |
**MapRendering** | [MrsVirtualPixels](docs/v1/MapRendering/models/MrsVirtualPixels.md) | `from gotham.v1.map_rendering.models import MrsVirtualPixels` |
**MapRendering** | [ObjectSourcingContent](docs/v1/MapRendering/models/ObjectSourcingContent.md) | `from gotham.v1.map_rendering.models import ObjectSourcingContent` |
**MapRendering** | [ObjectsReference](docs/v1/MapRendering/models/ObjectsReference.md) | `from gotham.v1.map_rendering.models import ObjectsReference` |
**MapRendering** | [ObjectsReferenceObjectSet](docs/v1/MapRendering/models/ObjectsReferenceObjectSet.md) | `from gotham.v1.map_rendering.models import ObjectsReferenceObjectSet` |
**MapRendering** | [RasterTilesRenderableContent](docs/v1/MapRendering/models/RasterTilesRenderableContent.md) | `from gotham.v1.map_rendering.models import RasterTilesRenderableContent` |
**MapRendering** | [Renderable](docs/v1/MapRendering/models/Renderable.md) | `from gotham.v1.map_rendering.models import Renderable` |
**MapRendering** | [RenderableContent](docs/v1/MapRendering/models/RenderableContent.md) | `from gotham.v1.map_rendering.models import RenderableContent` |
**MapRendering** | [RenderableContentType](docs/v1/MapRendering/models/RenderableContentType.md) | `from gotham.v1.map_rendering.models import RenderableContentType` |
**MapRendering** | [RenderableId](docs/v1/MapRendering/models/RenderableId.md) | `from gotham.v1.map_rendering.models import RenderableId` |
**MapRendering** | [RenderablePartId](docs/v1/MapRendering/models/RenderablePartId.md) | `from gotham.v1.map_rendering.models import RenderablePartId` |
**MapRendering** | [RendererReference](docs/v1/MapRendering/models/RendererReference.md) | `from gotham.v1.map_rendering.models import RendererReference` |
**MapRendering** | [RenderObjectsResponse](docs/v1/MapRendering/models/RenderObjectsResponse.md) | `from gotham.v1.map_rendering.models import RenderObjectsResponse` |
**MapRendering** | [Sourcing](docs/v1/MapRendering/models/Sourcing.md) | `from gotham.v1.map_rendering.models import Sourcing` |
**MapRendering** | [SourcingContent](docs/v1/MapRendering/models/SourcingContent.md) | `from gotham.v1.map_rendering.models import SourcingContent` |
**MapRendering** | [SourcingId](docs/v1/MapRendering/models/SourcingId.md) | `from gotham.v1.map_rendering.models import SourcingId` |
**MapRendering** | [StandardRendererReference](docs/v1/MapRendering/models/StandardRendererReference.md) | `from gotham.v1.map_rendering.models import StandardRendererReference` |
**MapRendering** | [TilesetId](docs/v1/MapRendering/models/TilesetId.md) | `from gotham.v1.map_rendering.models import TilesetId` |


<a id="all-errors"></a>
## Documentation for errors
<a id="errors-v1-link"></a>
## Documentation for V1 errors

Namespace | Name | Import |
--------- | ---- | ------ |
**Gotham** | ApiFeaturePreviewUsageOnly | `from gotham.v1.gotham.errors import ApiFeaturePreviewUsageOnly` |
**Gotham** | BasicLinkTypeNotFound | `from gotham.v1.gotham.errors import BasicLinkTypeNotFound` |
**Gotham** | DisallowedPropertyTypes | `from gotham.v1.gotham.errors import DisallowedPropertyTypes` |
**Gotham** | FederatedObjectUpdateNotAllowed | `from gotham.v1.gotham.errors import FederatedObjectUpdateNotAllowed` |
**Gotham** | FederatedSourceNotFound | `from gotham.v1.gotham.errors import FederatedSourceNotFound` |
**Gotham** | InvalidClassificationPortionMarkings | `from gotham.v1.gotham.errors import InvalidClassificationPortionMarkings` |
**Gotham** | InvalidGeotimeObservations | `from gotham.v1.gotham.errors import InvalidGeotimeObservations` |
**Gotham** | InvalidMessagePortionMarkings | `from gotham.v1.gotham.errors import InvalidMessagePortionMarkings` |
**Gotham** | InvalidMessageRequests | `from gotham.v1.gotham.errors import InvalidMessageRequests` |
**Gotham** | InvalidObjectRid | `from gotham.v1.gotham.errors import InvalidObjectRid` |
**Gotham** | InvalidOntologyTypes | `from gotham.v1.gotham.errors import InvalidOntologyTypes` |
**Gotham** | InvalidPageSize | `from gotham.v1.gotham.errors import InvalidPageSize` |
**Gotham** | InvalidPageToken | `from gotham.v1.gotham.errors import InvalidPageToken` |
**Gotham** | InvalidPermissions | `from gotham.v1.gotham.errors import InvalidPermissions` |
**Gotham** | InvalidPropertyValue | `from gotham.v1.gotham.errors import InvalidPropertyValue` |
**Gotham** | InvalidSidc | `from gotham.v1.gotham.errors import InvalidSidc` |
**Gotham** | InvalidTrackRid | `from gotham.v1.gotham.errors import InvalidTrackRid` |
**Gotham** | MalformedObjectPrimaryKeys | `from gotham.v1.gotham.errors import MalformedObjectPrimaryKeys` |
**Gotham** | MalformedPropertyFilters | `from gotham.v1.gotham.errors import MalformedPropertyFilters` |
**Gotham** | MalformedUnresolveRequest | `from gotham.v1.gotham.errors import MalformedUnresolveRequest` |
**Gotham** | MediaNotFound | `from gotham.v1.gotham.errors import MediaNotFound` |
**Gotham** | MissingRepresentativePropertyTypes | `from gotham.v1.gotham.errors import MissingRepresentativePropertyTypes` |
**Gotham** | NamespaceNotFound | `from gotham.v1.gotham.errors import NamespaceNotFound` |
**Gotham** | NoLocatorFoundForRid | `from gotham.v1.gotham.errors import NoLocatorFoundForRid` |
**Gotham** | ObjectNotFound | `from gotham.v1.gotham.errors import ObjectNotFound` |
**Gotham** | ObjectTypeNotFound | `from gotham.v1.gotham.errors import ObjectTypeNotFound` |
**Gotham** | PropertiesNotFound | `from gotham.v1.gotham.errors import PropertiesNotFound` |
**Gotham** | PropertyNotFound | `from gotham.v1.gotham.errors import PropertyNotFound` |
**Gotham** | PutConvolutionMetadataError | `from gotham.v1.gotham.errors import PutConvolutionMetadataError` |
**Gotham** | ResolvedObjectComponentsNotFound | `from gotham.v1.gotham.errors import ResolvedObjectComponentsNotFound` |
**Gotham** | ServiceNotConfigured | `from gotham.v1.gotham.errors import ServiceNotConfigured` |
**Gotham** | TargetNotOnTargetBoard | `from gotham.v1.gotham.errors import TargetNotOnTargetBoard` |
**Gotham** | TrackToObjectLinkageFailure | `from gotham.v1.gotham.errors import TrackToObjectLinkageFailure` |
**Gotham** | TrackToObjectUnlinkageFailure | `from gotham.v1.gotham.errors import TrackToObjectUnlinkageFailure` |
**Gotham** | TrackToTrackLinkageFailure | `from gotham.v1.gotham.errors import TrackToTrackLinkageFailure` |
**Gotham** | TrackToTrackUnlinkageFailure | `from gotham.v1.gotham.errors import TrackToTrackUnlinkageFailure` |
**Gotham** | UnclearGeotimeSeriesReference | `from gotham.v1.gotham.errors import UnclearGeotimeSeriesReference` |
**Gotham** | UnclearMultiSourcePropertyUpdateRequest | `from gotham.v1.gotham.errors import UnclearMultiSourcePropertyUpdateRequest` |
**Gotham** | UnknownRecipients | `from gotham.v1.gotham.errors import UnknownRecipients` |
**Gotham** | UserHasNoOwnerPerms | `from gotham.v1.gotham.errors import UserHasNoOwnerPerms` |
**Gotham** | WriteGeotimeObservationSizeLimit | `from gotham.v1.gotham.errors import WriteGeotimeObservationSizeLimit` |


## Contributions

This repository does not accept code contributions.

If you have any questions, concerns, or ideas for improvements, create an
issue with Palantir Support.

## License
This project is made available under the [Apache 2.0 License](/LICENSE).
