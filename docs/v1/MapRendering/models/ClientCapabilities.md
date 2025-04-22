# ClientCapabilities

The render capability of the client. Renderables will be returned in the best possible format that's supported
by the client.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**supported_renderable_content** | List[RenderableContentType] | Yes | Supported renderable content types. Unsupported types will be converted to supported ones. More advanced renderable content types may suffer lower performance or fidelity when being transcoded into the base geometry type. The base geometry type must always be supported. Refer to [RenderableContent](https://palantir.com/#/components/schemas/RenderableContent) for the shape of the renderable contents.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
