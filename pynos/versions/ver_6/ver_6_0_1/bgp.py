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
import pynos.utilities
from pynos.versions.base.bgp import BGP as BaseBGP


class BGP(BaseBGP):
    """
    The BGP class holds all relevent methods and attributes for the BGP
    capabilities of the NOS device.

    Attributes:
        None
    """
    def setup_bgp(self, **kwargs):
        """Set initial BGP state on NOS device.

        This action is required first to initiate the BGP process on a NOS
        device.

        Args:
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
            >>> import pynos
            >>> conn = ('10.10.1.1', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn, auth)
            >>> output = dev.bgp.setup_bgp(
            ... callback=pynos.utilities.print_xml_string)
            <config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">\
            <rbridge-id>1</rbridge-id><router>\
            <bgp xmlns="urn:brocade.com:mgmt:brocade-bgp">\
            </bgp></router></rbridge-id></config>
            >>> dev.bgp.setup_bgp()
            True

        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        ret = kwargs.pop('ret', False)

        config = ET.Element('config')
        rbridge = ET.SubElement(config, 'rbridge-id',
                                xmlns='urn:brocade.com:mgmt:brocade-rbridge')
        rbridge_id_el = ET.SubElement(rbridge, 'rbridge-id')
        rbridge_id_el.text = str(rbridge_id)

        router = ET.SubElement(rbridge, 'router')
        ET.SubElement(router, 'router-bgp',
                      xmlns='urn:brocade.com:mgmt:brocade-bgp')

        if ret is True:
            return config
        try:
            return callback(config)
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)

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
            >>> import pynos
            >>> conn = ('10.10.1.1', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn, auth)
            >>> output = dev.bgp.local_asn(local_as='65535',
            ... callback=pynos.utilities.print_xml_string)
            <config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">\
            <rbridge-id>1</rbridge-id><router>\
            <bgp xmlns="urn:brocade.com:mgmt:brocade-bgp">\
            <router-bgp-attributes><local-as>65535</local-as>\
            </router-bgp-attributes></bgp></router>\
            </rbridge-id></config>
            >>> dev.bgp.local_asn(local_as='65535')
            True
            >>> dev.bgp.local_asn() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError

        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        local_as = kwargs.pop('local_as')
        callback = kwargs.pop('callback', self._callback)

        config = self.setup_bgp(rbridge_id=rbridge_id,
                                callback=pynos.utilities.return_xml)
        bgp = config.find('rbridge-id').find('router').find('router-bgp')
        bgp_attr = ET.SubElement(bgp, 'router-bgp-attributes')
        asn = ET.SubElement(bgp_attr, 'local-as')
        asn.text = str(local_as)

        try:
            return callback(config)
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)

    def remove_bgp(self, **kwargs):
        """Remove BGP process completely.

        Args:
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
            >>> import pynos
            >>> conn = ('10.10.1.1', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn, auth)
            >>> output = dev.bgp.remove_bgp(
            ... callback=pynos.utilities.print_xml_string)
            <config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">\
            <rbridge-id>1</rbridge-id><router>\
            <bgp xmlns="urn:brocade.com:mgmt:brocade-bgp" operation="delete">\
            </bgp></router></rbridge-id></config>
            >>> dev.bgp.remove_bgp()
            True

        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        config = ET.Element('config')
        callback = kwargs.pop('callback', self._callback)

        rbridge = ET.SubElement(config, 'rbridge-id',
                                xmlns='urn:brocade.com:mgmt:brocade-rbridge')
        rbridge_id_el = ET.SubElement(rbridge, 'rbridge-id')
        rbridge_id_el.text = str(rbridge_id)
        router = ET.SubElement(rbridge, 'router')
        ET.SubElement(router, 'router-bgp',
                      xmlns='urn:brocade.com:mgmt:brocade-bgp',
                      operation='delete')

        try:
            return callback(config)
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)

    def add_neighbor(self, **kwargs):
        """Add BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
            remote_as (str): Remote ASN of BGP neighbor.
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
            >>> import pynos
            >>> conn = ('10.10.1.1', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn, auth)
            >>> output = dev.bgp.add_neighbor(ip_addr='10.10.10.10',
            ... remote_as='65535', callback=pynos.utilities.print_xml_string)
            <config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">\
            <rbridge-id>1</rbridge-id><router>\
            <bgp xmlns="urn:brocade.com:mgmt:brocade-bgp">\
            <router-bgp-attributes><neighbor><neighbor-ips><neighbor-addr>\
            <router-bgp-neighbor-address>10.10.10.10\
            </router-bgp-neighbor-address><remote-as>65535</remote-as>\
            </neighbor-addr></neighbor-ips></neighbor>\
            </router-bgp-attributes></bgp></router>\
            </rbridge-id></config>
            >>> dev.bgp.add_neighbor(ip_addr='10.10.10.10', remote_as='65535')
            True
            >>> dev.bgp.add_neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError

        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        ip_addr = kwargs.pop('ip_addr')
        remote_as = kwargs.pop('remote_as')
        callback = kwargs.pop('callback', self._callback)

        config = self.setup_bgp(rbridge_id=rbridge_id,
                                callback=pynos.utilities.return_xml)
        bgp = config.find('rbridge-id').find('router').find('router-bgp')
        bgp_attr = ET.SubElement(bgp, 'router-bgp-attributes')
        bgp_neighbor = ET.SubElement(bgp_attr, 'neighbor')
        neighbor_ips = ET.SubElement(bgp_neighbor, 'neighbor-ips')
        neighbor_addr = ET.SubElement(neighbor_ips, 'neighbor-addr')
        neighbor_ip = ET.SubElement(neighbor_addr,
                                    'router-bgp-neighbor-address')
        neighbor_ip.text = ip_addr
        neighbor_asn = ET.SubElement(neighbor_addr, 'remote-as')
        neighbor_asn.text = remote_as

        try:
            return callback(config)
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)

    def remove_neighbor(self, **kwargs):
        """Remove BGP neighbor.

        Args:
            ip_addr (str): IP Address of BGP neighbor.
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
            >>> import pynos
            >>> conn = ('10.10.1.1', '22')
            >>> auth = ('admin', 'password')
            >>> dev = pynos.device.Device(conn, auth)
            >>> output = dev.bgp.remove_neighbor(ip_addr='10.10.10.10',
            ... callback=pynos.utilities.print_xml_string)
            <config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">\
            <rbridge-id>1</rbridge-id><router>\
            <bgp xmlns="urn:brocade.com:mgmt:brocade-bgp">\
            <router-bgp-attributes><neighbor><neighbor-ips>\
            <neighbor-addr operation="delete">\
            <router-bgp-neighbor-address>10.10.10.10\
            </router-bgp-neighbor-address></neighbor-addr></neighbor-ips>\
            </neighbor></router-bgp-attributes></bgp>\
            </router></rbridge-id></config>
            >>> dev.bgp.remove_neighbor(ip_addr='10.10.10.10')
            True
            >>> dev.bgp.remove_neighbor() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError

        """
        rbridge_id = kwargs.pop('rbridge_id', '1')
        ip_addr = kwargs.pop('ip_addr')
        callback = kwargs.pop('callback', self._callback)

        config = self.setup_bgp(rbridge_id=rbridge_id,
                                callback=pynos.utilities.return_xml)
        bgp = config.find('rbridge-id').find('router').find('router-bgp')
        bgp_attr = ET.SubElement(bgp, 'router-bgp-attributes')
        bgp_neighbor = ET.SubElement(bgp_attr, 'neighbor')
        neighbor_ips = ET.SubElement(bgp_neighbor, 'neighbor-ips')
        neighbor_addr = ET.SubElement(neighbor_ips, 'neighbor-addr',
                                      operation='delete')
        neighbor_ip = ET.SubElement(neighbor_addr,
                                    'router-bgp-neighbor-address')
        neighbor_ip.text = ip_addr

        try:
            return callback(config)
        # TODO add logging and narrow exception window.
        except Exception as error:
            logging.error(error)
