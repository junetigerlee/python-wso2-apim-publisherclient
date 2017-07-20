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
from wso2_apim_publisherclient.models.wsdl import Wsdl


class TestWsdl(unittest.TestCase):
    """ Wsdl unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWsdl(self):
        """
        Test Wsdl
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = wso2_apim_publisherclient.models.wsdl.Wsdl()
        pass


if __name__ == '__main__':
    unittest.main()
