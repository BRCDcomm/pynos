#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_intf_loopback(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_intf_loopback_holder_interface_loopback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id = ET.SubElement(loopback, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_vrf_forwarding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        vrf = ET.SubElement(loopback, "vrf")
        forwarding = ET.SubElement(vrf, "forwarding")
        forwarding.text = kwargs.pop('forwarding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_intf_loopback_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        intf_loopback = ET.SubElement(loopback, "intf-loopback")
        shutdown = ET.SubElement(intf_loopback, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ip_ip_config_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ip = ET.SubElement(loopback, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
        ip_config = ET.SubElement(ip, "ip-config")
        address = ET.SubElement(ip_config, "address")
        address = ET.SubElement(address, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_use_link_local_only(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        use_link_local_only = ET.SubElement(address, "use-link-local-only")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_link_local_config_link_local_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        link_local_config = ET.SubElement(address, "link-local-config")
        link_local_address = ET.SubElement(link_local_config, "link-local-address")
        link_local_address.text = kwargs.pop('link_local_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_link_local_config_link_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        link_local_config = ET.SubElement(address, "link-local-config")
        link_local = ET.SubElement(link_local_config, "link-local")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_ipv6_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        ipv6_address = ET.SubElement(address, "ipv6-address")
        address = ET.SubElement(ipv6_address, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_ipv6_address_eui64(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        ipv6_address = ET.SubElement(address, "ipv6-address")
        address_key = ET.SubElement(ipv6_address, "address")
        address_key.text = kwargs.pop('address')
        eui64 = ET.SubElement(ipv6_address, "eui64")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_ipv6_address_anycast(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        ipv6_address = ET.SubElement(address, "ipv6-address")
        address_key = ET.SubElement(ipv6_address, "address")
        address_key.text = kwargs.pop('address')
        anycast = ET.SubElement(ipv6_address, "anycast")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id = ET.SubElement(loopback, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_vrf_forwarding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        vrf = ET.SubElement(loopback, "vrf")
        forwarding = ET.SubElement(vrf, "forwarding")
        forwarding.text = kwargs.pop('forwarding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_intf_loopback_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        intf_loopback = ET.SubElement(loopback, "intf-loopback")
        shutdown = ET.SubElement(intf_loopback, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ip_ip_config_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ip = ET.SubElement(loopback, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
        ip_config = ET.SubElement(ip, "ip-config")
        address = ET.SubElement(ip_config, "address")
        address = ET.SubElement(address, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_use_link_local_only(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        use_link_local_only = ET.SubElement(address, "use-link-local-only")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_link_local_config_link_local_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        link_local_config = ET.SubElement(address, "link-local-config")
        link_local_address = ET.SubElement(link_local_config, "link-local-address")
        link_local_address.text = kwargs.pop('link_local_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_link_local_config_link_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        link_local_config = ET.SubElement(address, "link-local-config")
        link_local = ET.SubElement(link_local_config, "link-local")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_ipv6_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        ipv6_address = ET.SubElement(address, "ipv6-address")
        address = ET.SubElement(ipv6_address, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_ipv6_address_eui64(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        ipv6_address = ET.SubElement(address, "ipv6-address")
        address_key = ET.SubElement(ipv6_address, "address")
        address_key.text = kwargs.pop('address')
        eui64 = ET.SubElement(ipv6_address, "eui64")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_intf_loopback_holder_interface_loopback_ipv6_ipv6_config_address_ipv6_address_anycast(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_intf_loopback_holder = ET.SubElement(config, "hide-intf-loopback-holder", xmlns="urn:brocade.com:mgmt:brocade-intf-loopback")
        interface = ET.SubElement(hide_intf_loopback_holder, "interface")
        loopback = ET.SubElement(interface, "loopback")
        id_key = ET.SubElement(loopback, "id")
        id_key.text = kwargs.pop('id')
        ipv6 = ET.SubElement(loopback, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
        ipv6_config = ET.SubElement(ipv6, "ipv6-config")
        address = ET.SubElement(ipv6_config, "address")
        ipv6_address = ET.SubElement(address, "ipv6-address")
        address_key = ET.SubElement(ipv6_address, "address")
        address_key.text = kwargs.pop('address')
        anycast = ET.SubElement(ipv6_address, "anycast")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        