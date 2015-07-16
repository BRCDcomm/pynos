#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_lacp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lacp = ET.SubElement(config, "lacp", xmlns="urn:brocade.com:mgmt:brocade-lacp")
        system_priority = ET.SubElement(lacp, "system-priority")
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lacp = ET.SubElement(config, "lacp", xmlns="urn:brocade.com:mgmt:brocade-lacp")
        system_priority = ET.SubElement(lacp, "system-priority")
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        