# Observation

A geotemporal object along a Geotime Track (SSID, CID, SpecID, TrackID quadruplet).

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**source_system_id** | SourceSystemId | Yes |  |
**collection_id** | CollectionId | Yes |  |
**observation_spec_id** | ObservationSpecId | Yes |  |
**track_id** | str | Yes | The ID of a series of location points. This is a shared ID between Observations which forms a Track. These IDs are typically derived from the integrated data. For example, a flight identifier used to distinguish a unique voyage by a plane. |
**position** | GeoPoint | Yes |  |
**timestamp** | datetime | Yes |  |
**name** | Optional[str] | No | The name of the entity associated with the Observation. For example, 'My Plane' or 'Air Force One'.  |
**static_properties** | List[ObservationField] | Yes | Properties that are expected to remain constant along a Geotime Track. E.g. A plane's tail number. |
**live_properties** | List[ObservationField] | Yes | Properties that are expected to be updated frequently along a Geotime Track. E.g. A plane's heading. |
**style** | Optional[ObservationStyle] | No |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
