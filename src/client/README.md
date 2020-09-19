# swagger-client
Internal API endpoint

- API version: 1.0.0
- Package version: 1.0.0

## Requirements.

Python 3.4+

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://risu.life*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InternalApi* | [**api_internal_scores_submit_post**](docs/InternalApi.md#api_internal_scores_submit_post) | **POST** /api/internal/scores/submit | Score submission

## Documentation For Models

 - [Error](docs/Error.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [UpdateScoreRequest](docs/UpdateScoreRequest.md)
 - [UpdateScoreRequestParsed](docs/UpdateScoreRequestParsed.md)

## Documentation For Authorization


## password

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - ****: 

