#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_span(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def monitor_session_session_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number = ET.SubElement(session, "session-number")
        session_number.text = kwargs.pop('session_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        description = ET.SubElement(session, "description")
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        source = ET.SubElement(span_command, "source")
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_src_tengigabitethernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        src_tengigabitethernet = ET.SubElement(span_command, "src-tengigabitethernet")
        src_tengigabitethernet.text = kwargs.pop('src_tengigabitethernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_src_tengigabitethernet_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        src_tengigabitethernet_val = ET.SubElement(span_command, "src-tengigabitethernet-val")
        src_tengigabitethernet_val.text = kwargs.pop('src_tengigabitethernet_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_destination(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        destination = ET.SubElement(span_command, "destination")
        destination.text = kwargs.pop('destination')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_tengigabitethernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        dest_tengigabitethernet = ET.SubElement(span_command, "dest-tengigabitethernet")
        dest_tengigabitethernet.text = kwargs.pop('dest_tengigabitethernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_tengigabitethernet_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        dest_tengigabitethernet_val = ET.SubElement(span_command, "dest-tengigabitethernet-val")
        dest_tengigabitethernet_val.text = kwargs.pop('dest_tengigabitethernet_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_vlan_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        dest_vlan_val = ET.SubElement(span_command, "dest-vlan-val")
        dest_vlan_val.text = kwargs.pop('dest_vlan_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        direction = ET.SubElement(span_command, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_session_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number = ET.SubElement(session, "session-number")
        session_number.text = kwargs.pop('session_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        description = ET.SubElement(session, "description")
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_source(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        source = ET.SubElement(span_command, "source")
        source.text = kwargs.pop('source')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_src_tengigabitethernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        src_tengigabitethernet = ET.SubElement(span_command, "src-tengigabitethernet")
        src_tengigabitethernet.text = kwargs.pop('src_tengigabitethernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_src_tengigabitethernet_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        src_tengigabitethernet_val = ET.SubElement(span_command, "src-tengigabitethernet-val")
        src_tengigabitethernet_val.text = kwargs.pop('src_tengigabitethernet_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_destination(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        destination = ET.SubElement(span_command, "destination")
        destination.text = kwargs.pop('destination')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_tengigabitethernet(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        dest_tengigabitethernet = ET.SubElement(span_command, "dest-tengigabitethernet")
        dest_tengigabitethernet.text = kwargs.pop('dest_tengigabitethernet')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_tengigabitethernet_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        dest_tengigabitethernet_val = ET.SubElement(span_command, "dest-tengigabitethernet-val")
        dest_tengigabitethernet_val.text = kwargs.pop('dest_tengigabitethernet_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_dest_vlan_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        dest_vlan_val = ET.SubElement(span_command, "dest-vlan-val")
        dest_vlan_val.text = kwargs.pop('dest_vlan_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def monitor_session_span_command_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        monitor = ET.SubElement(config, "monitor", xmlns="urn:brocade.com:mgmt:brocade-span")
        session = ET.SubElement(monitor, "session")
        session_number_key = ET.SubElement(session, "session-number")
        session_number_key.text = kwargs.pop('session_number')
        span_command = ET.SubElement(session, "span-command")
        direction = ET.SubElement(span_command, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        