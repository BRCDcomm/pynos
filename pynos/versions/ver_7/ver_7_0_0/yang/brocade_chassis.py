#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_chassis(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_virtual_ip_holder_chassis_virtual_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        virtual_ip = ET.SubElement(chassis, "virtual-ip")
        virtual_ip.text = kwargs.pop('virtual_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_virtual_ipv6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        virtual_ipv6 = ET.SubElement(chassis, "virtual-ipv6")
        virtual_ipv6.text = kwargs.pop('virtual_ipv6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_oper_address_virtual_oper_Vip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        oper_address = ET.SubElement(chassis, "oper-address")
        virtual_oper_Vip_address = ET.SubElement(oper_address, "virtual-oper-Vip-address")
        virtual_oper_Vip_address.text = kwargs.pop('virtual_oper_Vip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_virtual_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        virtual_ip = ET.SubElement(chassis, "virtual-ip")
        virtual_ip.text = kwargs.pop('virtual_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_virtual_ipv6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        virtual_ipv6 = ET.SubElement(chassis, "virtual-ipv6")
        virtual_ipv6.text = kwargs.pop('virtual_ipv6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_virtual_ip_holder_chassis_oper_address_virtual_oper_Vip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_virtual_ip_holder = ET.SubElement(config, "hide-virtual-ip-holder", xmlns="urn:brocade.com:mgmt:brocade-chassis")
        chassis = ET.SubElement(hide_virtual_ip_holder, "chassis")
        oper_address = ET.SubElement(chassis, "oper-address")
        virtual_oper_Vip_address = ET.SubElement(oper_address, "virtual-oper-Vip-address")
        virtual_oper_Vip_address.text = kwargs.pop('virtual_oper_Vip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        