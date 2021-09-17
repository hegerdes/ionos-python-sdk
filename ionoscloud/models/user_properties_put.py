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


class UserPropertiesPut(object):
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
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'administrator': 'bool',
        'force_sec_auth': 'bool',
        'sec_auth_active': 'bool',
        'active': 'bool',
    }

    attribute_map = {
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'administrator': 'administrator',
        'force_sec_auth': 'forceSecAuth',
        'sec_auth_active': 'secAuthActive',
        'active': 'active',
    }

    def __init__(self, firstname=None, lastname=None, email=None, administrator=None, force_sec_auth=None, sec_auth_active=None, active=None, local_vars_configuration=None):  # noqa: E501
        """UserPropertiesPut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._firstname = None
        self._lastname = None
        self._email = None
        self._administrator = None
        self._force_sec_auth = None
        self._sec_auth_active = None
        self._active = None
        self.discriminator = None

        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if administrator is not None:
            self.administrator = administrator
        if force_sec_auth is not None:
            self.force_sec_auth = force_sec_auth
        if sec_auth_active is not None:
            self.sec_auth_active = sec_auth_active
        if active is not None:
            self.active = active

    @property
    def firstname(self):
        """Gets the firstname of this UserPropertiesPut.  # noqa: E501

        first name of the user  # noqa: E501

        :return: The firstname of this UserPropertiesPut.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserPropertiesPut.

        first name of the user  # noqa: E501

        :param firstname: The firstname of this UserPropertiesPut.  # noqa: E501
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserPropertiesPut.  # noqa: E501

        last name of the user  # noqa: E501

        :return: The lastname of this UserPropertiesPut.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserPropertiesPut.

        last name of the user  # noqa: E501

        :param lastname: The lastname of this UserPropertiesPut.  # noqa: E501
        :type lastname: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this UserPropertiesPut.  # noqa: E501

        email address of the user  # noqa: E501

        :return: The email of this UserPropertiesPut.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserPropertiesPut.

        email address of the user  # noqa: E501

        :param email: The email of this UserPropertiesPut.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def administrator(self):
        """Gets the administrator of this UserPropertiesPut.  # noqa: E501

        indicates if the user has admin rights or not  # noqa: E501

        :return: The administrator of this UserPropertiesPut.  # noqa: E501
        :rtype: bool
        """
        return self._administrator

    @administrator.setter
    def administrator(self, administrator):
        """Sets the administrator of this UserPropertiesPut.

        indicates if the user has admin rights or not  # noqa: E501

        :param administrator: The administrator of this UserPropertiesPut.  # noqa: E501
        :type administrator: bool
        """

        self._administrator = administrator

    @property
    def force_sec_auth(self):
        """Gets the force_sec_auth of this UserPropertiesPut.  # noqa: E501

        indicates if secure authentication should be forced on the user or not  # noqa: E501

        :return: The force_sec_auth of this UserPropertiesPut.  # noqa: E501
        :rtype: bool
        """
        return self._force_sec_auth

    @force_sec_auth.setter
    def force_sec_auth(self, force_sec_auth):
        """Sets the force_sec_auth of this UserPropertiesPut.

        indicates if secure authentication should be forced on the user or not  # noqa: E501

        :param force_sec_auth: The force_sec_auth of this UserPropertiesPut.  # noqa: E501
        :type force_sec_auth: bool
        """

        self._force_sec_auth = force_sec_auth

    @property
    def sec_auth_active(self):
        """Gets the sec_auth_active of this UserPropertiesPut.  # noqa: E501

        indicates if secure authentication is active for the user or not  # noqa: E501

        :return: The sec_auth_active of this UserPropertiesPut.  # noqa: E501
        :rtype: bool
        """
        return self._sec_auth_active

    @sec_auth_active.setter
    def sec_auth_active(self, sec_auth_active):
        """Sets the sec_auth_active of this UserPropertiesPut.

        indicates if secure authentication is active for the user or not  # noqa: E501

        :param sec_auth_active: The sec_auth_active of this UserPropertiesPut.  # noqa: E501
        :type sec_auth_active: bool
        """

        self._sec_auth_active = sec_auth_active

    @property
    def active(self):
        """Gets the active of this UserPropertiesPut.  # noqa: E501

        indicates if the user is active  # noqa: E501

        :return: The active of this UserPropertiesPut.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserPropertiesPut.

        indicates if the user is active  # noqa: E501

        :param active: The active of this UserPropertiesPut.  # noqa: E501
        :type active: bool
        """

        self._active = active

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
        if not isinstance(other, UserPropertiesPut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPropertiesPut):
            return True

        return self.to_dict() != other.to_dict()
