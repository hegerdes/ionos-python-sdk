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


class KubernetesNodePoolLan(object):
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
        'id': 'int',
        'dhcp': 'bool',
        'routes': 'list[KubernetesNodePoolLanRoutes]',
    }

    attribute_map = {
        'id': 'id',
        'dhcp': 'dhcp',
        'routes': 'routes',
    }

    def __init__(self, id=None, dhcp=None, routes=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesNodePoolLan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._dhcp = None
        self._routes = None
        self.discriminator = None

        self.id = id
        if dhcp is not None:
            self.dhcp = dhcp
        if routes is not None:
            self.routes = routes

    @property
    def id(self):
        """Gets the id of this KubernetesNodePoolLan.  # noqa: E501

        The LAN ID of an existing LAN at the related datacenter  # noqa: E501

        :return: The id of this KubernetesNodePoolLan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KubernetesNodePoolLan.

        The LAN ID of an existing LAN at the related datacenter  # noqa: E501

        :param id: The id of this KubernetesNodePoolLan.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def dhcp(self):
        """Gets the dhcp of this KubernetesNodePoolLan.  # noqa: E501

        Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP  # noqa: E501

        :return: The dhcp of this KubernetesNodePoolLan.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this KubernetesNodePoolLan.

        Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP  # noqa: E501

        :param dhcp: The dhcp of this KubernetesNodePoolLan.  # noqa: E501
        :type dhcp: bool
        """

        self._dhcp = dhcp

    @property
    def routes(self):
        """Gets the routes of this KubernetesNodePoolLan.  # noqa: E501

        array of additional LANs attached to worker nodes  # noqa: E501

        :return: The routes of this KubernetesNodePoolLan.  # noqa: E501
        :rtype: list[KubernetesNodePoolLanRoutes]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this KubernetesNodePoolLan.

        array of additional LANs attached to worker nodes  # noqa: E501

        :param routes: The routes of this KubernetesNodePoolLan.  # noqa: E501
        :type routes: list[KubernetesNodePoolLanRoutes]
        """

        self._routes = routes

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
        if not isinstance(other, KubernetesNodePoolLan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesNodePoolLan):
            return True

        return self.to_dict() != other.to_dict()
