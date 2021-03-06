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


class ApisBusinessInformation(object):
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
        'business_owner': 'str',
        'business_owner_email': 'str',
        'technical_owner': 'str',
        'technical_owner_email': 'str'
    }

    attribute_map = {
        'business_owner': 'businessOwner',
        'business_owner_email': 'businessOwnerEmail',
        'technical_owner': 'technicalOwner',
        'technical_owner_email': 'technicalOwnerEmail'
    }

    def __init__(self, business_owner=None, business_owner_email=None, technical_owner=None, technical_owner_email=None):
        """
        ApisBusinessInformation - a model defined in Swagger
        """

        self._business_owner = None
        self._business_owner_email = None
        self._technical_owner = None
        self._technical_owner_email = None

        if business_owner is not None:
          self.business_owner = business_owner
        if business_owner_email is not None:
          self.business_owner_email = business_owner_email
        if technical_owner is not None:
          self.technical_owner = technical_owner
        if technical_owner_email is not None:
          self.technical_owner_email = technical_owner_email

    @property
    def business_owner(self):
        """
        Gets the business_owner of this ApisBusinessInformation.

        :return: The business_owner of this ApisBusinessInformation.
        :rtype: str
        """
        return self._business_owner

    @business_owner.setter
    def business_owner(self, business_owner):
        """
        Sets the business_owner of this ApisBusinessInformation.

        :param business_owner: The business_owner of this ApisBusinessInformation.
        :type: str
        """

        self._business_owner = business_owner

    @property
    def business_owner_email(self):
        """
        Gets the business_owner_email of this ApisBusinessInformation.

        :return: The business_owner_email of this ApisBusinessInformation.
        :rtype: str
        """
        return self._business_owner_email

    @business_owner_email.setter
    def business_owner_email(self, business_owner_email):
        """
        Sets the business_owner_email of this ApisBusinessInformation.

        :param business_owner_email: The business_owner_email of this ApisBusinessInformation.
        :type: str
        """

        self._business_owner_email = business_owner_email

    @property
    def technical_owner(self):
        """
        Gets the technical_owner of this ApisBusinessInformation.

        :return: The technical_owner of this ApisBusinessInformation.
        :rtype: str
        """
        return self._technical_owner

    @technical_owner.setter
    def technical_owner(self, technical_owner):
        """
        Sets the technical_owner of this ApisBusinessInformation.

        :param technical_owner: The technical_owner of this ApisBusinessInformation.
        :type: str
        """

        self._technical_owner = technical_owner

    @property
    def technical_owner_email(self):
        """
        Gets the technical_owner_email of this ApisBusinessInformation.

        :return: The technical_owner_email of this ApisBusinessInformation.
        :rtype: str
        """
        return self._technical_owner_email

    @technical_owner_email.setter
    def technical_owner_email(self, technical_owner_email):
        """
        Sets the technical_owner_email of this ApisBusinessInformation.

        :param technical_owner_email: The technical_owner_email of this ApisBusinessInformation.
        :type: str
        """

        self._technical_owner_email = technical_owner_email

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
        if not isinstance(other, ApisBusinessInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
