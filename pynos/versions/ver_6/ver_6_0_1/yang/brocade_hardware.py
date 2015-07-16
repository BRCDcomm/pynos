#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_hardware(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hardware_connector_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name = ET.SubElement(connector, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_sfp_breakout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name_key = ET.SubElement(connector, "name")
        name_key.text = kwargs.pop('name')
        sfp = ET.SubElement(connector, "sfp")
        breakout = ET.SubElement(sfp, "breakout")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name = ET.SubElement(port_group, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_performance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        mode = ET.SubElement(port_group, "mode")
        performance = ET.SubElement(mode, "performance")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id = ET.SubElement(connector_group, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id_key = ET.SubElement(connector_group, "id")
        id_key.text = kwargs.pop('id')
        speed = ET.SubElement(connector_group, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id = ET.SubElement(flexport, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        type = ET.SubElement(flexport_type, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        instance = ET.SubElement(flexport_type, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_skip_deconfig(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        skip_deconfig = ET.SubElement(flexport_type, "skip_deconfig")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name = ET.SubElement(kap_custom_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_lacp_lacp_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        lacp = ET.SubElement(kap_custom_profile, "lacp")
        lacp_hello_interval = ET.SubElement(lacp, "lacp_hello_interval")
        lacp_hello_interval.text = kwargs.pop('lacp_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_lacp_lacp_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        lacp = ET.SubElement(kap_custom_profile, "lacp")
        lacp_num_entry = ET.SubElement(lacp, "lacp_num_entry")
        lacp_num_entry.text = kwargs.pop('lacp_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_xstp_xstp_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        xstp = ET.SubElement(kap_custom_profile, "xstp")
        xstp_hello_interval = ET.SubElement(xstp, "xstp_hello_interval")
        xstp_hello_interval.text = kwargs.pop('xstp_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_xstp_xstp_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        xstp = ET.SubElement(kap_custom_profile, "xstp")
        xstp_num_entry = ET.SubElement(xstp, "xstp_num_entry")
        xstp_num_entry.text = kwargs.pop('xstp_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_rpvst_rpvst_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        rpvst = ET.SubElement(kap_custom_profile, "rpvst")
        rpvst_hello_interval = ET.SubElement(rpvst, "rpvst_hello_interval")
        rpvst_hello_interval.text = kwargs.pop('rpvst_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_rpvst_rpvst_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        rpvst = ET.SubElement(kap_custom_profile, "rpvst")
        rpvst_num_entry = ET.SubElement(rpvst, "rpvst_num_entry")
        rpvst_num_entry.text = kwargs.pop('rpvst_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_udld_udld_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        udld = ET.SubElement(kap_custom_profile, "udld")
        udld_hello_interval = ET.SubElement(udld, "udld_hello_interval")
        udld_hello_interval.text = kwargs.pop('udld_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_udld_udld_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        udld = ET.SubElement(kap_custom_profile, "udld")
        udld_num_entry = ET.SubElement(udld, "udld_num_entry")
        udld_num_entry.text = kwargs.pop('udld_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_vxlan_bfd_vxlan_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_vxlan = ET.SubElement(kap_custom_profile, "bfd-vxlan")
        bfd_vxlan_hello_interval = ET.SubElement(bfd_vxlan, "bfd_vxlan_hello_interval")
        bfd_vxlan_hello_interval.text = kwargs.pop('bfd_vxlan_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_vxlan_bfd_vxlan_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_vxlan = ET.SubElement(kap_custom_profile, "bfd-vxlan")
        bfd_vxlan_num_entry = ET.SubElement(bfd_vxlan, "bfd_vxlan_num_entry")
        bfd_vxlan_num_entry.text = kwargs.pop('bfd_vxlan_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_l3_bfd_l3_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_l3 = ET.SubElement(kap_custom_profile, "bfd-l3")
        bfd_l3_hello_interval = ET.SubElement(bfd_l3, "bfd_l3_hello_interval")
        bfd_l3_hello_interval.text = kwargs.pop('bfd_l3_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_l3_bfd_l3_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_l3 = ET.SubElement(kap_custom_profile, "bfd-l3")
        bfd_l3_num_entry = ET.SubElement(bfd_l3, "bfd_l3_num_entry")
        bfd_l3_num_entry.text = kwargs.pop('bfd_l3_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_fcoe_fcoe_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        fcoe = ET.SubElement(kap_custom_profile, "fcoe")
        fcoe_hello_interval = ET.SubElement(fcoe, "fcoe_hello_interval")
        fcoe_hello_interval.text = kwargs.pop('fcoe_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_fcoe_fcoe_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        fcoe = ET.SubElement(kap_custom_profile, "fcoe")
        fcoe_num_entry = ET.SubElement(fcoe, "fcoe_num_entry")
        fcoe_num_entry.text = kwargs.pop('fcoe_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_flexports_output_flexport_list_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_flexports = ET.Element("get_flexports")
        config = get_flexports
        output = ET.SubElement(get_flexports, "output")
        flexport_list = ET.SubElement(output, "flexport-list")
        port_id = ET.SubElement(flexport_list, "port-id")
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name = ET.SubElement(connector, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_sfp_breakout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector = ET.SubElement(hardware, "connector")
        name_key = ET.SubElement(connector, "name")
        name_key.text = kwargs.pop('name')
        sfp = ET.SubElement(connector, "sfp")
        breakout = ET.SubElement(sfp, "breakout")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name = ET.SubElement(port_group, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_port_group_mode_performance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        port_group = ET.SubElement(hardware, "port-group")
        name_key = ET.SubElement(port_group, "name")
        name_key.text = kwargs.pop('name')
        mode = ET.SubElement(port_group, "mode")
        performance = ET.SubElement(mode, "performance")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id = ET.SubElement(connector_group, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_connector_group_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        connector_group = ET.SubElement(hardware, "connector-group")
        id_key = ET.SubElement(connector_group, "id")
        id_key.text = kwargs.pop('id')
        speed = ET.SubElement(connector_group, "speed")
        speed.text = kwargs.pop('speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id = ET.SubElement(flexport, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        type = ET.SubElement(flexport_type, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        instance = ET.SubElement(flexport_type, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_flexport_flexport_type_skip_deconfig(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        flexport = ET.SubElement(hardware, "flexport")
        id_key = ET.SubElement(flexport, "id")
        id_key.text = kwargs.pop('id')
        flexport_type = ET.SubElement(flexport, "flexport_type")
        skip_deconfig = ET.SubElement(flexport_type, "skip_deconfig")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name = ET.SubElement(kap_custom_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_lacp_lacp_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        lacp = ET.SubElement(kap_custom_profile, "lacp")
        lacp_hello_interval = ET.SubElement(lacp, "lacp_hello_interval")
        lacp_hello_interval.text = kwargs.pop('lacp_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_lacp_lacp_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        lacp = ET.SubElement(kap_custom_profile, "lacp")
        lacp_num_entry = ET.SubElement(lacp, "lacp_num_entry")
        lacp_num_entry.text = kwargs.pop('lacp_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_xstp_xstp_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        xstp = ET.SubElement(kap_custom_profile, "xstp")
        xstp_hello_interval = ET.SubElement(xstp, "xstp_hello_interval")
        xstp_hello_interval.text = kwargs.pop('xstp_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_xstp_xstp_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        xstp = ET.SubElement(kap_custom_profile, "xstp")
        xstp_num_entry = ET.SubElement(xstp, "xstp_num_entry")
        xstp_num_entry.text = kwargs.pop('xstp_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_rpvst_rpvst_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        rpvst = ET.SubElement(kap_custom_profile, "rpvst")
        rpvst_hello_interval = ET.SubElement(rpvst, "rpvst_hello_interval")
        rpvst_hello_interval.text = kwargs.pop('rpvst_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_rpvst_rpvst_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        rpvst = ET.SubElement(kap_custom_profile, "rpvst")
        rpvst_num_entry = ET.SubElement(rpvst, "rpvst_num_entry")
        rpvst_num_entry.text = kwargs.pop('rpvst_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_udld_udld_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        udld = ET.SubElement(kap_custom_profile, "udld")
        udld_hello_interval = ET.SubElement(udld, "udld_hello_interval")
        udld_hello_interval.text = kwargs.pop('udld_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_udld_udld_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        udld = ET.SubElement(kap_custom_profile, "udld")
        udld_num_entry = ET.SubElement(udld, "udld_num_entry")
        udld_num_entry.text = kwargs.pop('udld_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_vxlan_bfd_vxlan_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_vxlan = ET.SubElement(kap_custom_profile, "bfd-vxlan")
        bfd_vxlan_hello_interval = ET.SubElement(bfd_vxlan, "bfd_vxlan_hello_interval")
        bfd_vxlan_hello_interval.text = kwargs.pop('bfd_vxlan_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_vxlan_bfd_vxlan_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_vxlan = ET.SubElement(kap_custom_profile, "bfd-vxlan")
        bfd_vxlan_num_entry = ET.SubElement(bfd_vxlan, "bfd_vxlan_num_entry")
        bfd_vxlan_num_entry.text = kwargs.pop('bfd_vxlan_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_l3_bfd_l3_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_l3 = ET.SubElement(kap_custom_profile, "bfd-l3")
        bfd_l3_hello_interval = ET.SubElement(bfd_l3, "bfd_l3_hello_interval")
        bfd_l3_hello_interval.text = kwargs.pop('bfd_l3_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_bfd_l3_bfd_l3_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        bfd_l3 = ET.SubElement(kap_custom_profile, "bfd-l3")
        bfd_l3_num_entry = ET.SubElement(bfd_l3, "bfd_l3_num_entry")
        bfd_l3_num_entry.text = kwargs.pop('bfd_l3_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_fcoe_fcoe_hello_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        fcoe = ET.SubElement(kap_custom_profile, "fcoe")
        fcoe_hello_interval = ET.SubElement(fcoe, "fcoe_hello_interval")
        fcoe_hello_interval.text = kwargs.pop('fcoe_hello_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hardware_custom_profile_kap_custom_profile_fcoe_fcoe_num_entry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hardware = ET.SubElement(config, "hardware", xmlns="urn:brocade.com:mgmt:brocade-hardware")
        custom_profile = ET.SubElement(hardware, "custom-profile")
        kap_custom_profile = ET.SubElement(custom_profile, "kap-custom-profile")
        name_key = ET.SubElement(kap_custom_profile, "name")
        name_key.text = kwargs.pop('name')
        fcoe = ET.SubElement(kap_custom_profile, "fcoe")
        fcoe_num_entry = ET.SubElement(fcoe, "fcoe_num_entry")
        fcoe_num_entry.text = kwargs.pop('fcoe_num_entry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_flexports_output_flexport_list_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_flexports = ET.Element("get_flexports")
        config = get_flexports
        output = ET.SubElement(get_flexports, "output")
        flexport_list = ET.SubElement(output, "flexport-list")
        port_id = ET.SubElement(flexport_list, "port-id")
        port_id.text = kwargs.pop('port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        