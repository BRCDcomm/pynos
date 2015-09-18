#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_threshold_monitor(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def threshold_monitor_hidden_threshold_monitor_sfp_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        apply = ET.SubElement(sfp, "apply")
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        pause = ET.SubElement(sfp, "pause")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name = ET.SubElement(policy, "policy_name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        type = ET.SubElement(area, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value = ET.SubElement(area, "area_value")
        area_value.text = kwargs.pop('area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        high_threshold = ET.SubElement(threshold, "high-threshold")
        high_threshold.text = kwargs.pop('high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        low_threshold = ET.SubElement(threshold, "low-threshold")
        low_threshold.text = kwargs.pop('low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        buffer = ET.SubElement(threshold, "buffer")
        buffer.text = kwargs.pop('buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_above_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        above_highthresh_action = ET.SubElement(above, "above-highthresh-action")
        above_highthresh_action.text = kwargs.pop('above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_below_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_highthresh_action = ET.SubElement(below, "below-highthresh-action")
        below_highthresh_action.text = kwargs.pop('below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_below_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_lowthresh_action = ET.SubElement(below, "below-lowthresh-action")
        below_lowthresh_action.text = kwargs.pop('below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        apply = ET.SubElement(security, "apply")
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        pause = ET.SubElement(security, "pause")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_sec_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name.text = kwargs.pop('sec_policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_sec_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value = ET.SubElement(area, "sec_area_value")
        sec_area_value.text = kwargs.pop('sec_area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_timebase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        timebase = ET.SubElement(area, "timebase")
        timebase.text = kwargs.pop('timebase')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        threshold = ET.SubElement(area, "threshold")
        sec_high_threshold = ET.SubElement(threshold, "sec-high-threshold")
        sec_high_threshold.text = kwargs.pop('sec_high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        threshold = ET.SubElement(area, "threshold")
        sec_low_threshold = ET.SubElement(threshold, "sec-low-threshold")
        sec_low_threshold.text = kwargs.pop('sec_low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        threshold = ET.SubElement(area, "threshold")
        sec_buffer = ET.SubElement(threshold, "sec-buffer")
        sec_buffer.text = kwargs.pop('sec_buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_above_sec_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        sec_above_highthresh_action = ET.SubElement(above, "sec-above-highthresh-action")
        sec_above_highthresh_action.text = kwargs.pop('sec_above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_below_sec_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        sec_below_highthresh_action = ET.SubElement(below, "sec-below-highthresh-action")
        sec_below_highthresh_action.text = kwargs.pop('sec_below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_below_sec_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        sec_below_lowthresh_action = ET.SubElement(below, "sec-below-lowthresh-action")
        sec_below_lowthresh_action.text = kwargs.pop('sec_below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_poll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        poll = ET.SubElement(Cpu, "poll")
        poll.text = kwargs.pop('poll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        retry = ET.SubElement(Cpu, "retry")
        retry.text = kwargs.pop('retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        limit = ET.SubElement(Cpu, "limit")
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_actions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        actions = ET.SubElement(Cpu, "actions")
        actions.text = kwargs.pop('actions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_poll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        poll = ET.SubElement(Memory, "poll")
        poll.text = kwargs.pop('poll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        retry = ET.SubElement(Memory, "retry")
        retry.text = kwargs.pop('retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        limit = ET.SubElement(Memory, "limit")
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_high_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        high_limit = ET.SubElement(Memory, "high-limit")
        high_limit.text = kwargs.pop('high_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_low_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        low_limit = ET.SubElement(Memory, "low-limit")
        low_limit.text = kwargs.pop('low_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_actions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        actions = ET.SubElement(Memory, "actions")
        actions.text = kwargs.pop('actions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        apply = ET.SubElement(interface, "apply")
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        pause = ET.SubElement(interface, "pause")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name = ET.SubElement(policy, "policy_name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        type = ET.SubElement(area, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value = ET.SubElement(area, "area_value")
        area_value.text = kwargs.pop('area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_timebase_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        timebase_value = ET.SubElement(threshold, "timebase_value")
        timebase_value.text = kwargs.pop('timebase_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        high_threshold = ET.SubElement(threshold, "high-threshold")
        high_threshold.text = kwargs.pop('high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        low_threshold = ET.SubElement(threshold, "low-threshold")
        low_threshold.text = kwargs.pop('low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        buffer = ET.SubElement(threshold, "buffer")
        buffer.text = kwargs.pop('buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_above_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        above_highthresh_action = ET.SubElement(above, "above-highthresh-action")
        above_highthresh_action.text = kwargs.pop('above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_above_above_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        above_lowthresh_action = ET.SubElement(above, "above-lowthresh-action")
        above_lowthresh_action.text = kwargs.pop('above_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_below_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_highthresh_action = ET.SubElement(below, "below-highthresh-action")
        below_highthresh_action.text = kwargs.pop('below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_below_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_lowthresh_action = ET.SubElement(below, "below-lowthresh-action")
        below_lowthresh_action.text = kwargs.pop('below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        apply = ET.SubElement(sfp, "apply")
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        pause = ET.SubElement(sfp, "pause")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name = ET.SubElement(policy, "policy_name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        type = ET.SubElement(area, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value = ET.SubElement(area, "area_value")
        area_value.text = kwargs.pop('area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        high_threshold = ET.SubElement(threshold, "high-threshold")
        high_threshold.text = kwargs.pop('high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        low_threshold = ET.SubElement(threshold, "low-threshold")
        low_threshold.text = kwargs.pop('low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_threshold_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        buffer = ET.SubElement(threshold, "buffer")
        buffer.text = kwargs.pop('buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_above_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        above_highthresh_action = ET.SubElement(above, "above-highthresh-action")
        above_highthresh_action.text = kwargs.pop('above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_below_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_highthresh_action = ET.SubElement(below, "below-highthresh-action")
        below_highthresh_action.text = kwargs.pop('below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_sfp_policy_area_alert_below_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        sfp = ET.SubElement(threshold_monitor, "sfp")
        policy = ET.SubElement(sfp, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_lowthresh_action = ET.SubElement(below, "below-lowthresh-action")
        below_lowthresh_action.text = kwargs.pop('below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        apply = ET.SubElement(security, "apply")
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        pause = ET.SubElement(security, "pause")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_sec_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name.text = kwargs.pop('sec_policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_sec_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value = ET.SubElement(area, "sec_area_value")
        sec_area_value.text = kwargs.pop('sec_area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_timebase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        timebase = ET.SubElement(area, "timebase")
        timebase.text = kwargs.pop('timebase')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        threshold = ET.SubElement(area, "threshold")
        sec_high_threshold = ET.SubElement(threshold, "sec-high-threshold")
        sec_high_threshold.text = kwargs.pop('sec_high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        threshold = ET.SubElement(area, "threshold")
        sec_low_threshold = ET.SubElement(threshold, "sec-low-threshold")
        sec_low_threshold.text = kwargs.pop('sec_low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_threshold_sec_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        threshold = ET.SubElement(area, "threshold")
        sec_buffer = ET.SubElement(threshold, "sec-buffer")
        sec_buffer.text = kwargs.pop('sec_buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_above_sec_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        sec_above_highthresh_action = ET.SubElement(above, "sec-above-highthresh-action")
        sec_above_highthresh_action.text = kwargs.pop('sec_above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_below_sec_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        sec_below_highthresh_action = ET.SubElement(below, "sec-below-highthresh-action")
        sec_below_highthresh_action.text = kwargs.pop('sec_below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_security_policy_area_alert_below_sec_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        security = ET.SubElement(threshold_monitor, "security")
        policy = ET.SubElement(security, "policy")
        sec_policy_name_key = ET.SubElement(policy, "sec_policy_name")
        sec_policy_name_key.text = kwargs.pop('sec_policy_name')
        area = ET.SubElement(policy, "area")
        sec_area_value_key = ET.SubElement(area, "sec_area_value")
        sec_area_value_key.text = kwargs.pop('sec_area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        sec_below_lowthresh_action = ET.SubElement(below, "sec-below-lowthresh-action")
        sec_below_lowthresh_action.text = kwargs.pop('sec_below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_poll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        poll = ET.SubElement(Cpu, "poll")
        poll.text = kwargs.pop('poll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        retry = ET.SubElement(Cpu, "retry")
        retry.text = kwargs.pop('retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        limit = ET.SubElement(Cpu, "limit")
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Cpu_actions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Cpu = ET.SubElement(threshold_monitor, "Cpu")
        actions = ET.SubElement(Cpu, "actions")
        actions.text = kwargs.pop('actions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_poll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        poll = ET.SubElement(Memory, "poll")
        poll.text = kwargs.pop('poll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        retry = ET.SubElement(Memory, "retry")
        retry.text = kwargs.pop('retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        limit = ET.SubElement(Memory, "limit")
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_high_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        high_limit = ET.SubElement(Memory, "high-limit")
        high_limit.text = kwargs.pop('high_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_low_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        low_limit = ET.SubElement(Memory, "low-limit")
        low_limit.text = kwargs.pop('low_limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_Memory_actions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        Memory = ET.SubElement(threshold_monitor, "Memory")
        actions = ET.SubElement(Memory, "actions")
        actions.text = kwargs.pop('actions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_apply(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        apply = ET.SubElement(interface, "apply")
        apply.text = kwargs.pop('apply')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_pause(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        pause = ET.SubElement(interface, "pause")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_policy_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name = ET.SubElement(policy, "policy_name")
        policy_name.text = kwargs.pop('policy_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        type = ET.SubElement(area, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_area_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value = ET.SubElement(area, "area_value")
        area_value.text = kwargs.pop('area_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_timebase_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        timebase_value = ET.SubElement(threshold, "timebase_value")
        timebase_value.text = kwargs.pop('timebase_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_high_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        high_threshold = ET.SubElement(threshold, "high-threshold")
        high_threshold.text = kwargs.pop('high_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_low_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        low_threshold = ET.SubElement(threshold, "low-threshold")
        low_threshold.text = kwargs.pop('low_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_threshold_buffer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        threshold = ET.SubElement(area, "threshold")
        buffer = ET.SubElement(threshold, "buffer")
        buffer.text = kwargs.pop('buffer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_above_above_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        above_highthresh_action = ET.SubElement(above, "above-highthresh-action")
        above_highthresh_action.text = kwargs.pop('above_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_above_above_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        above = ET.SubElement(alert, "above")
        above_lowthresh_action = ET.SubElement(above, "above-lowthresh-action")
        above_lowthresh_action.text = kwargs.pop('above_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_below_below_highthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_highthresh_action = ET.SubElement(below, "below-highthresh-action")
        below_highthresh_action.text = kwargs.pop('below_highthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def threshold_monitor_hidden_threshold_monitor_interface_policy_area_alert_below_below_lowthresh_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        threshold_monitor_hidden = ET.SubElement(config, "threshold-monitor-hidden", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
        threshold_monitor = ET.SubElement(threshold_monitor_hidden, "threshold-monitor")
        interface = ET.SubElement(threshold_monitor, "interface")
        policy = ET.SubElement(interface, "policy")
        policy_name_key = ET.SubElement(policy, "policy_name")
        policy_name_key.text = kwargs.pop('policy_name')
        area = ET.SubElement(policy, "area")
        type_key = ET.SubElement(area, "type")
        type_key.text = kwargs.pop('type')
        area_value_key = ET.SubElement(area, "area_value")
        area_value_key.text = kwargs.pop('area_value')
        alert = ET.SubElement(area, "alert")
        below = ET.SubElement(alert, "below")
        below_lowthresh_action = ET.SubElement(below, "below-lowthresh-action")
        below_lowthresh_action.text = kwargs.pop('below_lowthresh_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        