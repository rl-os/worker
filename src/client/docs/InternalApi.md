# src.client.InternalApi

All URIs are relative to *https://risu.life*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_internal_scores_submit_post**](InternalApi.md#api_internal_scores_submit_post) | **POST** /api/internal/scores/submit | Score submission

# **api_internal_scores_submit_post**
> InlineResponse200 api_internal_scores_submit_post(body)

Score submission

### Example
```python
from __future__ import print_function
import time
import src.client
from src.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: password
configuration = src.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = src.client.InternalApi(src.client.ApiClient(configuration))
body = src.client.UpdateScoreRequest() # UpdateScoreRequest | 

try:
    # Score submission
    api_response = api_instance.api_internal_scores_submit_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->api_internal_scores_submit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateScoreRequest**](UpdateScoreRequest.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[password](../README.md#password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

