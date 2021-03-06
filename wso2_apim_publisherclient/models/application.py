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


class Application(object):
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
        'application_id': 'str',
        'name': 'str',
        'subscriber': 'str',
        'throttling_tier': 'str',
        'description': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'application_id': 'applicationId',
        'name': 'name',
        'subscriber': 'subscriber',
        'throttling_tier': 'throttlingTier',
        'description': 'description',
        'group_id': 'groupId'
    }

    def __init__(self, application_id=None, name=None, subscriber=None, throttling_tier=None, description=None, group_id=None):
        """
        Application - a model defined in Swagger
        """

        self._application_id = None
        self._name = None
        self._subscriber = None
        self._throttling_tier = None
        self._description = None
        self._group_id = None

        if application_id is not None:
          self.application_id = application_id
        self.name = name
        if subscriber is not None:
          self.subscriber = subscriber
        self.throttling_tier = throttling_tier
        if description is not None:
          self.description = description
        if group_id is not None:
          self.group_id = group_id

    @property
    def application_id(self):
        """
        Gets the application_id of this Application.

        :return: The application_id of this Application.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this Application.

        :param application_id: The application_id of this Application.
        :type: str
        """

        self._application_id = application_id

    @property
    def name(self):
        """
        Gets the name of this Application.

        :return: The name of this Application.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Application.

        :param name: The name of this Application.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def subscriber(self):
        """
        Gets the subscriber of this Application.

        :return: The subscriber of this Application.
        :rtype: str
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """
        Sets the subscriber of this Application.

        :param subscriber: The subscriber of this Application.
        :type: str
        """

        self._subscriber = subscriber

    @property
    def throttling_tier(self):
        """
        Gets the throttling_tier of this Application.

        :return: The throttling_tier of this Application.
        :rtype: str
        """
        return self._throttling_tier

    @throttling_tier.setter
    def throttling_tier(self, throttling_tier):
        """
        Sets the throttling_tier of this Application.

        :param throttling_tier: The throttling_tier of this Application.
        :type: str
        """
        if throttling_tier is None:
            raise ValueError("Invalid value for `throttling_tier`, must not be `None`")

        self._throttling_tier = throttling_tier

    @property
    def description(self):
        """
        Gets the description of this Application.

        :return: The description of this Application.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Application.

        :param description: The description of this Application.
        :type: str
        """

        self._description = description

    @property
    def group_id(self):
        """
        Gets the group_id of this Application.

        :return: The group_id of this Application.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Application.

        :param group_id: The group_id of this Application.
        :type: str
        """

        self._group_id = group_id

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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
