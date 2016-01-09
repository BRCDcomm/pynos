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
import pynos.versions.ver_7.ver_7_0_0.lldp
import pynos.utilities


class TestLLDP(unittest.TestCase):
    """
    LLDP unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.lldp = pynos.versions.ver_7.ver_7_0_0.lldp\
            .LLDP(pynos.utilities.return_xml)
        self.namespace = 'urn:brocade.com:mgmt:brocade-lldp-ext'
        self.netconf_namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'

    def lldp_neighbors_xml(self, *args):
        message_id = 'urn:uuid:528cdf32-2e86-11e5-bb27-080027b782e4'
        neighbor_xml = ('<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '
                        'message-id="{2}"><ns1:lldp-neighbor-detail>'
                        '<ns1:local-interface-name>Fo 226/0/7'
                        '</ns1:local-interface-name>'
                        '<ns1:local-interface-ifindex>402882566'
                        '</ns1:local-interface-ifindex>'
                        '<ns1:local-interface-mac>0005.33e5.d764'
                        '</ns1:local-interface-mac><ns1:remote-interface-name>'
                        'port0</ns1:remote-interface-name>'
                        '<ns1:remote-interface-mac>8c7c.ff02.f100'
                        '</ns1:remote-interface-mac><ns1:dead-interval>120'
                        '</ns1:dead-interval><ns1:remaining-life>102'
                        '</ns1:remaining-life><ns1:remote-chassis-id>'
                        '8c7c.ff02.f100</ns1:remote-chassis-id>'
                        '<ns1:lldp-pdu-transmitted>5397'
                        '</ns1:lldp-pdu-transmitted><ns1:lldp-pdu-received>'
                        '5263</ns1:lldp-pdu-received>'
                        '<ns1:remote-system-description>hodor'
                        '</ns1:remote-system-description>'
                        '<ns1:remote-management-address>1.1.1.1'
                        '</ns1:remote-management-address>'
                        '</ns1:lldp-neighbor-detail><ns1:has-more>false'
                        '</ns1:has-more>'
                        '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                                  self.namespace,
                                                  message_id))
        return ET.fromstring(neighbor_xml)

    def lldp_neighbors_xml_missing_remote_system_description(self, *args):
        message_id = 'urn:uuid:528cdf32-2e86-11e5-bb27-080027b782e4'
        neighbor_xml = ('<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '
                        'message-id="{2}"><ns1:lldp-neighbor-detail>'
                        '<ns1:local-interface-name>Fo 226/0/7'
                        '</ns1:local-interface-name>'
                        '<ns1:local-interface-ifindex>402882566'
                        '</ns1:local-interface-ifindex>'
                        '<ns1:local-interface-mac>0005.33e5.d764'
                        '</ns1:local-interface-mac><ns1:remote-interface-name>'
                        'port0</ns1:remote-interface-name>'
                        '<ns1:remote-interface-mac>8c7c.ff02.f100'
                        '</ns1:remote-interface-mac><ns1:dead-interval>120'
                        '</ns1:dead-interval><ns1:remaining-life>102'
                        '</ns1:remaining-life><ns1:remote-chassis-id>'
                        '8c7c.ff02.f100</ns1:remote-chassis-id>'
                        '<ns1:lldp-pdu-transmitted>5397'
                        '</ns1:lldp-pdu-transmitted><ns1:lldp-pdu-received>'
                        '5263</ns1:lldp-pdu-received>'
                        '<ns1:remote-management-address>1.1.1.1'
                        '</ns1:remote-management-address>'
                        '</ns1:lldp-neighbor-detail><ns1:has-more>false'
                        '</ns1:has-more>'
                        '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                                  self.namespace,
                                                  message_id))
        return ET.fromstring(neighbor_xml)

    def lldp_neighbors_xml_missing_remote_management_address(self, *args):
        message_id = 'urn:uuid:528cdf32-2e86-11e5-bb27-080027b782e4'
        neighbor_xml = ('<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '
                        'message-id="{2}"><ns1:lldp-neighbor-detail>'
                        '<ns1:local-interface-name>Fo 226/0/7'
                        '</ns1:local-interface-name>'
                        '<ns1:local-interface-ifindex>402882566'
                        '</ns1:local-interface-ifindex>'
                        '<ns1:local-interface-mac>0005.33e5.d764'
                        '</ns1:local-interface-mac><ns1:remote-interface-name>'
                        'port0</ns1:remote-interface-name>'
                        '<ns1:remote-interface-mac>8c7c.ff02.f100'
                        '</ns1:remote-interface-mac><ns1:dead-interval>120'
                        '</ns1:dead-interval><ns1:remaining-life>102'
                        '</ns1:remaining-life><ns1:remote-chassis-id>'
                        '8c7c.ff02.f100</ns1:remote-chassis-id>'
                        '<ns1:lldp-pdu-transmitted>5397'
                        '</ns1:lldp-pdu-transmitted><ns1:lldp-pdu-received>'
                        '5263</ns1:lldp-pdu-received>'
                        '<ns1:remote-system-description>hodor'
                        '</ns1:remote-system-description>'
                        '</ns1:lldp-neighbor-detail><ns1:has-more>false'
                        '</ns1:has-more>'
                        '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                                  self.namespace,
                                                  message_id))
        return ET.fromstring(neighbor_xml)

    def test_neighbors(self):
        expected = {'local-int-name': 'FortyGigabitEthernet 226/0/7',
                    'local-int-mac': '0005.33e5.d764',
                    'remote-int-name': 'port0',
                    'remote-int-mac': '8c7c.ff02.f100',
                    'remote-chassis-id': '8c7c.ff02.f100',
                    'remote-system-name': '',
                    'remote-management-address': '1.1.1.1',
                    'remote-system-description': 'hodor'}

        self.lldp._callback = self.lldp_neighbors_xml
        results = self.lldp.neighbors()
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected, results[0])

    def test_neighbors_missing_remote_system_description(self):
        expected = {'local-int-name': 'FortyGigabitEthernet 226/0/7',
                    'local-int-mac': '0005.33e5.d764',
                    'remote-int-name': 'port0',
                    'remote-int-mac': '8c7c.ff02.f100',
                    'remote-chassis-id': '8c7c.ff02.f100',
                    'remote-system-name': '',
                    'remote-management-address': '1.1.1.1',
                    'remote-system-description': ''}

        self.lldp._callback = getattr(self,
                                      'lldp_neighbors_xml_'
                                      'missing_remote_system_description')
        results = self.lldp.neighbors()
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected, results[0])

    def test_neighbors_missing_remote_management_address(self):
        expected = {'local-int-name': 'FortyGigabitEthernet 226/0/7',
                    'local-int-mac': '0005.33e5.d764',
                    'remote-int-name': 'port0',
                    'remote-int-mac': '8c7c.ff02.f100',
                    'remote-chassis-id': '8c7c.ff02.f100',
                    'remote-system-name': '',
                    'remote-management-address': '',
                    'remote-system-description': 'hodor'}

        self.lldp._callback = getattr(self,
                                      'lldp_neighbors_xml_'
                                      'missing_remote_management_address')
        results = self.lldp.neighbors()
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected, results[0])

    def test_get_lldp_neighbors_request(self):
        expected = ('<get-lldp-neighbor-detail xmlns="{0}"><last-rcvd-ifindex>'
                    '1</last-rcvd-ifindex></get-lldp-neighbor-detail>'
                    .format(self.namespace))
        results = ET.tostring(self.lldp.get_lldp_neighbors_request('1', None))
        self.assertEqual(expected, results)
