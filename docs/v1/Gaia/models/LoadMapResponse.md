# LoadMapResponse

Contains information related to a Gaia map's structure and basic metadata.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**title** | str | Yes | The title of the loaded Gaia map.  |
**root_layer_ids** | List[GaiaLayerId] | Yes | The **root** layers of the loaded Gaia map. This does not include sub-layers, i.e. layers nested within a parent layer in a Gaia map.  |
**layers** | Dict[GaiaLayerId, GaiaLayerMetadata] | Yes | A mapping of **all** the layers contained in the Gaia map. Includes layers nested under the root layers.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
