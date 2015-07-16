#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_firmware(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def firmware_autoupgrade_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade = ET.SubElement(firmware, "autoupgrade")
        enable = ET.SubElement(autoupgrade, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        path = ET.SubElement(autoupgrade_params, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        protocol = ET.SubElement(autoupgrade_params, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_ipaddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        ipaddress = ET.SubElement(autoupgrade_params, "ipaddress")
        ipaddress.text = kwargs.pop('ipaddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        username = ET.SubElement(autoupgrade_params, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_pss(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        pss = ET.SubElement(autoupgrade_params, "pass")
        pss.text = kwargs.pop('pss')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_input_fwdl_tid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        input = ET.SubElement(fwdl_status, "input")
        fwdl_tid = ET.SubElement(input, "fwdl-tid")
        fwdl_tid.text = kwargs.pop('fwdl_tid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_number_of_entries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        number_of_entries = ET.SubElement(output, "number-of-entries")
        number_of_entries.text = kwargs.pop('number_of_entries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_state = ET.SubElement(output, "fwdl-state")
        fwdl_state.text = kwargs.pop('fwdl_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        index = ET.SubElement(fwdl_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        message_id = ET.SubElement(fwdl_entries, "message-id")
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        date_and_time_info = ET.SubElement(fwdl_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        message = ET.SubElement(fwdl_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_slot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_slot = ET.SubElement(fwdl_entries, "blade-slot")
        blade_slot.text = kwargs.pop('blade_slot')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_swbd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_swbd = ET.SubElement(fwdl_entries, "blade-swbd")
        blade_swbd.text = kwargs.pop('blade_swbd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_name = ET.SubElement(fwdl_entries, "blade-name")
        blade_name.text = kwargs.pop('blade_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_state = ET.SubElement(fwdl_entries, "blade-state")
        blade_state.text = kwargs.pop('blade_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_app(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_app = ET.SubElement(fwdl_entries, "blade-app")
        blade_app.text = kwargs.pop('blade_app')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        input = ET.SubElement(activate_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_overall_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        overall_status = ET.SubElement(output, "overall-status")
        overall_status.text = kwargs.pop('overall_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_overall_error_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        overall_error_msg = ET.SubElement(output, "overall-error-msg")
        overall_error_msg.text = kwargs.pop('overall_error_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_activate_entries_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        activate_entries = ET.SubElement(output, "activate-entries")
        rbridge_id = ET.SubElement(activate_entries, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_activate_entries_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        activate_entries = ET.SubElement(output, "activate-entries")
        status = ET.SubElement(activate_entries, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_user(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        user = ET.SubElement(input, "user")
        user.text = kwargs.pop('user')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        password = ET.SubElement(input, "password")
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        host = ET.SubElement(input, "host")
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        directory = ET.SubElement(input, "directory")
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        file = ET.SubElement(input, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_cluster_options_auto_activate_auto_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        cluster_options = ET.SubElement(input, "cluster-options")
        auto_activate = ET.SubElement(cluster_options, "auto-activate")
        auto_activate = ET.SubElement(auto_activate, "auto-activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_cluster_options_coldboot_coldboot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        cluster_options = ET.SubElement(input, "cluster-options")
        coldboot = ET.SubElement(cluster_options, "coldboot")
        coldboot = ET.SubElement(coldboot, "coldboot")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        protocol = ET.SubElement(input, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_fwdl_cmd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        fwdl_cmd_status = ET.SubElement(output, "fwdl-cmd-status")
        fwdl_cmd_status.text = kwargs.pop('fwdl_cmd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_fwdl_cmd_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        fwdl_cmd_msg = ET.SubElement(output, "fwdl-cmd-msg")
        fwdl_cmd_msg.text = kwargs.pop('fwdl_cmd_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        cluster_output = ET.SubElement(output, "cluster-output")
        rbridge_id = ET.SubElement(cluster_output, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_fwdl_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        cluster_output = ET.SubElement(output, "cluster-output")
        fwdl_status = ET.SubElement(cluster_output, "fwdl-status")
        fwdl_status.text = kwargs.pop('fwdl_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_fwdl_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        cluster_output = ET.SubElement(output, "cluster-output")
        fwdl_msg = ET.SubElement(cluster_output, "fwdl-msg")
        fwdl_msg.text = kwargs.pop('fwdl_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        input = ET.SubElement(logical_chassis_fwdl_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_overall_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        overall_status = ET.SubElement(output, "overall-status")
        overall_status.text = kwargs.pop('overall_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        rbridge_id = ET.SubElement(cluster_fwdl_entries, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_state = ET.SubElement(cluster_fwdl_entries, "fwdl-state")
        fwdl_state.text = kwargs.pop('fwdl_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        index = ET.SubElement(fwdl_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        message_id = ET.SubElement(fwdl_entries, "message-id")
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        date_and_time_info = ET.SubElement(fwdl_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        message = ET.SubElement(fwdl_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_slot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_slot = ET.SubElement(fwdl_entries, "blade-slot")
        blade_slot.text = kwargs.pop('blade_slot')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_swbd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_swbd = ET.SubElement(fwdl_entries, "blade-swbd")
        blade_swbd.text = kwargs.pop('blade_swbd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_name = ET.SubElement(fwdl_entries, "blade-name")
        blade_name.text = kwargs.pop('blade_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_state = ET.SubElement(fwdl_entries, "blade-state")
        blade_state.text = kwargs.pop('blade_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_app(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_app = ET.SubElement(fwdl_entries, "blade-app")
        blade_app.text = kwargs.pop('blade_app')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_last_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_last_state = ET.SubElement(output, "dad-last-state")
        dad_last_state.text = kwargs.pop('dad_last_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        index = ET.SubElement(dad_status_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        date_and_time_info = ET.SubElement(dad_status_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        message = ET.SubElement(dad_status_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade = ET.SubElement(firmware, "autoupgrade")
        enable = ET.SubElement(autoupgrade, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        path = ET.SubElement(autoupgrade_params, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        protocol = ET.SubElement(autoupgrade_params, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_ipaddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        ipaddress = ET.SubElement(autoupgrade_params, "ipaddress")
        ipaddress.text = kwargs.pop('ipaddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        username = ET.SubElement(autoupgrade_params, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def firmware_autoupgrade_params_pss(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        firmware = ET.SubElement(config, "firmware", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        autoupgrade_params = ET.SubElement(firmware, "autoupgrade-params")
        pss = ET.SubElement(autoupgrade_params, "pass")
        pss.text = kwargs.pop('pss')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_input_fwdl_tid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        input = ET.SubElement(fwdl_status, "input")
        fwdl_tid = ET.SubElement(input, "fwdl-tid")
        fwdl_tid.text = kwargs.pop('fwdl_tid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_number_of_entries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        number_of_entries = ET.SubElement(output, "number-of-entries")
        number_of_entries.text = kwargs.pop('number_of_entries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_state = ET.SubElement(output, "fwdl-state")
        fwdl_state.text = kwargs.pop('fwdl_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        index = ET.SubElement(fwdl_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        message_id = ET.SubElement(fwdl_entries, "message-id")
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        date_and_time_info = ET.SubElement(fwdl_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        message = ET.SubElement(fwdl_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_slot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_slot = ET.SubElement(fwdl_entries, "blade-slot")
        blade_slot.text = kwargs.pop('blade_slot')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_swbd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_swbd = ET.SubElement(fwdl_entries, "blade-swbd")
        blade_swbd.text = kwargs.pop('blade_swbd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_name = ET.SubElement(fwdl_entries, "blade-name")
        blade_name.text = kwargs.pop('blade_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_state = ET.SubElement(fwdl_entries, "blade-state")
        blade_state.text = kwargs.pop('blade_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fwdl_status_output_fwdl_entries_blade_app(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fwdl_status = ET.Element("fwdl_status")
        config = fwdl_status
        output = ET.SubElement(fwdl_status, "output")
        fwdl_entries = ET.SubElement(output, "fwdl-entries")
        blade_app = ET.SubElement(fwdl_entries, "blade-app")
        blade_app.text = kwargs.pop('blade_app')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        input = ET.SubElement(activate_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_overall_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        overall_status = ET.SubElement(output, "overall-status")
        overall_status.text = kwargs.pop('overall_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_overall_error_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        overall_error_msg = ET.SubElement(output, "overall-error-msg")
        overall_error_msg.text = kwargs.pop('overall_error_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_activate_entries_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        activate_entries = ET.SubElement(output, "activate-entries")
        rbridge_id = ET.SubElement(activate_entries, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def activate_status_output_activate_entries_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        activate_status = ET.Element("activate_status")
        config = activate_status
        output = ET.SubElement(activate_status, "output")
        activate_entries = ET.SubElement(output, "activate-entries")
        status = ET.SubElement(activate_entries, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_user(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        user = ET.SubElement(input, "user")
        user.text = kwargs.pop('user')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        password = ET.SubElement(input, "password")
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        host = ET.SubElement(input, "host")
        host.text = kwargs.pop('host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        directory = ET.SubElement(input, "directory")
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        file = ET.SubElement(input, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_cluster_options_auto_activate_auto_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        cluster_options = ET.SubElement(input, "cluster-options")
        auto_activate = ET.SubElement(cluster_options, "auto-activate")
        auto_activate = ET.SubElement(auto_activate, "auto-activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_cluster_options_coldboot_coldboot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        cluster_options = ET.SubElement(input, "cluster-options")
        coldboot = ET.SubElement(cluster_options, "coldboot")
        coldboot = ET.SubElement(coldboot, "coldboot")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_input_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        input = ET.SubElement(logical_chassis_fwdl_sanity, "input")
        protocol = ET.SubElement(input, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_fwdl_cmd_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        fwdl_cmd_status = ET.SubElement(output, "fwdl-cmd-status")
        fwdl_cmd_status.text = kwargs.pop('fwdl_cmd_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_fwdl_cmd_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        fwdl_cmd_msg = ET.SubElement(output, "fwdl-cmd-msg")
        fwdl_cmd_msg.text = kwargs.pop('fwdl_cmd_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        cluster_output = ET.SubElement(output, "cluster-output")
        rbridge_id = ET.SubElement(cluster_output, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_fwdl_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        cluster_output = ET.SubElement(output, "cluster-output")
        fwdl_status = ET.SubElement(cluster_output, "fwdl-status")
        fwdl_status.text = kwargs.pop('fwdl_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_sanity_output_cluster_output_fwdl_msg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_sanity = ET.Element("logical_chassis_fwdl_sanity")
        config = logical_chassis_fwdl_sanity
        output = ET.SubElement(logical_chassis_fwdl_sanity, "output")
        cluster_output = ET.SubElement(output, "cluster-output")
        fwdl_msg = ET.SubElement(cluster_output, "fwdl-msg")
        fwdl_msg.text = kwargs.pop('fwdl_msg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        input = ET.SubElement(logical_chassis_fwdl_status, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_overall_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        overall_status = ET.SubElement(output, "overall-status")
        overall_status.text = kwargs.pop('overall_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        rbridge_id = ET.SubElement(cluster_fwdl_entries, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_state = ET.SubElement(cluster_fwdl_entries, "fwdl-state")
        fwdl_state.text = kwargs.pop('fwdl_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        index = ET.SubElement(fwdl_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_message_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        message_id = ET.SubElement(fwdl_entries, "message-id")
        message_id.text = kwargs.pop('message_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        date_and_time_info = ET.SubElement(fwdl_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        message = ET.SubElement(fwdl_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_slot(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_slot = ET.SubElement(fwdl_entries, "blade-slot")
        blade_slot.text = kwargs.pop('blade_slot')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_swbd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_swbd = ET.SubElement(fwdl_entries, "blade-swbd")
        blade_swbd.text = kwargs.pop('blade_swbd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_name = ET.SubElement(fwdl_entries, "blade-name")
        blade_name.text = kwargs.pop('blade_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_state = ET.SubElement(fwdl_entries, "blade-state")
        blade_state.text = kwargs.pop('blade_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logical_chassis_fwdl_status_output_cluster_fwdl_entries_fwdl_entries_blade_app(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logical_chassis_fwdl_status = ET.Element("logical_chassis_fwdl_status")
        config = logical_chassis_fwdl_status
        output = ET.SubElement(logical_chassis_fwdl_status, "output")
        cluster_fwdl_entries = ET.SubElement(output, "cluster-fwdl-entries")
        fwdl_entries = ET.SubElement(cluster_fwdl_entries, "fwdl-entries")
        blade_app = ET.SubElement(fwdl_entries, "blade-app")
        blade_app.text = kwargs.pop('blade_app')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_last_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_last_state = ET.SubElement(output, "dad-last-state")
        dad_last_state.text = kwargs.pop('dad_last_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        index = ET.SubElement(dad_status_entries, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_date_and_time_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        date_and_time_info = ET.SubElement(dad_status_entries, "date-and-time-info")
        date_and_time_info.text = kwargs.pop('date_and_time_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def dad_status_output_dad_status_entries_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        dad_status = ET.Element("dad_status")
        config = dad_status
        output = ET.SubElement(dad_status, "output")
        dad_status_entries = ET.SubElement(output, "dad-status-entries")
        message = ET.SubElement(dad_status_entries, "message")
        message.text = kwargs.pop('message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        