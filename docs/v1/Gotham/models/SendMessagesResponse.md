# SendMessagesResponse

SendMessagesResponse

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**responses** | List[SendMessageResponse] | Yes | The list of messages which were sent successfully. Messages are returned in the order in which they were sent in the request.  |
**failures** | List[SendMessageFailure] | Yes | The list of messages which failed to be sent in Inbox due to conflicts with existing messages.  |


[[Back to Model list]](../../../../README.md#models-v1-link) [[Back to API list]](../../../../README.md#apis-v1-link) [[Back to README]](../../../../README.md)
