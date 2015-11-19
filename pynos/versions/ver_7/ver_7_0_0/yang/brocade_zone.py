#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_zone(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def zoning_defined_configuration_cfg_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        cfg = ET.SubElement(defined_configuration, "cfg")
        cfg_name = ET.SubElement(cfg, "cfg-name")
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_cfg_member_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        cfg = ET.SubElement(defined_configuration, "cfg")
        cfg_name_key = ET.SubElement(cfg, "cfg-name")
        cfg_name_key.text = kwargs.pop('cfg_name')
        member_zone = ET.SubElement(cfg, "member-zone")
        zone_name = ET.SubElement(member_zone, "zone-name")
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        zone = ET.SubElement(defined_configuration, "zone")
        zone_name = ET.SubElement(zone, "zone-name")
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_zone_member_entry_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        zone = ET.SubElement(defined_configuration, "zone")
        zone_name_key = ET.SubElement(zone, "zone-name")
        zone_name_key.text = kwargs.pop('zone_name')
        member_entry = ET.SubElement(zone, "member-entry")
        entry_name = ET.SubElement(member_entry, "entry-name")
        entry_name.text = kwargs.pop('entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_alias_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        alias = ET.SubElement(defined_configuration, "alias")
        alias_name = ET.SubElement(alias, "alias-name")
        alias_name.text = kwargs.pop('alias_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_alias_member_entry_alias_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        alias = ET.SubElement(defined_configuration, "alias")
        alias_name_key = ET.SubElement(alias, "alias-name")
        alias_name_key.text = kwargs.pop('alias_name')
        member_entry = ET.SubElement(alias, "member-entry")
        alias_entry_name = ET.SubElement(member_entry, "alias-entry-name")
        alias_entry_name.text = kwargs.pop('alias_entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        cfg_name = ET.SubElement(enabled_configuration, "cfg-name")
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_default_zone_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        default_zone_access = ET.SubElement(enabled_configuration, "default-zone-access")
        default_zone_access.text = kwargs.pop('default_zone_access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_cfg_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        cfg_action = ET.SubElement(enabled_configuration, "cfg-action")
        cfg_action.text = kwargs.pop('cfg_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_input_request_type_get_request_zone_name_pattern(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        input = ET.SubElement(show_zoning_enabled_configuration, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        zone_name_pattern = ET.SubElement(get_request, "zone-name-pattern")
        zone_name_pattern.text = kwargs.pop('zone_name_pattern')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_input_request_type_get_next_request_last_rcvd_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        input = ET.SubElement(show_zoning_enabled_configuration, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_zone_name = ET.SubElement(get_next_request, "last-rcvd-zone-name")
        last_rcvd_zone_name.text = kwargs.pop('last_rcvd_zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        cfg_name = ET.SubElement(enabled_configuration, "cfg-name")
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_enabled_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        enabled_zone = ET.SubElement(enabled_configuration, "enabled-zone")
        zone_name = ET.SubElement(enabled_zone, "zone-name")
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_enabled_zone_member_entry_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        enabled_zone = ET.SubElement(enabled_configuration, "enabled-zone")
        zone_name_key = ET.SubElement(enabled_zone, "zone-name")
        zone_name_key.text = kwargs.pop('zone_name')
        member_entry = ET.SubElement(enabled_zone, "member-entry")
        entry_name = ET.SubElement(member_entry, "entry-name")
        entry_name.text = kwargs.pop('entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        has_more = ET.SubElement(enabled_configuration, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_cfg_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        cfg = ET.SubElement(defined_configuration, "cfg")
        cfg_name = ET.SubElement(cfg, "cfg-name")
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_cfg_member_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        cfg = ET.SubElement(defined_configuration, "cfg")
        cfg_name_key = ET.SubElement(cfg, "cfg-name")
        cfg_name_key.text = kwargs.pop('cfg_name')
        member_zone = ET.SubElement(cfg, "member-zone")
        zone_name = ET.SubElement(member_zone, "zone-name")
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        zone = ET.SubElement(defined_configuration, "zone")
        zone_name = ET.SubElement(zone, "zone-name")
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_zone_member_entry_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        zone = ET.SubElement(defined_configuration, "zone")
        zone_name_key = ET.SubElement(zone, "zone-name")
        zone_name_key.text = kwargs.pop('zone_name')
        member_entry = ET.SubElement(zone, "member-entry")
        entry_name = ET.SubElement(member_entry, "entry-name")
        entry_name.text = kwargs.pop('entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_alias_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        alias = ET.SubElement(defined_configuration, "alias")
        alias_name = ET.SubElement(alias, "alias-name")
        alias_name.text = kwargs.pop('alias_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_defined_configuration_alias_member_entry_alias_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        defined_configuration = ET.SubElement(zoning, "defined-configuration")
        alias = ET.SubElement(defined_configuration, "alias")
        alias_name_key = ET.SubElement(alias, "alias-name")
        alias_name_key.text = kwargs.pop('alias_name')
        member_entry = ET.SubElement(alias, "member-entry")
        alias_entry_name = ET.SubElement(member_entry, "alias-entry-name")
        alias_entry_name.text = kwargs.pop('alias_entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        cfg_name = ET.SubElement(enabled_configuration, "cfg-name")
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_default_zone_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        default_zone_access = ET.SubElement(enabled_configuration, "default-zone-access")
        default_zone_access.text = kwargs.pop('default_zone_access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def zoning_enabled_configuration_cfg_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        zoning = ET.SubElement(config, "zoning", xmlns="urn:brocade.com:mgmt:brocade-zone")
        enabled_configuration = ET.SubElement(zoning, "enabled-configuration")
        cfg_action = ET.SubElement(enabled_configuration, "cfg-action")
        cfg_action.text = kwargs.pop('cfg_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_input_request_type_get_request_zone_name_pattern(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        input = ET.SubElement(show_zoning_enabled_configuration, "input")
        request_type = ET.SubElement(input, "request-type")
        get_request = ET.SubElement(request_type, "get-request")
        zone_name_pattern = ET.SubElement(get_request, "zone-name-pattern")
        zone_name_pattern.text = kwargs.pop('zone_name_pattern')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_input_request_type_get_next_request_last_rcvd_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        input = ET.SubElement(show_zoning_enabled_configuration, "input")
        request_type = ET.SubElement(input, "request-type")
        get_next_request = ET.SubElement(request_type, "get-next-request")
        last_rcvd_zone_name = ET.SubElement(get_next_request, "last-rcvd-zone-name")
        last_rcvd_zone_name.text = kwargs.pop('last_rcvd_zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_cfg_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        cfg_name = ET.SubElement(enabled_configuration, "cfg-name")
        cfg_name.text = kwargs.pop('cfg_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_enabled_zone_zone_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        enabled_zone = ET.SubElement(enabled_configuration, "enabled-zone")
        zone_name = ET.SubElement(enabled_zone, "zone-name")
        zone_name.text = kwargs.pop('zone_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_enabled_zone_member_entry_entry_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        enabled_zone = ET.SubElement(enabled_configuration, "enabled-zone")
        zone_name_key = ET.SubElement(enabled_zone, "zone-name")
        zone_name_key.text = kwargs.pop('zone_name')
        member_entry = ET.SubElement(enabled_zone, "member-entry")
        entry_name = ET.SubElement(member_entry, "entry-name")
        entry_name.text = kwargs.pop('entry_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_zoning_enabled_configuration_output_enabled_configuration_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_zoning_enabled_configuration = ET.Element("show_zoning_enabled_configuration")
        config = show_zoning_enabled_configuration
        output = ET.SubElement(show_zoning_enabled_configuration, "output")
        enabled_configuration = ET.SubElement(output, "enabled-configuration")
        has_more = ET.SubElement(enabled_configuration, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        