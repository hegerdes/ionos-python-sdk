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


class TargetGroupHttpHealthCheck(object):
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

        'path': 'str',

        'method': 'str',

        'match_type': 'str',

        'response': 'str',

        'regex': 'bool',

        'negate': 'bool',
    }

    attribute_map = {

        'path': 'path',

        'method': 'method',

        'match_type': 'matchType',

        'response': 'response',

        'regex': 'regex',

        'negate': 'negate',
    }

    def __init__(self, path=None, method=None, match_type=None, response=None, regex=None, negate=None, local_vars_configuration=None):  # noqa: E501
        """TargetGroupHttpHealthCheck - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._method = None
        self._match_type = None
        self._response = None
        self._regex = None
        self._negate = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if method is not None:
            self.method = method
        self.match_type = match_type
        self.response = response
        if regex is not None:
            self.regex = regex
        if negate is not None:
            self.negate = negate


    @property
    def path(self):
        """Gets the path of this TargetGroupHttpHealthCheck.  # noqa: E501

        The path (destination URL) for the HTTP health check request; the default is /.  # noqa: E501

        :return: The path of this TargetGroupHttpHealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TargetGroupHttpHealthCheck.

        The path (destination URL) for the HTTP health check request; the default is /.  # noqa: E501

        :param path: The path of this TargetGroupHttpHealthCheck.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def method(self):
        """Gets the method of this TargetGroupHttpHealthCheck.  # noqa: E501

        The method for the HTTP health check.  # noqa: E501

        :return: The method of this TargetGroupHttpHealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this TargetGroupHttpHealthCheck.

        The method for the HTTP health check.  # noqa: E501

        :param method: The method of this TargetGroupHttpHealthCheck.  # noqa: E501
        :type method: str
        """
        allowed_values = ["HEAD", "PUT", "POST", "GET", "TRACE", "PATCH", "OPTIONS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def match_type(self):
        """Gets the match_type of this TargetGroupHttpHealthCheck.  # noqa: E501

          # noqa: E501

        :return: The match_type of this TargetGroupHttpHealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this TargetGroupHttpHealthCheck.

          # noqa: E501

        :param match_type: The match_type of this TargetGroupHttpHealthCheck.  # noqa: E501
        :type match_type: str
        """
        if self.local_vars_configuration.client_side_validation and match_type is None:  # noqa: E501
            raise ValueError("Invalid value for `match_type`, must not be `None`")  # noqa: E501
        allowed_values = ["STATUS_CODE", "RESPONSE_BODY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and match_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `match_type` ({0}), must be one of {1}"  # noqa: E501
                .format(match_type, allowed_values)
            )

        self._match_type = match_type

    @property
    def response(self):
        """Gets the response of this TargetGroupHttpHealthCheck.  # noqa: E501

        The response returned by the request, depending on the match type.  # noqa: E501

        :return: The response of this TargetGroupHttpHealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this TargetGroupHttpHealthCheck.

        The response returned by the request, depending on the match type.  # noqa: E501

        :param response: The response of this TargetGroupHttpHealthCheck.  # noqa: E501
        :type response: str
        """
        if self.local_vars_configuration.client_side_validation and response is None:  # noqa: E501
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501

        self._response = response

    @property
    def regex(self):
        """Gets the regex of this TargetGroupHttpHealthCheck.  # noqa: E501

          # noqa: E501

        :return: The regex of this TargetGroupHttpHealthCheck.  # noqa: E501
        :rtype: bool
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this TargetGroupHttpHealthCheck.

          # noqa: E501

        :param regex: The regex of this TargetGroupHttpHealthCheck.  # noqa: E501
        :type regex: bool
        """

        self._regex = regex

    @property
    def negate(self):
        """Gets the negate of this TargetGroupHttpHealthCheck.  # noqa: E501

          # noqa: E501

        :return: The negate of this TargetGroupHttpHealthCheck.  # noqa: E501
        :rtype: bool
        """
        return self._negate

    @negate.setter
    def negate(self, negate):
        """Sets the negate of this TargetGroupHttpHealthCheck.

          # noqa: E501

        :param negate: The negate of this TargetGroupHttpHealthCheck.  # noqa: E501
        :type negate: bool
        """

        self._negate = negate
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
        if not isinstance(other, TargetGroupHttpHealthCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetGroupHttpHealthCheck):
            return True

        return self.to_dict() != other.to_dict()