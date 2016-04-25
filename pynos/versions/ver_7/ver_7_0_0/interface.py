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
from pynos.versions.ver_7.ver_7_0_0.yang.brocade_interface \
    import brocade_interface as brcd_intf
from pynos.versions.ver_7.ver_7_0_0.yang.brocade_rbridge \
    import brocade_rbridge as brcd_rbridge
import pynos.utilities
from pynos.versions.base.interface import Interface as InterfaceBase


class Interface(InterfaceBase):
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a NOS device.

    Attributes:
        None
    """
    def __init__(self, callback):
        super(Interface, self).__init__(callback)
        self._interface = brcd_intf(callback=pynos.utilities.return_xml)
        self._rbridge = brcd_rbridge(callback=pynos.utilities.return_xml)

    def ip_unnumbered(self, **kwargs):
        """Configure an unnumbered interface.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            name (str): Name of interface id.
                 (For interface: 1/0/5, 1/0/10 etc).
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            donor_type (str): Interface type of the donor interface.
            donor_name (str): Interface name of the donor interface.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `int_type`, `name`, `donor_type`, or `donor_name` is
                not passed.
            ValueError: if `int_type`, `name`, `donor_type`, or `donor_name`
                are invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='1', ip_addr='4.4.4.4/32', rbridge_id='230')
            ...        int_type = 'tengigabitethernet'
            ...        name = '230/0/20'
            ...        donor_type = 'loopback'
            ...        donor_name = '1'
            ...        output = dev.interface.disable_switchport(inter_type=
            ...        int_type, inter=name)
            ...        output = dev.interface.ip_unnumbered(int_type=int_type,
            ...        name=name, donor_type=donor_type, donor_name=donor_name)
            ...        output = dev.interface.ip_unnumbered(int_type=int_type,
            ...        name=name, donor_type=donor_type, donor_name=donor_name,
            ...        get=True)
            ...        output = dev.interface.ip_unnumbered(int_type=int_type,
            ...        name=name, donor_type=donor_type, donor_name=donor_name,
            ...        delete=True)
            ...        output = dev.interface.ip_address(int_type='loopback',
            ...        name='1', ip_addr='4.4.4.4/32', rbridge_id='230',
            ...        delete=True)
            ...        output = dev.interface.ip_unnumbered(int_type='hodor',
            ...        donor_name=donor_name, donor_type=donor_type, name=name)
            ...        # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            ValueError
        """
        kwargs['ip_donor_interface_name'] = kwargs.pop('donor_name')
        kwargs['ip_donor_interface_type'] = kwargs.pop('donor_type')
        kwargs['delete'] = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet']
        if kwargs['int_type'] not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))
        unnumbered_type = self._ip_unnumbered_type(**kwargs)
        unnumbered_name = self._ip_unnumbered_name(**kwargs)
        if kwargs.pop('get', False):
            return self._get_ip_unnumbered(unnumbered_type, unnumbered_name)
        config = pynos.utilities.merge_xml(unnumbered_type, unnumbered_name)
        return callback(config)

    def _ip_unnumbered_name(self, **kwargs):
        """Return the `ip unnumbered` donor name XML.

        You should not use this method.
        You probably want `Interface.ip_unnumbered`.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            delete (bool): Remove the configuration if ``True``.
            ip_donor_interface_name (str): The donor interface name (1, 2, etc)

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """

        method_name = 'interface_%s_ip_ip_config_unnumbered_ip_donor_'\
            'interface_name' % kwargs['int_type']
        ip_unnumbered_name = getattr(self._interface, method_name)
        config = ip_unnumbered_name(**kwargs)
        if kwargs['delete']:
            tag = 'ip-donor-interface-name'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _ip_unnumbered_type(self, **kwargs):
        """Return the `ip unnumbered` donor type XML.

        You should not use this method.
        You probably want `Interface.ip_unnumbered`.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
            delete (bool): Remove the configuration if ``True``.
            ip_donor_interface_type (str): The donor interface type (loopback)

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'interface_%s_ip_ip_config_unnumbered_ip_donor_'\
            'interface_type' % kwargs['int_type']
        ip_unnumbered_type = getattr(self._interface, method_name)
        config = ip_unnumbered_type(**kwargs)
        if kwargs['delete']:
            tag = 'ip-donor-interface-type'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _get_ip_unnumbered(self, unnumbered_type, unnumbered_name):
        """Get and merge the `ip unnumbered` config from an interface.

        You should not use this method.
        You probably want `Interface.ip_unnumbered`.

        Args:
            unnumbered_type: XML document with the XML to get the donor type.
            unnumbered_name: XML document with the XML to get the donor name.

        Returns:
            Merged XML document.

        Raises:
            None
        """
        unnumbered_type = self._callback(unnumbered_type, handler='get_config')
        unnumbered_name = self._callback(unnumbered_name, handler='get_config')
        unnumbered_type = pynos.utilities.return_xml(str(unnumbered_type))
        unnumbered_name = pynos.utilities.return_xml(str(unnumbered_name))
        return pynos.utilities.merge_xml(unnumbered_type, unnumbered_name)

    def anycast_mac(self, **kwargs):
        """Configure an anycast MAC address.

        Args:
            int_type (str): Type of interface. (gigabitethernet,
                 tengigabitethernet etc).
             mac (str): MAC address to configure
                 (example: '0011.2233.4455').
            delete (bool): True is the IP address is added and False if its to
                be deleted (True, False). Default value will be False if not
                specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `mac` is not passed.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.services.vrrp(ip_version='6',
            ...        enabled=True, rbridge_id='230')
            ...        output = dev.services.vrrp(enabled=True,
            ...        rbridge_id='230')
            ...        output = dev.services.vrrp(ip_version='6',
            ...        enabled=False, rbridge_id='230')
            ...        output = dev.services.vrrp(enabled=False,
            ...        rbridge_id='230')
            ...        output = dev.interface.anycast_mac(rbridge_id='230',
            ...        mac='0011.2233.4455')
            ...        output = dev.interface.anycast_mac(rbridge_id='230',
            ...        mac='0011.2233.4455', get=True)
            ...        output = dev.interface.anycast_mac(rbridge_id='230',
            ...        mac='0011.2233.4455', delete=True)
            ...        output = dev.services.vrrp(ip_version='6', enabled=True,
            ...        rbridge_id='230')
            ...        output = dev.services.vrrp(enabled=True,
            ...        rbridge_id='230')
        """
        callback = kwargs.pop('callback', self._callback)
        anycast_mac = getattr(self._rbridge, 'rbridge_id_ip_static_ag_ip_'
                              'config_anycast_gateway_mac_ip_anycast_'
                              'gateway_mac')
        config = anycast_mac(rbridge_id=kwargs.pop('rbridge_id', '1'),
                             ip_anycast_gateway_mac=kwargs.pop('mac'))
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            config.find('.//*anycast-gateway-mac').set('operation', 'delete')
        return callback(config)
