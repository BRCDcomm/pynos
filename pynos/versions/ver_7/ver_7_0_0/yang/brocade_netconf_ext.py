#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_netconf_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_netconf_client_capabilities_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        input = ET.SubElement(get_netconf_client_capabilities, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        session_id = ET.SubElement(session, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_user_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        user_name = ET.SubElement(session, "user-name")
        user_name.text = kwargs.pop('user_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_vendor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        vendor = ET.SubElement(session, "vendor")
        vendor.text = kwargs.pop('vendor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_product(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        product = ET.SubElement(session, "product")
        product.text = kwargs.pop('product')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        version = ET.SubElement(session, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_identity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        identity = ET.SubElement(session, "identity")
        identity.text = kwargs.pop('identity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_af_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        af_type = ET.SubElement(session, "af-type")
        af_type.text = kwargs.pop('af_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_host_ip_v6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        host_ip_v6 = ET.SubElement(session, "host-ip-v6")
        host_ip_v6.text = kwargs.pop('host_ip_v6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        host_ip = ET.SubElement(session, "host-ip")
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        time = ET.SubElement(session, "time")
        time.text = kwargs.pop('time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        input = ET.SubElement(get_netconf_client_capabilities, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        session_id = ET.SubElement(session, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_user_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        user_name = ET.SubElement(session, "user-name")
        user_name.text = kwargs.pop('user_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_vendor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        vendor = ET.SubElement(session, "vendor")
        vendor.text = kwargs.pop('vendor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_product(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        product = ET.SubElement(session, "product")
        product.text = kwargs.pop('product')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        version = ET.SubElement(session, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_identity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        identity = ET.SubElement(session, "identity")
        identity.text = kwargs.pop('identity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_af_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        af_type = ET.SubElement(session, "af-type")
        af_type.text = kwargs.pop('af_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_host_ip_v6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        host_ip_v6 = ET.SubElement(session, "host-ip-v6")
        host_ip_v6.text = kwargs.pop('host_ip_v6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        host_ip = ET.SubElement(session, "host-ip")
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_netconf_client_capabilities_output_session_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_netconf_client_capabilities = ET.Element("get_netconf_client_capabilities")
        config = get_netconf_client_capabilities
        output = ET.SubElement(get_netconf_client_capabilities, "output")
        session = ET.SubElement(output, "session")
        time = ET.SubElement(session, "time")
        time.text = kwargs.pop('time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        