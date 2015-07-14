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
import xml.etree.ElementTree as ET
import pynos.versions.base.interface as interface
import pynos.utilities


class TestInterface(unittest.TestCase):
    """
    Interface unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.interface = interface.Interface(pynos.utilities.return_xml)
        self.namespace = 'urn:brocade.com:mgmt:brocade-interface'
        self.phys_int_type = 'gigabitethernet'
        self.phys_name = '1/0/0'
        self.vlan_id = '40'
        self.sec_vlan = '50'

    def test_description(self):
        expected = '<config>'\
                   '<interface xmlns="{}"><gigabitethernet>'\
                   '<name>1/0/0</name>'\
                   '<description>Hodor</description>'\
                   '</gigabitethernet></interface>'\
                   '</config>'.format(self.namespace)
        description = 'Hodor'
        result = self.interface.description(int_type=self.phys_int_type,
                                            name=self.phys_name,
                                            desc=description)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_description_exception(self):
        with self.assertRaises(KeyError):
            self.interface.description(int_type=self.phys_int_type,
                                       desc='Hodor')

    def test_private_vlan_type(self):
        expected = '<config>'\
                   '<interface-vlan xmlns="{}"><interface>'\
                   '<vlan><name>40</name><private-vlan>'\
                   '<pvlan-type-leaf>isolated</pvlan-type-leaf>'\
                   '</private-vlan></vlan></interface></interface-vlan>'\
                   '</config>'.format(self.namespace)
        result = self.interface.private_vlan_type(name=self.vlan_id,
                                                  pvlan_type='isolated')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_private_vlan_type_exception(self):
        with self.assertRaises(KeyError):
            self.interface.private_vlan_type(name=self.vlan_id)

    def test_vlan_pvlan_association_add(self):
        expected = '<config><interface-vlan xmlns="{}"><interface><vlan>'\
                   '<name>{}</name><private-vlan><association>'\
                   '<sec-assoc-add>{}</sec-assoc-add></association>'\
                   '</private-vlan></vlan></interface></interface-vlan>'\
                   '</config>'.format(self.namespace,
                                      self.vlan_id,
                                      self.sec_vlan)
        interface = self.interface
        result = interface.vlan_pvlan_association_add(name=self.vlan_id,
                                                      sec_vlan=self.sec_vlan)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vlan_pvlan_association_add_exception(self):
        with self.assertRaises(KeyError):
            self.interface.vlan_pvlan_association_add(name=self.vlan_id)

    def test_pvlan_host_association(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><private-vlan><host-association>'\
                   '<host-pri-pvlan>{3}</host-pri-pvlan>'\
                   '<host-sec-pvlan>{4}</host-sec-pvlan></host-association>'\
                   '</private-vlan></switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, self.vlan_id,
                                      self.sec_vlan)
        interface = self.interface
        result = interface.pvlan_host_association(int_type=self.phys_int_type,
                                                  name=self.phys_name,
                                                  pri_vlan=self.vlan_id,
                                                  sec_vlan=self.sec_vlan)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_pvlan_host_association_exception(self):
        with self.assertRaises(KeyError):
            self.interface.pvlan_host_association(name=self.vlan_id)

    def test_admin_state_disabled(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<shutdown /></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.admin_state(int_type=self.phys_int_type,
                                            name=self.phys_name,
                                            enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_admin_state_enabled(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<shutdown operation="delete" /></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.admin_state(int_type=self.phys_int_type,
                                            name=self.phys_name,
                                            enabled=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_admin_state_exception(self):
        with self.assertRaises(KeyError):
            self.interface.admin_state(name=self.phys_name)
