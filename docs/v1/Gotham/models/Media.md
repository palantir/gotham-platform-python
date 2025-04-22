# Media

The representation of a media reference attached to an Object.
To download media contents, pass the Media RID to the [get media content](https://palantir.com/docs/gotham/api/revdb-resources/media/get-media-content) operation.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**rid** | MediaRid | Yes |  |
**title** | str | Yes | The user-friendly title of a of media, suitable for displaying to users. |
**description** | Optional[str] | No | The user-friendly description of a of media, suitable for displaying to users. May not be present for all media.  |
**size_bytes** | Optional[SizeBytes] | No |  |
**media_type** | MediaType | Yes |  |
**security** | List[SecurityKey] | Yes | The ID of the security details for this media. There can be multiple associated with a single media. If a user has he security markings or groups of any of them, they will have the associated permission.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
