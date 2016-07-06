#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_event_handler(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def event_handler_event_handler_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name = ET.SubElement(event_handler_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        description = ET.SubElement(event_handler_list, "description")
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        trigger = ET.SubElement(event_handler_list, "trigger")
        trigger_id = ET.SubElement(trigger, "trigger-id")
        trigger_id.text = kwargs.pop('trigger_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_choice_vcs_vcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        trigger = ET.SubElement(event_handler_list, "trigger")
        trigger_id_key = ET.SubElement(trigger, "trigger-id")
        trigger_id_key.text = kwargs.pop('trigger_id')
        trigger_choice = ET.SubElement(trigger, "trigger-choice")
        vcs = ET.SubElement(trigger_choice, "vcs")
        vcs = ET.SubElement(vcs, "vcs")
        vcs.text = kwargs.pop('vcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_choice_raslog_raslog(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        trigger = ET.SubElement(event_handler_list, "trigger")
        trigger_id_key = ET.SubElement(trigger, "trigger-id")
        trigger_id_key.text = kwargs.pop('trigger_id')
        trigger_choice = ET.SubElement(trigger, "trigger-choice")
        raslog = ET.SubElement(trigger_choice, "raslog")
        raslog = ET.SubElement(raslog, "raslog")
        raslog.text = kwargs.pop('raslog')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_action_action_choice_python_script_python_script(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        action = ET.SubElement(event_handler_list, "action")
        action_choice = ET.SubElement(action, "action-choice")
        python_script = ET.SubElement(action_choice, "python-script")
        python_script = ET.SubElement(python_script, "python-script")
        python_script.text = kwargs.pop('python_script')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name = ET.SubElement(event_handler_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        description = ET.SubElement(event_handler_list, "description")
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        trigger = ET.SubElement(event_handler_list, "trigger")
        trigger_id = ET.SubElement(trigger, "trigger-id")
        trigger_id.text = kwargs.pop('trigger_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_choice_vcs_vcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        trigger = ET.SubElement(event_handler_list, "trigger")
        trigger_id_key = ET.SubElement(trigger, "trigger-id")
        trigger_id_key.text = kwargs.pop('trigger_id')
        trigger_choice = ET.SubElement(trigger, "trigger-choice")
        vcs = ET.SubElement(trigger_choice, "vcs")
        vcs = ET.SubElement(vcs, "vcs")
        vcs.text = kwargs.pop('vcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_trigger_trigger_choice_raslog_raslog(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        trigger = ET.SubElement(event_handler_list, "trigger")
        trigger_id_key = ET.SubElement(trigger, "trigger-id")
        trigger_id_key.text = kwargs.pop('trigger_id')
        trigger_choice = ET.SubElement(trigger, "trigger-choice")
        raslog = ET.SubElement(trigger_choice, "raslog")
        raslog = ET.SubElement(raslog, "raslog")
        raslog.text = kwargs.pop('raslog')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def event_handler_event_handler_list_action_action_choice_python_script_python_script(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        event_handler = ET.SubElement(config, "event-handler", xmlns="urn:brocade.com:mgmt:brocade-event-handler")
        event_handler_list = ET.SubElement(event_handler, "event-handler-list")
        name_key = ET.SubElement(event_handler_list, "name")
        name_key.text = kwargs.pop('name')
        action = ET.SubElement(event_handler_list, "action")
        action_choice = ET.SubElement(action, "action-choice")
        python_script = ET.SubElement(action_choice, "python-script")
        python_script = ET.SubElement(python_script, "python-script")
        python_script.text = kwargs.pop('python_script')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        