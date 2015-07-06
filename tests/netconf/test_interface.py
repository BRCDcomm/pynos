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
from pynos.netconf.interface import Interface
import xml.etree.ElementTree as ET

_MOCK = Mock()


def _callback(out):
    """
    Callback to place value inside mock for testing results.
    """
    _MOCK.return_value = out


class TestInter(unittest.TestCase):
    """
    Interface unit tests. Compare expected XML to generated XML.
    """
    def test_add_vlan_int(self):
        """
        Test add VLAN Interface.
        """
        output = '<config><interface-vlan xmlns="urn:brocade.com:mgmt:brocade-\
interface"><interface><vlan><name>10</name></vlan></interface></interface-vlan\
></config>'
        inter = Interface(_callback)
        inter.add_vlan_int('10')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_del_vlan_int(self):
        """
        Test delete VLAN Interface.
        """
        output = '<config><interface-vlan xmlns="urn:brocade.com:mgmt:brocade-\
interface"><interface><vlan operation="delete"><name>10</name></vlan></interfa\
ce></interface-vlan></config>'

        inter = Interface(_callback)
        inter.del_vlan_int('10')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_enable_switchport(self):
        """
        Test enabling switchport.
        """
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-inter\
face"><tengigabitethernet><name>1/0/1</name><switchport-basic><basic /></switc\
hport-basic></tengigabitethernet></interface></config>'

        inter = Interface(_callback)
        inter.enable_switchport('tengigabitethernet', '1/0/1')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_disable_switchport(self):
        """
        Test disable switchport.
        """
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-inter\
face"><tengigabitethernet><name>1/0/1</name><switchport-basic operation="delet\
e" /></tengigabitethernet></interface></config>'

        inter = Interface(_callback)
        inter.disable_switchport('tengigabitethernet', '1/0/1')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_access_vlan(self):
        """
        Test add access VLAN.
        """
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-inter\
face"><tengigabitethernet><name>1/0/1</name><switchport><access><accessvlan>10\
</accessvlan></access></switchport></tengigabitethernet></interface></config>'

        inter = Interface(_callback)
        inter.access_vlan('tengigabitethernet', '1/0/1', '10')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_del_access_vlan(self):
        """
        Test delete access VLAN.
        """
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-inter\
face"><tengigabitethernet><name>1/0/1</name><switchport><access><accessvlan op\
eration="delete">10</accessvlan></access></switchport></tengigabitethernet></i\
nterface></config>'

        inter = Interface(_callback)
        inter.del_access_vlan('tengigabitethernet', '1/0/1', '10')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_set_ip(self):
        """
        Test add IP address.
        """
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-inter\
face"><tengigabitethernet><name>1/0/1</name><ip><ip-config xmlns="urn:brocade.\
com:mgmt:brocade-ip-config"><address><address>10.0.0.1/24</address></address><\
/ip-config></ip></tengigabitethernet></interface></config>'

        inter = Interface(_callback)
        inter.set_ip('tengigabitethernet', '1/0/1', '10.0.0.1/24')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_del_ip(self):
        """
        Test delete IP address.
        """
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-inter\
face"><tengigabitethernet><name>1/0/1</name><ip><ip-config xmlns="urn:brocade.\
com:mgmt:brocade-ip-config"><address operation="delete"><address>10.0.0.1/24</\
address></address></ip-config></ip></tengigabitethernet></interface></config>'

        inter = Interface(_callback)
        inter.del_ip('tengigabitethernet', '1/0/1', '10.0.0.1/24')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()
