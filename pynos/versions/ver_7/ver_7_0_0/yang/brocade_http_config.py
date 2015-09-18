#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_http_config(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def http_sa_http_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        http = ET.SubElement(http_sa, "http")
        server = ET.SubElement(http, "server")
        shutdown = ET.SubElement(server, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def http_sa_http_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        http = ET.SubElement(http_sa, "http")
        server = ET.SubElement(http, "server")
        shutdown = ET.SubElement(server, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        