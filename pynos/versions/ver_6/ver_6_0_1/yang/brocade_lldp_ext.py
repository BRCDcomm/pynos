#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_lldp_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_lldp_neighbor_detail_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_next_request_last_rcvd_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_ifindex = ET.SubElement(get_next_request, "last-rcvd-ifindex")
        last_rcvd_ifindex.text = kwargs.pop('last_rcvd_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_rbridge_specific_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_rbridge_specific = ET.SubElement(request_type, "get-rbridge-specific")
        rbridge_id = ET.SubElement(get_rbridge_specific, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        local_interface_name = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name.text = kwargs.pop('local_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        local_interface_mac = ET.SubElement(lldp_neighbor_detail, "local-interface-mac")
        local_interface_mac.text = kwargs.pop('local_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        local_interface_ifindex = ET.SubElement(lldp_neighbor_detail, "local-interface-ifindex")
        local_interface_ifindex.text = kwargs.pop('local_interface_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name.text = kwargs.pop('remote_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_interface_mac = ET.SubElement(lldp_neighbor_detail, "remote-interface-mac")
        remote_interface_mac.text = kwargs.pop('remote_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_port_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_port_description = ET.SubElement(lldp_neighbor_detail, "remote-port-description")
        remote_port_description.text = kwargs.pop('remote_port_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_chassis_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_chassis_id = ET.SubElement(lldp_neighbor_detail, "remote-chassis-id")
        remote_chassis_id.text = kwargs.pop('remote_chassis_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_system_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_system_name = ET.SubElement(lldp_neighbor_detail, "remote-system-name")
        remote_system_name.text = kwargs.pop('remote_system_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_system_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_system_description = ET.SubElement(lldp_neighbor_detail, "remote-system-description")
        remote_system_description.text = kwargs.pop('remote_system_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_dead_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        dead_interval = ET.SubElement(lldp_neighbor_detail, "dead-interval")
        dead_interval.text = kwargs.pop('dead_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remaining_life(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remaining_life = ET.SubElement(lldp_neighbor_detail, "remaining-life")
        remaining_life.text = kwargs.pop('remaining_life')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_lldp_pdu_transmitted(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        lldp_pdu_transmitted = ET.SubElement(lldp_neighbor_detail, "lldp-pdu-transmitted")
        lldp_pdu_transmitted.text = kwargs.pop('lldp_pdu_transmitted')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_lldp_pdu_received(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        lldp_pdu_received = ET.SubElement(lldp_neighbor_detail, "lldp-pdu-received")
        lldp_pdu_received.text = kwargs.pop('lldp_pdu_received')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_request_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_type = ET.SubElement(get_request, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_request_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        interface_name = ET.SubElement(get_request, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_next_request_last_rcvd_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_ifindex = ET.SubElement(get_next_request, "last-rcvd-ifindex")
        last_rcvd_ifindex.text = kwargs.pop('last_rcvd_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_input_request_type_get_rbridge_specific_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        input = ET.SubElement(get_lldp_neighbor_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        get_rbridge_specific = ET.SubElement(request_type, "get-rbridge-specific")
        rbridge_id = ET.SubElement(get_rbridge_specific, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        local_interface_name = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name.text = kwargs.pop('local_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        local_interface_mac = ET.SubElement(lldp_neighbor_detail, "local-interface-mac")
        local_interface_mac.text = kwargs.pop('local_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_local_interface_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        local_interface_ifindex = ET.SubElement(lldp_neighbor_detail, "local-interface-ifindex")
        local_interface_ifindex.text = kwargs.pop('local_interface_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name.text = kwargs.pop('remote_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_interface_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_interface_mac = ET.SubElement(lldp_neighbor_detail, "remote-interface-mac")
        remote_interface_mac.text = kwargs.pop('remote_interface_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_port_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_port_description = ET.SubElement(lldp_neighbor_detail, "remote-port-description")
        remote_port_description.text = kwargs.pop('remote_port_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_chassis_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_chassis_id = ET.SubElement(lldp_neighbor_detail, "remote-chassis-id")
        remote_chassis_id.text = kwargs.pop('remote_chassis_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_system_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_system_name = ET.SubElement(lldp_neighbor_detail, "remote-system-name")
        remote_system_name.text = kwargs.pop('remote_system_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remote_system_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remote_system_description = ET.SubElement(lldp_neighbor_detail, "remote-system-description")
        remote_system_description.text = kwargs.pop('remote_system_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_dead_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        dead_interval = ET.SubElement(lldp_neighbor_detail, "dead-interval")
        dead_interval.text = kwargs.pop('dead_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_remaining_life(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        remaining_life = ET.SubElement(lldp_neighbor_detail, "remaining-life")
        remaining_life.text = kwargs.pop('remaining_life')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_lldp_pdu_transmitted(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        lldp_pdu_transmitted = ET.SubElement(lldp_neighbor_detail, "lldp-pdu-transmitted")
        lldp_pdu_transmitted.text = kwargs.pop('lldp_pdu_transmitted')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_lldp_neighbor_detail_lldp_pdu_received(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        lldp_neighbor_detail = ET.SubElement(output, "lldp-neighbor-detail")
        local_interface_name_key = ET.SubElement(lldp_neighbor_detail, "local-interface-name")
        local_interface_name_key.text = kwargs.pop('local_interface_name')
        remote_interface_name_key = ET.SubElement(lldp_neighbor_detail, "remote-interface-name")
        remote_interface_name_key.text = kwargs.pop('remote_interface_name')
        lldp_pdu_received = ET.SubElement(lldp_neighbor_detail, "lldp-pdu-received")
        lldp_pdu_received.text = kwargs.pop('lldp_pdu_received')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_lldp_neighbor_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_lldp_neighbor_detail = ET.Element("get_lldp_neighbor_detail")
        config = get_lldp_neighbor_detail
        output = ET.SubElement(get_lldp_neighbor_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        