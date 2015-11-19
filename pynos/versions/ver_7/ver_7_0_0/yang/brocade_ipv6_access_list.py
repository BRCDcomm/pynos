#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ipv6_access_list(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def ipv6_acl_ipv6_access_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name = ET.SubElement(standard, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_src_host_any_sip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_any_sip = ET.SubElement(seq, "src-host-any-sip")
        src_host_any_sip.text = kwargs.pop('src_host_any_sip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_src_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_ip = ET.SubElement(seq, "src-host-ip")
        src_host_ip.text = kwargs.pop('src_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_src_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mask = ET.SubElement(seq, "src-mask")
        src_mask.text = kwargs.pop('src_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name = ET.SubElement(extended, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_protocol_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        protocol_type = ET.SubElement(seq, "protocol-type")
        protocol_type.text = kwargs.pop('protocol_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_src_host_any_sip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_any_sip = ET.SubElement(seq, "src-host-any-sip")
        src_host_any_sip.text = kwargs.pop('src_host_any_sip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_src_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_ip = ET.SubElement(seq, "src-host-ip")
        src_host_ip.text = kwargs.pop('src_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_src_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mask = ET.SubElement(seq, "src-mask")
        src_mask.text = kwargs.pop('src_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport = ET.SubElement(seq, "sport")
        sport.text = kwargs.pop('sport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_eq_neq_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_eq_neq_tcp = ET.SubElement(seq, "sport-number-eq-neq-tcp")
        sport_number_eq_neq_tcp.text = kwargs.pop('sport_number_eq_neq_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_lt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_lt_tcp = ET.SubElement(seq, "sport-number-lt-tcp")
        sport_number_lt_tcp.text = kwargs.pop('sport_number_lt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_gt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_gt_tcp = ET.SubElement(seq, "sport-number-gt-tcp")
        sport_number_gt_tcp.text = kwargs.pop('sport_number_gt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_eq_neq_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_eq_neq_udp = ET.SubElement(seq, "sport-number-eq-neq-udp")
        sport_number_eq_neq_udp.text = kwargs.pop('sport_number_eq_neq_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_lt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_lt_udp = ET.SubElement(seq, "sport-number-lt-udp")
        sport_number_lt_udp.text = kwargs.pop('sport_number_lt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_gt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_gt_udp = ET.SubElement(seq, "sport-number-gt-udp")
        sport_number_gt_udp.text = kwargs.pop('sport_number_gt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_lower_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_lower_tcp = ET.SubElement(seq, "sport-number-range-lower-tcp")
        sport_number_range_lower_tcp.text = kwargs.pop('sport_number_range_lower_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_lower_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_lower_udp = ET.SubElement(seq, "sport-number-range-lower-udp")
        sport_number_range_lower_udp.text = kwargs.pop('sport_number_range_lower_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_higher_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_higher_tcp = ET.SubElement(seq, "sport-number-range-higher-tcp")
        sport_number_range_higher_tcp.text = kwargs.pop('sport_number_range_higher_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_higher_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_higher_udp = ET.SubElement(seq, "sport-number-range-higher-udp")
        sport_number_range_higher_udp.text = kwargs.pop('sport_number_range_higher_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dst_host_any_dip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_host_any_dip = ET.SubElement(seq, "dst-host-any-dip")
        dst_host_any_dip.text = kwargs.pop('dst_host_any_dip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dst_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_host_ip = ET.SubElement(seq, "dst-host-ip")
        dst_host_ip.text = kwargs.pop('dst_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dst_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_mask = ET.SubElement(seq, "dst-mask")
        dst_mask.text = kwargs.pop('dst_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport = ET.SubElement(seq, "dport")
        dport.text = kwargs.pop('dport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_eq_neq_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_eq_neq_tcp = ET.SubElement(seq, "dport-number-eq-neq-tcp")
        dport_number_eq_neq_tcp.text = kwargs.pop('dport_number_eq_neq_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_lt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_lt_tcp = ET.SubElement(seq, "dport-number-lt-tcp")
        dport_number_lt_tcp.text = kwargs.pop('dport_number_lt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_gt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_gt_tcp = ET.SubElement(seq, "dport-number-gt-tcp")
        dport_number_gt_tcp.text = kwargs.pop('dport_number_gt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_eq_neq_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_eq_neq_udp = ET.SubElement(seq, "dport-number-eq-neq-udp")
        dport_number_eq_neq_udp.text = kwargs.pop('dport_number_eq_neq_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_lt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_lt_udp = ET.SubElement(seq, "dport-number-lt-udp")
        dport_number_lt_udp.text = kwargs.pop('dport_number_lt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_gt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_gt_udp = ET.SubElement(seq, "dport-number-gt-udp")
        dport_number_gt_udp.text = kwargs.pop('dport_number_gt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_lower_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_lower_tcp = ET.SubElement(seq, "dport-number-range-lower-tcp")
        dport_number_range_lower_tcp.text = kwargs.pop('dport_number_range_lower_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_lower_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_lower_udp = ET.SubElement(seq, "dport-number-range-lower-udp")
        dport_number_range_lower_udp.text = kwargs.pop('dport_number_range_lower_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_higher_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_higher_tcp = ET.SubElement(seq, "dport-number-range-higher-tcp")
        dport_number_range_higher_tcp.text = kwargs.pop('dport_number_range_higher_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_higher_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_higher_udp = ET.SubElement(seq, "dport-number-range-higher-udp")
        dport_number_range_higher_udp.text = kwargs.pop('dport_number_range_higher_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dscp = ET.SubElement(seq, "dscp")
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_urg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        urg = ET.SubElement(seq, "urg")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_ack(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        ack = ET.SubElement(seq, "ack")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_push(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        push = ET.SubElement(seq, "push")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_fin(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        fin = ET.SubElement(seq, "fin")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_rst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        rst = ET.SubElement(seq, "rst")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sync = ET.SubElement(seq, "sync")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        vlan = ET.SubElement(seq, "vlan")
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name = ET.SubElement(standard, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_src_host_any_sip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_any_sip = ET.SubElement(seq, "src-host-any-sip")
        src_host_any_sip.text = kwargs.pop('src_host_any_sip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_src_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_ip = ET.SubElement(seq, "src-host-ip")
        src_host_ip.text = kwargs.pop('src_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_src_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mask = ET.SubElement(seq, "src-mask")
        src_mask.text = kwargs.pop('src_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_standard_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        standard = ET.SubElement(access_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(standard, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name = ET.SubElement(extended, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_seq_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id = ET.SubElement(seq, "seq-id")
        seq_id.text = kwargs.pop('seq_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        action = ET.SubElement(seq, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_protocol_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        protocol_type = ET.SubElement(seq, "protocol-type")
        protocol_type.text = kwargs.pop('protocol_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_src_host_any_sip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_any_sip = ET.SubElement(seq, "src-host-any-sip")
        src_host_any_sip.text = kwargs.pop('src_host_any_sip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_src_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_host_ip = ET.SubElement(seq, "src-host-ip")
        src_host_ip.text = kwargs.pop('src_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_src_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        src_mask = ET.SubElement(seq, "src-mask")
        src_mask.text = kwargs.pop('src_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport = ET.SubElement(seq, "sport")
        sport.text = kwargs.pop('sport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_eq_neq_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_eq_neq_tcp = ET.SubElement(seq, "sport-number-eq-neq-tcp")
        sport_number_eq_neq_tcp.text = kwargs.pop('sport_number_eq_neq_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_lt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_lt_tcp = ET.SubElement(seq, "sport-number-lt-tcp")
        sport_number_lt_tcp.text = kwargs.pop('sport_number_lt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_gt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_gt_tcp = ET.SubElement(seq, "sport-number-gt-tcp")
        sport_number_gt_tcp.text = kwargs.pop('sport_number_gt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_eq_neq_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_eq_neq_udp = ET.SubElement(seq, "sport-number-eq-neq-udp")
        sport_number_eq_neq_udp.text = kwargs.pop('sport_number_eq_neq_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_lt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_lt_udp = ET.SubElement(seq, "sport-number-lt-udp")
        sport_number_lt_udp.text = kwargs.pop('sport_number_lt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_gt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_gt_udp = ET.SubElement(seq, "sport-number-gt-udp")
        sport_number_gt_udp.text = kwargs.pop('sport_number_gt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_lower_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_lower_tcp = ET.SubElement(seq, "sport-number-range-lower-tcp")
        sport_number_range_lower_tcp.text = kwargs.pop('sport_number_range_lower_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_lower_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_lower_udp = ET.SubElement(seq, "sport-number-range-lower-udp")
        sport_number_range_lower_udp.text = kwargs.pop('sport_number_range_lower_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_higher_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_higher_tcp = ET.SubElement(seq, "sport-number-range-higher-tcp")
        sport_number_range_higher_tcp.text = kwargs.pop('sport_number_range_higher_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sport_number_range_higher_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sport_number_range_higher_udp = ET.SubElement(seq, "sport-number-range-higher-udp")
        sport_number_range_higher_udp.text = kwargs.pop('sport_number_range_higher_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dst_host_any_dip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_host_any_dip = ET.SubElement(seq, "dst-host-any-dip")
        dst_host_any_dip.text = kwargs.pop('dst_host_any_dip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dst_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_host_ip = ET.SubElement(seq, "dst-host-ip")
        dst_host_ip.text = kwargs.pop('dst_host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dst_mask(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dst_mask = ET.SubElement(seq, "dst-mask")
        dst_mask.text = kwargs.pop('dst_mask')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport = ET.SubElement(seq, "dport")
        dport.text = kwargs.pop('dport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_eq_neq_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_eq_neq_tcp = ET.SubElement(seq, "dport-number-eq-neq-tcp")
        dport_number_eq_neq_tcp.text = kwargs.pop('dport_number_eq_neq_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_lt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_lt_tcp = ET.SubElement(seq, "dport-number-lt-tcp")
        dport_number_lt_tcp.text = kwargs.pop('dport_number_lt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_gt_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_gt_tcp = ET.SubElement(seq, "dport-number-gt-tcp")
        dport_number_gt_tcp.text = kwargs.pop('dport_number_gt_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_eq_neq_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_eq_neq_udp = ET.SubElement(seq, "dport-number-eq-neq-udp")
        dport_number_eq_neq_udp.text = kwargs.pop('dport_number_eq_neq_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_lt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_lt_udp = ET.SubElement(seq, "dport-number-lt-udp")
        dport_number_lt_udp.text = kwargs.pop('dport_number_lt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_gt_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_gt_udp = ET.SubElement(seq, "dport-number-gt-udp")
        dport_number_gt_udp.text = kwargs.pop('dport_number_gt_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_lower_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_lower_tcp = ET.SubElement(seq, "dport-number-range-lower-tcp")
        dport_number_range_lower_tcp.text = kwargs.pop('dport_number_range_lower_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_lower_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_lower_udp = ET.SubElement(seq, "dport-number-range-lower-udp")
        dport_number_range_lower_udp.text = kwargs.pop('dport_number_range_lower_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_higher_tcp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_higher_tcp = ET.SubElement(seq, "dport-number-range-higher-tcp")
        dport_number_range_higher_tcp.text = kwargs.pop('dport_number_range_higher_tcp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dport_number_range_higher_udp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dport_number_range_higher_udp = ET.SubElement(seq, "dport-number-range-higher-udp")
        dport_number_range_higher_udp.text = kwargs.pop('dport_number_range_higher_udp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        dscp = ET.SubElement(seq, "dscp")
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_urg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        urg = ET.SubElement(seq, "urg")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_ack(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        ack = ET.SubElement(seq, "ack")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_push(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        push = ET.SubElement(seq, "push")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_fin(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        fin = ET.SubElement(seq, "fin")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_rst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        rst = ET.SubElement(seq, "rst")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        sync = ET.SubElement(seq, "sync")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        vlan = ET.SubElement(seq, "vlan")
        vlan.text = kwargs.pop('vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        count = ET.SubElement(seq, "count")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_acl_ipv6_access_list_extended_seq_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6_acl = ET.SubElement(config, "ipv6-acl", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
        ipv6 = ET.SubElement(ipv6_acl, "ipv6")
        access_list = ET.SubElement(ipv6, "access-list")
        extended = ET.SubElement(access_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq = ET.SubElement(extended, "seq")
        seq_id_key = ET.SubElement(seq, "seq-id")
        seq_id_key.text = kwargs.pop('seq_id')
        log = ET.SubElement(seq, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        