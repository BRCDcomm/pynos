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
import pynos.versions.base.bgp
import pynos.utilities


class TestBGP(unittest.TestCase):
    """
    BGP unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.bgp = pynos.versions.base.bgp.BGP(pynos.utilities.return_xml)

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
