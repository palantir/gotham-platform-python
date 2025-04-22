# HighPriorityTargetLists

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /gotham/v1/twb/highPriorityTargetList | Stable |
[**get**](#get) | **GET** /gotham/v1/twb/highPriorityTargetList/{rid} | Stable |
[**update**](#update) | **PUT** /gotham/v1/twb/highPriorityTargetList/{rid} | Stable |

# **create**
Create a High Priority Target List.
Returns the RID of the created High Priority Target List.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**name** | str |  |  |
**security** | ArtifactSecurity |  |  |
**target_aois** | List[HptlTargetAoi] |  |  |
**targets** | List[HighPriorityTargetListTargetV2] | A list of HighPriorityTargetListTargets |  |
**area_geo** | Optional[GeoPolygon] |  | [optional] |
**area_object_rid** | Optional[ObjectPrimaryKey] |  | [optional] |
**description** | Optional[str] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |
**target_board** | Optional[TargetBoardRid] |  | [optional] |

### Return type
**CreateHighPriorityTargetListResponseV2**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# str
name = "Example hptl name."
# ArtifactSecurity
security = None
# List[HptlTargetAoi]
target_aois = [
    {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Lake215",
        "data": {"entity": "ri.gotham.123-456.object-internal.example"},
    },
    {
        "id": "123e4567-e89b-12d3-a456-426614174020",
        "name": "Lake230",
        "data": {"entity": "ri.gotham.123-456.object-internal.example"},
    },
]
# List[HighPriorityTargetListTargetV2] | A list of HighPriorityTargetListTargets
targets = [
    {
        "highPriorityTargetListTargetId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
        "targetType": "Airplane",
        "priority": 1,
        "subPriority": 4,
        "category": "Transport",
        "when": "PLANNED",
        "agm": {
            "agmId": "2a46fbf6-ff93-4710-951a-015ed5c92441",
            "effectType": "NEUTRALIZE",
            "effector": "F-16C",
            "effectorPriority": 2,
            "timelinessInMinutes": 5,
        },
        "aoiId": "123e4567-e89b-12d3-a456-426614174000",
    },
    {
        "highPriorityTargetListTargetId": "54ac3383-b953-4d65-8f98-7c3fbbbb481a",
        "targetType": "Ship",
        "priority": 1,
        "subPriority": 2,
        "category": "Transport",
        "when": "PLANNED",
        "agm": {
            "agmId": "2f0df2cb-0737-4675-a481-2c93259a78ae",
            "effectType": "DESTROY",
            "effector": "M777",
            "effectorPriority": 2,
            "timelinessInMinutes": 5,
        },
        "aoiId": "123e4567-e89b-12d3-a456-426614174020",
    },
]
# Optional[GeoPolygon]
area_geo = {"points": {"longitude": 1.0, "latitude": 1.0, "elevation": 1.0}}
# Optional[ObjectPrimaryKey]
area_object_rid = "ri.gotham-artifact.0-0.object-internal.example"
# Optional[str]
description = "Example description."
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True
# Optional[TargetBoardRid]
target_board = "ri.gotham-artifact.0-0.target-collection.example"


try:
    api_response = client.target_workbench.HighPriorityTargetLists.create(
        name=name,
        security=security,
        target_aois=target_aois,
        targets=targets,
        area_geo=area_geo,
        area_object_rid=area_object_rid,
        description=description,
        preview=preview,
        target_board=target_board,
    )
    print("The create response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling HighPriorityTargetLists.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateHighPriorityTargetListResponseV2  | Success response with the ID of the created High Priority Target List. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get**
Load a High Priority Target List by RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | HighPriorityTargetListRid | High Priority Target List RID |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**LoadHighPriorityTargetListResponseV2**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# HighPriorityTargetListRid | High Priority Target List RID
rid = "ri.gotham-artifact.0-0.hptl.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.HighPriorityTargetLists.get(rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling HighPriorityTargetLists.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadHighPriorityTargetListResponseV2  | Success response with the requested High Priority Target List. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **update**
Modify a High Priority Target List by RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | HighPriorityTargetListRid | High Priority Target List RID |  |
**base_revision_id** | int | The current version of the HighPriorityTargetList to be modified. Any modifying operations should be accompanied by this version to avoid concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.  |  |
**target_aois** | List[HptlTargetAoi] |  |  |
**targets** | List[HighPriorityTargetListTargetV2] | A list of HighPriorityTargetListTargets |  |
**area_geo** | Optional[GeoPolygon] |  | [optional] |
**area_object_rid** | Optional[ObjectPrimaryKey] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |
**target_board** | Optional[TargetBoardRid] |  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# HighPriorityTargetListRid | High Priority Target List RID
rid = "ri.gotham-artifact.0-0.target.example"
# int | The current version of the HighPriorityTargetList to be modified. Any modifying operations should be accompanied by this version to avoid concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.
base_revision_id = 1
# List[HptlTargetAoi]
target_aois = [
    {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Lake215",
        "data": {"entity": "ri.gotham.123-456.object-internal.example"},
    }
]
# List[HighPriorityTargetListTargetV2] | A list of HighPriorityTargetListTargets
targets = [
    {
        "highPriorityTargetListTargetId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
        "targetType": "Airplane",
        "priority": 1,
        "when": "PLANNED",
        "agm": {
            "agmId": "2a46fbf6-ff93-4710-951a-015ed5c92441",
            "effectType": "NEUTRALIZE",
            "effector": "F-16C",
            "effectorPriority": 2,
            "timelinessInMinutes": "5`",
        },
    },
    {
        "highPriorityTargetListTargetId": "54ac3383-b953-4d65-8f98-7c3fbbbb481a",
        "targetType": "Ship",
        "priority": 1,
        "when": "PLANNED",
        "agm": {
            "agmId": "2f0df2cb-0737-4675-a481-2c93259a78ae",
            "effectType": "DESTROY",
            "effector": "M777",
            "effectorPriority": 2,
            "timelinessInMinutes": 5,
        },
    },
]
# Optional[GeoPolygon]
area_geo = {"points": {"longitude": 1.0, "latitude": 1.0, "elevation": 1.0}}
# Optional[ObjectPrimaryKey]
area_object_rid = "ri.gotham-artifact.0-0.object-internal.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True
# Optional[TargetBoardRid]
target_board = None


try:
    api_response = client.target_workbench.HighPriorityTargetLists.update(
        rid,
        base_revision_id=base_revision_id,
        target_aois=target_aois,
        targets=targets,
        area_geo=area_geo,
        area_object_rid=area_object_rid,
        preview=preview,
        target_board=target_board,
    )
    print("The update response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling HighPriorityTargetLists.update: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

