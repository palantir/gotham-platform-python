# GeometryStyle

Describes styling information to control the appearance of observation geometry.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**stroke_width** | Optional[float] | No |  |
**stroke_color** | Optional[str] | No | A 6 character hexadecimal string describing the color of the border on all geometry. Default is "#FDFF00". The leading # is required.  |
**fill_color** | Optional[str] | No | A 6 character hexadecimal string describing the color to fill all geometry. The leading # is required. By default, the geometry will not be filled and will instead appear "hollow". If you want to fill a geometry, you must specify both fillColor and fillOpacity for this to have any effect.  |
**fill_opacity** | Optional[float] | No | A number between 0 and 1 (inclusive) which controls the opacity of the fill of all geometry. By default, this is 0. If you want to fill a geometry, you must specify both fillColor and fillOpacity for this to have any effect.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
