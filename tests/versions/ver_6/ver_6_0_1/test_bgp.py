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
import pynos.versions.ver_6.ver_6_0_1.bgp as bgp
import pynos.utilities


class TestBGP(unittest.TestCase):
    """
    BGP unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.bgp = bgp.BGP(pynos.utilities.return_xml)
        self.rbridge_namespace = 'urn:brocade.com:mgmt:brocade-rbridge'
        self.bgp_namespace = 'urn:brocade.com:mgmt:brocade-bgp'
        self.rbridge_id = '2'

    def test_local_asn(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><router><router-bgp xmlns="{2}">'\
                   '<router-bgp-attributes><local-as>65535</local-as>'\
                   '</router-bgp-attributes></router-bgp></router>'\
                   '</rbridge-id></config>'.format(self.rbridge_namespace,
                                                   self.rbridge_id,
                                                   self.bgp_namespace)
        result = self.bgp.local_asn(local_as='65535', rbridge_id='2', vrf='x')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_local_asn_exception(self):
        with self.assertRaises(KeyError):
            self.bgp.local_asn(rbridge='2', vrf='x')

    def test_remove_bgp(self):
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>{1}'\
                   '</rbridge-id><router>'\
                   '<router-bgp operation="delete" xmlns="{2}" /></router>'\
                   '</rbridge-id></config>'.format(self.rbridge_namespace,
                                                   self.rbridge_id,
                                                   self.bgp_namespace)
        result = ET.tostring(self.bgp.remove_bgp(rbridge_id=self.rbridge_id))
        self.assertEquals(expected, result)
