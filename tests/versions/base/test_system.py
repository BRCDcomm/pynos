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
import pynos.versions.base.system as system
import pynos.utilities


class TestSystem(unittest.TestCase):
    """
    System unit tests. Compare expected XML to generated XML.
    """
    def setUp(self):
        self.system = system.System(pynos.utilities.return_xml)
        self.namespace = 'urn:brocade.com:mgmt:brocade-system'
        self.netconf_namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'
        self.rbridge_namespace = 'urn:brocade.com:mgmt:brocade-rbridge'

    def uptime_xml(self, *args, **kwargs):
        message_id = 'urn:uuid:528cdf32-2e86-11e5-bb27-080027b782e4'
        uptime_xml = '<ns0:rpc-reply xmlns:ns0="{0}" '\
                     'xmlns:ns1="{1}" message-id="{2}">'\
                     '<ns1:show-system-uptime><ns1:rbridge-id>226'\
                     '</ns1:rbridge-id><ns1:days>1</ns1:days><ns1:hours>21'\
                     '</ns1:hours><ns1:minutes>59</ns1:minutes><ns1:seconds>'\
                     '57</ns1:seconds></ns1:show-system-uptime>'\
                     '</ns0:rpc-reply>'.format(self.netconf_namespace,
                                               self.namespace,
                                               message_id)
        return ET.fromstring(uptime_xml)

    def test_uptime(self):
        expected = {'days': '1',
                    'hours': '21',
                    'minutes': '59',
                    'seconds': '57'}
        self.system._callback = self.uptime_xml
        results = self.system.uptime
        self.assertDictEqual(expected, results)

    def test_router_id(self):
        rtm_namespace = 'urn:brocade.com:mgmt:brocade-rtm'
        expected = '<config><rbridge-id xmlns="{0}"><rbridge-id>2'\
                   '</rbridge-id><ip><rtm-config xmlns="{1}"><router-id>'\
                   '10.10.10.10</router-id></rtm-config></ip></rbridge-id>'\
                   '</config>'.format(self.rbridge_namespace, rtm_namespace)
        result = self.system.router_id(rbridge_id='2', router_id='10.10.10.10')
        result = ET.tostring(result)
        self.assertEquals(expected, result)

    def test_router_id_exception(self):
        with self.assertRaises(KeyError):
            self.system.router_id()
