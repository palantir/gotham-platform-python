# PortionMarking

Security markings represent the level of access control that applies to a specific piece of information (e.g., object property, object title).
Security markings are required upon creating a new object, and upon adding a new property to an existing object.
To access information with one or more markings, the user must have access to the markings associated with that information as defined by
your organization's defined security rules. Only users with the correct permissions can get, update, or delete a property
with security markings.

In particular, if a user creates an object and adds a property of type with highly restricted markings, it is possible
that subsequent calls to the get object properties endpoint may fail to display the highly restricted property.

Contact your Palantir administrator for more information on the markings that your organization uses.


## Type
```python
str
```


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
