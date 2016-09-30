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

from pynos.versions.base.yang.brocade_vcs import brocade_vcs
from ipaddress import ip_interface


class VCS(object):
    """
    VCS class containing all VCS methods and attributes.
    """

    def __init__(self, callback):
        """VCS init method.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            VCS Object
        Raises:
            None
        """
        self._callback = callback
        self._vcs = brocade_vcs(
            callback=pynos.utilities.return_xml
        )

    @property
    def vcs_nodes(self):
        """dict: vcs node details
        """
        urn = "{urn:brocade.com:mgmt:brocade-vcs}"
        namespace = 'urn:brocade.com:mgmt:brocade-vcs'
        show_vcs = ET.Element('show-vcs', xmlns=namespace)
        results = self._callback(show_vcs, handler='get')
        result = []
        for nodes in results.findall('%svcs-nodes' % urn):
            for item in nodes.findall('%svcs-node-info' % urn):
                serial_number = item.find('%snode-serial-num' % urn).text
                node_status = item.find('%snode-status' % urn).text
                vcs_id = item.find('%snode-vcs-id' % urn).text
                rbridge_id = item.find('%snode-rbridge-id' % urn).text
                switch_mac = item.find('%snode-switch-mac' % urn).text
                switch_wwn = item.find('%snode-switch-wwn' % urn).text
                switch_name = item.find('%snode-switchname' % urn).text
                node_is_principal = item.find('%snode-is-principal' % urn).text
                switch_ip = ''
                for switch_ip_addr in item.findall(
                        '%snode-public-ip-addresses' % urn):
                    switch_ip = switch_ip_addr.find(
                        '%snode-public-ip-address' % urn).text
                    break
                item_results = {'node-serial-num': serial_number,
                                'node-status': node_status,
                                'node-vcs-id': vcs_id,
                                'node-rbridge-id': rbridge_id,
                                'node-switch-mac': switch_mac,
                                'node-switch-wwn': switch_wwn,
                                'node-switch-ip': switch_ip,
                                'node-switchname': switch_name,
                                'node-is-principal': node_is_principal}

                result.append(item_results)

        return result

    def vcs_vip(self, **kwargs):
        """Set VCS Virtual IP.
        Args:
            vip (str): IPv4/IPv6 Virtual IP Address.
            rbridge_id (str): rbridge-id for device. Only required when type is
                `ve`.
            delete (bool): Deletes the virtual ip if `delete` is ``True``.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            KeyError: if `vip` is not passed.
            ValueError: if `vip` is invalid.
        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.211', '10.24.39.203']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...     conn = (switch, '22')
            ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24')
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64')
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24',delete=True)
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64',
            ...                               delete=True)
            ...         dev.interface.vcs_vip(vip='10.1.1.1/24',get=True)
            ...         dev.interface.vcs_vip(vip='fe80::cafe:beef:1000:1/64',
            ...                               get=True)
        """

        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        method_class = self._vcs

        if not get_config:
            vip = str(kwargs.pop('vip'))
            ipaddress = ip_interface(unicode(vip))
            vcs_vip = None

            if ipaddress.version == 4:
                method_name = 'vcs_virtual_ip_address_address'
                vcs_args = dict(address=vip)
                vcs_vip = getattr(method_class, method_name)
            elif ipaddress.version == 6:
                method_name = 'vcs_virtual_ipv6_address_ipv6address'
                vcs_args = dict(ipv6address=vip)
                vcs_vip = getattr(method_class, method_name)

            if not delete:
                config = vcs_vip(**vcs_args)
            else:
                if ipaddress.version == 4:
                    config = vcs_vip(**vcs_args)
                    config.find('.//*address').set('operation', 'delete')
                elif ipaddress.version == 6:
                    config = vcs_vip(**vcs_args)
                    config.find('.//*ipv6address').set('operation', 'delete')
        elif get_config:
            vip_info = {}

            method_name = 'vcs_virtual_ip_address_address'
            vcs_args = dict(address='')
            vcs_vip = getattr(method_class, method_name)
            config = vcs_vip(**vcs_args)
            vip_info['ipv4_vip'] = callback(config, handler='get_config')

            method_name = 'vcs_virtual_ipv6_address_ipv6address'
            vcs_args = dict(ipv6address='')
            vcs_vip = getattr(method_class, method_name)
            config = vcs_vip(**vcs_args)
            vip_info['ipv6_vip'] = callback(config, handler='get_config')
            return vip_info

        return callback(config)
