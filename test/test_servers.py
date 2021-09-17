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
from ionoscloud.models.servers import Servers  # noqa: E501
from ionoscloud.rest import ApiException

class TestServers(unittest.TestCase):
    """Servers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Servers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.servers.Servers()  # noqa: E501
        if include_optional :
            return Servers(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "collection",
                href = '<RESOURCE-URI>',
                items = [
                    ionoscloud.models.server.Server(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "server", 
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
                        properties = ionoscloud.models.server_properties.ServerProperties(
                            template_uuid = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                            name = 'My resource', 
                            cores = 4, 
                            ram = 4096, 
                            availability_zone = 'AUTO', 
                            vm_state = 'RUNNING', 
                            boot_cdrom = ionoscloud.models.resource_reference.ResourceReference(
                                id = '', 
                                type = "resource", 
                                href = '<RESOURCE-URI>', ), 
                            boot_volume = ionoscloud.models.resource_reference.ResourceReference(
                                id = '', 
                                type = "resource", 
                                href = '<RESOURCE-URI>', ), 
                            cpu_family = 'AMD_OPTERON', 
                            type = 'CUBE', ), 
                        entities = ionoscloud.models.server_entities.ServerEntities(
                            cdroms = ionoscloud.models.cdroms.Cdroms(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', 
                                offset = 0, 
                                limit = 1000, 
                                _links = ionoscloud.models.pagination_links.PaginationLinks(
                                    prev = '<PREVIOUS-PAGE-URI>', 
                                    self = '<THIS-PAGE-URI>', 
                                    next = '<NEXT-PAGE-URI>', ), ), 
                            volumes = ionoscloud.models.attached_volumes.AttachedVolumes(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = '<RESOURCE-URI>', 
                                offset = 0, 
                                limit = 1000, ), 
                            nics = ionoscloud.models.nics.Nics(
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
            return Servers(
        )

    def testServers(self):
        """Test Servers"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
