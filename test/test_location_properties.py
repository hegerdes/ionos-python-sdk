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
from ionoscloud.models.location_properties import LocationProperties  # noqa: E501
from ionoscloud.rest import ApiException

class TestLocationProperties(unittest.TestCase):
    """LocationProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocationProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.location_properties.LocationProperties()  # noqa: E501
        if include_optional :
            return LocationProperties(
                name = 'My resource',
                features = [SSD],
                image_aliases = [
                    ''
                    ],
                cpu_architecture = [
                    ionoscloud.models.cpu_architecture_properties.CpuArchitectureProperties(
                        cpu_family = 'AMD_OPTERON', 
                        max_cores = 62, 
                        max_ram = 245760, 
                        vendor = 'AuthenticAMD', )
                    ]
            )
        else :
            return LocationProperties(
        )

    def testLocationProperties(self):
        """Test LocationProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
