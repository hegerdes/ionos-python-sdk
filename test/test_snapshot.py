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
from ionoscloud.models.snapshot import Snapshot  # noqa: E501
from ionoscloud.rest import ApiException

class TestSnapshot(unittest.TestCase):
    """Snapshot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Snapshot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.snapshot.Snapshot()  # noqa: E501
        if include_optional :
            return Snapshot(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "snapshot",
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
                properties = ionoscloud.models.snapshot_properties.SnapshotProperties(
                    name = 'My resource', 
                    description = 'Image/Snapshot of Ubuntu ', 
                    location = 'us/las', 
                    size = 100.0, 
                    sec_auth_protection = True, 
                    cpu_hot_plug = True, 
                    cpu_hot_unplug = True, 
                    ram_hot_plug = True, 
                    ram_hot_unplug = True, 
                    nic_hot_plug = True, 
                    nic_hot_unplug = True, 
                    disc_virtio_hot_plug = True, 
                    disc_virtio_hot_unplug = True, 
                    disc_scsi_hot_plug = True, 
                    disc_scsi_hot_unplug = True, 
                    licence_type = 'LINUX', )
            )
        else :
            return Snapshot(
                properties = ionoscloud.models.snapshot_properties.SnapshotProperties(
                    name = 'My resource', 
                    description = 'Image/Snapshot of Ubuntu ', 
                    location = 'us/las', 
                    size = 100.0, 
                    sec_auth_protection = True, 
                    cpu_hot_plug = True, 
                    cpu_hot_unplug = True, 
                    ram_hot_plug = True, 
                    ram_hot_unplug = True, 
                    nic_hot_plug = True, 
                    nic_hot_unplug = True, 
                    disc_virtio_hot_plug = True, 
                    disc_virtio_hot_unplug = True, 
                    disc_scsi_hot_plug = True, 
                    disc_scsi_hot_unplug = True, 
                    licence_type = 'LINUX', ),
        )

    def testSnapshot(self):
        """Test Snapshot"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
