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


class Interfaces(object):
    """
    Expermintal Interfaces object
    """
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
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a NOS device.

    Attributes:
        None
    """
    def __init__(self, callback):
        """
        Interface init function.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            Interface Object

        Raises:
            None
        """
        self._callback = callback

    def add_vlan_int(self, vlan_id):
        """
        Add VLAN Interface. VLAN interfaces are required for VLANs even when
        not wanting to use the interface for any L3 features.

        Args:
            vlan_id: ID for the VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        vlinterface = ET.SubElement(config, 'interface-vlan',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-interface"))
        interface = ET.SubElement(vlinterface, 'interface')
        vlan = ET.SubElement(interface, 'vlan')
        name = ET.SubElement(vlan, 'name')
        name.text = vlan_id
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def del_vlan_int(self, vlan_id):
        """
        Delete VLAN Interface.

        Args:
            vlan_id: ID for the VLAN interface being created. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        vlinterface = ET.SubElement(config, 'interface-vlan',
                                    xmlns=("urn:brocade.com:mgmt:"
                                           "brocade-interface"))
        interface = ET.SubElement(vlinterface, 'interface')
        vlan = ET.SubElement(interface, 'vlan', operation='delete')
        name = ET.SubElement(vlan, 'name')
        name.text = vlan_id
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def enable_switchport(self, inter_type, inter):
        """
        Change an interface's operation to L2.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        int_type = ET.SubElement(interface, inter_type)
        name = ET.SubElement(int_type, 'name')
        name.text = inter
        switchport_basic = ET.SubElement(int_type, 'switchport-basic')
        ET.SubElement(switchport_basic, 'basic')
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def disable_switchport(self, inter_type, inter):
        """
        Change an interface's operation to L3.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        int_type = ET.SubElement(interface, inter_type)
        name = ET.SubElement(int_type, 'name')
        name.text = inter
        ET.SubElement(int_type, 'switchport-basic', operation='delete')
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def access_vlan(self, inter_type, inter, vlan_id):
        """
        Add a L2 Interface to a specific VLAN.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            vlan_id: ID for the VLAN interface being modified. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
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
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def del_access_vlan(self, inter_type, inter, vlan_id):
        """
        Remove a L2 Interface from a specific VLAN, placing it back into the
        default VLAN.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            vlan_id: ID for the VLAN interface being modified. Value of 2-4096.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
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
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def set_ip(self, inter_type, inter, ip_addr):
        """
        Set IP address of a L3 interface.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            ip_addr: IP Address in <prefix>/<bits> format. Ex: 10.10.10.1/24

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        intert = ET.SubElement(interface, inter_type)
        name = ET.SubElement(intert, 'name')
        name.text = inter
        ipel = ET.SubElement(intert, 'ip')
        ip_config = ET.SubElement(
            ipel, 'ip-config',
            xmlns="urn:brocade.com:mgmt:brocade-ip-config"
        )
        address = ET.SubElement(ip_config, 'address')
        ipaddr = ET.SubElement(address, 'address')
        ipaddr.text = ip_addr
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def del_ip(self, inter_type, inter, ip_addr):
        """
        Delete IP address from a L3 interface.

        Args:
            inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
            inter: The ID for the interface you want to configure. Ex. 1/0/1
            ip_addr: IP Address in <prefix>/<bits> format. Ex: 10.10.10.1/24

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        interface = ET.SubElement(config, 'interface',
                                  xmlns=("urn:brocade.com:mgmt:"
                                         "brocade-interface"))
        intert = ET.SubElement(interface, inter_type)
        name = ET.SubElement(intert, 'name')
        name.text = inter
        ipel = ET.SubElement(intert, 'ip')
        ip_config = ET.SubElement(
            ipel, 'ip-config',
            xmlns="urn:brocade.com:mgmt:brocade-ip-config"
        )
        address = ET.SubElement(ip_config, 'address', operation='delete')
        ipaddr = ET.SubElement(address, 'address')
        ipaddr.text = ip_addr
        try:
            self._callback(config)
            return True
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
            return False

    def description(self, **kwargs):
        """
        Set interface description.

        Args:

        Returns:

        Raises:
        """
        pass

    def private_vlan_type(self, **kwargs):
        """Set the PVLAN type (primary, isolated, community).

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def private_vlan_association(self, **kwargs):
        """Set interface PVLAN association.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def admin_state(self, **kwargs):
        """
        Set interface state.

        Args:
            state (bool): True to enable, false to disable.

        Returns:

        Raises:

        Examples:
        """
        pass

    def switchport_pvlan_host_assoc(self, **kwargs):
        """Set switchport private vlan host association.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def trunk_allowed_vlan(self, **kwargs):
        """Set trunk allowed VLAN. (includes ctags)

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def private_vlan_mode(self, **kwargs):
        """Set PVLAN mode (promiscuous, host, trunk).

        Args:

        Returns:

        Raises:
        """
        pass

    def spanning_tree_state(self, **kwargs):
        """Set spanning tree state.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def tag_native_vlan(self, **kwargs):
        """Set tagging of native VLAN on trunk.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def switchport_pvlan_mapping(self, **kwargs):
        """Switchport private VLAN mapping.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def mtu(self, **kwargs):
        """Set Interface MTU.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def fabric_isl(self, **kwargs):
        """Set fabric isl state.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def fabric_trunk(self, **kwargs):
        """Set fabric trunk state.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def v6_nd_suppress_ra(self, **kwargs):
        """Set fabric trunk state.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_vip(self, **kwargs):
        """Set VRRP VIP.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_state(self, **kwargs):
        """Set VRRP state (enabled, disabled).

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_preempt(self, **kwargs):
        """Set VRRP preempt mode (enabled, disabled).

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_priority(self, **kwargs):
        """Set VRRP priority.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def vrrp_advertisement_interval(self, **kwargs):
        """Set VRRP advertisement interval.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def proxy_arp(self, **kwargs):
        """Set proxy-arp (enabled, disabled).

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def port_channel_minimum_links(self, **kwargs):
        """Set minimum number of links for a port channel.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def port_channel_member(self, **kwargs):
        """Set port channel member.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def port_channel_mode(self, **kwargs):
        """Set port channel mode.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def port_channel_type(self, **kwargs):
        """Set port channel type.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def port_channel_vlag_ignore_split(self, **kwargs):
        """Ignore VLAG Splits.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def trunk_no_default_native(self, **kwargs):
        """Disable native VLAN on trunk port.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def transport_service(self, **kwargs):
        """Configure transport service.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def lacp_timeout(self, **kwargs):
        """Configure LACP timeout.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass
