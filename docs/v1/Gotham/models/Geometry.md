# Geometry

Abstract type for all GeoJSON object except Feature and FeatureCollection

This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
MultiPoint | MultiPoint
GeometryCollection | GeometryCollection
MultiLineString | MultiLineString
LineString | LineString
MultiPolygon | MultiPolygon
Point | Point
Polygon | Polygon


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
