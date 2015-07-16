#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_cee_map(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def cee_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name = ET.SubElement(cee_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_precedence(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        precedence = ET.SubElement(cee_map, "precedence")
        precedence.text = kwargs.pop('precedence')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_PGID(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        PGID = ET.SubElement(priority_group_table, "PGID")
        PGID.text = kwargs.pop('PGID')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_weight(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        PGID_key = ET.SubElement(priority_group_table, "PGID")
        PGID_key.text = kwargs.pop('PGID')
        weight = ET.SubElement(priority_group_table, "weight")
        weight.text = kwargs.pop('weight')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_pfc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        PGID_key = ET.SubElement(priority_group_table, "PGID")
        PGID_key.text = kwargs.pop('PGID')
        pfc = ET.SubElement(priority_group_table, "pfc")
        pfc.text = kwargs.pop('pfc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos0_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos0_pgid = ET.SubElement(priority_table, "map-cos0-pgid")
        map_cos0_pgid.text = kwargs.pop('map_cos0_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos1_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos1_pgid = ET.SubElement(priority_table, "map-cos1-pgid")
        map_cos1_pgid.text = kwargs.pop('map_cos1_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos2_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos2_pgid = ET.SubElement(priority_table, "map-cos2-pgid")
        map_cos2_pgid.text = kwargs.pop('map_cos2_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos3_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos3_pgid = ET.SubElement(priority_table, "map-cos3-pgid")
        map_cos3_pgid.text = kwargs.pop('map_cos3_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos4_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos4_pgid = ET.SubElement(priority_table, "map-cos4-pgid")
        map_cos4_pgid.text = kwargs.pop('map_cos4_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos5_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos5_pgid = ET.SubElement(priority_table, "map-cos5-pgid")
        map_cos5_pgid.text = kwargs.pop('map_cos5_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos6_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos6_pgid = ET.SubElement(priority_table, "map-cos6-pgid")
        map_cos6_pgid.text = kwargs.pop('map_cos6_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos7_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos7_pgid = ET.SubElement(priority_table, "map-cos7-pgid")
        map_cos7_pgid.text = kwargs.pop('map_cos7_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_remap_fabric_priority_fabric_remapped_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        remap = ET.SubElement(cee_map, "remap")
        fabric_priority = ET.SubElement(remap, "fabric-priority")
        fabric_remapped_priority = ET.SubElement(fabric_priority, "fabric-remapped-priority")
        fabric_remapped_priority.text = kwargs.pop('fabric_remapped_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_remap_lossless_priority_lossless_remapped_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        remap = ET.SubElement(cee_map, "remap")
        lossless_priority = ET.SubElement(remap, "lossless-priority")
        lossless_remapped_priority = ET.SubElement(lossless_priority, "lossless-remapped-priority")
        lossless_remapped_priority.text = kwargs.pop('lossless_remapped_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name = ET.SubElement(cee_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_precedence(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        precedence = ET.SubElement(cee_map, "precedence")
        precedence.text = kwargs.pop('precedence')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_PGID(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        PGID = ET.SubElement(priority_group_table, "PGID")
        PGID.text = kwargs.pop('PGID')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_weight(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        PGID_key = ET.SubElement(priority_group_table, "PGID")
        PGID_key.text = kwargs.pop('PGID')
        weight = ET.SubElement(priority_group_table, "weight")
        weight.text = kwargs.pop('weight')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_group_table_pfc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_group_table = ET.SubElement(cee_map, "priority-group-table")
        PGID_key = ET.SubElement(priority_group_table, "PGID")
        PGID_key.text = kwargs.pop('PGID')
        pfc = ET.SubElement(priority_group_table, "pfc")
        pfc.text = kwargs.pop('pfc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos0_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos0_pgid = ET.SubElement(priority_table, "map-cos0-pgid")
        map_cos0_pgid.text = kwargs.pop('map_cos0_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos1_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos1_pgid = ET.SubElement(priority_table, "map-cos1-pgid")
        map_cos1_pgid.text = kwargs.pop('map_cos1_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos2_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos2_pgid = ET.SubElement(priority_table, "map-cos2-pgid")
        map_cos2_pgid.text = kwargs.pop('map_cos2_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos3_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos3_pgid = ET.SubElement(priority_table, "map-cos3-pgid")
        map_cos3_pgid.text = kwargs.pop('map_cos3_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos4_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos4_pgid = ET.SubElement(priority_table, "map-cos4-pgid")
        map_cos4_pgid.text = kwargs.pop('map_cos4_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos5_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos5_pgid = ET.SubElement(priority_table, "map-cos5-pgid")
        map_cos5_pgid.text = kwargs.pop('map_cos5_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos6_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos6_pgid = ET.SubElement(priority_table, "map-cos6-pgid")
        map_cos6_pgid.text = kwargs.pop('map_cos6_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_priority_table_map_cos7_pgid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        priority_table = ET.SubElement(cee_map, "priority-table")
        map_cos7_pgid = ET.SubElement(priority_table, "map-cos7-pgid")
        map_cos7_pgid.text = kwargs.pop('map_cos7_pgid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_remap_fabric_priority_fabric_remapped_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        remap = ET.SubElement(cee_map, "remap")
        fabric_priority = ET.SubElement(remap, "fabric-priority")
        fabric_remapped_priority = ET.SubElement(fabric_priority, "fabric-remapped-priority")
        fabric_remapped_priority.text = kwargs.pop('fabric_remapped_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cee_map_remap_lossless_priority_lossless_remapped_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cee_map = ET.SubElement(config, "cee-map", xmlns="urn:brocade.com:mgmt:brocade-cee-map")
        name_key = ET.SubElement(cee_map, "name")
        name_key.text = kwargs.pop('name')
        remap = ET.SubElement(cee_map, "remap")
        lossless_priority = ET.SubElement(remap, "lossless-priority")
        lossless_remapped_priority = ET.SubElement(lossless_priority, "lossless-remapped-priority")
        lossless_remapped_priority.text = kwargs.pop('lossless_remapped_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        