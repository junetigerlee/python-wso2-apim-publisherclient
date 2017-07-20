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


class Sequence1(object):
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
        'id': 'str',
        'shared': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'id': 'id',
        'shared': 'shared'
    }

    def __init__(self, name=None, type=None, id=None, shared=None):
        """
        Sequence1 - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._id = None
        self._shared = None

        self.name = name
        if type is not None:
          self.type = type
        if id is not None:
          self.id = id
        if shared is not None:
          self.shared = shared

    @property
    def name(self):
        """
        Gets the name of this Sequence1.

        :return: The name of this Sequence1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Sequence1.

        :param name: The name of this Sequence1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Sequence1.

        :return: The type of this Sequence1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Sequence1.

        :param type: The type of this Sequence1.
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this Sequence1.

        :return: The id of this Sequence1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sequence1.

        :param id: The id of this Sequence1.
        :type: str
        """

        self._id = id

    @property
    def shared(self):
        """
        Gets the shared of this Sequence1.

        :return: The shared of this Sequence1.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this Sequence1.

        :param shared: The shared of this Sequence1.
        :type: bool
        """

        self._shared = shared

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
        if not isinstance(other, Sequence1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
