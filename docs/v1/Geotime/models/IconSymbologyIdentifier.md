# IconSymbologyIdentifier

A built-in generic icon identifier. The color properties, if specified, must be a 6-character hexadecimal string
describing the color to use for the icon. The leading # is required.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**code** | str | Yes | The code of an icon allowed on a given deployment.  |
**fill_color** | Optional[str] | No | A 6-character hexadecimal string describing the color to use to fill the icon (if supported). The leading # is required.  |
**stroke_color** | Optional[str] | No | A 6-character hexadecimal string describing the color to use for the icon's stroke (if supported). The leading # is required.  |
**type** | Literal["iconSym"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
