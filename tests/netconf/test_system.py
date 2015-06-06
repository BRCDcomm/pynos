#!/usr/bin/env python
'''
System Unittest
'''
import unittest
from pynos.netconf.system import System
import xml.etree.ElementTree as ET

class _Tester(object):
    '''
    Tester object
    '''
    def __init__(self):
        self.system = System(self._callback)
        self.output = None

    def _callback(self, config):
        '''
        Callback function to return text of XML
        '''
        self.output = ET.tostring(config)

TESTER = _Tester()

class TestSystem(unittest.TestCase):
    '''
    Testing System
    '''
    def test_add_snmp_community(self):
        '''
        Test adding an SNMP community
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><community><community>test</community></community></snmp-server></config>'

        TESTER.system.add_snmp_community('test')
        self.assertEqual(TESTER.output, output)

    def test_del_snmp_community(self):
        '''
        Test delete SNMP community
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><community operation="delete"><community>test</community></community></snmp-s\
erver></config>'

        TESTER.system.del_snmp_community('test')
        self.assertEqual(TESTER.output, output)

    def test_add_snmp_host(self):
        '''
        Test add snmp host
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><host><ip>10.0.0.1</ip><community>Public</community><udp-port>161</udp-port><\
/host></snmp-server></config>'

        TESTER.system.add_snmp_host(('10.0.0.1', '161'))
        self.assertEqual(TESTER.output, output)

    def test_del_snmp_host(self):
        '''
        Test delete snmp host
        '''
        output = '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp\
"><host operation="delete"><ip>10.0.0.1</ip><community>Public</community><udp-p\
ort>161</udp-port></host></snmp-server></config>'

        TESTER.system.del_snmp_host(('10.0.0.1', '161'))
        self.assertEqual(TESTER.output, output)
