#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_mld_snooping(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def mld_snooping_ipv6_mld_snooping_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mld_snooping = ET.SubElement(config, "mld-snooping", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
        ipv6 = ET.SubElement(mld_snooping, "ipv6")
        mld = ET.SubElement(ipv6, "mld")
        snooping = ET.SubElement(mld, "snooping")
        enable = ET.SubElement(snooping, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def mld_snooping_ipv6_mld_snooping_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        mld_snooping = ET.SubElement(config, "mld-snooping", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
        ipv6 = ET.SubElement(mld_snooping, "ipv6")
        mld = ET.SubElement(ipv6, "mld")
        snooping = ET.SubElement(mld, "snooping")
        enable = ET.SubElement(snooping, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        