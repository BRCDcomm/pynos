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
        
    def http_sa_http_server_http_vrf_cont_use_vrf_use_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        http = ET.SubElement(http_sa, "http")
        server = ET.SubElement(http, "server")
        http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
        use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
        use_vrf_name = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name.text = kwargs.pop('use_vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def http_sa_http_server_http_vrf_cont_use_vrf_http_vrf_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        http = ET.SubElement(http_sa, "http")
        server = ET.SubElement(http, "server")
        http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
        use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
        use_vrf_name_key = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name_key.text = kwargs.pop('use_vrf_name')
        http_vrf_shutdown = ET.SubElement(use_vrf, "http-vrf-shutdown")

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
        
    def http_sa_http_server_http_vrf_cont_use_vrf_use_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        http = ET.SubElement(http_sa, "http")
        server = ET.SubElement(http, "server")
        http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
        use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
        use_vrf_name = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name.text = kwargs.pop('use_vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def http_sa_http_server_http_vrf_cont_use_vrf_http_vrf_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        http_sa = ET.SubElement(config, "http-sa", xmlns="urn:brocade.com:mgmt:brocade-http")
        http = ET.SubElement(http_sa, "http")
        server = ET.SubElement(http, "server")
        http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
        use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
        use_vrf_name_key = ET.SubElement(use_vrf, "use-vrf-name")
        use_vrf_name_key.text = kwargs.pop('use_vrf_name')
        http_vrf_shutdown = ET.SubElement(use_vrf, "http-vrf-shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        