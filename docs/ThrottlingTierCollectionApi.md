# swagger_client.ThrottlingTierCollectionApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_tier_level_get**](ThrottlingTierCollectionApi.md#tiers_tier_level_get) | **GET** /tiers/{tierLevel} | Get all tiers
[**tiers_tier_level_post**](ThrottlingTierCollectionApi.md#tiers_tier_level_post) | **POST** /tiers/{tierLevel} | Create a Tier


# **tiers_tier_level_get**
> TierList tiers_tier_level_get(tier_level, limit=limit, offset=offset, accept=accept, if_none_match=if_none_match)

Get all tiers

This operation can be used to list the available tiers for a given tier level. Tier level should be specified as a path parameter and should be one of `api`, `application` and `resource`. 

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
api_instance = swagger_client.ThrottlingTierCollectionApi()
tier_level = 'tier_level_example' # str | List API or Application or Resource type tiers. 
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try: 
    # Get all tiers
    api_response = api_instance.tiers_tier_level_get(tier_level, limit=limit, offset=offset, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierCollectionApi->tiers_tier_level_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_level** | **str**| List API or Application or Resource type tiers.  | 
 **limit** | **int**| Maximum size of resource array to return.  | [optional] [default to 25]
 **offset** | **int**| Starting point within the complete list of items qualified.  | [optional] [default to 0]
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 

### Return type

[**TierList**](TierList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_tier_level_post**
> Tier1 tiers_tier_level_post(body, tier_level, content_type)

Create a Tier

This operation can be used to create a new throttling tier. The only supported tier level is `api` tiers. `POST https://127.0.0.1:9443/api/am/publisher/v0.11/tiers/api`  **IMPORTANT:** * This is only effective when Advanced Throttling is disabled in the Server. If enabled, we need to use Admin REST API for throttling tiers modification related operations. 

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
api_instance = swagger_client.ThrottlingTierCollectionApi()
body = swagger_client.Tier2() # Tier2 | Tier object that should to be added 
tier_level = 'tier_level_example' # str | List API or Application or Resource type tiers. 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)

try: 
    # Create a Tier
    api_response = api_instance.tiers_tier_level_post(body, tier_level, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierCollectionApi->tiers_tier_level_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tier2**](Tier2.md)| Tier object that should to be added  | 
 **tier_level** | **str**| List API or Application or Resource type tiers.  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]

### Return type

[**Tier1**](Tier1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

