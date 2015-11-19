#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_diagnostics(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def diag_post_rbridge_id_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        post = ET.SubElement(diag, "post")
        rbridge_id = ET.SubElement(post, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        enable = ET.SubElement(rbridge_id, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def diag_post_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        post = ET.SubElement(diag, "post")
        rbridge_id = ET.SubElement(post, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def diag_post_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        post = ET.SubElement(diag, "post")
        enable = ET.SubElement(post, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def diag_post_rbridge_id_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        post = ET.SubElement(diag, "post")
        rbridge_id = ET.SubElement(post, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        enable = ET.SubElement(rbridge_id, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def diag_post_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        post = ET.SubElement(diag, "post")
        rbridge_id = ET.SubElement(post, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def diag_post_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        diag = ET.SubElement(config, "diag", xmlns="urn:brocade.com:mgmt:brocade-diagnostics")
        post = ET.SubElement(diag, "post")
        enable = ET.SubElement(post, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        