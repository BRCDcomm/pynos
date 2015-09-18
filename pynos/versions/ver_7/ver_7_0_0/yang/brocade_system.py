#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_system(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_system_uptime_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        input = ET.SubElement(get_system_uptime, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_days(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        days = ET.SubElement(show_system_uptime, "days")
        days.text = kwargs.pop('days')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_hours(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        hours = ET.SubElement(show_system_uptime, "hours")
        hours.text = kwargs.pop('hours')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_minutes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        minutes = ET.SubElement(show_system_uptime, "minutes")
        minutes.text = kwargs.pop('minutes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_seconds(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        seconds = ET.SubElement(show_system_uptime, "seconds")
        seconds.text = kwargs.pop('seconds')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_cmd_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        cmd_error = ET.SubElement(output, "cmd-error")
        cmd_error.text = kwargs.pop('cmd_error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        input = ET.SubElement(get_system_uptime, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_days(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        days = ET.SubElement(show_system_uptime, "days")
        days.text = kwargs.pop('days')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_hours(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        hours = ET.SubElement(show_system_uptime, "hours")
        hours.text = kwargs.pop('hours')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_minutes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        minutes = ET.SubElement(show_system_uptime, "minutes")
        minutes.text = kwargs.pop('minutes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_show_system_uptime_seconds(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        show_system_uptime = ET.SubElement(output, "show-system-uptime")
        rbridge_id_key = ET.SubElement(show_system_uptime, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        seconds = ET.SubElement(show_system_uptime, "seconds")
        seconds.text = kwargs.pop('seconds')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_system_uptime_output_cmd_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_system_uptime = ET.Element("get_system_uptime")
        config = get_system_uptime
        output = ET.SubElement(get_system_uptime, "output")
        cmd_error = ET.SubElement(output, "cmd-error")
        cmd_error.text = kwargs.pop('cmd_error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        