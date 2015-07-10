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
