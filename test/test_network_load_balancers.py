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
from ionoscloud.models.network_load_balancers import NetworkLoadBalancers  # noqa: E501
from ionoscloud.rest import ApiException

class TestNetworkLoadBalancers(unittest.TestCase):
    """NetworkLoadBalancers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkLoadBalancers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.network_load_balancers.NetworkLoadBalancers()  # noqa: E501
        if include_optional :
            return NetworkLoadBalancers(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "collection",
                href = '<RESOURCE-URI>',
                items = [
                    ionoscloud.models.network_load_balancer.NetworkLoadBalancer(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "networkloadbalancer", 
                        href = '<RESOURCE-URI>', 
                        metadata = ionoscloud.models.datacenter_element_metadata.DatacenterElementMetadata(
                            etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                            created_date = '2015-12-04T14:34:09.809Z', 
                            created_by = 'user@example.com', 
                            created_by_user_id = 'user@example.com', 
                            last_modified_date = '2015-12-04T14:34:09.809Z', 
                            last_modified_by = 'user@example.com', 
                            last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                            state = 'AVAILABLE', ), 
                        properties = ionoscloud.models.network_load_balancer_properties.NetworkLoadBalancerProperties(
                            name = 'My Network Load Balancer', 
                            listener_lan = 1, 
                            ips = [81.173.1.2, 22.231.2.2, 22.231.2.3], 
                            target_lan = 2, 
                            lb_private_ips = [81.173.1.5/24, 22.231.2.5/24], ), 
                        entities = ionoscloud.models.network_load_balancer_entities.NetworkLoadBalancerEntities(
                            flowlogs = ionoscloud.models.flow_logs.FlowLogs(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', 
                                offset = 0, 
                                limit = 1000, 
                                _links = ionoscloud.models.pagination_links.PaginationLinks(
                                    prev = '<PREVIOUS-PAGE-URI>', 
                                    self = '<THIS-PAGE-URI>', 
                                    next = '<NEXT-PAGE-URI>', ), ), 
                            forwardingrules = ionoscloud.models.network_load_balancer_forwarding_rules.NetworkLoadBalancerForwardingRules(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', 
                                offset = 0, 
                                limit = 1000, ), ), )
                    ],
                offset = 0,
                limit = 1000,
                links = ionoscloud.models.pagination_links.PaginationLinks(
                    prev = '<PREVIOUS-PAGE-URI>', 
                    self = '<THIS-PAGE-URI>', 
                    next = '<NEXT-PAGE-URI>', )
            )
        else :
            return NetworkLoadBalancers(
        )

    def testNetworkLoadBalancers(self):
        """Test NetworkLoadBalancers"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
