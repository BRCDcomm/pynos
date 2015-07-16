#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_interface_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_vlan_brief_input_request_type_get_request_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        input = ET.SubElement(get_vlan_brief, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        vlan_id = ET.SubElement(get_request, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_input_request_type_get_next_request_last_rcvd_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        input = ET.SubElement(get_vlan_brief, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_vlan_id = ET.SubElement(get_next_request, "last-rcvd-vlan-id")
        last_rcvd_vlan_id.text = kwargs.pop('last_rcvd_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id = ET.SubElement(vlan, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        vlan_type = ET.SubElement(vlan, "vlan-type")
        vlan_type.text = kwargs.pop('vlan_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        vlan_name = ET.SubElement(vlan, "vlan-name")
        vlan_name.text = kwargs.pop('vlan_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        vlan_state = ET.SubElement(vlan, "vlan-state")
        vlan_state.text = kwargs.pop('vlan_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        tag = ET.SubElement(interface, "tag")
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_classification_classification_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        classification = ET.SubElement(interface, "classification")
        classification_value_key = ET.SubElement(classification, "classification-value")
        classification_value_key.text = kwargs.pop('classification_value')
        classification_type = ET.SubElement(classification, "classification-type")
        classification_type.text = kwargs.pop('classification_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_classification_classification_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        classification = ET.SubElement(interface, "classification")
        classification_type_key = ET.SubElement(classification, "classification-type")
        classification_type_key.text = kwargs.pop('classification_type')
        classification_value = ET.SubElement(classification, "classification-value")
        classification_value.text = kwargs.pop('classification_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_last_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        last_vlan_id = ET.SubElement(output, "last-vlan-id")
        last_vlan_id.text = kwargs.pop('last_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(switchport, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(switchport, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        mode = ET.SubElement(switchport, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_fcoe_port_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        fcoe_port_enabled = ET.SubElement(switchport, "fcoe-port-enabled")
        fcoe_port_enabled.text = kwargs.pop('fcoe_port_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_ingress_filter_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ingress_filter_enabled = ET.SubElement(switchport, "ingress-filter-enabled")
        ingress_filter_enabled.text = kwargs.pop('ingress_filter_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_acceptable_frame_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        acceptable_frame_type = ET.SubElement(switchport, "acceptable-frame-type")
        acceptable_frame_type.text = kwargs.pop('acceptable_frame_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_default_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        default_vlan = ET.SubElement(switchport, "default-vlan")
        default_vlan.text = kwargs.pop('default_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        input = ET.SubElement(get_ip_interface, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        input = ET.SubElement(get_ip_interface, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        input = ET.SubElement(get_ip_interface, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        rbridge_id = ET.SubElement(get_request, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_if_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_name = ET.SubElement(interface, "if-name")
        if_name.text = kwargs.pop('if_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ipv4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4 = ET.SubElement(ip_address, "ipv4")
        ipv4.text = kwargs.pop('ipv4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ipv4_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        ipv4_type = ET.SubElement(ip_address, "ipv4-type")
        ipv4_type.text = kwargs.pop('ipv4_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_broadcast(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        broadcast = ET.SubElement(ip_address, "broadcast")
        broadcast.text = kwargs.pop('broadcast')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ip_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        ip_mtu = ET.SubElement(ip_address, "ip-mtu")
        ip_mtu.text = kwargs.pop('ip_mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_state = ET.SubElement(interface, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_line_protocol_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_state = ET.SubElement(interface, "line-protocol-state")
        line_protocol_state.text = kwargs.pop('line_protocol_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_proxy_arp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        proxy_arp = ET.SubElement(interface, "proxy-arp")
        proxy_arp.text = kwargs.pop('proxy_arp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vrf = ET.SubElement(interface, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_next_request_last_rcvd_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_interface = ET.SubElement(get_next_request, "last-rcvd-interface")
        interface_type = ET.SubElement(last_rcvd_interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_next_request_last_rcvd_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_interface = ET.SubElement(get_next_request, "last-rcvd-interface")
        interface_name = ET.SubElement(last_rcvd_interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifindex = ET.SubElement(interface, "ifindex")
        ifindex.text = kwargs.pop('ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        mtu = ET.SubElement(interface, "mtu")
        mtu.text = kwargs.pop('mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ip_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_mtu = ET.SubElement(interface, "ip-mtu")
        ip_mtu.text = kwargs.pop('ip_mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_name = ET.SubElement(interface, "if-name")
        if_name.text = kwargs.pop('if_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_state = ET.SubElement(interface, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_state = ET.SubElement(interface, "line-protocol-state")
        line_protocol_state.text = kwargs.pop('line_protocol_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_state_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_state_info = ET.SubElement(interface, "line-protocol-state-info")
        line_protocol_state_info.text = kwargs.pop('line_protocol_state_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_exception_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_exception_info = ET.SubElement(interface, "line-protocol-exception-info")
        line_protocol_exception_info.text = kwargs.pop('line_protocol_exception_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_hardware_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        hardware_type = ET.SubElement(interface, "hardware-type")
        hardware_type.text = kwargs.pop('hardware_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_logical_hardware_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        logical_hardware_address = ET.SubElement(interface, "logical-hardware-address")
        logical_hardware_address.text = kwargs.pop('logical_hardware_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_current_hardware_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        current_hardware_address = ET.SubElement(interface, "current-hardware-address")
        current_hardware_address.text = kwargs.pop('current_hardware_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_media_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        media_type = ET.SubElement(interface, "media-type")
        media_type.text = kwargs.pop('media_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        wavelength = ET.SubElement(interface, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_description = ET.SubElement(interface, "if-description")
        if_description.text = kwargs.pop('if_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_actual_line_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        actual_line_speed = ET.SubElement(interface, "actual-line-speed")
        actual_line_speed.text = kwargs.pop('actual_line_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_configured_line_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        configured_line_speed = ET.SubElement(interface, "configured-line-speed")
        configured_line_speed.text = kwargs.pop('configured_line_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_duplex_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_duplex_state = ET.SubElement(interface, "line-duplex-state")
        line_duplex_state.text = kwargs.pop('line_duplex_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_flow_control(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        flow_control = ET.SubElement(interface, "flow-control")
        flow_control.text = kwargs.pop('flow_control')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_queuing_strategy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        queuing_strategy = ET.SubElement(interface, "queuing-strategy")
        queuing_strategy.text = kwargs.pop('queuing_strategy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_port_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        port_role = ET.SubElement(interface, "port-role")
        port_role.text = kwargs.pop('port_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_port_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        port_mode = ET.SubElement(interface, "port-mode")
        port_mode.text = kwargs.pop('port_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInOctets(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInOctets = ET.SubElement(interface, "ifHCInOctets")
        ifHCInOctets.text = kwargs.pop('ifHCInOctets')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInUcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInUcastPkts = ET.SubElement(interface, "ifHCInUcastPkts")
        ifHCInUcastPkts.text = kwargs.pop('ifHCInUcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInMulticastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInMulticastPkts = ET.SubElement(interface, "ifHCInMulticastPkts")
        ifHCInMulticastPkts.text = kwargs.pop('ifHCInMulticastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInBroadcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInBroadcastPkts = ET.SubElement(interface, "ifHCInBroadcastPkts")
        ifHCInBroadcastPkts.text = kwargs.pop('ifHCInBroadcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInErrors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInErrors = ET.SubElement(interface, "ifHCInErrors")
        ifHCInErrors.text = kwargs.pop('ifHCInErrors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutOctets(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutOctets = ET.SubElement(interface, "ifHCOutOctets")
        ifHCOutOctets.text = kwargs.pop('ifHCOutOctets')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutUcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutUcastPkts = ET.SubElement(interface, "ifHCOutUcastPkts")
        ifHCOutUcastPkts.text = kwargs.pop('ifHCOutUcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutMulticastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutMulticastPkts = ET.SubElement(interface, "ifHCOutMulticastPkts")
        ifHCOutMulticastPkts.text = kwargs.pop('ifHCOutMulticastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutBroadcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutBroadcastPkts = ET.SubElement(interface, "ifHCOutBroadcastPkts")
        ifHCOutBroadcastPkts.text = kwargs.pop('ifHCOutBroadcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutErrors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutErrors = ET.SubElement(interface, "ifHCOutErrors")
        ifHCOutErrors.text = kwargs.pop('ifHCOutErrors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        input = ET.SubElement(get_media_detail, "input")
        interface_type = ET.SubElement(input, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        input = ET.SubElement(get_media_detail, "input")
        interface_name = ET.SubElement(input, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        input = ET.SubElement(get_media_detail, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        speed = ET.SubElement(sfp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        connector = ET.SubElement(sfp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        encoding = ET.SubElement(sfp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_name = ET.SubElement(sfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_oui = ET.SubElement(sfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_pn = ET.SubElement(sfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_rev = ET.SubElement(sfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        distance = ET.SubElement(sfp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        media_form_factor = ET.SubElement(sfp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        wavelength = ET.SubElement(sfp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        serial_no = ET.SubElement(sfp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        date_code = ET.SubElement(sfp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        temperature = ET.SubElement(sfp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        voltage = ET.SubElement(sfp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        current = ET.SubElement(sfp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        tx_power = ET.SubElement(sfp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        rx_power = ET.SubElement(sfp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        speed = ET.SubElement(on_board, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        connector = ET.SubElement(on_board, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        encoding = ET.SubElement(on_board, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_name = ET.SubElement(on_board, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_oui = ET.SubElement(on_board, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_pn = ET.SubElement(on_board, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_rev = ET.SubElement(on_board, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_name = ET.SubElement(gbc, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_oui = ET.SubElement(gbc, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_pn = ET.SubElement(gbc, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_rev = ET.SubElement(gbc, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_name = ET.SubElement(xfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_oui = ET.SubElement(xfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_pn = ET.SubElement(xfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_rev = ET.SubElement(xfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_name = ET.SubElement(xff, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_oui = ET.SubElement(xff, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_pn = ET.SubElement(xff, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_rev = ET.SubElement(xff, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_name = ET.SubElement(xfpe, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_oui = ET.SubElement(xfpe, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_pn = ET.SubElement(xfpe, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_rev = ET.SubElement(xfpe, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_name = ET.SubElement(unknown, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_oui = ET.SubElement(unknown, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_pn = ET.SubElement(unknown, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_rev = ET.SubElement(unknown, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        speed = ET.SubElement(qsfp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        connector = ET.SubElement(qsfp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        encoding = ET.SubElement(qsfp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_name = ET.SubElement(qsfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_oui = ET.SubElement(qsfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_pn = ET.SubElement(qsfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_rev = ET.SubElement(qsfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        distance = ET.SubElement(qsfp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        media_form_factor = ET.SubElement(qsfp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        wavelength = ET.SubElement(qsfp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        serial_no = ET.SubElement(qsfp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        date_code = ET.SubElement(qsfp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        temperature = ET.SubElement(qsfp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        voltage = ET.SubElement(qsfp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        current = ET.SubElement(qsfp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        tx_power = ET.SubElement(qsfp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        rx_power = ET.SubElement(qsfp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        speed = ET.SubElement(qsfpp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        connector = ET.SubElement(qsfpp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        encoding = ET.SubElement(qsfpp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_name = ET.SubElement(qsfpp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_oui = ET.SubElement(qsfpp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_pn = ET.SubElement(qsfpp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_rev = ET.SubElement(qsfpp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        distance = ET.SubElement(qsfpp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        media_form_factor = ET.SubElement(qsfpp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        wavelength = ET.SubElement(qsfpp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        serial_no = ET.SubElement(qsfpp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        date_code = ET.SubElement(qsfpp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        temperature = ET.SubElement(qsfpp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        voltage = ET.SubElement(qsfpp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        current = ET.SubElement(qsfpp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        tx_power = ET.SubElement(qsfpp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        rx_power = ET.SubElement(qsfpp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        speed = ET.SubElement(cfp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        connector = ET.SubElement(cfp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        encoding = ET.SubElement(cfp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_name = ET.SubElement(cfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_oui = ET.SubElement(cfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_pn = ET.SubElement(cfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_rev = ET.SubElement(cfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        distance = ET.SubElement(cfp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        media_form_factor = ET.SubElement(cfp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        wavelength = ET.SubElement(cfp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        serial_no = ET.SubElement(cfp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        date_code = ET.SubElement(cfp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        temperature = ET.SubElement(cfp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        voltage = ET.SubElement(cfp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        current = ET.SubElement(cfp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        tx_power = ET.SubElement(cfp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        rx_power = ET.SubElement(cfp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        speed = ET.SubElement(cfp2, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        connector = ET.SubElement(cfp2, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        encoding = ET.SubElement(cfp2, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_name = ET.SubElement(cfp2, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_oui = ET.SubElement(cfp2, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_pn = ET.SubElement(cfp2, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_rev = ET.SubElement(cfp2, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        distance = ET.SubElement(cfp2, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        media_form_factor = ET.SubElement(cfp2, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        wavelength = ET.SubElement(cfp2, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        serial_no = ET.SubElement(cfp2, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        date_code = ET.SubElement(cfp2, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        temperature = ET.SubElement(cfp2, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        voltage = ET.SubElement(cfp2, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        current = ET.SubElement(cfp2, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        tx_power = ET.SubElement(cfp2, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        rx_power = ET.SubElement(cfp2, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_input_request_type_get_request_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        input = ET.SubElement(get_vlan_brief, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        vlan_id = ET.SubElement(get_request, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_input_request_type_get_next_request_last_rcvd_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        input = ET.SubElement(get_vlan_brief, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_vlan_id = ET.SubElement(get_next_request, "last-rcvd-vlan-id")
        last_rcvd_vlan_id.text = kwargs.pop('last_rcvd_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id = ET.SubElement(vlan, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        vlan_type = ET.SubElement(vlan, "vlan-type")
        vlan_type.text = kwargs.pop('vlan_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        vlan_name = ET.SubElement(vlan, "vlan-name")
        vlan_name.text = kwargs.pop('vlan_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_vlan_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        vlan_state = ET.SubElement(vlan, "vlan-state")
        vlan_state.text = kwargs.pop('vlan_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        tag = ET.SubElement(interface, "tag")
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_classification_classification_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        classification = ET.SubElement(interface, "classification")
        classification_value_key = ET.SubElement(classification, "classification-value")
        classification_value_key.text = kwargs.pop('classification_value')
        classification_type = ET.SubElement(classification, "classification-type")
        classification_type.text = kwargs.pop('classification_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_vlan_interface_classification_classification_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        vlan = ET.SubElement(output, "vlan")
        vlan_id_key = ET.SubElement(vlan, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        interface = ET.SubElement(vlan, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        classification = ET.SubElement(interface, "classification")
        classification_type_key = ET.SubElement(classification, "classification-type")
        classification_type_key.text = kwargs.pop('classification_type')
        classification_value = ET.SubElement(classification, "classification-value")
        classification_value.text = kwargs.pop('classification_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_last_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        last_vlan_id = ET.SubElement(output, "last-vlan-id")
        last_vlan_id.text = kwargs.pop('last_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vlan_brief_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vlan_brief = ET.Element("get_vlan_brief")
        config = get_vlan_brief
        output = ET.SubElement(get_vlan_brief, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(switchport, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(switchport, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        mode = ET.SubElement(switchport, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_fcoe_port_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        fcoe_port_enabled = ET.SubElement(switchport, "fcoe-port-enabled")
        fcoe_port_enabled.text = kwargs.pop('fcoe_port_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_ingress_filter_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ingress_filter_enabled = ET.SubElement(switchport, "ingress-filter-enabled")
        ingress_filter_enabled.text = kwargs.pop('ingress_filter_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_acceptable_frame_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        acceptable_frame_type = ET.SubElement(switchport, "acceptable-frame-type")
        acceptable_frame_type.text = kwargs.pop('acceptable_frame_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_switchport_output_switchport_default_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_switchport = ET.Element("get_interface_switchport")
        config = get_interface_switchport
        output = ET.SubElement(get_interface_switchport, "output")
        switchport = ET.SubElement(output, "switchport")
        interface_type_key = ET.SubElement(switchport, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(switchport, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        default_vlan = ET.SubElement(switchport, "default-vlan")
        default_vlan.text = kwargs.pop('default_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        input = ET.SubElement(get_ip_interface, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        input = ET.SubElement(get_ip_interface, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_input_request_type_get_request_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        input = ET.SubElement(get_ip_interface, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        rbridge_id = ET.SubElement(get_request, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_if_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_name = ET.SubElement(interface, "if-name")
        if_name.text = kwargs.pop('if_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ipv4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4 = ET.SubElement(ip_address, "ipv4")
        ipv4.text = kwargs.pop('ipv4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ipv4_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        ipv4_type = ET.SubElement(ip_address, "ipv4-type")
        ipv4_type.text = kwargs.pop('ipv4_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_broadcast(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        broadcast = ET.SubElement(ip_address, "broadcast")
        broadcast.text = kwargs.pop('broadcast')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_ip_address_ip_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_address = ET.SubElement(interface, "ip-address")
        ipv4_key = ET.SubElement(ip_address, "ipv4")
        ipv4_key.text = kwargs.pop('ipv4')
        ip_mtu = ET.SubElement(ip_address, "ip-mtu")
        ip_mtu.text = kwargs.pop('ip_mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_state = ET.SubElement(interface, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_line_protocol_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_state = ET.SubElement(interface, "line-protocol-state")
        line_protocol_state.text = kwargs.pop('line_protocol_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_proxy_arp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        proxy_arp = ET.SubElement(interface, "proxy-arp")
        proxy_arp.text = kwargs.pop('proxy_arp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_interface_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vrf = ET.SubElement(interface, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_ip_interface_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_ip_interface = ET.Element("get_ip_interface")
        config = get_ip_interface
        output = ET.SubElement(get_ip_interface, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_next_request_last_rcvd_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_interface = ET.SubElement(get_next_request, "last-rcvd-interface")
        interface_type = ET.SubElement(last_rcvd_interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_input_request_type_get_next_request_last_rcvd_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        input = ET.SubElement(get_interface_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_interface = ET.SubElement(get_next_request, "last-rcvd-interface")
        interface_name = ET.SubElement(last_rcvd_interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifindex = ET.SubElement(interface, "ifindex")
        ifindex.text = kwargs.pop('ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        mtu = ET.SubElement(interface, "mtu")
        mtu.text = kwargs.pop('mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ip_mtu(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ip_mtu = ET.SubElement(interface, "ip-mtu")
        ip_mtu.text = kwargs.pop('ip_mtu')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_name = ET.SubElement(interface, "if-name")
        if_name.text = kwargs.pop('if_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_state = ET.SubElement(interface, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_state = ET.SubElement(interface, "line-protocol-state")
        line_protocol_state.text = kwargs.pop('line_protocol_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_state_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_state_info = ET.SubElement(interface, "line-protocol-state-info")
        line_protocol_state_info.text = kwargs.pop('line_protocol_state_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_protocol_exception_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_protocol_exception_info = ET.SubElement(interface, "line-protocol-exception-info")
        line_protocol_exception_info.text = kwargs.pop('line_protocol_exception_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_hardware_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        hardware_type = ET.SubElement(interface, "hardware-type")
        hardware_type.text = kwargs.pop('hardware_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_logical_hardware_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        logical_hardware_address = ET.SubElement(interface, "logical-hardware-address")
        logical_hardware_address.text = kwargs.pop('logical_hardware_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_current_hardware_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        current_hardware_address = ET.SubElement(interface, "current-hardware-address")
        current_hardware_address.text = kwargs.pop('current_hardware_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_media_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        media_type = ET.SubElement(interface, "media-type")
        media_type.text = kwargs.pop('media_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        wavelength = ET.SubElement(interface, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_if_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        if_description = ET.SubElement(interface, "if-description")
        if_description.text = kwargs.pop('if_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_actual_line_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        actual_line_speed = ET.SubElement(interface, "actual-line-speed")
        actual_line_speed.text = kwargs.pop('actual_line_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_configured_line_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        configured_line_speed = ET.SubElement(interface, "configured-line-speed")
        configured_line_speed.text = kwargs.pop('configured_line_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_line_duplex_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        line_duplex_state = ET.SubElement(interface, "line-duplex-state")
        line_duplex_state.text = kwargs.pop('line_duplex_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_flow_control(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        flow_control = ET.SubElement(interface, "flow-control")
        flow_control.text = kwargs.pop('flow_control')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_queuing_strategy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        queuing_strategy = ET.SubElement(interface, "queuing-strategy")
        queuing_strategy.text = kwargs.pop('queuing_strategy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_port_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        port_role = ET.SubElement(interface, "port-role")
        port_role.text = kwargs.pop('port_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_port_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        port_mode = ET.SubElement(interface, "port-mode")
        port_mode.text = kwargs.pop('port_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInOctets(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInOctets = ET.SubElement(interface, "ifHCInOctets")
        ifHCInOctets.text = kwargs.pop('ifHCInOctets')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInUcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInUcastPkts = ET.SubElement(interface, "ifHCInUcastPkts")
        ifHCInUcastPkts.text = kwargs.pop('ifHCInUcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInMulticastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInMulticastPkts = ET.SubElement(interface, "ifHCInMulticastPkts")
        ifHCInMulticastPkts.text = kwargs.pop('ifHCInMulticastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInBroadcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInBroadcastPkts = ET.SubElement(interface, "ifHCInBroadcastPkts")
        ifHCInBroadcastPkts.text = kwargs.pop('ifHCInBroadcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCInErrors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCInErrors = ET.SubElement(interface, "ifHCInErrors")
        ifHCInErrors.text = kwargs.pop('ifHCInErrors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutOctets(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutOctets = ET.SubElement(interface, "ifHCOutOctets")
        ifHCOutOctets.text = kwargs.pop('ifHCOutOctets')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutUcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutUcastPkts = ET.SubElement(interface, "ifHCOutUcastPkts")
        ifHCOutUcastPkts.text = kwargs.pop('ifHCOutUcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutMulticastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutMulticastPkts = ET.SubElement(interface, "ifHCOutMulticastPkts")
        ifHCOutMulticastPkts.text = kwargs.pop('ifHCOutMulticastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutBroadcastPkts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutBroadcastPkts = ET.SubElement(interface, "ifHCOutBroadcastPkts")
        ifHCOutBroadcastPkts.text = kwargs.pop('ifHCOutBroadcastPkts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_interface_ifHCOutErrors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ifHCOutErrors = ET.SubElement(interface, "ifHCOutErrors")
        ifHCOutErrors.text = kwargs.pop('ifHCOutErrors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_interface_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_interface_detail = ET.Element("get_interface_detail")
        config = get_interface_detail
        output = ET.SubElement(get_interface_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        input = ET.SubElement(get_media_detail, "input")
        interface_type = ET.SubElement(input, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        input = ET.SubElement(get_media_detail, "input")
        interface_name = ET.SubElement(input, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        input = ET.SubElement(get_media_detail, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        speed = ET.SubElement(sfp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        connector = ET.SubElement(sfp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        encoding = ET.SubElement(sfp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_name = ET.SubElement(sfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_oui = ET.SubElement(sfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_pn = ET.SubElement(sfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        vendor_rev = ET.SubElement(sfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        distance = ET.SubElement(sfp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        media_form_factor = ET.SubElement(sfp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        wavelength = ET.SubElement(sfp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        serial_no = ET.SubElement(sfp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        date_code = ET.SubElement(sfp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        temperature = ET.SubElement(sfp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        voltage = ET.SubElement(sfp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        current = ET.SubElement(sfp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        tx_power = ET.SubElement(sfp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_sfp_sfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        sfp = ET.SubElement(interface_identifier, "sfp")
        sfp = ET.SubElement(sfp, "sfp")
        rx_power = ET.SubElement(sfp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        speed = ET.SubElement(on_board, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        connector = ET.SubElement(on_board, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        encoding = ET.SubElement(on_board, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_name = ET.SubElement(on_board, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_oui = ET.SubElement(on_board, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_pn = ET.SubElement(on_board, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_on_board_on_board_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        on_board = ET.SubElement(interface_identifier, "on-board")
        on_board = ET.SubElement(on_board, "on-board")
        vendor_rev = ET.SubElement(on_board, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_name = ET.SubElement(gbc, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_oui = ET.SubElement(gbc, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_pn = ET.SubElement(gbc, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_gbic_gbc_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        gbic = ET.SubElement(interface_identifier, "gbic")
        gbc = ET.SubElement(gbic, "gbc")
        vendor_rev = ET.SubElement(gbc, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_name = ET.SubElement(xfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_oui = ET.SubElement(xfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_pn = ET.SubElement(xfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfp_xfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfp = ET.SubElement(interface_identifier, "xfp")
        xfp = ET.SubElement(xfp, "xfp")
        vendor_rev = ET.SubElement(xfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_name = ET.SubElement(xff, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_oui = ET.SubElement(xff, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_pn = ET.SubElement(xff, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xff_xff_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xff = ET.SubElement(interface_identifier, "xff")
        xff = ET.SubElement(xff, "xff")
        vendor_rev = ET.SubElement(xff, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_name = ET.SubElement(xfpe, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_oui = ET.SubElement(xfpe, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_pn = ET.SubElement(xfpe, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_xfpe_xfpe_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        xfpe = ET.SubElement(interface_identifier, "xfpe")
        xfpe = ET.SubElement(xfpe, "xfpe")
        vendor_rev = ET.SubElement(xfpe, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_name = ET.SubElement(unknown, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_oui = ET.SubElement(unknown, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_pn = ET.SubElement(unknown, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_unknown_unknown_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        unknown = ET.SubElement(interface_identifier, "unknown")
        unknown = ET.SubElement(unknown, "unknown")
        vendor_rev = ET.SubElement(unknown, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        speed = ET.SubElement(qsfp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        connector = ET.SubElement(qsfp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        encoding = ET.SubElement(qsfp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_name = ET.SubElement(qsfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_oui = ET.SubElement(qsfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_pn = ET.SubElement(qsfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        vendor_rev = ET.SubElement(qsfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        distance = ET.SubElement(qsfp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        media_form_factor = ET.SubElement(qsfp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        wavelength = ET.SubElement(qsfp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        serial_no = ET.SubElement(qsfp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        date_code = ET.SubElement(qsfp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        temperature = ET.SubElement(qsfp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        voltage = ET.SubElement(qsfp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        current = ET.SubElement(qsfp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        tx_power = ET.SubElement(qsfp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfp_qsfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfp = ET.SubElement(interface_identifier, "qsfp")
        qsfp = ET.SubElement(qsfp, "qsfp")
        rx_power = ET.SubElement(qsfp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        speed = ET.SubElement(qsfpp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        connector = ET.SubElement(qsfpp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        encoding = ET.SubElement(qsfpp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_name = ET.SubElement(qsfpp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_oui = ET.SubElement(qsfpp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_pn = ET.SubElement(qsfpp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        vendor_rev = ET.SubElement(qsfpp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        distance = ET.SubElement(qsfpp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        media_form_factor = ET.SubElement(qsfpp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        wavelength = ET.SubElement(qsfpp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        serial_no = ET.SubElement(qsfpp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        date_code = ET.SubElement(qsfpp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        temperature = ET.SubElement(qsfpp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        voltage = ET.SubElement(qsfpp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        current = ET.SubElement(qsfpp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        tx_power = ET.SubElement(qsfpp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_qsfpp_qsfpp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        qsfpp = ET.SubElement(interface_identifier, "qsfpp")
        qsfpp = ET.SubElement(qsfpp, "qsfpp")
        rx_power = ET.SubElement(qsfpp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        speed = ET.SubElement(cfp, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        connector = ET.SubElement(cfp, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        encoding = ET.SubElement(cfp, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_name = ET.SubElement(cfp, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_oui = ET.SubElement(cfp, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_pn = ET.SubElement(cfp, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        vendor_rev = ET.SubElement(cfp, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        distance = ET.SubElement(cfp, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        media_form_factor = ET.SubElement(cfp, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        wavelength = ET.SubElement(cfp, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        serial_no = ET.SubElement(cfp, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        date_code = ET.SubElement(cfp, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        temperature = ET.SubElement(cfp, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        voltage = ET.SubElement(cfp, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        current = ET.SubElement(cfp, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        tx_power = ET.SubElement(cfp, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp_cfp_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp = ET.SubElement(interface_identifier, "cfp")
        cfp = ET.SubElement(cfp, "cfp")
        rx_power = ET.SubElement(cfp, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        speed = ET.SubElement(cfp2, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_connector(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        connector = ET.SubElement(cfp2, "connector")
        connector.text = kwargs.pop('connector')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_encoding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        encoding = ET.SubElement(cfp2, "encoding")
        encoding.text = kwargs.pop('encoding')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_name = ET.SubElement(cfp2, "vendor-name")
        vendor_name.text = kwargs.pop('vendor_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_oui(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_oui = ET.SubElement(cfp2, "vendor-oui")
        vendor_oui.text = kwargs.pop('vendor_oui')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_pn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_pn = ET.SubElement(cfp2, "vendor-pn")
        vendor_pn.text = kwargs.pop('vendor_pn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_vendor_rev(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        vendor_rev = ET.SubElement(cfp2, "vendor-rev")
        vendor_rev.text = kwargs.pop('vendor_rev')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        distance = ET.SubElement(cfp2, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_media_form_factor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        media_form_factor = ET.SubElement(cfp2, "media-form-factor")
        media_form_factor.text = kwargs.pop('media_form_factor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_wavelength(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        wavelength = ET.SubElement(cfp2, "wavelength")
        wavelength.text = kwargs.pop('wavelength')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_serial_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        serial_no = ET.SubElement(cfp2, "serial-no")
        serial_no.text = kwargs.pop('serial_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_date_code(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        date_code = ET.SubElement(cfp2, "date-code")
        date_code.text = kwargs.pop('date_code')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_temperature(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        temperature = ET.SubElement(cfp2, "temperature")
        temperature.text = kwargs.pop('temperature')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_voltage(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        voltage = ET.SubElement(cfp2, "voltage")
        voltage.text = kwargs.pop('voltage')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_current(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        current = ET.SubElement(cfp2, "current")
        current.text = kwargs.pop('current')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_tx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        tx_power = ET.SubElement(cfp2, "tx-power")
        tx_power.text = kwargs.pop('tx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_media_detail_output_interface_interface_identifier_cfp2_cfp2_rx_power(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_media_detail = ET.Element("get_media_detail")
        config = get_media_detail
        output = ET.SubElement(get_media_detail, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_identifier = ET.SubElement(interface, "interface-identifier")
        cfp2 = ET.SubElement(interface_identifier, "cfp2")
        cfp2 = ET.SubElement(cfp2, "cfp2")
        rx_power = ET.SubElement(cfp2, "rx-power")
        rx_power.text = kwargs.pop('rx_power')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        