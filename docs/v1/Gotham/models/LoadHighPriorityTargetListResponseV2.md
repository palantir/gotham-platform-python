# LoadHighPriorityTargetListResponseV2

The response body returned when loading a High Priority Target List.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**high_priority_target_list** | HighPriorityTargetListV2 | Yes |  |
**base_revision_id** | int | Yes | The current version of the HighPriorityTargetList retrieved. Any modifying operations should be accompanied by this version to avoid concurrent operations made since this version. If there are any conflicting edits that result in changes to these operations when they're applied, that will be noted in the response.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
