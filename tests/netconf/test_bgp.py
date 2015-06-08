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
from pynos.netconf.bgp import BGP
import xml.etree.ElementTree as ET

class _Tester(object):
    """
    Tester class 
    """
    def __init__(self):
        self.bgp = BGP(self._callback)
        self.output = None

    def _callback(self, config):
        '''
        Callback function to return text of XML.
        '''
        self.output = ET.tostring(config)

TESTER = _Tester()

class TestBGP(unittest.TestCase):
    '''
    Testing BGP
    '''
    def test_setup_bgp(self):
        '''
        Test setup BGP method.
        '''
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbrid\
ge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocade-\
bgp"><vrf-name>default</vrf-name></bgp></router></rbridge-id></config>'
        TESTER.bgp.setup_bgp()
        self.assertEqual(TESTER.output, output)

    def test_local_asn(self):
        '''
        Test Local ASN
        '''
        TESTER.bgp.local_asn('65000')
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbrid\
ge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocade-\
bgp"><vrf-name>default</vrf-name><router-bgp-cmds-holder><router-bgp-attributes\
><local-as>65000</local-as></router-bgp-attributes></router-bgp-cmds-holder></b\
gp></router></rbridge-id></config>'

        self.assertEqual(TESTER.output, output)

    def test_remove_bgp(self):
        '''
        Test Remove BGP
        '''
        TESTER.bgp.remove_bgp()
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbrid\
ge"><rbridge-id>1</rbridge-id><router><bgp operation="delete" xmlns="urn:brocad\
e.com:mgmt:brocade-bgp"><vrf-name>default</vrf-name></bgp></router></rbridge-id\
></config>'

        self.assertEqual(TESTER.output, output)

    def test_add_neighbor(self):
        '''
        Test Remove BGP
        '''
        TESTER.bgp.add_neighbor('10.0.0.1', '65000')
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbrid\
ge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocade-\
bgp"><vrf-name>default</vrf-name><router-bgp-cmds-holder><router-bgp-attributes\
><neighbor><neighbor-ips><neighbor-addr><router-bgp-neighbor-address>10.0.0.1</\
router-bgp-neighbor-address><remote-as>65000</remote-as></neighbor-addr></neigh\
bor-ips></neighbor></router-bgp-attributes></router-bgp-cmds-holder></bgp></rou\
ter></rbridge-id></config>'

        self.assertEqual(TESTER.output, output)

    def test_remove_neighbor(self):
        '''
        Test Remove BGP
        '''
        TESTER.bgp.remove_neighbor('10.0.0.1')
        output = '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbrid\
ge"><rbridge-id>1</rbridge-id><router><bgp xmlns="urn:brocade.com:mgmt:brocade-\
bgp"><vrf-name>default</vrf-name><router-bgp-cmds-holder><router-bgp-attributes\
><neighbor><neighbor-ips><neighbor-addr operation="delete"><router-bgp-neighbor\
-address>10.0.0.1</router-bgp-neighbor-address></neighbor-addr></neighbor-ips><\
/neighbor></router-bgp-attributes></router-bgp-cmds-holder></bgp></router></rbr\
idge-id></config>'

        self.assertEqual(TESTER.output, output)
