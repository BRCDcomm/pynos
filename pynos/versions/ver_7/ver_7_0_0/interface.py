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
from pynos.versions.ver_7.ver_7_0_0.yang.brocade_mac_address_table \
    import brocade_mac_address_table
from pynos.exceptions import InvalidVlanId
from ipaddress import ip_interface
import xml.etree.ElementTree as ET


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
        self._mac_address_table = brocade_mac_address_table(
            callback=pynos.utilities.return_xml
        )

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

    def bfd(self, **kwargs):
        """Configure BFD for Interface.

        Args:
            name (str): name of the interface to configure (230/0/1 etc)
            int_type (str): interface type (gigabitethernet etc)
            tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            rx (str): BFD receive interval in milliseconds (300, 500, etc)
            multiplier (str): BFD multiplier.  (3, 7, 5, etc)
            delete (bool): True if BFD configuration should be deleted.
                Default value will be False if not specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `tx`, `rx`, or `multiplier` is not passed.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.interface.bfd(name='230/0/4', rx='300',
            ...        tx='300', multiplier='3', int_type='tengigabitethernet')
            ...        output = dev.interface.bfd(name='230/0/4', rx='300',
            ...        tx='300', multiplier='3',
            ...        int_type='tengigabitethernet', get=True)
            ...        output = dev.interface.bfd(name='230/0/4', rx='300',
            ...        tx='300', multiplier='3',
            ...        int_type='tengigabitethernet', delete=True)
        """
        int_type = str(kwargs.pop('int_type').lower())
        kwargs['name'] = str(kwargs.pop('name'))
        kwargs['min_tx'] = kwargs.pop('tx')
        kwargs['min_rx'] = kwargs.pop('rx')
        kwargs['delete'] = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['gigabitethernet', 'tengigabitethernet',
                           'fortygigabitethernet', 'hundredgigabitethernet']

        if int_type not in valid_int_types:
            raise ValueError('int_type must be one of: %s' %
                             repr(valid_int_types))
        kwargs['int_type'] = int_type

        bfd_tx = self._bfd_tx(**kwargs)
        bfd_rx = self._bfd_rx(**kwargs)
        bfd_multiplier = self._bfd_multiplier(**kwargs)
        if kwargs.pop('get', False):
            return self._get_bfd(bfd_tx, bfd_rx, bfd_multiplier)
        config = pynos.utilities.merge_xml(bfd_tx, bfd_rx)
        config = pynos.utilities.merge_xml(config, bfd_multiplier)
        return callback(config)

    def _bfd_tx(self, **kwargs):
        """Return the BFD minimum transmit interval XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            min_tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        int_type = kwargs['int_type']
        method_name = 'interface_%s_bfd_interval_min_tx' % int_type
        bfd_tx = getattr(self._interface, method_name)
        config = bfd_tx(**kwargs)
        if kwargs['delete']:
            tag = 'min-tx'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _bfd_rx(self, **kwargs):
        """Return the BFD minimum receive interval XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            min_rx (str): BFD receive interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        int_type = kwargs['int_type']
        method_name = 'interface_%s_bfd_interval_min_rx' % int_type
        bfd_rx = getattr(self._interface, method_name)
        config = bfd_rx(**kwargs)
        if kwargs['delete']:
            tag = 'min-rx'
            config.find('.//*%s' % tag).set('operation', 'delete')
            pass
        return config

    def _bfd_multiplier(self, **kwargs):
        """Return the BFD multiplier XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            min_tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        int_type = kwargs['int_type']
        method_name = 'interface_%s_bfd_interval_multiplier' % int_type
        bfd_multiplier = getattr(self._interface, method_name)
        config = bfd_multiplier(**kwargs)
        if kwargs['delete']:
            tag = 'multiplier'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _get_bfd(self, tx, rx, multiplier):
        """Get and merge the `bfd` config from global BGP.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            tx: XML document with the XML to get the transmit interval.
            rx: XML document with the XML to get the receive interval.
            multiplier: XML document with the XML to get the interval
                multiplier.

        Returns:
            Merged XML document.

        Raises:
            None
        """
        tx = self._callback(tx, handler='get_config')
        rx = self._callback(rx, handler='get_config')
        multiplier = self._callback(multiplier, handler='get_config')
        tx = pynos.utilities.return_xml(str(tx))
        rx = pynos.utilities.return_xml(str(rx))
        multiplier = pynos.utilities.return_xml(str(multiplier))
        config = pynos.utilities.merge_xml(tx, rx)
        return pynos.utilities.merge_xml(config, multiplier)

    def vrf(self, **kwargs):
        """Create a vrf.
        Args:
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): False, the vrf is created and True if its to
                be deleted (True, False). Default value will be False if not
                specified.
            rbridge_id (str): rbridge-id for device.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name` is not passed.
            ValueError: if `rbridge_id`, `vrf_name` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf(vrf_name=vrf1,
            ...         rbridge_id='225')
            ...         output = dev.interface.vrf(rbridge_id='225',
            ...         get=True)
            ...         output = dev.interface.vrf(vrf_name=vrf1,
            ...         rbridge_id='225',delete=True)

        """
        rbridge_id = kwargs['rbridge_id']
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []
        method_class = self._rbridge
        method_name = 'rbridge_id_vrf_vrf_name'
        vrf = getattr(method_class, method_name)

        if not get_config:
            vrf_name = kwargs['vrf_name']
            vrf_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name)
            config = vrf(**vrf_args)

            if delete:
                config.find('.//*vrf').set('operation', 'delete')
            result = callback(config)

        elif get_config:
            vrf_args = dict(rbridge_id=rbridge_id, vrf_name='')
            config = vrf(**vrf_args)
            output = callback(config, handler='get_config')
            for item in output.data.findall('.//{*}vrf'):
                vrfname = item.find('.//{*}vrf-name').text
                tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrfname}
                result.append(tmp)
        return result

    def vrf_route_distiniguisher(self, **kwargs):
        """Configure Route distiniguisher.
        Args:
            rbridge_id (str): rbridge-id for device.
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            rd (str): Route distiniguisher <ASN:nn or IP-address:nn>
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): False, the vrf rd is configured and True if its to
                be deleted (True, False). Default value will be False if not
                specified.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name`, 'rd' is not passed.
            ValueError: if `rbridge_id`, `vrf_name`, 'rd' is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         vrf_name=vrf1, rbridge_id='2', rd='10.0.1.1:101')
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         vrf_name=vrf1, rbridge_id='2', rd='100:101')
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         rbridge_id='2', get=True)
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         rbridge_id='2', vrf_name='vrf2', get=True)
            ...         output = dev.interface.vrf_route_distiniguisher(
            ...         vrf_name=vrf1, rbridge_id='2', rd='100:101',
            ...         delete=True)

        """
        rbridge_id = kwargs['rbridge_id']
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        method_class = self._rbridge
        method_name = 'rbridge_id_vrf_route_distiniguisher'
        vrf_rd = getattr(method_class, method_name)

        if not get_config:
            vrf_name = kwargs['vrf_name']
            rd = kwargs['rd']
            rd_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name,
                           route_distiniguisher=rd)
            config = vrf_rd(**rd_args)

            if delete:
                config.find('.//*route-distiniguisher').set('operation',
                                                            'delete')
            result = callback(config)

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')
            rd_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name,
                           route_distiniguisher='')
            config = vrf_rd(**rd_args)
            output = callback(config, handler='get_config')
            for item in output.data.findall('.//{*}vrf'):
                vrfname = item.find('.//{*}vrf-name').text
                if item.find('.//{*}route-distiniguisher') is not None:
                    vrfrd = item.find('.//{*}route-distiniguisher').text
                else:
                    vrfrd = ''

                tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrfname,
                       'rd': vrfrd}
                result.append(tmp)
        return result

    def vrf_l3vni(self, **kwargs):
        """Configure Layer3 vni under vrf.
        Args:
            rbridge_id (str): rbridge-id for device.
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            l3vni (str): <NUMBER:1-16777215>   Layer 3 VNI.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): False the L3 vni is configured and True if its to
                be deleted (True, False). Default value will be False if not
                specified.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name`, 'l3vni' is not passed.
            ValueError: if `rbridge_id`, `vrf_name`, 'l3vni'  is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf_vni(
            ...         vrf_name=vrf1, rbridge_id='2', l3vni ='7201')
            ...         output = dev.interface.vrf_vni(rbridge_id='2',
            ...         get=True)
            ...         output = dev.interface.vrf_vni(rbridge_id='2',
            ...         , vrf_name='vrf2' get=True)
            ...         output = dev.interface.vrf_vni(vrf_name=vrf1,
            ...         rbridge_id='2', l3vni ='7201', delete=True)

        """
        rbridge_id = kwargs['rbridge_id']
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        method_class = self._rbridge
        method_name = 'rbridge_id_vrf_vni'
        vrf_vni = getattr(method_class, method_name)

        if not get_config:
            vrf_name = kwargs['vrf_name']
            l3vni = kwargs['l3vni']
            vni_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name,
                            vni=l3vni)
            config = vrf_vni(**vni_args)

            if delete:
                config.find('.//*vni').set('operation', 'delete')
            result = callback(config)

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')
            vni_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name,
                            vni='')
            config = vrf_vni(**vni_args)
            output = callback(config, handler='get_config')
            for item in output.data.findall('.//{*}vrf'):
                vrfname = item.find('.//{*}vrf-name').text
                if item.find('.//{*}vni') is not None:
                    vrfvni = item.find('.//{*}vni').text
                else:
                    vrfvni = ''

                tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrfname,
                       'l3vni': vrfvni}
                result.append(tmp)
        return result

    def vrf_afi_rt_evpn(self, **kwargs):
        """Configure Target VPN Extended Communities
        Args:
            rbridge_id (str): rbridge-id for device.
            vrf_name (str): Name of the vrf (vrf101, vrf-1 etc).
            rt (str): Route Target(import/export/both).
            rt_value (str): Route Target Value  ASN:nn Target
                            VPN Extended Community.
            afi (str): Address family (ip/ipv6).
            get (bool): Get config instead of editing config.
                        List all the details of
                        all afi under all vrf(True, False)
            delete_rt (bool): True to delete the route-target under
                              address family (True, False).
                              Default value will be False if not
                              specified.
            delete_afi (bool): True to delet the ip/ipv6 address family
                Default value will be False if not specified.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id`,`vrf_name`, 'afi', 'rt', 'rt_value'
                      is not passed.
            ValueError: if `rbridge_id`, `vrf_name`, 'afi', 'rt', rt_value
                        is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", rt='import', rt_value='101:101',
            ...         vrf_name="vrf1")
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", rt='import', rt_value='101:101',
            ...         vrf_name="vrf1",delete_rt=True)
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", rt='import', rt_value='101:101',
            ...         vrf_name="vrf1",delete_afi=True)
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", get=True)
            ...         output = dev.interface.vrf_vni(rbridge_id="1",
            ...         afi="ip", vrf_name="vrf2", get=True)

        """
        rbridge_id = kwargs['rbridge_id']
        afi = kwargs['afi']
        get_config = kwargs.pop('get', False)
        delete_rt = kwargs.pop('delete_rt', False)
        delete_afi = kwargs.pop('delete_afi', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        method_class = self._rbridge
        method_name = 'rbridge_id_vrf_address_family_%s_unicast_' \
                      'route_target_evpn' % afi
        vrf_rt = getattr(method_class, method_name)

        if not get_config:
            vrf_name = kwargs['vrf_name']
            rt = kwargs['rt']
            rt_value = kwargs['rt_value']
            rt_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name,
                           action=rt, target_community=rt_value)
            config = vrf_rt(**rt_args)

            if delete_afi is True:
                if config.find('.//*ipv6') is not None:
                    config.find('.//*ipv6').set('operation', 'delete')
                if config.find('.//*ip') is not None:
                    config.find('.//*ip').set('operation', 'delete')
            if delete_rt is True:
                config.find('.//*route-target').set('operation', 'delete')
            result = callback(config)

        elif get_config:
            vrf_name = kwargs.pop('vrf_name', '')

            rt_args = dict(rbridge_id=rbridge_id, vrf_name=vrf_name,
                           action='', target_community='')
            config = vrf_rt(**rt_args)
            output = callback(config, handler='get_config')
            for vrf_node in output.data.findall('.//{*}vrf'):
                afi = ''
                vrfrt = []
                vrfrtval = []
                vrfname = vrf_node.find('.//{*}vrf-name').text
                if vrf_node.find('.//{*}ip') is not None:
                    afi = "ip"
                    if vrf_node.find('.//{*}route-target') is not None:
                        for ipv4_action in vrf_node.findall('.//{*}action'):
                            rttemp = ipv4_action.text
                            vrfrt.append(rttemp)
                        for ipv4_rt in vrf_node.findall('.//{'
                                                        '*}target-community'):
                            valtemp = ipv4_rt.text
                            vrfrtval.append(valtemp)
                if vrf_node.find('.//{*}ipv6') is not None:
                    afi = "ipv6"
                    if vrf_node.find('.//{*}route-target') is not None:
                        for ipv6_action in vrf_node.findall('.//{*}action'):
                            rttemp = ipv6_action.text
                            vrfrt.append(rttemp)
                        for ipv6_rt in vrf_node.findall('.//{'
                                                        '*}target-community'):
                            valtemp = ipv6_rt.text
                            vrfrtval.append(valtemp)

                tmp = {'rbridge_id': rbridge_id, 'vrf_name': vrfname,
                       'afi': afi, 'rt': vrfrt, 'rtvalue': vrfrtval}
                result.append(tmp)

        return result

    def conversational_arp(self, **kwargs):
        """Enable conversational arp learning on VDX switches

        Args:
            rbridge_id (str): rbridge-id for device.
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the conversation arp learning.
                          (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `rbridge_id` is not passed.
            ValueError: if `rbridge_id` is invalid.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.conversational_arp(rbridge_id="1")
            ...     output = dev.interface.conversational_arp(rbridge_id="1",
                             get=True)
            ...     output = dev.interface.conversational_arp(rbridge_id="1",
                             delete=True)
        """

        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        arp_config = getattr(self._rbridge,
                             'rbridge_id_host_table_aging_mode_conversational')

        arp_args = dict(rbridge_id=rbridge_id)
        config = arp_config(**arp_args)
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            item = output.data.find('.//{*}aging-mode')
            if item is not None:
                return True
            else:
                return None
        if kwargs.pop('delete', False):
            config.find('.//*aging-mode').set('operation', 'delete')
        return callback(config)

    def ip_anycast_gateway(self, **kwargs):
        """
        Add anycast gateway under interface ve.

        Args:
            int_type: L3 interface type on which the anycast ip
               needs to be configured.
            name:L3 interface name on which the anycast ip
               needs to be configured.
            anycast_ip: Anycast ip which the L3 interface
               needs to be associated.
            enable (bool): If ip anycast gateway should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `int_type`, `name`, `anycast_ip` is not passed.
            ValueError: if `int_type`, `name`, `anycast_ip` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.ip_anycast_gateway(
            ...         int_type='ve',
            ...         name='89',
            ...         anycast_ip='10.20.1.1/24',
            ...         rbridge_id='1')
            ...         output = dev.interface.ip_anycast_gateway(
            ...         get=True,int_type='ve',
            ...         name='89',
            ...         anycast_ip='10.20.1.1/24',
            ...         rbridge_id='1')
            ...         output = dev.interface.ip_anycast_gateway(
            ...         enable=False,int_type='ve',
            ...         name='89',
            ...         anycast_ip='10.20.1.1/24',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        int_type = kwargs.pop('int_type').lower()
        name = kwargs.pop('name')
        anycast_ip = kwargs.pop('anycast_ip', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        valid_int_types = ['ve']
        method_class = self._rbridge
        if get and anycast_ip == '':
            enable = None
            if int_type not in valid_int_types:
                raise ValueError('`int_type` must be one of: %s' %
                                 repr(valid_int_types))
            anycast_args = dict(name=name, ip_address=anycast_ip,
                                ipv6_address=anycast_ip)
            method_name1 = 'interface_%s_ip_ip_anycast_'\
                           'address_ip_address' % int_type
            method_name2 = 'interface_%s_ipv6_ipv6_'\
                           'anycast_address_ipv6_address' % int_type
            method_name1 = 'rbridge_id_%s' % method_name1
            method_name2 = 'rbridge_id_%s' % method_name2
            anycast_args['rbridge_id'] = rbridge_id
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
            ip_anycast_gateway1 = getattr(method_class, method_name1)
            ip_anycast_gateway2 = getattr(method_class, method_name2)
            config1 = ip_anycast_gateway1(**anycast_args)
            config2 = ip_anycast_gateway2(**anycast_args)
            result = []
            result.append(callback(config1, handler='get_config'))
            result.append(callback(config2, handler='get_config'))
            return result
        elif get:
            enable = None
        ipaddress = ip_interface(unicode(anycast_ip))
        if int_type not in valid_int_types:
            raise ValueError('`int_type` must be one of: %s' %
                             repr(valid_int_types))
        if anycast_ip != '':
            ipaddress = ip_interface(unicode(anycast_ip))
            if ipaddress.version == 4:
                anycast_args = dict(name=name, ip_address=anycast_ip)
                method_name = 'interface_%s_ip_ip_anycast_'\
                              'address_ip_address' % int_type
            elif ipaddress.version == 6:
                anycast_args = dict(name=name, ipv6_address=anycast_ip)
                method_name = 'interface_%s_ipv6_ipv6_'\
                              'anycast_address_ipv6_address' % int_type
        method_name = 'rbridge_id_%s' % method_name
        anycast_args['rbridge_id'] = rbridge_id
        if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        ip_anycast_gateway = getattr(method_class, method_name)
        config = ip_anycast_gateway(**anycast_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            if ipaddress.version == 4:
                config.find('.//*ip-anycast-address').\
                  set('operation', 'delete')
            elif ipaddress.version == 6:
                config.find('.//*ipv6-anycast-address').\
                  set('operation', 'delete')
        return callback(config)

    def arp_suppression(self, **kwargs):
        """
        Enable Arp Suppression on a Vlan.

        Args:
            name:Vlan name on which the Arp suppression needs to be enabled.
            enable (bool): If arp suppression should be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `name` is not passed.
            ValueError: if `name` is invalid.
           output2 = dev.interface.arp_suppression(name='89')
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.arp_suppression(
            ...         name='89')
            ...         output = dev.interface.arp_suppression(
            ...         get=True,name='89')
            ...         output = dev.interface.arp_suppression(
            ...         enable=False,name='89')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        name = kwargs.pop('name')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        method_class = self._interface
        arp_args = dict(name=name)
        if name:
            if not pynos.utilities.valid_vlan_id(name):
                raise InvalidVlanId("`name` must be between `1` and `8191`")
        arp_suppression = getattr(method_class,
                                  'interface_vlan_interface_vlan_suppress_'
                                  'arp_suppress_arp_enable')
        config = arp_suppression(**arp_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
                config.find('.//*suppress-arp').set('operation', 'delete')
        return callback(config)

    def create_evpn_instance(self, **kwargs):
        """
        Add evpn instance.

        Args:
            evpn_instance_name: Instance name for evpn
            enable (bool): If evpn instance needs to be configured
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.interface.create_evpn_instance(
            ...         evpn_instance_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_evpn_instance(
            ...         get=True,
            ...         evpn_instance_name='100',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_evpn_instance(
            ...         enable=False,
            ...         evpn_instance_name='101',
            ...         rbridge_id='1')
            ...         output = dev.interface.create_evpn_instance(
            ...         get=True,
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        evpn_args = dict(instance_name=evpn_instance_name)
        if get:
            enable = None
        method_name = 'rbridge_id_evpn_instance_instance_name'
        method_class = self._rbridge
        evpn_args['rbridge_id'] = rbridge_id
        create_evpn_instance = getattr(method_class, method_name)
        config = create_evpn_instance(**evpn_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*/evpn-instance').set('operation', 'delete')
        pynos.utilities.print_xml_string(config)
        return callback(config)

    def evpn_instance_rt_both_ignore_as(self, **kwargs):
        """
        Add evpn instance route target ignore AS.

        Args:
            evpn_instance_name: Instance name for evpn
            enable (bool): If target community needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...conn = (switch, '22')
            ...with pynos.device.Device(conn=conn, auth=auth) as dev:
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... evpn_instance_name='100',
            ... rbridge_id='1')
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... get=True,
            ... evpn_instance_name='100',
            ... rbridge_id='1')
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... enable=False,
            ... evpn_instance_name='101',
            ... rbridge_id='1')
            ... output=dev.interface.evpn_instance_rt_both_ignore_as(
            ... get=True,
            ... rbridge_id='1')
            ...   # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        evpn_args = dict(instance_name=evpn_instance_name,
                         target_community='auto')
        if get:
            enable = None
        method_name = 'rbridge_id_evpn_instance_route_target_both_ignore_as'
        method_class = self._rbridge
        evpn_args['rbridge_id'] = rbridge_id
        evpn_instance_rt_both_ignore_as = getattr(method_class,
                                                  method_name)
        config = evpn_instance_rt_both_ignore_as(**evpn_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*target-community').set('operation', 'delete')
        return callback(config)

    def evpn_instance_duplicate_mac_timer(self, **kwargs):
        """
        Add "Duplicate MAC timer value" under evpn instance.

        Args:
            evpn_instance_name: Instance name for evpn
            duplicate_mac_timer_value: Duplicate MAC timer value.
            enable (bool): If target community needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         evpn_instance_name='100',
            ...         duplicate_mac_timer_value='10'
            ...         rbridge_id='1')
            ...         output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         get=True,
            ...         evpn_instance_name='100',
            ...         duplicate_mac_timer_value='10'
            ...         rbridge_id='1')
            ...         output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         enable=False,
            ...         evpn_instance_name='101',
            ...         duplicate_mac_timer_value='10'
            ...         rbridge_id='1')
            ...         output=dev.interface.evpn_instance_duplicate_mac_timer(
            ...         get=True,
            ...         evpn_instance_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        duplicate_mac_timer_value = kwargs.pop('duplicate_mac_timer_value',
                                               '180')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        evpn_args = dict(instance_name=evpn_instance_name,
                         duplicate_mac_timer_value=duplicate_mac_timer_value)
        if get:
            enable = None
        method_name = 'rbridge_id_evpn_instance_duplicate'\
                      '_mac_timer_duplicate_mac_timer_value'
        method_class = self._rbridge
        evpn_args['rbridge_id'] = rbridge_id
        evpn_instance_duplicate_mac_timer = getattr(method_class, method_name)
        config = evpn_instance_duplicate_mac_timer(**evpn_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*duplicate-mac-timer').set('operation', 'delete')
        return callback(config)

    def evpn_instance_mac_timer_max_count(self, **kwargs):
        """
        Add "Duplicate MAC max count" under evpn instance.

        Args:
            evpn_instance_name: Instance name for evpn
            max_count: Duplicate MAC max count.
            enable (bool): If target community needs to be enabled
                or disabled.Default:``True``.
            get (bool) : Get config instead of editing config. (True, False)
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            callback (function): A function executed upon completion of the
               method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if 'evpn_instance_name' is not passed.
            ValueError: if 'evpn_instance_name' is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         evpn_instance_name='100',
            ...         max_count='10'
            ...         rbridge_id='1')
            ...         output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         get=True,
            ...         evpn_instance_name='100',
            ...         max_count='10'
            ...         rbridge_id='1')
            ...         output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         enable=False,
            ...         evpn_instance_name='101',
            ...         max_count='10'
            ...         rbridge_id='1')
            ...         output=dev.interface.evpn_instance_mac_timer_max_count(
            ...         get=True,
            ...         evpn_instance_name='101',
            ...         rbridge_id='1')
            ...         # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
         """

        evpn_instance_name = kwargs.pop('evpn_instance_name', '')
        max_count = kwargs.pop('max_count', '5')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        evpn_args = dict(instance_name=evpn_instance_name,
                         max_count=max_count)
        if get:
            enable = None
        method_name = 'rbridge_id_evpn_instance_duplicate_'\
                      'mac_timer_max_count'
        method_class = self._rbridge
        evpn_args['rbridge_id'] = rbridge_id
        evpn_instance_mac_timer_max_count = getattr(method_class, method_name)
        config = evpn_instance_mac_timer_max_count(**evpn_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*duplicate-mac-timer').set('operation', 'delete')
        return callback(config)

    def evpn_instance_rd_auto(self, **kwargs):

        """
        Add RD auto under EVPN instance.

        Args:
            rbridge_id: Rbrdige id .
            instance_name: EVPN instance name.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output=dev.interface.evpn_instance_rd_auto(
            ...         evpn_instance_name='100',
            ...         rbridge_id='1')
         """
        config = ET.Element("config")
        rbridge_id = ET.SubElement(config, "rbridge-id",
                                   xmlns="urn:brocade.com"
                                         ":mgmt:brocade-rbridge")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        evpn_instance = ET.SubElement(rbridge_id, "evpn-instance",
                                      xmlns="urn:brocade.com:mgmt:brocade-bgp")
        instance_name_key = ET.SubElement(evpn_instance, "instance-name")
        instance_name_key.text = kwargs.pop('instance_name')
        route_distinguisher = ET.SubElement(evpn_instance,
                                            "route-distinguisher")
        ET.SubElement(route_distinguisher, "auto")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)

    def mac_move_detect_enable(self, **kwargs):
        """Enable mac move detect enable on vdx switches
        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac-move-detect-enable.
                           (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.mac_move_detect_enable()
            ...     output = dev.interface.mac_move_detect_enable(get=True)
            ...     output = dev.interface.mac_move_detect_enable(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        mac_move = getattr(self._mac_address_table,
                           'mac_address_table_mac_move_mac_move_'
                           'detect_enable')

        config = mac_move()
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            item = output.data.find('.//{*}mac-move-detect-enable')
            if item is not None:
                return True
            else:
                return None
        if kwargs.pop('delete', False):
            config.find('.//*mac-move-detect-enable').set('operation',
                                                          'delete')
        return callback(config)

    def mac_move_limit(self, **kwargs):
        """Configure mac move limit on vdx switches
        Args:
            mac_move_limit: set the limit of mac move limit
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac move limit.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.mac_move_limit()
            ...     output = dev.interface.mac_move_limit(get=True)
            ...     output = dev.interface.mac_move_limit(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        if not get_config:
            if not delete:
                mac_move_limit = kwargs.pop('mac_move_limit')
                mac_move = getattr(self._mac_address_table,
                                   'mac_address_table_mac_move_'
                                   'mac_move_limit')
                config = mac_move(mac_move_limit=mac_move_limit)
            else:
                mac_move = getattr(self._mac_address_table,
                                   'mac_address_table_mac_move_'
                                   'mac_move_limit')
                config = mac_move(mac_move_limit='')
                config.find('.//*mac-move-limit').set('operation',
                                                      'delete')
            return callback(config)

        if get_config:
            mac_move = getattr(self._mac_address_table,
                               'mac_address_table_mac_move_mac'
                               '_move_limit')
            config = mac_move(mac_move_limit='')
            output = callback(config, handler='get_config')
            if output.data.find('.//{*}mac-move-limit') is not None:
                limit = output.data.find('.//{*}mac-move-limit').text
                if limit is not None:
                    return limit
                else:
                    return None
            else:
                limit_default = "20"
                return limit_default
