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
import re

from pynos.versions.base.yang.brocade_interface import brocade_interface
from pynos.versions.base.yang.brocade_rbridge import brocade_rbridge
import pynos.utilities


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
            KeyError: if `int_type`, `name`, or `description` is not specified.
            ValueError: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.description(
            ... int_type='tengigabitethernet',
            ... name='225/0/38',
            ... desc='test')
            >>> dev.interface.description() # doctest: +IGNORE_EXCEPTION_DETAIL
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
            raise ValueError("%s must be one of: %s" %
                             repr(int_type), repr(int_types))

        desc_args = dict(name=name, description=desc)

        if int_type == "vlan":
            if re.search('^[0-9]{1,4}$', name) is None:
                raise ValueError("%s must be between `1` and `4096`" %
                                 repr(name))

            config = self._interface.interface_vlan_interface_vlan_description(
                **desc_args
                )
        else:
            if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
                raise ValueError("%s must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                                 "{1,3}$`" % repr(name))

            config = getattr(
                self._interface,
                'interface_%s_description' % int_type
                )(**desc_args)
        return callback(config)

    def private_vlan_type(self, **kwargs):
        """Set the PVLAN type (primary, isolated, community).

        Args:
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            pvlan_type (str): PVLAN type (primary, isolated, community)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan` is not
                specified.
            AttributeError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan`
                are invalid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> name = '90'
            >>> pvlan_type = 'isolated'
            >>> output = dev.interface.private_vlan_type(name=name,
            ... pvlan_type=pvlan_type)
            >>> dev.interface.private_vlan_type()
            ... # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = kwargs.pop('name')
        pvlan_type = kwargs.pop('pvlan_type')
        callback = kwargs.pop('callback', self._callback)
        allowed_pvlan_types = ['isolated', 'primary', 'community']

        if re.search('^[0-9]{1,4}$', name) is None:
            raise ValueError("Incorrect name value.")

        if pvlan_type not in allowed_pvlan_types:
            raise ValueError("Incorrect pvlan_type")

        pvlan_args = dict(name=name, pvlan_type_leaf=pvlan_type)
        config = self._interface.interface_vlan_interface_vlan_private_vlan_pvlan_type_leaf(**pvlan_args)
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
            AttributeError: if `name` or `sec_vlan` are invalid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> int_type = 'tengigabitethernet'
            >>> name = '20'
            >>> sec_vlan = '30'
            >>> output = dev.interface.private_vlan_type(name=name,
            ... pvlan_type='primary')
            >>> output = dev.interface.private_vlan_type(name=sec_vlan,
            ... pvlan_type='isolated')
            >>> output = dev.interface.vlan_pvlan_association_add(name=name,
            ... sec_vlan=sec_vlan)
            >>> dev.interface.vlan_pvlan_association_add()
            ... # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = kwargs.pop('name')
        sec_vlan = kwargs.pop('sec_vlan')
        callback = kwargs.pop('callback', self._callback)

        if re.search('^[0-9]{1,4}$', name) is None:
            raise ValueError("Incorrect name value.")

        pvlan_args = dict(name=name, sec_assoc_add=sec_vlan)
        config = self._interface.interface_vlan_interface_vlan_private_vlan_association_sec_assoc_add(**pvlan_args)
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
            AttributeError: if `int_type`, `name`, `pri_vlan`, or `sec_vlan`
                are invalid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/38'
            >>> pri_vlan = '75'
            >>> sec_vlan = '100'
            >>> output = dev.interface.private_vlan_type(name=pri_vlan,
            ... pvlan_type='primary')
            >>> output = dev.interface.private_vlan_type(name=sec_vlan,
            ... pvlan_type='isolated')
            >>> output = dev.interface.vlan_pvlan_association_add(
            ... name=pri_vlan, sec_vlan=sec_vlan)
            >>> output = dev.interface.enable_switchport(int_type, name)
            >>> output = dev.interface.private_vlan_mode(
            ... int_type=int_type, name=name, mode='host')
            >>> output = dev.interface.pvlan_host_association(
            ... int_type=int_type, name=name, pri_vlan=pri_vlan,
            ... sec_vlan=sec_vlan)
            >>> dev.interface.pvlan_host_association()
            ... # doctest: +IGNORE_EXCEPTION_DETAIL
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

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
            raise ValueError("Incorrect name value.")

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
            state (str): The administrative state of the interface (up, down).
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `state` is not passed.
            ValueError: if `int_type`, `name`, or `state` are invalid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> dev.interface.admin_state(int_type='tengigabitethernet',
            ... name='225/0/38', state='down')
            >>> dev.interface.admin_state(int_type='tengigabitethernet',
            ... name='225/0/38', state='up')
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        state = kwargs.pop('state').lower()
        callback = kwargs.pop('callback', self._callback)
        valid_states = ['up', 'down']
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet',
                           'port_channel']

        if int_type not in valid_int_types:
            raise ValueError('%s must be one of: %s' %
                             repr(int_type), repr(valid_int_types))

        if state not in valid_states:
            raise ValueError('%s must be `up` or `down`.' % repr(state))

        if re.search(r'^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
            raise ValueError('%s must be in the format of x/y/z.')

        state_args = dict(name=name)
        admin_state = getattr(self._interface,
                              'interface_%s_shutdown' % int_type)
        config = admin_state(**state_args)
        if state == 'up':
            shutdown = config.find('.//*shutdown')
            shutdown.set('operation', 'delete')
        try:
            return callback(config)
        # TODO: Catch existing 'no shut'
        # This is in place because if the interface is already admin up,
        # `ncclient` will raise an error if you try to admin up the interface
        # again.
        except AttributeError as (errno, errstr):
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
            AttributeError: if `int_type`, `name`, or `mode` are invalid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> int_type = 'tengigabitethernet'
            >>> name = '225/0/38'
            >>> output = dev.interface.enable_switchport(int_type, name)
            >>> output = dev.interface.private_vlan_mode(
            ... int_type=int_type, name=name, mode='trunk_host')
            >>> dev.interface.private_vlan_mode()
            ... # doctest: +IGNORE_EXCEPTION_DETAIL
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

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
            raise ValueError("Incorrect name value.")

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
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            mode (str): Trunk port mode (trunk, trunk-no-default-native).
            state (str): Enabled or disabled.
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
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.trunk_mode(
            ... int_type='tengigabitethernet',
            ... name='225/0/38',
            ... mode='trunk')
            >>> output = dev.interface.tag_native_vlan(
            ... int_type='tengigabitethernet',
            ... name='225/0/38')
            >>> output = dev.interface.tag_native_vlan(
            ... int_type='tengigabitethernet',
            ... name='225/0/38',
            ... state='disabled')
            >>> dev.interface.tag_native_vlan()
            ... # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        state = kwargs.pop('state', 'enabled').lower()
        callback = kwargs.pop('callback', self._callback)

        int_types = ['gigabitethernet', 'tengigabitethernet',
                     'fortygigabitethernet', 'hundredgigabitethernet',
                     'port_channel']

        if int_type not in int_types:
            raise ValueError("Incorrect int_type value.")

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
            raise ValueError("Incorrect name value.")

        valid_states = ['enabled', 'disabled']
        if state not in valid_states:
            raise ValueError("Invalid state.")

        tag_args = dict(name=name)
        tag_native_vlan = getattr(self._interface, 'interface_%s_switchport_'
                                  'trunk_tag_native_vlan' % int_type)
        config = tag_native_vlan(**tag_args)
        if state == 'disabled':
            untag = config.find('.//*native-vlan')
            untag.set('operation', 'delete')

        try:
            return callback(config)
        # TODO: Catch existing 'no switchport tag native-vlan'
        except AttributeError as (errno, errstr):
            return None

    def switchport_pvlan_mapping(self, **kwargs):
        """Switchport private VLAN mapping.

        Args:

        Returns:

        Raises:

        Examples:
        """
        pass

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

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.mtu(
            ... int_type='tengigabitethernet',
            ... name='225/0/38',
            ... mtu='1666')
            >>> dev.interface.mtu() # doctest: +IGNORE_EXCEPTION_DETAIL
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

        valid_mtu = range(1522, 9216)
        if int(mtu) not in valid_mtu:
            raise ValueError("Incorrect mtu value 1522-9216")

        mtu_args = dict(name=name, mtu=mtu)

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
                raise ValueError("Incorrect name value.")

        config = getattr(
            self._interface,
            'interface_%s_mtu' % int_type
            )(**mtu_args)
        return callback(config)

    def fabric_isl(self, **kwargs):
        """Set fabric ISL state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            state (str): State to set Fabric ISL to. (up, down)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `description` is not specified.
            ValueError: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.fabric_isl(
            ... int_type='tengigabitethernet',
            ... name='225/0/40',
            ... state='down')
            >>> dev.interface.fabric_isl() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        state = str(kwargs.pop('state'))
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
            ]

        if int_type not in int_types:
            raise ValueError("%s must be one of: %s" %
                             repr(int_type), repr(int_types))

        valid_states = ['up', 'down']
        if state not in valid_states:
            raise ValueError("%s must be one of: %s" %
                             repr(state), repr(valid_states))

        fabric_isl_args = dict(name=name)

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
            raise ValueError("%s must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                             "{1,3}$`" % repr(name))

        config = getattr(
            self._interface,
            'interface_%s_fabric_fabric_isl_fabric_isl_enable' % int_type
            )(**fabric_isl_args)

        if state == "down":
            fabric_isl = config.find('.//*fabric-isl')
            fabric_isl.set('operation', 'delete')

        return callback(config)

    def fabric_trunk(self, **kwargs):
        """Set fabric trunk state.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                tengigabitethernet, etc)
            name (str): Name of interface. (1/0/5, 1/0/10, etc)
            state (str): State to set Fabric ISL to. (up, down)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, or `description` is not specified.
            ValueError: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.fabric_trunk(
            ... int_type='tengigabitethernet',
            ... name='225/0/40',
            ... state='down')
            >>> dev.interface.fabric_trunk() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        int_type = str(kwargs.pop('int_type').lower())
        name = str(kwargs.pop('name'))
        state = str(kwargs.pop('state'))
        callback = kwargs.pop('callback', self._callback)

        int_types = [
            'gigabitethernet',
            'tengigabitethernet',
            'fortygigabitethernet',
            'hundredgigabitethernet'
            ]

        if int_type not in int_types:
            raise ValueError("%s must be one of: %s" %
                             repr(int_type), repr(int_types))

        valid_states = ['up', 'down']
        if state not in valid_states:
            raise ValueError("%s must be one of: %s" %
                             repr(state), repr(valid_states))

        fabric_trunk_args = dict(name=name)

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
            raise ValueError("%s must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                             "{1,3}$`" % repr(name))

        config = getattr(
            self._interface,
            'interface_%s_fabric_fabric_trunk_fabric_trunk_enable' % int_type
            )(**fabric_trunk_args)

        if state == "down":
            fabric_trunk = config.find('.//*fabric-trunk')
            fabric_trunk.set('operation', 'delete')

        return callback(config)

    def v6_nd_suppress_ra(self, **kwargs):
        """Set interface description.

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
            KeyError: if `int_type`, `name`, or `description` is not specified.
            ValueError: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.v6_nd_suppress_ra(
            ... int_type='ve',
            ... name='10',
            ... rbridge_id='225')
            >>> dev.interface.v6_nd_suppress_ra() # doctest: +IGNORE_EXCEPTION_DETAIL
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
            raise ValueError("%s must be one of: %s" %
                             repr(int_type), repr(int_types))

        if int_type == "ve":
            if re.search('^[0-9]{1,4}$', name) is None:
                raise ValueError("%s must be between `1` and `8191`" %
                                 repr(name))

            rbridge_id = kwargs.pop('rbridge_id', "1")

            nd_suppress_args = dict(name=name, rbridge_id=rbridge_id)
            config = self._rbridge.rbridge_id_interface_ve_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_suppress_ra_suppress_ra_all(
                **nd_suppress_args
                )
        else:
            if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
                raise ValueError("%s must match `^[0-9]{1,3}/[0-9]{1,3}/[0-9]"
                                 "{1,3}$`" % repr(name))

            nd_suppress_args = dict(name=name)
            config = getattr(
                self._interface,
                'interface_%s_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_suppress_ra_suppress_ra_all' % int_type
                )(**nd_suppress_args)
        return callback(config)

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
            KeyError: if `int_type`, `name`, or `description` is not specified.
            ValueError: if `name` or `int_type` are not valid values.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.port_channel_minimum_links(
            ... name='1',
            ... minimum_links='2')
            >>> dev.interface.port_channel_minimum_links() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        name = str(kwargs.pop('name'))
        minimum_links = str(kwargs.pop('minimum_links'))
        callback = kwargs.pop('callback', self._callback)

        min_links_args = dict(name=name, minimum_links=minimum_links)

        if re.search('^[0-9]{1,3}$', name) is None:
            raise ValueError("%s must match `^[0-9]{1,3}$"
                             "{1,3}$`" % repr(name))

        config = getattr(
            self._interface,
            'interface_port_channel_minimum_links'
            )(**min_links_args)

        return callback(config)

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
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.trunk_mode(
            ... int_type='tengigabitethernet',
            ... name='225/0/38',
            ... mode='trunk')
            >>> dev.interface.trunk_mode() # doctest: +IGNORE_EXCEPTION_DETAIL
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

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
                raise ValueError("Incorrect name value.")

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
            KeyError: if `vlan`, or `service_id` is not specified.
            AttributeError: if `vlan`, or `service_id` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> vlan = '6666'
            >>> service_id = '1'
            >>> output = dev.interface.transport_service(vlan=vlan,
            ... service_id=service_id)
            >>> dev.interface.transport_service()
            ... # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        vlan = kwargs.pop('vlan')
        service_id = kwargs.pop('service_id')
        callback = kwargs.pop('callback', self._callback)

        if re.search('^[0-9]{1,4}$', vlan) is None:
            raise ValueError("Incorrect vlan value.")

        service_args = dict(name=vlan, transport_service=service_id)
        config = self._interface.interface_vlan_interface_vlan_transport_service(**service_args)
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
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.interface.lacp_timeout(
            ... int_type='tengigabitethernet',
            ... name='225/0/38',
            ... timeout='long')
            >>> dev.interface.lacp_timeout() # doctest: +IGNORE_EXCEPTION_DETAIL
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

        if re.search('^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is None:
                raise ValueError("Incorrect name value.")

        config = getattr(
                self._interface,
                'interface_%s_lacp_timeout' % int_type
                )(**timeout_args)
        return callback(config)
