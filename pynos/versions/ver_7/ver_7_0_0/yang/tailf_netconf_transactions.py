#!/usr/bin/env python
import xml.etree.ElementTree as ET


class tailf_netconf_transactions(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def start_transaction_input_target_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        target = ET.SubElement(input, "target")
        target = ET.SubElement(target, "target")
        startup = ET.SubElement(target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_target_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        target = ET.SubElement(input, "target")
        target = ET.SubElement(target, "target")
        running = ET.SubElement(target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_target_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        target = ET.SubElement(input, "target")
        target = ET.SubElement(target, "target")
        candidate = ET.SubElement(target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_with_inactive(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        with_inactive = ET.SubElement(input, "with-inactive", xmlns="http://tail-f.com/ns/netconf/inactive/1.0")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_target_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        target = ET.SubElement(input, "target")
        target = ET.SubElement(target, "target")
        startup = ET.SubElement(target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_target_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        target = ET.SubElement(input, "target")
        target = ET.SubElement(target, "target")
        running = ET.SubElement(target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_target_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        target = ET.SubElement(input, "target")
        target = ET.SubElement(target, "target")
        candidate = ET.SubElement(target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def start_transaction_input_with_inactive(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        start_transaction = ET.Element("start_transaction")
        config = start_transaction
        input = ET.SubElement(start_transaction, "input")
        with_inactive = ET.SubElement(input, "with-inactive", xmlns="http://tail-f.com/ns/netconf/inactive/1.0")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        