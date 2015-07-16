#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_arp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_arp_holder_system_max_arp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        system_max = ET.SubElement(hide_arp_holder, "system-max")
        arp = ET.SubElement(system_max, "arp")
        arp.text = kwargs.pop('arp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_arp_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address.text = kwargs.pop('arp_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_mac_address_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        mac_address_value = ET.SubElement(arp_entry, "mac-address-value")
        mac_address_value.text = kwargs.pop('mac_address_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacename = ET.SubElement(arp_entry, "interfacename")
        interfacename.text = kwargs.pop('interfacename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_GigabitEthernet_GigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        GigabitEthernet = ET.SubElement(interfacetype, "GigabitEthernet")
        GigabitEthernet = ET.SubElement(GigabitEthernet, "GigabitEthernet")
        GigabitEthernet.text = kwargs.pop('GigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_TenGigabitEthernet_TenGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        TenGigabitEthernet = ET.SubElement(interfacetype, "TenGigabitEthernet")
        TenGigabitEthernet = ET.SubElement(TenGigabitEthernet, "TenGigabitEthernet")
        TenGigabitEthernet.text = kwargs.pop('TenGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_FortyGigabitEthernet_FortyGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        FortyGigabitEthernet = ET.SubElement(interfacetype, "FortyGigabitEthernet")
        FortyGigabitEthernet = ET.SubElement(FortyGigabitEthernet, "FortyGigabitEthernet")
        FortyGigabitEthernet.text = kwargs.pop('FortyGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_HundredGigabitEthernet_HundredGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        HundredGigabitEthernet = ET.SubElement(interfacetype, "HundredGigabitEthernet")
        HundredGigabitEthernet = ET.SubElement(HundredGigabitEthernet, "HundredGigabitEthernet")
        HundredGigabitEthernet.text = kwargs.pop('HundredGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_Ve_Ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        Ve = ET.SubElement(interfacetype, "Ve")
        Ve = ET.SubElement(Ve, "Ve")
        Ve.text = kwargs.pop('Ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        interface = ET.SubElement(input_type, "interface")
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        interface = ET.SubElement(input_type, "interface")
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_dynamic_dynamic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        dynamic = ET.SubElement(input_type, "dynamic")
        dynamic = ET.SubElement(dynamic, "dynamic")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_static_static(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        static = ET.SubElement(input_type, "static")
        static = ET.SubElement(static, "static")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_ip_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        ip = ET.SubElement(input_type, "ip")
        ip_address = ET.SubElement(ip, "ip-address")
        ip_address.text = kwargs.pop('ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address = ET.SubElement(arp_entry, "ip-address")
        ip_address.text = kwargs.pop('ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        mac_address = ET.SubElement(arp_entry, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        interface_type = ET.SubElement(arp_entry, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        interface_name = ET.SubElement(arp_entry, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_is_resolved(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        is_resolved = ET.SubElement(arp_entry, "is-resolved")
        is_resolved.text = kwargs.pop('is_resolved')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        age = ET.SubElement(arp_entry, "age")
        age.text = kwargs.pop('age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_entry_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        entry_type = ET.SubElement(arp_entry, "entry-type")
        entry_type.text = kwargs.pop('entry_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_system_max_arp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        system_max = ET.SubElement(hide_arp_holder, "system-max")
        arp = ET.SubElement(system_max, "arp")
        arp.text = kwargs.pop('arp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_arp_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address.text = kwargs.pop('arp_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_mac_address_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        mac_address_value = ET.SubElement(arp_entry, "mac-address-value")
        mac_address_value.text = kwargs.pop('mac_address_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacename = ET.SubElement(arp_entry, "interfacename")
        interfacename.text = kwargs.pop('interfacename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_GigabitEthernet_GigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        GigabitEthernet = ET.SubElement(interfacetype, "GigabitEthernet")
        GigabitEthernet = ET.SubElement(GigabitEthernet, "GigabitEthernet")
        GigabitEthernet.text = kwargs.pop('GigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_TenGigabitEthernet_TenGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        TenGigabitEthernet = ET.SubElement(interfacetype, "TenGigabitEthernet")
        TenGigabitEthernet = ET.SubElement(TenGigabitEthernet, "TenGigabitEthernet")
        TenGigabitEthernet.text = kwargs.pop('TenGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_FortyGigabitEthernet_FortyGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        FortyGigabitEthernet = ET.SubElement(interfacetype, "FortyGigabitEthernet")
        FortyGigabitEthernet = ET.SubElement(FortyGigabitEthernet, "FortyGigabitEthernet")
        FortyGigabitEthernet.text = kwargs.pop('FortyGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_HundredGigabitEthernet_HundredGigabitEthernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        HundredGigabitEthernet = ET.SubElement(interfacetype, "HundredGigabitEthernet")
        HundredGigabitEthernet = ET.SubElement(HundredGigabitEthernet, "HundredGigabitEthernet")
        HundredGigabitEthernet.text = kwargs.pop('HundredGigabitEthernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_arp_holder_arp_entry_interfacetype_Ve_Ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_arp_holder = ET.SubElement(config, "hide-arp-holder", xmlns="urn:brocade.com:mgmt:brocade-arp")
        arp_entry = ET.SubElement(hide_arp_holder, "arp-entry")
        arp_ip_address_key = ET.SubElement(arp_entry, "arp-ip-address")
        arp_ip_address_key.text = kwargs.pop('arp_ip_address')
        interfacetype = ET.SubElement(arp_entry, "interfacetype")
        Ve = ET.SubElement(interfacetype, "Ve")
        Ve = ET.SubElement(Ve, "Ve")
        Ve.text = kwargs.pop('Ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        interface = ET.SubElement(input_type, "interface")
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        interface = ET.SubElement(input_type, "interface")
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_dynamic_dynamic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        dynamic = ET.SubElement(input_type, "dynamic")
        dynamic = ET.SubElement(dynamic, "dynamic")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_static_static(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        static = ET.SubElement(input_type, "static")
        static = ET.SubElement(static, "static")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_input_input_type_ip_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        input = ET.SubElement(get_arp, "input")
        input_type = ET.SubElement(input, "input-type")
        ip = ET.SubElement(input_type, "ip")
        ip_address = ET.SubElement(ip, "ip-address")
        ip_address.text = kwargs.pop('ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address = ET.SubElement(arp_entry, "ip-address")
        ip_address.text = kwargs.pop('ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        mac_address = ET.SubElement(arp_entry, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        interface_type = ET.SubElement(arp_entry, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        interface_name = ET.SubElement(arp_entry, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_is_resolved(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        is_resolved = ET.SubElement(arp_entry, "is-resolved")
        is_resolved.text = kwargs.pop('is_resolved')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        age = ET.SubElement(arp_entry, "age")
        age.text = kwargs.pop('age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_arp_output_arp_entry_entry_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_arp = ET.Element("get_arp")
        config = get_arp
        output = ET.SubElement(get_arp, "output")
        arp_entry = ET.SubElement(output, "arp-entry")
        ip_address_key = ET.SubElement(arp_entry, "ip-address")
        ip_address_key.text = kwargs.pop('ip_address')
        entry_type = ET.SubElement(arp_entry, "entry-type")
        entry_type.text = kwargs.pop('entry_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        