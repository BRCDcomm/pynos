#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_igmp_snooping(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def igmp_snooping_ip_igmp_snooping_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        igmp_snooping = ET.SubElement(config, "igmp-snooping", xmlns="urn:brocade.com:mgmt:brocade-igmp-snooping")
        ip = ET.SubElement(igmp_snooping, "ip")
        igmp = ET.SubElement(ip, "igmp")
        snooping = ET.SubElement(igmp, "snooping")
        enable = ET.SubElement(snooping, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def igmp_snooping_ip_igmp_snooping_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        igmp_snooping = ET.SubElement(config, "igmp-snooping", xmlns="urn:brocade.com:mgmt:brocade-igmp-snooping")
        ip = ET.SubElement(igmp_snooping, "ip")
        igmp = ET.SubElement(ip, "igmp")
        snooping = ET.SubElement(igmp, "snooping")
        enable = ET.SubElement(snooping, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        