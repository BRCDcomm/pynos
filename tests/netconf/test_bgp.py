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
from pynos.netconf.bgp import BGP
import xml.etree.ElementTree as ET

_MOCK = Mock()


def _callback(out):
    """
    Callback to place value inside mock for testing results.
    """
    _MOCK.return_value = out


class TestBGP(unittest.TestCase):
    """
    BGP unit tests. Compare expected XML to generated XML.
    """
    def test_setup_bgp(self):
        """
        Test setup BGP.
        """
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbri\
dge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocad\
e-bgp"><vrf-name>default</vrf-name></bgp></router></rbridge-id></config>'
        bgp = BGP(_callback)
        bgp.setup_bgp()
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_local_asn(self):
        """
        Test adding local ASN.
        """
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbri\
dge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocad\
e-bgp"><vrf-name>default</vrf-name><router-bgp-cmds-holder><router-bgp-attribu\
tes><local-as>65000</local-as></router-bgp-attributes></router-bgp-cmds-holder\
></bgp></router></rbridge-id></config>'

        bgp = BGP(_callback)
        bgp.local_asn('65000')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_remove_bgp(self):
        """
        Test remove BGP.
        """
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbri\
dge"><rbridge-id>1</rbridge-id><router><bgp operation="delete" xmlns="urn:broc\
ade.com:mgmt:brocade-bgp"><vrf-name>default</vrf-name></bgp></router></rbridge\
-id></config>'

        bgp = BGP(_callback)
        bgp.remove_bgp()
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_add_neighbor(self):
        """
        Test adding BGP neighbor.
        """
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbri\
dge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocad\
e-bgp"><vrf-name>default</vrf-name><router-bgp-cmds-holder><router-bgp-attribu\
tes><neighbor><neighbor-ips><neighbor-addr><router-bgp-neighbor-address>10.0.0\
.1</router-bgp-neighbor-address><remote-as>65000</remote-as></neighbor-addr></\
neighbor-ips></neighbor></router-bgp-attributes></router-bgp-cmds-holder></bgp\
></router></rbridge-id></config>'

        bgp = BGP(_callback)
        bgp.add_neighbor('10.0.0.1', '65000')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()

    def test_remove_neighbor(self):
        """
        Test remove BGP neighbor.
        """
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbri\
dge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocad\
e-bgp"><vrf-name>default</vrf-name><router-bgp-cmds-holder><router-bgp-attribu\
tes><neighbor><neighbor-ips><neighbor-addr operation="delete"><router-bgp-neig\
hbor-address>10.0.0.1</router-bgp-neighbor-address></neighbor-addr></neighbor-\
ips></neighbor></router-bgp-attributes></router-bgp-cmds-holder></bgp></router\
></rbridge-id></config>'

        bgp = BGP(_callback)
        bgp.remove_neighbor('10.0.0.1')
        self.assertEqual(output, ET.tostring(_MOCK()))
        _MOCK.reset_mock()
