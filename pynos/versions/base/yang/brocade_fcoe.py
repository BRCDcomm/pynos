#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fcoe(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def fcoe_fsb_fcoe_fsb_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_fsb = ET.SubElement(config, "fcoe-fsb", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fsb_enable = ET.SubElement(fcoe_fsb, "fcoe-fsb-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name.text = kwargs.pop('fcoe_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_vlan = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-vlan")
        fcoe_fabric_map_vlan.text = kwargs.pop('fcoe_fabric_map_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_priority = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-priority")
        fcoe_fabric_map_priority.text = kwargs.pop('fcoe_fabric_map_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_virtual_fabric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_virtual_fabric = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-virtual-fabric")
        fcoe_fabric_map_virtual_fabric.text = kwargs.pop('fcoe_fabric_map_virtual_fabric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_fcmap(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_fcmap = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-fcmap")
        fcoe_fabric_map_fcmap.text = kwargs.pop('fcoe_fabric_map_fcmap')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fip_advertisement_fcoe_fip_advertisement_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fip_advertisement = ET.SubElement(fcoe_fabric_map, "fcoe-fip-advertisement")
        fcoe_fip_advertisement_interval = ET.SubElement(fcoe_fip_advertisement, "fcoe-fip-advertisement-interval")
        fcoe_fip_advertisement_interval.text = kwargs.pop('fcoe_fip_advertisement_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fip_keep_alive_fcoe_fip_keep_alive_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fip_keep_alive = ET.SubElement(fcoe_fabric_map, "fcoe-fip-keep-alive")
        fcoe_fip_keep_alive_timeout = ET.SubElement(fcoe_fip_keep_alive, "fcoe-fip-keep-alive-timeout")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        fcoe_map_name = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name.text = kwargs.pop('fcoe_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_fabric_map_fcoe_map_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        fcoe_map_name_key = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name_key.text = kwargs.pop('fcoe_map_name')
        fcoe_map_fabric_map = ET.SubElement(fcoe_map, "fcoe-map-fabric-map")
        fcoe_map_fabric_map_name = ET.SubElement(fcoe_map_fabric_map, "fcoe-map-fabric-map-name")
        fcoe_map_fabric_map_name.text = kwargs.pop('fcoe_map_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_cee_map_fcoe_map_cee_map_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        fcoe_map_name_key = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name_key.text = kwargs.pop('fcoe_map_name')
        fcoe_map_cee_map = ET.SubElement(fcoe_map, "fcoe-map-cee-map")
        fcoe_map_cee_map_leaf = ET.SubElement(fcoe_map_cee_map, "fcoe-map-cee-map-leaf")
        fcoe_map_cee_map_leaf.text = kwargs.pop('fcoe_map_cee_map_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fcf_map_fcf_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fcf_map = ET.SubElement(fcoe, "fcoe-fcf-map")
        fcf_map_name = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name.text = kwargs.pop('fcf_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fcf_map_fcf_map_fcoe_map_fcf_map_fcoe_map_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fcf_map = ET.SubElement(fcoe, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fcoe_map = ET.SubElement(fcoe_fcf_map, "fcf-map-fcoe-map")
        fcf_map_fcoe_map_leaf = ET.SubElement(fcf_map_fcoe_map, "fcf-map-fcoe-map-leaf")
        fcf_map_fcoe_map_leaf.text = kwargs.pop('fcf_map_fcoe_map_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fcf_map_fcf_map_ag_rbid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fcf_map = ET.SubElement(fcoe, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_ag_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-ag-rbid")
        fcf_map_ag_rbid.text = kwargs.pop('fcf_map_ag_rbid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fsb_fcoe_fsb_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_fsb = ET.SubElement(config, "fcoe-fsb", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fsb_enable = ET.SubElement(fcoe_fsb, "fcoe-fsb-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name.text = kwargs.pop('fcoe_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_vlan = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-vlan")
        fcoe_fabric_map_vlan.text = kwargs.pop('fcoe_fabric_map_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_priority = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-priority")
        fcoe_fabric_map_priority.text = kwargs.pop('fcoe_fabric_map_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_virtual_fabric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_virtual_fabric = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-virtual-fabric")
        fcoe_fabric_map_virtual_fabric.text = kwargs.pop('fcoe_fabric_map_virtual_fabric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_map_fcmap(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_map_fcmap = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-fcmap")
        fcoe_fabric_map_fcmap.text = kwargs.pop('fcoe_fabric_map_fcmap')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fip_advertisement_fcoe_fip_advertisement_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fip_advertisement = ET.SubElement(fcoe_fabric_map, "fcoe-fip-advertisement")
        fcoe_fip_advertisement_interval = ET.SubElement(fcoe_fip_advertisement, "fcoe-fip-advertisement-interval")
        fcoe_fip_advertisement_interval.text = kwargs.pop('fcoe_fip_advertisement_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fip_keep_alive_fcoe_fip_keep_alive_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fip_keep_alive = ET.SubElement(fcoe_fabric_map, "fcoe-fip-keep-alive")
        fcoe_fip_keep_alive_timeout = ET.SubElement(fcoe_fip_keep_alive, "fcoe-fip-keep-alive-timeout")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        fcoe_map_name = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name.text = kwargs.pop('fcoe_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_fabric_map_fcoe_map_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        fcoe_map_name_key = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name_key.text = kwargs.pop('fcoe_map_name')
        fcoe_map_fabric_map = ET.SubElement(fcoe_map, "fcoe-map-fabric-map")
        fcoe_map_fabric_map_name = ET.SubElement(fcoe_map_fabric_map, "fcoe-map-fabric-map-name")
        fcoe_map_fabric_map_name.text = kwargs.pop('fcoe_map_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_map_fcoe_map_cee_map_fcoe_map_cee_map_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_map = ET.SubElement(fcoe, "fcoe-map")
        fcoe_map_name_key = ET.SubElement(fcoe_map, "fcoe-map-name")
        fcoe_map_name_key.text = kwargs.pop('fcoe_map_name')
        fcoe_map_cee_map = ET.SubElement(fcoe_map, "fcoe-map-cee-map")
        fcoe_map_cee_map_leaf = ET.SubElement(fcoe_map_cee_map, "fcoe-map-cee-map-leaf")
        fcoe_map_cee_map_leaf.text = kwargs.pop('fcoe_map_cee_map_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fcf_map_fcf_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fcf_map = ET.SubElement(fcoe, "fcoe-fcf-map")
        fcf_map_name = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name.text = kwargs.pop('fcf_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fcf_map_fcf_map_fcoe_map_fcf_map_fcoe_map_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fcf_map = ET.SubElement(fcoe, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fcoe_map = ET.SubElement(fcoe_fcf_map, "fcf-map-fcoe-map")
        fcf_map_fcoe_map_leaf = ET.SubElement(fcf_map_fcoe_map, "fcf-map-fcoe-map-leaf")
        fcf_map_fcoe_map_leaf.text = kwargs.pop('fcf_map_fcoe_map_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fcf_map_fcf_map_ag_rbid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fcf_map = ET.SubElement(fcoe, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_ag_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-ag-rbid")
        fcf_map_ag_rbid.text = kwargs.pop('fcf_map_ag_rbid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        