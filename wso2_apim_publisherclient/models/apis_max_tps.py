# coding: utf-8

"""
    WSO2 API Manager - Publisher API

    This specifies a **RESTful API** for WSO2 **API Manager** - Publisher.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.publisher/src/main/resources/publisher-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApisMaxTps(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'production': 'int',
        'sandbox': 'int'
    }

    attribute_map = {
        'production': 'production',
        'sandbox': 'sandbox'
    }

    def __init__(self, production=None, sandbox=None):
        """
        ApisMaxTps - a model defined in Swagger
        """

        self._production = None
        self._sandbox = None

        if production is not None:
          self.production = production
        if sandbox is not None:
          self.sandbox = sandbox

    @property
    def production(self):
        """
        Gets the production of this ApisMaxTps.

        :return: The production of this ApisMaxTps.
        :rtype: int
        """
        return self._production

    @production.setter
    def production(self, production):
        """
        Sets the production of this ApisMaxTps.

        :param production: The production of this ApisMaxTps.
        :type: int
        """

        self._production = production

    @property
    def sandbox(self):
        """
        Gets the sandbox of this ApisMaxTps.

        :return: The sandbox of this ApisMaxTps.
        :rtype: int
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """
        Sets the sandbox of this ApisMaxTps.

        :param sandbox: The sandbox of this ApisMaxTps.
        :type: int
        """

        self._sandbox = sandbox

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApisMaxTps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
