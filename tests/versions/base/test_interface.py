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
import pynos.versions.base.interface as interface
from pynos.exceptions import InvalidVlanId
import pynos.utilities


class TestInterface(unittest.TestCase):

    """
    Interface unit tests. Compare expected XML to generated XML.
    """

    def setUp(self):
        self.interface = interface.Interface(pynos.utilities.return_xml)
        self.namespace = 'urn:brocade.com:mgmt:brocade-interface'
        self.phys_int_type = 'gigabitethernet'
        self.phys_vlan_type = 'vlan'
        self.phys_port_channel_type = 'port-channel'
        self.phys_name = '1/0/0'
        self.port_channel_name = '20'
        self.vlan_id = '40'
        self.sec_vlan = '50'
        self.ipv4_config_namespace = 'urn:brocade.com:mgmt:brocade-ip-config'
        self.ipv4_address = '20.10.10.1/24'
        self.ipv6_address = 'fc00:1:3:1ad3:0:0:23:a/64'
        self.ipv6_config_namespace = 'urn:brocade.com:mgmt:brocade-ipv6-config'
        self.port_channel_namespace = 'urn:brocade.com:mgmt:brocade-lag'
        self.netconf_namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'
        self.count = 0

    def raise_exception(self, *args, **kwargs):
        raise Exception()

    def raise_attribute_error(self, *args, **kwargs):
        raise AttributeError()

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

    def test_trunk_allowed_vlan_add(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><allowed><vlan><add>{3}</add></vlan>'\
                   '</allowed></trunk></switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, self.vlan_id)
        result = self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                                   name=self.phys_name,
                                                   vlan=self.vlan_id,
                                                   action='add')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_allowed_vlan_remove(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><allowed><vlan><remove>{3}</remove>'\
                   '</vlan></allowed></trunk></switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, self.vlan_id)
        result = self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                                   name=self.phys_name,
                                                   vlan=self.vlan_id,
                                                   action='remove')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_allowed_vlan_all(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><allowed><vlan><all /></vlan>'\
                   '</allowed></trunk></switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                                   name=self.phys_name,
                                                   vlan=self.vlan_id,
                                                   action='all')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_allowed_vlan_none(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><allowed><vlan><none /></vlan>'\
                   '</allowed></trunk></switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                                   name=self.phys_name,
                                                   vlan=self.vlan_id,
                                                   action='none')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_allowed_vlan_add_ctag(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><trunk-vlan-classification><allowed>'\
                   '<vlan><add><trunk-vlan-id>{3}</trunk-vlan-id>'\
                   '<trunk-ctag-range>{4}</trunk-ctag-range></add></vlan>'\
                   '</allowed></trunk-vlan-classification></trunk>'\
                   '</switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, self.vlan_id,
                                      self.sec_vlan)
        result = self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                                   name=self.phys_name,
                                                   vlan=self.vlan_id,
                                                   ctag=self.sec_vlan,
                                                   action='add')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_allowed_vlan_remove_ctag(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><trunk-vlan-classification><allowed>'\
                   '<vlan><remove><trunk-vlan-id>{3}</trunk-vlan-id>'\
                   '<trunk-ctag-range>{4}</trunk-ctag-range></remove></vlan>'\
                   '</allowed></trunk-vlan-classification></trunk>'\
                   '</switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, self.vlan_id,
                                      self.sec_vlan)
        result = self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                                   name=self.phys_name,
                                                   vlan=self.vlan_id,
                                                   ctag=self.sec_vlan,
                                                   action='remove')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_allowed_vlan_exception(self):
        with self.assertRaises(KeyError):
            self.interface.trunk_allowed_vlan(name=self.phys_name)

    def test_mtu(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<mtu>1666</mtu></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.mtu(int_type=self.phys_int_type,
                                    name=self.phys_name,
                                    mtu='1666')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_mtu_exception(self):
        with self.assertRaises(KeyError):
            self.interface.mtu(name=self.phys_name)

    def test_spanning_tree_state_phys_enabled(self):
        stp_namespace = 'urn:brocade.com:mgmt:brocade-xstp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<spanning-tree xmlns="{3}">'\
                   '<shutdown operation="delete" /></spanning-tree></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name,
                                                  stp_namespace)
        interface = self.interface
        result = interface.spanning_tree_state(int_type=self.phys_int_type,
                                               name=self.phys_name,
                                               enabled=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_phys_disabled(self):
        stp_namespace = 'urn:brocade.com:mgmt:brocade-xstp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<spanning-tree xmlns="{3}"><shutdown /></spanning-tree>'\
                   '</{1}></interface></config>'.format(self.namespace,
                                                        self.phys_int_type,
                                                        self.phys_name,
                                                        stp_namespace)
        interface = self.interface
        result = interface.spanning_tree_state(int_type=self.phys_int_type,
                                               name=self.phys_name,
                                               enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_vlan_enabled(self):
        stp_namespace = 'urn:brocade.com:mgmt:brocade-xstp'
        expected = '<config><interface-vlan xmlns="{0}"><interface><vlan>'\
                   '<name>{1}</name><spanning-tree xmlns="{2}">'\
                   '<stp-shutdown operation="delete" /></spanning-tree>'\
                   '</vlan></interface></interface-vlan>'\
                   '</config>'.format(self.namespace, self.vlan_id,
                                      stp_namespace)
        interface = self.interface
        result = interface.spanning_tree_state(int_type='vlan',
                                               name=self.vlan_id,
                                               enabled=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_vlan_disabled(self):
        stp_namespace = 'urn:brocade.com:mgmt:brocade-xstp'
        expected = '<config><interface-vlan xmlns="{0}"><interface><vlan>'\
                   '<name>{1}</name><spanning-tree xmlns="{2}">'\
                   '<stp-shutdown /></spanning-tree>'\
                   '</vlan></interface></interface-vlan>'\
                   '</config>'.format(self.namespace, self.vlan_id,
                                      stp_namespace)
        interface = self.interface
        result = interface.spanning_tree_state(int_type='vlan',
                                               name=self.vlan_id,
                                               enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_port_channel_enabled(self):
        stp_namespace = 'urn:brocade.com:mgmt:brocade-xstp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<spanning-tree xmlns="{3}">'\
                   '<shutdown operation="delete" /></spanning-tree></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_port_channel_type,
                                                  self.port_channel_name,
                                                  stp_namespace)
        interface = self.interface
        result = interface.spanning_tree_state(
            int_type='port_channel', name=self.port_channel_name,
            enabled=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_port_channel_disabled(self):
        stp_namespace = 'urn:brocade.com:mgmt:brocade-xstp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<spanning-tree xmlns="{3}"><shutdown /></spanning-tree>'\
                   '</{1}></interface>'\
                   '</config>'.format(self.namespace,
                                      self.phys_port_channel_type,
                                      self.port_channel_name, stp_namespace)
        interface = self.interface
        result = interface.spanning_tree_state(
            int_type='port_channel',
            name=self.port_channel_name,
            enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_exception(self):
        with self.assertRaises(KeyError):
            self.interface.spanning_tree_state(name=self.phys_name)

    def test_private_vlan_mode(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><mode><private-vlan><host /></private-vlan>'\
                   '</mode></switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.private_vlan_mode(int_type=self.phys_int_type,
                                                  name=self.phys_name,
                                                  mode='host')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_private_vlan_mode_exception(self):
        with self.assertRaises(KeyError):
            self.interface.private_vlan_mode(name=self.vlan_id)

    def test_vrrp_vip_ipv4(self):
        namespace = 'urn:brocade.com:mgmt:brocade-vrrp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<vrrp xmlns="{3}"><vrid>1</vrid><version>3</version>'\
                   '<virtual-ip><virtual-ipaddr>10.10.10.10</virtual-ipaddr>'\
                   '</virtual-ip></vrrp></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, namespace)

        result = self.interface.vrrp_vip(int_type=self.phys_int_type, vrid='1',
                                         name=self.phys_name,
                                         vip='10.10.10.10/24')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_vip_ipv6(self):
        namespace = 'urn:brocade.com:mgmt:brocade-vrrpv3'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ipv6><vrrpv3-group xmlns="{3}"><vrid>1</vrid>'\
                   '<virtual-ip><virtual-ipaddr>2001::1</virtual-ipaddr>'\
                   '</virtual-ip></vrrpv3-group></ipv6></gigabitethernet>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name,
                                                  namespace)

        result = self.interface.vrrp_vip(int_type=self.phys_int_type, vrid='1',
                                         name=self.phys_name, vip='2001::1/64')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_vip_exception(self):
        with self.assertRaises(KeyError):
            self.interface.vrrp_vip()

    def test_vrrp_priority_ipv4(self):
        namespace = 'urn:brocade.com:mgmt:brocade-vrrp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<vrrp xmlns="{3}"><vrid>1</vrid><version>3</version>'\
                   '<priority>50</priority></vrrp></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, namespace)
        result = self.interface.vrrp_priority(int_type=self.phys_int_type,
                                              name=self.phys_name,
                                              priority='50', vrid='1',
                                              ip_version='4')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_priority_ipv6(self):
        namespace = 'urn:brocade.com:mgmt:brocade-vrrpv3'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ipv6><vrrpv3-group xmlns="{3}"><vrid>1</vrid>'\
                   '<priority>50</priority></vrrpv3-group></ipv6></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name, namespace)
        result = self.interface.vrrp_priority(int_type=self.phys_int_type,
                                              name=self.phys_name,
                                              priority='50', vrid='1',
                                              ip_version='6')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_vrrp_priority_exception(self):
        with self.assertRaises(KeyError):
            self.interface.vrrp_priority()

    def test_proxy_arp_enabled(self):
        namespace = 'urn:brocade.com:mgmt:brocade-ip-config'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ip><ip-config xmlns="{3}"><proxy-arp /></ip-config></ip>'\
                   '</{1}></interface></config>'.format(self.namespace,
                                                        self.phys_int_type,
                                                        self.phys_name,
                                                        namespace)
        result = self.interface.proxy_arp(int_type=self.phys_int_type,
                                          name=self.phys_name, enabled=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_proxy_arp_disabled(self):
        namespace = 'urn:brocade.com:mgmt:brocade-ip-config'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ip><ip-config xmlns="{3}">'\
                   '<proxy-arp operation="delete" /></ip-config></ip>'\
                   '</{1}></interface></config>'.format(self.namespace,
                                                        self.phys_int_type,
                                                        self.phys_name,
                                                        namespace)
        result = self.interface.proxy_arp(int_type=self.phys_int_type,
                                          name=self.phys_name, enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_proxy_arp_exception(self):
        with self.assertRaises(KeyError):
            self.interface.proxy_arp()

    def test_lacp_timeout_short(self):
        namespace = 'urn:brocade.com:mgmt:brocade-lacp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<lacp xmlns="{3}"><timeout>short</timeout></lacp></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name, namespace)
        result = self.interface.lacp_timeout(int_type=self.phys_int_type,
                                             name=self.phys_name,
                                             timeout='short')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_lacp_timeout_long(self):
        namespace = 'urn:brocade.com:mgmt:brocade-lacp'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<lacp xmlns="{3}"><timeout>long</timeout></lacp></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name, namespace)
        result = self.interface.lacp_timeout(int_type=self.phys_int_type,
                                             name=self.phys_name,
                                             timeout='long')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_lacp_timeout_exception(self):
        with self.assertRaises(KeyError):
            self.interface.lacp_timeout()

    def test_transport_service(self):
        expected = '<config><interface-vlan xmlns="{0}"><interface><vlan>'\
                   '<name>{1}</name><transport-service>1</transport-service>'\
                   '</vlan></interface></interface-vlan>'\
                   '</config>'.format(self.namespace, self.vlan_id)
        result = self.interface.transport_service(vlan=self.vlan_id,
                                                  service_id='1')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_transport_service_exception(self):
        with self.assertRaises(KeyError):
            self.interface.transport_service()

    def test_port_channel_minimum_links(self):
        expected = '<config><interface xmlns="{0}"><port-channel><name>'\
                   '3</name><minimum-links>2</minimum-links></port-channel>'\
                   '</interface></config>'.format(self.namespace)
        result = self.interface.port_channel_minimum_links(name='3',
                                                           minimum_links='2')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_port_channel_minimum_links_exception(self):
        with self.assertRaises(KeyError):
            self.interface.port_channel_minimum_links()

    def test_fabric_isl_enabled(self):
        namespace = 'urn:brocade.com:mgmt:brocade-fcoe'
        expected = '<config><interface xmlns="{0}"><tengigabitethernet><name>'\
                   '{1}</name><fabric xmlns="{2}"><fabric-isl>'\
                   '<fabric-isl-enable /></fabric-isl></fabric>'\
                   '</tengigabitethernet></interface>'\
                   '</config>'.format(self.namespace, self.phys_name,
                                      namespace)
        result = self.interface.fabric_isl(int_type='tengigabitethernet',
                                           name=self.phys_name)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_fabric_isl_disabled(self):
        namespace = 'urn:brocade.com:mgmt:brocade-fcoe'
        expected = '<config><interface xmlns="{0}"><tengigabitethernet><name>'\
                   '{1}</name><fabric xmlns="{2}">'\
                   '<fabric-isl operation="delete"><fabric-isl-enable />'\
                   '</fabric-isl></fabric></tengigabitethernet></interface>'\
                   '</config>'.format(self.namespace, self.phys_name,
                                      namespace)
        result = self.interface.fabric_isl(int_type='tengigabitethernet',
                                           name=self.phys_name, enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_fabric_isl_exception(self):
        with self.assertRaises(KeyError):
            self.interface.fabric_isl()

    def test_fabric_trunk_enabled(self):
        namespace = 'urn:brocade.com:mgmt:brocade-fcoe'
        expected = '<config><interface xmlns="{0}"><tengigabitethernet><name>'\
                   '{1}</name><fabric xmlns="{2}"><fabric-trunk>'\
                   '<fabric-trunk-enable /></fabric-trunk></fabric>'\
                   '</tengigabitethernet></interface>'\
                   '</config>'.format(self.namespace, self.phys_name,
                                      namespace)
        result = self.interface.fabric_trunk(int_type='tengigabitethernet',
                                             name=self.phys_name)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_fabric_trunk_disabled(self):
        namespace = 'urn:brocade.com:mgmt:brocade-fcoe'
        expected = '<config><interface xmlns="{0}"><tengigabitethernet><name>'\
                   '{1}</name><fabric xmlns="{2}">'\
                   '<fabric-trunk operation="delete"><fabric-trunk-enable />'\
                   '</fabric-trunk></fabric></tengigabitethernet></interface>'\
                   '</config>'.format(self.namespace, self.phys_name,
                                      namespace)
        result = self.interface.fabric_trunk(int_type='tengigabitethernet',
                                             name=self.phys_name,
                                             enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_fabric_trunk_exception(self):
        with self.assertRaises(KeyError):
            self.interface.fabric_trunk()

    def test_channel_group_brocade(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<channel-group><mode>active</mode><port-int>5</port-int>'\
                   '<type>brocade</type></channel-group></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.channel_group(int_type=self.phys_int_type,
                                              name=self.phys_name,
                                              mode='active', port_int='5',
                                              channel_type='brocade')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_channel_group_standard(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<channel-group><mode>active</mode><port-int>5</port-int>'\
                   '<type>standard</type></channel-group></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.channel_group(int_type=self.phys_int_type,
                                              name=self.phys_name,
                                              mode='active', port_int='5',
                                              channel_type='standard')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_channel_group_exception(self):
        with self.assertRaises(KeyError):
            self.interface.channel_group()

    def test_port_channel_vlag_ignore_split_enabled(self):
        expected = '<config><interface xmlns="{0}"><port-channel>'\
                   '<name>5</name><vlag><ignore-split /></vlag>'\
                   '</port-channel></interface>'\
                   '</config>'.format(self.namespace)
        result = self.interface.port_channel_vlag_ignore_split(name='5',
                                                               enabled=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_port_channel_vlag_ignore_split_disabled(self):
        expected = '<config><interface xmlns="{0}"><port-channel>'\
                   '<name>5</name><vlag><ignore-split operation="delete" />'\
                   '</vlag></port-channel></interface>'\
                   '</config>'.format(self.namespace)
        result = self.interface.port_channel_vlag_ignore_split(name='5',
                                                               enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_port_channel_vlag_ignore_split_exception(self):
        with self.assertRaises(KeyError):
            self.interface.port_channel_vlag_ignore_split()

    def test_tag_native_vlan_enabled(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><tag><native-vlan /></tag></trunk>'\
                   '</switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.tag_native_vlan(int_type=self.phys_int_type,
                                                name=self.phys_name)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_tag_native_vlan_disabled(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><trunk><tag>'\
                   '<native-vlan operation="delete" /></tag></trunk>'\
                   '</switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.tag_native_vlan(int_type=self.phys_int_type,
                                                name=self.phys_name,
                                                enabled=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_tag_native_vlan_exception(self):
        with self.assertRaises(KeyError):
            self.interface.tag_native_vlan()

    def test_v6_nd_suppress_ra(self):
        ra_namespace = 'urn:brocade.com:mgmt:brocade-ipv6-nd-ra'
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ipv6><ipv6-nd-ra xmlns="{3}"><ipv6-intf-cmds><nd>'\
                   '<suppress-ra><suppress-ra-all /></suppress-ra></nd>'\
                   '</ipv6-intf-cmds></ipv6-nd-ra></ipv6></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, ra_namespace)
        result = self.interface.v6_nd_suppress_ra(int_type=self.phys_int_type,
                                                  name=self.phys_name)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_v6_nd_suppress_ra_interface_ve(self):
        rbridge_namespace = 'urn:brocade.com:mgmt:brocade-rbridge'
        ipv6_namespace = 'urn:brocade.com:mgmt:brocade-ipv6-config'
        ra_namespace = 'urn:brocade.com:mgmt:brocade-ipv6-nd-ra'
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>1'\
                   '</rbridge-id><interface xmlns="{1}"><ve><name>7</name>'\
                   '<ipv6 xmlns="{2}"><ipv6-nd-ra xmlns="{3}">'\
                   '<ipv6-intf-cmds><nd><suppress-ra><suppress-ra-all />'\
                   '</suppress-ra></nd></ipv6-intf-cmds></ipv6-nd-ra></ipv6>'\
                   '</ve></interface></rbridge-id>'\
                   '</config>'.format(rbridge_namespace, self.namespace,
                                      ipv6_namespace, ra_namespace)
        result = self.interface.v6_nd_suppress_ra(int_type='ve', name='7')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_v6_nd_suppress_ra_exception(self):
        with self.assertRaises(KeyError):
            self.interface.v6_nd_suppress_ra()

    def test_trunk_mode(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><mode><vlan-mode>trunk</vlan-mode></mode>'\
                   '</switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.trunk_mode(int_type=self.phys_int_type,
                                           name=self.phys_name, mode='trunk')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_trunk_mode_exception(self):
        with self.assertRaises(KeyError):
            self.interface.trunk_mode()

    def test_switchport_pvlan_mapping(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<switchport><private-vlan><mapping><promis-pri-pvlan>'\
                   '{3}</promis-pri-pvlan><promis-sec-pvlan-range>{4}'\
                   '</promis-sec-pvlan-range></mapping></private-vlan>'\
                   '</switchport></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name, self.vlan_id,
                                      self.sec_vlan)
        intf = self.interface
        result = intf.switchport_pvlan_mapping(int_type=self.phys_int_type,
                                               name=self.phys_name,
                                               pri_vlan=self.vlan_id,
                                               sec_vlan=self.sec_vlan)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_switchport_pvlan_mapping_exception(self):
        with self.assertRaises(KeyError):
            self.interface.switchport_pvlan_mapping()

    def test_ip_address_exception(self):
        with self.assertRaises(KeyError):
            self.interface.ip_address(name=self.phys_name)

    def test_ipv4_address_add(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ip><ip-config xmlns="{3}"><address><address>{4}'\
                   '</address></address></ip-config></ip></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name,
                                      self.ipv4_config_namespace,
                                      self.ipv4_address)
        result = self.interface.ip_address(int_type=self.phys_int_type,
                                           name=self.phys_name,
                                           ip_addr=self.ipv4_address,
                                           delete=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_ipv4_address_delete(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ip><ip-config xmlns="{3}"><address operation="delete">'\
                   '<address>{4}</address></address></ip-config></ip></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name,
                                                  self.ipv4_config_namespace,
                                                  self.ipv4_address)
        result = self.interface.ip_address(int_type=self.phys_int_type,
                                           name=self.phys_name,
                                           ip_addr=self.ipv4_address,
                                           delete=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_ipv6_address_add(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ipv6><ipv6-config xmlns="{3}"><address><ipv6-address>'\
                   '<address>{4}</address></ipv6-address></address>'\
                   '</ipv6-config></ipv6></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name,
                                      self.ipv6_config_namespace,
                                      self.ipv6_address)
        result = self.interface.ip_address(int_type=self.phys_int_type,
                                           name=self.phys_name,
                                           ip_addr=self.ipv6_address,
                                           delete=False)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_ipv6_address_delete(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<ipv6><ipv6-config xmlns="{3}"><address '\
                   'operation="delete"><ipv6-address><address>{4}</address>'\
                   '</ipv6-address></address></ipv6-config></ipv6></{1}>'\
                   '</interface></config>'.format(self.namespace,
                                                  self.phys_int_type,
                                                  self.phys_name,
                                                  self.ipv6_config_namespace,
                                                  self.ipv6_address)
        result = self.interface.ip_address(int_type=self.phys_int_type,
                                           name=self.phys_name,
                                           ip_addr=self.ipv6_address,
                                           delete=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_ip_address_int_type_exception(self):
        with self.assertRaises(ValueError):
            self.interface.ip_address(int_type='junk',
                                      name=self.phys_name,
                                      ip_addr=self.ipv6_address,
                                      delete=False)

    def test_ip_address_interface_name_exception(self):
        with self.assertRaises(ValueError):
            self.interface.ip_address(int_type=self.phys_int_type,
                                      name='junk',
                                      ip_addr=self.ipv6_address,
                                      delete=False)

    def test_remove_port_channel_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.remove_port_channel(port_int='2/0/3')

    def test_ip_address_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.ip_address(int_type='port_channel', name='225/0/20',
                                      ip_addr='10.0.0.1/30')

    def test_ip_address_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.ip_address(int_type='tengigabitethernet',
                                      name='225/0', ip_addr='10.0.0.1/30')

    def test_description_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.description(int_type='port-channel', name='5',
                                       desc='hodor')

    def test_description_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.description(int_type='gigabitethernet', name='5/0',
                                       desc='hodor')

    def test_description_vlan_name_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.description(int_type='vlan', name='9000',
                                       desc='hodor')

    def test_description_vlan(self):
        desc = 'Hodor'
        expected = '<config><interface-vlan xmlns="{0}"><interface><vlan>'\
                   '<name>{1}</name><description>{2}</description></vlan>'\
                   '</interface></interface-vlan>'\
                   '</config>'.format(self.namespace, self.vlan_id, desc)
        result = self.interface.description(int_type='vlan', name=self.vlan_id,
                                            desc=desc)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_private_vlan_type_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.private_vlan_type(name='9000',
                                             pvlan_type='primary')

    def test_private_vlan_type_pvlan_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.private_vlan_type(name='5', pvlan_type='hodor')

    def test_vlan_pvlan_association_add_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.vlan_pvlan_association_add(name='9000',
                                                      sec_vlan='5')

    def test_vlan_pvlan_association_add_sec_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.vlan_pvlan_association_add(name='5',
                                                      sec_vlan='9000')

    def test_add_vlan_int_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.add_vlan_int(self.vlan_id)
        self.assertEquals(expected, result)

    def test_del_vlan_int_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.del_vlan_int(self.vlan_id)
        self.assertEquals(expected, result)

    def test_enable_switchport_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.enable_switchport(self.phys_int_type,
                                                  self.phys_name)
        self.assertEquals(expected, result)

    def test_disable_switchport_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.disable_switchport(self.phys_int_type,
                                                   self.phys_name)
        self.assertEquals(expected, result)

    def test_access_vlan_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.access_vlan(self.phys_int_type, self.phys_name,
                                            self.vlan_id)
        self.assertEquals(expected, result)

    def test_del_access_vlan_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.del_access_vlan(self.phys_int_type,
                                                self.phys_name,
                                                self.vlan_id)
        self.assertEquals(expected, result)

    def test_set_ip_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.set_ip(self.phys_int_type, self.phys_name,
                                       self.ipv4_address)
        self.assertEquals(expected, result)

    def test_del_ip_exception(self):
        self.interface._callback = self.raise_exception
        expected = False
        result = self.interface.del_ip(self.phys_int_type, self.phys_name,
                                       self.ipv4_address)
        self.assertEquals(expected, result)

    def test_ip_address_attribute_error(self):
        self.interface._callback = self.raise_attribute_error
        expected = None
        result = self.interface.ip_address(int_type=self.phys_int_type,
                                           name=self.phys_name,
                                           ip_addr=self.ipv4_address)
        self.assertEquals(expected, result)

    def test_admin_state_attribute_error(self):
        self.interface._callback = self.raise_attribute_error
        expected = None
        result = self.interface.admin_state(int_type=self.phys_int_type,
                                            name=self.phys_name,
                                            enabled=True)
        self.assertEquals(expected, result)

    def test_spanning_tree_state_attribute_error(self):
        self.interface._callback = self.raise_attribute_error
        expected = None
        int_type = self.phys_int_type
        result = self.interface.spanning_tree_state(int_type=int_type,
                                                    name=self.phys_name,
                                                    enabled=True)
        self.assertEquals(expected, result)

    def test_tag_native_vlan_attribute_error(self):
        self.interface._callback = self.raise_attribute_error
        expected = None
        result = self.interface.tag_native_vlan(int_type=self.phys_int_type,
                                                name=self.phys_name,
                                                mode='trunk',
                                                enabled=True)
        self.assertEquals(expected, result)

    def test_proxy_arp_attribute_error(self):
        self.interface._callback = self.raise_attribute_error
        expected = None
        result = self.interface.proxy_arp(int_type=self.phys_int_type,
                                          name=self.phys_name,
                                          enabled=True)
        self.assertEquals(expected, result)

    def test_pvlan_host_association_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.pvlan_host_association(int_type='port-channel',
                                                  name='5',
                                                  pri_vlan=self.vlan_id,
                                                  sec_vlan=self.sec_vlan)

    def test_pvlan_host_association_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.pvlan_host_association(int_type='port_channel',
                                                  name='2/0',
                                                  pri_vlan=self.vlan_id,
                                                  sec_vlan=self.sec_vlan)

    def test_pvlan_host_association_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.pvlan_host_association(int_type='gigabitethernet',
                                                  name='2/0',
                                                  pri_vlan=self.vlan_id,
                                                  sec_vlan=self.sec_vlan)

    def test_pvlan_host_association_pri_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.pvlan_host_association(int_type='gigabitethernet',
                                                  name='2/0/1',
                                                  pri_vlan='9000',
                                                  sec_vlan=self.sec_vlan)

    def test_pvlan_host_association_sec_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.pvlan_host_association(int_type='gigabitethernet',
                                                  name='2/0/1',
                                                  pri_vlan=self.vlan_id,
                                                  sec_vlan='9000')

    def test_admin_state_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.admin_state(int_type='port-channel', name='5',
                                       enabled=True)

    def test_admin_state_bool_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.admin_state(int_type='port_channel', name='5',
                                       enabled='True')

    def test_admin_state_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.admin_state(int_type=self.phys_int_type, name='5',
                                       enabled='True')

    def test_admin_state_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.admin_state(int_type='port_channel', name='225/0/0',
                                       enabled='True')

    def test_trunk_allowed_vlan_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_allowed_vlan(int_type='port-channel',
                                              name='5', action='add',
                                              vlan=self.vlan_id,
                                              ctag=self.sec_vlan)

    def test_trunk_allowed_vlan_action_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_allowed_vlan(int_type='port_channel',
                                              name='5', action='hodor',
                                              vlan=self.vlan_id,
                                              ctag=self.sec_vlan)

    def test_trunk_allowed_vlan_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_allowed_vlan(int_type=self.phys_int_type,
                                              name='5/0', action='add',
                                              vlan=self.vlan_id,
                                              ctag=self.sec_vlan)

    def test_trunk_allowed_vlan_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_allowed_vlan(int_type='port_channel',
                                              name='2/0', action='add',
                                              vlan=self.vlan_id,
                                              ctag=self.sec_vlan)

    def test_trunk_allowed_vlan_ctag_missing_vlan_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_allowed_vlan(int_type='port_channel',
                                              name='2', action='add',
                                              ctag=self.sec_vlan)

    def test_trunk_allowed_vlan_ctag_action_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_allowed_vlan(int_type='port_channel',
                                              name='2/0', action='all',
                                              vlan=self.vlan_id,
                                              ctag=self.sec_vlan)

    def test_private_vlan_mode_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.private_vlan_mode(int_type='port-channel',
                                             name='2', mode='host')

    def test_private_vlan_mode_mode_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.private_vlan_mode(int_type='port_channel',
                                             name='2', mode='hodor')

    def test_private_vlan_mode_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.private_vlan_mode(int_type=self.phys_int_type,
                                             name='2/0', mode='host')

    def test_private_vlan_mode_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.private_vlan_mode(int_type='port_channel',
                                             name='3/0', mode='host')

    def test_spanning_tree_state_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.spanning_tree_state(int_type='port-channel',
                                               name='3', enabled=True)

    def test_spanning_tree_state_bool_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.spanning_tree_state(int_type='port_channel',
                                               name='3', enabled='hodor')

    def test_spanning_tree_state_vlan_name_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.spanning_tree_state(int_type='vlan',
                                               name='9000', enabled=True)

    def test_spanning_tree_state_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.spanning_tree_state(int_type=self.phys_int_type,
                                               name='9/0', enabled=True)

    def test_spanning_tree_state_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.spanning_tree_state(int_type='port_channel',
                                               name='9/0', enabled=True)

    def test_tag_native_vlan_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.tag_native_vlan(int_type='hodor', name='9')

    def test_tag_native_vlan_phys_int_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.tag_native_vlan(int_type=self.phys_int_type,
                                           name='9/0')

    def test_tag_native_vlan_port_channel_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.tag_native_vlan(int_type='port_channel', name='9/0')

    def test_tag_native_vlan_bool_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.tag_native_vlan(int_type='port_channel', name='9',
                                           enabled='hodor')

    def test_switchport_pvlan_mapping_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.switchport_pvlan_mapping(int_type='port-channel',
                                                    name='9',
                                                    pri_vlan=self.vlan_id,
                                                    sec_vlan=self.sec_vlan)

    def test_switchport_pvlan_mapping_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            int_type = self.phys_int_type
            self.interface.switchport_pvlan_mapping(int_type=int_type,
                                                    name='9/0',
                                                    pri_vlan=self.vlan_id,
                                                    sec_vlan=self.sec_vlan)

    def test_switchport_pvlan_mapping_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.switchport_pvlan_mapping(int_type='port_channel',
                                                    name='9/0',
                                                    pri_vlan=self.vlan_id,
                                                    sec_vlan=self.sec_vlan)

    def test_switchport_pvlan_mapping_pri_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.switchport_pvlan_mapping(int_type='port_channel',
                                                    name='9', pri_vlan='9000',
                                                    sec_vlan=self.sec_vlan)

    def test_switchport_pvlan_mapping_sec_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.switchport_pvlan_mapping(int_type='port_channel',
                                                    name='9', sec_vlan='9000',
                                                    pri_vlan=self.vlan_id)

    def test_mtu_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.mtu(int_type='port-channel', name='9', mtu='1522')

    def test_mtu_mtu_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.mtu(int_type='port_channel', name='9', mtu='9217')

    def test_mtu_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.mtu(int_type=self.phys_int_type, name='9/0',
                               mtu='1522')

    def test_mtu_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.mtu(int_type='port_channel', name='9/0', mtu='1522')

    def test_fabric_isl_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.fabric_isl(int_type=self.phys_int_type,
                                      name=self.phys_name)

    def test_fabric_isl_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.fabric_isl(int_type='tengigabitethernet',
                                      name='2/0')

    def test_fabric_isl_bool_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.fabric_isl(int_type='tengigabitethernet',
                                      name='2/0/0', enabled='hodor')

    def test_fabric_trunk_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.fabric_trunk(int_type=self.phys_int_type,
                                        name=self.phys_name)

    def test_fabric_trunk_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.fabric_trunk(int_type='tengigabitethernet',
                                        name='2/0')

    def test_fabric_trunk_bool_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.fabric_trunk(int_type='tengigabitethernet',
                                        name='2/0/0',
                                        enabled='hodor')

    def test_v6_nd_suppress_ra_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.v6_nd_suppress_ra(int_type='port_channel', name='5')

    def test_v6_nd_suppress_ra_ve_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.v6_nd_suppress_ra(int_type='ve', name='12345')

    def test_v6_nd_suppress_ra_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.v6_nd_suppress_ra(int_type=self.phys_int_type,
                                             name='2/0')

    def test_vrrp_vip_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.vrrp_vip(int_type='port-channel', name='5',
                                    vrid='1', vip='10.0.0.1')

    def test_vrrp_vip_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.vrrp_vip(int_type=self.phys_int_type, name='2/0',
                                    vrid='1', vip='10.0.0.1')

    def test_vrrp_vip_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.vrrp_vip(int_type='port_channel', name='2/0',
                                    vrid='1', vip='10.0.0.1')

    def test_vrrp_priority_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.vrrp_priority(int_type='port-channel', name='5',
                                         vrid='1', priority='75',
                                         ip_version='4')

    def test_vrrp_priority_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.vrrp_priority(int_type=self.phys_int_type,
                                         name='2/0', vrid='1', priority='75',
                                         ip_version='4')

    def test_vrrp_priority_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.vrrp_priority(int_type='port_channel', name='2/0',
                                         vrid='1', priority='75',
                                         ip_version='4')

    def test_proxy_arp_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.proxy_arp(int_type='port-channel', name='2')

    def test_proxy_arp_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.proxy_arp(int_type=self.phys_int_type, name='2/0')

    def test_proxy_arp_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.proxy_arp(int_type='port_channel', name='2/0')

    def test_proxy_arp_bool_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.proxy_arp(int_type='port_channel', name='2',
                                     enabled='hodor')

    def test_port_channel_minimum_links_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.port_channel_minimum_links(name=self.phys_name,
                                                      minimum_links='3')

    def test_channel_group_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.channel_group(int_type='port_channel', name='5',
                                         channel_type='standard', port_int='7',
                                         mode='active')

    def test_channel_group_channel_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.channel_group(int_type=self.phys_int_type,
                                         name=self.phys_name, mode='active',
                                         channel_type='hodor', port_int='7')

    def test_channel_group_mode_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.channel_group(int_type=self.phys_int_type,
                                         name=self.phys_name, mode='hodor',
                                         channel_type='standard', port_int='7')

    def test_channel_group_port_int_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.channel_group(int_type=self.phys_int_type,
                                         name=self.phys_name, mode='active',
                                         channel_type='standard',
                                         port_int='12345')

    def test_channel_group_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.channel_group(int_type=self.phys_int_type,
                                         name='2/0', mode='active',
                                         channel_type='standard', port_int='7')

    def test_channel_group_delete(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<channel-group operation="delete"><mode>active</mode>'\
                   '</channel-group></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.channel_group(int_type=self.phys_int_type,
                                              name=self.phys_name,
                                              mode='active', port_int='5',
                                              channel_type='brocade',
                                              delete=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_port_channel_vlag_ignore_split_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.port_channel_vlag_ignore_split(name='2/0',
                                                          enabled=True)

    def test_trunk_mode_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_mode(int_type='port-channel', name='5',
                                      mode='trunk')

    def test_trunk_mode_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_mode(int_type=self.phys_int_type,
                                      name='2/0', mode='trunk')

    def test_trunk_mode_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_mode(int_type='port_channel', name='2/0',
                                      mode='trunk')

    def test_trunk_mode_mode_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.trunk_mode(int_type=self.phys_int_type,
                                      name=self.phys_name, mode='hodor')

    def test_transport_service_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.transport_service(vlan='9000', service_id='1')

    def test_lacp_timeout_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.lacp_timeout(int_type='port_channel',
                                        name='225/0/1', timeout='long')

    def test_lacp_timeout_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.lacp_timeout(int_type=self.phys_int_type,
                                        name='5',
                                        timeout='5')

    def test_lacp_timeout_timeout_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.lacp_timeout(int_type=self.phys_int_type,
                                        name=self.phys_name, timeout='5')

    def test_switchport_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.switchport(int_type='port-channel',
                                      name=self.phys_name)

    def test_switchport_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.switchport(int_type=self.phys_int_type, name='2/0')

    def test_switchport_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.switchport(int_type='port_channel', name='2/0')

    def test_acc_vlan_int_type_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.acc_vlan(int_type='port-channel', name='5',
                                    vlan=self.vlan_id)

    def test_acc_vlan_vlan_value_error(self):
        with self.assertRaises(InvalidVlanId):
            self.interface.acc_vlan(int_type=self.phys_int_type,
                                    name=self.phys_name, vlan='9000')

    def test_acc_vlan_phys_int_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.acc_vlan(int_type=self.phys_int_type,
                                    name='2/0', vlan=self.vlan_id)

    def test_acc_vlan_port_channel_name_value_error(self):
        with self.assertRaises(ValueError):
            self.interface.acc_vlan(int_type='port_channel', name='2/0',
                                    vlan=self.vlan_id)

    def test_port_channel_vlag_ignore_split_enabled_default_value(self):
        expected = '<config><interface xmlns="{0}"><port-channel>'\
                   '<name>5</name><vlag><ignore-split /></vlag>'\
                   '</port-channel></interface>'\
                   '</config>'.format(self.namespace)
        result = self.interface.port_channel_vlag_ignore_split(name='5')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_mtu_too_low(self):
        with self.assertRaises(ValueError):
            self.interface.mtu(int_type=self.phys_int_type, mtu='1521',
                               name=self.phys_name)

    def test_mtu_too_high(self):
        with self.assertRaises(ValueError):
            self.interface.mtu(int_type=self.phys_int_type, mtu='9217',
                               name=self.phys_name)

    def test_mtu_floor(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<mtu>1522</mtu></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.mtu(int_type=self.phys_int_type, mtu='1522',
                                    name=self.phys_name)

        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_mtu_ceiling(self):
        expected = '<config><interface xmlns="{0}"><{1}><name>{2}</name>'\
                   '<mtu>9216</mtu></{1}></interface>'\
                   '</config>'.format(self.namespace, self.phys_int_type,
                                      self.phys_name)
        result = self.interface.mtu(int_type=self.phys_int_type, mtu='9216',
                                    name=self.phys_name)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def vlan_xml(self, *args):
        netconf_ns = "urn:ietf:params:xml:ns:netconf:base:1.0"
        interface_ns = "urn:brocade.com:mgmt:brocade-interface-ext"
        msg_id = "urn:uuid:7d752e80-8e8e-11e5-a4f1-005056c00008"
        vlans_xml = []
        vlan_xml = '<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" ' \
                   'message-id="{2}">' \
                   '<ns1:configured-vlans-count>3</ns1:configured-vlans-' \
                   'count>' \
                   '<ns1:provisioned-vlans-count>2</ns1:provisioned-vlans-' \
                   'count>' \
                   '<ns1:unprovisioned-vlans-count>1</ns1:unprovisioned-' \
                   'vlans-count>' \
                   '<ns1:vlan>' \
                   '<ns1:vlan-id>1</ns1:vlan-id>' \
                   '<ns1:vlan-type>static</ns1:vlan-type>' \
                   '<ns1:vlan-name>default</ns1:vlan-name>' \
                   '<ns1:vlan-state>suspend</ns1:vlan-state>' \
                   '<ns1:interface>' \
                   '<ns1:interface-type>tengigabitethernet</ns1:interface-' \
                   'type>' \
                   '<ns1:interface-name>226/0/11</ns1:interface-name>' \
                   '<ns1:tag>tagged</ns1:tag>' \
                   '</ns1:interface>' \
                   '</ns1:vlan>' \
                   '<ns1:last-vlan-id>1</ns1:last-vlan-id>' \
                   '<ns1:has-more>true</ns1:has-more>' \
                   '</ns0:rpc-reply>'.format(netconf_ns, interface_ns, msg_id)
        vlans_xml.append(ET.fromstring(vlan_xml))
        vlan_xml = '<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" ' \
                   'message-id="{2}">' \
                   '<ns1:configured-vlans-count>3</ns1:configured-vlans-' \
                   'count>' \
                   '<ns1:provisioned-vlans-count>2</ns1:provisioned-vlans-' \
                   'count>' \
                   '<ns1:unprovisioned-vlans-count>1</ns1:unprovisioned-' \
                   'vlans-count>' \
                   '<ns1:vlan>' \
                   '<ns1:vlan-id>2</ns1:vlan-id>' \
                   '<ns1:vlan-type>static</ns1:vlan-type>' \
                   '<ns1:vlan-name>default</ns1:vlan-name>' \
                   '<ns1:vlan-state>suspend</ns1:vlan-state>' \
                   '</ns1:vlan>' \
                   '<ns1:last-vlan-id>2</ns1:last-vlan-id>' \
                   '<ns1:has-more>false</ns1:has-more>' \
                   '</ns0:rpc-reply>'.format(netconf_ns, interface_ns, msg_id)
        vlans_xml.append(ET.fromstring(vlan_xml))
        return vlans_xml

    def test_vlans(self):
        expected_1 = {'vlan-id': '1',
                      'vlan-type': 'static',
                      'vlan-state': 'suspend',
                      'interface': [{'interface-name': '226/0/11',
                                     'interface-type': 'tengigabitethernet',
                                     'tag': 'tagged'}],
                      'interface-name': 'default'}
        expected_2 = {'vlan-id': '2',
                      'vlan-type': 'static',
                      'vlan-state': 'suspend',
                      'interface': [],
                      'interface-name': 'default'}
        self.interface._callback = self.vlan_side_effect
        results = self.interface.vlans
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected_1, results[0])
        self.assertDictEqual(expected_2, results[1])
        self.count = 0

    def vlan_side_effect(self, call, handler='edit_config', target='running',
                         source='startup'):
        vlan_xml = self.vlan_xml()[self.count]
        self.count += 1
        return vlan_xml

    def port_channel_xml(self, *args):
        message_id = 'urn:uuid:2ff00dc0-7d5d-11e5-991a-e06995e6af0a'
        result_xml = []
        neighbor_xml = '<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '\
                       'message-id="{2}"><ns1:lacp>'\
                       '<ns1:aggregator-id>1</ns1:aggregator-id>'\
                       '<ns1:aggregator-type>standard</ns1:aggregator-type>'\
                       '<ns1:isvlag>false</ns1:isvlag>'\
                       '<ns1:aggregator-mode>dynamic</ns1:aggregator-mode>'\
                       '<ns1:system-priority>32768</ns1:system-priority>'\
                       '<ns1:actor-system-id>01:e0:52:00:00:01' \
                       '</ns1:actor-system-id><ns1:partner-oper-priority>0' \
                       '</ns1:partner-oper-priority><ns1:partner-system-id>' \
                       '00:00:00:00:00:00</ns1:partner-system-id>' \
                       '<ns1:admin-key>1</ns1:admin-key><ns1:oper-key>1' \
                       '</ns1:oper-key><ns1:partner-oper-key>0' \
                       '</ns1:partner-oper-key><ns1:rx-link-count>0' \
                       '</ns1:rx-link-count><ns1:tx-link-count>0' \
                       '</ns1:tx-link-count><ns1:individual-agg>0' \
                       '</ns1:individual-agg><ns1:ready-agg>0' \
                       '</ns1:ready-agg><ns1:aggr-member><ns1:rbridge-id>'\
                       '51</ns1:rbridge-id><ns1:interface-type>' \
                       'tengigabitethernet</ns1:interface-type>' \
                       '<ns1:interface-name>51/0/1</ns1:interface-name>' \
                       '<ns1:actor-port>219446018048</ns1:actor-port>' \
                       '<ns1:sync>0</ns1:sync></ns1:aggr-member></ns1:lacp>'\
                       '<ns1:has-more>true</ns1:has-more>' \
                       '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                                 self.port_channel_namespace,
                                                 message_id)
        result_xml.append(ET.fromstring(neighbor_xml))
        neighbor_xml = '<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '\
                       'message-id="{2}"><ns1:lacp>'\
                       '<ns1:aggregator-id>2</ns1:aggregator-id>'\
                       '<ns1:aggregator-type>standard</ns1:aggregator-type>'\
                       '<ns1:isvlag>false</ns1:isvlag>'\
                       '<ns1:aggregator-mode>dynamic</ns1:aggregator-mode>'\
                       '<ns1:system-priority>32769</ns1:system-priority>'\
                       '<ns1:actor-system-id>01:e0:52:00:00:01' \
                       '</ns1:actor-system-id><ns1:partner-oper-priority>0' \
                       '</ns1:partner-oper-priority><ns1:partner-system-id>' \
                       '00:00:00:00:00:00</ns1:partner-system-id>' \
                       '<ns1:admin-key>1</ns1:admin-key><ns1:oper-key>1' \
                       '</ns1:oper-key><ns1:partner-oper-key>0' \
                       '</ns1:partner-oper-key><ns1:rx-link-count>0' \
                       '</ns1:rx-link-count><ns1:tx-link-count>0' \
                       '</ns1:tx-link-count><ns1:individual-agg>0' \
                       '</ns1:individual-agg><ns1:ready-agg>0' \
                       '</ns1:ready-agg><ns1:aggr-member><ns1:rbridge-id>'\
                       '51</ns1:rbridge-id><ns1:interface-type>' \
                       'tengigabitethernet</ns1:interface-type>' \
                       '<ns1:interface-name>51/0/2</ns1:interface-name>' \
                       '<ns1:actor-port>219446018049</ns1:actor-port>' \
                       '<ns1:sync>0</ns1:sync></ns1:aggr-member></ns1:lacp>'\
                       '<ns1:has-more>false</ns1:has-more>' \
                       '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                                 self.port_channel_namespace,
                                                 message_id)
        result_xml.append(ET.fromstring(neighbor_xml))
        return result_xml

    def test_port_channels(self):
        expected_1 = {'interface-name': 'port-channel-1',
                      'oper-key': '1',
                      'aggregator_id': '1',
                      'aggregator_type': 'standard',
                      'interfaces': [{'interface-type': 'tengigabitethernet',
                                      'rbridge-id': '51',
                                      'interface-name': '51/0/1',
                                      'sync': '0',
                                      'actor_port': '219446018048'}],
                      'aggregator_mode': 'dynamic',
                      'partner-oper-priority': '0',
                      'ready-agg': '0',
                      'rx-link-count': '0',
                      'tx-link-count': '0',
                      'individual-agg': '0',
                      'partner-oper-key': '0',
                      'partner-system-id': '00:00:00:00:00:00',
                      'actor_system_id': '01:e0:52:00:00:01',
                      'is_vlag': 'false',
                      'admin-key': '1',
                      'system_priority': '32768'}
        expected_2 = {'interface-name': 'port-channel-2',
                      'oper-key': '1',
                      'aggregator_id': '2',
                      'aggregator_type': 'standard',
                      'interfaces': [{'interface-type': 'tengigabitethernet',
                                      'rbridge-id': '51',
                                      'interface-name': '51/0/2',
                                      'sync': '0',
                                      'actor_port': '219446018049'}],
                      'aggregator_mode': 'dynamic',
                      'partner-oper-priority': '0',
                      'ready-agg': '0',
                      'rx-link-count': '0',
                      'tx-link-count': '0',
                      'individual-agg': '0',
                      'partner-oper-key': '0',
                      'partner-system-id': '00:00:00:00:00:00',
                      'actor_system_id': '01:e0:52:00:00:01',
                      'is_vlag': 'false',
                      'admin-key': '1',
                      'system_priority': '32769'}
        self.interface._callback = self.port_channel_side_effect
        results = self.interface.port_channels
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected_1, results[0])
        self.assertDictEqual(expected_2, results[1])
        self.count = 0

    def port_channel_side_effect(self, call, handler='edit_config',
                                 target='running', source='startup'):
        port_channel_xml = self.port_channel_xml()[self.count]
        self.count += 1
        return port_channel_xml
