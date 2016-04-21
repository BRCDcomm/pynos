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
import pynos.versions.base.vcs
import pynos.utilities


class TestVCS(unittest.TestCase):
    """
    VCS unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.vcs = pynos.versions.base.vcs.VCS(pynos.utilities.return_xml)
        self._namespace = 'urn:brocade.com:mgmt:brocade-vcs'
        self._netconf_namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'
        self._message_id = 'urn:uuid:286adf24-7f21-11e5-bafd-5ce0c5934fb8'
        self._wwn = '10:00:00:05:33:65:09:D8'
        self._mac = '00:05:33:65:09:d8'
        self._fcf_mac = '00:05:33:65:0a:5e'
        self._serial = 'CGS0301J001'
        self._vcs_id = '211'
        self._rbridge_id = '225'
        self._internal_ip = '127.1.0.225'
        self._mgmt_ip = '10.24.39.211'

    def vcs_nodes_xml(self, *args, **kwargs):
        node_xml = '<ns0:rpc-reply xmlns:ns0="{0}" xmlns:ns1="{1}" '\
            'message-id="{2}"><ns1:vcs-cluster-type-info>'\
            'vcs-management-cluster</ns1:vcs-cluster-type-info><ns1:vcs-guid>'\
            '00000000000000000000000000000000</ns1:vcs-guid>'\
            '<ns1:virtual-ip-address>NULL</ns1:virtual-ip-address>'\
            '<ns1:principal-switch-wwn>{3}</ns1:principal-switch-wwn>'\
            '<ns1:co-ordinator-wwn></ns1:co-ordinator-wwn>'\
            '<ns1:total-nodes-in-cluster>1</ns1:total-nodes-in-cluster>'\
            '<ns1:nodes-disconnected-from-cluster>0'\
            '</ns1:nodes-disconnected-from-cluster>'\
            '<ns1:cluster-generic-status>Good</ns1:cluster-generic-status>'\
            '<ns1:cluster-specific-status>All Nodes Present in the Cluster'\
            '</ns1:cluster-specific-status><ns1:vcs-nodes><ns1:vcs-node-info>'\
            '<ns1:node-num>1</ns1:node-num><ns1:node-serial-num>{4}'\
            '</ns1:node-serial-num><ns1:node-condition>Good'\
            '</ns1:node-condition><ns1:node-status>Co-ordinator'\
            '</ns1:node-status><ns1:node-vcs-mode>Enabled</ns1:node-vcs-mode>'\
            '<ns1:node-vcs-id>{5}</ns1:node-vcs-id><ns1:node-rbridge-id>{6}'\
            '</ns1:node-rbridge-id><ns1:node-is-principal>true'\
            '</ns1:node-is-principal><ns1:co-ordinator>true'\
            '</ns1:co-ordinator><ns1:node-switch-mac>{7}'\
            '</ns1:node-switch-mac>'\
            '<ns1:node-switch-wwn>{3}</ns1:node-switch-wwn>'\
            '<ns1:switch-fcf-mac>{8}</ns1:switch-fcf-mac>'\
            '<ns1:node-internal-ip-address>{9}</ns1:node-internal-ip-address>'\
            '<ns1:node-public-ip-addresses><ns1:node-public-ip-address>{10}'\
            '</ns1:node-public-ip-address></ns1:node-public-ip-addresses>'\
            '<ns1:node-public-ipv6-addresses>'\
            '</ns1:node-public-ipv6-addresses><ns1:node-swbd-number>131'\
            '</ns1:node-swbd-number><ns1:firmware-version>'\
            'v5.0.1nos5.0.1x_patch_150720_1800</ns1:firmware-version>'\
            '<ns1:node-switchname>sw0</ns1:node-switchname>'\
            '<ns1:node-switchtype>BR-VDX6740</ns1:node-switchtype>'\
            '<ns1:node-state>Online</ns1:node-state><ns1:node-fabric-state>'\
            'Online</ns1:node-fabric-state></ns1:vcs-node-info>'\
            '</ns1:vcs-nodes>'\
            '</ns0:rpc-reply>'.format(self._netconf_namespace, self._namespace,
                                      self._message_id, self._wwn,
                                      self._serial, self._vcs_id,
                                      self._rbridge_id, self._mac,
                                      self._fcf_mac, self._internal_ip,
                                      self._mgmt_ip)
        return ET.fromstring(node_xml)

    def test_neighbors(self):
        expected = {'node-rbridge-id': '225', 'node-serial-num': 'CGS0301J001',
                    'node-status': 'Co-ordinator', 'node-switch-ip':
                        '10.24.39.211', 'node-vcs-id': '211',
                    'node-switch-mac': '00:05:33:65:09:d8',
                    'node-switch-wwn': '10:00:00:05:33:65:09:D8',
                    'node-switchname': 'sw0',
                    'node-is-principal': 'true'}
        self.vcs._callback = self.vcs_nodes_xml
        results = self.vcs.vcs_nodes
        self.assertIsInstance(results, list)
        self.assertDictEqual(expected, results[0])
