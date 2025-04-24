# TargetBoards

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /gotham/v1/twb/targetBoard | Stable |
[**delete**](#delete) | **PUT** /gotham/v1/twb/targetBoard/{rid}/archive | Stable |
[**get**](#get) | **GET** /gotham/v1/twb/targetBoard/{rid} | Stable |
[**load_target_pucks**](#load_target_pucks) | **PUT** /gotham/v1/twb/board/{rid}/loadTargetPucks | Stable |
[**update**](#update) | **PUT** /gotham/v1/twb/targetBoard/{rid} | Stable |
[**update_target_column**](#update_target_column) | **PUT** /gotham/v1/twb/setTargetColumn/{targetRid} | Stable |

# **create**
By default, create a TargetBoard with default columns: IDENTIFIED TARGET, PRIORITIZED TARGET, IN COORDINATION, IN EXECUTION, COMPLETE.
Returns the RID of the created TargetBoard.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**name** | str |  |  |
**security** | ArtifactSecurity |  |  |
**configuration** | Optional[TargetBoardConfiguration] |  | [optional] |
**description** | Optional[str] |  | [optional] |
**high_priority_target_list** | Optional[HighPriorityTargetListRid] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**CreateTargetBoardResponseV2**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# str
name = "Example target board name."
# ArtifactSecurity
security = {"portionMarkings": ["SENSITIVE"]}
# Optional[TargetBoardConfiguration]
configuration = {
    "columns": [{"id": "id12345", "name": "DONE", "color": "RED"}],
    "targetIdentifiers": ["CUSTOM"],
}
# Optional[str]
description = "Example description."
# Optional[HighPriorityTargetListRid]
high_priority_target_list = "ri.gotham-artifact.0-0.hptl.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.TargetBoards.create(
        name=name,
        security=security,
        configuration=configuration,
        description=description,
        high_priority_target_list=high_priority_target_list,
        preview=preview,
    )
    print("The create response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling TargetBoards.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateTargetBoardResponseV2  | Success response with the ID of the created Target Board. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **delete**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Archive a Collection by RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetBoardRid | Target Board RID |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetBoardRid | Target Board RID
rid = "ri.gotham-artifact.0-0.target-board.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.TargetBoards.delete(rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling TargetBoards.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get**
Load Target Board by RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetBoardRid | Target Board RID |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**LoadTargetBoardResponseV2**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetBoardRid | Target Board RID
rid = "ri.gotham-artifact.0-0.target-collection.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.TargetBoards.get(rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling TargetBoards.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadTargetBoardResponseV2  | Success response with the requested Target Board. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **load_target_pucks**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::
Loads target pucks contained in a target board. The response may include the puck's associated location and
board status metadata, depending on the load levels specified in the request.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetBoardRid | Target Board RID to load target pucks from.  |  |
**load_level** | List[TargetPuckLoadLevel] | Determines the set of information to load for a given target puck.  |  |
**allow_stale_loads** | Optional[bool] | If set to true, will potentially load "stale" data associated with the target puck. Defaults to false. Note that even if the returned data is stale, the data will be stale in the order of minutes or less. Setting this option to true will yield better performance, especially for consumers that wish to poll this endpoint at a frequent interval.  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**LoadTargetPucksResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetBoardRid | Target Board RID to load target pucks from.
rid = "ri.gotham-artifact.0-0.target-board.example"
# List[TargetPuckLoadLevel] | Determines the set of information to load for a given target puck.
load_level = ["LOCATION", "BOARD_STATUS"]
# Optional[bool] | If set to true, will potentially load "stale" data associated with the target puck. Defaults to false. Note that even if the returned data is stale, the data will be stale in the order of minutes or less. Setting this option to true will yield better performance, especially for consumers that wish to poll this endpoint at a frequent interval.
allow_stale_loads = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.TargetBoards.load_target_pucks(
        rid, load_level=load_level, allow_stale_loads=allow_stale_loads, preview=preview
    )
    print("The load_target_pucks response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling TargetBoards.load_target_pucks: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadTargetPucksResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **update**
Modify a Target Board by RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetBoardRid | TargetBoard RID |  |
**base_revision_id** | Long | The current version of the Target Board to be modified. The archive operation will be transformed against any concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.  |  |
**name** | str |  |  |
**configuration** | Optional[TargetBoardConfiguration] |  | [optional] |
**description** | Optional[str] |  | [optional] |
**high_priority_target_list** | Optional[HighPriorityTargetListRid] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetBoardRid | TargetBoard RID
rid = "ri.gotham-artifact.0-0.target-collection.example"
# Long | The current version of the Target Board to be modified. The archive operation will be transformed against any concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.
base_revision_id = 1
# str
name = "New example target board name"
# Optional[TargetBoardConfiguration]
configuration = {
    "columns": [{"id": "EXECUTION", "name": "IN PROGRESS", "color": "RED"}],
    "targetIdentifiers": ["CUSTOM"],
}
# Optional[str]
description = "New example description."
# Optional[HighPriorityTargetListRid]
high_priority_target_list = "ri.gotham-artifact.0-0.hptl.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.TargetBoards.update(
        rid,
        base_revision_id=base_revision_id,
        name=name,
        configuration=configuration,
        description=description,
        high_priority_target_list=high_priority_target_list,
        preview=preview,
    )
    print("The update response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling TargetBoards.update: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **update_target_column**
Move a Target into a TargetBoardColumn from an old column.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**target_rid** | TargetRid |  |  |
**base_revision_id** | Long | The version of Target Board you are working with. The set operation will be transformed against any concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.  |  |
**board_rid** | TargetBoardRid |  |  |
**new_column_id** | TargetBoardColumnId |  |  |
**client_id** | Optional[str] | The client id is used to identify conflicting edits made by the same client, typically due to retries, and discard them. Clients should choose an arbitrary random identifier to distinguish themselves. There is no need persist and re-use the same client id over multiple sessions.  The client id is also used to avoid broadcasting operations to the client who submitted them.  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetRid
target_rid = "ri.gotham-artifact.0-0.target.example"
# Long | The version of Target Board you are working with. The set operation will be transformed against any concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.
base_revision_id = None
# TargetBoardRid
board_rid = "ri.gotham-artifact.0-0.target-board.example"
# TargetBoardColumnId
new_column_id = "CLOSED"
# Optional[str] | The client id is used to identify conflicting edits made by the same client, typically due to retries, and discard them. Clients should choose an arbitrary random identifier to distinguish themselves. There is no need persist and re-use the same client id over multiple sessions.  The client id is also used to avoid broadcasting operations to the client who submitted them.
client_id = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.TargetBoards.update_target_column(
        target_rid,
        base_revision_id=base_revision_id,
        board_rid=board_rid,
        new_column_id=new_column_id,
        client_id=client_id,
        preview=preview,
    )
    print("The update_target_column response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling TargetBoards.update_target_column: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

