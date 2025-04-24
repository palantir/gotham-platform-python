# Media

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**get_media_content**](#get_media_content) | **GET** /gotham/v1/media/{mediaRid}/content | Stable |
[**get_object_media**](#get_object_media) | **GET** /gotham/v1/objects/{primaryKey}/media | Stable |

# **get_media_content**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Get the content of media.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**media_rid** | MediaRid | The RID of the media. |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**bytes**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# MediaRid | The RID of the media.
media_rid = (
    "ri.gotham.111111-0.media-internal.111111.xtdsXlRMFmRRUdwQsD2kZOYOLY_2FS0VQ9SviNM6AJ_2FJM_3D"
)
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.media.Media.get_media_content(media_rid, preview=preview)
    print("The get_media_content response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Media.get_media_content: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | bytes  | Success response. | */* |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get_object_media**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Get media metadata for object. Media metadata contains an identifier and other
attributes suitable for display/download, such as content type and title.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**primary_key** | ObjectPrimaryKey | The primary key of the requested object. |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**GetMediaResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# ObjectPrimaryKey | The primary key of the requested object.
primary_key = "ri.gotham.111111-0.object-internal.111111"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.media.Media.get_object_media(primary_key, preview=preview)
    print("The get_object_media response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Media.get_object_media: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | GetMediaResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

