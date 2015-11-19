#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ha(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def redundancy_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        input = ET.SubElement(redundancy, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_output_rd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        output = ET.SubElement(redundancy, "output")
        rd_status = ET.SubElement(output, "rd_status")
        rd_status.text = kwargs.pop('rd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_output_rd_mesg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        output = ET.SubElement(redundancy, "output")
        rd_mesg = ET.SubElement(output, "rd_mesg")
        rd_mesg.text = kwargs.pop('rd_mesg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        input = ET.SubElement(reload, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_system(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        input = ET.SubElement(reload, "input")
        system = ET.SubElement(input, "system")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_standby(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        input = ET.SubElement(reload, "input")
        standby = ET.SubElement(input, "standby")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        input = ET.SubElement(redundancy, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_output_rd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        output = ET.SubElement(redundancy, "output")
        rd_status = ET.SubElement(output, "rd_status")
        rd_status.text = kwargs.pop('rd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def redundancy_output_rd_mesg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        redundancy = ET.Element("redundancy")
        config = redundancy
        output = ET.SubElement(redundancy, "output")
        rd_mesg = ET.SubElement(output, "rd_mesg")
        rd_mesg.text = kwargs.pop('rd_mesg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        input = ET.SubElement(reload, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_system(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        input = ET.SubElement(reload, "input")
        system = ET.SubElement(input, "system")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def reload_input_standby(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        reload = ET.Element("reload")
        config = reload
        input = ET.SubElement(reload, "input")
        standby = ET.SubElement(input, "standby")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        