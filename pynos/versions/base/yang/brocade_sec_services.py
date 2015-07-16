#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_sec_services(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def telnet_sa_telnet_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        telnet = ET.SubElement(telnet_sa, "telnet")
        server = ET.SubElement(telnet, "server")
        shutdown = ET.SubElement(server, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def telnet_sa_telnet_server_standby_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        telnet = ET.SubElement(telnet_sa, "telnet")
        server = ET.SubElement(telnet, "server")
        standby = ET.SubElement(server, "standby")
        enable = ET.SubElement(standby, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        shutdown = ET.SubElement(server, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_exchange_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key_exchange = ET.SubElement(server, "key-exchange")
        protocol = ET.SubElement(key_exchange, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_rekey_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        rekey_interval = ET.SubElement(server, "rekey-interval")
        rekey_interval.text = kwargs.pop('rekey_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_cipher(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        cipher = ET.SubElement(server, "cipher")
        cipher.text = kwargs.pop('cipher')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_standby_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        standby = ET.SubElement(server, "standby")
        enable = ET.SubElement(standby, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_rsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key = ET.SubElement(server, "key")
        rsa = ET.SubElement(key, "rsa")
        rsa.text = kwargs.pop('rsa')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_ecdsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key = ET.SubElement(server, "key")
        ecdsa = ET.SubElement(key, "ecdsa")
        ecdsa.text = kwargs.pop('ecdsa')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_dsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key = ET.SubElement(server, "key")
        dsa = ET.SubElement(key, "dsa")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_client_cipher(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        client = ET.SubElement(ssh, "client")
        cipher = ET.SubElement(client, "cipher")
        cipher.text = kwargs.pop('cipher')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def telnet_sa_telnet_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        telnet = ET.SubElement(telnet_sa, "telnet")
        server = ET.SubElement(telnet, "server")
        shutdown = ET.SubElement(server, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def telnet_sa_telnet_server_standby_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        telnet_sa = ET.SubElement(config, "telnet-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        telnet = ET.SubElement(telnet_sa, "telnet")
        server = ET.SubElement(telnet, "server")
        standby = ET.SubElement(server, "standby")
        enable = ET.SubElement(standby, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        shutdown = ET.SubElement(server, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_exchange_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key_exchange = ET.SubElement(server, "key-exchange")
        protocol = ET.SubElement(key_exchange, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_rekey_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        rekey_interval = ET.SubElement(server, "rekey-interval")
        rekey_interval.text = kwargs.pop('rekey_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_cipher(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        cipher = ET.SubElement(server, "cipher")
        cipher.text = kwargs.pop('cipher')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_standby_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        standby = ET.SubElement(server, "standby")
        enable = ET.SubElement(standby, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_rsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key = ET.SubElement(server, "key")
        rsa = ET.SubElement(key, "rsa")
        rsa.text = kwargs.pop('rsa')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_ecdsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key = ET.SubElement(server, "key")
        ecdsa = ET.SubElement(key, "ecdsa")
        ecdsa.text = kwargs.pop('ecdsa')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_server_key_dsa(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        server = ET.SubElement(ssh, "server")
        key = ET.SubElement(server, "key")
        dsa = ET.SubElement(key, "dsa")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ssh_sa_ssh_client_cipher(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ssh_sa = ET.SubElement(config, "ssh-sa", xmlns="urn:brocade.com:mgmt:brocade-sec-services")
        ssh = ET.SubElement(ssh_sa, "ssh")
        client = ET.SubElement(ssh, "client")
        cipher = ET.SubElement(client, "cipher")
        cipher.text = kwargs.pop('cipher')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        