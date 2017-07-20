# swagger_client.SubscriptionIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_block_subscription_post**](SubscriptionIndividualApi.md#subscriptions_block_subscription_post) | **POST** /subscriptions/block-subscription | Block a subscription
[**subscriptions_subscription_id_get**](SubscriptionIndividualApi.md#subscriptions_subscription_id_get) | **GET** /subscriptions/{subscriptionId} | Get details of a subscription
[**subscriptions_unblock_subscription_post**](SubscriptionIndividualApi.md#subscriptions_unblock_subscription_post) | **POST** /subscriptions/unblock-subscription | Unblock a Subscription


# **subscriptions_block_subscription_post**
> subscriptions_block_subscription_post(subscription_id, block_state, if_match=if_match, if_unmodified_since=if_unmodified_since)

Block a subscription

This operation can be used to block a subscription. Along with the request, `blockState` must be specified as a query parameter.  1. `BLOCKED` : Subscription is completely blocked for both Production and Sandbox environments. 2. `PROD_ONLY_BLOCKED` : Subscription is blocked for Production environment only. 

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
api_instance = swagger_client.SubscriptionIndividualApi()
subscription_id = 'subscription_id_example' # str | Subscription Id 
block_state = 'block_state_example' # str | Subscription block state. 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Block a subscription
    api_instance.subscriptions_block_subscription_post(subscription_id, block_state, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling SubscriptionIndividualApi->subscriptions_block_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id  | 
 **block_state** | **str**| Subscription block state.  | 
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

# **subscriptions_subscription_id_get**
> Subscription1 subscriptions_subscription_id_get(subscription_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get details of a subscription

This operation can be used to get details of a single subscription. 

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
api_instance = swagger_client.SubscriptionIndividualApi()
subscription_id = 'subscription_id_example' # str | Subscription Id 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get details of a subscription
    api_response = api_instance.subscriptions_subscription_id_get(subscription_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionIndividualApi->subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Subscription1**](Subscription1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_unblock_subscription_post**
> subscriptions_unblock_subscription_post(subscription_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Unblock a Subscription

This operation can be used to unblock a subscription specifying the subscription Id. The subscription will be fully unblocked after performing this operation. 

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
api_instance = swagger_client.SubscriptionIndividualApi()
subscription_id = 'subscription_id_example' # str | Subscription Id 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Unblock a Subscription
    api_instance.subscriptions_unblock_subscription_post(subscription_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling SubscriptionIndividualApi->subscriptions_unblock_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id  | 
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

