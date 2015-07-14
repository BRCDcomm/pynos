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
from pynos.versions.base.yang.brocade_rbridge import brocade_rbridge
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
            vrf (str): The VRF for this BGP process.
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
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.bgp.local_asn(local_as='65535', rbridge_id='225')
            >>> dev.bgp.local_asn() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        vrf = kwargs.pop('vrf', 'default')
        local_as = kwargs.pop('local_as')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        bgp_args = dict(vrf_name=vrf, rbridge_id=rbridge_id)
        config = self._rbridge.rbridge_id_router_bgp_vrf_name(**bgp_args)
        callback(config)
        local_as_args = dict(vrf_name=vrf,
                             local_as=local_as,
                             rbridge_id=rbridge_id)
        local_as = getattr(self._rbridge,
                           'rbridge_id_router_bgp_router_bgp_cmds_holder_'
                           'router_bgp_attributes_local_as')
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
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.bgp.local_asn(local_as='65535', rbridge_id='225')
            >>> output = dev.bgp.remove_bgp(rbridge_id='225')
        """
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        bgp_args = dict(vrf_name=vrf, rbridge_id=rbridge_id)
        config = self._rbridge.rbridge_id_router_bgp_vrf_name(**bgp_args)
        bgp = config.find('.//*bgp')
        bgp.set('operation', 'delete')

        return callback(config)

    def add_neighbor(self, **kwargs):
        """Add BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `remote_as` or `ip_addr` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.bgp.local_asn(local_as='65535', rbridge_id='225')
            >>> output = dev.bgp.add_neighbor(ip_addr='10.10.10.10',
            ... remote_as='65535', rbridge_id='225')
            >>> dev.bgp.add_neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_addr = kwargs.pop('ip_addr')
        remote_as = kwargs.pop('remote_as')
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        neighbor_args = dict(router_bgp_neighbor_address=ip_addr,
                             remote_as=remote_as,
                             vrf_name=vrf,
                             rbridge_id=rbridge_id)

        add_neighbor = getattr(self._rbridge,
                               'rbridge_id_router_bgp_router_bgp_cmds_holder_'
                               'router_bgp_attributes_neighbor_neighbor_ips_'
                               'neighbor_addr_remote_as')
        config = add_neighbor(**neighbor_args)
        return callback(config)

    def remove_neighbor(self, **kwargs):
        """Remove BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `ip_addr` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.48.225', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn=conn, auth=auth)
            >>> output = dev.bgp.remove_neighbor(ip_addr='10.10.10.10',
            ... rbridge_id='225')
            >>> dev.bgp.remove_neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_addr = kwargs.pop('ip_addr')
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        neighbor_args = dict(router_bgp_neighbor_address=ip_addr,
                             vrf_name=vrf,
                             rbridge_id=rbridge_id)

        remove_neighbor = getattr(self._rbridge,
                                  'rbridge_id_router_bgp_router_bgp_'
                                  'cmds_holder_router_bgp_attributes_neighbor_'
                                  'neighbor_ips_neighbor_addr_router_bgp_'
                                  'neighbor_address')
        config = remove_neighbor(**neighbor_args)
        neighbor_addr = config.find('.//*neighbor-addr')
        neighbor_addr.set('operation', 'delete')
        return callback(config)
