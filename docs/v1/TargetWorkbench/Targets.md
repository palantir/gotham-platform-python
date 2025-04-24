# Targets

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**create**](#create) | **POST** /gotham/v1/twb/target | Stable |
[**create_intel**](#create_intel) | **PUT** /gotham/v1/twb/createTargetIntel/{rid} | Stable |
[**delete**](#delete) | **PUT** /gotham/v1/twb/target/{rid}/archive | Stable |
[**get**](#get) | **GET** /gotham/v1/twb/target/{rid} | Stable |
[**remove_intel**](#remove_intel) | **PUT** /gotham/v1/twb/removeTargetIntel/{rid} | Stable |
[**update**](#update) | **PUT** /gotham/v1/twb/target/{rid} | Stable |

# **create**
Create a Target.
Returns the RID of the created Target.

If `sidc` field is specified and invalid according to MIL-STD-2525C specification,
an `InvalidSidc` error is thrown.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**aimpoints** | List[TargetAimpointV2] |  |  |
**column** | TargetBoardColumnId |  |  |
**name** | str |  |  |
**security** | ArtifactSecurity |  |  |
**target_board** | TargetBoardRid |  |  |
**description** | Optional[str] |  | [optional] |
**entity_rid** | Optional[ObjectPrimaryKey] |  | [optional] |
**high_priority_target_list_target_subtype** | Optional[HptlTargetSubtype] |  | [optional] |
**location** | Optional[LocationSource] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |
**sidc** | Optional[str] | MIL-STD 2525C Symbol Identification Code | [optional] |
**target_identifier** | Optional[TargetIdentifier] |  | [optional] |
**target_type** | Optional[str] | The resource type of the target. Example: Building  | [optional] |

### Return type
**CreateTargetResponseV2**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[TargetAimpointV2]
aimpoints = [
    {
        "id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
        "number": 1,
        "name": "Example targetAimPoint name",
        "location": {
            "center": {"longitude": 0.0, "latitude": 0.0, "elevation": 0.0},
            "radius": 1.1,
        },
        "geotimeTrack": "ri.gotham.0-0.geotime-track.aa.bb.cc.example",
        "entityRid": "ri.gotham.123-456.object-internal.example",
    },
    {
        "id": "54ac3383-b953-4d65-8f98-7c3fbbbb481a",
        "number": 1,
        "name": "Example targetAimPoint name",
        "location": {
            "center": {"longitude": 0.0, "latitude": 0.0, "elevation": 0.0},
            "radius": 1.1,
        },
        "geotimeTrack": "ri.gotham.0-0.geotime-track.aa.bb.cc.example",
        "entityRid": "ri.gotham.123-456.object-internal.example",
    },
]
# TargetBoardColumnId
column = "DRAFT"
# str
name = "Enemy Building"
# ArtifactSecurity
security = {"portionMarkings": ["SENSITIVE"]}
# TargetBoardRid
target_board = "ri.gotham-artifact.0-0.target-board.example"
# Optional[str]
description = "Known enemy building."
# Optional[ObjectPrimaryKey]
entity_rid = "ri.gotham.123-456.object-internal.example"
# Optional[HptlTargetSubtype]
high_priority_target_list_target_subtype = "Red Car"
# Optional[LocationSource]
location = {
    "manualLocation": {
        "lat": 0.0,
        "lng": 0.0,
        "circularErrorInMeters": 0.0,
        "hae": 0.0,
        "msl": 0.0,
        "agl": 0.0,
    }
}
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True
# Optional[str] | MIL-STD 2525C Symbol Identification Code
sidc = "SEGPU-------"
# Optional[TargetIdentifier]
target_identifier = {"customTargetIdentifier": "Example Identifier 000"}
# Optional[str] | The resource type of the target. Example: Building
target_type = "Building"


try:
    api_response = client.target_workbench.Targets.create(
        aimpoints=aimpoints,
        column=column,
        name=name,
        security=security,
        target_board=target_board,
        description=description,
        entity_rid=entity_rid,
        high_priority_target_list_target_subtype=high_priority_target_list_target_subtype,
        location=location,
        preview=preview,
        sidc=sidc,
        target_identifier=target_identifier,
        target_type=target_type,
    )
    print("The create response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Targets.create: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | CreateTargetResponseV2  | Success response with the RID of the created target. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **create_intel**
Create Intel on Target by RID


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetRid | Target RID |  |
**domain** | IntelDomain |  |  |
**id** | IntelId |  |  |
**intel_type** | IntelUnion |  |  |
**name** | str |  |  |
**valid_time** | datetime |  |  |
**confidence** | Optional[float] |  | [optional] |
**description** | Optional[str] |  | [optional] |
**location** | Optional[GeoCircle] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |
**source** | Optional[str] |  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetRid | Target RID
rid = "ri.gotham-artifact.0-0.target.example"
# IntelDomain
domain = None
# IntelId
id = "Example Intel Id"
# IntelUnion
intel_type = {
    "IntelGeotimeObservation": {"geotimeTrack": "ri.gotham.0-0.geotime-track.aa.bb.cc.example"}
}
# str
name = "Example Intel Name"
# datetime
valid_time = "2023-10-04T14:48:00.000Z"
# Optional[float]
confidence = 3.0
# Optional[str]
description = "Intel containing location."
# Optional[GeoCircle]
location = {"center": {"longitude": 0.0, "latitude": 0.0, "elevation": 0.0}, "radius": 1.1}
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True
# Optional[str]
source = "Example source"


try:
    api_response = client.target_workbench.Targets.create_intel(
        rid,
        domain=domain,
        id=id,
        intel_type=intel_type,
        name=name,
        valid_time=valid_time,
        confidence=confidence,
        description=description,
        location=location,
        preview=preview,
        source=source,
    )
    print("The create_intel response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Targets.create_intel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **delete**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Archive a Target by RID.
The user is required to have OWN permissions on the target.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetRid | Target RID |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetRid | Target RID
rid = "ri.gotham-artifact.0-0.target.example"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.Targets.delete(rid, preview=preview)
    print("The delete response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Targets.delete: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **get**
Load a Target by RID.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetRid | Target RID |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**LoadTargetResponseV2**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetRid | Target RID
rid = None
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.Targets.get(rid, preview=preview)
    print("The get response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Targets.get: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | LoadTargetResponseV2  | Success response with the requested Target. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **remove_intel**
Remove Intel on Target by RID


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetRid | Target RID |  |
**id** | IntelId |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetRid | Target RID
rid = "ri.gotham-artifact.0-0.target.example"
# IntelId
id = "Example Intel Id"
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.target_workbench.Targets.remove_intel(rid, id=id, preview=preview)
    print("The remove_intel response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Targets.remove_intel: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

# **update**
Set current state of Target by RID.

If `sidc` field is specified and invalid according to MIL-STD-2525C specification,
an `InvalidSidc` error is thrown.


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**rid** | TargetRid | Target RID |  |
**aimpoints** | List[TargetAimpointV2] |  |  |
**base_revision_id** | Long | The version of the Target to be modified. The modifying operations will be transformed against any concurrent operations made since this version.   If the supplied version is outdated, the server will respond back with RevisionTooOld exception and the client must resend the request with the updated baseRevisionId.  |  |
**name** | str |  |  |
**client_id** | Optional[str] | The client id is used to identify conflicting edits made by the same client, typically due to retries, and discard them. Clients should choose an arbitrary random identifier to distinguish themselves. There is no need persist and re-use the same client id over multiple sessions.  The client id is also used to avoid broadcasting operations to the client who submitted them.  | [optional] |
**description** | Optional[str] |  | [optional] |
**entity_rid** | Optional[ObjectPrimaryKey] |  | [optional] |
**high_priority_target_list_target_subtype** | Optional[HptlTargetSubtype] |  | [optional] |
**location** | Optional[LocationSource] |  | [optional] |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |
**sidc** | Optional[str] | MIL-STD 2525C Symbol Identification Code | [optional] |
**target_identifier** | Optional[TargetIdentifier] |  | [optional] |
**target_type** | Optional[str] | The resource type of the target. Example: Building  | [optional] |

### Return type
**EmptySuccessResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# TargetRid | Target RID
rid = "ri.gotham-artifact.0-0.target.example"
# List[TargetAimpointV2]
aimpoints = [
    {
        "id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
        "number": 1,
        "name": "Example targetAimPoint name",
        "location": {
            "center": {"longitude": 4.0, "latitude": 4.0, "elevation": 4.0},
            "radius": 1.1,
        },
        "geotimeTrack": "ri.gotham.0-0.geotime-track.aa.bb.cc.example",
        "entityRid": "ri.gotham.123-456.object-internal.example",
    },
    {
        "id": "54ac3383-b953-4d65-8f98-7c3fbbbb481a",
        "number": 1,
        "name": "Example targetAimPoint name",
        "location": {
            "center": {"longitude": 0.0, "latitude": 0.0, "elevation": 0.0},
            "radius": 1.1,
        },
        "geotimeTrack": "ri.gotham.0-0.geotime-track.aa.bb.cc.example",
        "entityRid": "ri.gotham.123-456.object-internal.example",
    },
]
# Long | The version of the Target to be modified. The modifying operations will be transformed against any concurrent operations made since this version.   If the supplied version is outdated, the server will respond back with RevisionTooOld exception and the client must resend the request with the updated baseRevisionId.
base_revision_id = 1
# str
name = "Enemy Building"
# Optional[str] | The client id is used to identify conflicting edits made by the same client, typically due to retries, and discard them. Clients should choose an arbitrary random identifier to distinguish themselves. There is no need persist and re-use the same client id over multiple sessions.  The client id is also used to avoid broadcasting operations to the client who submitted them.
client_id = "123e4567-e89b-12d3-a456-426614174000"
# Optional[str]
description = "Known enemy building."
# Optional[ObjectPrimaryKey]
entity_rid = "ri.gotham.123-456.object-internal.example"
# Optional[HptlTargetSubtype]
high_priority_target_list_target_subtype = "Blue Car"
# Optional[LocationSource]
location = {
    "manualLocation": {
        "lat": 0.0,
        "lng": 0.0,
        "circularErrorInMeters": 0.0,
        "hae": 0.0,
        "msl": 0.0,
        "agl": 0.0,
    }
}
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True
# Optional[str] | MIL-STD 2525C Symbol Identification Code
sidc = "SEGPU-------"
# Optional[TargetIdentifier]
target_identifier = {"customTargetIdentifier": "Example Identifier 005"}
# Optional[str] | The resource type of the target. Example: Building
target_type = "Building"


try:
    api_response = client.target_workbench.Targets.update(
        rid,
        aimpoints=aimpoints,
        base_revision_id=base_revision_id,
        name=name,
        client_id=client_id,
        description=description,
        entity_rid=entity_rid,
        high_priority_target_list_target_subtype=high_priority_target_list_target_subtype,
        location=location,
        preview=preview,
        sidc=sidc,
        target_identifier=target_identifier,
        target_type=target_type,
    )
    print("The update response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Targets.update: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | EmptySuccessResponse  | Success response. | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

