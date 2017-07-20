# swagger_client.ThrottlingTierIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_tier_level_tier_name_delete**](ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_delete) | **DELETE** /tiers/{tierLevel}/{tierName} | Delete a Tier
[**tiers_tier_level_tier_name_get**](ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_get) | **GET** /tiers/{tierLevel}/{tierName} | Get details of a tier
[**tiers_tier_level_tier_name_put**](ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_put) | **PUT** /tiers/{tierLevel}/{tierName} | Update a Tier
[**tiers_update_permission_post**](ThrottlingTierIndividualApi.md#tiers_update_permission_post) | **POST** /tiers/update-permission | Update tier permission


# **tiers_tier_level_tier_name_delete**
> tiers_tier_level_tier_name_delete(tier_name, tier_level, if_match=if_match, if_unmodified_since=if_unmodified_since)

Delete a Tier

This operation can be used to delete an existing tier. The only supported tier level is `api` tiers. `DELETE https://127.0.0.1:9443/api/am/publisher/v0.11/tiers/api/Low`  **IMPORTANT:** * This is only effective when Advanced Throttling is disabled in the Server. If enabled, we need to use Admin REST API for throttling tiers modification related operations. 

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
api_instance = swagger_client.ThrottlingTierIndividualApi()
tier_name = 'tier_name_example' # str | Tier name 
tier_level = 'tier_level_example' # str | List API or Application or Resource type tiers. 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Delete a Tier
    api_instance.tiers_tier_level_tier_name_delete(tier_name, tier_level, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling ThrottlingTierIndividualApi->tiers_tier_level_tier_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_name** | **str**| Tier name  | 
 **tier_level** | **str**| List API or Application or Resource type tiers.  | 
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

# **tiers_tier_level_tier_name_get**
> Tier1 tiers_tier_level_tier_name_get(tier_name, tier_level, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get details of a tier

This operation can be used to retrieve details of a single tier by specifying the tier level and tier name. 

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
api_instance = swagger_client.ThrottlingTierIndividualApi()
tier_name = 'tier_name_example' # str | Tier name 
tier_level = 'tier_level_example' # str | List API or Application or Resource type tiers. 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get details of a tier
    api_response = api_instance.tiers_tier_level_tier_name_get(tier_name, tier_level, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierIndividualApi->tiers_tier_level_tier_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_name** | **str**| Tier name  | 
 **tier_level** | **str**| List API or Application or Resource type tiers.  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Tier1**](Tier1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_tier_level_tier_name_put**
> Tier1 tiers_tier_level_tier_name_put(tier_name, body, tier_level, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update a Tier

This operation can be used to update an existing tier. The only supported tier level is `api` tiers. `PUT https://127.0.0.1:9443/api/am/publisher/v0.11/tiers/api/Low`  **IMPORTANT:** * This is only effective when Advanced Throttling is disabled in the Server. If enabled, we need to use Admin REST API for throttling tiers modification related operations. 

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
api_instance = swagger_client.ThrottlingTierIndividualApi()
tier_name = 'tier_name_example' # str | Tier name 
body = swagger_client.Tier3() # Tier3 | Tier object that needs to be modified 
tier_level = 'tier_level_example' # str | List API or Application or Resource type tiers. 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update a Tier
    api_response = api_instance.tiers_tier_level_tier_name_put(tier_name, body, tier_level, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierIndividualApi->tiers_tier_level_tier_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_name** | **str**| Tier name  | 
 **body** | [**Tier3**](Tier3.md)| Tier object that needs to be modified  | 
 **tier_level** | **str**| List API or Application or Resource type tiers.  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**Tier1**](Tier1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tiers_update_permission_post**
> list[Tier1] tiers_update_permission_post(tier_name, tier_level, if_match=if_match, if_unmodified_since=if_unmodified_since, permissions=permissions)

Update tier permission

This operation can be used to update tier permissions which controls access for the particular tier based on the subscribers' roles. 

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
api_instance = swagger_client.ThrottlingTierIndividualApi()
tier_name = 'tier_name_example' # str | Name of the tier 
tier_level = 'tier_level_example' # str | List API or Application or Resource type tiers. 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)
permissions = swagger_client.TierPermission() # TierPermission |  (optional)

try: 
    # Update tier permission
    api_response = api_instance.tiers_update_permission_post(tier_name, tier_level, if_match=if_match, if_unmodified_since=if_unmodified_since, permissions=permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierIndividualApi->tiers_update_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_name** | **str**| Name of the tier  | 
 **tier_level** | **str**| List API or Application or Resource type tiers.  | 
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 
 **permissions** | [**TierPermission**](TierPermission.md)|  | [optional] 

### Return type

[**list[Tier1]**](Tier1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

