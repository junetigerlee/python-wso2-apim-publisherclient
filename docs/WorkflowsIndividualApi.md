# swagger_client.WorkflowsIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflows_update_workflow_status_post**](WorkflowsIndividualApi.md#workflows_update_workflow_status_post) | **POST** /workflows/update-workflow-status | Update workflow status


# **workflows_update_workflow_status_post**
> Workflow1 workflows_update_workflow_status_post(workflow_reference_id, body)

Update workflow status

This operation can be used to approve or reject a workflow task. . 

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
api_instance = swagger_client.WorkflowsIndividualApi()
workflow_reference_id = 'workflow_reference_id_example' # str | Workflow reference id 
body = swagger_client.Workflow() # Workflow | Workflow event that need to be updated 

try: 
    # Update workflow status
    api_response = api_instance.workflows_update_workflow_status_post(workflow_reference_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsIndividualApi->workflows_update_workflow_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_reference_id** | **str**| Workflow reference id  | 
 **body** | [**Workflow**](Workflow.md)| Workflow event that need to be updated  | 

### Return type

[**Workflow1**](Workflow1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

