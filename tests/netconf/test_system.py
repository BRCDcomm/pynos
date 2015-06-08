#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Inc.

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
from mock import Mock
from pynos.netconf.system import System
import xml.etree.ElementTree as ET

_MOCK = Mock()

def _callback(out):
    """
    Callback to place value inside mock for testing results.
    """
    _MOCK.return_value = out

class TestSystem(unittest.TestCase):
    """
    System unit tests. Compare expected XML to generated XML.
    """
    def test_add_snmp_community(self):
        """
        Test adding an SNMP community.
        """
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><community><community>test</community></community></snmp-server></config>'

        system = System(_callback)
        system.add_snmp_community('test')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_del_snmp_community(self):
        """
        Test delete SNMP community.
        """
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><community operation="delete"><community>test</community></community></snmp-s\
erver></config>'

        system = System(_callback)
        system.del_snmp_community('test')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_add_snmp_host(self):
        """
        Test add snmp host.
        """
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><host><ip>10.0.0.1</ip><community>Public</community><udp-port>161</udp-port><\
/host></snmp-server></config>'

        system = System(_callback)
        system.add_snmp_host(('10.0.0.1', '161'))
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_del_snmp_host(self):
        """
        Test delete snmp host.
        """
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><host operation="delete"><ip>10.0.0.1</ip><community>Public</community><udp-p\
ort>161</udp-port></host></snmp-server></config>'

        system = System(_callback)
        system.del_snmp_host(('10.0.0.1', '161'))
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()
