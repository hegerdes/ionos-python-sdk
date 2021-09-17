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
from ionoscloud.models.lan_post import LanPost  # noqa: E501
from ionoscloud.rest import ApiException

class TestLanPost(unittest.TestCase):
    """LanPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LanPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.lan_post.LanPost()  # noqa: E501
        if include_optional :
            return LanPost(
                id = '5',
                type = "lan",
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
                entities = ionoscloud.models.lan_entities.LanEntities(
                    nics = ionoscloud.models.lan_nics.LanNics(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', 
                        items = [
                            ionoscloud.models.nic.Nic(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "nic", 
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
                                properties = ionoscloud.models.nic_properties.NicProperties(
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
                                    pci_slot = 7, ), 
                                entities = ionoscloud.models.nic_entities.NicEntities(
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
                                    firewallrules = ionoscloud.models.firewall_rules.FirewallRules(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = "collection", 
                                        href = '<RESOURCE-URI>', 
                                        offset = 0, 
                                        limit = 1000, ), ), )
                            ], 
                        offset = 0, 
                        limit = 1000, 
                        _links = ionoscloud.models.pagination_links.PaginationLinks(
                            prev = '<PREVIOUS-PAGE-URI>', 
                            self = '<THIS-PAGE-URI>', 
                            next = '<NEXT-PAGE-URI>', ), ), ),
                properties = ionoscloud.models.lan_properties_post.LanPropertiesPost(
                    name = 'My resource', 
                    ip_failover = [
                        ionoscloud.models.ip_failover.IPFailover(
                            ip = '192.18.2.231', 
                            nic_uuid = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', )
                        ], 
                    pcc = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', 
                    public = True, )
            )
        else :
            return LanPost(
                properties = ionoscloud.models.lan_properties_post.LanPropertiesPost(
                    name = 'My resource', 
                    ip_failover = [
                        ionoscloud.models.ip_failover.IPFailover(
                            ip = '192.18.2.231', 
                            nic_uuid = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', )
                        ], 
                    pcc = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', 
                    public = True, ),
        )

    def testLanPost(self):
        """Test LanPost"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
