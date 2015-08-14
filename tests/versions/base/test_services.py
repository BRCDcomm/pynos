#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import unittest
import xml.etree.ElementTree as ET
import pynos.versions.base.services
import pynos.utilities


class TestServices(unittest.TestCase):
    """Services unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        services = pynos.versions.base.services
        self.services = services.Services(pynos.utilities.return_xml)
        self.rbridge_namespace = 'urn:brocade.com:mgmt:brocade-rbridge'
        self.interface_namespace = 'urn:brocade.com:mgmt:brocade-interface'
        self.vrrp_namespace = 'urn:brocade.com:mgmt:brocade-vrrp'
        self.vrrpv3_namespace = 'urn:brocade.com:mgmt:brocade-vrrpv3'
        self.rbridge_id = '2'

    def test_vrrp_enable_ipv4(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><protocol xmlns="{2}">'\
                   '<hide-vrrp-holder xmlns="{3}"><vrrp /></hide-vrrp-holder>'\
                   '</protocol></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace, self.rbridge_id,
                                      self.interface_namespace,
                                      self.vrrp_namespace)
        result = self.services.vrrp(rbridge_id=self.rbridge_id)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_enable_ipv6(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><ipv6><proto-vrrpv3 xmlns="{2}"><vrrp />'\
                   '</proto-vrrpv3></ipv6></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace, self.rbridge_id,
                                      self.vrrpv3_namespace)
        result = self.services.vrrp(rbridge_id=self.rbridge_id, ip_version='6')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_disable_ipv4(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><protocol xmlns="{2}">'\
                   '<hide-vrrp-holder xmlns="{3}"><vrrp operation="delete" />'\
                   '</hide-vrrp-holder></protocol></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace, self.rbridge_id,
                                      self.interface_namespace,
                                      self.vrrp_namespace)

        result = self.services.vrrp(rbridge_id=self.rbridge_id, enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_disable_ipv6(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><ipv6><proto-vrrpv3 xmlns="{2}">'\
                   '<vrrp operation="delete" /></proto-vrrpv3></ipv6>'\
                   '</rbridge-id></config>'.format(self.rbridge_namespace,
                                                   self.rbridge_id,
                                                   self.vrrpv3_namespace)
        result = self.services.vrrp(rbridge_id=self.rbridge_id, ip_version='6',
                                    enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)
