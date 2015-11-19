#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ras_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_raslog_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        input = ET.SubElement(show_raslog, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_input_number_of_latest_events(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        input = ET.SubElement(show_raslog, "input")
        number_of_latest_events = ET.SubElement(input, "number-of-latest-events")
        number_of_latest_events.text = kwargs.pop('number_of_latest_events')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        rbridge_id = ET.SubElement(show_all_raslog, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_number_of_entries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        number_of_entries = ET.SubElement(show_all_raslog, "number-of-entries")
        number_of_entries.text = kwargs.pop('number_of_entries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        index = ET.SubElement(raslog_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        message_id = ET.SubElement(raslog_entries, "message-id")
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        date_and_time_info = ET.SubElement(raslog_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_severity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        severity = ET.SubElement(raslog_entries, "severity")
        severity.text = kwargs.pop('severity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_repeat_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        repeat_count = ET.SubElement(raslog_entries, "repeat-count")
        repeat_count.text = kwargs.pop('repeat_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        message = ET.SubElement(raslog_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message_flag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        message_flag = ET.SubElement(raslog_entries, "message-flag")
        message_flag.text = kwargs.pop('message_flag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_log_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        log_type = ET.SubElement(raslog_entries, "log-type")
        log_type.text = kwargs.pop('log_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_switch_or_chassis_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        switch_or_chassis_name = ET.SubElement(raslog_entries, "switch-or-chassis-name")
        switch_or_chassis_name.text = kwargs.pop('switch_or_chassis_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_cmd_status_error_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        cmd_status_error_msg = ET.SubElement(output, "cmd-status-error-msg")
        cmd_status_error_msg.text = kwargs.pop('cmd_status_error_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        input = ET.SubElement(show_support_save_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        rbridge_id = ET.SubElement(show_support_save_status, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        status = ET.SubElement(show_support_save_status, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        message = ET.SubElement(show_support_save_status, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_percentage_of_completion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        percentage_of_completion = ET.SubElement(show_support_save_status, "percentage-of-completion")
        percentage_of_completion.text = kwargs.pop('percentage_of_completion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        input = ET.SubElement(show_system_info, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_output_show_system_info_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        output = ET.SubElement(show_system_info, "output")
        show_system_info = ET.SubElement(output, "show-system-info")
        rbridge_id = ET.SubElement(show_system_info, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_output_show_system_info_stack_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        output = ET.SubElement(show_system_info, "output")
        show_system_info = ET.SubElement(output, "show-system-info")
        stack_mac = ET.SubElement(show_system_info, "stack-mac")
        stack_mac.text = kwargs.pop('stack_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        input = ET.SubElement(show_raslog, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_input_number_of_latest_events(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        input = ET.SubElement(show_raslog, "input")
        number_of_latest_events = ET.SubElement(input, "number-of-latest-events")
        number_of_latest_events.text = kwargs.pop('number_of_latest_events')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        rbridge_id = ET.SubElement(show_all_raslog, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_number_of_entries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        number_of_entries = ET.SubElement(show_all_raslog, "number-of-entries")
        number_of_entries.text = kwargs.pop('number_of_entries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        index = ET.SubElement(raslog_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        message_id = ET.SubElement(raslog_entries, "message-id")
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        date_and_time_info = ET.SubElement(raslog_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_severity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        severity = ET.SubElement(raslog_entries, "severity")
        severity.text = kwargs.pop('severity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_repeat_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        repeat_count = ET.SubElement(raslog_entries, "repeat-count")
        repeat_count.text = kwargs.pop('repeat_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        message = ET.SubElement(raslog_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_message_flag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        message_flag = ET.SubElement(raslog_entries, "message-flag")
        message_flag.text = kwargs.pop('message_flag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_log_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        log_type = ET.SubElement(raslog_entries, "log-type")
        log_type.text = kwargs.pop('log_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_show_all_raslog_raslog_entries_switch_or_chassis_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        show_all_raslog = ET.SubElement(output, "show-all-raslog")
        raslog_entries = ET.SubElement(show_all_raslog, "raslog-entries")
        switch_or_chassis_name = ET.SubElement(raslog_entries, "switch-or-chassis-name")
        switch_or_chassis_name.text = kwargs.pop('switch_or_chassis_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_raslog_output_cmd_status_error_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_raslog = ET.Element("show_raslog")
        config = show_raslog
        output = ET.SubElement(show_raslog, "output")
        cmd_status_error_msg = ET.SubElement(output, "cmd-status-error-msg")
        cmd_status_error_msg.text = kwargs.pop('cmd_status_error_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        input = ET.SubElement(show_support_save_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        rbridge_id = ET.SubElement(show_support_save_status, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        status = ET.SubElement(show_support_save_status, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        message = ET.SubElement(show_support_save_status, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_support_save_status_output_show_support_save_status_percentage_of_completion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_support_save_status = ET.Element("show_support_save_status")
        config = show_support_save_status
        output = ET.SubElement(show_support_save_status, "output")
        show_support_save_status = ET.SubElement(output, "show-support-save-status")
        percentage_of_completion = ET.SubElement(show_support_save_status, "percentage-of-completion")
        percentage_of_completion.text = kwargs.pop('percentage_of_completion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        input = ET.SubElement(show_system_info, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_output_show_system_info_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        output = ET.SubElement(show_system_info, "output")
        show_system_info = ET.SubElement(output, "show-system-info")
        rbridge_id = ET.SubElement(show_system_info, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_system_info_output_show_system_info_stack_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_system_info = ET.Element("show_system_info")
        config = show_system_info
        output = ET.SubElement(show_system_info, "output")
        show_system_info = ET.SubElement(output, "show-system-info")
        stack_mac = ET.SubElement(show_system_info, "stack-mac")
        stack_mac.text = kwargs.pop('stack_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        