#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_trilloam(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def l2traceroute_input_src_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        src_mac = ET.SubElement(input, "src-mac")
        src_mac.text = kwargs.pop('src_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_dest_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        dest_mac = ET.SubElement(input, "dest-mac")
        dest_mac.text = kwargs.pop('dest_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        vlan_id = ET.SubElement(input, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        src_ip = ET.SubElement(IP, "src-ip")
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        dest_ip = ET.SubElement(IP, "dest-ip")
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        l4protocol = ET.SubElement(IP, "l4protocol")
        l4protocol.text = kwargs.pop('l4protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4_src_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        l4_src_port = ET.SubElement(IP, "l4-src-port")
        l4_src_port.text = kwargs.pop('l4_src_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4_dest_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        l4_dest_port = ET.SubElement(IP, "l4-dest-port")
        l4_dest_port.text = kwargs.pop('l4_dest_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        output = ET.SubElement(l2traceroute, "output")
        session_id = ET.SubElement(output, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_l2traceroutedone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        output = ET.SubElement(l2traceroute, "output")
        l2traceroutedone = ET.SubElement(output, "l2traceroutedone")
        l2traceroutedone.text = kwargs.pop('l2traceroutedone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        output = ET.SubElement(l2traceroute, "output")
        reason = ET.SubElement(output, "reason")
        reason.text = kwargs.pop('reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        input = ET.SubElement(l2traceroute_result, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        rbridge_id = ET.SubElement(l2_hop, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_ingress_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        ingress = ET.SubElement(l2_hop, "ingress")
        interface_type = ET.SubElement(ingress, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_ingress_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        ingress = ET.SubElement(l2_hop, "ingress")
        interface_name = ET.SubElement(ingress, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_egress_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        egress = ET.SubElement(l2_hop, "egress")
        interface_type = ET.SubElement(egress, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_egress_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        egress = ET.SubElement(l2_hop, "egress")
        interface_name = ET.SubElement(egress, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_roundtriptime(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        roundtriptime = ET.SubElement(l2_hop, "roundtriptime")
        roundtriptime.text = kwargs.pop('roundtriptime')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2traceroutedone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2traceroutedone = ET.SubElement(output, "l2traceroutedone")
        l2traceroutedone.text = kwargs.pop('l2traceroutedone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        reason = ET.SubElement(output, "reason")
        reason.text = kwargs.pop('reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_src_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        src_mac = ET.SubElement(input, "src-mac")
        src_mac.text = kwargs.pop('src_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_dest_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        dest_mac = ET.SubElement(input, "dest-mac")
        dest_mac.text = kwargs.pop('dest_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        vlan_id = ET.SubElement(input, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        src_ip = ET.SubElement(IP, "src-ip")
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        dest_ip = ET.SubElement(IP, "dest-ip")
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        l4protocol = ET.SubElement(IP, "l4protocol")
        l4protocol.text = kwargs.pop('l4protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4_src_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        l4_src_port = ET.SubElement(IP, "l4-src-port")
        l4_src_port.text = kwargs.pop('l4_src_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_input_protocolType_IP_l4_dest_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        input = ET.SubElement(l2traceroute, "input")
        protocolType = ET.SubElement(input, "protocolType")
        IP = ET.SubElement(protocolType, "IP")
        l4_dest_port = ET.SubElement(IP, "l4-dest-port")
        l4_dest_port.text = kwargs.pop('l4_dest_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        output = ET.SubElement(l2traceroute, "output")
        session_id = ET.SubElement(output, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_l2traceroutedone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        output = ET.SubElement(l2traceroute, "output")
        l2traceroutedone = ET.SubElement(output, "l2traceroutedone")
        l2traceroutedone.text = kwargs.pop('l2traceroutedone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_output_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute = ET.Element("l2traceroute")
        config = l2traceroute
        output = ET.SubElement(l2traceroute, "output")
        reason = ET.SubElement(output, "reason")
        reason.text = kwargs.pop('reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        input = ET.SubElement(l2traceroute_result, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        rbridge_id = ET.SubElement(l2_hop, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_ingress_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        ingress = ET.SubElement(l2_hop, "ingress")
        interface_type = ET.SubElement(ingress, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_ingress_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        ingress = ET.SubElement(l2_hop, "ingress")
        interface_name = ET.SubElement(ingress, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_egress_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        egress = ET.SubElement(l2_hop, "egress")
        interface_type = ET.SubElement(egress, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_egress_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        egress = ET.SubElement(l2_hop, "egress")
        interface_name = ET.SubElement(egress, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2_hop_results_l2_hop_roundtriptime(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2_hop_results = ET.SubElement(output, "l2-hop-results")
        l2_hop = ET.SubElement(l2_hop_results, "l2-hop")
        roundtriptime = ET.SubElement(l2_hop, "roundtriptime")
        roundtriptime.text = kwargs.pop('roundtriptime')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_l2traceroutedone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        l2traceroutedone = ET.SubElement(output, "l2traceroutedone")
        l2traceroutedone.text = kwargs.pop('l2traceroutedone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def l2traceroute_result_output_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        l2traceroute_result = ET.Element("l2traceroute_result")
        config = l2traceroute_result
        output = ET.SubElement(l2traceroute_result, "output")
        reason = ET.SubElement(output, "reason")
        reason.text = kwargs.pop('reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        