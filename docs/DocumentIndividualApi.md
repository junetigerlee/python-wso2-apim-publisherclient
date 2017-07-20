# swagger_client.DocumentIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apis_api_id_documents_document_id_content_get**](DocumentIndividualApi.md#apis_api_id_documents_document_id_content_get) | **GET** /apis/{apiId}/documents/{documentId}/content | Get the content of an API document
[**apis_api_id_documents_document_id_content_post**](DocumentIndividualApi.md#apis_api_id_documents_document_id_content_post) | **POST** /apis/{apiId}/documents/{documentId}/content | Upload the content of an API document
[**apis_api_id_documents_document_id_delete**](DocumentIndividualApi.md#apis_api_id_documents_document_id_delete) | **DELETE** /apis/{apiId}/documents/{documentId} | Delete a document of an API
[**apis_api_id_documents_document_id_get**](DocumentIndividualApi.md#apis_api_id_documents_document_id_get) | **GET** /apis/{apiId}/documents/{documentId} | Get a document of an API
[**apis_api_id_documents_document_id_put**](DocumentIndividualApi.md#apis_api_id_documents_document_id_put) | **PUT** /apis/{apiId}/documents/{documentId} | Update a document of an API


# **apis_api_id_documents_document_id_content_get**
> apis_api_id_documents_document_id_content_get(api_id, document_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get the content of an API document

This operation can be used to retrive the content of an API's document.  The document can be of 3 types. In each cases responses are different.  1. **Inline type**:    The content of the document will be retrieved in `text/plain` content type 2. **FILE type**:     The file will be downloaded with the related content type (eg. `application/pdf`) 3. **URL type**:     The client will recieve the URL of the document as the Location header with the response with - `303 See Other` 

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
api_instance = swagger_client.DocumentIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
document_id = 'document_id_example' # str | Document Identifier 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get the content of an API document
    api_instance.apis_api_id_documents_document_id_content_get(api_id, document_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
except ApiException as e:
    print("Exception when calling DocumentIndividualApi->apis_api_id_documents_document_id_content_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **document_id** | **str**| Document Identifier  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_api_id_documents_document_id_content_post**
> Document1 apis_api_id_documents_document_id_content_post(api_id, document_id, content_type, file=file, inline_content=inline_content, if_match=if_match, if_unmodified_since=if_unmodified_since)

Upload the content of an API document

Thid operation can be used to upload a file or add inline content to an API document.  **IMPORTANT:** * Either **file** or **inlineContent** form data parameters should be specified at one time. * Document's source type should be **FILE** in order to upload a file to the document using **file** parameter. * Document's source type should be **INLINE** in order to add inline content to the document using **inlineContent** parameter. 

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
api_instance = swagger_client.DocumentIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
document_id = 'document_id_example' # str | Document Identifier 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)
file = '/path/to/file.txt' # file | Document to upload (optional)
inline_content = 'inline_content_example' # str | Inline content of the document (optional)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Upload the content of an API document
    api_response = api_instance.apis_api_id_documents_document_id_content_post(api_id, document_id, content_type, file=file, inline_content=inline_content, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentIndividualApi->apis_api_id_documents_document_id_content_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **document_id** | **str**| Document Identifier  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]
 **file** | **file**| Document to upload | [optional] 
 **inline_content** | **str**| Inline content of the document | [optional] 
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**Document1**](Document1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_api_id_documents_document_id_delete**
> apis_api_id_documents_document_id_delete(api_id, document_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete a document of an API

This operation can be used to delete a document associated with an API. 

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
api_instance = swagger_client.DocumentIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
document_id = 'document_id_example' # str | Document Identifier 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete a document of an API
    api_instance.apis_api_id_documents_document_id_delete(api_id, document_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling DocumentIndividualApi->apis_api_id_documents_document_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **document_id** | **str**| Document Identifier  | 
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

# **apis_api_id_documents_document_id_get**
> Document1 apis_api_id_documents_document_id_get(api_id, document_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get a document of an API

This operation can be used to retrieve a particular document's metadata associated with an API. 

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
api_instance = swagger_client.DocumentIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
document_id = 'document_id_example' # str | Document Identifier 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get a document of an API
    api_response = api_instance.apis_api_id_documents_document_id_get(api_id, document_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentIndividualApi->apis_api_id_documents_document_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **document_id** | **str**| Document Identifier  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Document1**](Document1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apis_api_id_documents_document_id_put**
> Document1 apis_api_id_documents_document_id_put(api_id, document_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update a document of an API

This operation can be used to update metadata of an API's document. 

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
api_instance = swagger_client.DocumentIndividualApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**. 
document_id = 'document_id_example' # str | Document Identifier 
body = swagger_client.Document3() # Document3 | Document object that needs to be added 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update a document of an API
    api_response = api_instance.apis_api_id_documents_document_id_put(api_id, document_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentIndividualApi->apis_api_id_documents_document_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  | 
 **document_id** | **str**| Document Identifier  | 
 **body** | [**Document3**](Document3.md)| Document object that needs to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**Document1**](Document1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

