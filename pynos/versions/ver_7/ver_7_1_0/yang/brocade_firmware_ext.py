#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_firmware_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_firmware_version_input_switchid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        input = ET.SubElement(show_firmware_version, "input")
        switchid = ET.SubElement(input, "switchid")
        switchid.text = kwargs.pop('switchid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_switchid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        switchid = ET.SubElement(show_firmware_version, "switchid")
        switchid.text = kwargs.pop('switchid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_os_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        os_name = ET.SubElement(show_firmware_version, "os-name")
        os_name.text = kwargs.pop('os_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_os_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        os_version = ET.SubElement(show_firmware_version, "os-version")
        os_version.text = kwargs.pop('os_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_copy_right_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        copy_right_info = ET.SubElement(show_firmware_version, "copy-right-info")
        copy_right_info.text = kwargs.pop('copy_right_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_build_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        build_time = ET.SubElement(show_firmware_version, "build-time")
        build_time.text = kwargs.pop('build_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_firmware_full_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        firmware_full_version = ET.SubElement(show_firmware_version, "firmware-full-version")
        firmware_full_version.text = kwargs.pop('firmware_full_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_vendor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        control_processor_vendor = ET.SubElement(show_firmware_version, "control-processor-vendor")
        control_processor_vendor.text = kwargs.pop('control_processor_vendor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_chipset(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        control_processor_chipset = ET.SubElement(show_firmware_version, "control-processor-chipset")
        control_processor_chipset.text = kwargs.pop('control_processor_chipset')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_memory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        control_processor_memory = ET.SubElement(show_firmware_version, "control-processor-memory")
        control_processor_memory.text = kwargs.pop('control_processor_memory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_slot_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        slot_no = ET.SubElement(node_info, "slot-no")
        slot_no.text = kwargs.pop('slot_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_node_instance_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        node_instance_no = ET.SubElement(node_info, "node-instance-no")
        node_instance_no.text = kwargs.pop('node_instance_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_node_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        node_type = ET.SubElement(node_info, "node-type")
        node_type.text = kwargs.pop('node_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_is_active_cp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        is_active_cp = ET.SubElement(node_info, "is-active-cp")
        is_active_cp.text = kwargs.pop('is_active_cp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_application_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        application_name = ET.SubElement(firmware_version_info, "application-name")
        application_name.text = kwargs.pop('application_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_primary_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        primary_version = ET.SubElement(firmware_version_info, "primary-version")
        primary_version.text = kwargs.pop('primary_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_secondary_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        secondary_version = ET.SubElement(firmware_version_info, "secondary-version")
        secondary_version.text = kwargs.pop('secondary_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_input_switchid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        input = ET.SubElement(show_firmware_version, "input")
        switchid = ET.SubElement(input, "switchid")
        switchid.text = kwargs.pop('switchid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_switchid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        switchid = ET.SubElement(show_firmware_version, "switchid")
        switchid.text = kwargs.pop('switchid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_os_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        os_name = ET.SubElement(show_firmware_version, "os-name")
        os_name.text = kwargs.pop('os_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_os_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        os_version = ET.SubElement(show_firmware_version, "os-version")
        os_version.text = kwargs.pop('os_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_copy_right_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        copy_right_info = ET.SubElement(show_firmware_version, "copy-right-info")
        copy_right_info.text = kwargs.pop('copy_right_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_build_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        build_time = ET.SubElement(show_firmware_version, "build-time")
        build_time.text = kwargs.pop('build_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_firmware_full_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        firmware_full_version = ET.SubElement(show_firmware_version, "firmware-full-version")
        firmware_full_version.text = kwargs.pop('firmware_full_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_vendor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        control_processor_vendor = ET.SubElement(show_firmware_version, "control-processor-vendor")
        control_processor_vendor.text = kwargs.pop('control_processor_vendor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_chipset(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        control_processor_chipset = ET.SubElement(show_firmware_version, "control-processor-chipset")
        control_processor_chipset.text = kwargs.pop('control_processor_chipset')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_control_processor_memory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        control_processor_memory = ET.SubElement(show_firmware_version, "control-processor-memory")
        control_processor_memory.text = kwargs.pop('control_processor_memory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_slot_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        slot_no = ET.SubElement(node_info, "slot-no")
        slot_no.text = kwargs.pop('slot_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_node_instance_no(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        node_instance_no = ET.SubElement(node_info, "node-instance-no")
        node_instance_no.text = kwargs.pop('node_instance_no')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_node_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        node_type = ET.SubElement(node_info, "node-type")
        node_type.text = kwargs.pop('node_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_is_active_cp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        is_active_cp = ET.SubElement(node_info, "is-active-cp")
        is_active_cp.text = kwargs.pop('is_active_cp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_application_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        application_name = ET.SubElement(firmware_version_info, "application-name")
        application_name.text = kwargs.pop('application_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_primary_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        primary_version = ET.SubElement(firmware_version_info, "primary-version")
        primary_version.text = kwargs.pop('primary_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_firmware_version_output_show_firmware_version_node_info_firmware_version_info_secondary_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_firmware_version = ET.Element("show_firmware_version")
        config = show_firmware_version
        output = ET.SubElement(show_firmware_version, "output")
        show_firmware_version = ET.SubElement(output, "show-firmware-version")
        node_info = ET.SubElement(show_firmware_version, "node-info")
        firmware_version_info = ET.SubElement(node_info, "firmware-version-info")
        secondary_version = ET.SubElement(firmware_version_info, "secondary-version")
        secondary_version.text = kwargs.pop('secondary_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        