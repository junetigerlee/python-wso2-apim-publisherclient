# swagger_client.DocumentCollectionApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_api_id_documents_get**](DocumentCollectionApi.md#apis_api_id_documents_get) | **GET** /apis/{apiId}/documents | Get a list of documents of an API
[**apis_api_id_documents_post**](DocumentCollectionApi.md#apis_api_id_documents_post) | **POST** /apis/{apiId}/documents | Add a new document to an API


# **apis_api_id_documents_get**
> DocumentList apis_api_id_documents_get(api_id, limit=limit, offset=offset, accept=accept, if_none_match=if_none_match)

Get a list of documents of an API

This operation can be used to retrive a list of documents belonging to an API by providing the id of the API. 

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
api_instance = swagger_client.DocumentCollectionApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try: 
    # Get a list of documents of an API
    api_response = api_instance.apis_api_id_documents_get(api_id, limit=limit, offset=offset, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentCollectionApi->apis_api_id_documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **limit** | **int**| Maximum size of resource array to return.  | [optional] [default to 25]
 **offset** | **int**| Starting point within the complete list of items qualified.  | [optional] [default to 0]
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_api_id_documents_post**
> Document1 apis_api_id_documents_post(api_id, body, content_type)

Add a new document to an API

This operation can be used to add a new documentation to an API. This operation only adds the metadata of a document. To add the actual content we need to use **Upload the content of an API document ** API once we obtain a document Id by this operation. 

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
api_instance = swagger_client.DocumentCollectionApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
body = swagger_client.Document2() # Document2 | Document object that needs to be added 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)

try: 
    # Add a new document to an API
    api_response = api_instance.apis_api_id_documents_post(api_id, body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentCollectionApi->apis_api_id_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **body** | [**Document2**](Document2.md)| Document object that needs to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]

### Return type

[**Document1**](Document1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

