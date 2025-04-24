# Invocation

Represents a request to render a set of Foundry objects. This includes information on how the objects should be
rendered.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | InvocationId | Yes |  |
**sourcing_only** | Optional[bool] | No | Set to only receive sourcing information with no renderables. This is useful for rendering a list view without displaying renderables, such as in the case of a layer with visibility toggled off.  |
**objects** | ObjectsReference | Yes |  |
**renderer** | RendererReference | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
