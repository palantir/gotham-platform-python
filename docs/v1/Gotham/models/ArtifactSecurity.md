# ArtifactSecurity

Security mutation details for a target, target board, or hptl.
Specifying security overrides the system's default security when creating and updating data.
This model may evolve over time for other security features.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**portion_markings** | List[PortionMarking] | Yes | Collection of classification portion markings; markings are validated against the system's Classification Based Access Control (CBAC) rules; if invalid, an error is raised.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
