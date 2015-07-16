#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_common_def(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def ip_dns_dom_name_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        dns = ET.SubElement(ip, "dns", xmlns="urn:brocade.com:mgmt:brocade-ip-administration")
        dom_name = ET.SubElement(dns, "dom-name")
        domain_name = ET.SubElement(dom_name, "domain-name")
        domain_name.text = kwargs.pop('domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_dns_name_server_name_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        dns = ET.SubElement(ip, "dns", xmlns="urn:brocade.com:mgmt:brocade-ip-administration")
        name_server = ET.SubElement(dns, "name-server")
        name_server_ip = ET.SubElement(name_server, "name-server-ip")
        name_server_ip.text = kwargs.pop('name_server_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(prefix_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(prefix_list, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_action_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        action_ipp = ET.SubElement(prefix_list, "action-ipp")
        action_ipp.text = kwargs.pop('action_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_prefix_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        prefix_ipp = ET.SubElement(prefix_list, "prefix-ipp")
        prefix_ipp.text = kwargs.pop('prefix_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_ge_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ge_ipp = ET.SubElement(prefix_list, "ge-ipp")
        ge_ipp.text = kwargs.pop('ge_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_le_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        le_ipp = ET.SubElement(prefix_list, "le-ipp")
        le_ipp.text = kwargs.pop('le_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(access_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(access_list, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(access_list, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_ip_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_action = ET.SubElement(access_list, "ip-action")
        ip_action.text = kwargs.pop('ip_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_ip_reg_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_reg_expr = ET.SubElement(access_list, "ip-reg-expr")
        ip_reg_expr.text = kwargs.pop('ip_reg_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(standard, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(standard, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(standard, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_ip_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_action = ET.SubElement(standard, "ip-action")
        ip_action.text = kwargs.pop('ip_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_std_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        std_community_expr = ET.SubElement(standard, "std-community-expr")
        std_community_expr.text = kwargs.pop('std_community_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(extended, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(extended, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(extended, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_ip_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_action = ET.SubElement(extended, "ip-action")
        ip_action.text = kwargs.pop('ip_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_ip_community_reg_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_community_reg_expr = ET.SubElement(extended, "ip-community-reg-expr")
        ip_community_reg_expr.text = kwargs.pop('ip_community_reg_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_ext_community_list_holder_extcommunity_list_extcommunity_list_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_ext_community_list_holder = ET.SubElement(ip, "hide-ext-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        extcommunity_list = ET.SubElement(hide_ext_community_list_holder, "extcommunity-list")
        extcommunity_list_num = ET.SubElement(extcommunity_list, "extcommunity-list-num")
        extcommunity_list_num.text = kwargs.pop('extcommunity_list_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_ext_community_list_holder_extcommunity_list_ext_community_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_ext_community_list_holder = ET.SubElement(ip, "hide-ext-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        extcommunity_list = ET.SubElement(hide_ext_community_list_holder, "extcommunity-list")
        extcommunity_list_num_key = ET.SubElement(extcommunity_list, "extcommunity-list-num")
        extcommunity_list_num_key.text = kwargs.pop('extcommunity_list_num')
        ext_community_action = ET.SubElement(extcommunity_list, "ext-community-action")
        ext_community_action.text = kwargs.pop('ext_community_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_ext_community_list_holder_extcommunity_list_ext_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_ext_community_list_holder = ET.SubElement(ip, "hide-ext-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        extcommunity_list = ET.SubElement(hide_ext_community_list_holder, "extcommunity-list")
        extcommunity_list_num_key = ET.SubElement(extcommunity_list, "extcommunity-list-num")
        extcommunity_list_num_key.text = kwargs.pop('extcommunity_list_num')
        ext_community_expr = ET.SubElement(extcommunity_list, "ext-community-expr")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_router_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        router_id = ET.SubElement(rtm_config, "router-id")
        router_id.text = kwargs.pop('router_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_load_sharing(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        load_sharing = ET.SubElement(rtm_config, "load-sharing")
        load_sharing.text = kwargs.pop('load_sharing')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_static_route_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        static_route_dest = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest.text = kwargs.pop('static_route_dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_static_route_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop.text = kwargs.pop('static_route_next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_route_attributes_metric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        route_attributes = ET.SubElement(static_route_nh, "route-attributes")
        metric = ET.SubElement(route_attributes, "metric")
        metric.text = kwargs.pop('metric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_route_attributes_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        route_attributes = ET.SubElement(static_route_nh, "route-attributes")
        distance = ET.SubElement(route_attributes, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_route_attributes_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        route_attributes = ET.SubElement(static_route_nh, "route-attributes")
        tag = ET.SubElement(route_attributes, "tag")
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_vrf_static_route_next_vrf_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh_vrf = ET.SubElement(route, "static-route-nh-vrf")
        next_hop_vrf_key = ET.SubElement(static_route_nh_vrf, "next-hop-vrf")
        next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
        static_route_next_hop_key = ET.SubElement(static_route_nh_vrf, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        static_route_next_vrf_dest = ET.SubElement(static_route_nh_vrf, "static-route-next-vrf-dest")
        static_route_next_vrf_dest.text = kwargs.pop('static_route_next_vrf_dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_vrf_next_hop_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh_vrf = ET.SubElement(route, "static-route-nh-vrf")
        static_route_next_vrf_dest_key = ET.SubElement(static_route_nh_vrf, "static-route-next-vrf-dest")
        static_route_next_vrf_dest_key.text = kwargs.pop('static_route_next_vrf_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh_vrf, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        next_hop_vrf = ET.SubElement(static_route_nh_vrf, "next-hop-vrf")
        next_hop_vrf.text = kwargs.pop('next_hop_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_vrf_static_route_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh_vrf = ET.SubElement(route, "static-route-nh-vrf")
        static_route_next_vrf_dest_key = ET.SubElement(static_route_nh_vrf, "static-route-next-vrf-dest")
        static_route_next_vrf_dest_key.text = kwargs.pop('static_route_next_vrf_dest')
        next_hop_vrf_key = ET.SubElement(static_route_nh_vrf, "next-hop-vrf")
        next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
        static_route_next_hop = ET.SubElement(static_route_nh_vrf, "static-route-next-hop")
        static_route_next_hop.text = kwargs.pop('static_route_next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_static_route_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        static_route_dest = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest.text = kwargs.pop('static_route_dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_static_route_oif_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        static_route_oif_type = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type.text = kwargs.pop('static_route_oif_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_static_route_oif_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name.text = kwargs.pop('static_route_oif_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_route_attributes_metric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        route_attributes = ET.SubElement(static_route_oif, "route-attributes")
        metric = ET.SubElement(route_attributes, "metric")
        metric.text = kwargs.pop('metric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_route_attributes_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        route_attributes = ET.SubElement(static_route_oif, "route-attributes")
        distance = ET.SubElement(route_attributes, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_route_attributes_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        route_attributes = ET.SubElement(static_route_oif, "route-attributes")
        tag = ET.SubElement(route_attributes, "tag")
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_ipv6route_route_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        ipv6route = ET.SubElement(ipv6, "ipv6route", xmlns="urn:brocade.com:mgmt:brocade-ip-forward")
        route = ET.SubElement(ipv6route, "route")
        dest = ET.SubElement(route, "dest")
        dest.text = kwargs.pop('dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_ipv6route_route_next_ipv6_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        ipv6route = ET.SubElement(ipv6, "ipv6route", xmlns="urn:brocade.com:mgmt:brocade-ip-forward")
        route = ET.SubElement(ipv6route, "route")
        dest_key = ET.SubElement(route, "dest")
        dest_key.text = kwargs.pop('dest')
        next = ET.SubElement(route, "next")
        ipv6_hop = ET.SubElement(next, "ipv6-hop")
        next_hop = ET.SubElement(ipv6_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(prefix_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(prefix_list, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_action_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        action_ipp = ET.SubElement(prefix_list, "action-ipp")
        action_ipp.text = kwargs.pop('action_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_ipv6_prefix_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ipv6_prefix_ipp = ET.SubElement(prefix_list, "ipv6-prefix-ipp")
        ipv6_prefix_ipp.text = kwargs.pop('ipv6_prefix_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_ge_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ge_ipp = ET.SubElement(prefix_list, "ge-ipp")
        ge_ipp.text = kwargs.pop('ge_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_le_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        le_ipp = ET.SubElement(prefix_list, "le-ipp")
        le_ipp.text = kwargs.pop('le_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_enable_global(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        enable_global = ET.SubElement(ipv4, "enable_global")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_gratuitous_arp_timer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        gratuitous_arp = ET.SubElement(ipv4, "gratuitous-arp")
        timer = ET.SubElement(gratuitous_arp, "timer")
        timer.text = kwargs.pop('timer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_gateway_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        gateway_mac_address = ET.SubElement(ipv4, "gateway-mac-address")
        gateway_mac_address.text = kwargs.pop('gateway_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_accept_unicast_arp_request(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        accept_unicast_arp_request = ET.SubElement(ipv4, "accept-unicast-arp-request")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv6_enable_global(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv6 = ET.SubElement(address_family, "ipv6")
        enable_global = ET.SubElement(ipv6, "enable_global")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv6_gratuitous_arp_timer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv6 = ET.SubElement(address_family, "ipv6")
        gratuitous_arp = ET.SubElement(ipv6, "gratuitous-arp")
        timer = ET.SubElement(gratuitous_arp, "timer")
        timer.text = kwargs.pop('timer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv6_gateway_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv6 = ET.SubElement(address_family, "ipv6")
        gateway_mac_address = ET.SubElement(ipv6, "gateway-mac-address")
        gateway_mac_address.text = kwargs.pop('gateway_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_dns_dom_name_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        dns = ET.SubElement(ip, "dns", xmlns="urn:brocade.com:mgmt:brocade-ip-administration")
        dom_name = ET.SubElement(dns, "dom-name")
        domain_name = ET.SubElement(dom_name, "domain-name")
        domain_name.text = kwargs.pop('domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_dns_name_server_name_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        dns = ET.SubElement(ip, "dns", xmlns="urn:brocade.com:mgmt:brocade-ip-administration")
        name_server = ET.SubElement(dns, "name-server")
        name_server_ip = ET.SubElement(name_server, "name-server-ip")
        name_server_ip.text = kwargs.pop('name_server_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(prefix_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(prefix_list, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_action_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        action_ipp = ET.SubElement(prefix_list, "action-ipp")
        action_ipp.text = kwargs.pop('action_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_prefix_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        prefix_ipp = ET.SubElement(prefix_list, "prefix-ipp")
        prefix_ipp.text = kwargs.pop('prefix_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_ge_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ge_ipp = ET.SubElement(prefix_list, "ge-ipp")
        ge_ipp.text = kwargs.pop('ge_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_prefix_holder_prefix_list_le_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ip, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        le_ipp = ET.SubElement(prefix_list, "le-ipp")
        le_ipp.text = kwargs.pop('le_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(access_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(access_list, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(access_list, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_ip_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_action = ET.SubElement(access_list, "ip-action")
        ip_action.text = kwargs.pop('ip_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_as_path_holder_as_path_access_list_ip_reg_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_as_path_holder = ET.SubElement(ip, "hide-as-path-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        as_path = ET.SubElement(hide_as_path_holder, "as-path")
        access_list = ET.SubElement(as_path, "access-list")
        name_key = ET.SubElement(access_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(access_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(access_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_reg_expr = ET.SubElement(access_list, "ip-reg-expr")
        ip_reg_expr.text = kwargs.pop('ip_reg_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(standard, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(standard, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(standard, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_ip_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_action = ET.SubElement(standard, "ip-action")
        ip_action.text = kwargs.pop('ip_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_standard_std_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        standard = ET.SubElement(community_list, "standard")
        name_key = ET.SubElement(standard, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(standard, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(standard, "instance")
        instance_key.text = kwargs.pop('instance')
        std_community_expr = ET.SubElement(standard, "std-community-expr")
        std_community_expr.text = kwargs.pop('std_community_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(extended, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(extended, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(extended, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_ip_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_action = ET.SubElement(extended, "ip-action")
        ip_action.text = kwargs.pop('ip_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_community_list_holder_community_list_extended_ip_community_reg_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_community_list_holder = ET.SubElement(ip, "hide-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        community_list = ET.SubElement(hide_community_list_holder, "community-list")
        extended = ET.SubElement(community_list, "extended")
        name_key = ET.SubElement(extended, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(extended, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(extended, "instance")
        instance_key.text = kwargs.pop('instance')
        ip_community_reg_expr = ET.SubElement(extended, "ip-community-reg-expr")
        ip_community_reg_expr.text = kwargs.pop('ip_community_reg_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_ext_community_list_holder_extcommunity_list_extcommunity_list_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_ext_community_list_holder = ET.SubElement(ip, "hide-ext-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        extcommunity_list = ET.SubElement(hide_ext_community_list_holder, "extcommunity-list")
        extcommunity_list_num = ET.SubElement(extcommunity_list, "extcommunity-list-num")
        extcommunity_list_num.text = kwargs.pop('extcommunity_list_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_ext_community_list_holder_extcommunity_list_ext_community_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_ext_community_list_holder = ET.SubElement(ip, "hide-ext-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        extcommunity_list = ET.SubElement(hide_ext_community_list_holder, "extcommunity-list")
        extcommunity_list_num_key = ET.SubElement(extcommunity_list, "extcommunity-list-num")
        extcommunity_list_num_key.text = kwargs.pop('extcommunity_list_num')
        ext_community_action = ET.SubElement(extcommunity_list, "ext-community-action")
        ext_community_action.text = kwargs.pop('ext_community_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_hide_ext_community_list_holder_extcommunity_list_ext_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_ext_community_list_holder = ET.SubElement(ip, "hide-ext-community-list-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        extcommunity_list = ET.SubElement(hide_ext_community_list_holder, "extcommunity-list")
        extcommunity_list_num_key = ET.SubElement(extcommunity_list, "extcommunity-list-num")
        extcommunity_list_num_key.text = kwargs.pop('extcommunity_list_num')
        ext_community_expr = ET.SubElement(extcommunity_list, "ext-community-expr")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_router_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        router_id = ET.SubElement(rtm_config, "router-id")
        router_id.text = kwargs.pop('router_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_load_sharing(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        load_sharing = ET.SubElement(rtm_config, "load-sharing")
        load_sharing.text = kwargs.pop('load_sharing')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_static_route_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        static_route_dest = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest.text = kwargs.pop('static_route_dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_static_route_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop.text = kwargs.pop('static_route_next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_route_attributes_metric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        route_attributes = ET.SubElement(static_route_nh, "route-attributes")
        metric = ET.SubElement(route_attributes, "metric")
        metric.text = kwargs.pop('metric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_route_attributes_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        route_attributes = ET.SubElement(static_route_nh, "route-attributes")
        distance = ET.SubElement(route_attributes, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_route_attributes_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh = ET.SubElement(route, "static-route-nh")
        static_route_dest_key = ET.SubElement(static_route_nh, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        route_attributes = ET.SubElement(static_route_nh, "route-attributes")
        tag = ET.SubElement(route_attributes, "tag")
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_vrf_static_route_next_vrf_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh_vrf = ET.SubElement(route, "static-route-nh-vrf")
        next_hop_vrf_key = ET.SubElement(static_route_nh_vrf, "next-hop-vrf")
        next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
        static_route_next_hop_key = ET.SubElement(static_route_nh_vrf, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        static_route_next_vrf_dest = ET.SubElement(static_route_nh_vrf, "static-route-next-vrf-dest")
        static_route_next_vrf_dest.text = kwargs.pop('static_route_next_vrf_dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_vrf_next_hop_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh_vrf = ET.SubElement(route, "static-route-nh-vrf")
        static_route_next_vrf_dest_key = ET.SubElement(static_route_nh_vrf, "static-route-next-vrf-dest")
        static_route_next_vrf_dest_key.text = kwargs.pop('static_route_next_vrf_dest')
        static_route_next_hop_key = ET.SubElement(static_route_nh_vrf, "static-route-next-hop")
        static_route_next_hop_key.text = kwargs.pop('static_route_next_hop')
        next_hop_vrf = ET.SubElement(static_route_nh_vrf, "next-hop-vrf")
        next_hop_vrf.text = kwargs.pop('next_hop_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_nh_vrf_static_route_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_nh_vrf = ET.SubElement(route, "static-route-nh-vrf")
        static_route_next_vrf_dest_key = ET.SubElement(static_route_nh_vrf, "static-route-next-vrf-dest")
        static_route_next_vrf_dest_key.text = kwargs.pop('static_route_next_vrf_dest')
        next_hop_vrf_key = ET.SubElement(static_route_nh_vrf, "next-hop-vrf")
        next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
        static_route_next_hop = ET.SubElement(static_route_nh_vrf, "static-route-next-hop")
        static_route_next_hop.text = kwargs.pop('static_route_next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_static_route_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        static_route_dest = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest.text = kwargs.pop('static_route_dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_static_route_oif_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        static_route_oif_type = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type.text = kwargs.pop('static_route_oif_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_static_route_oif_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name.text = kwargs.pop('static_route_oif_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_route_attributes_metric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        route_attributes = ET.SubElement(static_route_oif, "route-attributes")
        metric = ET.SubElement(route_attributes, "metric")
        metric.text = kwargs.pop('metric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_route_attributes_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        route_attributes = ET.SubElement(static_route_oif, "route-attributes")
        distance = ET.SubElement(route_attributes, "distance")
        distance.text = kwargs.pop('distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ip_rtm_config_route_static_route_oif_route_attributes_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ip = ET.SubElement(config, "ip", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
        route = ET.SubElement(rtm_config, "route")
        static_route_oif = ET.SubElement(route, "static-route-oif")
        static_route_dest_key = ET.SubElement(static_route_oif, "static-route-dest")
        static_route_dest_key.text = kwargs.pop('static_route_dest')
        static_route_oif_type_key = ET.SubElement(static_route_oif, "static-route-oif-type")
        static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
        static_route_oif_name_key = ET.SubElement(static_route_oif, "static-route-oif-name")
        static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
        route_attributes = ET.SubElement(static_route_oif, "route-attributes")
        tag = ET.SubElement(route_attributes, "tag")
        tag.text = kwargs.pop('tag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_ipv6route_route_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        ipv6route = ET.SubElement(ipv6, "ipv6route", xmlns="urn:brocade.com:mgmt:brocade-ip-forward")
        route = ET.SubElement(ipv6route, "route")
        dest = ET.SubElement(route, "dest")
        dest.text = kwargs.pop('dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_ipv6route_route_next_ipv6_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        ipv6route = ET.SubElement(ipv6, "ipv6route", xmlns="urn:brocade.com:mgmt:brocade-ip-forward")
        route = ET.SubElement(ipv6route, "route")
        dest_key = ET.SubElement(route, "dest")
        dest_key.text = kwargs.pop('dest')
        next = ET.SubElement(route, "next")
        ipv6_hop = ET.SubElement(next, "ipv6-hop")
        next_hop = ET.SubElement(ipv6_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(prefix_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_seq_keyword(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        seq_keyword = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword.text = kwargs.pop('seq_keyword')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance = ET.SubElement(prefix_list, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_action_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        action_ipp = ET.SubElement(prefix_list, "action-ipp")
        action_ipp.text = kwargs.pop('action_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_ipv6_prefix_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ipv6_prefix_ipp = ET.SubElement(prefix_list, "ipv6-prefix-ipp")
        ipv6_prefix_ipp.text = kwargs.pop('ipv6_prefix_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_ge_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        ge_ipp = ET.SubElement(prefix_list, "ge-ipp")
        ge_ipp.text = kwargs.pop('ge_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ipv6_hide_prefix_holder_prefix_list_le_ipp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ipv6 = ET.SubElement(config, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        hide_prefix_holder = ET.SubElement(ipv6, "hide-prefix-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        prefix_list = ET.SubElement(hide_prefix_holder, "prefix-list")
        name_key = ET.SubElement(prefix_list, "name")
        name_key.text = kwargs.pop('name')
        seq_keyword_key = ET.SubElement(prefix_list, "seq-keyword")
        seq_keyword_key.text = kwargs.pop('seq_keyword')
        instance_key = ET.SubElement(prefix_list, "instance")
        instance_key.text = kwargs.pop('instance')
        le_ipp = ET.SubElement(prefix_list, "le-ipp")
        le_ipp.text = kwargs.pop('le_ipp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_enable_global(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        enable_global = ET.SubElement(ipv4, "enable_global")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_gratuitous_arp_timer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        gratuitous_arp = ET.SubElement(ipv4, "gratuitous-arp")
        timer = ET.SubElement(gratuitous_arp, "timer")
        timer.text = kwargs.pop('timer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_gateway_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        gateway_mac_address = ET.SubElement(ipv4, "gateway-mac-address")
        gateway_mac_address.text = kwargs.pop('gateway_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv4_accept_unicast_arp_request(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv4 = ET.SubElement(address_family, "ipv4")
        accept_unicast_arp_request = ET.SubElement(ipv4, "accept-unicast-arp-request")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv6_enable_global(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv6 = ET.SubElement(address_family, "ipv6")
        enable_global = ET.SubElement(ipv6, "enable_global")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv6_gratuitous_arp_timer(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv6 = ET.SubElement(address_family, "ipv6")
        gratuitous_arp = ET.SubElement(ipv6, "gratuitous-arp")
        timer = ET.SubElement(gratuitous_arp, "timer")
        timer.text = kwargs.pop('timer')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def router_fabric_virtual_gateway_address_family_ipv6_gateway_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        router = ET.SubElement(config, "router", xmlns="urn:brocade.com:mgmt:brocade-common-def")
        fabric_virtual_gateway = ET.SubElement(router, "fabric-virtual-gateway", xmlns="urn:brocade.com:mgmt:brocade-anycast-gateway")
        address_family = ET.SubElement(fabric_virtual_gateway, "address-family")
        ipv6 = ET.SubElement(address_family, "ipv6")
        gateway_mac_address = ET.SubElement(ipv6, "gateway-mac-address")
        gateway_mac_address.text = kwargs.pop('gateway_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        