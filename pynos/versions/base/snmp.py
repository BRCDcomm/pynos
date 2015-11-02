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
import xml.etree.ElementTree as ET


class SNMP(object):
    """
    SNMP class containing all SNMP level methods and attributes.
    """
    def __init__(self, callback):
        """
        SNMP init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            SNMP Object

        Raises:
            None
        """
        self._callback = callback

    def add_snmp_community(self, **kwargs):
        """
        Add SNMP Community to NOS device.

        Args:
            community (str): Community string to be added to device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `community` is not defined.
        """
        community = kwargs.pop('community')
        callback = kwargs.pop('callback', self._callback)

        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        community_el = ET.SubElement(snmp_server, 'community')
        community_name = ET.SubElement(community_el, 'community')
        community_name.text = community

        return callback(config)

    def del_snmp_community(self, **kwargs):
        """
        Delete SNMP Community from NOS device.

        Args:
            community (str): Community string to be added to device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `community` is not defined.
        """
        community = kwargs.pop('community')
        callback = kwargs.pop('callback', self._callback)

        config = ET.Element('config')
        snmp_server = ET.SubElement(config, 'snmp-server',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-snmp"))
        community_el = ET.SubElement(snmp_server, 'community',
                                     operation='delete')
        community_name = ET.SubElement(community_el, 'community')
        community_name.text = community
        return callback(config)

    def add_snmp_host(self, **kwargs):
        """
        Add SNMP host to NOS device.

        Args:
            host_info (tuple(str, str)): Tuple of host IP and port.
            community (str): Community string to be added to device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `host_info` or `community` is not defined.
        """
        host_info = kwargs.pop('host_info')
        community = kwargs.pop('community')
        callback = kwargs.pop('callback', self._callback)

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
        return callback(config)

    def del_snmp_host(self, **kwargs):
        """
        Delete SNMP host from NOS device.

        Args:
            host_info (tuple(str, str)): Tuple of host IP and port.
            community (str): Community string to be added to device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `host_info` or `community` is not defined.
        """
        host_info = kwargs.pop('host_info')
        community = kwargs.pop('community')
        callback = kwargs.pop('callback', self._callback)

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
        return callback(config)
