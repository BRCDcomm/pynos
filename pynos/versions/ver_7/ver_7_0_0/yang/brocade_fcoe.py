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
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_mode = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-mode")
        fcoe_fabric_mode.text = kwargs.pop('fcoe_fabric_mode')

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
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name.text = kwargs.pop('fcf_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fcf_rbid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fcf_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fcf-rbid")
        fcf_map_fcf_rbid.text = kwargs.pop('fcf_map_fcf_rbid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fif_rbid_fcf_map_fif_rbid_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fif_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fif-rbid")
        fcf_map_fif_rbid_add = ET.SubElement(fcf_map_fif_rbid, "fcf-map-fif-rbid-add")
        fcf_map_fif_rbid_add.text = kwargs.pop('fcf_map_fif_rbid_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fif_rbid_fcf_map_fif_rbid_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fif_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fif-rbid")
        fcf_map_fif_rbid_remove = ET.SubElement(fcf_map_fif_rbid, "fcf-map-fif-rbid-remove")
        fcf_map_fif_rbid_remove.text = kwargs.pop('fcf_map_fif_rbid_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcport_group_config_fcport_group_rbid_fcport_group_rbid_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcport_group_config = ET.SubElement(fcoe_fabric_map, "fcoe-fcport-group-config")
        fcport_group_rbid = ET.SubElement(fcoe_fcport_group_config, "fcport-group-rbid")
        fcport_group_rbid_add = ET.SubElement(fcport_group_rbid, "fcport-group-rbid-add")
        fcport_group_rbid_add.text = kwargs.pop('fcport_group_rbid_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcport_group_config_fcport_group_rbid_fcport_group_rbid_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcport_group_config = ET.SubElement(fcoe_fabric_map, "fcoe-fcport-group-config")
        fcport_group_rbid = ET.SubElement(fcoe_fcport_group_config, "fcport-group-rbid")
        fcport_group_rbid_remove = ET.SubElement(fcport_group_rbid, "fcport-group-rbid-remove")
        fcport_group_rbid_remove.text = kwargs.pop('fcport_group_rbid_remove')

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
        
    def fcoe_fcoe_fabric_map_fcoe_fabric_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fabric_mode = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-mode")
        fcoe_fabric_mode.text = kwargs.pop('fcoe_fabric_mode')

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
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name.text = kwargs.pop('fcf_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fcf_rbid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fcf_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fcf-rbid")
        fcf_map_fcf_rbid.text = kwargs.pop('fcf_map_fcf_rbid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fif_rbid_fcf_map_fif_rbid_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fif_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fif-rbid")
        fcf_map_fif_rbid_add = ET.SubElement(fcf_map_fif_rbid, "fcf-map-fif-rbid-add")
        fcf_map_fif_rbid_add.text = kwargs.pop('fcf_map_fif_rbid_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcf_map_fcf_map_fif_rbid_fcf_map_fif_rbid_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcf_map = ET.SubElement(fcoe_fabric_map, "fcoe-fcf-map")
        fcf_map_name_key = ET.SubElement(fcoe_fcf_map, "fcf-map-name")
        fcf_map_name_key.text = kwargs.pop('fcf_map_name')
        fcf_map_fif_rbid = ET.SubElement(fcoe_fcf_map, "fcf-map-fif-rbid")
        fcf_map_fif_rbid_remove = ET.SubElement(fcf_map_fif_rbid, "fcf-map-fif-rbid-remove")
        fcf_map_fif_rbid_remove.text = kwargs.pop('fcf_map_fif_rbid_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcport_group_config_fcport_group_rbid_fcport_group_rbid_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcport_group_config = ET.SubElement(fcoe_fabric_map, "fcoe-fcport-group-config")
        fcport_group_rbid = ET.SubElement(fcoe_fcport_group_config, "fcport-group-rbid")
        fcport_group_rbid_add = ET.SubElement(fcport_group_rbid, "fcport-group-rbid-add")
        fcport_group_rbid_add.text = kwargs.pop('fcport_group_rbid_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_fcoe_fabric_map_fcoe_fcport_group_config_fcport_group_rbid_fcport_group_rbid_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe = ET.SubElement(config, "fcoe", xmlns="urn:brocade.com:mgmt:brocade-fcoe")
        fcoe_fabric_map = ET.SubElement(fcoe, "fcoe-fabric-map")
        fcoe_fabric_map_name_key = ET.SubElement(fcoe_fabric_map, "fcoe-fabric-map-name")
        fcoe_fabric_map_name_key.text = kwargs.pop('fcoe_fabric_map_name')
        fcoe_fcport_group_config = ET.SubElement(fcoe_fabric_map, "fcoe-fcport-group-config")
        fcport_group_rbid = ET.SubElement(fcoe_fcport_group_config, "fcport-group-rbid")
        fcport_group_rbid_remove = ET.SubElement(fcport_group_rbid, "fcport-group-rbid-remove")
        fcport_group_rbid_remove.text = kwargs.pop('fcport_group_rbid_remove')

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
        