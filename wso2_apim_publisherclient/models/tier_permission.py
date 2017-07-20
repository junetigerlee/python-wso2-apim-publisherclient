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


class TierPermission(object):
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
        'permission_type': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'permission_type': 'permissionType',
        'roles': 'roles'
    }

    def __init__(self, permission_type=None, roles=None):
        """
        TierPermission - a model defined in Swagger
        """

        self._permission_type = None
        self._roles = None

        self.permission_type = permission_type
        self.roles = roles

    @property
    def permission_type(self):
        """
        Gets the permission_type of this TierPermission.

        :return: The permission_type of this TierPermission.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """
        Sets the permission_type of this TierPermission.

        :param permission_type: The permission_type of this TierPermission.
        :type: str
        """
        if permission_type is None:
            raise ValueError("Invalid value for `permission_type`, must not be `None`")
        allowed_values = ["allow", "deny"]
        if permission_type not in allowed_values:
            raise ValueError(
                "Invalid value for `permission_type` ({0}), must be one of {1}"
                .format(permission_type, allowed_values)
            )

        self._permission_type = permission_type

    @property
    def roles(self):
        """
        Gets the roles of this TierPermission.

        :return: The roles of this TierPermission.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this TierPermission.

        :param roles: The roles of this TierPermission.
        :type: list[str]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")

        self._roles = roles

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
        if not isinstance(other, TierPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other