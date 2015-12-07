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
import pynos.versions.base.fabric_service
import pynos.utilities


class TestFabricService(unittest.TestCase):
    """
    Fabric Service unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.fabric = pynos.versions.base.fabric_service.FabricService(
            pynos.utilities.return_xml)
        self.namespace = 'urn:brocade.com:mgmt:brocade-fabric-service'
        self.netconf_namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'

    def trill_links_xml(self, *args, **kwargs):
        message_id = 'urn:uuid:528cdf32-2e86-11e5-bb27-080027b782e4'
        links_xml = ('<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '
                     'message-id="{2}"><ns1:show-link-info>'
                     '<ns1:linkinfo-rbridgeid>1</ns1:linkinfo-rbridgeid>'
                     '<ns1:linkinfo-domain-reachable>Yes'
                     '</ns1:linkinfo-domain-reachable><ns1:linkinfo-version>'
                     '1</ns1:linkinfo-version><ns1:linkinfo-wwn>'
                     '10:00:00:05:33:65:09:D8</ns1:linkinfo-wwn>'
                     '<ns1:linkinfo-isl><ns1:linkinfo-isl-linknumber>1'
                     '</ns1:linkinfo-isl-linknumber>'
                     '<ns1:linkinfo-isllink-destdomain>1'
                     '</ns1:linkinfo-isllink-destdomain>'
                     '<ns1:linkinfo-isllink-srcport>64'
                     '</ns1:linkinfo-isllink-srcport>'
                     '<ns1:linkinfo-isllink-srcport-type>Te'
                     '</ns1:linkinfo-isllink-srcport-type>'
                     '<ns1:linkinfo-isllink-srcport-interface>1/0/1'
                     '</ns1:linkinfo-isllink-srcport-interface>'
                     '<ns1:linkinfo-isllink-destport>64'
                     '</ns1:linkinfo-isllink-destport>'
                     '<ns1:linkinfo-isllink-destport-type>Te'
                     '</ns1:linkinfo-isllink-destport-type>'
                     '<ns1:linkinfo-isllink-destport-interface>2/0/1'
                     '</ns1:linkinfo-isllink-destport-interface>'
                     '<ns1:linkinfo-isl-linkcost>500'
                     '</ns1:linkinfo-isl-linkcost>'
                     '<ns1:linkinfo-isllink-costcount>10'
                     '</ns1:linkinfo-isllink-costcount>'
                     '<ns1:linkinfo-isllink-type>4</ns1:linkinfo-isllink-type>'
                     '<ns1:linkinfo-trunked>Yes</ns1:linkinfo-trunked>'
                     '</ns1:linkinfo-isl></ns1:show-link-info>'
                     '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                               self.namespace,
                                               message_id))
        return ET.fromstring(links_xml)

    def test_links(self):
        expected = {'dest-interface': '2/0/1',
                    'dest-rbridgeid': '1',
                    'link-cost': '500',
                    'link-costcount': '10',
                    'source-interface': '1/0/1',
                    'source-rbridgeid': '1',
                    'source-switch-wwn': '10:00:00:05:33:65:09:D8'}
        self.fabric._callback = self.trill_links_xml
        results = self.fabric.trill_links
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected, results[0])
