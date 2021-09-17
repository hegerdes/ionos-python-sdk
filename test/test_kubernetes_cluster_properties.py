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
from ionoscloud.models.kubernetes_cluster_properties import KubernetesClusterProperties  # noqa: E501
from ionoscloud.rest import ApiException

class TestKubernetesClusterProperties(unittest.TestCase):
    """KubernetesClusterProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubernetesClusterProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.kubernetes_cluster_properties.KubernetesClusterProperties()  # noqa: E501
        if include_optional :
            return KubernetesClusterProperties(
                name = 'k8s',
                k8s_version = '1.15.4',
                maintenance_window = ionoscloud.models.kubernetes_maintenance_window.KubernetesMaintenanceWindow(
                    day_of_the_week = 'Monday', 
                    time = '13:00:00', ),
                available_upgrade_versions = [1.16.4, 1.17.7],
                viable_node_pool_versions = [1.17.7, 1.18.2],
                public = True,
                api_subnet_allow_list = [1.2.3.4/32, 2002::1234:abcd:ffff:c0a8:101/64, 1.2.3.4, 2002::1234:abcd:ffff:c0a8:101],
                s3_buckets = [
                    ionoscloud.models.s3_bucket.S3Bucket(
                        name = '', )
                    ]
            )
        else :
            return KubernetesClusterProperties(
                name = 'k8s',
        )

    def testKubernetesClusterProperties(self):
        """Test KubernetesClusterProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
