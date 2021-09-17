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
from ionoscloud.models.kubernetes_node_metadata import KubernetesNodeMetadata  # noqa: E501
from ionoscloud.rest import ApiException

class TestKubernetesNodeMetadata(unittest.TestCase):
    """KubernetesNodeMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubernetesNodeMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.kubernetes_node_metadata.KubernetesNodeMetadata()  # noqa: E501
        if include_optional :
            return KubernetesNodeMetadata(
                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3',
                created_date = '2015-12-04T14:34:09.809Z',
                last_modified_date = '2015-12-04T14:34:09.809Z',
                state = 'AVAILABLE',
                last_software_updated_date = '2015-12-04T14:34:09.809Z'
            )
        else :
            return KubernetesNodeMetadata(
        )

    def testKubernetesNodeMetadata(self):
        """Test KubernetesNodeMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
