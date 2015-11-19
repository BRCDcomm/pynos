#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_maps_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def maps_get_all_policy_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_all_policy = ET.Element("maps_get_all_policy")
        config = maps_get_all_policy
        input = ET.SubElement(maps_get_all_policy, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_all_policy_output_policy_policyname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_all_policy = ET.Element("maps_get_all_policy")
        config = maps_get_all_policy
        output = ET.SubElement(maps_get_all_policy, "output")
        policy = ET.SubElement(output, "policy")
        policyname = ET.SubElement(policy, "policyname")
        policyname.text = kwargs.pop('policyname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        input = ET.SubElement(maps_get_default_rules, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        rbridgeid = ET.SubElement(rules, "rbridgeid")
        rbridgeid.text = kwargs.pop('rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_rulename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        rulename = ET.SubElement(rules, "rulename")
        rulename.text = kwargs.pop('rulename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        groupname = ET.SubElement(rules, "groupname")
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_monitor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        monitor = ET.SubElement(rules, "monitor")
        monitor.text = kwargs.pop('monitor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_op(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        op = ET.SubElement(rules, "op")
        op.text = kwargs.pop('op')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        value = ET.SubElement(rules, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        action = ET.SubElement(rules, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_timebase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        timebase = ET.SubElement(rules, "timebase")
        timebase.text = kwargs.pop('timebase')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_policyname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        policyname = ET.SubElement(rules, "policyname")
        policyname.text = kwargs.pop('policyname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_all_policy_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_all_policy = ET.Element("maps_get_all_policy")
        config = maps_get_all_policy
        input = ET.SubElement(maps_get_all_policy, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_all_policy_output_policy_policyname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_all_policy = ET.Element("maps_get_all_policy")
        config = maps_get_all_policy
        output = ET.SubElement(maps_get_all_policy, "output")
        policy = ET.SubElement(output, "policy")
        policyname = ET.SubElement(policy, "policyname")
        policyname.text = kwargs.pop('policyname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        input = ET.SubElement(maps_get_default_rules, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        rbridgeid = ET.SubElement(rules, "rbridgeid")
        rbridgeid.text = kwargs.pop('rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_rulename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        rulename = ET.SubElement(rules, "rulename")
        rulename.text = kwargs.pop('rulename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        groupname = ET.SubElement(rules, "groupname")
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_monitor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        monitor = ET.SubElement(rules, "monitor")
        monitor.text = kwargs.pop('monitor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_op(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        op = ET.SubElement(rules, "op")
        op.text = kwargs.pop('op')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        value = ET.SubElement(rules, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        action = ET.SubElement(rules, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_timebase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        timebase = ET.SubElement(rules, "timebase")
        timebase.text = kwargs.pop('timebase')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def maps_get_default_rules_output_rules_policyname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        maps_get_default_rules = ET.Element("maps_get_default_rules")
        config = maps_get_default_rules
        output = ET.SubElement(maps_get_default_rules, "output")
        rules = ET.SubElement(output, "rules")
        policyname = ET.SubElement(rules, "policyname")
        policyname.text = kwargs.pop('policyname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        