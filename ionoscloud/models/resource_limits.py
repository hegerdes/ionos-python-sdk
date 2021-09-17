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


class ResourceLimits(object):
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
        'cores_per_server': 'int',
        'cores_per_contract': 'int',
        'cores_provisioned': 'int',
        'ram_per_server': 'int',
        'ram_per_contract': 'int',
        'ram_provisioned': 'int',
        'hdd_limit_per_volume': 'int',
        'hdd_limit_per_contract': 'int',
        'hdd_volume_provisioned': 'int',
        'ssd_limit_per_volume': 'int',
        'ssd_limit_per_contract': 'int',
        'ssd_volume_provisioned': 'int',
        'das_volume_provisioned': 'int',
        'reservable_ips': 'int',
        'reserved_ips_on_contract': 'int',
        'reserved_ips_in_use': 'int',
        'k8s_cluster_limit_total': 'int',
        'k8s_clusters_provisioned': 'int',
        'nlb_limit_total': 'int',
        'nlb_provisioned': 'int',
        'nat_gateway_limit_total': 'int',
        'nat_gateway_provisioned': 'int',
    }

    attribute_map = {
        'cores_per_server': 'coresPerServer',
        'cores_per_contract': 'coresPerContract',
        'cores_provisioned': 'coresProvisioned',
        'ram_per_server': 'ramPerServer',
        'ram_per_contract': 'ramPerContract',
        'ram_provisioned': 'ramProvisioned',
        'hdd_limit_per_volume': 'hddLimitPerVolume',
        'hdd_limit_per_contract': 'hddLimitPerContract',
        'hdd_volume_provisioned': 'hddVolumeProvisioned',
        'ssd_limit_per_volume': 'ssdLimitPerVolume',
        'ssd_limit_per_contract': 'ssdLimitPerContract',
        'ssd_volume_provisioned': 'ssdVolumeProvisioned',
        'das_volume_provisioned': 'dasVolumeProvisioned',
        'reservable_ips': 'reservableIps',
        'reserved_ips_on_contract': 'reservedIpsOnContract',
        'reserved_ips_in_use': 'reservedIpsInUse',
        'k8s_cluster_limit_total': 'k8sClusterLimitTotal',
        'k8s_clusters_provisioned': 'k8sClustersProvisioned',
        'nlb_limit_total': 'nlbLimitTotal',
        'nlb_provisioned': 'nlbProvisioned',
        'nat_gateway_limit_total': 'natGatewayLimitTotal',
        'nat_gateway_provisioned': 'natGatewayProvisioned',
    }

    def __init__(self, cores_per_server=None, cores_per_contract=None, cores_provisioned=None, ram_per_server=None, ram_per_contract=None, ram_provisioned=None, hdd_limit_per_volume=None, hdd_limit_per_contract=None, hdd_volume_provisioned=None, ssd_limit_per_volume=None, ssd_limit_per_contract=None, ssd_volume_provisioned=None, das_volume_provisioned=None, reservable_ips=None, reserved_ips_on_contract=None, reserved_ips_in_use=None, k8s_cluster_limit_total=None, k8s_clusters_provisioned=None, nlb_limit_total=None, nlb_provisioned=None, nat_gateway_limit_total=None, nat_gateway_provisioned=None, local_vars_configuration=None):  # noqa: E501
        """ResourceLimits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cores_per_server = None
        self._cores_per_contract = None
        self._cores_provisioned = None
        self._ram_per_server = None
        self._ram_per_contract = None
        self._ram_provisioned = None
        self._hdd_limit_per_volume = None
        self._hdd_limit_per_contract = None
        self._hdd_volume_provisioned = None
        self._ssd_limit_per_volume = None
        self._ssd_limit_per_contract = None
        self._ssd_volume_provisioned = None
        self._das_volume_provisioned = None
        self._reservable_ips = None
        self._reserved_ips_on_contract = None
        self._reserved_ips_in_use = None
        self._k8s_cluster_limit_total = None
        self._k8s_clusters_provisioned = None
        self._nlb_limit_total = None
        self._nlb_provisioned = None
        self._nat_gateway_limit_total = None
        self._nat_gateway_provisioned = None
        self.discriminator = None

        self.cores_per_server = cores_per_server
        self.cores_per_contract = cores_per_contract
        self.cores_provisioned = cores_provisioned
        self.ram_per_server = ram_per_server
        self.ram_per_contract = ram_per_contract
        self.ram_provisioned = ram_provisioned
        self.hdd_limit_per_volume = hdd_limit_per_volume
        self.hdd_limit_per_contract = hdd_limit_per_contract
        self.hdd_volume_provisioned = hdd_volume_provisioned
        self.ssd_limit_per_volume = ssd_limit_per_volume
        self.ssd_limit_per_contract = ssd_limit_per_contract
        self.ssd_volume_provisioned = ssd_volume_provisioned
        self.das_volume_provisioned = das_volume_provisioned
        self.reservable_ips = reservable_ips
        self.reserved_ips_on_contract = reserved_ips_on_contract
        self.reserved_ips_in_use = reserved_ips_in_use
        self.k8s_cluster_limit_total = k8s_cluster_limit_total
        self.k8s_clusters_provisioned = k8s_clusters_provisioned
        self.nlb_limit_total = nlb_limit_total
        self.nlb_provisioned = nlb_provisioned
        self.nat_gateway_limit_total = nat_gateway_limit_total
        self.nat_gateway_provisioned = nat_gateway_provisioned

    @property
    def cores_per_server(self):
        """Gets the cores_per_server of this ResourceLimits.  # noqa: E501

        maximum number of cores per server  # noqa: E501

        :return: The cores_per_server of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._cores_per_server

    @cores_per_server.setter
    def cores_per_server(self, cores_per_server):
        """Sets the cores_per_server of this ResourceLimits.

        maximum number of cores per server  # noqa: E501

        :param cores_per_server: The cores_per_server of this ResourceLimits.  # noqa: E501
        :type cores_per_server: int
        """
        if self.local_vars_configuration.client_side_validation and cores_per_server is None:  # noqa: E501
            raise ValueError("Invalid value for `cores_per_server`, must not be `None`")  # noqa: E501

        self._cores_per_server = cores_per_server

    @property
    def cores_per_contract(self):
        """Gets the cores_per_contract of this ResourceLimits.  # noqa: E501

        maximum cores per contract  # noqa: E501

        :return: The cores_per_contract of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._cores_per_contract

    @cores_per_contract.setter
    def cores_per_contract(self, cores_per_contract):
        """Sets the cores_per_contract of this ResourceLimits.

        maximum cores per contract  # noqa: E501

        :param cores_per_contract: The cores_per_contract of this ResourceLimits.  # noqa: E501
        :type cores_per_contract: int
        """
        if self.local_vars_configuration.client_side_validation and cores_per_contract is None:  # noqa: E501
            raise ValueError("Invalid value for `cores_per_contract`, must not be `None`")  # noqa: E501

        self._cores_per_contract = cores_per_contract

    @property
    def cores_provisioned(self):
        """Gets the cores_provisioned of this ResourceLimits.  # noqa: E501

        number of cores provisioned  # noqa: E501

        :return: The cores_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._cores_provisioned

    @cores_provisioned.setter
    def cores_provisioned(self, cores_provisioned):
        """Sets the cores_provisioned of this ResourceLimits.

        number of cores provisioned  # noqa: E501

        :param cores_provisioned: The cores_provisioned of this ResourceLimits.  # noqa: E501
        :type cores_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and cores_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `cores_provisioned`, must not be `None`")  # noqa: E501

        self._cores_provisioned = cores_provisioned

    @property
    def ram_per_server(self):
        """Gets the ram_per_server of this ResourceLimits.  # noqa: E501

        maximum ram per server  # noqa: E501

        :return: The ram_per_server of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._ram_per_server

    @ram_per_server.setter
    def ram_per_server(self, ram_per_server):
        """Sets the ram_per_server of this ResourceLimits.

        maximum ram per server  # noqa: E501

        :param ram_per_server: The ram_per_server of this ResourceLimits.  # noqa: E501
        :type ram_per_server: int
        """
        if self.local_vars_configuration.client_side_validation and ram_per_server is None:  # noqa: E501
            raise ValueError("Invalid value for `ram_per_server`, must not be `None`")  # noqa: E501

        self._ram_per_server = ram_per_server

    @property
    def ram_per_contract(self):
        """Gets the ram_per_contract of this ResourceLimits.  # noqa: E501

        maximum ram per contract  # noqa: E501

        :return: The ram_per_contract of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._ram_per_contract

    @ram_per_contract.setter
    def ram_per_contract(self, ram_per_contract):
        """Sets the ram_per_contract of this ResourceLimits.

        maximum ram per contract  # noqa: E501

        :param ram_per_contract: The ram_per_contract of this ResourceLimits.  # noqa: E501
        :type ram_per_contract: int
        """
        if self.local_vars_configuration.client_side_validation and ram_per_contract is None:  # noqa: E501
            raise ValueError("Invalid value for `ram_per_contract`, must not be `None`")  # noqa: E501

        self._ram_per_contract = ram_per_contract

    @property
    def ram_provisioned(self):
        """Gets the ram_provisioned of this ResourceLimits.  # noqa: E501

        ram provisioned  # noqa: E501

        :return: The ram_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._ram_provisioned

    @ram_provisioned.setter
    def ram_provisioned(self, ram_provisioned):
        """Sets the ram_provisioned of this ResourceLimits.

        ram provisioned  # noqa: E501

        :param ram_provisioned: The ram_provisioned of this ResourceLimits.  # noqa: E501
        :type ram_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and ram_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `ram_provisioned`, must not be `None`")  # noqa: E501

        self._ram_provisioned = ram_provisioned

    @property
    def hdd_limit_per_volume(self):
        """Gets the hdd_limit_per_volume of this ResourceLimits.  # noqa: E501

        hdd limit per volume  # noqa: E501

        :return: The hdd_limit_per_volume of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._hdd_limit_per_volume

    @hdd_limit_per_volume.setter
    def hdd_limit_per_volume(self, hdd_limit_per_volume):
        """Sets the hdd_limit_per_volume of this ResourceLimits.

        hdd limit per volume  # noqa: E501

        :param hdd_limit_per_volume: The hdd_limit_per_volume of this ResourceLimits.  # noqa: E501
        :type hdd_limit_per_volume: int
        """
        if self.local_vars_configuration.client_side_validation and hdd_limit_per_volume is None:  # noqa: E501
            raise ValueError("Invalid value for `hdd_limit_per_volume`, must not be `None`")  # noqa: E501

        self._hdd_limit_per_volume = hdd_limit_per_volume

    @property
    def hdd_limit_per_contract(self):
        """Gets the hdd_limit_per_contract of this ResourceLimits.  # noqa: E501

        hdd limit per contract  # noqa: E501

        :return: The hdd_limit_per_contract of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._hdd_limit_per_contract

    @hdd_limit_per_contract.setter
    def hdd_limit_per_contract(self, hdd_limit_per_contract):
        """Sets the hdd_limit_per_contract of this ResourceLimits.

        hdd limit per contract  # noqa: E501

        :param hdd_limit_per_contract: The hdd_limit_per_contract of this ResourceLimits.  # noqa: E501
        :type hdd_limit_per_contract: int
        """
        if self.local_vars_configuration.client_side_validation and hdd_limit_per_contract is None:  # noqa: E501
            raise ValueError("Invalid value for `hdd_limit_per_contract`, must not be `None`")  # noqa: E501

        self._hdd_limit_per_contract = hdd_limit_per_contract

    @property
    def hdd_volume_provisioned(self):
        """Gets the hdd_volume_provisioned of this ResourceLimits.  # noqa: E501

        hdd volume provisioned  # noqa: E501

        :return: The hdd_volume_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._hdd_volume_provisioned

    @hdd_volume_provisioned.setter
    def hdd_volume_provisioned(self, hdd_volume_provisioned):
        """Sets the hdd_volume_provisioned of this ResourceLimits.

        hdd volume provisioned  # noqa: E501

        :param hdd_volume_provisioned: The hdd_volume_provisioned of this ResourceLimits.  # noqa: E501
        :type hdd_volume_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and hdd_volume_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `hdd_volume_provisioned`, must not be `None`")  # noqa: E501

        self._hdd_volume_provisioned = hdd_volume_provisioned

    @property
    def ssd_limit_per_volume(self):
        """Gets the ssd_limit_per_volume of this ResourceLimits.  # noqa: E501

        ssd limit per volume  # noqa: E501

        :return: The ssd_limit_per_volume of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._ssd_limit_per_volume

    @ssd_limit_per_volume.setter
    def ssd_limit_per_volume(self, ssd_limit_per_volume):
        """Sets the ssd_limit_per_volume of this ResourceLimits.

        ssd limit per volume  # noqa: E501

        :param ssd_limit_per_volume: The ssd_limit_per_volume of this ResourceLimits.  # noqa: E501
        :type ssd_limit_per_volume: int
        """
        if self.local_vars_configuration.client_side_validation and ssd_limit_per_volume is None:  # noqa: E501
            raise ValueError("Invalid value for `ssd_limit_per_volume`, must not be `None`")  # noqa: E501

        self._ssd_limit_per_volume = ssd_limit_per_volume

    @property
    def ssd_limit_per_contract(self):
        """Gets the ssd_limit_per_contract of this ResourceLimits.  # noqa: E501

        ssd limit per contract  # noqa: E501

        :return: The ssd_limit_per_contract of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._ssd_limit_per_contract

    @ssd_limit_per_contract.setter
    def ssd_limit_per_contract(self, ssd_limit_per_contract):
        """Sets the ssd_limit_per_contract of this ResourceLimits.

        ssd limit per contract  # noqa: E501

        :param ssd_limit_per_contract: The ssd_limit_per_contract of this ResourceLimits.  # noqa: E501
        :type ssd_limit_per_contract: int
        """
        if self.local_vars_configuration.client_side_validation and ssd_limit_per_contract is None:  # noqa: E501
            raise ValueError("Invalid value for `ssd_limit_per_contract`, must not be `None`")  # noqa: E501

        self._ssd_limit_per_contract = ssd_limit_per_contract

    @property
    def ssd_volume_provisioned(self):
        """Gets the ssd_volume_provisioned of this ResourceLimits.  # noqa: E501

        ssd volume provisioned  # noqa: E501

        :return: The ssd_volume_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._ssd_volume_provisioned

    @ssd_volume_provisioned.setter
    def ssd_volume_provisioned(self, ssd_volume_provisioned):
        """Sets the ssd_volume_provisioned of this ResourceLimits.

        ssd volume provisioned  # noqa: E501

        :param ssd_volume_provisioned: The ssd_volume_provisioned of this ResourceLimits.  # noqa: E501
        :type ssd_volume_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and ssd_volume_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `ssd_volume_provisioned`, must not be `None`")  # noqa: E501

        self._ssd_volume_provisioned = ssd_volume_provisioned

    @property
    def das_volume_provisioned(self):
        """Gets the das_volume_provisioned of this ResourceLimits.  # noqa: E501

        DAS (Direct Attached Storage) volume provisioned  # noqa: E501

        :return: The das_volume_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._das_volume_provisioned

    @das_volume_provisioned.setter
    def das_volume_provisioned(self, das_volume_provisioned):
        """Sets the das_volume_provisioned of this ResourceLimits.

        DAS (Direct Attached Storage) volume provisioned  # noqa: E501

        :param das_volume_provisioned: The das_volume_provisioned of this ResourceLimits.  # noqa: E501
        :type das_volume_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and das_volume_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `das_volume_provisioned`, must not be `None`")  # noqa: E501

        self._das_volume_provisioned = das_volume_provisioned

    @property
    def reservable_ips(self):
        """Gets the reservable_ips of this ResourceLimits.  # noqa: E501

        total reservable ip limit of the customer  # noqa: E501

        :return: The reservable_ips of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._reservable_ips

    @reservable_ips.setter
    def reservable_ips(self, reservable_ips):
        """Sets the reservable_ips of this ResourceLimits.

        total reservable ip limit of the customer  # noqa: E501

        :param reservable_ips: The reservable_ips of this ResourceLimits.  # noqa: E501
        :type reservable_ips: int
        """
        if self.local_vars_configuration.client_side_validation and reservable_ips is None:  # noqa: E501
            raise ValueError("Invalid value for `reservable_ips`, must not be `None`")  # noqa: E501

        self._reservable_ips = reservable_ips

    @property
    def reserved_ips_on_contract(self):
        """Gets the reserved_ips_on_contract of this ResourceLimits.  # noqa: E501

        reserved ips on a contract  # noqa: E501

        :return: The reserved_ips_on_contract of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._reserved_ips_on_contract

    @reserved_ips_on_contract.setter
    def reserved_ips_on_contract(self, reserved_ips_on_contract):
        """Sets the reserved_ips_on_contract of this ResourceLimits.

        reserved ips on a contract  # noqa: E501

        :param reserved_ips_on_contract: The reserved_ips_on_contract of this ResourceLimits.  # noqa: E501
        :type reserved_ips_on_contract: int
        """
        if self.local_vars_configuration.client_side_validation and reserved_ips_on_contract is None:  # noqa: E501
            raise ValueError("Invalid value for `reserved_ips_on_contract`, must not be `None`")  # noqa: E501

        self._reserved_ips_on_contract = reserved_ips_on_contract

    @property
    def reserved_ips_in_use(self):
        """Gets the reserved_ips_in_use of this ResourceLimits.  # noqa: E501

        reserved ips in use  # noqa: E501

        :return: The reserved_ips_in_use of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._reserved_ips_in_use

    @reserved_ips_in_use.setter
    def reserved_ips_in_use(self, reserved_ips_in_use):
        """Sets the reserved_ips_in_use of this ResourceLimits.

        reserved ips in use  # noqa: E501

        :param reserved_ips_in_use: The reserved_ips_in_use of this ResourceLimits.  # noqa: E501
        :type reserved_ips_in_use: int
        """
        if self.local_vars_configuration.client_side_validation and reserved_ips_in_use is None:  # noqa: E501
            raise ValueError("Invalid value for `reserved_ips_in_use`, must not be `None`")  # noqa: E501

        self._reserved_ips_in_use = reserved_ips_in_use

    @property
    def k8s_cluster_limit_total(self):
        """Gets the k8s_cluster_limit_total of this ResourceLimits.  # noqa: E501

        k8s clusters total limit  # noqa: E501

        :return: The k8s_cluster_limit_total of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._k8s_cluster_limit_total

    @k8s_cluster_limit_total.setter
    def k8s_cluster_limit_total(self, k8s_cluster_limit_total):
        """Sets the k8s_cluster_limit_total of this ResourceLimits.

        k8s clusters total limit  # noqa: E501

        :param k8s_cluster_limit_total: The k8s_cluster_limit_total of this ResourceLimits.  # noqa: E501
        :type k8s_cluster_limit_total: int
        """
        if self.local_vars_configuration.client_side_validation and k8s_cluster_limit_total is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_cluster_limit_total`, must not be `None`")  # noqa: E501

        self._k8s_cluster_limit_total = k8s_cluster_limit_total

    @property
    def k8s_clusters_provisioned(self):
        """Gets the k8s_clusters_provisioned of this ResourceLimits.  # noqa: E501

        k8s clusters provisioned  # noqa: E501

        :return: The k8s_clusters_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._k8s_clusters_provisioned

    @k8s_clusters_provisioned.setter
    def k8s_clusters_provisioned(self, k8s_clusters_provisioned):
        """Sets the k8s_clusters_provisioned of this ResourceLimits.

        k8s clusters provisioned  # noqa: E501

        :param k8s_clusters_provisioned: The k8s_clusters_provisioned of this ResourceLimits.  # noqa: E501
        :type k8s_clusters_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and k8s_clusters_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_clusters_provisioned`, must not be `None`")  # noqa: E501

        self._k8s_clusters_provisioned = k8s_clusters_provisioned

    @property
    def nlb_limit_total(self):
        """Gets the nlb_limit_total of this ResourceLimits.  # noqa: E501

        NLB total limit  # noqa: E501

        :return: The nlb_limit_total of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._nlb_limit_total

    @nlb_limit_total.setter
    def nlb_limit_total(self, nlb_limit_total):
        """Sets the nlb_limit_total of this ResourceLimits.

        NLB total limit  # noqa: E501

        :param nlb_limit_total: The nlb_limit_total of this ResourceLimits.  # noqa: E501
        :type nlb_limit_total: int
        """
        if self.local_vars_configuration.client_side_validation and nlb_limit_total is None:  # noqa: E501
            raise ValueError("Invalid value for `nlb_limit_total`, must not be `None`")  # noqa: E501

        self._nlb_limit_total = nlb_limit_total

    @property
    def nlb_provisioned(self):
        """Gets the nlb_provisioned of this ResourceLimits.  # noqa: E501

        NLBs provisioned  # noqa: E501

        :return: The nlb_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._nlb_provisioned

    @nlb_provisioned.setter
    def nlb_provisioned(self, nlb_provisioned):
        """Sets the nlb_provisioned of this ResourceLimits.

        NLBs provisioned  # noqa: E501

        :param nlb_provisioned: The nlb_provisioned of this ResourceLimits.  # noqa: E501
        :type nlb_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and nlb_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `nlb_provisioned`, must not be `None`")  # noqa: E501

        self._nlb_provisioned = nlb_provisioned

    @property
    def nat_gateway_limit_total(self):
        """Gets the nat_gateway_limit_total of this ResourceLimits.  # noqa: E501

        NAT gateway total limit  # noqa: E501

        :return: The nat_gateway_limit_total of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._nat_gateway_limit_total

    @nat_gateway_limit_total.setter
    def nat_gateway_limit_total(self, nat_gateway_limit_total):
        """Sets the nat_gateway_limit_total of this ResourceLimits.

        NAT gateway total limit  # noqa: E501

        :param nat_gateway_limit_total: The nat_gateway_limit_total of this ResourceLimits.  # noqa: E501
        :type nat_gateway_limit_total: int
        """
        if self.local_vars_configuration.client_side_validation and nat_gateway_limit_total is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_gateway_limit_total`, must not be `None`")  # noqa: E501

        self._nat_gateway_limit_total = nat_gateway_limit_total

    @property
    def nat_gateway_provisioned(self):
        """Gets the nat_gateway_provisioned of this ResourceLimits.  # noqa: E501

        NAT gateways provisioned  # noqa: E501

        :return: The nat_gateway_provisioned of this ResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._nat_gateway_provisioned

    @nat_gateway_provisioned.setter
    def nat_gateway_provisioned(self, nat_gateway_provisioned):
        """Sets the nat_gateway_provisioned of this ResourceLimits.

        NAT gateways provisioned  # noqa: E501

        :param nat_gateway_provisioned: The nat_gateway_provisioned of this ResourceLimits.  # noqa: E501
        :type nat_gateway_provisioned: int
        """
        if self.local_vars_configuration.client_side_validation and nat_gateway_provisioned is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_gateway_provisioned`, must not be `None`")  # noqa: E501

        self._nat_gateway_provisioned = nat_gateway_provisioned

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
        if not isinstance(other, ResourceLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceLimits):
            return True

        return self.to_dict() != other.to_dict()
