#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_clock(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def clock_sa_clock_timezone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        clock_sa = ET.SubElement(config, "clock-sa", xmlns="urn:brocade.com:mgmt:brocade-clock")
        clock = ET.SubElement(clock_sa, "clock")
        timezone = ET.SubElement(clock, "timezone")
        timezone.text = kwargs.pop('timezone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        input = ET.SubElement(show_clock, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        output = ET.SubElement(show_clock, "output")
        clock_time = ET.SubElement(output, "clock-time")
        rbridge_id_out = ET.SubElement(clock_time, "rbridge-id-out")
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_current_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        output = ET.SubElement(show_clock, "output")
        clock_time = ET.SubElement(output, "clock-time")
        current_time = ET.SubElement(clock_time, "current-time")
        current_time.text = kwargs.pop('current_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_timezone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        output = ET.SubElement(show_clock, "output")
        clock_time = ET.SubElement(output, "clock-time")
        timezone = ET.SubElement(clock_time, "timezone")
        timezone.text = kwargs.pop('timezone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def clock_sa_clock_timezone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        clock_sa = ET.SubElement(config, "clock-sa", xmlns="urn:brocade.com:mgmt:brocade-clock")
        clock = ET.SubElement(clock_sa, "clock")
        timezone = ET.SubElement(clock, "timezone")
        timezone.text = kwargs.pop('timezone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        input = ET.SubElement(show_clock, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_rbridge_id_out(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        output = ET.SubElement(show_clock, "output")
        clock_time = ET.SubElement(output, "clock-time")
        rbridge_id_out = ET.SubElement(clock_time, "rbridge-id-out")
        rbridge_id_out.text = kwargs.pop('rbridge_id_out')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_current_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        output = ET.SubElement(show_clock, "output")
        clock_time = ET.SubElement(output, "clock-time")
        current_time = ET.SubElement(clock_time, "current-time")
        current_time.text = kwargs.pop('current_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_clock_output_clock_time_timezone(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_clock = ET.Element("show_clock")
        config = show_clock
        output = ET.SubElement(show_clock, "output")
        clock_time = ET.SubElement(output, "clock-time")
        timezone = ET.SubElement(clock_time, "timezone")
        timezone.text = kwargs.pop('timezone')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        