# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class NetworkLoadBalancerProperties(object):
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

        'name': 'str',

        'listener_lan': 'int',

        'ips': 'list[str]',

        'target_lan': 'int',

        'lb_private_ips': 'list[str]',
    }

    attribute_map = {

        'name': 'name',

        'listener_lan': 'listenerLan',

        'ips': 'ips',

        'target_lan': 'targetLan',

        'lb_private_ips': 'lbPrivateIps',
    }

    def __init__(self, name=None, listener_lan=None, ips=None, target_lan=None, lb_private_ips=None, local_vars_configuration=None):  # noqa: E501
        """NetworkLoadBalancerProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._listener_lan = None
        self._ips = None
        self._target_lan = None
        self._lb_private_ips = None
        self.discriminator = None

        self.name = name
        self.listener_lan = listener_lan
        if ips is not None:
            self.ips = ips
        self.target_lan = target_lan
        if lb_private_ips is not None:
            self.lb_private_ips = lb_private_ips


    @property
    def name(self):
        """Gets the name of this NetworkLoadBalancerProperties.  # noqa: E501

        The name of the Network Load Balancer.  # noqa: E501

        :return: The name of this NetworkLoadBalancerProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkLoadBalancerProperties.

        The name of the Network Load Balancer.  # noqa: E501

        :param name: The name of this NetworkLoadBalancerProperties.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def listener_lan(self):
        """Gets the listener_lan of this NetworkLoadBalancerProperties.  # noqa: E501

        ID of the listening LAN (inbound).  # noqa: E501

        :return: The listener_lan of this NetworkLoadBalancerProperties.  # noqa: E501
        :rtype: int
        """
        return self._listener_lan

    @listener_lan.setter
    def listener_lan(self, listener_lan):
        """Sets the listener_lan of this NetworkLoadBalancerProperties.

        ID of the listening LAN (inbound).  # noqa: E501

        :param listener_lan: The listener_lan of this NetworkLoadBalancerProperties.  # noqa: E501
        :type listener_lan: int
        """
        if self.local_vars_configuration.client_side_validation and listener_lan is None:  # noqa: E501
            raise ValueError("Invalid value for `listener_lan`, must not be `None`")  # noqa: E501

        self._listener_lan = listener_lan

    @property
    def ips(self):
        """Gets the ips of this NetworkLoadBalancerProperties.  # noqa: E501

        Collection of the Network Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan must be customer-reserved IPs for public Load Balancers, and private IPs for private Load Balancers.  # noqa: E501

        :return: The ips of this NetworkLoadBalancerProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this NetworkLoadBalancerProperties.

        Collection of the Network Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan must be customer-reserved IPs for public Load Balancers, and private IPs for private Load Balancers.  # noqa: E501

        :param ips: The ips of this NetworkLoadBalancerProperties.  # noqa: E501
        :type ips: list[str]
        """

        self._ips = ips

    @property
    def target_lan(self):
        """Gets the target_lan of this NetworkLoadBalancerProperties.  # noqa: E501

        ID of the balanced private target LAN (outbound).  # noqa: E501

        :return: The target_lan of this NetworkLoadBalancerProperties.  # noqa: E501
        :rtype: int
        """
        return self._target_lan

    @target_lan.setter
    def target_lan(self, target_lan):
        """Sets the target_lan of this NetworkLoadBalancerProperties.

        ID of the balanced private target LAN (outbound).  # noqa: E501

        :param target_lan: The target_lan of this NetworkLoadBalancerProperties.  # noqa: E501
        :type target_lan: int
        """
        if self.local_vars_configuration.client_side_validation and target_lan is None:  # noqa: E501
            raise ValueError("Invalid value for `target_lan`, must not be `None`")  # noqa: E501

        self._target_lan = target_lan

    @property
    def lb_private_ips(self):
        """Gets the lb_private_ips of this NetworkLoadBalancerProperties.  # noqa: E501

        Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain a valid subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.  # noqa: E501

        :return: The lb_private_ips of this NetworkLoadBalancerProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._lb_private_ips

    @lb_private_ips.setter
    def lb_private_ips(self, lb_private_ips):
        """Sets the lb_private_ips of this NetworkLoadBalancerProperties.

        Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain a valid subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.  # noqa: E501

        :param lb_private_ips: The lb_private_ips of this NetworkLoadBalancerProperties.  # noqa: E501
        :type lb_private_ips: list[str]
        """

        self._lb_private_ips = lb_private_ips
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
        if not isinstance(other, NetworkLoadBalancerProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkLoadBalancerProperties):
            return True

        return self.to_dict() != other.to_dict()
