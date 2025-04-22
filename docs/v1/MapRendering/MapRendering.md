# MapRendering

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**load_generic_symbol**](#load_generic_symbol) | **GET** /gotham/v1/maprendering/symbols/generic/{id} | Stable |
[**load_resource_tile**](#load_resource_tile) | **GET** /gotham/v1/maprendering/resources/tiles/{tileset}/{zoom}/{xCoordinate}/{yCoordinate} | Stable |
[**render_objects**](#render_objects) | **PUT** /gotham/v1/maprendering/render | Stable |

# **load_generic_symbol**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Loads a PNG format icon with the provided ID, resizing it if requested.
This endpoint has the following features that make it more easily usable from browsers:
- Respects the If-None-Match etag header, returning 304 if the icon is unchanged.
- Will use a PALANTIR_TOKEN cookie if no authorization header was provided.
- Returns Cache-Control and Content-Type headers.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**id** | MrsGenericSymbolId | The generic symbol ID returned by the service that uniquely identifies a symbol.  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |
**size** | Optional[int] | Resize the icon so that its reference size matches this value. The actually returned image may be larger or smaller than this value.  | [optional] |

### Return type
**bytes**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MrsGenericSymbolId | The generic symbol ID returned by the service that uniquely identifies a symbol.
id = "ePkllYLiI7HHUFwC7Gyk5haAZvwB3ioZ3w"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True
# Optional[int] | Resize the icon so that its reference size matches this value. The actually returned image may be larger or smaller than this value.
size = "15"


try:
    api_response = client.map_rendering.MapRendering.load_generic_symbol(
        id, preview=preview, size=size
    )
    print("The load_generic_symbol response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling MapRendering.load_generic_symbol: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | A successful render response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **load_resource_tile**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Loads a tile from the provided tileset at the provided coordinates.
This endpoint has the following features that make it more easily usable from browsers:
- Respects the If-None-Match etag header, returning 304 if the tile is unchanged.
- Will use a PALANTIR_TOKEN cookie if no authorization header was provided.
- Returns Cache-Control and Content-Type headers.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**tileset** | TilesetId |  |  |
**zoom** | int |  |  |
**x_coordinate** | int |  |  |
**y_coordinate** | int |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**bytes**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TilesetId
tileset = "ePkllYLiQ1gYmJuZY2RqZOpbmlOSGQBa6OM8EVPoV3diXjKw8wHmFf_4ocnooKkmyV9fX--myeCgJKbAKKIUzfYTLK4s5Q8UtwaJiwdzyooaeEDElUz1YeLCwjzMkvHKEHE5GXGYOaK1hTGx9lBxeX57mHrJ9GpuRX4uiLgsO8jeQJC4NKNEiaic-8-f7YlVmbmlJRnFP352gJaJAV2bCmR3AtsaZZB2LVAiNz8F2M5NLSr-9bu9uDI3KT_HM8XP3cNd193HTRcCIn7_BgA0xGLI"
# int
zoom = None
# int
x_coordinate = None
# int
y_coordinate = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.map_rendering.MapRendering.load_resource_tile(
        tileset, zoom, x_coordinate, y_coordinate, preview=preview
    )
    print("The load_resource_tile response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling MapRendering.load_resource_tile: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | A successful render response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **render_objects**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Stateless api to fetch a snapshot of renderables for a given object set. Only includes initial renderable values
in snapshot, does not reflect changes made while rendering.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**capabilities** | ClientCapabilities |  |  |
**invocations** | List[Invocation] |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**RenderObjectsResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ClientCapabilities
capabilities = {"supportedRenderableContent": ["GEOMETRY"]}
# List[Invocation]
invocations = [
    {
        "id": "InvocationOne",
        "sourcingOnly": False,
        "objects": {
            "type": "objectSet",
            "objectSetRid": "ri.object-set.main.object-set.5958b23c-88f7-4f0e-a844-c3027f93705d",
        },
        "renderer": {"type": "standard"},
    },
    {
        "id": "InvocationTwo",
        "objects": {
            "type": "objectSet",
            "objectSetRid": "ri.object-set.main.object-set.6bdee6b7-c501-47bc-8e34-dba162dfa505",
        },
        "renderer": {"type": "standard"},
    },
]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.map_rendering.MapRendering.render_objects(
        capabilities=capabilities, invocations=invocations, preview=preview
    )
    print("The render_objects response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling MapRendering.render_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | RenderObjectsResponse  | A successful load layers response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

