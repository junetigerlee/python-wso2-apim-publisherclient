# Tier3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**tier_level** | **str** |  | [optional] 
**attributes** | **dict(str, str)** | Custom attributes added to the tier policy  | [optional] 
**request_count** | **int** | Maximum number of requests which can be sent within a provided unit time  | 
**unit_time** | **int** |  | 
**time_unit** | **str** |  | [optional] 
**tier_plan** | **str** | This attribute declares whether this tier is available under commercial or free  | 
**stop_on_quota_reach** | **bool** | By making this attribute to false, you are capabale of sending requests even if the request count exceeded within a unit time  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


