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

from ipaddress import ip_interface
from pynos.versions.ver_6.ver_6_0_1.yang.brocade_rbridge import brocade_rbridge
import pynos.utilities


class BGP(object):
    """
    The BGP class holds all relevent methods and attributes for the BGP
    capabilities of the NOS device.

    Attributes:
        None
    """
    def __init__(self, callback):
        """
        BGP object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            BGP Object

        Raises:
            None
        """
        self._callback = callback
        self._rbridge = brocade_rbridge(callback=pynos.utilities.return_xml)

    def local_asn(self, **kwargs):
        """Set BGP local ASN.

        Args:
            local_as (str): Local ASN of NOS deice.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `local_as` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     dev.bgp.local_asn() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        local_as = kwargs.pop('local_as')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        local_as_args = dict(local_as=local_as,
                             rbridge_id=rbridge_id)
        enable_bgp = getattr(self._rbridge,
                             'rbridge_id_router_router_bgp_router_bgp_'
                             'attributes_local_as')(**local_as_args)
        bgp = enable_bgp.find('.//*.//*.//*')
        bgp.remove(bgp.find('.//*'))
        callback(enable_bgp)
        local_as = getattr(self._rbridge,
                           'rbridge_id_router_router_bgp_router_bgp_attri'
                           'butes_local_as')
        config = local_as(**local_as_args)
        return callback(config)

    def remove_bgp(self, **kwargs):
        """Remove BGP process completely.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
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
            ...     output = dev.bgp.remove_bgp(rbridge_id='225')
        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        disable_args = dict(rbridge_id=rbridge_id, local_as='65000')
        config = getattr(self._rbridge,
                         'rbridge_id_router_router_bgp_router_bgp_'
                         'attributes_local_as')(**disable_args)
        bgp = config.find('.//*.//*.//*')
        bgp.remove(bgp.find('.//*'))
        bgp.set('operation', 'delete')

        return callback(config)

    def neighbor(self, **kwargs):
        """Add BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        # Returns:
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
            ...     delete=True, rbridge_id='225')
            ...     dev.bgp.neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_addr = kwargs.pop('ip_addr')
        remote_as = kwargs.pop('remote_as', None)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        ip_addr = ip_interface(unicode(ip_addr))

        if not delete and remote_as is None:
            raise ValueError('When configuring a neighbor, you must specify '
                             'its remote-as.')
        if delete and ip_addr.version == 6:
            raise NotImplementedError('IPv6 Neighbor removal on NOS 6.0.1 is '
                                      'currently not supported.')

        neighbor_args = dict(router_bgp_neighbor_address=str(ip_addr.ip),
                             remote_as=remote_as,
                             rbridge_id=rbridge_id)

        if ip_addr.version == 4:
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_'
                               'router_bgp_attributes_neighbor_neighbor_ips_'
                               'neighbor_addr_remote_as')
            ip_addr_path = './/*neighbor-addr'
        else:
            neighbor_args['router_bgp_neighbor_ipv6_address'] = str(ip_addr.ip)
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_'
                               'router_bgp_attributes_neighbor_'
                               'neighbor_ipv6s_neighbor_ipv6_addr_remote_as')
            ip_addr_path = './/*neighbor-ipv6-addr'

        config = neighbor(**neighbor_args)

        if delete:
            neighbor = config.find(ip_addr_path)
            neighbor.set('operation', 'delete')
            neighbor.remove(neighbor.find('remote-as'))
        else:
            if ip_addr.version == 6:
                callback(config)
                activate_args = dict(rbridge_id=rbridge_id,
                                     af_ipv6_neighbor_address=str(ip_addr.ip))
                activate_neighbor = getattr(self._rbridge,
                                            'rbridge_id_router_router_bgp_'
                                            'address_family_ipv6_ipv6_unicast_'
                                            'default_vrf_neighbor_af_ipv6_'
                                            'neighbor_address_holder_af_ipv6_'
                                            'neighbor_address_activate')
                config = activate_neighbor(**activate_args)
        return callback(config)
