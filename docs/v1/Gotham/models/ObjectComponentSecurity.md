# ObjectComponentSecurity

Security mutation details for a component of an object - property, media, link.
Specifying security overrides the system's default security when creating and updating data.
If portion markings are specified, permissions *may* be specified. If portion markings are not specified,
permissions *must* be specified.

This model may evolve over time for other security features.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**portion_markings** | List[PortionMarking] | Yes | Collection of classification portion markings; markings are validated against the system's Classification Based Access Control (CBAC) rules.  If invalid, an [InvalidClassificationPortionMarkings](https://palantir.com/docs/gotham/api/general/overview/errors#security-errors) error will be thrown.  If not specified, no markings will be applied.  |
**permissions** | List[PermissionItem] | Yes | An optional mapping of groups to permissions allowed for the group. If not specified, the system's default is for the Everyone group to have WRITE permission, and the Administrators group to have OWNER permission.  A user will get the highest permission of any of the group they belong to. If portion markings are specified, the user must have access to all the markings specified before these permissions are applied.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
