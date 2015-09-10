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
import xml.etree.ElementTree as ET
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

    @property
    def enabled(self):
        """bool: ``True`` if BGP is enabled; ``False`` if BGP is disabled.
        """
        namespace = 'urn:ietf:params:xml:ns:netconf:base:1.0'
        bgp_filter = 'rbridge-id/router/bgp'
        bgp_config = ET.Element('get-config', xmlns="%s" % namespace)
        source = ET.SubElement(bgp_config, 'source')
        ET.SubElement(source, 'running')
        ET.SubElement(bgp_config, 'filter',
                      type="xpath", select="%s" % bgp_filter)
        bgp_config = self._callback(bgp_config, handler='get')
        namespace = 'urn:brocade.com:mgmt:brocade-bgp'
        enabled = bgp_config.find('.//*{%s}bgp' % namespace)
        if enabled is not None:
            return True
        return False

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
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     dev.bgp.local_asn() # doctest: +IGNORE_EXCEPTION_DETAIL
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
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.local_asn(local_as='65535',
            ...     rbridge_id='225')
            ...     output = dev.bgp.remove_bgp(rbridge_id='225')
        """
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        bgp_args = dict(vrf_name=vrf, rbridge_id=rbridge_id)
        config = self._rbridge.rbridge_id_router_bgp_vrf_name(**bgp_args)
        config.find('.//*bgp').set('operation', 'delete')

        return callback(config)

    def neighbor(self, **kwargs):
        """Add BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `remote_as` or `ip_addr` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
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
            ...     output = dev.bgp.neighbor(delete=True, rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     dev.bgp.neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_addr = kwargs.pop('ip_addr')
        remote_as = kwargs.pop('remote_as', None)
        vrf = kwargs.pop('vrf', 'default')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        ip_addr = ip_interface(unicode(ip_addr))

        if not delete and remote_as is None:
            raise ValueError('When configuring a neighbor, you must specify '
                             'its remote-as.')

        neighbor_args = dict(router_bgp_neighbor_address=str(ip_addr.ip),
                             remote_as=remote_as,
                             vrf_name=vrf,
                             rbridge_id=rbridge_id)

        if ip_addr.version == 4:
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_bgp_router_bgp_cmds_holder_'
                               'router_bgp_attributes_neighbor_ips_'
                               'neighbor_addr_remote_as')
            ip_addr_path = './/*neighbor-addr'
        else:
            neighbor_args['router_bgp_neighbor_ipv6_address'] = str(ip_addr.ip)
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_bgp_router_bgp_cmds_holder_'
                               'router_bgp_attributes_neighbor_ipv6s_neighbor_'
                               'ipv6_addr_remote_as')
            ip_addr_path = './/*neighbor-ipv6-addr'

        config = neighbor(**neighbor_args)

        if delete:
            neighbor = config.find(ip_addr_path)
            neighbor.set('operation', 'delete')
            neighbor.remove(neighbor.find('remote-as'))
            if ip_addr.version == 6:
                activate_args = dict(vrf_name=vrf, rbridge_id=rbridge_id,
                                     af_ipv6_neighbor_address=str(ip_addr.ip))
                activate_neighbor = getattr(self._rbridge,
                                            'rbridge_id_router_bgp_router_bgp_'
                                            'cmds_holder_address_family_ipv6_'
                                            'ipv6_unicast_af_ipv6_neighbor_'
                                            'address_holder_af_ipv6_'
                                            'neighbor_address_activate')
                deactivate = activate_neighbor(**activate_args)
                deactivate.find('.//*af-ipv6-neighbor-'
                                'address').set('operation', 'delete')
                callback(deactivate)
        else:
            if ip_addr.version == 6:
                callback(config)
                activate_args = dict(vrf_name=vrf, rbridge_id=rbridge_id,
                                     af_ipv6_neighbor_address=str(ip_addr.ip))
                activate_neighbor = getattr(self._rbridge,
                                            'rbridge_id_router_bgp_router_bgp_'
                                            'cmds_holder_address_family_ipv6_'
                                            'ipv6_unicast_af_ipv6_neighbor_'
                                            'address_holder_af_ipv6_'
                                            'neighbor_address_activate')
                config = activate_neighbor(**activate_args)
        return callback(config)
