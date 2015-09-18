#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_entity(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_contained_in_ID_output_contained_in_ID(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_contained_in_ID = ET.Element("get_contained_in_ID")
        config = get_contained_in_ID
        output = ET.SubElement(get_contained_in_ID, "output")
        contained_in_ID = ET.SubElement(output, "contained-in-ID")
        contained_in_ID.text = kwargs.pop('contained_in_ID')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_contained_in_ID_output_contained_in_ID(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_contained_in_ID = ET.Element("get_contained_in_ID")
        config = get_contained_in_ID
        output = ET.SubElement(get_contained_in_ID, "output")
        contained_in_ID = ET.SubElement(output, "contained-in-ID")
        contained_in_ID.text = kwargs.pop('contained_in_ID')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        