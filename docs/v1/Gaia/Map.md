# Map

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**add_artifacts**](#add_artifacts) | **POST** /gotham/v1/maps/{mapRid}/layers/artifacts | Stable |
[**add_enterprise_map_layers**](#add_enterprise_map_layers) | **POST** /gotham/v1/maps/{mapRid}/layers/emls | Stable |
[**add_objects**](#add_objects) | **POST** /gotham/v1/maps/{mapRid}/layers/objects | Stable |
[**export_kmz**](#export_kmz) | **POST** /gotham/v1/maps/{mapId}/kmz | Stable |
[**load**](#load) | **GET** /gotham/v1/maps/load/{mapGid} | Stable |
[**load_layers**](#load_layers) | **PUT** /gotham/v1/maps/load/{mapGid}/layers | Stable |
[**render_symbol**](#render_symbol) | **PUT** /gotham/v1/maps/rendering/symbol | Stable |
[**search**](#search) | **GET** /gotham/v1/maps | Stable |

# **add_artifacts**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Add artifacts to a map. Currently only target collection artifacts may be added. If unknown artifacts
or artifacts that don't satisfy the security requirements are provided, the entire request will fail.
For each request, a new layer is created for each artifact, thus not idempotent.
Returns the IDs of the layers created.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_rid** | GaiaMapRid | The RID of the Gaia map that you wish to add artifacts to.  |  |
**artifact_gids** | List[ArtifactGid] | The GIDs of the artifacts to be added to the map.  |  |
**label** | str | The name of the layer to be created  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**AddArtifactsToMapResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapRid | The RID of the Gaia map that you wish to add artifacts to.
map_rid = "ri.gaia..map.a1A2bcD3e45fg6h7ij"
# List[ArtifactGid] | The GIDs of the artifacts to be added to the map.
artifact_gids = ["ri.gotham-artifact.instance.service-type.a1A2bcD3e45fg6h7ij"]
# str | The name of the layer to be created
label = "Example layer name."
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.add_artifacts(
        map_rid, artifact_gids=artifact_gids, label=label, preview=preview
    )
    print("The add_artifacts response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.add_artifacts: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AddArtifactsToMapResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **add_enterprise_map_layers**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Add enterprise map layers to a map. If unknown enterprise map layers or enterprise map layers that don't 
satisfy the security requirements are provided, the entire request will fail. For each request, a new layer 
is created for each enterprise map layer provided, thus not idempotent.
Returns the IDs of the layers created.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_rid** | GaiaMapRid | The RID of the Gaia map that you wish to add objects to.  |  |
**eml_ids** | List[EmlId] | The IDs of the enterprise map layers to be added to the map.  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**AddEnterpriseMapLayersToMapResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapRid | The RID of the Gaia map that you wish to add objects to.
map_rid = "ri.gaia..map.a1A2bcD3e45fg6h7ij"
# List[EmlId] | The IDs of the enterprise map layers to be added to the map.
eml_ids = [
    "0123456789012345678901234567890123456789012345678901234567890123",
    1234567890123456789012345678901234567890123456789012345678901234,
]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.add_enterprise_map_layers(
        map_rid, eml_ids=eml_ids, preview=preview
    )
    print("The add_enterprise_map_layers response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.add_enterprise_map_layers: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AddEnterpriseMapLayersToMapResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **add_objects**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Add objects to a map. Currently only Foundry-managed object types may be added. If unknown objects 
or objects that don't satisfy the security requirements are provided, the entire request will fail.
This creates a new layer that includes all the provided objects per request, thus not idempotent.
Returns the ID of the layer created.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_rid** | GaiaMapRid | The RID of the Gaia map that you wish to add objects to.  |  |
**label** | str | The name of the layer to be created  |  |
**object_rids** | List[RID] |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**AddObjectsToMapResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapRid | The RID of the Gaia map that you wish to add objects to.
map_rid = "ri.gaia..map.a1A2bcD3e45fg6h7ij"
# str | The name of the layer to be created
label = "Example layer name."
# List[RID]
object_rids = [
    "ri.phonograph2-objects.main.object.example1",
    "ri.phonograph2-objects.main.object.example2",
]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.add_objects(
        map_rid, label=label, object_rids=object_rids, preview=preview
    )
    print("The add_objects response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.add_objects: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | AddObjectsToMapResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **export_kmz**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Export all map elements from a Gaia map to a KMZ file suitable for rendering in external applications, such as Google Earth. There are no schema compatibility guarantees provided for internal KMZ content exported by this endpoint.
Only local map elements will be exported i.e. no elements from linked maps.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_id** | GaiaMapId | The artifact identifier of the Gaia map being exported, which can be copied via **Help** > **Developer** > **Copy id**. The export call will download all elements in the referenced map.  |  |
**name** | Optional[str] | The name of the exported file. Defaults to 'palantir-export'.  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**bytes**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapId | The artifact identifier of the Gaia map being exported, which can be copied via **Help** > **Developer** > **Copy id**. The export call will download all elements in the referenced map.
map_id = "ri.gotham-artifact.1234567890123456789-0987654321123456789.gaia-map.a1A2bcD3e45fg6h7ij"
# Optional[str] | The name of the exported file. Defaults to 'palantir-export'.
name = "Example file name"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.export_kmz(map_id, name=name, preview=preview)
    print("The export_kmz response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.export_kmz: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **load**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Loads the structure and basic metadata of a Gaia map, given a map GID. Metadata includes the map's title and 
layer labels.

The response contains a mapping of all layers contained in the map. The map's layer hierarchy can be recreated 
by using the `rootLayerIds` in the response along with the `subLayerIds` field in the layer's metadata.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_gid** | GaiaMapGid | The GID of the map to be loaded.  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**LoadMapResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapGid | The GID of the map to be loaded.
map_gid = "ri.gotham-artifact.0-1.gaia-map.a1A2bcD3e45fg6h7ij"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.load(map_gid, preview=preview)
    print("The load response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.load: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadMapResponse  | A successful map load response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **load_layers**
Loads the elements contained in the requested layers of a Gaia map. The response includes the geometries 
associated with the elements.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_gid** | GaiaMapGid | The GID of the map containing the layers to be loaded.  |  |
**layer_ids** | List[GaiaLayerId] | The set of layer IDs to load from a Gaia map.  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**LoadLayersResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapGid | The GID of the map containing the layers to be loaded.
map_gid = "ri.gotham-artifact.0-1.gaia-map.a1A2bcD3e45fg6h7ij"
# List[GaiaLayerId] | The set of layer IDs to load from a Gaia map.
layer_ids = ["exampleLayerId"]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.load_layers(map_gid, layer_ids=layer_ids, preview=preview)
    print("The load_layers response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.load_layers: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadLayersResponse  | A successful load layers response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **render_symbol**
Fetches the PNG for the given symbol identifier


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**gaia_symbol** | GaiaSymbol | Body of the request |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**bytes**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaSymbol | Body of the request
gaia_symbol = {"type": "MilsymSymbol", "sidc": "SHG-USTI-------"}
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.render_symbol(gaia_symbol, preview=preview)
    print("The render_symbol response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.render_symbol: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | A successful render response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **search**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Retrieves all published maps containing the mapName (does not have to be exact).


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**map_name** | GaiaMapName | The name of the map(s) to be queried.  |  |
**page_size** | Optional[PageSize] | The maximum number of matching Gaia maps to return. Defaults to 50.  | [optional] |
**page_token** | Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request.  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**SearchMapsResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# GaiaMapName | The name of the map(s) to be queried.
map_name = "Example Map Name"
# Optional[PageSize] | The maximum number of matching Gaia maps to return. Defaults to 50.
page_size = 10
# Optional[PageToken] | The page token indicates where to start paging. This should be omitted from the first page's request.
page_token = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.gaia.Map.search(
        map_name=map_name, page_size=page_size, page_token=page_token, preview=preview
    )
    print("The search response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Map.search: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SearchMapsResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

