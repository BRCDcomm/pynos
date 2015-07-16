#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_vlan(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def vlan_classifier_rule_ruleid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid = ET.SubElement(rule, "ruleid")
        ruleid.text = kwargs.pop('ruleid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_mac_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        class_type = ET.SubElement(rule, "class-type")
        mac = ET.SubElement(class_type, "mac")
        mac = ET.SubElement(mac, "mac")
        address = ET.SubElement(mac, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_proto_proto_proto_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        class_type = ET.SubElement(rule, "class-type")
        proto = ET.SubElement(class_type, "proto")
        proto = ET.SubElement(proto, "proto")
        proto_val = ET.SubElement(proto, "proto-val")
        proto_val.text = kwargs.pop('proto_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_proto_proto_encap(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        class_type = ET.SubElement(rule, "class-type")
        proto = ET.SubElement(class_type, "proto")
        proto = ET.SubElement(proto, "proto")
        encap = ET.SubElement(proto, "encap")
        encap.text = kwargs.pop('encap')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_groupid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        groupid = ET.SubElement(group, "groupid")
        groupid.text = kwargs.pop('groupid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_oper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        oper = ET.SubElement(group, "oper")
        oper.text = kwargs.pop('oper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_rule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        rule_name = ET.SubElement(group, "rule-name")
        rule_name.text = kwargs.pop('rule_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_ruleid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        ruleid = ET.SubElement(group, "ruleid")
        ruleid.text = kwargs.pop('ruleid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_dot1q_tag_native(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        dot1q = ET.SubElement(vlan, "dot1q")
        tag = ET.SubElement(dot1q, "tag")
        native = ET.SubElement(tag, "native")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_ruleid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid = ET.SubElement(rule, "ruleid")
        ruleid.text = kwargs.pop('ruleid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_mac_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        class_type = ET.SubElement(rule, "class-type")
        mac = ET.SubElement(class_type, "mac")
        mac = ET.SubElement(mac, "mac")
        address = ET.SubElement(mac, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_proto_proto_proto_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        class_type = ET.SubElement(rule, "class-type")
        proto = ET.SubElement(class_type, "proto")
        proto = ET.SubElement(proto, "proto")
        proto_val = ET.SubElement(proto, "proto-val")
        proto_val.text = kwargs.pop('proto_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_rule_class_type_proto_proto_encap(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        rule = ET.SubElement(classifier, "rule")
        ruleid_key = ET.SubElement(rule, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        class_type = ET.SubElement(rule, "class-type")
        proto = ET.SubElement(class_type, "proto")
        proto = ET.SubElement(proto, "proto")
        encap = ET.SubElement(proto, "encap")
        encap.text = kwargs.pop('encap')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_groupid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        groupid = ET.SubElement(group, "groupid")
        groupid.text = kwargs.pop('groupid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_oper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        oper = ET.SubElement(group, "oper")
        oper.text = kwargs.pop('oper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_rule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        ruleid_key = ET.SubElement(group, "ruleid")
        ruleid_key.text = kwargs.pop('ruleid')
        rule_name = ET.SubElement(group, "rule-name")
        rule_name.text = kwargs.pop('rule_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_classifier_group_ruleid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        classifier = ET.SubElement(vlan, "classifier")
        group = ET.SubElement(classifier, "group")
        groupid_key = ET.SubElement(group, "groupid")
        groupid_key.text = kwargs.pop('groupid')
        oper_key = ET.SubElement(group, "oper")
        oper_key.text = kwargs.pop('oper')
        rule_name_key = ET.SubElement(group, "rule-name")
        rule_name_key.text = kwargs.pop('rule_name')
        ruleid = ET.SubElement(group, "ruleid")
        ruleid.text = kwargs.pop('ruleid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vlan_dot1q_tag_native(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vlan = ET.SubElement(config, "vlan", xmlns="urn:brocade.com:mgmt:brocade-vlan")
        dot1q = ET.SubElement(vlan, "dot1q")
        tag = ET.SubElement(dot1q, "tag")
        native = ET.SubElement(tag, "native")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        