# coding: utf-8

"""
    WSO2 API Manager - Publisher API

    This specifies a **RESTful API** for WSO2 **API Manager** - Publisher.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.publisher/src/main/resources/publisher-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SubscriptionIndividualApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def subscriptions_block_subscription_post(self, subscription_id, block_state, **kwargs):
        """
        Block a subscription
        This operation can be used to block a subscription. Along with the request, `blockState` must be specified as a query parameter.  1. `BLOCKED` : Subscription is completely blocked for both Production and Sandbox environments. 2. `PROD_ONLY_BLOCKED` : Subscription is blocked for Production environment only. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_block_subscription_post(subscription_id, block_state, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: Subscription Id  (required)
        :param str block_state: Subscription block state.  (required)
        :param str if_match: Validator for conditional requests; based on ETag. 
        :param str if_unmodified_since: Validator for conditional requests; based on Last Modified header. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.subscriptions_block_subscription_post_with_http_info(subscription_id, block_state, **kwargs)
        else:
            (data) = self.subscriptions_block_subscription_post_with_http_info(subscription_id, block_state, **kwargs)
            return data

    def subscriptions_block_subscription_post_with_http_info(self, subscription_id, block_state, **kwargs):
        """
        Block a subscription
        This operation can be used to block a subscription. Along with the request, `blockState` must be specified as a query parameter.  1. `BLOCKED` : Subscription is completely blocked for both Production and Sandbox environments. 2. `PROD_ONLY_BLOCKED` : Subscription is blocked for Production environment only. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_block_subscription_post_with_http_info(subscription_id, block_state, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: Subscription Id  (required)
        :param str block_state: Subscription block state.  (required)
        :param str if_match: Validator for conditional requests; based on ETag. 
        :param str if_unmodified_since: Validator for conditional requests; based on Last Modified header. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'block_state', 'if_match', 'if_unmodified_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_block_subscription_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `subscriptions_block_subscription_post`")
        # verify the required parameter 'block_state' is set
        if ('block_state' not in params) or (params['block_state'] is None):
            raise ValueError("Missing the required parameter `block_state` when calling `subscriptions_block_subscription_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subscription_id' in params:
            query_params.append(('subscriptionId', params['subscription_id']))
        if 'block_state' in params:
            query_params.append(('blockState', params['block_state']))

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']
        if 'if_unmodified_since' in params:
            header_params['If-Unmodified-Since'] = params['if_unmodified_since']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/subscriptions/block-subscription', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def subscriptions_subscription_id_get(self, subscription_id, **kwargs):
        """
        Get details of a subscription
        This operation can be used to get details of a single subscription. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_subscription_id_get(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: Subscription Id  (required)
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :param str if_modified_since: Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource. 
        :return: Subscription1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.subscriptions_subscription_id_get_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.subscriptions_subscription_id_get_with_http_info(subscription_id, **kwargs)
            return data

    def subscriptions_subscription_id_get_with_http_info(self, subscription_id, **kwargs):
        """
        Get details of a subscription
        This operation can be used to get details of a single subscription. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_subscription_id_get_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: Subscription Id  (required)
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :param str if_modified_since: Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource. 
        :return: Subscription1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'accept', 'if_none_match', 'if_modified_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_subscription_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `subscriptions_subscription_id_get`")


        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']

        query_params = []

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']
        if 'if_modified_since' in params:
            header_params['If-Modified-Since'] = params['if_modified_since']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/subscriptions/{subscriptionId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Subscription1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def subscriptions_unblock_subscription_post(self, subscription_id, **kwargs):
        """
        Unblock a Subscription
        This operation can be used to unblock a subscription specifying the subscription Id. The subscription will be fully unblocked after performing this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_unblock_subscription_post(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: Subscription Id  (required)
        :param str if_match: Validator for conditional requests; based on ETag. 
        :param str if_unmodified_since: Validator for conditional requests; based on Last Modified header. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.subscriptions_unblock_subscription_post_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.subscriptions_unblock_subscription_post_with_http_info(subscription_id, **kwargs)
            return data

    def subscriptions_unblock_subscription_post_with_http_info(self, subscription_id, **kwargs):
        """
        Unblock a Subscription
        This operation can be used to unblock a subscription specifying the subscription Id. The subscription will be fully unblocked after performing this operation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_unblock_subscription_post_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_id: Subscription Id  (required)
        :param str if_match: Validator for conditional requests; based on ETag. 
        :param str if_unmodified_since: Validator for conditional requests; based on Last Modified header. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'if_match', 'if_unmodified_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_unblock_subscription_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `subscriptions_unblock_subscription_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subscription_id' in params:
            query_params.append(('subscriptionId', params['subscription_id']))

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']
        if 'if_unmodified_since' in params:
            header_params['If-Unmodified-Since'] = params['if_unmodified_since']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/subscriptions/unblock-subscription', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
