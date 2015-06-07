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

    def setup_bgp(self, vrf='default', rbridge_id='1', ret=False):
        """
        Set initial BGP state on NOS device. This action is required first to
        initiate the BGP process on a NOS device.

        Args:
            vrf: The VRF for this BGP process.
            rbridge_id: The rbridge ID of the device BGP will be set up on in a
                VCS fabric.
            ret: Bool of if the method should return the text or call the
                callback function.

        Returns:
            Element Tree object if ret is set to True. If ret is set to True it
            will return a bool. True if command completes successfully or False
            if not.

        Raises:
            None
        """
        config = ET.Element('config')
        rbridge = ET.SubElement(config, 'rbridge-id',
                                xmlns="urn:brocade.com:mgmt:brocade-rbridge")
        rbridge_id_el = ET.SubElement(rbridge, 'rbridge-id')
        rbridge_id_el.text = str(rbridge_id)

        router = ET.SubElement(rbridge, 'router')
        bgp = ET.SubElement(router, 'bgp',
                            xmlns="urn:brocade.com:mgmt:brocade-bgp")
        vrf_el = ET.SubElement(bgp, 'vrf-name')
        vrf_el.text = vrf

        if ret == True:
            return config
        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def local_asn(self, local_as, vrf='default', rbridge_id='1'):
        """
        Set BGP local ASN.

        Args:
            local_as: Local ASN of NOS deice.
            vrf: The VRF for this BGP process.
            rbridge_id: The rbridge ID of the device BGP will be set up on in a
                VCS fabric.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = self.setup_bgp(vrf, rbridge_id, True)
        bgp = config.find('rbridge-id').find('router').find('bgp')
        bgp_cmds = ET.SubElement(bgp, 'router-bgp-cmds-holder')
        bgp_attr = ET.SubElement(bgp_cmds, 'router-bgp-attributes')
        asn = ET.SubElement(bgp_attr, 'local-as')
        asn.text = str(local_as)

        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def remove_bgp(self, vrf='default', rbridge_id='1'):
        """
        Remove BGP process completely.

        Args:
            vrf: The VRF for this BGP process.
            rbridge_id: The rbridge ID of the device BGP will be set up on in a
                VCS fabric.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = ET.Element('config')
        rbridge = ET.SubElement(config, 'rbridge-id',
                                xmlns="urn:brocade.com:mgmt:brocade-rbridge")
        rbridge_id_el = ET.SubElement(rbridge, 'rbridge-id')
        rbridge_id_el.text = str(rbridge_id)
        router = ET.SubElement(rbridge, 'router')
        bgp = ET.SubElement(router, 'bgp',
                            xmlns="urn:brocade.com:mgmt:brocade-bgp",
                            operation='delete')
        vrf_el = ET.SubElement(bgp, 'vrf-name')
        vrf_el.text = vrf
        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def add_neighbor(self, ip_addr, remote_as, vrf='default', rbridge_id='1'):
        """
        Add BGP neighbor.

        Args:
            ip_addr: IP Address of BGP neighbor.
            remote_as: Remote ASN of BGP neighbor.
            vrf: The VRF for this BGP process.
            rbridge_id: The rbridge ID of the device BGP will be set up on in a
                VCS fabric.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = self.setup_bgp(vrf, rbridge_id, True)
        bgp = config.find('rbridge-id').find('router').find('bgp')
        bgp_cmds = ET.SubElement(bgp, 'router-bgp-cmds-holder')
        bgp_attr = ET.SubElement(bgp_cmds, 'router-bgp-attributes')
        bgp_neighbor = ET.SubElement(bgp_attr, 'neighbor')
        neighbor_ips = ET.SubElement(bgp_neighbor, 'neighbor-ips')
        neighbor_addr = ET.SubElement(neighbor_ips, 'neighbor-addr')
        neighbor_ip = ET.SubElement(neighbor_addr,
                                    'router-bgp-neighbor-address')
        neighbor_ip.text = ip_addr
        neighbor_asn = ET.SubElement(neighbor_addr, 'remote-as')
        neighbor_asn.text = remote_as

        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False

    def remove_neighbor(self, ip_addr, vrf='default', rbridge_id='1'):
        """
        Remove BGP neighbor.

        Args:
            ip_addr: IP Address of BGP neighbor.
            vrf: The VRF for this BGP process.
            rbridge_id: The rbridge ID of the device BGP will be set up on in a
                VCS fabric.

        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """
        config = self.setup_bgp(vrf, rbridge_id, True)
        bgp = config.find('rbridge-id').find('router').find('bgp')
        bgp_cmds = ET.SubElement(bgp, 'router-bgp-cmds-holder')
        bgp_attr = ET.SubElement(bgp_cmds, 'router-bgp-attributes')
        bgp_neighbor = ET.SubElement(bgp_attr, 'neighbor')
        neighbor_ips = ET.SubElement(bgp_neighbor, 'neighbor-ips')
        neighbor_addr = ET.SubElement(neighbor_ips, 'neighbor-addr',
                                      operation='delete')
        neighbor_ip = ET.SubElement(neighbor_addr,
                                    'router-bgp-neighbor-address')
        neighbor_ip.text = ip_addr

        try:
            self._callback(config)
            return True
        #TODO add logging and narrow exception window.
        except Exception, _:
            return False
