# GeoJsonObject

GeoJSON object

The coordinate reference system for all GeoJSON coordinates is a
geographic coordinate reference system, using the World Geodetic System
1984 (WGS 84) datum, with longitude and latitude units of decimal
degrees.
This is equivalent to the coordinate reference system identified by the
Open Geospatial Consortium (OGC) URN
An OPTIONAL third-position element SHALL be the height in meters above
or below the WGS 84 reference ellipsoid.
In the absence of elevation values, applications sensitive to height or
depth SHOULD interpret positions as being at local ground or sea level.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
MultiPoint | MultiPoint
GeometryCollection | GeometryCollection
MultiLineString | MultiLineString
FeatureCollection | FeatureCollection
LineString | LineString
MultiPolygon | MultiPolygon
Point | Point
Polygon | Polygon
Feature | Feature


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
