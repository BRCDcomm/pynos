#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_port_profile_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_port_profile_for_intf_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_getnext_request_last_received_interface_info_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_interface_info = ET.SubElement(getnext_request, "last-received-interface-info")
        interface_type = ET.SubElement(last_received_interface_info, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_getnext_request_last_received_interface_info_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_interface_info = ET.SubElement(getnext_request, "last-received-interface-info")
        interface_name = ET.SubElement(last_received_interface_info, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        port_profile = ET.SubElement(interface, "port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        port_profile_name = ET.SubElement(input, "port-profile-name")
        port_profile_name.text = kwargs.pop('port_profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_port_profile_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        port_profile_status = ET.SubElement(input, "port-profile-status")
        port_profile_status.text = kwargs.pop('port_profile_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_request_type_getnext_request_last_received_port_profile_info_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_port_profile_info = ET.SubElement(getnext_request, "last-received-port-profile-info")
        profile_name = ET.SubElement(last_received_port_profile_info, "profile-name")
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_request_type_getnext_request_last_received_port_profile_info_profile_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_port_profile_info = ET.SubElement(getnext_request, "last-received-port-profile-info")
        profile_mac = ET.SubElement(last_received_port_profile_info, "profile-mac")
        profile_mac.text = kwargs.pop('profile_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_ppid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        ppid = ET.SubElement(port_profile, "ppid")
        ppid.text = kwargs.pop('ppid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_is_active(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        is_active = ET.SubElement(port_profile, "is-active")
        is_active.text = kwargs.pop('is_active')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        mac_association = ET.SubElement(port_profile, "mac-association")
        mac = ET.SubElement(mac_association, "mac")
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_applied_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        mac_association = ET.SubElement(port_profile, "mac-association")
        mac_key = ET.SubElement(mac_association, "mac")
        mac_key.text = kwargs.pop('mac')
        applied_interface = ET.SubElement(mac_association, "applied-interface")
        interface_type = ET.SubElement(applied_interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_applied_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        mac_association = ET.SubElement(port_profile, "mac-association")
        mac_key = ET.SubElement(mac_association, "mac")
        mac_key.text = kwargs.pop('mac')
        applied_interface = ET.SubElement(mac_association, "applied-interface")
        interface_name = ET.SubElement(applied_interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        has_more = ET.SubElement(port_profile, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_getnext_request_last_received_interface_info_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_interface_info = ET.SubElement(getnext_request, "last-received-interface-info")
        interface_type = ET.SubElement(last_received_interface_info, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_input_request_type_getnext_request_last_received_interface_info_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        input = ET.SubElement(get_port_profile_for_intf, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_interface_info = ET.SubElement(getnext_request, "last-received-interface-info")
        interface_name = ET.SubElement(last_received_interface_info, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_interface_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        port_profile = ET.SubElement(interface, "port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_for_intf_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_for_intf = ET.Element("get_port_profile_for_intf")
        config = get_port_profile_for_intf
        output = ET.SubElement(get_port_profile_for_intf, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        port_profile_name = ET.SubElement(input, "port-profile-name")
        port_profile_name.text = kwargs.pop('port_profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_port_profile_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        port_profile_status = ET.SubElement(input, "port-profile-status")
        port_profile_status.text = kwargs.pop('port_profile_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_request_type_getnext_request_last_received_port_profile_info_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_port_profile_info = ET.SubElement(getnext_request, "last-received-port-profile-info")
        profile_name = ET.SubElement(last_received_port_profile_info, "profile-name")
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_input_request_type_getnext_request_last_received_port_profile_info_profile_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        input = ET.SubElement(get_port_profile_status, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_received_port_profile_info = ET.SubElement(getnext_request, "last-received-port-profile-info")
        profile_mac = ET.SubElement(last_received_port_profile_info, "profile-mac")
        profile_mac.text = kwargs.pop('profile_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_ppid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        ppid = ET.SubElement(port_profile, "ppid")
        ppid.text = kwargs.pop('ppid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_is_active(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        is_active = ET.SubElement(port_profile, "is-active")
        is_active.text = kwargs.pop('is_active')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        mac_association = ET.SubElement(port_profile, "mac-association")
        mac = ET.SubElement(mac_association, "mac")
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_applied_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        mac_association = ET.SubElement(port_profile, "mac-association")
        mac_key = ET.SubElement(mac_association, "mac")
        mac_key.text = kwargs.pop('mac')
        applied_interface = ET.SubElement(mac_association, "applied-interface")
        interface_type = ET.SubElement(applied_interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_mac_association_applied_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        mac_association = ET.SubElement(port_profile, "mac-association")
        mac_key = ET.SubElement(mac_association, "mac")
        mac_key.text = kwargs.pop('mac')
        applied_interface = ET.SubElement(mac_association, "applied-interface")
        interface_name = ET.SubElement(applied_interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_profile_status_output_port_profile_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_profile_status = ET.Element("get_port_profile_status")
        config = get_port_profile_status
        output = ET.SubElement(get_port_profile_status, "output")
        port_profile = ET.SubElement(output, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        has_more = ET.SubElement(port_profile, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        