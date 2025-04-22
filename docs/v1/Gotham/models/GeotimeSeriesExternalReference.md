# GeotimeSeriesExternalReference

Reference to a geotime series suitable for external usage.
Series ID (also referred to as Track ID) is a per-series/track-level attribute, such
as a flight, manifest or voyage number.

Observation Spec / Source System and Collection uniquely define a "collection" of observations in a given
source system adhering to a specific shape.

See [Observation basics](https://palantir.com/docs/gotham/api/geotime-resources/observations/observation-basics) for more
information about geotime observations.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**source_system_spec_id** | str | Yes |  |
**collection_id** | str | Yes |  |
**observation_spec_id** | str | Yes |  |
**series_id** | str | Yes |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
