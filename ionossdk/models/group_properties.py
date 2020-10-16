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


class GroupProperties(object):
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
        'create_data_center': 'bool',
        'create_snapshot': 'bool',
        'reserve_ip': 'bool',
        'access_activity_log': 'bool',
        'create_pcc': 'bool',
        's3_privilege': 'bool',
        'create_backup_unit': 'bool',
        'create_internet_access': 'bool',
        'create_k8s_cluster': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'create_data_center': 'createDataCenter',
        'create_snapshot': 'createSnapshot',
        'reserve_ip': 'reserveIp',
        'access_activity_log': 'accessActivityLog',
        'create_pcc': 'createPcc',
        's3_privilege': 's3Privilege',
        'create_backup_unit': 'createBackupUnit',
        'create_internet_access': 'createInternetAccess',
        'create_k8s_cluster': 'createK8sCluster'
    }

    def __init__(self, name=None, create_data_center=None, create_snapshot=None, reserve_ip=None, access_activity_log=None, create_pcc=None, s3_privilege=None, create_backup_unit=None, create_internet_access=None, create_k8s_cluster=None, local_vars_configuration=None):  # noqa: E501
        """GroupProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._create_data_center = None
        self._create_snapshot = None
        self._reserve_ip = None
        self._access_activity_log = None
        self._create_pcc = None
        self._s3_privilege = None
        self._create_backup_unit = None
        self._create_internet_access = None
        self._create_k8s_cluster = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if create_data_center is not None:
            self.create_data_center = create_data_center
        if create_snapshot is not None:
            self.create_snapshot = create_snapshot
        if reserve_ip is not None:
            self.reserve_ip = reserve_ip
        if access_activity_log is not None:
            self.access_activity_log = access_activity_log
        if create_pcc is not None:
            self.create_pcc = create_pcc
        if s3_privilege is not None:
            self.s3_privilege = s3_privilege
        if create_backup_unit is not None:
            self.create_backup_unit = create_backup_unit
        if create_internet_access is not None:
            self.create_internet_access = create_internet_access
        if create_k8s_cluster is not None:
            self.create_k8s_cluster = create_k8s_cluster

    @property
    def name(self):
        """Gets the name of this GroupProperties.  # noqa: E501

        A name of that resource  # noqa: E501

        :return: The name of this GroupProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupProperties.

        A name of that resource  # noqa: E501

        :param name: The name of this GroupProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def create_data_center(self):
        """Gets the create_data_center of this GroupProperties.  # noqa: E501

        create data center privilege  # noqa: E501

        :return: The create_data_center of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._create_data_center

    @create_data_center.setter
    def create_data_center(self, create_data_center):
        """Sets the create_data_center of this GroupProperties.

        create data center privilege  # noqa: E501

        :param create_data_center: The create_data_center of this GroupProperties.  # noqa: E501
        :type create_data_center: bool
        """

        self._create_data_center = create_data_center

    @property
    def create_snapshot(self):
        """Gets the create_snapshot of this GroupProperties.  # noqa: E501

        create snapshot privilege  # noqa: E501

        :return: The create_snapshot of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._create_snapshot

    @create_snapshot.setter
    def create_snapshot(self, create_snapshot):
        """Sets the create_snapshot of this GroupProperties.

        create snapshot privilege  # noqa: E501

        :param create_snapshot: The create_snapshot of this GroupProperties.  # noqa: E501
        :type create_snapshot: bool
        """

        self._create_snapshot = create_snapshot

    @property
    def reserve_ip(self):
        """Gets the reserve_ip of this GroupProperties.  # noqa: E501

        reserve ip block privilege  # noqa: E501

        :return: The reserve_ip of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._reserve_ip

    @reserve_ip.setter
    def reserve_ip(self, reserve_ip):
        """Sets the reserve_ip of this GroupProperties.

        reserve ip block privilege  # noqa: E501

        :param reserve_ip: The reserve_ip of this GroupProperties.  # noqa: E501
        :type reserve_ip: bool
        """

        self._reserve_ip = reserve_ip

    @property
    def access_activity_log(self):
        """Gets the access_activity_log of this GroupProperties.  # noqa: E501

        activity log access privilege  # noqa: E501

        :return: The access_activity_log of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._access_activity_log

    @access_activity_log.setter
    def access_activity_log(self, access_activity_log):
        """Sets the access_activity_log of this GroupProperties.

        activity log access privilege  # noqa: E501

        :param access_activity_log: The access_activity_log of this GroupProperties.  # noqa: E501
        :type access_activity_log: bool
        """

        self._access_activity_log = access_activity_log

    @property
    def create_pcc(self):
        """Gets the create_pcc of this GroupProperties.  # noqa: E501

        create pcc privilege  # noqa: E501

        :return: The create_pcc of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._create_pcc

    @create_pcc.setter
    def create_pcc(self, create_pcc):
        """Sets the create_pcc of this GroupProperties.

        create pcc privilege  # noqa: E501

        :param create_pcc: The create_pcc of this GroupProperties.  # noqa: E501
        :type create_pcc: bool
        """

        self._create_pcc = create_pcc

    @property
    def s3_privilege(self):
        """Gets the s3_privilege of this GroupProperties.  # noqa: E501

        S3 privilege  # noqa: E501

        :return: The s3_privilege of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._s3_privilege

    @s3_privilege.setter
    def s3_privilege(self, s3_privilege):
        """Sets the s3_privilege of this GroupProperties.

        S3 privilege  # noqa: E501

        :param s3_privilege: The s3_privilege of this GroupProperties.  # noqa: E501
        :type s3_privilege: bool
        """

        self._s3_privilege = s3_privilege

    @property
    def create_backup_unit(self):
        """Gets the create_backup_unit of this GroupProperties.  # noqa: E501

        create backup unit privilege  # noqa: E501

        :return: The create_backup_unit of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._create_backup_unit

    @create_backup_unit.setter
    def create_backup_unit(self, create_backup_unit):
        """Sets the create_backup_unit of this GroupProperties.

        create backup unit privilege  # noqa: E501

        :param create_backup_unit: The create_backup_unit of this GroupProperties.  # noqa: E501
        :type create_backup_unit: bool
        """

        self._create_backup_unit = create_backup_unit

    @property
    def create_internet_access(self):
        """Gets the create_internet_access of this GroupProperties.  # noqa: E501

        create internet access privilege  # noqa: E501

        :return: The create_internet_access of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._create_internet_access

    @create_internet_access.setter
    def create_internet_access(self, create_internet_access):
        """Sets the create_internet_access of this GroupProperties.

        create internet access privilege  # noqa: E501

        :param create_internet_access: The create_internet_access of this GroupProperties.  # noqa: E501
        :type create_internet_access: bool
        """

        self._create_internet_access = create_internet_access

    @property
    def create_k8s_cluster(self):
        """Gets the create_k8s_cluster of this GroupProperties.  # noqa: E501

        create kubernetes cluster privilege  # noqa: E501

        :return: The create_k8s_cluster of this GroupProperties.  # noqa: E501
        :rtype: bool
        """
        return self._create_k8s_cluster

    @create_k8s_cluster.setter
    def create_k8s_cluster(self, create_k8s_cluster):
        """Sets the create_k8s_cluster of this GroupProperties.

        create kubernetes cluster privilege  # noqa: E501

        :param create_k8s_cluster: The create_k8s_cluster of this GroupProperties.  # noqa: E501
        :type create_k8s_cluster: bool
        """

        self._create_k8s_cluster = create_k8s_cluster

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
        if not isinstance(other, GroupProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupProperties):
            return True

        return self.to_dict() != other.to_dict()
