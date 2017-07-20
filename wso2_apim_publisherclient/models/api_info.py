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


class APIInfo(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'context': 'str',
        'version': 'str',
        'provider': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'context': 'context',
        'version': 'version',
        'provider': 'provider',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, description=None, context=None, version=None, provider=None, status=None):
        """
        APIInfo - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._context = None
        self._version = None
        self._provider = None
        self._status = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if context is not None:
          self.context = context
        if version is not None:
          self.version = version
        if provider is not None:
          self.provider = provider
        if status is not None:
          self.status = status

    @property
    def id(self):
        """
        Gets the id of this APIInfo.

        :return: The id of this APIInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this APIInfo.

        :param id: The id of this APIInfo.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this APIInfo.

        :return: The name of this APIInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this APIInfo.

        :param name: The name of this APIInfo.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this APIInfo.

        :return: The description of this APIInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this APIInfo.

        :param description: The description of this APIInfo.
        :type: str
        """

        self._description = description

    @property
    def context(self):
        """
        Gets the context of this APIInfo.

        :return: The context of this APIInfo.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this APIInfo.

        :param context: The context of this APIInfo.
        :type: str
        """

        self._context = context

    @property
    def version(self):
        """
        Gets the version of this APIInfo.

        :return: The version of this APIInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this APIInfo.

        :param version: The version of this APIInfo.
        :type: str
        """

        self._version = version

    @property
    def provider(self):
        """
        Gets the provider of this APIInfo.
        If the provider value is not given, the user invoking the API will be used as the provider. 

        :return: The provider of this APIInfo.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this APIInfo.
        If the provider value is not given, the user invoking the API will be used as the provider. 

        :param provider: The provider of this APIInfo.
        :type: str
        """

        self._provider = provider

    @property
    def status(self):
        """
        Gets the status of this APIInfo.

        :return: The status of this APIInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this APIInfo.

        :param status: The status of this APIInfo.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, APIInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
