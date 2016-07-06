#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_policer(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def police_priority_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name = ET.SubElement(police_priority_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri0_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri0_conform = ET.SubElement(conform, "map-pri0-conform")
        map_pri0_conform.text = kwargs.pop('map_pri0_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri1_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri1_conform = ET.SubElement(conform, "map-pri1-conform")
        map_pri1_conform.text = kwargs.pop('map_pri1_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri2_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri2_conform = ET.SubElement(conform, "map-pri2-conform")
        map_pri2_conform.text = kwargs.pop('map_pri2_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri3_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri3_conform = ET.SubElement(conform, "map-pri3-conform")
        map_pri3_conform.text = kwargs.pop('map_pri3_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri4_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri4_conform = ET.SubElement(conform, "map-pri4-conform")
        map_pri4_conform.text = kwargs.pop('map_pri4_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri5_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri5_conform = ET.SubElement(conform, "map-pri5-conform")
        map_pri5_conform.text = kwargs.pop('map_pri5_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri6_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri6_conform = ET.SubElement(conform, "map-pri6-conform")
        map_pri6_conform.text = kwargs.pop('map_pri6_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri7_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri7_conform = ET.SubElement(conform, "map-pri7-conform")
        map_pri7_conform.text = kwargs.pop('map_pri7_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri0_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri0_exceed = ET.SubElement(exceed, "map-pri0-exceed")
        map_pri0_exceed.text = kwargs.pop('map_pri0_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri1_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri1_exceed = ET.SubElement(exceed, "map-pri1-exceed")
        map_pri1_exceed.text = kwargs.pop('map_pri1_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri2_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri2_exceed = ET.SubElement(exceed, "map-pri2-exceed")
        map_pri2_exceed.text = kwargs.pop('map_pri2_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri3_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri3_exceed = ET.SubElement(exceed, "map-pri3-exceed")
        map_pri3_exceed.text = kwargs.pop('map_pri3_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri4_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri4_exceed = ET.SubElement(exceed, "map-pri4-exceed")
        map_pri4_exceed.text = kwargs.pop('map_pri4_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri5_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri5_exceed = ET.SubElement(exceed, "map-pri5-exceed")
        map_pri5_exceed.text = kwargs.pop('map_pri5_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri6_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri6_exceed = ET.SubElement(exceed, "map-pri6-exceed")
        map_pri6_exceed.text = kwargs.pop('map_pri6_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri7_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri7_exceed = ET.SubElement(exceed, "map-pri7-exceed")
        map_pri7_exceed.text = kwargs.pop('map_pri7_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def class_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        class_map = ET.SubElement(config, "class-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name = ET.SubElement(class_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def class_map_match_access_group_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        class_map = ET.SubElement(config, "class-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(class_map, "name")
        name_key.text = kwargs.pop('name')
        match = ET.SubElement(class_map, "match")
        access_group = ET.SubElement(match, "access-group")
        access_group_name = ET.SubElement(access_group, "access-group-name")
        access_group_name.text = kwargs.pop('access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_po_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name = ET.SubElement(policy_map, "po-name")
        po_name.text = kwargs.pop('po_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_cl_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class_el")
        cl_name = ET.SubElement(class_el, "cl-name")
        cl_name.text = kwargs.pop('cl_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_cir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        cir = ET.SubElement(police, "cir")
        cir.text = kwargs.pop('cir')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_cbs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        cbs = ET.SubElement(police, "cbs")
        cbs.text = kwargs.pop('cbs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_eir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        eir = ET.SubElement(police, "eir")
        eir.text = kwargs.pop('eir')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_ebs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        ebs = ET.SubElement(police, "ebs")
        ebs.text = kwargs.pop('ebs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_set_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        set_priority = ET.SubElement(police, "set-priority")
        set_priority.text = kwargs.pop('set_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        conform_set_dscp = ET.SubElement(police, "conform-set-dscp")
        conform_set_dscp.text = kwargs.pop('conform_set_dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_prec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        conform_set_prec = ET.SubElement(police, "conform-set-prec")
        conform_set_prec.text = kwargs.pop('conform_set_prec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_tc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        conform_set_tc = ET.SubElement(police, "conform-set-tc")
        conform_set_tc.text = kwargs.pop('conform_set_tc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        exceed_set_dscp = ET.SubElement(police, "exceed-set-dscp")
        exceed_set_dscp.text = kwargs.pop('exceed_set_dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_prec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        exceed_set_prec = ET.SubElement(police, "exceed-set-prec")
        exceed_set_prec.text = kwargs.pop('exceed_set_prec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_tc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        exceed_set_tc = ET.SubElement(police, "exceed-set-tc")
        exceed_set_tc.text = kwargs.pop('exceed_set_tc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_cos_tc_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        set = ET.SubElement(class_el, "set")
        set_cos_tc = ET.SubElement(set, "set_cos_tc")
        cos = ET.SubElement(set_cos_tc, "cos")
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_cos_tc_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        set = ET.SubElement(class_el, "set")
        set_cos_tc = ET.SubElement(set, "set_cos_tc")
        traffic_class = ET.SubElement(set_cos_tc, "traffic-class")
        traffic_class.text = kwargs.pop('traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_dscp_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        set = ET.SubElement(class_el, "set")
        set_dscp = ET.SubElement(set, "set_dscp")
        dscp = ET.SubElement(set_dscp, "dscp")
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_span_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        span = ET.SubElement(class_el, "span")
        session = ET.SubElement(span, "session")
        session.text = kwargs.pop('session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_cos_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        cos_mutation.text = kwargs.pop('cos_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_cos_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        cos_traffic_class.text = kwargs.pop('cos_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos.text = kwargs.pop('dscp_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class.text = kwargs.pop('dscp_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation.text = kwargs.pop('dscp_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_sflow(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        sflow = ET.SubElement(map, "sflow")
        sflow.text = kwargs.pop('sflow')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_shape_shaping_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        shape = ET.SubElement(class_el, "shape")
        shaping_rate = ET.SubElement(shape, "shaping_rate")
        shaping_rate.text = kwargs.pop('shaping_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_priority_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        priority_number = ET.SubElement(strict_priority, "priority-number")
        priority_number.text = kwargs.pop('priority_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_scheduler_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        scheduler_type = ET.SubElement(strict_priority, "scheduler-type")
        scheduler_type.text = kwargs.pop('scheduler_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class0 = ET.SubElement(strict_priority, "dwrr-traffic-class0")
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class1 = ET.SubElement(strict_priority, "dwrr-traffic-class1")
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class2 = ET.SubElement(strict_priority, "dwrr-traffic-class2")
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class3 = ET.SubElement(strict_priority, "dwrr-traffic-class3")
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class4 = ET.SubElement(strict_priority, "dwrr-traffic-class4")
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class5 = ET.SubElement(strict_priority, "dwrr-traffic-class5")
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class6 = ET.SubElement(strict_priority, "dwrr-traffic-class6")
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class_last(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class_last = ET.SubElement(strict_priority, "dwrr-traffic-class-last")
        dwrr_traffic_class_last.text = kwargs.pop('dwrr_traffic_class_last')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC1 = ET.SubElement(strict_priority, "TC1")
        TC1.text = kwargs.pop('TC1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC2 = ET.SubElement(strict_priority, "TC2")
        TC2.text = kwargs.pop('TC2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC3 = ET.SubElement(strict_priority, "TC3")
        TC3.text = kwargs.pop('TC3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC4 = ET.SubElement(strict_priority, "TC4")
        TC4.text = kwargs.pop('TC4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC5 = ET.SubElement(strict_priority, "TC5")
        TC5.text = kwargs.pop('TC5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC6 = ET.SubElement(strict_priority, "TC6")
        TC6.text = kwargs.pop('TC6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC7 = ET.SubElement(strict_priority, "TC7")
        TC7.text = kwargs.pop('TC7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_priority_mapping_table_imprt_cee(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        priority_mapping_table = ET.SubElement(class_el, "priority-mapping-table")
        imprt = ET.SubElement(priority_mapping_table, "import")
        cee = ET.SubElement(imprt, "cee")
        cee.text = kwargs.pop('cee')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        direction = ET.SubElement(service_policy, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_policy_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        policy_map_name = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name.text = kwargs.pop('policy_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_attach_rbridge_id_add_rb_add_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        attach = ET.SubElement(service_policy, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        add = ET.SubElement(rbridge_id, "add")
        rb_add_range = ET.SubElement(add, "rb-add-range")
        rb_add_range.text = kwargs.pop('rb_add_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_attach_rbridge_id_remove_rb_remove_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        attach = ET.SubElement(service_policy, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        remove = ET.SubElement(rbridge_id, "remove")
        rb_remove_range = ET.SubElement(remove, "rb-remove-range")
        rb_remove_range.text = kwargs.pop('rb_remove_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name = ET.SubElement(police_priority_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri0_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri0_conform = ET.SubElement(conform, "map-pri0-conform")
        map_pri0_conform.text = kwargs.pop('map_pri0_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri1_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri1_conform = ET.SubElement(conform, "map-pri1-conform")
        map_pri1_conform.text = kwargs.pop('map_pri1_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri2_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri2_conform = ET.SubElement(conform, "map-pri2-conform")
        map_pri2_conform.text = kwargs.pop('map_pri2_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri3_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri3_conform = ET.SubElement(conform, "map-pri3-conform")
        map_pri3_conform.text = kwargs.pop('map_pri3_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri4_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri4_conform = ET.SubElement(conform, "map-pri4-conform")
        map_pri4_conform.text = kwargs.pop('map_pri4_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri5_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri5_conform = ET.SubElement(conform, "map-pri5-conform")
        map_pri5_conform.text = kwargs.pop('map_pri5_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri6_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri6_conform = ET.SubElement(conform, "map-pri6-conform")
        map_pri6_conform.text = kwargs.pop('map_pri6_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_conform_map_pri7_conform(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        conform = ET.SubElement(police_priority_map, "conform")
        map_pri7_conform = ET.SubElement(conform, "map-pri7-conform")
        map_pri7_conform.text = kwargs.pop('map_pri7_conform')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri0_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri0_exceed = ET.SubElement(exceed, "map-pri0-exceed")
        map_pri0_exceed.text = kwargs.pop('map_pri0_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri1_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri1_exceed = ET.SubElement(exceed, "map-pri1-exceed")
        map_pri1_exceed.text = kwargs.pop('map_pri1_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri2_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri2_exceed = ET.SubElement(exceed, "map-pri2-exceed")
        map_pri2_exceed.text = kwargs.pop('map_pri2_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri3_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri3_exceed = ET.SubElement(exceed, "map-pri3-exceed")
        map_pri3_exceed.text = kwargs.pop('map_pri3_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri4_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri4_exceed = ET.SubElement(exceed, "map-pri4-exceed")
        map_pri4_exceed.text = kwargs.pop('map_pri4_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri5_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri5_exceed = ET.SubElement(exceed, "map-pri5-exceed")
        map_pri5_exceed.text = kwargs.pop('map_pri5_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri6_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri6_exceed = ET.SubElement(exceed, "map-pri6-exceed")
        map_pri6_exceed.text = kwargs.pop('map_pri6_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def police_priority_map_exceed_map_pri7_exceed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        police_priority_map = ET.SubElement(config, "police-priority-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(police_priority_map, "name")
        name_key.text = kwargs.pop('name')
        exceed = ET.SubElement(police_priority_map, "exceed")
        map_pri7_exceed = ET.SubElement(exceed, "map-pri7-exceed")
        map_pri7_exceed.text = kwargs.pop('map_pri7_exceed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def class_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        class_map = ET.SubElement(config, "class-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name = ET.SubElement(class_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def class_map_match_access_group_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        class_map = ET.SubElement(config, "class-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        name_key = ET.SubElement(class_map, "name")
        name_key.text = kwargs.pop('name')
        match = ET.SubElement(class_map, "match")
        access_group = ET.SubElement(match, "access-group")
        access_group_name = ET.SubElement(access_group, "access-group-name")
        access_group_name.text = kwargs.pop('access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_po_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name = ET.SubElement(policy_map, "po-name")
        po_name.text = kwargs.pop('po_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_cl_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name = ET.SubElement(class_el, "cl-name")
        cl_name.text = kwargs.pop('cl_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_cir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class_el")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        cir = ET.SubElement(police, "cir")
        cir.text = kwargs.pop('cir')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_cbs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        cbs = ET.SubElement(police, "cbs")
        cbs.text = kwargs.pop('cbs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_eir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        eir = ET.SubElement(police, "eir")
        eir.text = kwargs.pop('eir')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_ebs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        ebs = ET.SubElement(police, "ebs")
        ebs.text = kwargs.pop('ebs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_set_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        set_priority = ET.SubElement(police, "set-priority")
        set_priority.text = kwargs.pop('set_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        conform_set_dscp = ET.SubElement(police, "conform-set-dscp")
        conform_set_dscp.text = kwargs.pop('conform_set_dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_prec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        conform_set_prec = ET.SubElement(police, "conform-set-prec")
        conform_set_prec.text = kwargs.pop('conform_set_prec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_conform_set_tc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        conform_set_tc = ET.SubElement(police, "conform-set-tc")
        conform_set_tc.text = kwargs.pop('conform_set_tc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        exceed_set_dscp = ET.SubElement(police, "exceed-set-dscp")
        exceed_set_dscp.text = kwargs.pop('exceed_set_dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_prec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        exceed_set_prec = ET.SubElement(police, "exceed-set-prec")
        exceed_set_prec.text = kwargs.pop('exceed_set_prec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_police_exceed_set_tc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        police = ET.SubElement(class_el, "police")
        exceed_set_tc = ET.SubElement(police, "exceed-set-tc")
        exceed_set_tc.text = kwargs.pop('exceed_set_tc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_cos_tc_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        set = ET.SubElement(class_el, "set")
        set_cos_tc = ET.SubElement(set, "set_cos_tc")
        cos = ET.SubElement(set_cos_tc, "cos")
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_cos_tc_traffic_class_el(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        set = ET.SubElement(class_el, "set")
        set_cos_tc = ET.SubElement(set, "set_cos_tc")
        traffic_class = ET.SubElement(set_cos_tc, "traffic-class")
        traffic_class.text = kwargs.pop('traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_set_set_dscp_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        set = ET.SubElement(class_el, "set")
        set_dscp = ET.SubElement(set, "set_dscp")
        dscp = ET.SubElement(set_dscp, "dscp")
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_span_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        span = ET.SubElement(class_el, "span")
        session = ET.SubElement(span, "session")
        session.text = kwargs.pop('session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_cos_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        cos_mutation.text = kwargs.pop('cos_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_cos_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        cos_traffic_class.text = kwargs.pop('cos_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos.text = kwargs.pop('dscp_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class.text = kwargs.pop('dscp_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_dscp_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation.text = kwargs.pop('dscp_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_map_sflow(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        map = ET.SubElement(class_el, "map")
        sflow = ET.SubElement(map, "sflow")
        sflow.text = kwargs.pop('sflow')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_shape_shaping_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        shape = ET.SubElement(class_el, "shape")
        shaping_rate = ET.SubElement(shape, "shaping_rate")
        shaping_rate.text = kwargs.pop('shaping_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_priority_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        priority_number = ET.SubElement(strict_priority, "priority-number")
        priority_number.text = kwargs.pop('priority_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_scheduler_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        scheduler_type = ET.SubElement(strict_priority, "scheduler-type")
        scheduler_type.text = kwargs.pop('scheduler_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class0 = ET.SubElement(strict_priority, "dwrr-traffic-class0")
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class1 = ET.SubElement(strict_priority, "dwrr-traffic-class1")
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class2 = ET.SubElement(strict_priority, "dwrr-traffic-class2")
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class3 = ET.SubElement(strict_priority, "dwrr-traffic-class3")
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class4 = ET.SubElement(strict_priority, "dwrr-traffic-class4")
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class5 = ET.SubElement(strict_priority, "dwrr-traffic-class5")
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class6 = ET.SubElement(strict_priority, "dwrr-traffic-class6")
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_dwrr_traffic_class_last(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class_last = ET.SubElement(strict_priority, "dwrr-traffic-class-last")
        dwrr_traffic_class_last.text = kwargs.pop('dwrr_traffic_class_last')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC1 = ET.SubElement(strict_priority, "TC1")
        TC1.text = kwargs.pop('TC1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC2 = ET.SubElement(strict_priority, "TC2")
        TC2.text = kwargs.pop('TC2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC3 = ET.SubElement(strict_priority, "TC3")
        TC3.text = kwargs.pop('TC3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC4 = ET.SubElement(strict_priority, "TC4")
        TC4.text = kwargs.pop('TC4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC5 = ET.SubElement(strict_priority, "TC5")
        TC5.text = kwargs.pop('TC5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC6 = ET.SubElement(strict_priority, "TC6")
        TC6.text = kwargs.pop('TC6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_scheduler_strict_priority_TC7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        scheduler = ET.SubElement(class_el, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        TC7 = ET.SubElement(strict_priority, "TC7")
        TC7.text = kwargs.pop('TC7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def policy_map_class_priority_mapping_table_imprt_cee(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        policy_map = ET.SubElement(config, "policy-map", xmlns="urn:brocade.com:mgmt:brocade-policer")
        po_name_key = ET.SubElement(policy_map, "po-name")
        po_name_key.text = kwargs.pop('po_name')
        class_el = ET.SubElement(policy_map, "class")
        cl_name_key = ET.SubElement(class_el, "cl-name")
        cl_name_key.text = kwargs.pop('cl_name')
        priority_mapping_table = ET.SubElement(class_el, "priority-mapping-table")
        imprt = ET.SubElement(priority_mapping_table, "import")
        cee = ET.SubElement(imprt, "cee")
        cee.text = kwargs.pop('cee')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        direction = ET.SubElement(service_policy, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_policy_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        policy_map_name = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name.text = kwargs.pop('policy_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_attach_rbridge_id_add_rb_add_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        attach = ET.SubElement(service_policy, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        add = ET.SubElement(rbridge_id, "add")
        rb_add_range = ET.SubElement(add, "rb-add-range")
        rb_add_range.text = kwargs.pop('rb_add_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_qos_qos_service_policy_attach_rbridge_id_remove_rb_remove_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_qos = ET.SubElement(config, "system-qos", xmlns="urn:brocade.com:mgmt:brocade-policer")
        qos = ET.SubElement(system_qos, "qos")
        service_policy = ET.SubElement(qos, "service-policy")
        direction_key = ET.SubElement(service_policy, "direction")
        direction_key.text = kwargs.pop('direction')
        policy_map_name_key = ET.SubElement(service_policy, "policy-map-name")
        policy_map_name_key.text = kwargs.pop('policy_map_name')
        attach = ET.SubElement(service_policy, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        remove = ET.SubElement(rbridge_id, "remove")
        rb_remove_range = ET.SubElement(remove, "rb-remove-range")
        rb_remove_range.text = kwargs.pop('rb_remove_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        