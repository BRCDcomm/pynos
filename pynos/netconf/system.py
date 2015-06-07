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
import xml.etree.ElementTree as ET

class System(object):
    """
    System class containing all system level methods and attributes.

    Attributes:
        None
    """
    def __init__(self, callback):
        """
        System init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            System Object

        Raises:
            None
        """
        self._callback = callback

    def add_snmp_community(self, community):
        """
        Add SNMP Community to NOS device.

        Args:
            community: Community string to be added to device.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        community_el = ET.SubElement(snmp_server, 'community')
        community_name = ET.SubElement(community_el, 'community')
        community_name.text = community
        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def del_snmp_community(self, community):
        """
        Delete SNMP Community from NOS device.

        Args:
            community: Community string to be added to device.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        community_el = ET.SubElement(snmp_server, 'community',
                                     operation='delete')
        community_name = ET.SubElement(community_el, 'community')
        community_name.text = community
        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def add_snmp_host(self, host_info=(None, '162'), community='Public'):
        """
        Add SNMP host to NOS device.

        Args:
            host_info: Tuple of host IP and port.
            community: Community string to be added to device.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
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
        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def del_snmp_host(self, host_info=(None, '162'), community='Public'):
        """
        Delete SNMP host from NOS device.

        Args:
            host_info: Tuple of host IP and port.
            community: Community string to be added to device.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
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
        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False
