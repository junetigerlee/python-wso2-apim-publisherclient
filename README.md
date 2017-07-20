# python-wso2-apim-publisherclient
This specifies a **RESTful API** for WSO2 **API Manager** - Publisher.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.publisher/src/main/resources/publisher-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.11.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://wso2.com/products/api-manager/](http://wso2.com/products/api-manager/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import wso2_apim_publisherclient 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wso2_apim_publisherclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import wso2_apim_publisherclient
from wso2_apim_publisherclient.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
wso2_apim_publisherclient.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = wso2_apim_publisherclient.APICollectionApi()
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
query = 'query_example' # str | **Search condition**.  You can search in attributes by using an **\"<attribute>:\"** modifier.  Eg. \"provider:wso2\" will match an API if the provider of the API is exactly \"wso2\".  Additionally you can use wildcards.  Eg. \"provider:wso2*\" will match an API if the provider of the API starts with \"wso2\".  Supported attribute modifiers are [**version, context, status, description, subcontext, doc, provider**]  If no advanced attribute modifier has been specified, search will match the given query string against API Name.  (optional)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try:
    # Retrieve/Search APIs  
    api_response = api_instance.apis_get(limit=limit, offset=offset, query=query, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APICollectionApi->apis_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apis.wso2.com/api/am/publisher/v0.11*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APICollectionApi* | [**apis_get**](docs/APICollectionApi.md#apis_get) | **GET** /apis | Retrieve/Search APIs  
*APICollectionApi* | [**apis_post**](docs/APICollectionApi.md#apis_post) | **POST** /apis | Create a new API
*APICollectionApi* | [**policies_mediation_get**](docs/APICollectionApi.md#policies_mediation_get) | **GET** /policies/mediation | Retrieve/Search APIs 
*APIIndividualApi* | [**apis_api_id_delete**](docs/APIIndividualApi.md#apis_api_id_delete) | **DELETE** /apis/{apiId} | Delete an API
*APIIndividualApi* | [**apis_api_id_get**](docs/APIIndividualApi.md#apis_api_id_get) | **GET** /apis/{apiId} | Get details of an API
*APIIndividualApi* | [**apis_api_id_policies_mediation_get**](docs/APIIndividualApi.md#apis_api_id_policies_mediation_get) | **GET** /apis/{apiId}/policies/mediation | Retrieve/Search APIs 
*APIIndividualApi* | [**apis_api_id_policies_mediation_mediation_policy_id_delete**](docs/APIIndividualApi.md#apis_api_id_policies_mediation_mediation_policy_id_delete) | **DELETE** /apis/{apiId}/policies/mediation/{mediationPolicyId} | Delete an API
*APIIndividualApi* | [**apis_api_id_policies_mediation_mediation_policy_id_get**](docs/APIIndividualApi.md#apis_api_id_policies_mediation_mediation_policy_id_get) | **GET** /apis/{apiId}/policies/mediation/{mediationPolicyId} | Get a global mediation squence
*APIIndividualApi* | [**apis_api_id_policies_mediation_mediation_policy_id_put**](docs/APIIndividualApi.md#apis_api_id_policies_mediation_mediation_policy_id_put) | **PUT** /apis/{apiId}/policies/mediation/{mediationPolicyId} | Update an mediation policy
*APIIndividualApi* | [**apis_api_id_policies_mediation_post**](docs/APIIndividualApi.md#apis_api_id_policies_mediation_post) | **POST** /apis/{apiId}/policies/mediation | Upload a global mediation policy
*APIIndividualApi* | [**apis_api_id_put**](docs/APIIndividualApi.md#apis_api_id_put) | **PUT** /apis/{apiId} | Update an API
*APIIndividualApi* | [**apis_api_id_swagger_get**](docs/APIIndividualApi.md#apis_api_id_swagger_get) | **GET** /apis/{apiId}/swagger | Get swagger definition
*APIIndividualApi* | [**apis_api_id_swagger_put**](docs/APIIndividualApi.md#apis_api_id_swagger_put) | **PUT** /apis/{apiId}/swagger | Update swagger definition
*APIIndividualApi* | [**apis_api_id_thumbnail_get**](docs/APIIndividualApi.md#apis_api_id_thumbnail_get) | **GET** /apis/{apiId}/thumbnail | Get thumbnail image
*APIIndividualApi* | [**apis_api_id_thumbnail_post**](docs/APIIndividualApi.md#apis_api_id_thumbnail_post) | **POST** /apis/{apiId}/thumbnail | Upload a thumbnail image
*APIIndividualApi* | [**apis_change_lifecycle_post**](docs/APIIndividualApi.md#apis_change_lifecycle_post) | **POST** /apis/change-lifecycle | Change API Status
*APIIndividualApi* | [**apis_copy_api_post**](docs/APIIndividualApi.md#apis_copy_api_post) | **POST** /apis/copy-api | Create a new API version
*ApplicationIndividualApi* | [**applications_application_id_get**](docs/ApplicationIndividualApi.md#applications_application_id_get) | **GET** /applications/{applicationId} | Get details of an application
*DocumentCollectionApi* | [**apis_api_id_documents_get**](docs/DocumentCollectionApi.md#apis_api_id_documents_get) | **GET** /apis/{apiId}/documents | Get a list of documents of an API
*DocumentCollectionApi* | [**apis_api_id_documents_post**](docs/DocumentCollectionApi.md#apis_api_id_documents_post) | **POST** /apis/{apiId}/documents | Add a new document to an API
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_content_get**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_content_get) | **GET** /apis/{apiId}/documents/{documentId}/content | Get the content of an API document
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_content_post**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_content_post) | **POST** /apis/{apiId}/documents/{documentId}/content | Upload the content of an API document
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_delete**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_delete) | **DELETE** /apis/{apiId}/documents/{documentId} | Delete a document of an API
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_get**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_get) | **GET** /apis/{apiId}/documents/{documentId} | Get a document of an API
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_put**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_put) | **PUT** /apis/{apiId}/documents/{documentId} | Update a document of an API
*EnvironmentCollectionApi* | [**environments_get**](docs/EnvironmentCollectionApi.md#environments_get) | **GET** /environments | Get all gateway environments
*SubscriptionCollectionApi* | [**subscriptions_get**](docs/SubscriptionCollectionApi.md#subscriptions_get) | **GET** /subscriptions | Get all Subscriptions
*SubscriptionIndividualApi* | [**subscriptions_block_subscription_post**](docs/SubscriptionIndividualApi.md#subscriptions_block_subscription_post) | **POST** /subscriptions/block-subscription | Block a subscription
*SubscriptionIndividualApi* | [**subscriptions_subscription_id_get**](docs/SubscriptionIndividualApi.md#subscriptions_subscription_id_get) | **GET** /subscriptions/{subscriptionId} | Get details of a subscription
*SubscriptionIndividualApi* | [**subscriptions_unblock_subscription_post**](docs/SubscriptionIndividualApi.md#subscriptions_unblock_subscription_post) | **POST** /subscriptions/unblock-subscription | Unblock a Subscription
*ThrottlingTierCollectionApi* | [**tiers_tier_level_get**](docs/ThrottlingTierCollectionApi.md#tiers_tier_level_get) | **GET** /tiers/{tierLevel} | Get all tiers
*ThrottlingTierCollectionApi* | [**tiers_tier_level_post**](docs/ThrottlingTierCollectionApi.md#tiers_tier_level_post) | **POST** /tiers/{tierLevel} | Create a Tier
*ThrottlingTierIndividualApi* | [**tiers_tier_level_tier_name_delete**](docs/ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_delete) | **DELETE** /tiers/{tierLevel}/{tierName} | Delete a Tier
*ThrottlingTierIndividualApi* | [**tiers_tier_level_tier_name_get**](docs/ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_get) | **GET** /tiers/{tierLevel}/{tierName} | Get details of a tier
*ThrottlingTierIndividualApi* | [**tiers_tier_level_tier_name_put**](docs/ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_put) | **PUT** /tiers/{tierLevel}/{tierName} | Update a Tier
*ThrottlingTierIndividualApi* | [**tiers_update_permission_post**](docs/ThrottlingTierIndividualApi.md#tiers_update_permission_post) | **POST** /tiers/update-permission | Update tier permission
*WorkflowsIndividualApi* | [**workflows_update_workflow_status_post**](docs/WorkflowsIndividualApi.md#workflows_update_workflow_status_post) | **POST** /workflows/update-workflow-status | Update workflow status
*WsdlIndividualApi* | [**apis_api_id_wsdl_get**](docs/WsdlIndividualApi.md#apis_api_id_wsdl_get) | **GET** /apis/{apiId}/wsdl | Get a wsdl correspond to a API
*WsdlIndividualApi* | [**apis_api_id_wsdl_post**](docs/WsdlIndividualApi.md#apis_api_id_wsdl_post) | **POST** /apis/{apiId}/wsdl | Add wsdl


## Documentation For Models

 - [API](docs/API.md)
 - [APIInfo](docs/APIInfo.md)
 - [APIInfoObjectWithBasicAPIDetails_](docs/APIInfoObjectWithBasicAPIDetails_.md)
 - [APIList](docs/APIList.md)
 - [APIObject](docs/APIObject.md)
 - [APIObject1](docs/APIObject1.md)
 - [APIObject2](docs/APIObject2.md)
 - [ApisBusinessInformation](docs/ApisBusinessInformation.md)
 - [ApisCorsConfiguration](docs/ApisCorsConfiguration.md)
 - [ApisEndpointSecurity](docs/ApisEndpointSecurity.md)
 - [ApisMaxTps](docs/ApisMaxTps.md)
 - [Application](docs/Application.md)
 - [Application1](docs/Application1.md)
 - [DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_](docs/DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.md)
 - [Document](docs/Document.md)
 - [Document1](docs/Document1.md)
 - [Document2](docs/Document2.md)
 - [Document3](docs/Document3.md)
 - [DocumentList](docs/DocumentList.md)
 - [Environment](docs/Environment.md)
 - [Environment1](docs/Environment1.md)
 - [EnvironmentEndpoints](docs/EnvironmentEndpoints.md)
 - [EnvironmentList](docs/EnvironmentList.md)
 - [Error](docs/Error.md)
 - [ErrorListItem](docs/ErrorListItem.md)
 - [ErrorObjectReturnedWith4XXHTTPStatus](docs/ErrorObjectReturnedWith4XXHTTPStatus.md)
 - [FileInfo](docs/FileInfo.md)
 - [FileInformationIncludingMetaData](docs/FileInformationIncludingMetaData.md)
 - [Mediation](docs/Mediation.md)
 - [Mediation1](docs/Mediation1.md)
 - [Mediation2](docs/Mediation2.md)
 - [Mediation3](docs/Mediation3.md)
 - [MediationInfo](docs/MediationInfo.md)
 - [MediationInfo1](docs/MediationInfo1.md)
 - [MediationList](docs/MediationList.md)
 - [Sequence](docs/Sequence.md)
 - [Sequence1](docs/Sequence1.md)
 - [Subscription](docs/Subscription.md)
 - [Subscription1](docs/Subscription1.md)
 - [SubscriptionList](docs/SubscriptionList.md)
 - [Tier](docs/Tier.md)
 - [Tier1](docs/Tier1.md)
 - [Tier2](docs/Tier2.md)
 - [Tier3](docs/Tier3.md)
 - [TierList](docs/TierList.md)
 - [TierPermission](docs/TierPermission.md)
 - [Workflow](docs/Workflow.md)
 - [Workflow1](docs/Workflow1.md)
 - [Wsdl](docs/Wsdl.md)
 - [Wsdl1](docs/Wsdl1.md)
 - [Wsdl2](docs/Wsdl2.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: password
- **Token URL**: https://apis.wso2.com/oauth2/token
- **Scopes**: 
 - **apim:api_view**: apim:api_view
 - **apim:api_create**: apim:api_create
 - **apim:api_publish**: apim:api_publish
 - **apim:tier_view**: apim:tier_view
 - **apim:tier_manage**: apim:tier_manage
 - **apim:subscription_view**: apim:subscription_view
 - **apim:subscription_block**: apim:subscription_block
 - **apim:mediation_policy_view**: apim:mediation_policy_view
 - **apim:api_workflow**: apim:api_workflow


## Author

architecture@wso2.com

