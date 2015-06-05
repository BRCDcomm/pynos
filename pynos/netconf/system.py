#!/usr/bin/env python
'''
NetCONF serilization of system actions for Brocade NOS devices.
'''
import xml.etree.ElementTree as ET

class System(object):
    '''
    Main System object.
    '''
    def __init__(self, callback):
        self._callback = callback

    def add_snmp_community(self, community):
        '''
        Add SNMP Community
        Paramaters:
            community: Community string
        '''
        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        community_el = ET.SubElement(snmp_server, 'community')
        community_name = ET.SubElement(community_el, 'community')
        community_name.text = community
        self._callback(config)

    def del_snmp_community(self, community):
        '''
        Add SNMP Community
        Paramaters:
            community: Community string
        '''
        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        community_el = ET.SubElement(snmp_server, 'community',
                                     operation='delete')
        community_name = ET.SubElement(community_el, 'community')
        community_name.text = community
        self._callback(config)

    def add_snmp_host(self, host_info=(None, None), community='Public'):
        '''
        Add SNMP host
        '''
        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        host = ET.SubElement(snmp_server, 'host')
        ip_addr = ET.SubElement(host, 'ip')
        ip_addr.text = host_info[0]
        com = ET.SubElement(host, 'community')
        com.text = community
        udp_port = ET.SubElement(host, 'udp-port')
        udp_port.text = host_info[1]
        self._callback(config)

    def del_snmp_host(self, host_info=(None, None), community='Public'):
        '''
        Delete SNMP Host
        '''
        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        host = ET.SubElement(snmp_server, 'host', operation='delete')
        ip_addr = ET.SubElement(host, 'ip')
        ip_addr.text = host_info[0]
        com = ET.SubElement(host, 'community')
        com.text = community
        udp_port = ET.SubElement(host, 'udp-port')
        udp_port.text = host_info[1]
        self._callback(config)
