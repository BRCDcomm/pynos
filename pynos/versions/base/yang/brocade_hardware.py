#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_hardware(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hardware_connector_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name = ET.SubElement(connector, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_sfp_breakout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name_key = ET.SubElement(connector, "name")
        name_key.text = kwargs.pop('name')
        sfp = ET.SubElement(connector, "sfp")
        breakout = ET.SubElement(sfp, "breakout")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name = ET.SubElement(port_group, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_performance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        mode = ET.SubElement(port_group, "mode")
        performance = ET.SubElement(mode, "performance")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id = ET.SubElement(connector_group, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id_key = ET.SubElement(connector_group, "id")
        id_key.text = kwargs.pop('id')
        speed = ET.SubElement(connector_group, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id = ET.SubElement(flexport, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        type = ET.SubElement(flexport_type, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        instance = ET.SubElement(flexport_type, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_skip_deconfig(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        skip_deconfig = ET.SubElement(flexport_type, "skip_deconfig")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_flexports_output_flexport_list_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_flexports = ET.Element("get_flexports")
        config = get_flexports
        output = ET.SubElement(get_flexports, "output")
        flexport_list = ET.SubElement(output, "flexport-list")
        port_id = ET.SubElement(flexport_list, "port-id")
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name = ET.SubElement(connector, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_sfp_breakout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name_key = ET.SubElement(connector, "name")
        name_key.text = kwargs.pop('name')
        sfp = ET.SubElement(connector, "sfp")
        breakout = ET.SubElement(sfp, "breakout")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name = ET.SubElement(port_group, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_performance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        mode = ET.SubElement(port_group, "mode")
        performance = ET.SubElement(mode, "performance")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id = ET.SubElement(connector_group, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id_key = ET.SubElement(connector_group, "id")
        id_key.text = kwargs.pop('id')
        speed = ET.SubElement(connector_group, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id = ET.SubElement(flexport, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        type = ET.SubElement(flexport_type, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        instance = ET.SubElement(flexport_type, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_skip_deconfig(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        skip_deconfig = ET.SubElement(flexport_type, "skip_deconfig")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_flexports_output_flexport_list_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_flexports = ET.Element("get_flexports")
        config = get_flexports
        output = ET.SubElement(get_flexports, "output")
        flexport_list = ET.SubElement(output, "flexport-list")
        port_id = ET.SubElement(flexport_list, "port-id")
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        