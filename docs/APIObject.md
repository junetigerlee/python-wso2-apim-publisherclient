# APIObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of the api registry artifact  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**context** | **str** |  | 
**version** | **str** |  | 
**provider** | **str** | If the provider value is not given user invoking the api will be used as the provider.  | [optional] 
**api_definition** | **str** | Swagger definition of the API which contains details about URI templates and scopes  | [optional] 
**wsdl_uri** | **str** | WSDL URL if the API is based on a WSDL endpoint  | [optional] 
**status** | **str** |  | [optional] 
**response_caching** | **str** |  | [optional] 
**cache_timeout** | **int** |  | [optional] 
**destination_stats_enabled** | **str** |  | [optional] 
**is_default_version** | **bool** |  | 
**type** | **str** |  | [default to 'HTTP']
**transport** | **list[str]** | Supported transports for the API (http and/or https).  | 
**tags** | **list[str]** |  | [optional] 
**tiers** | **list[str]** |  | 
**max_tps** | [**ApisMaxTps**](ApisMaxTps.md) |  | [optional] 
**thumbnail_uri** | **str** |  | [optional] 
**visibility** | **str** |  | 
**visible_roles** | **list[str]** |  | [optional] 
**visible_tenants** | **list[str]** |  | [optional] 
**endpoint_config** | **str** |  | 
**endpoint_security** | [**ApisEndpointSecurity**](ApisEndpointSecurity.md) |  | [optional] 
**gateway_environments** | **str** | Comma separated list of gateway environments.  | [optional] 
**sequences** | [**list[Sequence1]**](Sequence1.md) |  | [optional] 
**subscription_availability** | **str** |  | [optional] 
**subscription_available_tenants** | **list[str]** |  | [optional] 
**business_information** | [**ApisBusinessInformation**](ApisBusinessInformation.md) |  | [optional] 
**cors_configuration** | [**ApisCorsConfiguration**](ApisCorsConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


