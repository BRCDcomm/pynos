#!/usr/bin/env python
'''
NetCONF serilization of Interface actions for Brocade NOS devices.
'''
import xml.etree.ElementTree as ET

class Interfaces(object):
    '''
    Interfaces object
    '''
    def __init__(self, callback):
        self._callback = callback
        for interface in self._get_interfaces():
            setattr(self, interface, Interface(callback))

    def _get_interfaces(self):
        '''
        Get all interfaces
        '''
        pass

class Interface(object):
    '''
    Main interface object.
    '''
    def __init__(self, callback):
        self._callback = callback

    def add_vlan_int(self, vlan_id):
        '''
        Create VLAN on switch.
        '''
        config = ET.Element('config')
        vlinterface = ET.SubElement(config, 'interface-vlan',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-interface"))
        interface = ET.SubElement(vlinterface, 'interface')
        vlan = ET.SubElement(interface, 'vlan')
        name = ET.SubElement(vlan, 'name')
        name.text = vlan_id
        self._callback(config)

    def del_vlan_int(self, vlan_id):
        '''
        Create VLAN on switch.
        '''
        config = ET.Element('config')
        vlinterface = ET.SubElement(config, 'interface-vlan',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-interface"))
        interface = ET.SubElement(vlinterface, 'interface')
        vlan = ET.SubElement(interface, 'vlan', operation='delete')
        name = ET.SubElement(vlan, 'name')
        name.text = vlan_id
        self._callback(config)

    def enable_switchport(self, inter_type, inter):
        '''
        Set switchport for interface
        '''
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        int_type = ET.SubElement(interface, inter_type)
        name = ET.SubElement(int_type, 'name')
        name.text = inter
        switchport_basic = ET.SubElement(int_type, 'switchport-basic')
        ET.SubElement(switchport_basic, 'basic')
        self._callback(config)

    def disable_switchport(self, inter_type, inter):
        '''
        Unset switchport for interface
        '''
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        int_type = ET.SubElement(interface, inter_type)
        name = ET.SubElement(int_type, 'name')
        name.text = inter
        ET.SubElement(int_type, 'switchport-basic', operation='delete')
        self._callback(config)

    def access_vlan(self, inter_type, inter, vlan_id):
        '''
        Set access VLAN on Interface

        Parameters:
            inter_type: Type of interface. Ex: gigabitethernet
            inter: The actual interface referece. Ex: 1/0/1
            vlan_id: The desired access VLAN.
        '''
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        int_type = ET.SubElement(interface, inter_type)
        name = ET.SubElement(int_type, 'name')
        name.text = inter
        switchport = ET.SubElement(int_type, 'switchport')
        access = ET.SubElement(switchport, 'access')
        accessvlan = ET.SubElement(access, 'accessvlan')
        accessvlan.text = vlan_id
        self._callback(config)

    def del_access_vlan(self, inter_type, inter, vlan_id):
        '''
        Delete access VLAN on Interface

        Parameters:
            inter_type: Type of interface. Ex: gigabitethernet
            inter: The actual interface referece. Ex: 1/0/1
            vlan_id: The desired access VLAN.
        '''
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        int_type = ET.SubElement(interface, inter_type)
        name = ET.SubElement(int_type, 'name')
        name.text = inter
        switchport = ET.SubElement(int_type, 'switchport')
        access = ET.SubElement(switchport, 'access')
        accessvlan = ET.SubElement(access, 'accessvlan', operation='delete')
        accessvlan.text = vlan_id
        self._callback(config)

    def set_ip(self, inter_type, inter, ip_addr):
        '''
        Generate NETCONF from inputs to add IP to interface.

        Parameters:
            inter_type: Type of interface. Ex: gigabitethernet
            inter: The actual interface referece. Ex: 1/0/1
            ip_addr: IP Address in <prefix>/<bits> format. Ex: 10.10.10.1/24
        '''
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        intert = ET.SubElement(interface, inter_type)
        name = ET.SubElement(intert, 'name')
        name.text = inter
        ipel = ET.SubElement(intert, 'ip')
        ip_config = ET.SubElement(ipel, 'ip-config',
                                  xmlns="urn:brocade.com:mgmt:brocade-ip-config"
                                 )
        address = ET.SubElement(ip_config, 'address')
        ipaddr = ET.SubElement(address, 'address')
        ipaddr.text = ip_addr
        self._callback(config)

    def del_ip(self, inter_type, inter, ip_addr):
        '''
        Generate NETCONF from inputs to remove IP from interface.

        Parameters:
            inter_type: Type of interface. Ex: gigabitethernet
            inter: The actual interface referece. Ex: 1/0/1
            ip_addr: IP Address in <prefix>/<bits> format. Ex: 10.10.10.1/24
        '''
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        intert = ET.SubElement(interface, inter_type)
        name = ET.SubElement(intert, 'name')
        name.text = inter
        ipel = ET.SubElement(intert, 'ip')
        ip_config = ET.SubElement(ipel, 'ip-config',
                                  xmlns="urn:brocade.com:mgmt:brocade-ip-config"
                                 )
        address = ET.SubElement(ip_config, 'address', operation='delete')
        ipaddr = ET.SubElement(address, 'address')
        ipaddr.text = ip_addr
        self._callback(config)
