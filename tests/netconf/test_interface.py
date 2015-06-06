#!/usr/bin/env python
'''
Interface Unittest
'''
import unittest
from pynos.netconf.interface import Interface
import xml.etree.ElementTree as ET

class _Tester(object):
    '''
    Tester object
    '''
    def __init__(self):
        self.inter = Interface(self._callback)
        self.output = None

    def _callback(self, config):
        '''
        Callback function to return text of XML
        '''
        self.output = ET.tostring(config)

TESTER = _Tester()

class TestInterface(unittest.TestCase):
    '''
    Testing Interfaces
    '''
    def test_add_vlan_int(self):
        '''
        Test add VLAN Interface
        '''
        output = '<config><interface-vlan xmlns="urn:brocade.com:mgmt:brocade-i\
nterface"><interface><vlan><name>10</name></vlan></interface></interface-vlan><\
/config>'
        TESTER.inter.add_vlan_int('10')
        self.assertEqual(TESTER.output, output)

    def test_del_vlan_int(self):
        '''
        Test delete VLAN Interface
        '''
        output = '<config><interface-vlan xmlns="urn:brocade.com:mgmt:brocade-i\
nterface"><interface><vlan operation="delete"><name>10</name></vlan></interface\
></interface-vlan></config>'

        TESTER.inter.del_vlan_int('10')
        self.assertEqual(TESTER.output, output)

    def test_enable_switchport(self):
        '''
        Test enabling switchport
        '''
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interf\
ace"><tengigabitethernet><name>1/0/1</name><switchport-basic><basic /></switchp\
ort-basic></tengigabitethernet></interface></config>'

        TESTER.inter.enable_switchport('tengigabitethernet', '1/0/1')

        self.assertEqual(TESTER.output, output)

    def test_disable_switchport(self):
        '''
        Test disable switchport
        '''
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interf\
ace"><tengigabitethernet><name>1/0/1</name><switchport-basic operation="delete"\
 /></tengigabitethernet></interface></config>'

        TESTER.inter.disable_switchport('tengigabitethernet', '1/0/1')

        self.assertEqual(TESTER.output, output)

    def test_access_vlan(self):
        '''
        Test add access VLAN
        '''
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interf\
ace"><tengigabitethernet><name>1/0/1</name><switchport><access><accessvlan>10</\
accessvlan></access></switchport></tengigabitethernet></interface></config>'

        TESTER.inter.access_vlan('tengigabitethernet', '1/0/1', '10')

        self.assertEqual(TESTER.output, output)

    def test_del_access_vlan(self):
        '''
        Test delete access VLAN
        '''
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interf\
ace"><tengigabitethernet><name>1/0/1</name><switchport><access><accessvlan oper\
ation="delete">10</accessvlan></access></switchport></tengigabitethernet></inte\
rface></config>'

        TESTER.inter.del_access_vlan('tengigabitethernet', '1/0/1', '10')

        self.assertEqual(TESTER.output, output)

    def test_set_ip(self):
        '''
        Test add IP address
        '''
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interf\
ace"><tengigabitethernet><name>1/0/1</name><ip><ip-config xmlns="urn:brocade.co\
m:mgmt:brocade-ip-config"><address><address>10.0.0.1/24</address></address></ip\
-config></ip></tengigabitethernet></interface></config>'

        TESTER.inter.set_ip('tengigabitethernet', '1/0/1', '10.0.0.1/24')

        self.assertEqual(TESTER.output, output)

    def test_del_ip(self):
        '''
        Test delete IP address
        '''
        output = '<config><interface xmlns="urn:brocade.com:mgmt:brocade-interf\
ace"><tengigabitethernet><name>1/0/1</name><ip><ip-config xmlns="urn:brocade.co\
m:mgmt:brocade-ip-config"><address operation="delete"><address>10.0.0.1/24</add\
ress></address></ip-config></ip></tengigabitethernet></interface></config>'

        TESTER.inter.del_ip('tengigabitethernet', '1/0/1', '10.0.0.1/24')

        self.assertEqual(TESTER.output, output)
