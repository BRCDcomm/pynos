#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_mac_address_table(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def mac_address_table_static_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address = ET.SubElement(static, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_forward(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        forward = ET.SubElement(static, "forward")
        forward.text = kwargs.pop('forward')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        interface_type = ET.SubElement(static, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        interface_name = ET.SubElement(static, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        vlan = ET.SubElement(static, "vlan")
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_vlanid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid = ET.SubElement(static, "vlanid")
        vlanid.text = kwargs.pop('vlanid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_learning_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        learning_mode = ET.SubElement(mac_address_table, "learning-mode")
        learning_mode.text = kwargs.pop('learning_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_aging_time_conversational_time_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        aging_time = ET.SubElement(mac_address_table, "aging-time")
        conversational_time_out = ET.SubElement(aging_time, "conversational-time-out")
        conversational_time_out.text = kwargs.pop('conversational_time_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_aging_time_legacy_time_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        aging_time = ET.SubElement(mac_address_table, "aging-time")
        legacy_time_out = ET.SubElement(aging_time, "legacy-time-out")
        legacy_time_out.text = kwargs.pop('legacy_time_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_mac_move_mac_move_detect_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_move = ET.SubElement(mac_address_table, "mac-move")
        mac_move_detect_enable = ET.SubElement(mac_move, "mac-move-detect-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_mac_move_mac_move_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_move = ET.SubElement(mac_address_table, "mac-move")
        mac_move_limit = ET.SubElement(mac_move, "mac-move-limit")
        mac_move_limit.text = kwargs.pop('mac_move_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_consistency_check_mac_consistency_check_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        consistency_check = ET.SubElement(mac_address_table, "consistency-check")
        mac_consistency_check_suppress = ET.SubElement(consistency_check, "mac-consistency-check-suppress")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_consistency_check_mac_consistency_check_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        consistency_check = ET.SubElement(mac_address_table, "consistency-check")
        mac_consistency_check_interval = ET.SubElement(consistency_check, "mac-consistency-check-interval")
        mac_consistency_check_interval.text = kwargs.pop('mac_consistency_check_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_group_mac_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_group = ET.SubElement(config, "mac-group", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_group_id = ET.SubElement(mac_group, "mac-group-id")
        mac_group_id.text = kwargs.pop('mac_group_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_group_mac_group_entry_entry_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_group = ET.SubElement(config, "mac-group", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_group_id_key = ET.SubElement(mac_group, "mac-group-id")
        mac_group_id_key.text = kwargs.pop('mac_group_id')
        mac_group_entry = ET.SubElement(mac_group, "mac-group-entry")
        entry_address = ET.SubElement(mac_group_entry, "entry-address")
        entry_address.text = kwargs.pop('entry_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_request_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        mac_address = ET.SubElement(get_request, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        last_mac_address = ET.SubElement(last_mac_address_details, "last-mac-address")
        last_mac_address.text = kwargs.pop('last_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        last_vlan_id = ET.SubElement(last_mac_address_details, "last-vlan-id")
        last_vlan_id.text = kwargs.pop('last_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        last_mac_type = ET.SubElement(last_mac_address_details, "last-mac-type")
        last_mac_type.text = kwargs.pop('last_mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_vlanid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        vlanid = ET.SubElement(mac_address_table, "vlanid")
        vlanid.text = kwargs.pop('vlanid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address = ET.SubElement(mac_address_table, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        mac_type = ET.SubElement(mac_address_table, "mac-type")
        mac_type.text = kwargs.pop('mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        mac_state = ET.SubElement(mac_address_table, "mac-state")
        mac_state.text = kwargs.pop('mac_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_forwarding_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forwarding_interface = ET.SubElement(mac_address_table, "forwarding-interface")
        interface_type = ET.SubElement(forwarding_interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_forwarding_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forwarding_interface = ET.SubElement(mac_address_table, "forwarding-interface")
        interface_name = ET.SubElement(forwarding_interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address = ET.SubElement(static, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_forward(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        forward = ET.SubElement(static, "forward")
        forward.text = kwargs.pop('forward')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        interface_type = ET.SubElement(static, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        interface_name = ET.SubElement(static, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlanid_key = ET.SubElement(static, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        vlan = ET.SubElement(static, "vlan")
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_static_vlanid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        static = ET.SubElement(mac_address_table, "static")
        mac_address_key = ET.SubElement(static, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forward_key = ET.SubElement(static, "forward")
        forward_key.text = kwargs.pop('forward')
        interface_type_key = ET.SubElement(static, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(static, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        vlan_key = ET.SubElement(static, "vlan")
        vlan_key.text = kwargs.pop('vlan')
        vlanid = ET.SubElement(static, "vlanid")
        vlanid.text = kwargs.pop('vlanid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_learning_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        learning_mode = ET.SubElement(mac_address_table, "learning-mode")
        learning_mode.text = kwargs.pop('learning_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_aging_time_conversational_time_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        aging_time = ET.SubElement(mac_address_table, "aging-time")
        conversational_time_out = ET.SubElement(aging_time, "conversational-time-out")
        conversational_time_out.text = kwargs.pop('conversational_time_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_aging_time_legacy_time_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        aging_time = ET.SubElement(mac_address_table, "aging-time")
        legacy_time_out = ET.SubElement(aging_time, "legacy-time-out")
        legacy_time_out.text = kwargs.pop('legacy_time_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_mac_move_mac_move_detect_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_move = ET.SubElement(mac_address_table, "mac-move")
        mac_move_detect_enable = ET.SubElement(mac_move, "mac-move-detect-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_mac_move_mac_move_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_move = ET.SubElement(mac_address_table, "mac-move")
        mac_move_limit = ET.SubElement(mac_move, "mac-move-limit")
        mac_move_limit.text = kwargs.pop('mac_move_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_consistency_check_mac_consistency_check_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        consistency_check = ET.SubElement(mac_address_table, "consistency-check")
        mac_consistency_check_suppress = ET.SubElement(consistency_check, "mac-consistency-check-suppress")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_address_table_consistency_check_mac_consistency_check_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_address_table = ET.SubElement(config, "mac-address-table", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        consistency_check = ET.SubElement(mac_address_table, "consistency-check")
        mac_consistency_check_interval = ET.SubElement(consistency_check, "mac-consistency-check-interval")
        mac_consistency_check_interval.text = kwargs.pop('mac_consistency_check_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_group_mac_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_group = ET.SubElement(config, "mac-group", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_group_id = ET.SubElement(mac_group, "mac-group-id")
        mac_group_id.text = kwargs.pop('mac_group_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_group_mac_group_entry_entry_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac_group = ET.SubElement(config, "mac-group", xmlns="urn:brocade.com:mgmt:brocade-mac-address-table")
        mac_group_id_key = ET.SubElement(mac_group, "mac-group-id")
        mac_group_id_key.text = kwargs.pop('mac_group_id')
        mac_group_entry = ET.SubElement(mac_group, "mac-group-entry")
        entry_address = ET.SubElement(mac_group_entry, "entry-address")
        entry_address.text = kwargs.pop('entry_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_request_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        mac_address = ET.SubElement(get_request, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        last_mac_address = ET.SubElement(last_mac_address_details, "last-mac-address")
        last_mac_address.text = kwargs.pop('last_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        last_vlan_id = ET.SubElement(last_mac_address_details, "last-vlan-id")
        last_vlan_id.text = kwargs.pop('last_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_input_request_type_get_next_request_last_mac_address_details_last_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        input = ET.SubElement(get_mac_address_table, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_mac_address_details = ET.SubElement(get_next_request, "last-mac-address-details")
        last_mac_type = ET.SubElement(last_mac_address_details, "last-mac-type")
        last_mac_type.text = kwargs.pop('last_mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_vlanid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        vlanid = ET.SubElement(mac_address_table, "vlanid")
        vlanid.text = kwargs.pop('vlanid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address = ET.SubElement(mac_address_table, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        mac_type = ET.SubElement(mac_address_table, "mac-type")
        mac_type.text = kwargs.pop('mac_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_mac_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        mac_state = ET.SubElement(mac_address_table, "mac-state")
        mac_state.text = kwargs.pop('mac_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_forwarding_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forwarding_interface = ET.SubElement(mac_address_table, "forwarding-interface")
        interface_type = ET.SubElement(forwarding_interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_mac_address_table_forwarding_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        mac_address_table = ET.SubElement(output, "mac-address-table")
        vlanid_key = ET.SubElement(mac_address_table, "vlanid")
        vlanid_key.text = kwargs.pop('vlanid')
        mac_address_key = ET.SubElement(mac_address_table, "mac-address")
        mac_address_key.text = kwargs.pop('mac_address')
        forwarding_interface = ET.SubElement(mac_address_table, "forwarding-interface")
        interface_name = ET.SubElement(forwarding_interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_address_table_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_address_table = ET.Element("get_mac_address_table")
        config = get_mac_address_table
        output = ET.SubElement(get_mac_address_table, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        