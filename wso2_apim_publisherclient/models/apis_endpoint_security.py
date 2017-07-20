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


class ApisEndpointSecurity(object):
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
        'type': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'type': 'type',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, type=None, username=None, password=None):
        """
        ApisEndpointSecurity - a model defined in Swagger
        """

        self._type = None
        self._username = None
        self._password = None

        if type is not None:
          self.type = type
        if username is not None:
          self.username = username
        if password is not None:
          self.password = password

    @property
    def type(self):
        """
        Gets the type of this ApisEndpointSecurity.

        :return: The type of this ApisEndpointSecurity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApisEndpointSecurity.

        :param type: The type of this ApisEndpointSecurity.
        :type: str
        """
        allowed_values = ["basic", "digest"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def username(self):
        """
        Gets the username of this ApisEndpointSecurity.

        :return: The username of this ApisEndpointSecurity.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ApisEndpointSecurity.

        :param username: The username of this ApisEndpointSecurity.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this ApisEndpointSecurity.

        :return: The password of this ApisEndpointSecurity.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ApisEndpointSecurity.

        :param password: The password of this ApisEndpointSecurity.
        :type: str
        """

        self._password = password

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
        if not isinstance(other, ApisEndpointSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
