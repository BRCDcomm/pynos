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
import logging


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
        # TODO add logging and narrow exception window.
        except Exception, error:
            logging.error(error)
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
        # TODO add logging and narrow exception window.
        except Exception, error:
            logging.error(error)
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
        # TODO add logging and narrow exception window.
        except Exception, error:
            logging.error(error)
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
        # TODO add logging and narrow exception window.
        except Exception, error:
            logging.error(error)
            return False

    @property
    def neighbors(self):
        """
        Args:
            None

        Returns:
            A list of LLDP Neighbors. Each list item is a dictionary containing
            the following elements:
                local-int-name: Local interface name
                local-int-mac: Local interface MAC address
                remote-int-name: Remote interface name
                remote-int-mac: Remote interface MAC address
                remote-chassis-id: Remote chassis ID
                remote-system-name: Hostname of remote system

        Raises:
            None
        """
        urn = "{urn:brocade.com:mgmt:brocade-lldp-ext}"

        result = []

        request_lldp = ET.Element(
            'get-lldp-neighbor-detail',
            xmlns="urn:brocade.com:mgmt:brocade-lldp-ext"
        )

        lldp_result = self._callback(request_lldp, 'get')

        for item in lldp_result.findall('%slldp-neighbor-detail' % urn):
            local_int_name = item.find('%slocal-interface-name' % urn).text
            local_int_mac = item.find('%slocal-interface-mac' % urn).text
            remote_int_name = item.find('%sremote-interface-name' % urn).text
            remote_int_mac = item.find('%sremote-interface-mac' % urn).text
            remote_chas_id = item.find('%sremote-chassis-id' % urn).text
            remote_sys_name = item.find('%sremote-system-name' % urn).text

            if 'Fo ' in local_int_name:
                local_int_name = local_int_name.replace(
                    'Fo ',
                    'FortyGigabitEthernet '
                )

            item_results = {'local-int-name': local_int_name,
                            'local-int-mac': local_int_mac,
                            'remote-int-name': remote_int_name,
                            'remote-int-mac': remote_int_mac,
                            'remote-chassis-id': remote_chas_id,
                            'remote-system-name': remote_sys_name}
            result.append(item_results)

        return result
