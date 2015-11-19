#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_http_redirect(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def set_http_application_url_input_config_http_app_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        input = ET.SubElement(set_http_application_url, "input")
        config_http_app_url = ET.SubElement(input, "config-http-app-url")
        url = ET.SubElement(config_http_app_url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_input_config_http_app_url_op_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        input = ET.SubElement(set_http_application_url, "input")
        config_http_app_url = ET.SubElement(input, "config-http-app-url")
        op_type = ET.SubElement(config_http_app_url, "op-type")
        op_type.text = kwargs.pop('op_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_output_status_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        output = ET.SubElement(set_http_application_url, "output")
        status_code = ET.SubElement(output, "status-code")
        status_code.text = kwargs.pop('status_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        output = ET.SubElement(set_http_application_url, "output")
        status_string = ET.SubElement(output, "status-string")
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_input_config_http_app_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        input = ET.SubElement(set_http_application_url, "input")
        config_http_app_url = ET.SubElement(input, "config-http-app-url")
        url = ET.SubElement(config_http_app_url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_input_config_http_app_url_op_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        input = ET.SubElement(set_http_application_url, "input")
        config_http_app_url = ET.SubElement(input, "config-http-app-url")
        op_type = ET.SubElement(config_http_app_url, "op-type")
        op_type.text = kwargs.pop('op_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_output_status_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        output = ET.SubElement(set_http_application_url, "output")
        status_code = ET.SubElement(output, "status-code")
        status_code.text = kwargs.pop('status_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def set_http_application_url_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        set_http_application_url = ET.Element("set_http_application_url")
        config = set_http_application_url
        output = ET.SubElement(set_http_application_url, "output")
        status_string = ET.SubElement(output, "status-string")
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        