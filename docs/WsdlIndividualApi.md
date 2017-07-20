# swagger_client.WsdlIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_api_id_wsdl_get**](WsdlIndividualApi.md#apis_api_id_wsdl_get) | **GET** /apis/{apiId}/wsdl | Get a wsdl correspond to a API
[**apis_api_id_wsdl_post**](WsdlIndividualApi.md#apis_api_id_wsdl_post) | **POST** /apis/{apiId}/wsdl | Add wsdl


# **apis_api_id_wsdl_get**
> Wsdl1 apis_api_id_wsdl_get(api_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get a wsdl correspond to a API

This operation can be used to retrieve a particular global mediation policy. 

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
api_instance = swagger_client.WsdlIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get a wsdl correspond to a API
    api_response = api_instance.apis_api_id_wsdl_get(api_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WsdlIndividualApi->apis_api_id_wsdl_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Wsdl1**](Wsdl1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_api_id_wsdl_post**
> apis_api_id_wsdl_post(api_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Add wsdl

This operation can be used to add a wsdl to an existing API. wsdl definition to be updated is passed as a form data parameter `wsdlDefinition`. 

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
api_instance = swagger_client.WsdlIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
body = swagger_client.Wsdl2() # Wsdl2 | DTO including WSDL definition that needs to be added 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Add wsdl
    api_instance.apis_api_id_wsdl_post(api_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling WsdlIndividualApi->apis_api_id_wsdl_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **body** | [**Wsdl2**](Wsdl2.md)| DTO including WSDL definition that needs to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

