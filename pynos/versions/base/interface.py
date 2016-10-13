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
import re
import xml.etree.ElementTree as ET

from ipaddress import ip_interface

import pynos.utilities
from pynos.exceptions import InvalidVlanId
from pynos.versions.base.yang.brocade_interface import brocade_interface
from pynos.versions.base.yang.brocade_rbridge import brocade_rbridge


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
        self._interface = brocade_interface(
            callback=pynos.utilities.return_xml
        )
        self._rbridge = brocade_rbridge(
            callback=pynos.utilities.return_xml
        )

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

    def remove_port_channel(self, **kwargs):
        """
        Remove a port channel interface.

        Args:
            port_int (str): port-channel number (1, 2, 3, etc).
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `port_int` is not passed.
            ValueError: if `port_int` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name='225/0/20',
            ...         int_type='tengigabitethernet',
            ...         port_int='1', channel_type='standard', mode='active')
            ...         output = dev.interface.remove_port_channel(
            ...         port_int='1')
        """
        port_int = kwargs.pop('port_int')
        callback = kwargs.pop('callback', self._callback)

        if re.search('^[0-9]{1,3}$', port_int) is None:
            raise ValueError('%s must be in the format of x for port channel '
                             'interfaces.' % repr(port_int))

        port_channel = getattr(self._interface, 'interface_port_channel_name')
        port_channel_args = dict(name=port_int)

        config = port_channel(**port_channel_args)

        delete_channel = config.find('.//*port-channel')
        delete_channel.set('operation', 'delete')

        return callback(config)

    def ip_address(self, **kwargs):
        """
        Set IP Address on an Interface.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            name (str): Name of interface id.
                 (For interface: 1/0/5, 1/0/10 etc).
            ip_addr (str): IPv4/IPv6 Virtual IP Address..
                Ex: 10.10.10.1/24 or 2001:db8::/48
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `ip_addr` is not passed.
            ValueError: if `int_type`, `name`, or `ip_addr` are invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        int_type = 'tengigabitethernet'
            ...        name = '225/0/4'
            ...        ip_addr = '20.10.10.1/24'
            ...        output = dev.interface.disable_switchport(inter_type=
            ...        int_type, inter=name)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        output = dev.interface.add_vlan_int('86')
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, delete=True,
            ...        rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='225', ip_addr='10.225.225.225/32',
            ...        rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='225', ip_addr='10.225.225.225/32', delete=True,
            ...        rbridge_id='225')
            ...        ip_addr = 'fc00:1:3:1ad3:0:0:23:a/64'
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, rbridge_id='225')
            ...        output = dev.interface.ip_address(int_type='ve',
            ...        name='86', ip_addr=ip_addr, delete=True,
            ...        rbridge_id='225')
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        ip_addr = str(kwargs.pop('ip_addr'))
        delete = kwargs.pop('delete', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet', 've',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'loopback']

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))

        ipaddress = ip_interface(unicode(ip_addr))
        ip_args = dict(name=name, address=ip_addr)
        method_name = None
        method_class = self._interface
        if ipaddress.version == 4:
            method_name = 'interface_%s_ip_ip_config_address_'\
                          'address' % int_type
        elif ipaddress.version == 6:
            method_name = 'interface_%s_ipv6_ipv6_config_address_ipv6_'\
                          'address_address' % int_type

        if int_type == 've':
            method_name = "rbridge_id_%s" % method_name
            method_class = self._rbridge
            ip_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif int_type == 'loopback':
            method_name = 'rbridge_id_interface_loopback_ip_ip_config_'\
                          'address_address'
            if ipaddress.version == 6:
                method_name = 'rbridge_id_interface_loopback_ipv6_ipv6_'\
                              'config_address_ipv6_address_address'
            method_class = self._rbridge
            ip_args['rbridge_id'] = rbridge_id
            ip_args['id'] = name
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces.')

        ip_address_attr = getattr(method_class, method_name)
        config = ip_address_attr(**ip_args)
        if delete:
            config.find('.//*address').set('operation', 'delete')
        try:
            if kwargs.pop('get', False):
                return callback(config, handler='get_config')
            else:
                return callback(config)
        # TODO Setting IP on port channel is not done yet.
        except AttributeError:
            return None

    def get_ip_addresses(self, **kwargs):
        """
        Get IP Addresses already set on an Interface.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            name (str): Name of interface id.
                 (For interface: 1/0/5, 1/0/10 etc).
            version (int): 4 or 6 to represent IPv4 or IPv6 address
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            List of 0 or more IPs configure on the specified interface.

        Raises:
            KeyError: if `int_type` or `name` is not passed.
            ValueError: if `int_type` or `name` are invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        int_type = 'tengigabitethernet'
            ...        name = '225/0/4'
            ...        ip_addr = '20.10.10.1/24'
            ...        version = 4
            ...        output = dev.interface.disable_switchport(inter_type=
            ...        int_type, inter=name)
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        result = dev.interface.get_ip_addresses(
            ...        int_type=int_type, name=name, version=version)
            ...        assert len(result) >= 1
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
            ...        ip_addr = 'fc00:1:3:1ad3:0:0:23:a/64'
            ...        version = 6
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr)
            ...        result = dev.interface.get_ip_addresses(
            ...        int_type=int_type, name=name, version=version)
            ...        assert len(result) >= 1
            ...        output = dev.interface.ip_address(int_type=int_type,
            ...        name=name, ip_addr=ip_addr, delete=True)
        """

        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        version = int(kwargs.pop('version'))
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet']
        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))
        method_name = None
        method_class = self._interface
        if version == 4:
            method_name = 'interface_%s_ip_ip_config_address_' \
                          'address' % int_type
        elif version == 6:
            method_name = 'interface_%s_ipv6_ipv6_config_address_ipv6_' \
                          'address_address' % int_type

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces.')
        ip_args = dict(name=name, address='')
        ip_address_attr = getattr(method_class, method_name)
        config = ip_address_attr(**ip_args)

        output = callback(config, handler='get_config')
        result = []
        if version == 4:
            for item in output.data.findall(
                    './/{*}address/{*}address'):
                result.append(item.text)

        elif version == 6:
            for item in output.data.findall(
                    './/{*}address/{*}ipv6-address/{'
                    '*}address'):
                result.append(item.text)
        return result
        # TODO Getting IP's from ve and vlan is not done yet.

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
        """Set interface description.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            desc (str): The description of the interface.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `desc` is not specified.
            ValueError: if `name`, `int_type`, or `desc` is not a valid
                value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.description(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38',
            ...         desc='test')
            ...         dev.interface.description()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        desc = str(kwargs.pop('desc'))
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
            'port_channel',
            'vlan'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        desc_args = dict(name=name, description=desc)

        if int_type == "vlan":
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")

            config = self._interface.interface_vlan_interface_vlan_description(
                **desc_args
            )
        else:
            if not pynos.utilities.valid_interface(int_type, name):
                raise ValueError('`name` must be in the format of x/y/z for '
                                 'physical interfaces or x for port channel.')

            config = getattr(
                self._interface,
                'interface_%s_description' % int_type
            )(**desc_args)
        return callback(config)

    def private_vlan_type(self, **kwargs):
        """Set the PVLAN type (primary, isolated, community).

        Args:
            name (str): VLAN ID.
            pvlan_type (str): PVLAN type (primary, isolated, community)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `pvlan_type` is not specified.
            ValueError: if `name` or `pvlan_type` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> name = '90'
            >>> pvlan_type = 'isolated'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=name,
            ...         pvlan_type=pvlan_type)
            ...         dev.interface.private_vlan_type()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = kwargs.pop('name')
        pvlan_type = kwargs.pop('pvlan_type')
        callback = kwargs.pop('callback', self._callback)
        allowed_pvlan_types = ['isolated', 'primary', 'community']

        if not pynos.utilities.valid_vlan_id(name):
            raise InvalidVlanId("Incorrect name value.")

        if pvlan_type not in allowed_pvlan_types:
            raise ValueError("Incorrect pvlan_type")

        pvlan_args = dict(name=name, pvlan_type_leaf=pvlan_type)
        pvlan_type = getattr(self._interface,
                             'interface_vlan_interface_vlan_'
                             'private_vlan_pvlan_type_leaf')
        config = pvlan_type(**pvlan_args)
        return callback(config)

    def vlan_pvlan_association_add(self, **kwargs):
        """Add a secondary PVLAN to a primary PVLAN.

        Args:
            name (str): VLAN number (1-4094).
            sec_vlan (str): The secondary PVLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `sec_vlan` is not specified.
            ValueError: if `name` or `sec_vlan` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '20'
            >>> sec_vlan = '30'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=name,
            ...         pvlan_type='primary')
            ...         output = dev.interface.private_vlan_type(name=sec_vlan,
            ...         pvlan_type='isolated')
            ...         output = dev.interface.vlan_pvlan_association_add(
            ...         name=name, sec_vlan=sec_vlan)
            ...         dev.interface.vlan_pvlan_association_add()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = kwargs.pop('name')
        sec_vlan = kwargs.pop('sec_vlan')
        callback = kwargs.pop('callback', self._callback)

        if not pynos.utilities.valid_vlan_id(name):
            raise InvalidVlanId("Incorrect name value.")
        if not pynos.utilities.valid_vlan_id(sec_vlan):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `8191`.")

        pvlan_args = dict(name=name, sec_assoc_add=sec_vlan)
        pvlan_assoc = getattr(self._interface,
                              'interface_vlan_interface_vlan_'
                              'private_vlan_association_sec_assoc_add')
        config = pvlan_assoc(**pvlan_args)
        return callback(config)

    def pvlan_host_association(self, **kwargs):
        """Set interface PVLAN association.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            pri_vlan (str): The primary PVLAN.
            sec_vlan (str): The secondary PVLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan` is not
                specified.
            ValueError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan`
                is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/38'
            >>> pri_vlan = '75'
            >>> sec_vlan = '100'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=pri_vlan,
            ...         pvlan_type='primary')
            ...         output = dev.interface.private_vlan_type(name=sec_vlan,
            ...         pvlan_type='isolated')
            ...         output = dev.interface.vlan_pvlan_association_add(
            ...         name=pri_vlan, sec_vlan=sec_vlan)
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.private_vlan_mode(
            ...         int_type=int_type, name=name, mode='host')
            ...         output = dev.interface.pvlan_host_association(
            ...         int_type=int_type, name=name, pri_vlan=pri_vlan,
            ...         sec_vlan=sec_vlan)
            ...         dev.interface.pvlan_host_association()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        pri_vlan = kwargs.pop('pri_vlan')
        sec_vlan = kwargs.pop('sec_vlan')
        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        if not pynos.utilities.valid_vlan_id(pri_vlan):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `4095`.")
        if not pynos.utilities.valid_vlan_id(sec_vlan):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `4095`.")

        pvlan_args = dict(name=name, host_pri_pvlan=pri_vlan)

        associate_pvlan = getattr(self._interface,
                                  'interface_%s_switchport_private_vlan_'
                                  'host_association_host_pri_pvlan' %
                                  int_type)
        config = associate_pvlan(**pvlan_args)
        sec_assoc = config.find('.//*host-association')
        sec_assoc = ET.SubElement(sec_assoc, 'host-sec-pvlan')
        sec_assoc.text = sec_vlan
        return callback(config)

    def admin_state(self, **kwargs):
        """Set interface administrative state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            enabled (bool): Is the interface enabled? (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed and
                `get` is not ``True``.
            ValueError: if `int_type`, `name`, or `enabled` are invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.admin_state(
            ...         int_type='tengigabitethernet', name='225/0/38',
            ...         enabled=False)
            ...         dev.interface.admin_state(
            ...         int_type='tengigabitethernet', name='225/0/38',
            ...         enabled=True)
            ...         output = dev.interface.add_vlan_int('87')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='87', ip_addr='10.0.0.1/24', rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='ve',
            ...         name='87', enabled=True, rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='ve',
            ...         name='87', enabled=False, rbridge_id='225')
            ...         output = dev.interface.ip_address(int_type='loopback',
            ...         name='225', ip_addr='10.225.225.225/32',
            ...         rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='loopback',
            ...         name='225', enabled=True, rbridge_id='225')
            ...         output = dev.interface.admin_state(int_type='loopback',
            ...         name='225', enabled=False, rbridge_id='225')
            ...         output = dev.interface.ip_address(int_type='loopback',
            ...         name='225', ip_addr='10.225.225.225/32',
            ...         rbridge_id='225', delete=True)

        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        get = kwargs.pop('get', False)
        if get:
            enabled = None
        else:
            enabled = kwargs.pop('enabled')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've', 'loopback']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if not isinstance(enabled, bool) and not get:
            raise ValueError('`enabled` must be `True` or `False`.')

        state_args = dict(name=name)
        method_name = 'interface_%s_shutdown' % int_type
        method_class = self._interface
        if int_type == 've':
            method_name = "rbridge_id_%s" % method_name
            method_class = self._rbridge
            state_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif int_type == 'loopback':
            method_name = 'rbridge_id_interface_{0}_intf_'\
                          '{0}_shutdown'.format(int_type)
            method_class = self._rbridge
            state_args['rbridge_id'] = rbridge_id
            state_args['id'] = name
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        admin_state = getattr(method_class, method_name)
        config = admin_state(**state_args)
        if enabled:
            config.find('.//*shutdown').set('operation', 'delete')
        try:
            if get:
                return callback(config, handler='get_config')
            else:
                return callback(config)
        # TODO: Catch existing 'no shut'
        # This is in place because if the interface is already admin up,
        # `ncclient` will raise an error if you try to admin up the interface
        # again.
        except AttributeError:
            return None

    def pvlan_trunk_association(self, **kwargs):
        """Set switchport private vlan host association.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def trunk_allowed_vlan(self, **kwargs):
        """Modify allowed VLANs on Trunk (add, remove, none, all).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            action (str): Action to take on trunk. (add, remove, none, all)
            vlan (str): vlan id for action. Only valid for add and remove.
            ctag (str): ctag range. Only valid for add and remove.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is invalid.

        Examples:
            >>> # Skip due to current dev work
            >>> # TODO: Reenable after dev work
            >>> def test_trunk_allowed_vlan():
            ...     import pynos.device
            ...     switches = ['10.24.39.212', '10.24.39.202']
            ...     auth = ('admin', 'password')
            ...     int_type = 'tengigabitethernet'
            ...     name = '226/0/4'
            ...     for switch in switches:
            ...         conn = (switch, '22')
            ...         with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...             output = dev.interface.enable_switchport(int_type,
            ...             name)
            ...             output = dev.interface.trunk_mode(name=name,
            ...             int_type=int_type, mode='trunk')
            ...             output = dev.interface.add_vlan_int('25')
            ...             output = dev.interface.add_vlan_int('8000')
            ...             output = dev.interface.trunk_allowed_vlan(
            ...             int_type=int_type, name=name, action='add',
            ...             ctag='25', vlan='8000')
            ...             dev.interface.private_vlan_mode()
            ...             # doctest: +IGNORE_EXCEPTION_DETAIL
            >>> test_trunk_allowed_vlan() # doctest: +SKIP
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        action = kwargs.pop('action')
        ctag = kwargs.pop('ctag', None)
        vlan = kwargs.pop('vlan', None)
        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']
        valid_actions = ['add', 'remove', 'none', 'all']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" %
                             repr(int_types))

        if action not in valid_actions:
            raise ValueError('%s must be one of: %s' % (action, valid_actions))

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        allowed_vlan_args = dict(name=name,
                                 add=vlan,
                                 remove=vlan,
                                 trunk_vlan_id=vlan,
                                 trunk_ctag_range=ctag)

        ctag_actions = ['add', 'remove']

        if ctag and not vlan:
            raise ValueError('vlan must be set when ctag is set ')

        if ctag and action not in ctag_actions:
            raise ValueError('%s must be in %s when %s is set '
                             % (repr(action),
                                repr(ctag_actions),
                                repr(ctag)))

        if not ctag:
            allowed_vlan = getattr(self._interface,
                                   'interface_%s_switchport_trunk_'
                                   'allowed_vlan_%s' %
                                   (int_type, action))
        else:
            allowed_vlan = getattr(self._interface,
                                   'interface_%s_switchport_trunk_trunk_vlan_'
                                   'classification_allowed_vlan_%s_trunk_'
                                   'ctag_range'
                                   % ((int_type, action)))
        config = allowed_vlan(**allowed_vlan_args)
        return callback(config)

    def private_vlan_mode(self, **kwargs):
        """Set PVLAN mode (promiscuous, host, trunk).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): The switchport PVLAN mode.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/38'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.private_vlan_mode(
            ...         int_type=int_type, name=name, mode='trunk_host')
            ...         dev.interface.private_vlan_mode()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        mode = kwargs.pop('mode').lower()
        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']
        valid_modes = ['host', 'promiscuous', 'trunk_host',
                       'trunk_basic', 'trunk_promiscuous']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if mode not in valid_modes:
            raise ValueError('%s must be one of: %s' % (mode, valid_modes))

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        pvlan_args = dict(name=name)

        if 'trunk' in mode:
            pvlan_mode = getattr(self._interface,
                                 'interface_%s_switchport_mode_'
                                 'private_vlan_private_vlan_trunk_%s' %
                                 (int_type, mode))
        else:
            pvlan_mode = getattr(self._interface,
                                 'interface_%s_switchport_mode_'
                                 'private_vlan_%s' % (int_type, mode))
        config = pvlan_mode(**pvlan_args)
        return callback(config)

    def spanning_tree_state(self, **kwargs):
        """Set Spanning Tree state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, vlan, port_channel etc).
            name (str): Name of interface or VLAN id.
                (For interface: 1/0/5, 1/0/10 etc).
                (For VLANs 0, 1, 100 etc).
                (For Port Channels 1, 100 etc).
            enabled (bool): Is Spanning Tree enabled? (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `enabled` is not passed.
            ValueError: if `int_type`, `name`, or `enabled` are invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         enabled = True
            ...         int_type = 'tengigabitethernet'
            ...         name = '225/0/37'
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         enabled = False
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         int_type = 'vlan'
            ...         name = '102'
            ...         enabled = False
            ...         output = dev.interface.add_vlan_int(name)
            ...         output = dev.interface.enable_switchport(
            ...             int_type, name)
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         enabled = False
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         output = dev.interface.del_vlan_int(name)
            ...         int_type = 'port_channel'
            ...         name = '2'
            ...         enabled = False
            ...         output = dev.interface.channel_group(name='225/0/20',
            ...                              int_type='tengigabitethernet',
            ...                              port_int=name,
            ...                              channel_type='standard',
            ...                              mode='active')
            ...         output = dev.interface.enable_switchport(
            ...             int_type, name)
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         enabled = False
            ...         output = dev.interface.spanning_tree_state(
            ...         int_type=int_type, name=name, enabled=enabled)
            ...         output = dev.interface.remove_port_channel(
            ...             port_int=name)
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        enabled = kwargs.pop('enabled')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 'vlan']

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))

        if not isinstance(enabled, bool):
            raise ValueError('%s must be `True` or `False`.' % repr(enabled))

        if int_type == 'vlan':
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId('%s must be between 0 to 8191.' % int_type)

            state_args = dict(name=name)
            spanning_tree_state = getattr(self._interface,
                                          'interface_%s_interface_%s_spanning_'
                                          'tree_stp_shutdown' % (int_type,
                                                                 int_type))

        else:
            if not pynos.utilities.valid_interface(int_type, name):
                raise ValueError('`name` must be in the format of x/y/z for '
                                 'physical interfaces or x for port channel.')

            state_args = dict(name=name)
            spanning_tree_state = getattr(self._interface,
                                          'interface_%s_spanning_tree_'
                                          'shutdown' % int_type)

        config = spanning_tree_state(**state_args)

        if enabled:
            if int_type == 'vlan':
                shutdown = config.find('.//*stp-shutdown')
            else:
                shutdown = config.find('.//*shutdown')
            shutdown.set('operation', 'delete')
        try:
            return callback(config)
        # TODO: Catch existing 'no shut'
        # This is in place because if the interface spanning tree is already
        # up,`ncclient` will raise an error if you try to admin up the
        # interface again.
        # TODO: add logic to shutdown STP at protocol level too.
        except AttributeError:
            return None

    def tag_native_vlan(self, **kwargs):
        """Set tagging of native VLAN on trunk.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): Trunk port mode (trunk, trunk-no-default-native).
            enabled (bool): Is tagging of the VLAN enabled on trunks?
                (True, False)
            callback (function): A function executed upon completion oj the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not specified.
            ValueError: if `int_type`, `name`, or `state` is not valid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.trunk_mode(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38', mode='trunk')
            ...         output = dev.interface.tag_native_vlan(name='225/0/38',
            ...         int_type='tengigabitethernet')
            ...         output = dev.interface.tag_native_vlan(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/38', enabled=False)
            ...         dev.interface.tag_native_vlan()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        if not isinstance(enabled, bool):
            raise ValueError("Invalid state.")

        tag_args = dict(name=name)
        tag_native_vlan = getattr(self._interface, 'interface_%s_switchport_'
                                  'trunk_tag_native_vlan' % int_type)
        config = tag_native_vlan(**tag_args)
        if not enabled:
            untag = config.find('.//*native-vlan')
            untag.set('operation', 'delete')

        try:
            return callback(config)
        # TODO: Catch existing 'no switchport tag native-vlan'
        except AttributeError:
            return None

    def switchport_pvlan_mapping(self, **kwargs):
        """Switchport private VLAN mapping.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            pri_vlan (str): The primary PVLAN.
            sec_vlan (str): The secondary PVLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/37'
            >>> pri_vlan = '3000'
            >>> sec_vlan = ['3001', '3002']
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.private_vlan_type(name=pri_vlan,
            ...         pvlan_type='primary')
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.private_vlan_mode(
            ...         int_type=int_type, name=name, mode='trunk_promiscuous')
            ...         for spvlan in sec_vlan:
            ...             output = dev.interface.private_vlan_type(
            ...             name=spvlan, pvlan_type='isolated')
            ...             output = dev.interface.vlan_pvlan_association_add(
            ...             name=pri_vlan, sec_vlan=spvlan)
            ...             output = dev.interface.switchport_pvlan_mapping(
            ...             int_type=int_type, name=name, pri_vlan=pri_vlan,
            ...             sec_vlan=spvlan)
            ...         dev.interface.switchport_pvlan_mapping()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        pri_vlan = kwargs.pop('pri_vlan')
        sec_vlan = kwargs.pop('sec_vlan')
        callback = kwargs.pop('callback', self._callback)
        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError("`name` must be in the format of x/y/x for "
                             "physical interfaces or x for port channel.")

        if not pynos.utilities.valid_vlan_id(pri_vlan, extended=True):
            raise InvalidVlanId("`pri_vlan` must be between `1` and `4096`")

        if not pynos.utilities.valid_vlan_id(sec_vlan, extended=True):
            raise InvalidVlanId("`sec_vlan` must be between `1` and `4096`")

        pvlan_args = dict(name=name,
                          promis_pri_pvlan=pri_vlan,
                          promis_sec_pvlan_range=sec_vlan)
        pvlan_mapping = getattr(self._interface,
                                'interface_gigabitethernet_switchport_'
                                'private_vlan_mapping_promis_sec_pvlan_range')
        config = pvlan_mapping(**pvlan_args)
        return callback(config)

    def mtu(self, **kwargs):
        """Set interface mtu.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mtu (str): Value between 1522 and 9216
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mtu` is not specified.
            ValueError: if `int_type`, `name`, or `mtu` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.mtu(mtu='1666',
            ...         int_type='tengigabitethernet', name='225/0/38')
            ...         dev.interface.mtu() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        mtu = kwargs.pop('mtu')
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
            'port_channel'
        ]

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        minimum_mtu = 1522
        maximum_mtu = 9216
        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError("Incorrect mtu value 1522-9216")

        mtu_args = dict(name=name, mtu=mtu)

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        config = getattr(
            self._interface,
            'interface_%s_mtu' % int_type
        )(**mtu_args)
        return callback(config)

    def ip_mtu(self, **kwargs):
        """Set interface mtu.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mtu (str): Value between 1300 and 9018
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mtu` is not specified.
            ValueError: if `int_type`, `name`, or `mtu` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.ip_mtu(mtu='1666',
            ...         int_type='tengigabitethernet', name='225/0/38')
            ...         dev.interface.ip_mtu() # doctest:
            +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        mtu = kwargs.pop('mtu')
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        minimum_mtu = 1300
        maximum_mtu = 9018
        if int(mtu) < minimum_mtu or int(mtu) > maximum_mtu:
            raise ValueError("Incorrect mtu value 1300-9018")

        mtu_args = dict(name=name, mtu=mtu)

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces.')

        config = getattr(
            self._interface,
            'interface_%s_ip_ip_config_mtu' % int_type
        )(**mtu_args)
        return callback(config)

    def fabric_isl(self, **kwargs):
        """Set fabric ISL state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            enabled (bool): Is fabric ISL state enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not specified.
            ValueError: if `int_type`, `name`, or `state` is not a valid value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.fabric_isl(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/40',
            ...         enabled=False)
            ...         dev.interface.fabric_isl()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" %
                             repr(int_types))

        if not isinstance(enabled, bool):
            raise ValueError('`enabled` must be `True` or `False`.')

        fabric_isl_args = dict(name=name)

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError("`name` must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                             "{1,3}$`")

        config = getattr(
            self._interface,
            'interface_%s_fabric_fabric_isl_fabric_isl_enable' % int_type
        )(**fabric_isl_args)

        if not enabled:
            fabric_isl = config.find('.//*fabric-isl')
            fabric_isl.set('operation', 'delete')

        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        else:
            return callback(config)

    def fabric_trunk(self, **kwargs):
        """Set fabric trunk state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            enabled (bool): Is Fabric trunk enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not specified.
            ValueError: if `int_type`, `name`, or `state` is not a valid value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.fabric_trunk(name='225/0/40',
            ...         int_type='tengigabitethernet', enabled=False)
            ...         dev.interface.fabric_trunk()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        if not isinstance(enabled, bool):
            raise ValueError('`enabled` must be `True` or `False`.')

        fabric_trunk_args = dict(name=name)

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError("`name` must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                             "{1,3}$`")

        config = getattr(
            self._interface,
            'interface_%s_fabric_fabric_trunk_fabric_trunk_enable' % int_type
        )(**fabric_trunk_args)

        if not enabled:
            fabric_trunk = config.find('.//*fabric-trunk')
            fabric_trunk.set('operation', 'delete')

        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        else:
            return callback(config)

    def v6_nd_suppress_ra(self, **kwargs):
        """Disable IPv6 Router Advertisements

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `rbridge_id` is not specified.
            ValueError: if `int_type`, `name`, or `rbridge_id` is not a valid
                value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_vlan_int('10')
            ...         output = dev.interface.v6_nd_suppress_ra(name='10',
            ...         int_type='ve', rbridge_id='225')
            ...         dev.interface.v6_nd_suppress_ra()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet',
            've'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        if int_type == "ve":
            if not pynos.utilities.valid_vlan_id(name):
                raise ValueError("`name` must be between `1` and `8191`")

            rbridge_id = kwargs.pop('rbridge_id', "1")

            nd_suppress_args = dict(name=name, rbridge_id=rbridge_id)
            nd_suppress = getattr(self._rbridge,
                                  'rbridge_id_interface_ve_ipv6_'
                                  'ipv6_nd_ra_ipv6_intf_cmds_'
                                  'nd_suppress_ra_suppress_ra_all')
            config = nd_suppress(**nd_suppress_args)
        else:
            if not pynos.utilities.valid_interface(int_type, name):
                raise ValueError("`name` must match "
                                 "`^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$`")

            nd_suppress_args = dict(name=name)
            nd_suppress = getattr(self._interface,
                                  'interface_%s_ipv6_ipv6_nd_ra_'
                                  'ipv6_intf_cmds_nd_suppress_ra_'
                                  'suppress_ra_all' % int_type)
            config = nd_suppress(**nd_suppress_args)
        return callback(config)

    def vrrp_vip(self, **kwargs):
        """Set VRRP VIP.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): VRRPv3 ID.
            vip (str): IPv4/IPv6 Virtual IP Address.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vip` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vip` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.anycast_mac(rbridge_id='225',
            ...         mac='aabb.ccdd.eeff', delete=True)
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=True, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=True,
            ...         rbridge_id='225')
            ...         output = dev.interface.set_ip('tengigabitethernet',
            ...         '225/0/18', '10.1.1.2/24')
            ...         output = dev.interface.ip_address(name='225/0/18',
            ...         int_type='tengigabitethernet',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', vip='10.1.1.1/24')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='2001:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         output = dev.interface.add_vlan_int('89')
            ...         output = dev.interface.ip_address(name='89',
            ...         int_type='ve', ip_addr='172.16.1.1/24',
            ...         rbridge_id='225')
            ...         output = dev.interface.ip_address(name='89',
            ...         int_type='ve', rbridge_id='225',
            ...         ip_addr='2002:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='ve', name='89',
            ...         vrid='1', vip='172.16.1.2/24', rbridge_id='225')
            ...         dev.interface.vrrp_vip(int_type='ve', name='89',
            ...         vrid='1', vip='fe80::dafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         dev.interface.vrrp_vip(int_type='ve', name='89',
            ...         vrid='1', vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=False, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=False,
            ...         rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        vip = kwargs.pop('vip')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        ipaddress = ip_interface(unicode(vip))
        vrrp_vip = None
        vrrp_args = dict(name=name,
                         vrid=vrid,
                         virtual_ipaddr=str(ipaddress.ip))
        method_class = self._interface

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if ipaddress.version == 4:
            vrrp_args['version'] = '3'
            method_name = 'interface_%s_vrrp_virtual_ip_virtual_' \
                          'ipaddr' % int_type
        elif ipaddress.version == 6:
            method_name = 'interface_%s_ipv6_vrrpv3_group_virtual_ip_' \
                          'virtual_ipaddr' % int_type

        if int_type == 've':
            method_name = 'rbridge_id_%s' % method_name
            if ipaddress.version == 6:
                method_name = method_name.replace('group_', '')
            method_class = self._rbridge
            vrrp_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        vrrp_vip = getattr(method_class, method_name)
        config = vrrp_vip(**vrrp_args)
        return callback(config)

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
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): VRRPv3 ID.
            priority (str): VRRP Priority.
            ip_version (str): Version of IP (4, 6).
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `vrid`, `priority`, or
                `ip_version` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, `priority`, or
                `ip_version` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.anycast_mac(rbridge_id='225',
            ...         mac='aabb.ccdd.eeff', delete=True)
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=True, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=True,
            ...         rbridge_id='225')
            ...         output = dev.interface.set_ip('tengigabitethernet',
            ...         '225/0/18', '10.1.1.2/24')
            ...         output = dev.interface.ip_address(name='225/0/18',
            ...         int_type='tengigabitethernet',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', vip='10.1.1.1/24')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='2001:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_priority(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', ip_version='4',
            ...         priority='66')
            ...         dev.interface.vrrp_priority(
            ...         int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', ip_version='6',
            ...         priority='77')
            ...         output = dev.interface.add_vlan_int('88')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='88', ip_addr='172.16.10.1/24', rbridge_id='225')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='88', rbridge_id='225',
            ...         ip_addr='2003:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrp_vip(int_type='ve', name='88',
            ...         vrid='1', vip='172.16.10.2/24', rbridge_id='225')
            ...         dev.interface.vrrp_vip(int_type='ve', name='88',
            ...         rbridge_id='225', vrid='1',
            ...         vip='fe80::dafe:beef:1000:1/64')
            ...         dev.interface.vrrp_vip(int_type='ve', rbridge_id='225',
            ...         name='88', vrid='1',
            ...         vip='2003:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         dev.interface.vrrp_priority(int_type='ve', name='88',
            ...         rbridge_id='225', vrid='1', ip_version='4',
            ...         priority='66')
            ...         dev.interface.vrrp_priority(int_type='ve', name='88',
            ...         rbridge_id='225', vrid='1', ip_version='6',
            ...         priority='77')
            ...         output = dev.services.vrrp(ip_version='6',
            ...         enabled=False, rbridge_id='225')
            ...         output = dev.services.vrrp(enabled=False,
            ...         rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        priority = kwargs.pop('priority')
        ip_version = int(kwargs.pop('ip_version'))
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        vrrp_args = dict(name=name, vrid=vrid, priority=priority)
        vrrp_priority = None
        method_name = None
        method_class = self._interface

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))

        if ip_version == 4:
            vrrp_args['version'] = '3'
            method_name = 'interface_%s_vrrp_priority' % int_type
        elif ip_version == 6:
            method_name = 'interface_%s_ipv6_vrrpv3_group_priority' % int_type

        if int_type == 've':
            method_name = "rbridge_id_%s" % method_name
            if ip_version == 6:
                method_name = method_name.replace('group_', '')
            method_class = self._rbridge
            vrrp_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        vrrp_priority = getattr(method_class, method_name)
        config = vrrp_priority(**vrrp_args)
        return callback(config)

    def vrrp_advertisement_interval(self, **kwargs):
        """Set VRRP advertisement interval.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

    def proxy_arp(self, **kwargs):
        """Set interface administrative state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            enabled (bool): Is proxy-arp enabled? (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not passed.
            ValueError: if `int_type`, `name`, or `state` is invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.proxy_arp(int_type='tengigabitethernet',
            ...         name='225/0/12', enabled=True)
            ...         dev.interface.proxy_arp(int_type='tengigabitethernet',
            ...         name='225/0/12', enabled=False)
            ...         output = dev.interface.add_vlan_int('86')
            ...         output = dev.interface.ip_address(int_type='ve',
            ...         name='86', ip_addr='172.16.2.1/24', rbridge_id='225')
            ...         output = dev.interface.proxy_arp(int_type='ve',
            ...         name='86', enabled=True, rbridge_id='225')
            ...         output = dev.interface.proxy_arp(int_type='ve',
            ...         name='86', enabled=False, rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        enabled = kwargs.pop('enabled', True)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        if not isinstance(enabled, bool):
            raise ValueError('`enabled` must be `True` or `False`.')

        method_name = 'interface_%s_ip_ip_config_proxy_arp' % int_type
        method_class = self._interface
        proxy_arp_args = dict(name=name)
        if int_type == 've':
            method_name = "rbridge_id_%s" % method_name
            method_class = self._rbridge
            proxy_arp_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'phyiscal interfaces or x for port channel.')

        proxy_arp = getattr(method_class, method_name)
        config = proxy_arp(**proxy_arp_args)
        if not enabled:
            config.find('.//*proxy-arp').set('operation', 'delete')
        try:
            return callback(config)
        # TODO: Catch existing 'no proxy arp'
        # This is in place because if proxy arp is already disabled,
        # `ncclient` will raise an error if you try to disable it again.
        except AttributeError:
            return None

    def port_channel_minimum_links(self, **kwargs):
        """Set minimum number of links in a port channel.

        Args:
            name (str): Port-channel number. (1, 5, etc)
            minimum_links (str): Minimum number of links in channel group.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `minimum_links` is not specified.
            ValueError: if `name` is not a valid value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.port_channel_minimum_links(
            ...         name='1', minimum_links='2')
            ...         dev.interface.port_channel_minimum_links()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = str(kwargs.pop('name'))
        minimum_links = str(kwargs.pop('minimum_links'))
        callback = kwargs.pop('callback', self._callback)

        min_links_args = dict(name=name, minimum_links=minimum_links)

        if not pynos.utilities.valid_interface('port_channel', name):
            raise ValueError("`name` must match `^[0-9]{1,3}${1,3}$`")

        config = getattr(
            self._interface,
            'interface_port_channel_minimum_links'
        )(**min_links_args)

        return callback(config)

    def channel_group(self, **kwargs):
        """set channel group mode.

        args:
            int_type (str): type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): name of interface. (1/0/5, 1/0/10, etc)
            port_int (str): port-channel number (1, 2, 3, etc).
            channel_type (str): tiype of port-channel (standard, brocade)
            mode (str): mode of channel group (active, on, passive).
            delete (bool): Removes channel group configuration from this
                interface if `delete` is ``True``.
            callback (function): a function executed upon completion of the
                method.  the only parameter passed to `callback` will be the
                ``elementtree`` `config`.

        returns:
            return value of `callback`.

        raises:
            keyerror: if `int_type`, `name`, or `description` is not specified.
            valueerror: if `name` or `int_type` are not valid values.

        examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name='225/0/20',
            ...         int_type='tengigabitethernet',
            ...         port_int='1', channel_type='standard', mode='active')
            ...         dev.interface.channel_group()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        channel_type = kwargs.pop('channel_type')
        port_int = kwargs.pop('port_int')
        mode = kwargs.pop('mode')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))

        valid_modes = ['active', 'on', 'passive']

        if mode not in valid_modes:
            raise ValueError("`mode` must be one of: %s" % repr(valid_modes))

        valid_types = ['brocade', 'standard']

        if channel_type not in valid_types:
            raise ValueError("`channel_type` must be one of: %s" %
                             repr(valid_types))

        if not pynos.utilities.valid_interface('port_channel', port_int):
            raise ValueError("incorrect port_int value.")

        channel_group_args = dict(name=name, mode=mode)

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError("incorrect name value.")

        config = getattr(
            self._interface,
            'interface_%s_channel_group_mode' % int_type
        )(**channel_group_args)

        channel_group = config.find('.//*channel-group')
        if delete is True:
            channel_group.set('operation', 'delete')
        else:
            ET.SubElement(channel_group, 'port-int').text = port_int
            ET.SubElement(channel_group, 'type').text = channel_type

        return callback(config)

    def port_channel_vlag_ignore_split(self, **kwargs):
        """Ignore VLAG Split.

        Args:
            name (str): Port-channel number. (1, 5, etc)
            enabled (bool): Is ignore split enabled? (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `name` or `enable` is not specified.
            ValueError: if `name` is not a valid value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.port_channel_vlag_ignore_split(
            ...         name='1', enabled=True)
            ...         dev.interface.port_channel_vlag_ignore_split()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = str(kwargs.pop('name'))
        enabled = bool(kwargs.pop('enabled', True))
        callback = kwargs.pop('callback', self._callback)

        vlag_ignore_args = dict(name=name)

        if not pynos.utilities.valid_interface('port_channel', name):
            raise ValueError("`name` must match x")

        config = getattr(
            self._interface,
            'interface_port_channel_vlag_ignore_split'
        )(**vlag_ignore_args)

        if not enabled:
            ignore_split = config.find('.//*ignore-split')
            ignore_split.set('operation', 'delete')

        return callback(config)

    def trunk_mode(self, **kwargs):
        """Set trunk mode (trunk, trunk-no-default-vlan).

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): Trunk port mode (trunk, trunk-no-default-native).
            callback (function): A function executed upon completion oj the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `mode` is not specified.
            ValueError: if `int_type`, `name`, or `mode` is not valid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.trunk_mode(name='225/0/38',
            ...         int_type='tengigabitethernet', mode='trunk')
            ...         dev.interface.trunk_mode()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        mode = kwargs.pop('mode').lower()
        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        valid_modes = ['trunk', 'trunk-no-default-native']
        if mode not in valid_modes:
            raise ValueError("Incorrect mode value")

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        mode_args = dict(name=name, vlan_mode=mode)
        switchport_mode = getattr(self._interface, 'interface_%s_switchport_'
                                  'mode_vlan_mode' % int_type)
        config = switchport_mode(**mode_args)
        return callback(config)

    def transport_service(self, **kwargs):
        """Configure VLAN Transport Service.

        Args:
            vlan (str): The VLAN ID.
            service_id (str): The transport-service ID.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vlan` or `service_id` is not specified.
            ValueError: if `vlan` is invalid.

        Examples:
            >>> # Skip due to current work in devel
            >>> # TODO: Reenable
            >>> def test_transport_service():
            ...     import pynos.device
            ...     switches = ['10.24.39.212', '10.24.39.202']
            ...     auth = ('admin', 'password')
            ...     vlan = '6666'
            ...     service_id = '1'
            ...     for switch in switches:
            ...         conn = (switch, '22')
            ...         with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...             output = dev.interface.add_vlan_int(vlan)
            ...             output = dev.interface.spanning_tree_state(
            ...             int_type='vlan', name=vlan, enabled=False)
            ...             output = dev.interface.transport_service(vlan=vlan,
            ...             service_id=service_id)
            ...             dev.interface.transport_service()
            ...             # doctest: +IGNORE_EXCEPTION_DETAIL
            >>> test_transport_service() # doctest: +SKIP
        """
        vlan = kwargs.pop('vlan')
        service_id = kwargs.pop('service_id')
        callback = kwargs.pop('callback', self._callback)

        if not pynos.utilities.valid_vlan_id(vlan, extended=True):
            raise InvalidVlanId("vlan must be between `1` and `8191`")

        service_args = dict(name=vlan, transport_service=service_id)
        transport_service = getattr(self._interface,
                                    'interface_vlan_interface_vlan_'
                                    'transport_service')
        config = transport_service(**service_args)
        return callback(config)

    def lacp_timeout(self, **kwargs):
        """Set lacp timeout.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            timeout (str):  Timeout length.  (short, long)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `timeout` is not specified.
            ValueError: if `int_type`, `name`, or `timeout is not valid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/39'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name=name,
            ...         int_type=int_type, port_int='1',
            ...         channel_type='standard', mode='active')
            ...         output = dev.interface.lacp_timeout(name=name,
            ...         int_type=int_type, timeout='long')
            ...         dev.interface.lacp_timeout()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        timeout = kwargs.pop('timeout')
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
        ]

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        valid_timeouts = ['long', 'short']
        if timeout not in valid_timeouts:
            raise ValueError("Incorrect timeout value")

        timeout_args = dict(name=name, timeout=timeout)

        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError("Incorrect name value.")

        config = getattr(
            self._interface,
            'interface_%s_lacp_timeout' % int_type
        )(**timeout_args)
        return callback(config)

    def switchport(self, **kwargs):
        """Set interface switchport status.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            enabled (bool): Is the interface enabled? (True, False)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type` or `name` is not specified.
            ValueError: if `name` or `int_type` is not a valid
                value.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.switchport(name='225/0/19',
            ...         int_type='tengigabitethernet')
            ...         output = dev.interface.switchport(name='225/0/19',
            ...         int_type='tengigabitethernet', enabled=False)
            ...         dev.interface.switchport()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)
        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel', 'vlan']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))
        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        switchport_args = dict(name=name)
        switchport = getattr(self._interface,
                             'interface_%s_switchport_basic_basic' % int_type)

        config = switchport(**switchport_args)
        if not enabled:
            config.find('.//*switchport-basic').set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        else:
            return callback(config)

    def acc_vlan(self, **kwargs):
        """Set access VLAN on a port.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            vlan (str): VLAN ID to set as the access VLAN.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `vlan` is not specified.
            ValueError: if `int_type`, `name`, or `vlan` is not valid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/30'
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.add_vlan_int('736')
            ...         output = dev.interface.enable_switchport(int_type,
            ...         name)
            ...         output = dev.interface.acc_vlan(int_type=int_type,
            ...         name=name, vlan='736')
            ...         dev.interface.acc_vlan()
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type')
        name = kwargs.pop('name')
        vlan = kwargs.pop('vlan')
        callback = kwargs.pop('callback', self._callback)
        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("`int_type` must be one of: %s" % repr(int_types))
        if not pynos.utilities.valid_vlan_id(vlan):
            raise InvalidVlanId("`name` must be between `1` and `4096`")
        if not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        vlan_args = dict(name=name, accessvlan=vlan)
        access_vlan = getattr(self._interface,
                              'interface_%s_switchport_access_accessvlan' %
                              int_type)
        config = access_vlan(**vlan_args)
        return callback(config)

    @property
    def interfaces(self):
        """list[dict]: A list of dictionary items describing the operational
        state of interfaces.
        This method currently only lists the Physical Interfaces (
        Gigabitethernet, tengigabitethernet, fortygigabitethernet,
        hundredgigabitethernet) and Loopback interfaces.  It currently
        excludes VLAN interfaces, FCoE, Port-Channels, Management and Fibre
        Channel ports.
        """
        urn = "{urn:brocade.com:mgmt:brocade-interface-ext}"
        int_ns = 'urn:brocade.com:mgmt:brocade-interface-ext'

        result = []
        has_more = ''
        last_interface_name = ''
        last_interface_type = ''

        while (has_more == '') or (has_more == 'true'):
            request_interface = self.get_interface_detail_request(
                last_interface_name, last_interface_type)
            interface_result = self._callback(request_interface, 'get')
            has_more = interface_result.find('%shas-more' % urn).text

            for item in interface_result.findall('%sinterface' % urn):
                interface_type = item.find('%sinterface-type' % urn).text
                interface_name = item.find('%sinterface-name' % urn).text
                last_interface_type = interface_type
                last_interface_name = interface_name
                if "gigabitethernet" in interface_type:
                    interface_role = item.find('%sport-role' % urn).text
                    if_name = item.find('%sif-name' % urn).text
                    interface_state = item.find('%sif-state' % urn).text
                    interface_proto_state = item.find('%sline-protocol-state' %
                                                      urn).text
                    interface_mac = item.find(
                        '%scurrent-hardware-address' % urn).text

                    item_results = {'interface-type': interface_type,
                                    'interface-name': interface_name,
                                    'interface-role': interface_role,
                                    'if-name': if_name,
                                    'interface-state': interface_state,
                                    'interface-proto-state':
                                        interface_proto_state,
                                    'interface-mac': interface_mac}
                    result.append(item_results)
        # Loopback interfaces. Probably for other non-physical interfaces, too.
        ip_result = []
        request_interface = ET.Element('get-ip-interface', xmlns=int_ns)
        interface_result = self._callback(request_interface, 'get')
        for interface in interface_result.findall('%sinterface' % urn):
            int_type = interface.find('%sinterface-type' % urn).text
            int_name = interface.find('%sinterface-name' % urn).text
            if int_type == 'unknown':
                continue

            int_state = interface.find('%sif-state' % urn).text
            int_proto_state = interface.find('%sline-protocol-state' %
                                             urn).text
            ip_address = interface.find('.//%sipv4' % urn).text
            results = {'interface-type': int_type,
                       'interface-name': int_name,
                       'interface-role': None,
                       'if-name': None,
                       'interface-state': int_state,
                       'interface-proto-state': int_proto_state,
                       'interface-mac': None,
                       'ip-address': ip_address}
            x = next((x for x in result if int_type == x['interface-type'] and
                      int_name == x['interface-name']), None)
            if x is not None:
                results.update(x)
            ip_result.append(results)
        return ip_result

    @staticmethod
    def get_interface_detail_request(last_interface_name,
                                     last_interface_type):
        """ Creates a new Netconf request based on the last received
        interface name and type when the hasMore flag is true
        """

        request_interface = ET.Element(
            'get-interface-detail',
            xmlns="urn:brocade.com:mgmt:brocade-interface-ext"
        )
        if last_interface_name != '':
            last_received_int = ET.SubElement(request_interface,
                                              "last-rcvd-interface")
            last_int_type_el = ET.SubElement(last_received_int,
                                             "interface-type")
            last_int_type_el.text = last_interface_type
            last_int_name_el = ET.SubElement(last_received_int,
                                             "interface-name")
            last_int_name_el.text = last_interface_name
        return request_interface

    @property
    def interface_detail(self):
        """list[dict]: A list of dictionary items describing the
        interface type, name, role, mac, admin and operational
        state of interfaces of all rbridges.
        This method currently only lists the Physical Interfaces (
        Gigabitethernet, tengigabitethernet, fortygigabitethernet,
        hundredgigabitethernet) and port-channel
        """
        urn = "{urn:brocade.com:mgmt:brocade-interface-ext}"

        result = []
        has_more = ''
        last_interface_name = ''
        last_interface_type = ''

        while (has_more == '') or (has_more == 'true'):
            request_interface = self.get_interface_detail_request(
                last_interface_name, last_interface_type)
            interface_result = self._callback(request_interface, 'get')
            has_more = interface_result.find('%shas-more' % urn).text

            for item in interface_result.findall('%sinterface' % urn):
                interface_type = item.find('%sinterface-type' % urn).text
                interface_name = item.find('%sinterface-name' % urn).text
                last_interface_type = interface_type
                last_interface_name = interface_name
                if "gigabitethernet" in interface_type or "port-channel" in \
                        interface_type:
                    if "gigabitethernet" in interface_type:
                        interface_role = item.find('%sport-role' % urn).text
                    else:
                        interface_role = "None"
                    if_name = item.find('%sif-name' % urn).text
                    interface_state = item.find('%sif-state' % urn).text
                    interface_proto_state = item.find('%sline-protocol-state' %
                                                      urn).text
                    interface_mac = item.find(
                        '%scurrent-hardware-address' % urn).text
                    item_results = {'interface-type': interface_type,
                                    'interface-name': interface_name,
                                    'interface-role': interface_role,
                                    'if-name': if_name,
                                    'interface-state': interface_state,
                                    'interface-proto-state':
                                        interface_proto_state,
                                    'interface-mac': interface_mac}
                result.append(item_results)

        return result

    @property
    def vlans(self):
        """list[dict]: A list of dictionary items describing the details of
        vlan interfaces.
        This method fetches the VLAN interfaces
        Examples:
            >>> import pynos.device
            >>> switch = '10.24.39.202'
            >>> auth = ('admin', 'password')
            >>> conn = (switch, '22')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.add_vlan_int('736')
            ...     interfaces = dev.interface.vlans
            ...     is_vlan_interface_present = False
            ...     for interface in interfaces:
            ...         if interface['vlan-id'] == '736':
            ...             is_vlan_interface_present = True
            ...             break
            ...     dev.interface.del_vlan_int('736')
            ...     assert is_vlan_interface_present
            True
        """
        urn = "{urn:brocade.com:mgmt:brocade-interface-ext}"

        result = []
        has_more = ''
        last_vlan_id = ''
        while (has_more == '') or (has_more == 'true'):
            request_interface = self.get_vlan_brief_request(last_vlan_id)
            interface_result = self._callback(request_interface, 'get')
            has_more = self.get_node_value(interface_result, '%shas-more', urn)
            last_vlan_id = self.get_node_value(
                interface_result, '%slast-vlan-id', urn)
            for interface in interface_result.findall('%svlan' % urn):
                vlan_id = self.get_node_value(interface, '%svlan-id', urn)
                vlan_type = self.get_node_value(interface, '%svlan-type', urn)
                vlan_name = self.get_node_value(interface, '%svlan-name', urn)
                vlan_state = self.get_node_value(
                    interface, '%svlan-state', urn)
                ports = []
                for intf in interface.findall('%sinterface' % urn):
                    interface_type = self.get_node_value(
                        intf, '%sinterface-type', urn)
                    interface_name = self.get_node_value(
                        intf, '%sinterface-name', urn)
                    tag = self.get_node_value(intf, '%stag', urn)
                    port_results = {'interface-type': interface_type,
                                    'interface-name': interface_name,
                                    'tag': tag}
                    ports.append(port_results)
                results = {'interface-name': vlan_name,
                           'vlan-state': vlan_state,
                           'vlan-id': vlan_id,
                           'vlan-type': vlan_type,
                           'interface': ports}
                result.append(results)
        return result

    @staticmethod
    def get_vlan_brief_request(last_vlan_id):
        """ Creates a new Netconf request based on the last received
        vlan id when the hasMore flag is true
        """

        request_interface = ET.Element(
            'get-vlan-brief',
            xmlns="urn:brocade.com:mgmt:brocade-interface-ext"
        )
        if last_vlan_id != '':
            last_received_int_el = ET.SubElement(request_interface,
                                                 "last-rcvd-vlan-id")
            last_received_int_el.text = last_vlan_id
        return request_interface

    @property
    def switchport_list(self):
        """list[dict]:A list of dictionary items describing the details
            of list of dictionary items describing the details of switch
            port"""
        urn = "{urn:brocade.com:mgmt:brocade-interface-ext}"
        result = []
        request_interface = self.get_interface_switchport_request()
        interface_result = self._callback(request_interface, 'get')
        for interface in interface_result.findall('%sswitchport' % urn):
            vlans = []
            interface_type = self.get_node_value(interface, '%sinterface-type',
                                                 urn)
            interface_name = self.get_node_value(interface, '%sinterface-name',
                                                 urn)
            mode = self.get_node_value(interface, '%smode', urn)
            intf = interface.find('%sactive-vlans' % urn)
            for vlan_node in intf.findall('%svlanid' % urn):
                vlan = vlan_node.text
                vlans.append(vlan)
            results = {'vlan-id': vlans,
                       'mode': mode,
                       'interface-name': interface_name,
                       'interface_type': interface_type}
            result.append(results)
        return result

    @staticmethod
    def get_interface_switchport_request():
        """Creates a new Netconf request"""
        request_interface = ET.Element(
            'get-interface-switchport',
            xmlns="urn:brocade.com:mgmt:brocade-interface-ext"
        )
        return request_interface

    @property
    def port_channels(self):
        """list[dict]: A list of dictionary items of port channels.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.202']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.channel_group(name='226/0/1',
            ...         int_type='tengigabitethernet',
            ...         port_int='1', channel_type='standard', mode='active')
            ...         result = dev.interface.port_channels
            ...         is_port_channel_exist = False
            ...         for port_chann in result:
            ...             if port_chann['interface-name']=='port-channel-1':
            ...                 for interfaces in port_chann['interfaces']:
            ...                     for keys, values in interfaces.items():
            ...                         if '226/0/1' in values:
            ...                             is_port_channel_exist = True
            ...                             break
            ...         output = dev.interface.remove_port_channel(
            ...         port_int='1')
            ...         assert is_port_channel_exist
        """
        pc_urn = "{urn:brocade.com:mgmt:brocade-lag}"
        result = []
        has_more = ''
        last_aggregator_id = ''
        while (has_more == '') or (has_more == 'true'):
            request_port_channel = self.get_port_chann_detail_request(
                last_aggregator_id)
            port_channel_result = self._callback(request_port_channel, 'get')
            has_more = self.get_node_value(port_channel_result,
                                           '%shas-more', pc_urn)
            if has_more == 'true':
                for x in port_channel_result.findall('%slacp' % pc_urn):
                    last_aggregator_id = self.get_node_value(x,
                                                             '%saggregator-id',
                                                             pc_urn)

            for item in port_channel_result.findall('%slacp' % pc_urn):
                interface_list = []
                aggregator_id = self.get_node_value(
                    item, '%saggregator-id', pc_urn)
                aggregator_type = self.get_node_value(
                    item, '%saggregator-type', pc_urn)
                is_vlag = self.get_node_value(item, '%sisvlag', pc_urn)
                aggregator_mode = self.get_node_value(
                    item, '%saggregator-mode', pc_urn)
                system_priority = self.get_node_value(
                    item, '%ssystem-priority', pc_urn)
                actor_system_id = self.get_node_value(
                    item, '%sactor-system-id', pc_urn)
                partner_oper_priority = self.get_node_value(
                    item, '%spartner-oper-priority', pc_urn)
                partner_system_id = self.get_node_value(
                    item, '%spartner-system-id', pc_urn)
                admin_key = self.get_node_value(
                    item, '%sadmin-key', pc_urn)
                oper_key = self.get_node_value(item, '%soper-key', pc_urn)
                partner_oper_key = self.get_node_value(
                    item, '%spartner-oper-key', pc_urn)
                rx_link_count = self.get_node_value(
                    item, '%srx-link-count', pc_urn)
                tx_link_count = self.get_node_value(
                    item, '%stx-link-count', pc_urn)
                individual_agg = self.get_node_value(
                    item, '%sindividual-agg', pc_urn)
                ready_agg = self.get_node_value(
                    item, '%sready-agg', pc_urn)
                for item1 in item.findall('%saggr-member' % pc_urn):
                    rbridge_id = self.get_node_value(
                        item1, '%srbridge-id', pc_urn)
                    int_type = self.get_node_value(
                        item1, '%sinterface-type', pc_urn)
                    int_name = self.get_node_value(
                        item1, '%sinterface-name', pc_urn)
                    actor_port = self.get_node_value(
                        item1, '%sactor-port', pc_urn)
                    sync = self.get_node_value(item1, '%ssync',  pc_urn)
                    port_channel_interface = {'rbridge-id': rbridge_id,
                                              'interface-type': int_type,
                                              'interface-name': int_name,
                                              'actor_port': actor_port,
                                              'sync': sync}
                    interface_list.append(port_channel_interface)
                results = {'interface-name': 'port-channel-' + aggregator_id,
                           'interfaces': interface_list,
                           'aggregator_id': aggregator_id,
                           'aggregator_type': aggregator_type,
                           'is_vlag': is_vlag,
                           'aggregator_mode': aggregator_mode,
                           'system_priority': system_priority,
                           'actor_system_id': actor_system_id,
                           'partner-oper-priority': partner_oper_priority,
                           'partner-system-id': partner_system_id,
                           'admin-key': admin_key,
                           'oper-key': oper_key,
                           'partner-oper-key': partner_oper_key,
                           'rx-link-count': rx_link_count,
                           'tx-link-count': tx_link_count,
                           'individual-agg': individual_agg,
                           'ready-agg': ready_agg}

                result.append(results)
        return result

    @staticmethod
    def get_node_value(node, node_name, urn):
        value = node.find(node_name % urn)
        if value is not None:
            return value.text
        else:
            return ''

    @staticmethod
    def get_port_chann_detail_request(last_aggregator_id):
        """ Creates a new Netconf request based on the last received
        aggregator id when the hasMore flag is true
        """

        port_channel_ns = 'urn:brocade.com:mgmt:brocade-lag'
        request_port_channel = ET.Element('get-port-channel-detail',
                                          xmlns=port_channel_ns)

        if last_aggregator_id != '':
            last_received_port_chann_el = ET.SubElement(request_port_channel,
                                                        "last-aggregator-id")
            last_received_port_chann_el.text = last_aggregator_id
        return request_port_channel

    def bfd(self, **kwargs):
        raise NotImplementedError

    def vrrpe_spf_basic(self, **kwargs):
        """Set vrrpe short path forwarding to default.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            enable (bool): If vrrpe short path fowarding should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            vrid (str): vrrpe router ID.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid` is not passed.
            ValueError: if `int_type`, `name`, `vrid` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(ip_version='6',
            ...         enable=True, rbridge_id='225')
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89', vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrrpe_spf_basic(int_type='ve',
            ...         name='89', vrid='1', rbridge_id='1')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        vrrpe_args = dict(name=name, vrid=vrid)
        method_class = self._interface
        if get:
            enable = None
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        method_name = 'interface_%s_vrrpe_short_path_forwarding_basic' % \
                      int_type
        if int_type == 've':
            method_name = 'rbridge_id_%s' % method_name
            method_class = self._rbridge
            vrrpe_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')
        vrrpe_spf_basic = getattr(method_class, method_name)
        config = vrrpe_spf_basic(**vrrpe_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*short-path-forwarding').set('operation', 'delete')
        return callback(config)

    def vrrpe_vip(self, **kwargs):
        """Set vrrpe VIP.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): vrrpev3 ID.
            enable (bool): If vrrpe virtual IP should be enabled
                or disabled.Default:``True``.
            get (bool): Get config instead of editing config. (True, False)
            vip (str): IPv4/IPv6 Virtual IP Address.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vip` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vip` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(enable=True,
            ...         rbridge_id='225')
            ...         output = dev.interface.set_ip('tengigabitethernet',
            ...         '225/0/18', '10.1.1.2/24')
            ...         output = dev.interface.ip_address(name='225/0/18',
            ...         int_type='tengigabitethernet',
            ...         ip_addr='2001:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         dev.interface.vrrpe_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1', vip='10.1.1.1/24')
            ...         dev.interface.vrrpe_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vrrpe_vip(int_type='tengigabitethernet',
            ...         name='225/0/18', vrid='1',
            ...         vip='2001:4818:f000:1ab:cafe:beef:1000:1/64')
            ...         output = dev.interface.add_vlan_int('89')
            ...         output = dev.interface.ip_address(name='89',
            ...         int_type='ve', ip_addr='172.16.1.1/24',
            ...         rbridge_id='225')
            ...         output = dev.interface.ip_address(name='89',
            ...         int_type='ve', rbridge_id='225',
            ...         ip_addr='2002:4818:f000:1ab:cafe:beef:1000:2/64')
            ...         output = dev.services.vrrpe(ip_version='6',
            ...         enable=False, rbridge_id='225')
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         dev.interface.vrrpe_vip(int_type='ve', name='89',
            ...         vrid='1', vip='172.16.1.2/24', rbridge_id='225')
            ...         dev.interface.vrrpe_vip(int_type='ve', name='89',
            ...         vrid='1', vip='fe80::dafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         dev.interface.vrrpe_vip(int_type='ve', name='89',
            ...         vrid='1', vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        vip = kwargs.pop('vip')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        if get:
            enable = None
        ipaddress = ip_interface(unicode(vip))
        vrrpe_vip = None
        vrrpe_args = dict(name=name,
                          vrid=vrid,
                          virtual_ipaddr=str(ipaddress.ip))
        method_class = self._interface

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        if ipaddress.version == 4:
            vrrpe_args['version'] = '3'
            method_name = 'interface_%s_vrrpe_virtual_ip_virtual_' \
                          'ipaddr' % int_type
        elif ipaddress.version == 6:
            method_name = 'interface_%s_ipv6_vrrpv3e_group_virtual_ip_' \
                          'virtual_ipaddr' % int_type

        if int_type == 've':
            method_name = 'rbridge_id_%s' % method_name
            if ipaddress.version == 6:
                method_name = method_name.replace('group_', '')
            method_class = self._rbridge
            vrrpe_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')

        vrrpe_vip = getattr(method_class, method_name)
        config = vrrpe_vip(**vrrpe_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*virtual-ip').set('operation', 'delete')
        return callback(config)

    def vrrpe_vmac(self, **kwargs):
        """Set vrrpe virtual mac.
        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc).
            name (str): Name of interface. (1/0/5, 1/0/10, etc).
            vrid (str): vrrpev3 ID.
            enable (bool): If vrrpe virtual MAC should be enabled
                or disabled.Default:``True``.
            get (bool): Get config instead of editing config. (True, False)
            virtual_mac (str):Virtual mac-address in the format
            02e0.5200.00xx.
            rbridge_id (str): rbridge-id for device. Only required
            when type is 've'.
            callback (function): A function executed upon completion
            of the  method.  The only parameter passed to `callback`
            will be the ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `vrid`, or `vmac` is not passed.
            ValueError: if `int_type`, `name`, `vrid`, or `vmac` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrrpe_vip(int_type='ve',
            ...         name='89',vrid='1',
            ...         vip='2002:4818:f000:1ab:cafe:beef:1000:1/64',
            ...         rbridge_id='225')
            ...         output = dev.services.vrrpe(enable=False,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrrpe_vmac(int_type='ve',
            ...         name='89', vrid='1', rbridge_id='1',
            ...         virtual_mac='aaaa.bbbb.cccc')
        """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        vrid = kwargs.pop('vrid')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        virtual_mac = kwargs.pop('virtual_mac', '02e0.5200.00xx')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel', 've']
        if get:
            enable = None
        vrrpe_args = dict(name=name,
                          vrid=vrid,
                          virtual_mac=virtual_mac)
        method_class = self._interface

        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        method_name = 'interface_%s_vrrpe_virtual_mac' % int_type

        if int_type == 've':
            method_name = 'rbridge_id_%s' % method_name
            method_class = self._rbridge
            vrrpe_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        elif not pynos.utilities.valid_interface(int_type, name):
            raise ValueError('`name` must be in the format of x/y/z for '
                             'physical interfaces or x for port channel.')
        vrrpe_vmac = getattr(method_class, method_name)
        config = vrrpe_vmac(**vrrpe_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*virtual-mac').set('operation', 'delete')
        return callback(config)

    @property
    def ve_interfaces(self):
        """list[dict]: A list of dictionary items describing the operational
        state of ve interfaces along with the ip address associations.
        """
        urn = "{urn:brocade.com:mgmt:brocade-interface-ext}"
        int_ns = 'urn:brocade.com:mgmt:brocade-interface-ext'

        ip_result = []
        request_interface = ET.Element('get-ip-interface', xmlns=int_ns)
        interface_result = self._callback(request_interface, 'get')
        for interface in interface_result.findall('%sinterface' % urn):
            int_type = interface.find('%sinterface-type' % urn).text
            int_name = interface.find('%sinterface-name' % urn).text
            int_state = interface.find('%sif-state' % urn).text
            int_proto_state = interface.find('%sline-protocol-state' %
                                             urn).text
            ip_address = interface.find('.//%sipv4' % urn).text
            if_name = interface.find('%sif-name' % urn).text
            results = {'interface-type': int_type,
                       'interface-name': int_name,
                       'if-name': if_name,
                       'interface-state': int_state,
                       'interface-proto-state': int_proto_state,
                       'ip-address': ip_address}
            ip_result.append(results)
        return ip_result
