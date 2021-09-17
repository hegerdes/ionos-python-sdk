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
from ionoscloud.models.nic_properties import NicProperties  # noqa: E501
from ionoscloud.rest import ApiException

class TestNicProperties(unittest.TestCase):
    """NicProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NicProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.nic_properties.NicProperties()  # noqa: E501
        if include_optional :
            return NicProperties(
                name = 'My resource',
                mac = '00:0a:95:9d:68:16',
                ips = [
                    ''
                    ],
                dhcp = True,
                lan = 2,
                firewall_active = False,
                firewall_type = 'INGRESS',
                device_number = 3,
                pci_slot = 7
            )
        else :
            return NicProperties(
                lan = 2,
        )

    def testNicProperties(self):
        """Test NicProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
