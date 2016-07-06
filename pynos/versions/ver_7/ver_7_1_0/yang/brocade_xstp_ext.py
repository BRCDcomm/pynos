#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_xstp_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_stp_brief_info_input_request_type_getnext_request_last_rcvd_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        input = ET.SubElement(get_stp_brief_info, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_rcvd_instance = ET.SubElement(getnext_request, "last-rcvd-instance")
        instance_id = ET.SubElement(last_rcvd_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_stp_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        stp_mode = ET.SubElement(spanning_tree_info, "stp-mode")
        stp_mode.text = kwargs.pop('stp_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        transmit_hold_count = ET.SubElement(rstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        migrate_time = ET.SubElement(rstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        transmit_hold_count = ET.SubElement(mstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        migrate_time = ET.SubElement(mstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id = ET.SubElement(pvstp, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        transmit_hold_count = ET.SubElement(pvstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        migrate_time = ET.SubElement(pvstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id = ET.SubElement(rpvstp, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        transmit_hold_count = ET.SubElement(rpvstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        migrate_time = ET.SubElement(rpvstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_last_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        last_instance = ET.SubElement(output, "last-instance")
        instance_id = ET.SubElement(last_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_input_request_type_getnext_request_last_rcvd_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        input = ET.SubElement(get_stp_mst_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_rcvd_instance = ET.SubElement(getnext_request, "last-rcvd-instance")
        instance_id = ET.SubElement(last_rcvd_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        cist_root_id = ET.SubElement(cist, "cist-root-id")
        cist_root_id.text = kwargs.pop('cist_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        cist_bridge_id = ET.SubElement(cist, "cist-bridge-id")
        cist_bridge_id.text = kwargs.pop('cist_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_reg_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        cist_reg_root_id = ET.SubElement(cist, "cist-reg-root-id")
        cist_reg_root_id.text = kwargs.pop('cist_reg_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_root_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        root_forward_delay = ET.SubElement(cist, "root-forward-delay")
        root_forward_delay.text = kwargs.pop('root_forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        hello_time = ET.SubElement(cist, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        max_age = ET.SubElement(cist, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_max_hops(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        max_hops = ET.SubElement(cist, "max-hops")
        max_hops.text = kwargs.pop('max_hops')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        migrate_time = ET.SubElement(cist, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id = ET.SubElement(msti, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        msti_root_id = ET.SubElement(msti, "msti-root-id")
        msti_root_id.text = kwargs.pop('msti_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        msti_bridge_id = ET.SubElement(msti, "msti-bridge-id")
        msti_bridge_id.text = kwargs.pop('msti_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        msti_bridge_priority = ET.SubElement(msti, "msti-bridge-priority")
        msti_bridge_priority.text = kwargs.pop('msti_bridge_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_last_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        last_instance = ET.SubElement(output, "last-instance")
        instance_id = ET.SubElement(last_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_input_request_type_getnext_request_last_rcvd_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        input = ET.SubElement(get_stp_brief_info, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_rcvd_instance = ET.SubElement(getnext_request, "last-rcvd-instance")
        instance_id = ET.SubElement(last_rcvd_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_stp_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        stp_mode = ET.SubElement(spanning_tree_info, "stp-mode")
        stp_mode.text = kwargs.pop('stp_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        root_bridge = ET.SubElement(stp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        bridge = ET.SubElement(stp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_stp_stp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        stp = ET.SubElement(spanning_tree_mode, "stp")
        stp = ET.SubElement(stp, "stp")
        port = ET.SubElement(stp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        root_bridge = ET.SubElement(rstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        bridge = ET.SubElement(rstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        transmit_hold_count = ET.SubElement(rstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        migrate_time = ET.SubElement(rstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rstp_rstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rstp = ET.SubElement(spanning_tree_mode, "rstp")
        rstp = ET.SubElement(rstp, "rstp")
        port = ET.SubElement(rstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        root_bridge = ET.SubElement(mstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        bridge = ET.SubElement(mstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        transmit_hold_count = ET.SubElement(mstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        migrate_time = ET.SubElement(mstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_mstp_mstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        mstp = ET.SubElement(spanning_tree_mode, "mstp")
        mstp = ET.SubElement(mstp, "mstp")
        port = ET.SubElement(mstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id = ET.SubElement(pvstp, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(pvstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(pvstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        transmit_hold_count = ET.SubElement(pvstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        migrate_time = ET.SubElement(pvstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_pvstp_pvstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        pvstp = ET.SubElement(spanning_tree_mode, "pvstp")
        pvstp = ET.SubElement(pvstp, "pvstp")
        vlan_id_key = ET.SubElement(pvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(pvstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id = ET.SubElement(rpvstp, "vlan-id")
        vlan_id.text = kwargs.pop('vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        priority = ET.SubElement(root_bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        bridge_id = ET.SubElement(root_bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        hello_time = ET.SubElement(root_bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        max_age = ET.SubElement(root_bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_root_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        root_bridge = ET.SubElement(rpvstp, "root-bridge")
        forward_delay = ET.SubElement(root_bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        priority = ET.SubElement(bridge, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        bridge_id = ET.SubElement(bridge, "bridge-id")
        bridge_id.text = kwargs.pop('bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        hello_time = ET.SubElement(bridge, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        max_age = ET.SubElement(bridge, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_bridge_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        bridge = ET.SubElement(rpvstp, "bridge")
        forward_delay = ET.SubElement(bridge, "forward-delay")
        forward_delay.text = kwargs.pop('forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_transmit_hold_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        transmit_hold_count = ET.SubElement(rpvstp, "transmit-hold-count")
        transmit_hold_count.text = kwargs.pop('transmit_hold_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        migrate_time = ET.SubElement(rpvstp, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_spanning_tree_info_spanning_tree_mode_rpvstp_rpvstp_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        spanning_tree_info = ET.SubElement(output, "spanning-tree-info")
        spanning_tree_mode = ET.SubElement(spanning_tree_info, "spanning-tree-mode")
        rpvstp = ET.SubElement(spanning_tree_mode, "rpvstp")
        rpvstp = ET.SubElement(rpvstp, "rpvstp")
        vlan_id_key = ET.SubElement(rpvstp, "vlan-id")
        vlan_id_key.text = kwargs.pop('vlan_id')
        port = ET.SubElement(rpvstp, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_brief_info_output_last_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_brief_info = ET.Element("get_stp_brief_info")
        config = get_stp_brief_info
        output = ET.SubElement(get_stp_brief_info, "output")
        last_instance = ET.SubElement(output, "last-instance")
        instance_id = ET.SubElement(last_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_input_request_type_getnext_request_last_rcvd_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        input = ET.SubElement(get_stp_mst_detail, "input")
        request_type = ET.SubElement(input, "request-type")
        getnext_request = ET.SubElement(request_type, "getnext-request")
        last_rcvd_instance = ET.SubElement(getnext_request, "last-rcvd-instance")
        instance_id = ET.SubElement(last_rcvd_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        cist_root_id = ET.SubElement(cist, "cist-root-id")
        cist_root_id.text = kwargs.pop('cist_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        cist_bridge_id = ET.SubElement(cist, "cist-bridge-id")
        cist_bridge_id.text = kwargs.pop('cist_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_cist_reg_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        cist_reg_root_id = ET.SubElement(cist, "cist-reg-root-id")
        cist_reg_root_id.text = kwargs.pop('cist_reg_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_root_forward_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        root_forward_delay = ET.SubElement(cist, "root-forward-delay")
        root_forward_delay.text = kwargs.pop('root_forward_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        hello_time = ET.SubElement(cist, "hello-time")
        hello_time.text = kwargs.pop('hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_max_age(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        max_age = ET.SubElement(cist, "max-age")
        max_age.text = kwargs.pop('max_age')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_max_hops(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        max_hops = ET.SubElement(cist, "max-hops")
        max_hops.text = kwargs.pop('max_hops')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_migrate_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        migrate_time = ET.SubElement(cist, "migrate-time")
        migrate_time.text = kwargs.pop('migrate_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_cist_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        cist = ET.SubElement(output, "cist")
        port = ET.SubElement(cist, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id = ET.SubElement(msti, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_root_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        msti_root_id = ET.SubElement(msti, "msti-root-id")
        msti_root_id.text = kwargs.pop('msti_root_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        msti_bridge_id = ET.SubElement(msti, "msti-bridge-id")
        msti_bridge_id.text = kwargs.pop('msti_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_msti_bridge_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        msti_bridge_priority = ET.SubElement(msti, "msti-bridge-priority")
        msti_bridge_priority.text = kwargs.pop('msti_bridge_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        interface_type = ET.SubElement(port, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        interface_name = ET.SubElement(port, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_spanningtree_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        spanningtree_enabled = ET.SubElement(port, "spanningtree-enabled")
        spanningtree_enabled.text = kwargs.pop('spanningtree_enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        if_index = ET.SubElement(port, "if-index")
        if_index.text = kwargs.pop('if_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_interface_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        interface_id = ET.SubElement(port, "interface-id")
        interface_id.text = kwargs.pop('interface_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        if_role = ET.SubElement(port, "if-role")
        if_role.text = kwargs.pop('if_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_if_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        if_state = ET.SubElement(port, "if-state")
        if_state.text = kwargs.pop('if_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_external_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        external_path_cost = ET.SubElement(port, "external-path-cost")
        external_path_cost.text = kwargs.pop('external_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_internal_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        internal_path_cost = ET.SubElement(port, "internal-path-cost")
        internal_path_cost.text = kwargs.pop('internal_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_configured_path_cost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        configured_path_cost = ET.SubElement(port, "configured-path-cost")
        configured_path_cost.text = kwargs.pop('configured_path_cost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_designated_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        designated_port_id = ET.SubElement(port, "designated-port-id")
        designated_port_id.text = kwargs.pop('designated_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_port_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        port_priority = ET.SubElement(port, "port-priority")
        port_priority.text = kwargs.pop('port_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_designated_bridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        designated_bridge_id = ET.SubElement(port, "designated-bridge-id")
        designated_bridge_id.text = kwargs.pop('designated_bridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_port_hello_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        port_hello_time = ET.SubElement(port, "port-hello-time")
        port_hello_time.text = kwargs.pop('port_hello_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_forward_transitions_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        forward_transitions_count = ET.SubElement(port, "forward-transitions-count")
        forward_transitions_count.text = kwargs.pop('forward_transitions_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_received_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        received_stp_type = ET.SubElement(port, "received-stp-type")
        received_stp_type.text = kwargs.pop('received_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_transmitted_stp_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        transmitted_stp_type = ET.SubElement(port, "transmitted-stp-type")
        transmitted_stp_type.text = kwargs.pop('transmitted_stp_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_edge_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        edge_port = ET.SubElement(port, "edge-port")
        edge_port.text = kwargs.pop('edge_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_auto_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        auto_edge = ET.SubElement(port, "auto-edge")
        auto_edge.text = kwargs.pop('auto_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_admin_edge(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        admin_edge = ET.SubElement(port, "admin-edge")
        admin_edge.text = kwargs.pop('admin_edge')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_edge_delay(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        edge_delay = ET.SubElement(port, "edge-delay")
        edge_delay.text = kwargs.pop('edge_delay')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_configured_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        configured_root_guard = ET.SubElement(port, "configured-root-guard")
        configured_root_guard.text = kwargs.pop('configured_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_root_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        oper_root_guard = ET.SubElement(port, "oper-root-guard")
        oper_root_guard.text = kwargs.pop('oper_root_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_boundary_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        boundary_port = ET.SubElement(port, "boundary-port")
        boundary_port.text = kwargs.pop('boundary_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_bpdu_guard(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        oper_bpdu_guard = ET.SubElement(port, "oper-bpdu-guard")
        oper_bpdu_guard.text = kwargs.pop('oper_bpdu_guard')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_oper_bpdu_filter(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        oper_bpdu_filter = ET.SubElement(port, "oper-bpdu-filter")
        oper_bpdu_filter.text = kwargs.pop('oper_bpdu_filter')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_link_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        link_type = ET.SubElement(port, "link-type")
        link_type.text = kwargs.pop('link_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_rx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        rx_bpdu_count = ET.SubElement(port, "rx-bpdu-count")
        rx_bpdu_count.text = kwargs.pop('rx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_msti_port_tx_bpdu_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        msti = ET.SubElement(output, "msti")
        instance_id_key = ET.SubElement(msti, "instance-id")
        instance_id_key.text = kwargs.pop('instance_id')
        port = ET.SubElement(msti, "port")
        tx_bpdu_count = ET.SubElement(port, "tx-bpdu-count")
        tx_bpdu_count.text = kwargs.pop('tx_bpdu_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_stp_mst_detail_output_last_instance_instance_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_stp_mst_detail = ET.Element("get_stp_mst_detail")
        config = get_stp_mst_detail
        output = ET.SubElement(get_stp_mst_detail, "output")
        last_instance = ET.SubElement(output, "last-instance")
        instance_id = ET.SubElement(last_instance, "instance-id")
        instance_id.text = kwargs.pop('instance_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        