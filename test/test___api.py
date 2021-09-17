# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ionoscloud
from ionoscloud.api.__api import Api  # noqa: E501
from ionoscloud.rest import ApiException


class TestApi(unittest.TestCase):
    """Api unit test stubs"""

    def setUp(self):
        self.api = ionoscloud.api.__api.Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_info_get(self):
        """Test case for api_info_get

        Display API information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
