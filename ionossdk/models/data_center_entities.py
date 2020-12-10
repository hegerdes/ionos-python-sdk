# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionossdk.configuration import Configuration


class DataCenterEntities(object):
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
        'servers': 'Servers',
        'volumes': 'Volumes',
        'loadbalancers': 'Loadbalancers',
        'lans': 'Lans'
    }

    attribute_map = {
        'servers': 'servers',
        'volumes': 'volumes',
        'loadbalancers': 'loadbalancers',
        'lans': 'lans'
    }

    def __init__(self, servers=None, volumes=None, loadbalancers=None, lans=None, local_vars_configuration=None):  # noqa: E501
        """DataCenterEntities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._servers = None
        self._volumes = None
        self._loadbalancers = None
        self._lans = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if volumes is not None:
            self.volumes = volumes
        if loadbalancers is not None:
            self.loadbalancers = loadbalancers
        if lans is not None:
            self.lans = lans

    @property
    def servers(self):
        """Gets the servers of this DataCenterEntities.  # noqa: E501


        :return: The servers of this DataCenterEntities.  # noqa: E501
        :rtype: Servers
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this DataCenterEntities.


        :param servers: The servers of this DataCenterEntities.  # noqa: E501
        :type servers: Servers
        """

        self._servers = servers

    @property
    def volumes(self):
        """Gets the volumes of this DataCenterEntities.  # noqa: E501


        :return: The volumes of this DataCenterEntities.  # noqa: E501
        :rtype: Volumes
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this DataCenterEntities.


        :param volumes: The volumes of this DataCenterEntities.  # noqa: E501
        :type volumes: Volumes
        """

        self._volumes = volumes

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this DataCenterEntities.  # noqa: E501


        :return: The loadbalancers of this DataCenterEntities.  # noqa: E501
        :rtype: Loadbalancers
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this DataCenterEntities.


        :param loadbalancers: The loadbalancers of this DataCenterEntities.  # noqa: E501
        :type loadbalancers: Loadbalancers
        """

        self._loadbalancers = loadbalancers

    @property
    def lans(self):
        """Gets the lans of this DataCenterEntities.  # noqa: E501


        :return: The lans of this DataCenterEntities.  # noqa: E501
        :rtype: Lans
        """
        return self._lans

    @lans.setter
    def lans(self, lans):
        """Sets the lans of this DataCenterEntities.


        :param lans: The lans of this DataCenterEntities.  # noqa: E501
        :type lans: Lans
        """

        self._lans = lans

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
        if not isinstance(other, DataCenterEntities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataCenterEntities):
            return True

        return self.to_dict() != other.to_dict()
