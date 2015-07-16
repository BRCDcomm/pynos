#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ntp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_ntp_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        input = ET.SubElement(show_ntp, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        output = ET.SubElement(show_ntp, "output")
        node_active_server = ET.SubElement(output, "node-active-server")
        rbridge_id_out = ET.SubElement(node_active_server, "rbridge-id-out")
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_ip4_6_or_local_ipv4_6_active_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        output = ET.SubElement(show_ntp, "output")
        node_active_server = ET.SubElement(output, "node-active-server")
        ip4_6_or_local = ET.SubElement(node_active_server, "ip4-6-or-local")
        ipv4_6 = ET.SubElement(ip4_6_or_local, "ipv4-6")
        active_server = ET.SubElement(ipv4_6, "active-server")
        active_server.text = kwargs.pop('active_server')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_ip4_6_or_local_local_LOCL(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        output = ET.SubElement(show_ntp, "output")
        node_active_server = ET.SubElement(output, "node-active-server")
        ip4_6_or_local = ET.SubElement(node_active_server, "ip4-6-or-local")
        local = ET.SubElement(ip4_6_or_local, "local")
        LOCL = ET.SubElement(local, "LOCL")
        LOCL.text = kwargs.pop('LOCL')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        server = ET.SubElement(ntp, "server")
        ip = ET.SubElement(server, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        server = ET.SubElement(ntp, "server")
        ip_key = ET.SubElement(server, "ip")
        ip_key.text = kwargs.pop('ip')
        key = ET.SubElement(server, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_keyid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        authentication_key = ET.SubElement(ntp, "authentication-key")
        keyid = ET.SubElement(authentication_key, "keyid")
        keyid.text = kwargs.pop('keyid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_md5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        authentication_key = ET.SubElement(ntp, "authentication-key")
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        md5 = ET.SubElement(authentication_key, "md5")
        md5.text = kwargs.pop('md5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        authentication_key = ET.SubElement(ntp, "authentication-key")
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        encryption_level = ET.SubElement(authentication_key, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        source_ip = ET.SubElement(ntp, "source-ip")
        source_ip.text = kwargs.pop('source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        input = ET.SubElement(show_ntp, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        output = ET.SubElement(show_ntp, "output")
        node_active_server = ET.SubElement(output, "node-active-server")
        rbridge_id_out = ET.SubElement(node_active_server, "rbridge-id-out")
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_ip4_6_or_local_ipv4_6_active_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        output = ET.SubElement(show_ntp, "output")
        node_active_server = ET.SubElement(output, "node-active-server")
        ip4_6_or_local = ET.SubElement(node_active_server, "ip4-6-or-local")
        ipv4_6 = ET.SubElement(ip4_6_or_local, "ipv4-6")
        active_server = ET.SubElement(ipv4_6, "active-server")
        active_server.text = kwargs.pop('active_server')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_ntp_output_node_active_server_ip4_6_or_local_local_LOCL(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_ntp = ET.Element("show_ntp")
        config = show_ntp
        output = ET.SubElement(show_ntp, "output")
        node_active_server = ET.SubElement(output, "node-active-server")
        ip4_6_or_local = ET.SubElement(node_active_server, "ip4-6-or-local")
        local = ET.SubElement(ip4_6_or_local, "local")
        LOCL = ET.SubElement(local, "LOCL")
        LOCL.text = kwargs.pop('LOCL')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        server = ET.SubElement(ntp, "server")
        ip = ET.SubElement(server, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_server_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        server = ET.SubElement(ntp, "server")
        ip_key = ET.SubElement(server, "ip")
        ip_key.text = kwargs.pop('ip')
        key = ET.SubElement(server, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_keyid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        authentication_key = ET.SubElement(ntp, "authentication-key")
        keyid = ET.SubElement(authentication_key, "keyid")
        keyid.text = kwargs.pop('keyid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_md5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        authentication_key = ET.SubElement(ntp, "authentication-key")
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        md5 = ET.SubElement(authentication_key, "md5")
        md5.text = kwargs.pop('md5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_authentication_key_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        authentication_key = ET.SubElement(ntp, "authentication-key")
        keyid_key = ET.SubElement(authentication_key, "keyid")
        keyid_key.text = kwargs.pop('keyid')
        encryption_level = ET.SubElement(authentication_key, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ntp_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ntp = ET.SubElement(config, "ntp", xmlns="urn:brocade.com:mgmt:brocade-ntp")
        source_ip = ET.SubElement(ntp, "source-ip")
        source_ip.text = kwargs.pop('source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        