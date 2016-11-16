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

from ipaddress import ip_interface
from pynos.versions.ver_6.ver_6_0_1.bgp import BGP as BaseBGP
from pynos.versions.ver_7.ver_7_0_0.yang.brocade_rbridge import brocade_rbridge

import pynos.utilities
import xml.etree.ElementTree as ET


class BGP(BaseBGP):
    """Holds all relevent methods and attributes for the BGP on NOS devices.

    Attributes:
        None
    """

    def __init__(self, callback):
        super(BGP, self).__init__(callback)
        self._rbridge = brocade_rbridge(callback=pynos.utilities.return_xml)

    def neighbor(self, **kwargs):
        """Experimental neighbor method.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            afis (list): A list of AFIs to configure.  Do not include IPv4 or
                IPv6 unicast as these are inferred from the `ip_addr`
                parameter.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `remote_as` or `ip_addr` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     delete=True, rbridge_id='225', remote_as='65535')
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225', delete=True,
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
        """
        ip_addr = ip_interface(unicode(kwargs.pop('ip_addr')))
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        remote_as = kwargs.pop('remote_as', None)
        get_config = kwargs.pop('get', False)
        if not get_config and remote_as is None:
            raise ValueError('When configuring a neighbor, you must specify '
                             'its remote-as.')
        neighbor_args = dict(router_bgp_neighbor_address=str(ip_addr.ip),
                             remote_as=remote_as,
                             rbridge_id=rbridge_id)
        if ip_addr.version == 6:
            neighbor_args['router_bgp_neighbor_ipv6_address'] = str(ip_addr.ip)

        neighbor, ip_addr_path = self._unicast_xml(ip_addr.version)
        config = neighbor(**neighbor_args)
        if ip_addr.version == 6 and not delete:
            config = self._build_ipv6(ip_addr, config, rbridge_id)

        if delete and config.find(ip_addr_path) is not None:
            if ip_addr.version == 4:
                config.find(ip_addr_path).set('operation', 'delete')
                config.find('.//*router-bgp-neighbor-address').set('operation',
                                                                   'delete')
            elif ip_addr.version == 6:
                config.find(ip_addr_path).set('operation', 'delete')
                config.find('.//*router-bgp-neighbor-ipv6-address').set(
                    'operation', 'delete')
        if get_config:
            return callback(config, handler='get_config')
        return callback(config)

    def _unicast_xml(self, ip_version):
        if ip_version == 4:
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_'
                               'router_bgp_attributes_neighbor_neighbor_ips_'
                               'neighbor_addr_remote_as')
            ip_addr_path = './/*remote-as'
        else:
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_'
                               'router_bgp_attributes_neighbor_'
                               'neighbor_ipv6s_neighbor_ipv6_addr_remote_as')
            ip_addr_path = './/*remote-as'
        return neighbor, ip_addr_path

    def _build_ipv6(self, ip_addr, config, rbridge_id):
        activate_args = dict(rbridge_id=rbridge_id,
                             af_ipv6_neighbor_address=str(ip_addr.ip))
        activate_neighbor = getattr(self._rbridge,
                                    'rbridge_id_router_router_bgp_address_'
                                    'family_ipv6_ipv6_unicast_default_vrf_'
                                    'neighbor_af_ipv6_neighbor_address_'
                                    'holder_af_ipv6_neighbor_address_activate')
        activate_neighbor = activate_neighbor(**activate_args)
        return pynos.utilities.merge_xml(config, activate_neighbor)

    def evpn_afi(self, **kwargs):
        """EVPN AFI. This method just enables/disables or gets the EVPN AFI.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225', get=True)
            ...     output = dev.bgp.evpn_afi(rbridge_id='225',
            ...     delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        config = ET.Element("config")
        rbridge_id = ET.SubElement(config, "rbridge-id",
                                   xmlns="urn:brocade.com:mgmt:"
                                         "brocade-rbridge")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        router = ET.SubElement(rbridge_id, "router")
        router_bgp = ET.SubElement(router, "router-bgp",
                                   xmlns="urn:brocade.com:mgmt:brocade-bgp")
        address_family = ET.SubElement(router_bgp, "address-family")
        l2vpn = ET.SubElement(address_family, "l2vpn")
        ET.SubElement(l2vpn, "evpn")

        if kwargs.pop('delete', False):
            config.find('.//*l2vpn').set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        return callback(config)

    def evpn_afi_peer_activate(self, **kwargs):
        """
        Activate EVPN AFI for a peer.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
                Deactivate
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.evpn_afi(rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.11',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.evpn_afi_peer_activate(rbridge_id='225',
            ...     peer_ip='10.10.10.11')
            ...     output = dev.bgp.evpn_afi_peer_activate(rbridge_id='225',
            ...     peer_ip='10.10.10.11', get=True)
            ...     output = dev.bgp.evpn_afi_peer_activate(rbridge_id='225',
            ...     peer_ip='10.10.10.11', delete=True)
            ...     output = dev.bgp.evpn_afi(rbridge_id='225',
            ...     delete=True)
            ...     output = dev.bgp.remove_bgp(rbridge_id='225')

        """
        peer_ip = kwargs.pop('peer_ip')
        callback = kwargs.pop('callback', self._callback)
        evpn_activate = getattr(self._rbridge,
                                'rbridge_id_router_router_bgp_address_family_'
                                'l2vpn_evpn_neighbor_evpn_neighbor_ipv4_'
                                'activate')
        args = dict(evpn_neighbor_ipv4_address=peer_ip, ip_addr=peer_ip,
                    rbridge_id=kwargs.pop('rbridge_id'),
                    afi='evpn')
        evpn_activate = evpn_activate(**args)
        if kwargs.pop('delete', False):
            evpn_activate.find('.//*activate').set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(evpn_activate, handler='get_config')
        return callback(evpn_activate)

    def bfd(self, **kwargs):
        """Configure BFD for BGP globally.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
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
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230')
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', get=True)
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', delete=True)
        """
        kwargs['min_tx'] = kwargs.pop('tx')
        kwargs['min_rx'] = kwargs.pop('rx')
        kwargs['delete'] = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
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
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'bfd_interval_min_tx'
        bfd_tx = getattr(self._rbridge, method_name)
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
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'bfd_interval_min_rx'
        bfd_rx = getattr(self._rbridge, method_name)
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
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'bfd_interval_multiplier'
        bfd_multiplier = getattr(self._rbridge, method_name)
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

    def retain_rt_all(self, **kwargs):
        """Retain route targets.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.retain_rt_all(rbridge_id='225')
            ...     output = dev.bgp.retain_rt_all(rbridge_id='225', get=True)
            ...     output = dev.bgp.retain_rt_all(rbridge_id='225',
            ...     delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        retain_rt_all = getattr(self._rbridge,
                                'rbridge_id_router_router_bgp_address_family_'
                                'l2vpn_evpn_retain_route_target_all')
        config = retain_rt_all(rbridge_id=kwargs.pop('rbridge_id', '1'))
        if kwargs.pop('delete', False):
            config.find('.//*retain').set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        return callback(config)

    def evpn_next_hop_unchanged(self, **kwargs):
        """Configure next hop unchanged for an EVPN neighbor.

        You probably don't want this method.  You probably want to configure
        an EVPN neighbor using `BGP.neighbor`.  That will configure next-hop
        unchanged automatically.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.evpn_next_hop_unchanged(rbridge_id='225',
            ...     ip_addr='10.10.10.10')
            ...     output = dev.bgp.evpn_next_hop_unchanged(rbridge_id='225',
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.evpn_next_hop_unchanged(rbridge_id='225',
            ...     ip_addr='10.10.10.10', delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'),
                    evpn_neighbor_ipv4_address=kwargs.pop('ip_addr'))
        next_hop_unchanged = getattr(self._rbridge,
                                     'rbridge_id_router_router_bgp_address_'
                                     'family_l2vpn_evpn_neighbor_evpn_'
                                     'neighbor_ipv4_next_hop_unchanged')
        config = next_hop_unchanged(**args)
        if kwargs.pop('delete', False):
            config.find('.//*next-hop-unchanged').set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        return callback(config)

    def graceful_restart(self, **kwargs):
        """Set BGP graceful restart

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            afi (str): Address family to configure. (ipv4, ipv6, evpn)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6',
            evpn]

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.graceful_restart(rbridge_id='225')
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     get=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     delete=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv6')
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv6', get=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='225',
            ...     afi='ipv6', delete=True)
        """
        # TODO: Add support for timers
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6', 'evpn']:
            raise AttributeError('Invalid AFI.')
        args = dict(vrf_name=kwargs.pop('vrf', 'default'),
                    rbridge_id=kwargs.pop('rbridge_id', '1'))
        graceful = None
        if 'evpn' not in afi:
            graceful = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_address_family_'
                               '{0}_{0}_unicast_default_vrf_af_common_cmds_'
                               'holder_graceful_restart_graceful_restart_'
                               'status'.format(afi))
        else:
            graceful = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_address_'
                               'family_l2vpn_evpn_graceful_restart_'
                               'graceful_restart_status'.format(afi))
        config = graceful(**args)
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            tag = 'graceful-restart'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return callback(config)

    def evpn_allowas_in(self, **kwargs):
        """Configure allowas_in for an EVPN neighbor.

        You probably don't want this method.  You probably want to configure
        an EVPN neighbor using `BGP.neighbor`.  That will configure next-hop
        unchanged automatically.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.evpn_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10')
            ...     output = dev.bgp.evpn_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.evpn_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', delete=True)
        """
        callback = kwargs.pop('callback', self._callback)
        args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'),
                    evpn_neighbor_ipv4_address=kwargs.pop('ip_addr'),
                    allowas_in=kwargs.pop('allowas_in', '5'))
        allowas_in = getattr(self._rbridge,
                             'rbridge_id_router_router_bgp_address_'
                             'family_l2vpn_evpn_neighbor_evpn_'
                             'neighbor_ipv4_allowas_in')
        config = allowas_in(**args)
        if kwargs.pop('delete', False):
            config.find('.//*allowas-in').set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        return callback(config)

    def af_ip_allowas_in(self, **kwargs):
        """Set BGP allowas-in for IPV4 and IPV6

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            allowas_in (str): Values for allowas_in (default: 5).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.l

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', get=True)
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='10.10.10.10', delete=True)
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1', afi='ipv6')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1', get=True,
            ...     afi='ipv6')
            ...     output = dev.bgp.af_ip_allowas_in(rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1', delete=True,
            ...     afi='ipv6')
        """
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        args = dict(vrf_name=kwargs.pop('vrf', 'default'),
                    rbridge_id=kwargs.pop('rbridge_id', '1'),
                    allowas_in=kwargs.pop('allowas_in', '5'))
        args['af_{0}_neighbor_address'.format(afi)] = kwargs.pop('ip_addr')
        allowas_in = getattr(self._rbridge,
                             'rbridge_id_router_router_bgp_address_family_'
                             '{0}_{0}_unicast_default_vrf_neighbor_'
                             'af_{0}_neighbor_address_holder_'
                             'af_{0}_neighbor_address_allowas_in'.format(afi))

        config = allowas_in(**args)
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            config.find('.//*allowas-in').set('operation', 'delete')
        return callback(config)

    def peer_bfd_timers(self, **kwargs):
        """Configure BFD for BGP globally.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
            peer_ip (str): Peer IPv4 address for BFD setting.
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
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        remote_as='65535', rbridge_id='230')
            ...        output = dev.bgp.peer_bfd_timers(peer_ip='10.10.10.20',
            ...        rx='300', tx='300', multiplier='3', rbridge_id='230')
            ...        output = dev.bgp.peer_bfd_timers(peer_ip='10.10.10.20',
            ...        rx='300', tx='300', multiplier='3', rbridge_id='230',
            ...        get=True)
            ...        output = dev.bgp.peer_bfd_timers(peer_ip='10.10.10.20',
            ...        rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', delete=True)
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        delete=True, rbridge_id='230', remote_as='65535')
        """
        kwargs['min_tx'] = kwargs.pop('tx')
        kwargs['min_rx'] = kwargs.pop('rx')
        kwargs['router_bgp_neighbor_address'] = kwargs.pop('peer_ip')
        kwargs['delete'] = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        bfd_tx = self._peer_bfd_tx(**kwargs)
        bfd_rx = self._peer_bfd_rx(**kwargs)
        bfd_multiplier = self._peer_bfd_multiplier(**kwargs)
        if kwargs.pop('get', False):
            return self._peer_get_bfd(bfd_tx, bfd_rx, bfd_multiplier)
        config = pynos.utilities.merge_xml(bfd_tx, bfd_rx)
        config = pynos.utilities.merge_xml(config, bfd_multiplier)
        return callback(config)

    def enable_peer_bfd(self, **kwargs):
        """BFD enable for each specified peer.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
            peer_ip (str): Peer IPv4 address for BFD setting.
            delete (bool): True if BFD configuration should be deleted.
                Default value will be False if not specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.
        Returns:
            XML to be passed to the switch.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        remote_as='65535', rbridge_id='230')
            ...        output = dev.bgp.enable_peer_bfd(peer_ip='10.10.10.20',
            ...        rbridge_id='230')
            ...        output = dev.bgp.enable_peer_bfd(peer_ip='10.10.10.20',
            ...        rbridge_id='230',get=True)
            ...        output = dev.bgp.enable_peer_bfd(peer_ip='10.10.10.20',
            ...        rbridge_id='230', delete=True)
            ...        output = dev.bgp.neighbor(ip_addr='10.10.10.20',
            ...        delete=True, rbridge_id='230', remote_as='65535')
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'neighbor_neighbor_ips_neighbor_addr_bfd_bfd_enable'
        bfd_enable = getattr(self._rbridge, method_name)
        kwargs['router_bgp_neighbor_address'] = kwargs.pop('peer_ip')
        callback = kwargs.pop('callback', self._callback)
        config = bfd_enable(**kwargs)
        if kwargs.pop('delete', False):
            tag = 'bfd-enable'
            config.find('.//*%s' % tag).set('operation', 'delete')
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        else:
            return callback(config)

    def _peer_bfd_tx(self, **kwargs):
        """Return the BFD minimum transmit interval XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            peer_ip (str): Peer IPv4 address for BFD setting.
            min_tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'neighbor_neighbor_ips_neighbor_addr_bfd_interval_min_tx'
        bfd_tx = getattr(self._rbridge, method_name)
        config = bfd_tx(**kwargs)
        if kwargs['delete']:
            tag = 'min-tx'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _peer_bfd_rx(self, **kwargs):
        """Return the BFD minimum receive interval XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            peer_ip (str): Peer IPv4 address for BFD setting.
            min_rx (str): BFD receive interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'neighbor_neighbor_ips_neighbor_addr_bfd_interval_min_rx'
        bfd_rx = getattr(self._rbridge, method_name)
        config = bfd_rx(**kwargs)
        if kwargs['delete']:
            tag = 'min-rx'
            config.find('.//*%s' % tag).set('operation', 'delete')
            pass
        return config

    def _peer_bfd_multiplier(self, **kwargs):
        """Return the BFD multiplier XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            peer_ip (str): Peer IPv4 address for BFD setting.
            min_tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_' \
                      'neighbor_neighbor_ips_neighbor_addr_bfd_interval_' \
                      'multiplier'

        bfd_multiplier = getattr(self._rbridge, method_name)
        config = bfd_multiplier(**kwargs)
        if kwargs['delete']:
            tag = 'multiplier'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _peer_get_bfd(self, tx, rx, multiplier):
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

    def vni_add(self, **kwargs):
        """Add VNIs to the EVPN Instance
        Args:
            rbridge_id (str): rbridge-id for device.
            evpn_instance (str): Name of the evpn instance.
            vni (str): vnis to the evpn instance
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the vni configuration
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `rbridge_id`,`evpn_instance`, 'vni' is not passed.
            ValueError: if `rbridge_id`, `evpn_instance`, 'vni' is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         evpn_instance="leaf1", vni='10')
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         evpn_instance="leaf1", vni='10', delete=True)
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         evpn_instance="leaf1", vni='10', delete=True)
            ...         output = dev.bgp.vni_add(rbridge_id='2',
            ...         get=True)

        """
        rbridge_id = kwargs['rbridge_id']
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        result = []

        method_class = self._rbridge
        if not get_config:
            evpn_instance = kwargs['evpn_instance']
            vni = kwargs['vni']
            if not delete:
                method_name = 'rbridge_id_evpn_instance_vni_vni_add_add'
                vni_add = getattr(method_class, method_name)
                vni_args = dict(rbridge_id=rbridge_id,
                                instance_name=evpn_instance,
                                add=vni)
                config = vni_add(**vni_args)
            else:
                method_name = 'rbridge_id_evpn_instance_vni_vni_add_remove'
                vni_add = getattr(method_class, method_name)
                vni_args = dict(rbridge_id=rbridge_id,
                                instance_name=evpn_instance,
                                remove=vni)
                config = vni_add(**vni_args)
                config.find('.//*vni-add').set('operation', 'delete')
            result = callback(config)

        elif get_config:
            evpn_instance = kwargs.pop('evpn_instance', '')
            method_name = 'rbridge_id_evpn_instance_vni_vni_add_add'
            vni_add = getattr(method_class, method_name)
            vni_args = dict(rbridge_id=rbridge_id, instance_name=evpn_instance,
                            add='')
            config = vni_add(**vni_args)
            evpninstance = ''
            evpn_vni = ''
            output = callback(config, handler='get_config')
            for item in output.data.findall('.//{*}evpn-instance'):
                if item.find('.//{*}instance-name') is not None:
                    evpninstance = item.find('.//{*}instance-name').text

                if item.find('.//{*}add') is not None:
                    evpn_vni = item.find('.//{*}add').text
            tmp = {'rbridge_id': rbridge_id, 'evpn_instance': evpninstance,
                   'vni': evpn_vni}
            result.append(tmp)
        return result

    def vrf_redistribute_connected(self, **kwargs):
        """Enable redistribute connected on vrf address family.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vrf' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6. Default = ipv4

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.vrf_redistribute_connected(vrf='vrf101',
            ...     rbridge_id='4')
            ...     device.bgp.vrf_redistribute_connected(vrf='vrf101',
            ...     get=True, rbridge_id='4')
            ...     device.bgp.vrf_redistribute_connected(vrf='vrf101',
            ...     delete=True, rbridge_id='4')
        """
        afi = kwargs.pop('afi', 'ipv4')
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')

        if "ipv4" in afi:
            addr_family = getattr(self._rbridge,
                                  'rbridge_id_router_router_bgp_address_family'
                                  '_ipv4_ipv4_unicast_af_vrf_af_ipv4_uc_and_'
                                  'vrf_cmds_call_point_holder_redistribute_'
                                  'connected_redistribute_connected')
            neighbor_args = dict(af_vrf_name=vrf,
                                 rbridge_id=rbridge_id)
        elif "ipv6" in afi:
            addr_family = getattr(self._rbridge,
                                  'rbridge_id_router_router_bgp_address_family'
                                  '_ipv6_ipv6_unicast_af_ipv6_vrf_af_ipv6_uc_'
                                  'and_vrf_cmds_call_point_holder_redistribute'
                                  '_connected_redistribute_connected')
            neighbor_args = dict(af_ipv6_vrf_name=vrf,
                                 rbridge_id=rbridge_id)

        config = addr_family(**neighbor_args)

        result = False
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            if output.data.findall('.//{*}redistribute/{*}connected') != []:
                result = True
        elif delete:
            config.find('.//*redistribute-connected')\
                .set('operation', 'delete')
            result = callback(config)
        else:
            result = callback(config)

        return result

    def vrf_unicast_address_family(self, **kwargs):
        """Add BGP v4/v6 address family.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `vrf' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6. Default = ipv4

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.vrf_unicast_address_family(delete=True,
            ...     vrf='vrf101', rbridge_id='4')
            ...     device.bgp.vrf_unicast_address_family(get=True,
            ...     vrf='vrf101', rbridge_id='4')
            ...     device.bgp.vrf_unicast_address_family(vrf='vrf101',
            ...     rbridge_id='4')
        """
        afi = kwargs.pop('afi', 'ipv4')
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')

        if "ipv4" in afi:
            addr_family = getattr(self._rbridge,
                                  'rbridge_id_router_router_bgp_address_family'
                                  '_ipv4_ipv4_unicast_af_vrf_af_vrf_name')
            neighbor_args = dict(af_vrf_name=vrf,
                                 rbridge_id=rbridge_id)
        elif "ipv6" in afi:
            addr_family = getattr(self._rbridge,
                                  'rbridge_id_router_router_bgp_address_family'
                                  '_ipv6_ipv6_unicast_af_ipv6_vrf_af_ipv6_'
                                  'vrf_name')
            neighbor_args = dict(af_ipv6_vrf_name=vrf,
                                 rbridge_id=rbridge_id)

        config = addr_family(**neighbor_args)

        result = False
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            if "ipv4" in afi:
                if output.data.findall('.//{*}af-vrf-name') != []:
                    result = True
            elif "ipv6" in afi:
                if output.data.findall('.//{*}af-ipv6-vrf-name') != []:
                    result = True
        elif delete:
            if "ipv4" in afi:
                config.find('.//*af-vrf').set('operation', 'delete')
                result = callback(config)
            elif "ipv6" in afi:
                config.find('.//*af-ipv6-vrf').set('operation', 'delete')
                result = callback(config)
        else:
            result = callback(config)
        return result

    def vrf_max_paths(self, **kwargs):
        """Set BGP max paths property on VRF address family.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            paths (str): Number of paths for BGP ECMP (default: 8).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.vrf_max_paths(paths='8',
            ...     rbridge_id='225')
            ...     output = dev.bgp.vrf_max_paths(
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225')
            ...     output = dev.bgp.vrf_max_paths(afi='ipv6',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.vrf_max_paths(paths='8', afi='ipv5',
            ...     rbridge_id='225') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        vrf = kwargs.pop('vrf', 'default')
        get_config = kwargs.pop('get', False)
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        if "ipv4" in afi:
            if not get_config:
                args = dict(af_vrf_name=vrf,
                            rbridge_id=kwargs.pop('rbridge_id', '1'),
                            load_sharing_value=kwargs.pop('paths', '8'))
            else:
                args = dict(af_vrf_name=vrf,
                            rbridge_id=kwargs.pop('rbridge_id', '1'),
                            load_sharing_value='')
            max_paths = getattr(self._rbridge,
                                'rbridge_id_router_router_bgp_address_family_'
                                'ipv4_ipv4_unicast_af_vrf_maximum_paths_'
                                'load_sharing_value')
        elif "ipv6" in afi:
            if not get_config:
                args = dict(af_ipv6_vrf_name=vrf,
                            rbridge_id=kwargs.pop('rbridge_id', '1'),
                            load_sharing_value=kwargs.pop('paths', '8'))
            else:
                args = dict(af_ipv6_vrf_name=vrf,
                            rbridge_id=kwargs.pop('rbridge_id', '1'),
                            load_sharing_value='')
            max_paths = getattr(self._rbridge,
                                'rbridge_id_router_router_bgp_address_family_'
                                'ipv6_ipv6_unicast_af_ipv6_vrf_maximum_paths_'
                                'load_sharing_value')

        config = max_paths(**args)
        if get_config:
            output = callback(config, handler='get_config')
            if output.data.find('.//{*}load-sharing-value') is not None:
                max_path = output.data.find('.//{*}load-sharing-value').text
                result = {"vrf": vrf,
                          "max_path": max_path}
                return result
            else:
                return None
        if kwargs.pop('delete', False):
            config.find('.//*load-sharing-value').set('operation', 'delete')
        return callback(config)

    def default_vrf_unicast_address_family(self, **kwargs):
        """Create default address family (ipv4/ipv6) under router bgp.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                              configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected under default vrf
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `afi' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.default_vrf_unicast_address_family(delete=True,
            ...     rbridge_id='4')
            ...     device.bgp.default_vrf_unicast_address_family(get=True,
            ...     rbridge_id='4')
            ...     device.bgp.default_vrf_unicast_address_family(
            ...     rbridge_id='4', afi='ipv6')
        """
        afi = kwargs.pop('afi', 'ipv4')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')

        addr_family = getattr(self._rbridge,
                              'rbridge_id_router_router_bgp_address_family'
                              '_{0}_{0}_unicast_default_vrf_default_vrf_'
                              'selected'.format(afi))
        neighbor_args = dict(rbridge_id=rbridge_id)

        config = addr_family(**neighbor_args)

        result = False
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            if output.data.findall('.//{*}default-vrf-selected') != []:
                result = True
        elif delete:
            config.find('.//*af-vrf').set('operation', 'delete')
            result = callback(config)
        else:
            result = callback(config)
        return result

    def default_vrf_redistribute_connected(self, **kwargs):
        """Enable redistribute connected on default vrf address family.

        Args:
            afi (str): Address family to configure. (ipv4, ipv6)
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the redistribute connected under default vrf
                if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `afi' is not expected
            AttributeError: if 'afi' is not in ipv4,ipv6. Default = ipv4

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     device.bgp.default.vrf_redistribute_connected(
            ...     rbridge_id='4')
            ...     device.bgp.default.vrf_redistribute_connected(
            ...     get=True, rbridge_id='4')
            ...     device.bgp.default.vrf_redistribute_connected(
            ...     delete=True, rbridge_id='4')
        """
        afi = kwargs.pop('afi', 'ipv4')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')

        addr_family = getattr(self._rbridge,
                              'rbridge_id_router_router_bgp_address_family'
                              '_{0}_{0}_unicast_default_vrf_af_{0}_uc_and_'
                              'vrf_cmds_call_point_holder_redistribute_'
                              'connected_redistribute_connected'.format(afi))
        neighbor_args = dict(rbridge_id=rbridge_id)

        config = addr_family(**neighbor_args)

        result = False
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            if output.data.findall('.//{*}redistribute/{*}connected') != []:
                result = True
        elif delete:
            config.find('.//*redistribute-connected')\
                .set('operation', 'delete')
            result = callback(config)
        else:
            result = callback(config)

        return result

    def default_vrf_max_paths(self, **kwargs):
        """Set BGP max paths property on default VRF address family.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            paths (str): Number of paths for BGP ECMP (default: 8).
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            ``AttributeError``: When `afi` is not one of ['ipv4', 'ipv6']

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...     rbridge_id='225')
            ...     output = dev.bgp.default_vrf_max_paths(
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...              afi='ipv6', rbridge_id='225')
            ...     output = dev.bgp.default_vrf_max_paths(
            ...              afi='ipv6', rbridge_id='225', get=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...              afi='ipv6', rbridge_id='225', delete=True)
            ...     output = dev.bgp.default_vrf_max_paths(paths='8',
            ...              afi='ipv5', rbridge_id='225')
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        if not get_config:
            args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'),
                        load_sharing_value=kwargs.pop('paths', '8'))
        else:
            args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'),
                        load_sharing_value='')
        max_paths = getattr(self._rbridge,
                            'rbridge_id_router_router_bgp_address_family_'
                            '{0}_{0}_unicast_default_vrf_af_common_cmds_'
                            'holder_maximum_paths_load_'
                            'sharing_value'.format(afi))

        config = max_paths(**args)
        if get_config:
            output = callback(config, handler='get_config')
            if output.data.find('.//{*}load-sharing-value') is not None:
                max_path = output.data.find('.//{*}load-sharing-value').text
                result = {"max_path": max_path}
                return result
            else:
                return None
        if kwargs.pop('delete', False):
            config.find('.//*load-sharing-value').set('operation', 'delete')
        return callback(config)
