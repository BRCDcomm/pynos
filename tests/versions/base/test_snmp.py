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
import pynos.versions.base.snmp
import pynos.utilities


class TestSNMP(unittest.TestCase):
    """
    System unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.snmp = pynos.versions.base.snmp.SNMP(pynos.utilities.return_xml)
        self.namespace = 'urn:brocade.com:mgmt:brocade-snmp'
        self.community = 'public'

    def test_add_snmp_community(self):
        expected = '<config><snmp-server xmlns="{0}"><community><community>'\
                   '{1}</community></community></snmp-server>'\
                   '</config>'.format(self.namespace, self.community)
        result = self.snmp.add_snmp_community(community='public')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_add_snmp_community_exception(self):
        with self.assertRaises(KeyError):
            self.snmp.add_snmp_community()

    def test_del_snmp_community(self):
        expected = '<config><snmp-server xmlns="{0}">'\
                   '<community operation="delete"><community>{1}</community>'\
                   '</community></snmp-server></config>'.format(self.namespace,
                                                                self.community)
        result = self.snmp.del_snmp_community(community='public')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_del_snmp_community_exception(self):
        with self.assertRaises(KeyError):
            self.snmp.del_snmp_community()

    def test_add_snmp_host(self):
        expected = '<config><snmp-server xmlns="{0}"><host><ip>10.10.10.10'\
                   '</ip><community>{1}</community><udp-port>162</udp-port>'\
                   '</host></snmp-server></config>'.format(self.namespace,
                                                           self.community)
        result = self.snmp.add_snmp_host(community='public',
                                         host_info=('10.10.10.10', '162'))
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_add_snmp_host_exception(self):
        with self.assertRaises(KeyError):
            self.snmp.add_snmp_host()

    def test_del_snmp_host(self):
        expected = '<config><snmp-server xmlns="{0}">'\
                   '<host operation="delete"><ip>10.10.10.10</ip><community>'\
                   '{1}</community><udp-port>162</udp-port></host>'\
                   '</snmp-server></config>'.format(self.namespace,
                                                    self.community)
        result = self.snmp.del_snmp_host(community='public',
                                         host_info=('10.10.10.10', '162'))
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_del_snmp_host_exception(self):
        with self.assertRaises(KeyError):
            self.snmp.del_snmp_host()
