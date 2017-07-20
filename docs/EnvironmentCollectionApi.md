# swagger_client.EnvironmentCollectionApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environments_get**](EnvironmentCollectionApi.md#environments_get) | **GET** /environments | Get all gateway environments


# **environments_get**
> EnvironmentList environments_get(api_id=api_id)

Get all gateway environments

This operation can be used to retrieve the list of gateway environments available. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.EnvironmentCollectionApi()
api_id = 'api_id_example' # str | Will return environment list for the provided API.  (optional)

try: 
    # Get all gateway environments
    api_response = api_instance.environments_get(api_id=api_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentCollectionApi->environments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| Will return environment list for the provided API.  | [optional] 

### Return type

[**EnvironmentList**](EnvironmentList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

