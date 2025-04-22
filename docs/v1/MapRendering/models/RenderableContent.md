# RenderableContent

Represents a set of geopositioned geometries and their corresponding style to be rendered on to a map.


This is a discriminator type and does not contain any fields. Instead, it is a union
of of the models listed below.

This discriminator class uses the `type` field to differentiate between classes.

| Class | Value
| ------------ | -------------
GeometryRenderableContent | geometry
RasterTilesRenderableContent | rasterTilesWebMercator


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
