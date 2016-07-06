#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_isns(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def isns_isns_vrf_isns_vrf_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance.text = kwargs.pop('isns_vrf_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_ipaddress_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_ipaddress = ET.SubElement(isns_vrf, "isns-ipaddress")
        ip = ET.SubElement(isns_ipaddress, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_ipaddress_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_ipaddress = ET.SubElement(isns_vrf, "isns-ipaddress")
        loopback = ET.SubElement(isns_ipaddress, "loopback")
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_esi_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        esi_timeout = ET.SubElement(isns_vrf, "esi-timeout")
        esi_timeout.text = kwargs.pop('esi_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_discovery_domain_isns_discovery_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_discovery_domain = ET.SubElement(isns_vrf, "isns-discovery-domain")
        isns_discovery_domain_name = ET.SubElement(isns_discovery_domain, "isns-discovery-domain-name")
        isns_discovery_domain_name.text = kwargs.pop('isns_discovery_domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_discovery_domain_set_isns_discovery_domain_set_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_discovery_domain_set = ET.SubElement(isns_vrf, "isns-discovery-domain-set")
        isns_discovery_domain_set_name = ET.SubElement(isns_discovery_domain_set, "isns-discovery-domain-set-name")
        isns_discovery_domain_set_name.text = kwargs.pop('isns_discovery_domain_set_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_discovery_domain_set_isns_discovery_domain_set_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_discovery_domain_set = ET.SubElement(isns_vrf, "isns-discovery-domain-set")
        isns_discovery_domain_set_name_key = ET.SubElement(isns_discovery_domain_set, "isns-discovery-domain-set-name")
        isns_discovery_domain_set_name_key.text = kwargs.pop('isns_discovery_domain_set_name')
        isns_discovery_domain_set_enable = ET.SubElement(isns_discovery_domain_set, "isns-discovery-domain-set-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_vrf_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance.text = kwargs.pop('isns_vrf_instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_ipaddress_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_ipaddress = ET.SubElement(isns_vrf, "isns-ipaddress")
        ip = ET.SubElement(isns_ipaddress, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_ipaddress_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_ipaddress = ET.SubElement(isns_vrf, "isns-ipaddress")
        loopback = ET.SubElement(isns_ipaddress, "loopback")
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_esi_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        esi_timeout = ET.SubElement(isns_vrf, "esi-timeout")
        esi_timeout.text = kwargs.pop('esi_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_discovery_domain_isns_discovery_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_discovery_domain = ET.SubElement(isns_vrf, "isns-discovery-domain")
        isns_discovery_domain_name = ET.SubElement(isns_discovery_domain, "isns-discovery-domain-name")
        isns_discovery_domain_name.text = kwargs.pop('isns_discovery_domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_discovery_domain_set_isns_discovery_domain_set_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_discovery_domain_set = ET.SubElement(isns_vrf, "isns-discovery-domain-set")
        isns_discovery_domain_set_name = ET.SubElement(isns_discovery_domain_set, "isns-discovery-domain-set-name")
        isns_discovery_domain_set_name.text = kwargs.pop('isns_discovery_domain_set_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def isns_isns_vrf_isns_discovery_domain_set_isns_discovery_domain_set_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        isns = ET.SubElement(config, "isns", xmlns="urn:brocade.com:mgmt:brocade-isns")
        isns_vrf = ET.SubElement(isns, "isns-vrf")
        isns_vrf_instance_key = ET.SubElement(isns_vrf, "isns-vrf-instance")
        isns_vrf_instance_key.text = kwargs.pop('isns_vrf_instance')
        isns_discovery_domain_set = ET.SubElement(isns_vrf, "isns-discovery-domain-set")
        isns_discovery_domain_set_name_key = ET.SubElement(isns_discovery_domain_set, "isns-discovery-domain-set-name")
        isns_discovery_domain_set_name_key.text = kwargs.pop('isns_discovery_domain_set_name')
        isns_discovery_domain_set_enable = ET.SubElement(isns_discovery_domain_set, "isns-discovery-domain-set-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        