# TargetV2

The Target object.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | TargetRid | Yes |  |
**name** | str | Yes |  |
**description** | Optional[str] | No |  |
**target_boards** | List[TargetBoardRid] | Yes |  |
**location** | Optional[LocationSource] | No |  |
**target_type** | Optional[str] | No | This is used for effector pairing and determination around HPTL category and time sensitivity Example: Building  |
**entity_rid** | Optional[ObjectPrimaryKey] | No |  |
**sidc** | Optional[str] | No | MIL-STD 2525C Symbol Identification Code |
**aimpoints** | List[TargetAimpointV2] | Yes |  |
**target_identifier** | Optional[TargetIdentifier] | No |  |
**high_priority_target_list_target_subtype** | Optional[HptlTargetSubtype] | No |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
