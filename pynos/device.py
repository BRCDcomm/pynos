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
import logging
import xml.etree.ElementTree as ET

from ncclient import manager
from ncclient import xml_
import ncclient

import pynos.versions.ver_5.ver_5_0_1.bgp
import pynos.versions.ver_5.ver_5_0_1.snmp
import pynos.versions.ver_5.ver_5_0_1.interface
import pynos.versions.ver_5.ver_5_0_1.lldp
import pynos.versions.ver_5.ver_5_0_1.system
import pynos.versions.ver_5.ver_5_0_1.services
import pynos.versions.ver_5.ver_5_0_1.fabric_service
import pynos.versions.ver_5.ver_5_0_1.vcs
import pynos.versions.ver_5.ver_5_0_1.firmware
import pynos.versions.ver_5.ver_5_0_1.ras
import pynos.versions.ver_6.ver_6_0_1.bgp
import pynos.versions.ver_6.ver_6_0_1.snmp
import pynos.versions.ver_6.ver_6_0_1.interface
import pynos.versions.ver_6.ver_6_0_1.lldp
import pynos.versions.ver_6.ver_6_0_1.system
import pynos.versions.ver_6.ver_6_0_1.services
import pynos.versions.ver_6.ver_6_0_1.fabric_service
import pynos.versions.ver_6.ver_6_0_1.vcs
import pynos.versions.ver_6.ver_6_0_1.firmware
import pynos.versions.ver_6.ver_6_0_1.ras
import pynos.versions.ver_7.ver_7_0_0.bgp
import pynos.versions.ver_7.ver_7_0_0.interface
import pynos.versions.ver_7.ver_7_0_0.lldp
import pynos.versions.ver_7.ver_7_0_0.firmware
import pynos.versions.ver_7.ver_7_1_0.system

VERSIONS = {
    '5.0.1': {
        'bgp': pynos.versions.ver_5.ver_5_0_1.bgp.BGP,
        'snmp': pynos.versions.ver_5.ver_5_0_1.snmp.SNMP,
        'interface': pynos.versions.ver_5.ver_5_0_1.interface.Interface,
        'lldp': pynos.versions.ver_5.ver_5_0_1.lldp.LLDP,
        'system': pynos.versions.ver_5.ver_5_0_1.system.System,
        'services': pynos.versions.ver_5.ver_5_0_1.services.Services,
        'fabric_service': pynos.versions.ver_5.ver_5_0_1.fabric_service
                          .FabricService,
        'vcs': pynos.versions.ver_5.ver_5_0_1.vcs.VCS,
        'firmware': pynos.versions.ver_5.ver_5_0_1.firmware.Firmware,
        'ras': pynos.versions.ver_5.ver_5_0_1.ras.RAS,
    },
    '6.0.1': {
        'bgp': pynos.versions.ver_6.ver_6_0_1.bgp.BGP,
        'snmp': pynos.versions.ver_6.ver_6_0_1.snmp.SNMP,
        'interface': pynos.versions.ver_6.ver_6_0_1.interface.Interface,
        'lldp': pynos.versions.ver_6.ver_6_0_1.lldp.LLDP,
        'system': pynos.versions.ver_6.ver_6_0_1.system.System,
        'services': pynos.versions.ver_6.ver_6_0_1.services.Services,
        'fabric_service': pynos.versions.ver_6.ver_6_0_1.fabric_service
                          .FabricService,
        'vcs': pynos.versions.ver_6.ver_6_0_1.vcs.VCS,
        'firmware': pynos.versions.ver_6.ver_6_0_1.firmware.Firmware,
        'ras': pynos.versions.ver_6.ver_6_0_1.ras.RAS,
    },
    '6.0.2': {
        'bgp': pynos.versions.ver_6.ver_6_0_1.bgp.BGP,
        'snmp': pynos.versions.ver_6.ver_6_0_1.snmp.SNMP,
        'interface': pynos.versions.ver_6.ver_6_0_1.interface.Interface,
        'lldp': pynos.versions.ver_6.ver_6_0_1.lldp.LLDP,
        'system': pynos.versions.ver_6.ver_6_0_1.system.System,
        'services': pynos.versions.ver_6.ver_6_0_1.services.Services,
        'fabric_service': pynos.versions.ver_6.ver_6_0_1.fabric_service
                          .FabricService,
        'vcs': pynos.versions.ver_6.ver_6_0_1.vcs.VCS,
        'firmware': pynos.versions.ver_6.ver_6_0_1.firmware.Firmware,
        'ras': pynos.versions.ver_6.ver_6_0_1.ras.RAS,
    },
    '7.0.0': {
        'bgp': pynos.versions.ver_7.ver_7_0_0.bgp.BGP,
        'snmp': pynos.versions.ver_6.ver_6_0_1.snmp.SNMP,
        'interface': pynos.versions.ver_7.ver_7_0_0.interface.Interface,
        'lldp': pynos.versions.ver_7.ver_7_0_0.lldp.LLDP,
        'system': pynos.versions.ver_6.ver_6_0_1.system.System,
        'services': pynos.versions.ver_6.ver_6_0_1.services.Services,
        'fabric_service': pynos.versions.ver_6.ver_6_0_1.fabric_service
                          .FabricService,
        'vcs': pynos.versions.ver_6.ver_6_0_1.vcs.VCS,
        'firmware': pynos.versions.ver_7.ver_7_0_0.firmware.Firmware,
        'ras': pynos.versions.ver_6.ver_6_0_1.ras.RAS,
    },
    '7.0.1': {
        'bgp': pynos.versions.ver_7.ver_7_0_0.bgp.BGP,
        'snmp': pynos.versions.ver_6.ver_6_0_1.snmp.SNMP,
        'interface': pynos.versions.ver_7.ver_7_0_0.interface.Interface,
        'lldp': pynos.versions.ver_7.ver_7_0_0.lldp.LLDP,
        'system': pynos.versions.ver_6.ver_6_0_1.system.System,
        'services': pynos.versions.ver_6.ver_6_0_1.services.Services,
        'fabric_service': pynos.versions.ver_6.ver_6_0_1.fabric_service
                          .FabricService,
        'vcs': pynos.versions.ver_6.ver_6_0_1.vcs.VCS,
        'firmware': pynos.versions.ver_7.ver_7_0_0.firmware.Firmware,
        'ras': pynos.versions.ver_6.ver_6_0_1.ras.RAS,
    },
    '7.1.0': {
        'bgp': pynos.versions.ver_7.ver_7_0_0.bgp.BGP,
        'snmp': pynos.versions.ver_6.ver_6_0_1.snmp.SNMP,
        'interface': pynos.versions.ver_7.ver_7_0_0.interface.Interface,
        'lldp': pynos.versions.ver_7.ver_7_0_0.lldp.LLDP,
        'system': pynos.versions.ver_7.ver_7_1_0.system.System,
        'services': pynos.versions.ver_6.ver_6_0_1.services.Services,
        'fabric_service': pynos.versions.ver_6.ver_6_0_1.fabric_service
                          .FabricService,
        'vcs': pynos.versions.ver_6.ver_6_0_1.vcs.VCS,
        'firmware': pynos.versions.ver_7.ver_7_0_0.firmware.Firmware,
        'ras': pynos.versions.ver_6.ver_6_0_1.ras.RAS,
    }
}

