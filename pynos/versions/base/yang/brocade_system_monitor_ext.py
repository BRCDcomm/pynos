#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_system_monitor_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_system_monitor_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        input = ET.SubElement(show_system_monitor, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        rbridge_id_out = ET.SubElement(switch_status, "rbridge-id-out")
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_name = ET.SubElement(switch_status, "switch-name")
        switch_name.text = kwargs.pop('switch_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_ip = ET.SubElement(switch_status, "switch-ip")
        switch_ip.text = kwargs.pop('switch_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_report_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        report_time = ET.SubElement(switch_status, "report-time")
        report_time.text = kwargs.pop('report_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_state = ET.SubElement(switch_status, "switch-state")
        switch_state.text = kwargs.pop('switch_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_state_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_state_reason = ET.SubElement(switch_status, "switch-state-reason")
        switch_state_reason.text = kwargs.pop('switch_state_reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_component_status_component_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        component_status = ET.SubElement(switch_status, "component-status")
        component_name = ET.SubElement(component_status, "component-name")
        component_name.text = kwargs.pop('component_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_component_status_component_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        component_status = ET.SubElement(switch_status, "component-status")
        component_state = ET.SubElement(component_status, "component-state")
        component_state.text = kwargs.pop('component_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_area(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        port_status = ET.SubElement(switch_status, "port-status")
        port_area = ET.SubElement(port_status, "port-area")
        port_area.text = kwargs.pop('port_area')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        port_status = ET.SubElement(switch_status, "port-status")
        port_name = ET.SubElement(port_status, "port-name")
        port_name.text = kwargs.pop('port_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        port_status = ET.SubElement(switch_status, "port-status")
        port_state = ET.SubElement(port_status, "port-state")
        port_state.text = kwargs.pop('port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        input = ET.SubElement(show_system_monitor, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        rbridge_id_out = ET.SubElement(switch_status, "rbridge-id-out")
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_name = ET.SubElement(switch_status, "switch-name")
        switch_name.text = kwargs.pop('switch_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_ip = ET.SubElement(switch_status, "switch-ip")
        switch_ip.text = kwargs.pop('switch_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_report_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        report_time = ET.SubElement(switch_status, "report-time")
        report_time.text = kwargs.pop('report_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_state = ET.SubElement(switch_status, "switch-state")
        switch_state.text = kwargs.pop('switch_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_switch_state_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        switch_state_reason = ET.SubElement(switch_status, "switch-state-reason")
        switch_state_reason.text = kwargs.pop('switch_state_reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_component_status_component_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        component_status = ET.SubElement(switch_status, "component-status")
        component_name = ET.SubElement(component_status, "component-name")
        component_name.text = kwargs.pop('component_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_component_status_component_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        component_status = ET.SubElement(switch_status, "component-status")
        component_state = ET.SubElement(component_status, "component-state")
        component_state.text = kwargs.pop('component_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_area(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        port_status = ET.SubElement(switch_status, "port-status")
        port_area = ET.SubElement(port_status, "port-area")
        port_area.text = kwargs.pop('port_area')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        port_status = ET.SubElement(switch_status, "port-status")
        port_name = ET.SubElement(port_status, "port-name")
        port_name.text = kwargs.pop('port_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_monitor_output_switch_status_port_status_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_monitor = ET.Element("show_system_monitor")
        config = show_system_monitor
        output = ET.SubElement(show_system_monitor, "output")
        switch_status = ET.SubElement(output, "switch-status")
        port_status = ET.SubElement(switch_status, "port-status")
        port_state = ET.SubElement(port_status, "port-state")
        port_state.text = kwargs.pop('port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        