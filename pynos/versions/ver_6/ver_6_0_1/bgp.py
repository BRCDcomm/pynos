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
from pynos.versions.ver_6.ver_6_0_1.yang.brocade_rbridge import brocade_rbridge
import pynos.utilities
from pynos.versions.base.bgp import BGP as BaseBGP


class BGP(BaseBGP):
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
            get (bool): Get config instead of editing config. (True, False)
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
        is_get_config = kwargs.pop('get', False)
        if not is_get_config:
            local_as = kwargs.pop('local_as')
        else:
            local_as = ''
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        local_as_args = dict(local_as=local_as,
                             rbridge_id=rbridge_id)
        enable_bgp = getattr(self._rbridge,
                             'rbridge_id_router_router_bgp_router_bgp_'
                             'attributes_local_as')(**local_as_args)
        bgp = enable_bgp.find('.//*.//*.//*')
        bgp.remove(bgp.find('.//*'))
        if not is_get_config:
            callback(enable_bgp)
        local_as = getattr(self._rbridge,
                           'rbridge_id_router_router_bgp_router_bgp_attri'
                           'butes_local_as')
        config = local_as(**local_as_args)
        if is_get_config:
            return callback(config, handler='get_config')
        return callback(config)

    def as4_capability(self, **kwargs):
        """Set Spanning Tree state.

        Args:
            enabled (bool): Is AS4 Capability enabled? (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:

            ValueError: if `enabled` are invalid.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.local_asn(local_as='65535',
            ...         rbridge_id='225')
            ...         output = dev.bgp.as4_capability(
            ...         rbridge_id='225', enabled=True)
            ...         output = dev.bgp.as4_capability(
            ...         rbridge_id='225', enabled=False)
        """
        enabled = kwargs.pop('enabled', True)
        callback = kwargs.pop('callback', self._callback)

        if not isinstance(enabled, bool):
            raise ValueError('%s must be `True` or `False`.' % repr(enabled))

        as4_capability_args = dict(vrf_name=kwargs.pop('vrf', 'default'),
                                   rbridge_id=kwargs.pop('rbridge_id', '1'))

        as4_capability = getattr(self._rbridge,
                                 'rbridge_id_router_router_bgp_router_bgp'
                                 '_attributes_capability_as4_enable')

        config = as4_capability(**as4_capability_args)

        if not enabled:
            capability = config.find('.//*capability')
            capability.set('operation', 'delete')
            # shutdown = capability.find('.//*as4-enable')
            # shutdown.set('operation', 'delete')

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
            get (bool): Get config instead of editing config. (True, False)
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
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1',
            ...     delete=True)
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

        neighbor_args = dict(router_bgp_neighbor_address=str(ip_addr.ip),
                             remote_as=remote_as,
                             rbridge_id=rbridge_id)
        if ip_addr.version == 6:
            neighbor_args['router_bgp_neighbor_ipv6_address'] = str(ip_addr.ip)

        if ip_addr.version == 4:
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

        config = neighbor(**neighbor_args)

        if delete and config.find(ip_addr_path) is not None:
            if ip_addr.version == 4:
                config.find(ip_addr_path).set('operation', 'delete')
                config.find('.//*router-bgp-neighbor-address').set('operation',
                                                                   'delete')
            elif ip_addr.version == 6:
                config.find(ip_addr_path).set('operation', 'delete')
                config.find('.//*router-bgp-neighbor-ipv6-address').set(
                    'operation', 'delete')
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
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        return callback(config)

    def neighbor_password(self, **kwargs):
        """Add BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            password (str): Password to be used between the peers for MD5
            authentication
            delete (bool): Deletes the neighbor if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
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
            ...     output = dev.bgp.neighbor_password(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225', password='test')
            ...     output = dev.bgp.neighbor_password(ip_addr='10.10.10.10',
            ...     remote_as='65535', rbridge_id='225', password='test',
            ...     delete=True)
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     output = dev.bgp.neighbor_password(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1',
            ...     password='test')
            ...     output = dev.bgp.neighbor_password(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1',
            ...     delete=True)
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     delete=True, rbridge_id='225')
            ...     output = dev.bgp.neighbor(remote_as='65535',
            ...     rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1',
            ...     delete=True)
            ...     dev.bgp.neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_addr = kwargs.pop('ip_addr')
        remote_as = kwargs.pop('remote_as', None)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        delete = kwargs.pop('delete', False)
        password = kwargs.pop('password', '')
        callback = kwargs.pop('callback', self._callback)
        ip_addr = ip_interface(unicode(ip_addr))
        get_config = kwargs.pop('get', False)

        if password == '' and not delete and not get_config:
            raise ValueError('When configuring a neighbor password, you must '
                             'specify a non empty password')
        if not delete and remote_as is None:
            raise ValueError('When configuring a neighbor, you must specify '
                             'its remote-as.')

        neighbor_args = dict(router_bgp_neighbor_address=str(ip_addr.ip),
                             remote_as=remote_as,
                             rbridge_id=rbridge_id,
                             password=password)

        if ip_addr.version == 4:
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_'
                               'router_bgp_attributes_neighbor_neighbor_ips_'
                               'neighbor_addr_password')
            ip_addr_path = './/*password'
        else:
            neighbor_args['router_bgp_neighbor_ipv6_address'] = str(ip_addr.ip)
            neighbor = getattr(self._rbridge,
                               'rbridge_id_router_router_bgp_'
                               'router_bgp_attributes_neighbor_'
                               'neighbor_ipv6s_neighbor_ipv6_addr_password')
            ip_addr_path = './/*password'

        config = neighbor(**neighbor_args)

        if delete:
            if ip_addr.version == 4:
                config.find('.//*router-bgp-neighbor-address').set('operation',
                                                                   'delete')
                config.find(ip_addr_path).set('operation', 'delete')
            elif ip_addr.version == 6:
                config.find('.//*router-bgp-neighbor-ipv6-address').set(
                    'operation', 'delete')
                config.find(ip_addr_path).set('operation', 'delete')

        if get_config:
            return callback(config, handler='get_config')
        return callback(config)

    def get_bgp_neighbors(self, **kwargs):
        """Get BGP neighbors configured on a device.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            vrf (str): The VRF for this BGP process.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            List of 0 or more BGP Neighbors on the specified rbridge.

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
            ...     result = dev.bgp.get_bgp_neighbors(rbridge_id='225')
            ...     assert len(result) >= 1
            ...     output = dev.bgp.neighbor(ip_addr='10.10.10.10',
            ...     delete=True, rbridge_id='225')
            ...     output = dev.bgp.neighbor(delete=True, rbridge_id='225',
            ...     ip_addr='2001:4818:f000:1ab:cafe:beef:1000:1')
            ...     dev.bgp.neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            NotImplementedError
            KeyError
        """
        callback = kwargs.pop('callback', self._callback)
        neighbor_args = dict(router_bgp_neighbor_address='',
                             remote_as='',
                             vrf_name=kwargs.pop('vrf', 'default'),
                             rbridge_id=kwargs.pop('rbridge_id', '1'))

        neighbor = getattr(self._rbridge,
                           'rbridge_id_router_router_bgp_'
                           'router_bgp_attributes_neighbor_neighbor_ips_'
                           'neighbor_addr_remote_as')
        config = neighbor(**neighbor_args)
        output = callback(config, handler='get_config')
        result = []
        urn = "{urn:brocade.com:mgmt:brocade-bgp}"
        # IPv4 BGP Neighbor Handling
        for item in output.data.findall('.//{*}neighbor-addr'):
            neighbor_address = item.find(
                '%srouter-bgp-neighbor-address' % urn).text
            remote_as = item.find('%sremote-as' % urn).text
            item_results = {'neighbor-address': neighbor_address,
                            'remote-as': remote_as}
            result.append(item_results)

        # IPv6 BGP Neighbor handling
        neighbor_args['router_bgp_neighbor_ipv6_address'] = ''
        neighbor = getattr(self._rbridge,
                           'rbridge_id_router_router_bgp_'
                           'router_bgp_attributes_neighbor_'
                           'neighbor_ipv6s_neighbor_ipv6_addr_remote_as')
        config = neighbor(**neighbor_args)
        output = callback(config, handler='get_config')
        for item in output.data.findall('.//{*}neighbor-ipv6-addr'):
            neighbor_address = item.find(
                '%srouter-bgp-neighbor-ipv6-address' % urn).text
            remote_as = item.find('%sremote-as' % urn).text
            item_results = {'neighbor-address': neighbor_address,
                            'remote-as': remote_as}
            result.append(item_results)

        return result

    def redistribute(self, **kwargs):
        """Set BGP redistribute properties.

        Args:
            vrf (str): The VRF for this BGP process.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            source (str): Source for redistributing. (connected)
            afi (str): Address family to configure. (ipv4, ipv6)
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `source` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.redistribute(source='connected',
            ...     rbridge_id='225')
            ...     output = dev.bgp.redistribute(source='connected',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.redistribute(source='connected',
            ...     rbridge_id='225', delete=True)
            ...     dev.bgp.redistribute() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
            ...     dev.bgp.redistribute(source='connected', rbridge_id='225',
            ...     afi='hodor') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
            ...     dev.bgp.redistribute(source='hodor', rbridge_id='225',
            ...     afi='ipv4') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        # This method is the same as the base method except for one place.
        # The class doesn't inherit from the base class, though, so we have
        # to duplicate.
        source = kwargs.pop('source')
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'),
                    afi=afi, source=source)
        redistribute = self._redistribute_builder(afi=afi, source=source)
        config = redistribute(**args)
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            tag = 'redistribute-%s' % source
            config.find('.//*%s' % tag).set('operation', 'delete')
        return callback(config)

    def _redistribute_builder(self, afi='ipv4', source=None):
        """Build BGP redistribute method.

        Do not use this method directly.  You probably want ``redistribute``.

        Args:
            source (str): Source for redistributing. (connected)
            afi (str): Address family to configure. (ipv4, ipv6)

        Returns:
            Method to redistribute desired source.

        Raises:
            KeyError: if `source` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp._redistribute_builder(source='connected',
            ...     afi='ipv4')
            ...     dev.bgp._redistribute_builder(source='hodor',
            ...     afi='ipv4') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        if source == 'connected':
            return getattr(self._rbridge,
                           'rbridge_id_router_router_bgp_address_family_{0}_'
                           '{0}_unicast_default_vrf_af_{0}_uc_and_vrf_cmds_'
                           'call_point_holder_redistribute_connected_'
                           'redistribute_connected'.format(afi))
        # TODO: Add support for 'static' and 'ospf'
        else:
            raise AttributeError('Invalid source.')

    def max_paths(self, **kwargs):
        """Set BGP max paths property.

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
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.max_paths(paths='8',
            ...     rbridge_id='225')
            ...     output = dev.bgp.max_paths(paths='8',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.max_paths(paths='8',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225')
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225', get=True)
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv6',
            ...     rbridge_id='225', delete=True)
            ...     output = dev.bgp.max_paths(paths='8', afi='ipv5',
            ...     rbridge_id='225') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'),
                    load_sharing_value=kwargs.pop('paths', '8'))
        max_paths = getattr(self._rbridge,
                            'rbridge_id_router_router_bgp_address_family_{0}_'
                            '{0}_unicast_default_vrf_af_common_cmds_holder_'
                            'maximum_paths_load_sharing_value'.format(afi))
        config = max_paths(**args)
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            tag = 'maximum-paths'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return callback(config)

    def recursion(self, **kwargs):
        """Set BGP next hop recursion property.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
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
            >>> conn = ('10.24.39.203', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.recursion(rbridge_id='225')
            ...     output = dev.bgp.recursion(rbridge_id='225', get=True)
            ...     output = dev.bgp.recursion(rbridge_id='225', delete=True)
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv6')
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv6',
            ...     get=True)
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv6',
            ...     delete=True)
            ...     output = dev.bgp.max_paths(rbridge_id='225', afi='ipv5')
            ...     # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        args = dict(vrf_name=kwargs.pop('vrf', 'default'),
                    rbridge_id=kwargs.pop('rbridge_id', '1'))

        recursion = getattr(self._rbridge,
                            'rbridge_id_router_router_bgp_address_family_{0}_'
                            '{0}_unicast_default_vrf_next_hop_'
                            'recursion'.format(afi))
        config = recursion(**args)
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            tag = 'next-hop-recursion'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return callback(config)

    def graceful_restart(self, **kwargs):
        """Set BGP next hop recursion property.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
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
            >>> conn = ('10.24.39.212', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp.graceful_restart(rbridge_id='226')
            ...     output = dev.bgp.graceful_restart(rbridge_id='226',
            ...     get=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='226',
            ...     delete=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='226',
            ...     afi='ipv6')
            ...     output = dev.bgp.graceful_restart(rbridge_id='226',
            ...     afi='ipv6', get=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='226',
            ...     afi='ipv6', delete=True)
            ...     output = dev.bgp.graceful_restart(rbridge_id='226',
            ...     afi='ipv5') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
        """
        # TODO: Add support for timers
        afi = kwargs.pop('afi', 'ipv4')
        callback = kwargs.pop('callback', self._callback)
        if afi not in ['ipv4', 'ipv6']:
            raise AttributeError('Invalid AFI.')
        args = dict(rbridge_id=kwargs.pop('rbridge_id', '1'))
        graceful = getattr(self._rbridge,
                           'rbridge_id_router_router_bgp_address_family_{0}_'
                           '{0}_unicast_default_vrf_af_common_cmds_holder_'
                           'graceful_restart_graceful_restart_'
                           'status'.format(afi))
        config = graceful(**args)
        if kwargs.pop('get', False):
            return callback(config, handler='get_config')
        if kwargs.pop('delete', False):
            tag = 'graceful-restart'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return callback(config)

    def _multihop_xml(self, **kwargs):
        """Build BGP multihop XML.

        Do not use this method directly.  You probably want ``multihop``.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            neighbor (ipaddress.ip_interface): `ip_interface` object containing
                peer IP address (IPv4 or IPv6).
            count (str): Number of hops to allow. (1-255)

        Returns:
            ``ElementTree``: XML for configuring BGP multihop.

        Raises:
            KeyError: if any arg is not specified.

        Examples:
            >>> import pynos.device
            >>> from ipaddress import ip_interface
            >>> conn = ('10.24.39.230', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     dev.bgp._multihop_xml(neighbor=ip_interface(unicode(
            ...     '10.10.10.10')), count='5', vrf='default', rbridge_id='1')
            ...     dev.bgp._multihop_xml(
            ...     ip='10.10.10.10') # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_addr = kwargs.pop('neighbor')
        ip = str(ip_addr.ip)
        rbr_ns = 'urn:brocade.com:mgmt:brocade-rbridge'
        bgp_ns = 'urn:brocade.com:mgmt:brocade-bgp'
        config = ET.Element('config')
        ele = ET.SubElement(config, 'rbridge-id', xmlns=rbr_ns)
        ET.SubElement(ele, 'rbridge-id').text = kwargs.pop('rbridge_id')
        ele = ET.SubElement(ele, 'router')
        ele = ET.SubElement(ele, 'router-bgp', xmlns=bgp_ns)
        ele = ET.SubElement(ele, 'router-bgp-attributes')
        ele = ET.SubElement(ele, 'neighbor')
        if ip_addr.version == 4:
            ele = ET.SubElement(ele, 'neighbor-ips')
            ele = ET.SubElement(ele, 'neighbor-addr')
            ET.SubElement(ele, 'router-bgp-neighbor-address').text = ip
        else:
            ele = ET.SubElement(ele, 'neighbor-ipv6s')
            ele = ET.SubElement(ele, 'neighbor-ipv6-addr')
            ET.SubElement(ele, 'router-bgp-neighbor-ipv6-address').text = ip
        ele = ET.SubElement(ele, 'ebgp-multihop')
        ET.SubElement(ele, 'ebgp-multihop-count').text = kwargs.pop('count')
        return config

    def _update_source_xml(self, **kwargs):
        """Build BGP update source XML.

        Do not use this method directly.  You probably want ``update_source``.
        This currently only supports loopback interfaces.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            neighbor (ipaddress.ip_interface): `ip_interface` object containing
                peer IP address (IPv4 or IPv6).
            int_type (str): Interface type (loopback)
            int_name (str): Interface identifier (1, 5, 7, etc)

        Returns:
            ``ElementTree``: XML for configuring BGP update source.

        Raises:
            KeyError: if any arg is not specified.

        Examples:
            >>> import pynos.device
            >>> from ipaddress import ip_interface
            >>> conn = ('10.24.39.230', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.bgp._update_source_xml(neighbor=ip_interface(
            ...     unicode('10.10.10.10')), rbridge_id='1',
            ...     int_type='loopback', int_name='1')
        """
        ip_addr = kwargs.pop('neighbor')
        ip = str(ip_addr.ip)
        rbr_ns = 'urn:brocade.com:mgmt:brocade-rbridge'
        bgp_ns = 'urn:brocade.com:mgmt:brocade-bgp'
        config = ET.Element('config')
        ele = ET.SubElement(config, 'rbridge-id', xmlns=rbr_ns)
        ET.SubElement(ele, 'rbridge-id').text = kwargs.pop('rbridge_id')
        ele = ET.SubElement(ele, 'router')
        ele = ET.SubElement(ele, 'router-bgp', xmlns=bgp_ns)
        ele = ET.SubElement(ele, 'router-bgp-attributes')
        ele = ET.SubElement(ele, 'neighbor')
        if ip_addr.version == 4:
            ele = ET.SubElement(ele, 'neighbor-ips')
            ele = ET.SubElement(ele, 'neighbor-addr')
            ET.SubElement(ele, 'router-bgp-neighbor-address').text = ip
        else:
            ele = ET.SubElement(ele, 'neighbor-ipv6s')
            ele = ET.SubElement(ele, 'neighbor-ipv6-addr')
            ET.SubElement(ele, 'router-bgp-neighbor-ipv6-address').text = ip
        ele = ET.SubElement(ele, 'update-source')
        ET.SubElement(ele, 'loopback').text = kwargs.pop('int_name')
        return config
