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

import xml.etree.ElementTree as ET

import pynos.utilities
from pynos.versions.base.yang.brocade_rbridge import brocade_rbridge


class Services(object):
    """
    The Services class holds all relevent methods and attributes for enabling
    and disabling NOS services, such as VRRP.

    Attributes:
        None
    """
    def __init__(self, callback):
        """
        Services object init.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            Services Object

        Raises:
            None
        """
        self._callback = callback
        self._rbridge = brocade_rbridge(callback=pynos.utilities.return_xml)

    @property
    def arp(self):
        """dict: trill link details
                """
        xmlns = 'urn:brocade.com:mgmt:brocade-arp'
        get_arp_info = ET.Element('get-arp', xmlns=xmlns)
        results = self._callback(get_arp_info, handler='get')
        result = []
        for item in results.findall('{%s}arp-entry' % xmlns):
            ip_address = item.find('{%s}ip-address' % xmlns).text
            mac_address = item.find('{%s}mac-address' % xmlns).text
            interface_type = item.find('{%s}interface-type' % xmlns).text
            interface_name = item.find('{%s}interface-name' % xmlns).text
            is_resolved = item.find('{%s}is-resolved' % xmlns).text
            age = item.find('{%s}age' % xmlns).text
            entry_type = item.find('{%s}entry-type' % xmlns).text
            item_results = {'ip-address': ip_address,
                            'mac-address': mac_address,
                            'interface-type': interface_type,
                            'interface-name': interface_name,
                            'is-resolved': is_resolved,
                            'age': age,
                            'entry-type': entry_type
                            }
            result.append(item_results)
        return result

    def vrrp(self, **kwargs):
        """Enable or Disable VRRP.

        Args:
            ip_version (str): The IP version ('4' or '6') for which VRRP should
                be enabled/disabled.  Default: `4`.
            enabled (bool): If VRRP should be enabled or disabled.  Default:
                ``True``.
            rbridge_id (str): The rbridge ID of the device on which VRRP will
                be enabled/disabled.  Default: `1`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            None

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         output = dev.bgp.local_asn(rbridge_id='225')
            ...         output = dev.bgp.local_asn(rbridge_id='225',
            ...         enabled=False)
            ...         output = dev.bgp.local_asn(rbridge_id='225',
            ...         ip_version='6')
            ...         output = dev.bgp.local_asn(rbridge_id='225',
            ...         enabled=False, ip_version='6')
            ...         dev.services.vrrp() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        ip_version = kwargs.pop('ip_version', '4')
        enabled = kwargs.pop('enabled', True)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        vrrp_args = dict(rbridge_id=rbridge_id)
        vrrp_method = 'rbridge_id_protocol_hide_vrrp_holder_vrrp'
        if ip_version == '6':
            vrrp_method = 'rbridge_id_ipv6_proto_vrrpv3_vrrp'
        vrrp = getattr(self._rbridge, vrrp_method)
        config = vrrp(**vrrp_args)
        if not enabled:
            config.find('.//*vrrp').set('operation', 'delete')
        return callback(config)

    def vrrpe(self, **kwargs):
        """Enable or Disable Vrrpe.
        Args:
            ip_version (str): The IP version ('4' or '6') for which vrrpe
                should be enabled/disabled.  Default: `4`.
            enable (bool): If vrrpe should be enabled or disabled.  Default:
                ``True``.
            get (bool): Get config instead of editing config. (True, False)
            rbridge_id (str): The rbridge ID of the device on which vrrpe will
                be enabled/disabled.  Default: `1`.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.services.vrrpe(rbridge_id='25',enable=False)
            ...         dev.services.vrrpe(rbridge_id='25',enable=True)
            ...         dev.services.vrrpe()
            Traceback (most recent call last):
            KeyError
        """
        ip_version = kwargs.pop('ip_version', '4')
        enable = kwargs.pop('enable', True)
        get = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        if get:
            enable = None
        vrrpe_args = dict(rbridge_id=rbridge_id)
        vrrpe_method = 'rbridge_id_protocol_hide_vrrp_holder_vrrp_extended'
        if ip_version == '6':
            vrrpe_method = 'rbridge_id_ipv6_proto_vrrpv3_vrrp_extended'
        vrrpe = getattr(self._rbridge, vrrpe_method)
        config = vrrpe(**vrrpe_args)
        if get:
            return callback(config, handler='get_config')
        if not enable:
            config.find('.//*vrrp-extended').set('operation', 'delete')
        return callback(config)
