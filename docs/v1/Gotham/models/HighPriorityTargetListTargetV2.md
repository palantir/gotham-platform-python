# HighPriorityTargetListTargetV2

The target on an High Priority Target List.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**high_priority_target_list_target_id** | HighPriorityTargetListTargetId | Yes |  |
**aoi_id** | Optional[HptlTargetAoiId] | No |  |
**target_type** | str | Yes | The type of object of this High Priority Target List Target. Example: Car  |
**target_subtypes** | List[HptlTargetSubtype] | Yes | A target's subtype will be matched for membership against this set of subtypes in order to determine priority, subpriority, and AGM. An empty set of targetSubtypes indicates that this HptlTarget can be matched against ANY target subtype.  |
**priority** | int | Yes | Priority between 1 (highest priority) to 10 of this High Priority Target List Target.  |
**sub_priority** | Optional[int] | No | Further categorization of a HptlTarget's priority.  |
**category** | Optional[str] | No | The object class appearing on HighPriorityTargetList. Example: Airplane  |
**elnots** | List[HptlTargetElnot] | Yes | ELINT Notations (ELNOTs) associated with the HPTL target type  |
**when** | HighPriorityTargetListWhen | Yes |  |
**agm** | Dict[HighPriorityTargetListAgmId, HighPriorityTargetListAgm] | Yes | A map of HighPriorityTargetListAgmId to HighPriorityTargetListAgm  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