NOS_ATTRS = ['bgp', 'snmp', 'interface', 'lldp', 'system', 'services',
             'fabric_service', 'vcs', 'firmware', 'ras']


class DeviceCommError(Exception):
    """
    Error with device communication.
    """
    pass


class Device(object):
    """
    Device object holds the state for a single NOS device.

    Attributes:
        bgp: BGP related actions and attributes.
        interface: Interface related actions and attributes.
        snmp: SNMP related actions and attributes.
        lldp: LLDP related actions and attributes.
        system: System level actions and attributes.
    """

    def __init__(self, **kwargs):
        """
        Args:
            conn (tuple): IP/Hostname and port of the VDX device you
                intend to connect to. Ex. ('10.0.0.1', '22')
            auth (tuple): Username and password of the VDX device you
                intend to connect to. Ex. ('admin', 'password')
            hostkey_verify (bool): True to verify hostkey, False to bypass
                verify.
            auth_method (string): ```key``` if using ssh-key auth.
                ```userpass``` if using username/password auth.
            auth_key (string): Location of ssh key to use for authentication.

        Returns:
            Instance of the device object.

        Examples:
            >>> from pprint import pprint
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> dev.connection
            True
            >>> del dev
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     pprint(dev.mac_table) # doctest: +ELLIPSIS
            [{'interface'...'mac_address'...'state'...'type'...'vlan'...}]
            >>> dev.connection
            False
        """
        self._conn = kwargs.pop('conn')
        self._auth = kwargs.pop('auth', (None, None))
        self._hostkey_verify = kwargs.pop('hostkey_verify', None)
        self._auth_method = kwargs.pop('auth_method', 'userpass')
        self._auth_key = kwargs.pop('auth_key', None)
        self._test = kwargs.pop('test', False)
        self._callback = kwargs.pop('callback', None)
        if self._callback is None:
            self._callback = self._callback_main

        self._mgr = None

        if self._test is False:
            self.reconnect()
            ver = self.firmware_version
        else:
            ver = '5.0.1'

        for nos_attr in NOS_ATTRS:
            setattr(self, nos_attr, VERSIONS[ver][nos_attr](self._callback))

    def __enter__(self):
        if not self.connection and self._test is False:
            self.reconnect()
        return self

    def __exit__(self, exctype, excisnt, exctb):
        if self.connection:
            self.close()

    @property
    def mac_table(self):
        """list[dict]: the MAC table of the device.
        """
        table = []
        namespace = 'urn:brocade.com:mgmt:brocade-mac-address-table'
        request_mac_table = ET.Element('get-mac-address-table',
                                       xmlns=namespace)
        result = self._callback(request_mac_table, handler='get')
        for entry in result.findall('{%s}mac-address-table' % namespace):
            address = entry.find('{%s}mac-address' % namespace).text
            vlan = entry.find('{%s}vlanid' % namespace).text
            mac_type = entry.find('{%s}mac-type' % namespace).text
            state = entry.find('{%s}mac-state' % namespace).text
            interface = entry.find('{%s}forwarding-interface' % namespace)
            interface_type = interface.find('{%s}interface-type' %
                                            namespace).text
            interface_name = interface.find('{%s}interface-name' %
                                            namespace).text
            interface = '%s%s' % (interface_type, interface_name)

            table.append(dict(mac_address=address, interface=interface,
                              state=state, vlan=vlan,
                              type=mac_type))

        return table

    @property
    def firmware_version(self):
        """
        Returns firmware version.

        Args:
            None

        Returns:
            Dictionary

        Raises:
            None
        """
        namespace = "urn:brocade.com:mgmt:brocade-firmware-ext"

        request_ver = ET.Element("show-firmware-version", xmlns=namespace)

        ver = self._callback(request_ver, handler='get')
        return ver.find('.//*{%s}os-version' % namespace).text

    def _callback_main(self, call, handler='edit_config', target='running',
                       source='startup'):
        """
        Callback for NETCONF calls.

        Args:
            call: An Element Tree element containing the XML of the NETCONF
                call you intend to make to the device.
            handler: Type of ncclient call to make.
                get_config: NETCONF standard get config.
                get: ncclient dispatch. For custom RPCs.
                edit_config: NETCONF standard edit.
                delete_config: NETCONF standard delete.
                copy_config: NETCONF standard copy.
            target: Target configuration location for action. Only used for
                edit_config, delete_config, and copy_config.
            source: Source of configuration information for copying
                configuration. Only used for copy_config.

        Returns:
            None

        Raises:
            None
        """
        try:
            if handler == 'get_config':
                call = ET.tostring(call.getchildren()[0])
                return self._mgr.get(filter=('subtree', call))

            call = ET.tostring(call)
            if handler == 'get':
                call_element = xml_.to_ele(call)
                return ET.fromstring(str(self._mgr.dispatch(call_element)))
            if handler == 'edit_config':
                self._mgr.edit_config(target=target, config=call)
            if handler == 'delete_config':
                self._mgr.delete_config(target=target)
            if handler == 'copy_config':
                self._mgr.copy_config(target=target, source=source)
        except (ncclient.transport.TransportError,
                ncclient.transport.SessionCloseError,
                ncclient.transport.SSHError,
                ncclient.transport.AuthenticationError,
                ncclient.transport.SSHUnknownHostError) as error:
            logging.error(error)
            raise DeviceCommError

    @property
    def connection(self):
        """
        Poll if object is still connected to device in question.

        Args:
            None

        Returns:
            bool: True if connected, False if not.

        Raises:
            None
        """
        if self._test is False:
            return self._mgr.connected
        else:
            return False

    def reconnect(self):
        """
        Reconnect session with device.

        Args:
            None

        Returns:
            bool: True if reconnect succeeds, False if not.

        Raises:
            None
        """
        if self._auth_method is "userpass":
            self._mgr = manager.connect(host=self._conn[0],
                                        port=self._conn[1],
                                        username=self._auth[0],
                                        password=self._auth[1],
                                        hostkey_verify=self._hostkey_verify)
        elif self._auth_method is "key":
            self._mgr = manager.connect(host=self._conn[0],
                                        port=self._conn[1],
                                        username=self._auth[0],
                                        key_filename=self._auth_key,
                                        hostkey_verify=self._hostkey_verify)
        else:
            raise ValueError("auth_method incorrect value.")
        self._mgr.timeout = 600

        return True

    def find_interface_by_mac(self, **kwargs):
        """Find the interface through which a MAC can be reached.

        Args:
            mac_address (str): A MAC address in 'xx:xx:xx:xx:xx:xx' format.

        Returns:
            list[dict]: a list of mac table data.

        Raises:
            KeyError: if `mac_address` is not specified.

        Examples:
            >>> from pprint import pprint
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     x = dev.find_interface_by_mac(
            ...     mac_address='10:23:45:67:89:ab')
            ...     pprint(x) # doctest: +ELLIPSIS
            [{'interface'...'mac_address'...'state'...'type'...'vlan'...}]
        """
        mac = kwargs.pop('mac_address')
        results = [x for x in self.mac_table if x['mac_address'] == mac]
        return results

    def close(self):
        """Close NETCONF session.

        Args:
            None

        Returns:
            None

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> dev.connection
            True
            >>> dev.close() # doctest: +ELLIPSIS
            <?xml...<rpc-reply...<ok/>...
            >>> dev.connection
            False
        """
        return self._mgr.close_session()
