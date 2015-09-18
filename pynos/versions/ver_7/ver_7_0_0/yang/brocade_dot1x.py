#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_dot1x(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def dot1x_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dot1x = ET.SubElement(config, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
        enable = ET.SubElement(dot1x, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dot1x_test_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dot1x = ET.SubElement(config, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
        test = ET.SubElement(dot1x, "test")
        timeout = ET.SubElement(test, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dot1x_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dot1x = ET.SubElement(config, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
        enable = ET.SubElement(dot1x, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dot1x_test_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dot1x = ET.SubElement(config, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
        test = ET.SubElement(dot1x, "test")
        timeout = ET.SubElement(test, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        