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


class TierList(object):
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
        'count': 'int',
        'next': 'str',
        'previous': 'str',
        'list': 'list[Tier1]'
    }

    attribute_map = {
        'count': 'count',
        'next': 'next',
        'previous': 'previous',
        'list': 'list'
    }

    def __init__(self, count=None, next=None, previous=None, list=None):
        """
        TierList - a model defined in Swagger
        """

        self._count = None
        self._next = None
        self._previous = None
        self._list = None

        if count is not None:
          self.count = count
        if next is not None:
          self.next = next
        if previous is not None:
          self.previous = previous
        if list is not None:
          self.list = list

    @property
    def count(self):
        """
        Gets the count of this TierList.
        Number of Tiers returned. 

        :return: The count of this TierList.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this TierList.
        Number of Tiers returned. 

        :param count: The count of this TierList.
        :type: int
        """

        self._count = count

    @property
    def next(self):
        """
        Gets the next of this TierList.
        Link to the next subset of resources qualified. Empty if no more resources are to be returned. 

        :return: The next of this TierList.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this TierList.
        Link to the next subset of resources qualified. Empty if no more resources are to be returned. 

        :param next: The next of this TierList.
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """
        Gets the previous of this TierList.
        Link to the previous subset of resources qualified. Empty if current subset is the first subset returned. 

        :return: The previous of this TierList.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this TierList.
        Link to the previous subset of resources qualified. Empty if current subset is the first subset returned. 

        :param previous: The previous of this TierList.
        :type: str
        """

        self._previous = previous

    @property
    def list(self):
        """
        Gets the list of this TierList.

        :return: The list of this TierList.
        :rtype: list[Tier1]
        """
        return self._list

    @list.setter
    def list(self, list):
        """
        Sets the list of this TierList.

        :param list: The list of this TierList.
        :type: list[Tier1]
        """

        self._list = list

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
        if not isinstance(other, TierList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
