#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_preprovision(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def preprovision_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        preprovision = ET.SubElement(config, "preprovision", xmlns="urn:brocade.com:mgmt:brocade-preprovision")
        rbridge_id = ET.SubElement(preprovision, "rbridge-id")
        wwn_key = ET.SubElement(rbridge_id, "wwn")
        wwn_key.text = kwargs.pop('wwn')
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def preprovision_rbridge_id_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        preprovision = ET.SubElement(config, "preprovision", xmlns="urn:brocade.com:mgmt:brocade-preprovision")
        rbridge_id = ET.SubElement(preprovision, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        wwn = ET.SubElement(rbridge_id, "wwn")
        wwn.text = kwargs.pop('wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_bare_metal_state_output_bare_metal_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_bare_metal_state = ET.Element("show_bare_metal_state")
        config = show_bare_metal_state
        output = ET.SubElement(show_bare_metal_state, "output")
        bare_metal_state = ET.SubElement(output, "bare-metal-state")
        bare_metal_state.text = kwargs.pop('bare_metal_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def preprovision_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        preprovision = ET.SubElement(config, "preprovision", xmlns="urn:brocade.com:mgmt:brocade-preprovision")
        rbridge_id = ET.SubElement(preprovision, "rbridge-id")
        wwn_key = ET.SubElement(rbridge_id, "wwn")
        wwn_key.text = kwargs.pop('wwn')
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def preprovision_rbridge_id_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        preprovision = ET.SubElement(config, "preprovision", xmlns="urn:brocade.com:mgmt:brocade-preprovision")
        rbridge_id = ET.SubElement(preprovision, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        wwn = ET.SubElement(rbridge_id, "wwn")
        wwn.text = kwargs.pop('wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_bare_metal_state_output_bare_metal_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_bare_metal_state = ET.Element("show_bare_metal_state")
        config = show_bare_metal_state
        output = ET.SubElement(show_bare_metal_state, "output")
        bare_metal_state = ET.SubElement(output, "bare-metal-state")
        bare_metal_state.text = kwargs.pop('bare_metal_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        