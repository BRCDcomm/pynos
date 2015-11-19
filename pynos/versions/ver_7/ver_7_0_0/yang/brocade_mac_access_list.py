#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_mac_access_list(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def mac_access_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name = ET.SubElement(standard, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        source = ET.SubElement(seq, "source")
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_srchost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        srchost = ET.SubElement(seq, "srchost")
        srchost.text = kwargs.pop('srchost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_src_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mac_addr_mask = ET.SubElement(seq, "src-mac-addr-mask")
        src_mac_addr_mask.text = kwargs.pop('src_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name = ET.SubElement(extended, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        source = ET.SubElement(seq, "source")
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_srchost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        srchost = ET.SubElement(seq, "srchost")
        srchost.text = kwargs.pop('srchost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_src_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mac_addr_mask = ET.SubElement(seq, "src-mac-addr-mask")
        src_mac_addr_mask.text = kwargs.pop('src_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst = ET.SubElement(seq, "dst")
        dst.text = kwargs.pop('dst')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dsthost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dsthost = ET.SubElement(seq, "dsthost")
        dsthost.text = kwargs.pop('dsthost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dst_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_mac_addr_mask = ET.SubElement(seq, "dst-mac-addr-mask")
        dst_mac_addr_mask.text = kwargs.pop('dst_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_ethertype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        ethertype = ET.SubElement(seq, "ethertype")
        ethertype.text = kwargs.pop('ethertype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        vlan = ET.SubElement(seq, "vlan")
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        interface_type = ET.SubElement(input, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        interface_name = ET.SubElement(input, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        direction = ET.SubElement(input, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_ingress_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ingress_policy = ET.SubElement(interface, "ingress-policy")
        policy_name = ET.SubElement(ingress_policy, "policy-name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_egress_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        egress_policy = ET.SubElement(interface, "egress-policy")
        policy_name = ET.SubElement(egress_policy, "policy-name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name = ET.SubElement(standard, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        source = ET.SubElement(seq, "source")
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_srchost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        srchost = ET.SubElement(seq, "srchost")
        srchost.text = kwargs.pop('srchost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_src_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mac_addr_mask = ET.SubElement(seq, "src-mac-addr-mask")
        src_mac_addr_mask.text = kwargs.pop('src_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_standard_hide_mac_acl_std_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_std = ET.SubElement(standard, "hide-mac-acl-std")
        seq = ET.SubElement(hide_mac_acl_std, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name = ET.SubElement(extended, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        source = ET.SubElement(seq, "source")
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_srchost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        srchost = ET.SubElement(seq, "srchost")
        srchost.text = kwargs.pop('srchost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_src_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mac_addr_mask = ET.SubElement(seq, "src-mac-addr-mask")
        src_mac_addr_mask.text = kwargs.pop('src_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst = ET.SubElement(seq, "dst")
        dst.text = kwargs.pop('dst')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dsthost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dsthost = ET.SubElement(seq, "dsthost")
        dsthost.text = kwargs.pop('dsthost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_dst_mac_addr_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_mac_addr_mask = ET.SubElement(seq, "dst-mac-addr-mask")
        dst_mac_addr_mask.text = kwargs.pop('dst_mac_addr_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_ethertype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        ethertype = ET.SubElement(seq, "ethertype")
        ethertype.text = kwargs.pop('ethertype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        vlan = ET.SubElement(seq, "vlan")
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mac_access_list_extended_hide_mac_acl_ext_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mac = ET.SubElement(config, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
        access_list = ET.SubElement(mac, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        hide_mac_acl_ext = ET.SubElement(extended, "hide-mac-acl-ext")
        seq = ET.SubElement(hide_mac_acl_ext, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        interface_type = ET.SubElement(input, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        interface_name = ET.SubElement(input, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_input_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        input = ET.SubElement(get_mac_acl_for_intf, "input")
        direction = ET.SubElement(input, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        interface_type = ET.SubElement(interface, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name = ET.SubElement(interface, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_ingress_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        ingress_policy = ET.SubElement(interface, "ingress-policy")
        policy_name = ET.SubElement(ingress_policy, "policy-name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_mac_acl_for_intf_output_interface_egress_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_mac_acl_for_intf = ET.Element("get_mac_acl_for_intf")
        config = get_mac_acl_for_intf
        output = ET.SubElement(get_mac_acl_for_intf, "output")
        interface = ET.SubElement(output, "interface")
        interface_type_key = ET.SubElement(interface, "interface-type")
        interface_type_key.text = kwargs.pop('interface_type')
        interface_name_key = ET.SubElement(interface, "interface-name")
        interface_name_key.text = kwargs.pop('interface_name')
        egress_policy = ET.SubElement(interface, "egress-policy")
        policy_name = ET.SubElement(egress_policy, "policy-name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        