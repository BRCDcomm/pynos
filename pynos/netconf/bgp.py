#!/usr/bin/env python
'''
NetCONF serilization of BGP actions for Brocade NOS devices.
'''
import xml.etree.ElementTree as ET

class BGP(object):
    '''
    BGP Class
    '''
    def __init__(self, callback):
        self._callback = callback

    def setup_bgp(self, vrf='default', rbridge_id='1', ret=False):
        '''
        Set BGP attributes
        '''
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
        self._callback(config)

    def local_asn(self, local_as, vrf='default', rbridge_id='1'):
        '''
        Set BGP attributes
        '''
        config = self.setup_bgp(vrf, rbridge_id, True)
        bgp = config.find('rbridge-id').find('router').find('bgp')
        bgp_cmds = ET.SubElement(bgp, 'router-bgp-cmds-holder')
        bgp_attr = ET.SubElement(bgp_cmds, 'router-bgp-attributes')
        asn = ET.SubElement(bgp_attr, 'local-as')
        asn.text = str(local_as)

        self._callback(config)

    def remove_bgp(self, vrf='default', rbridge_id='1'):
        '''
        Remove BGP Config
        '''
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
        self._callback(config)

    def add_neighbor(self, ip_addr, remote_as, vrf='default', rbridge_id='1'):
        '''
        Add BGP neighbor.
        '''
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

        self._callback(config)

    def remove_neighbor(self, ip_addr, vrf='default', rbridge_id='1'):
        '''
        Remove BGP neighbor

        Parameters:
            ip_: IP Address of neighbor
        '''
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

        self._callback(config)
