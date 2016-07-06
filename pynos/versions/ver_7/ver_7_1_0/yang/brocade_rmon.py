#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_rmon(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def rmon_event_entry_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index = ET.SubElement(event_entry, "event-index")
        event_index.text = kwargs.pop('event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        event_description = ET.SubElement(event_entry, "event-description")
        event_description.text = kwargs.pop('event_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        log = ET.SubElement(event_entry, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        event_community = ET.SubElement(event_entry, "event-community")
        event_community.text = kwargs.pop('event_community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_owner(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        event_owner = ET.SubElement(event_entry, "event-owner")
        event_owner.text = kwargs.pop('event_owner')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index.text = kwargs.pop('alarm_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_snmp_oid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        snmp_oid = ET.SubElement(alarm_entry, "snmp-oid")
        snmp_oid.text = kwargs.pop('snmp_oid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_interval = ET.SubElement(alarm_entry, "alarm-interval")
        alarm_interval.text = kwargs.pop('alarm_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_sample(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_sample = ET.SubElement(alarm_entry, "alarm-sample")
        alarm_sample.text = kwargs.pop('alarm_sample')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_rising_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_rising_threshold = ET.SubElement(alarm_entry, "alarm-rising-threshold")
        alarm_rising_threshold.text = kwargs.pop('alarm_rising_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_rising_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_rising_event_index = ET.SubElement(alarm_entry, "alarm-rising-event-index")
        alarm_rising_event_index.text = kwargs.pop('alarm_rising_event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_falling_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_falling_threshold = ET.SubElement(alarm_entry, "alarm-falling-threshold")
        alarm_falling_threshold.text = kwargs.pop('alarm_falling_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_falling_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_falling_event_index = ET.SubElement(alarm_entry, "alarm-falling-event-index")
        alarm_falling_event_index.text = kwargs.pop('alarm_falling_event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_owner(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_owner = ET.SubElement(alarm_entry, "alarm-owner")
        alarm_owner.text = kwargs.pop('alarm_owner')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index = ET.SubElement(event_entry, "event-index")
        event_index.text = kwargs.pop('event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        event_description = ET.SubElement(event_entry, "event-description")
        event_description.text = kwargs.pop('event_description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_log(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        log = ET.SubElement(event_entry, "log")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        event_community = ET.SubElement(event_entry, "event-community")
        event_community.text = kwargs.pop('event_community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_event_entry_event_owner(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        event_entry = ET.SubElement(rmon, "event-entry")
        event_index_key = ET.SubElement(event_entry, "event-index")
        event_index_key.text = kwargs.pop('event_index')
        event_owner = ET.SubElement(event_entry, "event-owner")
        event_owner.text = kwargs.pop('event_owner')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index.text = kwargs.pop('alarm_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_snmp_oid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        snmp_oid = ET.SubElement(alarm_entry, "snmp-oid")
        snmp_oid.text = kwargs.pop('snmp_oid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_interval = ET.SubElement(alarm_entry, "alarm-interval")
        alarm_interval.text = kwargs.pop('alarm_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_sample(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_sample = ET.SubElement(alarm_entry, "alarm-sample")
        alarm_sample.text = kwargs.pop('alarm_sample')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_rising_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_rising_threshold = ET.SubElement(alarm_entry, "alarm-rising-threshold")
        alarm_rising_threshold.text = kwargs.pop('alarm_rising_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_rising_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_rising_event_index = ET.SubElement(alarm_entry, "alarm-rising-event-index")
        alarm_rising_event_index.text = kwargs.pop('alarm_rising_event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_falling_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_falling_threshold = ET.SubElement(alarm_entry, "alarm-falling-threshold")
        alarm_falling_threshold.text = kwargs.pop('alarm_falling_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_falling_event_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_falling_event_index = ET.SubElement(alarm_entry, "alarm-falling-event-index")
        alarm_falling_event_index.text = kwargs.pop('alarm_falling_event_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rmon_alarm_entry_alarm_owner(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rmon = ET.SubElement(config, "rmon", xmlns="urn:brocade.com:mgmt:brocade-rmon")
        alarm_entry = ET.SubElement(rmon, "alarm-entry")
        alarm_index_key = ET.SubElement(alarm_entry, "alarm-index")
        alarm_index_key.text = kwargs.pop('alarm_index')
        alarm_owner = ET.SubElement(alarm_entry, "alarm-owner")
        alarm_owner.text = kwargs.pop('alarm_owner')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        