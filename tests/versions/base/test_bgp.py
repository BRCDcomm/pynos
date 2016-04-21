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
import pynos.versions.base.bgp
import pynos.utilities


class TestBGP(unittest.TestCase):
    """
    BGP unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.bgp = pynos.versions.base.bgp.BGP(pynos.utilities.return_xml)
        self.rbridge_namespace = 'urn:brocade.com:mgmt:brocade-rbridge'
        self.bgp_namespace = 'urn:brocade.com:mgmt:brocade-bgp'
        self.rbridge_id = '2'

    def test_local_asn(self):
        expected = '<config>'\
                   '<rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">'\
                   '<rbridge-id>2</rbridge-id><router>'\
                   '<bgp xmlns="urn:brocade.com:mgmt:brocade-bgp">'\
                   '<vrf-name>x</vrf-name>'\
                   '<router-bgp-cmds-holder><router-bgp-attributes>'\
                   '<local-as>65535</local-as></router-bgp-attributes>'\
                   '</router-bgp-cmds-holder></bgp></router></rbridge-id>'\
                   '</config>'
        result = self.bgp.local_asn(local_as='65535', rbridge_id='2', vrf='x')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_local_asn_exception(self):
        with self.assertRaises(KeyError):
            self.bgp.local_asn(rbridge='2', vrf='x')

    def test_remove_bgp(self):
        expected = '<config>'\
                   '<rbridge-id xmlns="%s"><rbridge-id>1</rbridge-id><router>'\
                   '<bgp operation="delete" xmlns="%s">'\
                   '<vrf-name>default</vrf-name></bgp></router></rbridge-id>'\
                   '</config>' % (self.rbridge_namespace, self.bgp_namespace)
        result = ET.tostring(self.bgp.remove_bgp())
        self.assertEquals(expected, result)

    def test_neighbor_ipv4_enable(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><router><bgp xmlns="{2}"><vrf-name>x'\
                   '</vrf-name><router-bgp-cmds-holder>'\
                   '<router-bgp-attributes><neighbor-ips><neighbor-addr>'\
                   '<router-bgp-neighbor-address>10.10.10.10'\
                   '</router-bgp-neighbor-address><remote-as>65535'\
                   '</remote-as></neighbor-addr></neighbor-ips>'\
                   '</router-bgp-attributes></router-bgp-cmds-holder></bgp>'\
                   '</router></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace, self.rbridge_id,
                                      self.bgp_namespace)
        result = self.bgp.neighbor(remote_as='65535',
                                   rbridge_id=self.rbridge_id,
                                   ip_addr='10.10.10.10', vrf='x')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_neighbor_ipv4_disable(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><router><bgp xmlns="{2}"><vrf-name>x'\
                   '</vrf-name><router-bgp-cmds-holder>'\
                   '<router-bgp-attributes><neighbor-ips>'\
                   '<neighbor-addr operation="delete">'\
                   '<router-bgp-neighbor-address>10.10.10.10'\
                   '</router-bgp-neighbor-address></neighbor-addr>'\
                   '</neighbor-ips></router-bgp-attributes>'\
                   '</router-bgp-cmds-holder></bgp></router></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace, self.rbridge_id,
                                      self.bgp_namespace)
        result = self.bgp.neighbor(remote_as='65535',
                                   rbridge_id=self.rbridge_id,
                                   ip_addr='10.10.10.10', vrf='x', delete=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_neighbor_ipv6_enable(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><router><bgp xmlns="{2}"><vrf-name>x'\
                   '</vrf-name><router-bgp-cmds-holder><address-family><ipv6>'\
                   '<ipv6-unicast><af-ipv6-neighbor-address-holder>'\
                   '<af-ipv6-neighbor-address><af-ipv6-neighbor-address>'\
                   '2001::1</af-ipv6-neighbor-address><activate />'\
                   '</af-ipv6-neighbor-address>'\
                   '</af-ipv6-neighbor-address-holder></ipv6-unicast></ipv6>'\
                   '</address-family></router-bgp-cmds-holder></bgp></router>'\
                   '</rbridge-id></config>'.format(self.rbridge_namespace,
                                                   self.rbridge_id,
                                                   self.bgp_namespace)
        result = self.bgp.neighbor(remote_as='65535',
                                   rbridge_id=self.rbridge_id,
                                   ip_addr='2001::1', vrf='x')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_neighbor_ipv6_disable(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><router><bgp xmlns="{2}"><vrf-name>x'\
                   '</vrf-name><router-bgp-cmds-holder>'\
                   '<router-bgp-attributes><neighbor-ipv6s>'\
                   '<neighbor-ipv6-addr operation="delete">'\
                   '<router-bgp-neighbor-ipv6-address>2001::1'\
                   '</router-bgp-neighbor-ipv6-address></neighbor-ipv6-addr>'\
                   '</neighbor-ipv6s></router-bgp-attributes>'\
                   '</router-bgp-cmds-holder></bgp></router></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace,
                                      self.rbridge_id,
                                      self.bgp_namespace)
        result = self.bgp.neighbor(remote_as='65535',
                                   rbridge_id=self.rbridge_id,
                                   ip_addr='2001::1', vrf='x', delete=True)
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_neighbor_exception(self):
        with self.assertRaises(KeyError):
            self.bgp.neighbor()

    def test_neighbor_value_error(self):
        with self.assertRaises(ValueError):
            self.bgp.neighbor(ip_addr='2001::1', rbridge_id=self.rbridge_id)

    def test_enabled_true(self):
        def enabled_xml(self, *args, **kwargs):
            ietf_namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'
            rbridge_namespace = 'urn:brocade.com:mgmt:brocade-rbridge'
            bgp_namespace = 'urn:brocade.com:mgmt:brocade-bgp'
            rbridge_id = '2'
            xml = '<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '\
                  'xmlns:ns2="{2}"><ns0:data><ns1:rbridge-id><ns1:rbridge-id>'\
                  '{3}</ns1:rbridge-id><ns1:router><ns2:bgp><ns2:vrf-name>'\
                  'default</ns2:vrf-name><ns2:router-bgp-cmds-holder>'\
                  '<ns2:router-bgp-attributes><ns2:local-as>65535'\
                  '</ns2:local-as></ns2:router-bgp-attributes>'\
                  '<ns2:address-family><ns2:ipv4><ns2:ipv4-unicast>'\
                  '<ns2:af-common-cmds-holder>'\
                  '<ns2:client-to-client-reflection />'\
                  '</ns2:af-common-cmds-holder></ns2:ipv4-unicast></ns2:ipv4>'\
                  '<ns2:ipv6><ns2:ipv6-unicast><ns2:af-common-cmds-holder>'\
                  '<ns2:client-to-client-reflection />'\
                  '</ns2:af-common-cmds-holder></ns2:ipv6-unicast></ns2:ipv6>'\
                  '</ns2:address-family></ns2:router-bgp-cmds-holder>'\
                  '</ns2:bgp>'\
                  '</ns1:router></ns1:rbridge-id></ns0:data>'\
                  '</ns0:rpc-reply>'.format(ietf_namespace, rbridge_namespace,
                                            bgp_namespace, rbridge_id)

            return ET.fromstring(xml)

        self.bgp._callback = enabled_xml
        expected = True
        result = self.bgp.enabled
        self.assertEquals(expected, result)

    def test_enabled_false(self):
        def disabled_xml(*args, **kwargs):
            return ET.fromstring('<rpc-reply><data /></rpc-reply>')
        self.bgp._callback = disabled_xml
        expected = False
        result = self.bgp.enabled
        self.assertEquals(expected, result)
        pass
