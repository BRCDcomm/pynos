#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_license(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def dpod_port_id_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dpod = ET.SubElement(config, "dpod", xmlns="urn:brocade.com:mgmt:brocade-license")
        port_id = ET.SubElement(dpod, "port-id")
        port_id = ET.SubElement(port_id, "port-id")
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dpod_port_id_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dpod = ET.SubElement(config, "dpod", xmlns="urn:brocade.com:mgmt:brocade-license")
        port_id = ET.SubElement(dpod, "port-id")
        port_id_key = ET.SubElement(port_id, "port-id")
        port_id_key.text = kwargs.pop('port_id')
        operation = ET.SubElement(port_id, "operation")
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dpod_port_id_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dpod = ET.SubElement(config, "dpod", xmlns="urn:brocade.com:mgmt:brocade-license")
        port_id = ET.SubElement(dpod, "port-id")
        port_id = ET.SubElement(port_id, "port-id")
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dpod_port_id_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dpod = ET.SubElement(config, "dpod", xmlns="urn:brocade.com:mgmt:brocade-license")
        port_id = ET.SubElement(dpod, "port-id")
        port_id_key = ET.SubElement(port_id, "port-id")
        port_id_key.text = kwargs.pop('port_id')
        operation = ET.SubElement(port_id, "operation")
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        