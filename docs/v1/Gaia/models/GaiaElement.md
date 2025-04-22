# GaiaElement

A representation of an element in a Gaia map. An element can be thought as a leaf node in the structure of a
map. It contains information such as the geometry of a feature. An element has one or more features.

Each element has an ID unique within the context of its parent layer; the ID is not guaranteed to be unique
within the context of a map.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**id** | GaiaElementId | Yes |  |
**parent_id** | GaiaLayerId | Yes |  |
**features** | List[GaiaFeature] | Yes |  |
**label** | str | Yes |  |
**properties** | Optional[GaiaProperties] | No |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
