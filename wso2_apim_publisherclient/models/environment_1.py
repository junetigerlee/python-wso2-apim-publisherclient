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


class Environment1(object):
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
        'name': 'str',
        'type': 'str',
        'server_url': 'str',
        'show_in_api_console': 'bool',
        'endpoints': 'EnvironmentEndpoints'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'server_url': 'serverUrl',
        'show_in_api_console': 'showInApiConsole',
        'endpoints': 'endpoints'
    }

    def __init__(self, name=None, type=None, server_url=None, show_in_api_console=None, endpoints=None):
        """
        Environment1 - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._server_url = None
        self._show_in_api_console = None
        self._endpoints = None

        self.name = name
        self.type = type
        self.server_url = server_url
        self.show_in_api_console = show_in_api_console
        if endpoints is not None:
          self.endpoints = endpoints

    @property
    def name(self):
        """
        Gets the name of this Environment1.

        :return: The name of this Environment1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Environment1.

        :param name: The name of this Environment1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Environment1.

        :return: The type of this Environment1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Environment1.

        :param type: The type of this Environment1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def server_url(self):
        """
        Gets the server_url of this Environment1.

        :return: The server_url of this Environment1.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """
        Sets the server_url of this Environment1.

        :param server_url: The server_url of this Environment1.
        :type: str
        """
        if server_url is None:
            raise ValueError("Invalid value for `server_url`, must not be `None`")

        self._server_url = server_url

    @property
    def show_in_api_console(self):
        """
        Gets the show_in_api_console of this Environment1.

        :return: The show_in_api_console of this Environment1.
        :rtype: bool
        """
        return self._show_in_api_console

    @show_in_api_console.setter
    def show_in_api_console(self, show_in_api_console):
        """
        Sets the show_in_api_console of this Environment1.

        :param show_in_api_console: The show_in_api_console of this Environment1.
        :type: bool
        """
        if show_in_api_console is None:
            raise ValueError("Invalid value for `show_in_api_console`, must not be `None`")

        self._show_in_api_console = show_in_api_console

    @property
    def endpoints(self):
        """
        Gets the endpoints of this Environment1.

        :return: The endpoints of this Environment1.
        :rtype: EnvironmentEndpoints
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this Environment1.

        :param endpoints: The endpoints of this Environment1.
        :type: EnvironmentEndpoints
        """

        self._endpoints = endpoints

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
        if not isinstance(other, Environment1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
