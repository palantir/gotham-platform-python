# Messages

Method | HTTP request | Release Stage |
------------- | ------------- | ----- |
[**send**](#send) | **POST** /gotham/v1/inbox/messages | Stable |

# **send**
:::callout{theme=warning title=Warning}
This endpoint is in preview and may be modified or removed at any time.
To use this endpoint, add `preview=true` to the request query parameters.
:::

Send messages in Global Inbox.

Validation failure for any message will cause the entire request to throw before any messages are sent.

The response reports all messages which were successfully sent, and any messages which failed to
be sent due to a conflict with an existing message.

Callers must be added to the internal "External Inbox Alert Producers" group in Gotham Security (multipass).

Note that the recipient `realm` must be specified if the caller's `realm` is not identical. For
example, to send to the "Everyone" group in the "palantir-internal-realm" realm, the caller must either specify the realm or already be
in "palantir-internal-realm".


### Parameters

Name | Type | Description  | Notes |
------------- | ------------- | ------------- | ------------- |
**messages** | List[SendMessageRequest] |  |  |
**preview** | Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.  | [optional] |

### Return type
**SendMessagesResponse**

### Example

```python
from gotham import GothamClient
import gotham
from pprint import pprint

client = GothamClient(auth=gotham.UserTokenAuth(...), hostname="example.palantirfoundry.com")

# List[SendMessageRequest]
messages = [
    {
        "sender": {"displayName": "My External Message Sender"},
        "title": {"value": "Hello from the sendMessages API!"},
        "security": {"portionMarkings": ["SENSITIVE"]},
        "groupRecipients": [{"name": "my-example-group"}],
        "body": {
            "value": "Some **styled** extra content for my message",
            "formatStyle": "MARKDOWN",
        },
    }
]
# Optional[PreviewMode] | Represents a boolean value that restricts an endpoint to preview mode when set to true.
preview = True


try:
    api_response = client.inbox.Messages.send(messages=messages, preview=preview)
    print("The send response:\n")
    pprint(api_response)
except gotham.PalantirRPCException as e:
    print("HTTP error when calling Messages.send: %s\n" % e)

```



### Authorization

See [README](../../../README.md#authorization)

### HTTP response details
| Status Code | Type        | Description | Content Type |
|-------------|-------------|-------------|------------------|
**200** | SendMessagesResponse  | Success response | application/json |

[[Back to top]](#) [[Back to API list]](../../../README.md#apis-v1-link) [[Back to Model list]](../../../README.md#models-v1-link) [[Back to README]](../../../README.md)

