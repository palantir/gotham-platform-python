# LabelStyle

Styling properties for rendering labels on a map. Right now, this will always be attached to a Point geometry.
The "text" field should be drawn with the given visibility/opacity/color. The Y-coordinate of the point 
geometry represents the vertical midpoint of the rendered text and the X-coordinate of the point geometry 
should line up with either the leftmost, center, or rightmost part of the rendered text as determined by the
textAlignment field. Then, the text should be rotated clockwise about this point geometry as determined by the
rotation field.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**text** | Optional[str] | No | The text to render on the feature  |
**text_rotation** | Optional[float] | No | How many degrees (clockwise) to rotate the rendered text about the point provided in the geometry field  |
**text_color** | Optional[str] | No | A 6 character hexadecimal string describing the text color, if applicable. The leading # is required,  e.g. "#FF00FF"  |
**text_alignment** | Optional[TextAlignment] | No |  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
