# LoadTargetResponseV2

The response body returned when loading a Target. The objectRid is the RID of the object being targeted.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**target** | TargetV2 | Yes |  |
**base_revision_id** | Long | Yes | The current version of the Target retrieved. Any modifying operations should be accompanied by this version to avoid concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
