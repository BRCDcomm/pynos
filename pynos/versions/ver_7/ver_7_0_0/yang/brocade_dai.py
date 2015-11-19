#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_dai(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def arp_access_list_acl_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name = ET.SubElement(access_list, "acl-name")
        acl_name.text = kwargs.pop('acl_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_ip_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        ip_type = ET.SubElement(permit_list, "ip-type")
        ip_type.text = kwargs.pop('ip_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        host_ip = ET.SubElement(permit_list, "host-ip")
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        mac_type = ET.SubElement(permit_list, "mac-type")
        mac_type.text = kwargs.pop('mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_host_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac = ET.SubElement(permit_list, "host-mac")
        host_mac.text = kwargs.pop('host_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        log = ET.SubElement(permit_list, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_acl_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name = ET.SubElement(access_list, "acl-name")
        acl_name.text = kwargs.pop('acl_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_ip_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        ip_type = ET.SubElement(permit_list, "ip-type")
        ip_type.text = kwargs.pop('ip_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        host_ip = ET.SubElement(permit_list, "host-ip")
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        mac_type = ET.SubElement(permit_list, "mac-type")
        mac_type.text = kwargs.pop('mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_host_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac = ET.SubElement(permit_list, "host-mac")
        host_mac.text = kwargs.pop('host_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def arp_access_list_permit_permit_list_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        arp = ET.SubElement(config, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
        access_list = ET.SubElement(arp, "access-list")
        acl_name_key = ET.SubElement(access_list, "acl-name")
        acl_name_key.text = kwargs.pop('acl_name')
        permit = ET.SubElement(access_list, "permit")
        permit_list = ET.SubElement(permit, "permit-list")
        ip_type_key = ET.SubElement(permit_list, "ip-type")
        ip_type_key.text = kwargs.pop('ip_type')
        host_ip_key = ET.SubElement(permit_list, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        mac_type_key = ET.SubElement(permit_list, "mac-type")
        mac_type_key.text = kwargs.pop('mac_type')
        host_mac_key = ET.SubElement(permit_list, "host-mac")
        host_mac_key.text = kwargs.pop('host_mac')
        log = ET.SubElement(permit_list, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        