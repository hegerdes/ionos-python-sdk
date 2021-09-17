# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.nat_gateway_lan_properties import NatGatewayLanProperties  # noqa: E501
from ionoscloud.rest import ApiException

class TestNatGatewayLanProperties(unittest.TestCase):
    """NatGatewayLanProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NatGatewayLanProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.nat_gateway_lan_properties.NatGatewayLanProperties()  # noqa: E501
        if include_optional :
            return NatGatewayLanProperties(
                id = 3,
                gateway_ips = [10.12.1.2/24, 10.11.2.5/24, 10.11.2.4]
            )
        else :
            return NatGatewayLanProperties(
                id = 3,
        )

    def testNatGatewayLanProperties(self):
        """Test NatGatewayLanProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
