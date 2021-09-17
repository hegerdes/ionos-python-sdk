# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class GroupShares(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'Type',
        'href': 'str',
        'items': 'list[GroupShare]',
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'href': 'href',
        'items': 'items',
    }

    def __init__(self, id=None, type=None, href=None, items=None, local_vars_configuration=None):  # noqa: E501
        """GroupShares - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._href = None
        self._items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if href is not None:
            self.href = href
        if items is not None:
            self.items = items

    @property
    def id(self):
        """Gets the id of this GroupShares.  # noqa: E501

        The resource's unique identifier  # noqa: E501

        :return: The id of this GroupShares.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupShares.

        The resource's unique identifier  # noqa: E501

        :param id: The id of this GroupShares.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GroupShares.  # noqa: E501

        Share representing groups and resource relationship  # noqa: E501

        :return: The type of this GroupShares.  # noqa: E501
        :rtype: Type
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupShares.

        Share representing groups and resource relationship  # noqa: E501

        :param type: The type of this GroupShares.  # noqa: E501
        :type type: Type
        """

        self._type = type

    @property
    def href(self):
        """Gets the href of this GroupShares.  # noqa: E501

        URL to the object representation (absolute path)  # noqa: E501

        :return: The href of this GroupShares.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this GroupShares.

        URL to the object representation (absolute path)  # noqa: E501

        :param href: The href of this GroupShares.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def items(self):
        """Gets the items of this GroupShares.  # noqa: E501

        Array of items in that collection  # noqa: E501

        :return: The items of this GroupShares.  # noqa: E501
        :rtype: list[GroupShare]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this GroupShares.

        Array of items in that collection  # noqa: E501

        :param items: The items of this GroupShares.  # noqa: E501
        :type items: list[GroupShare]
        """

        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupShares):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupShares):
            return True

        return self.to_dict() != other.to_dict()
