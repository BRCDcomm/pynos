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
            self.interface.tag_native_vlan()

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
