# coding: utf-8

"""
    WSO2 API Manager - Publisher API

    This specifies a **RESTful API** for WSO2 **API Manager** - Publisher.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.publisher/src/main/resources/publisher-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import wso2_apim_publisherclient
from wso2_apim_publisherclient.rest import ApiException
from wso2_apim_publisherclient.apis.document_individual_api import DocumentIndividualApi


class TestDocumentIndividualApi(unittest.TestCase):
    """ DocumentIndividualApi unit test stubs """

    def setUp(self):
        self.api = wso2_apim_publisherclient.apis.document_individual_api.DocumentIndividualApi()

    def tearDown(self):
        pass

    def test_apis_api_id_documents_document_id_content_get(self):
        """
        Test case for apis_api_id_documents_document_id_content_get

        Get the content of an API document
        """
        pass

    def test_apis_api_id_documents_document_id_content_post(self):
        """
        Test case for apis_api_id_documents_document_id_content_post

        Upload the content of an API document
        """
        pass

    def test_apis_api_id_documents_document_id_delete(self):
        """
        Test case for apis_api_id_documents_document_id_delete

        Delete a document of an API
        """
        pass

    def test_apis_api_id_documents_document_id_get(self):
        """
        Test case for apis_api_id_documents_document_id_get

        Get a document of an API
        """
        pass

    def test_apis_api_id_documents_document_id_put(self):
        """
        Test case for apis_api_id_documents_document_id_put

        Update a document of an API
        """
        pass


if __name__ == '__main__':
    unittest.main()
