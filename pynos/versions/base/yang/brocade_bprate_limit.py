#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_bprate_limit(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def bp_rate_limit_heavy_bp_rate_limit_slot_bp_rate_limit_slot_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bp_rate_limit = ET.SubElement(config, "bp-rate-limit", xmlns="urn:brocade.com:mgmt:brocade-bprate-limit")
        heavy = ET.SubElement(bp_rate_limit, "heavy")
        bp_rate_limit_slot = ET.SubElement(heavy, "bp-rate-limit-slot")
        bp_rate_limit_slot_num = ET.SubElement(bp_rate_limit_slot, "bp-rate-limit-slot-num")
        bp_rate_limit_slot_num.text = kwargs.pop('bp_rate_limit_slot_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bp_rate_limit_heavy_bp_rate_limit_slot_bp_rate_limit_slot_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bp_rate_limit = ET.SubElement(config, "bp-rate-limit", xmlns="urn:brocade.com:mgmt:brocade-bprate-limit")
        heavy = ET.SubElement(bp_rate_limit, "heavy")
        bp_rate_limit_slot = ET.SubElement(heavy, "bp-rate-limit-slot")
        bp_rate_limit_slot_num = ET.SubElement(bp_rate_limit_slot, "bp-rate-limit-slot-num")
        bp_rate_limit_slot_num.text = kwargs.pop('bp_rate_limit_slot_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        