# RasterTilesRenderableContent

Renderable content represented with raster tiles in the Web Mercator (EPSG:3857) projection, laid out with the
single root tile, (z=0, x=0, y=0), covering the whole world. Construct the url using the url template supplied
to load the raster tile.
See https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**url** | str | Yes | URL template to use to fetch image tiles in the slippy layout. Example '.../{z}/{x}/{y}'  |
**tile_display_resolution** | MrsVirtualPixels | Yes |  |
**covering_geometry** | GeoJsonObject | Yes |  |
**style** | MrsRasterStyle | Yes |  |
**type** | Literal["rasterTilesWebMercator"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
