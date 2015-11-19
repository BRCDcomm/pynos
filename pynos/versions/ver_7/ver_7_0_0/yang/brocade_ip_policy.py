#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ip_policy(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def hide_routemap_holder_route_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(route_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_action_rm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        action_rm = ET.SubElement(route_map, "action-rm")
        action_rm.text = kwargs.pop('action_rm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance = ET.SubElement(route_map, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        vrf = ET.SubElement(match, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_address_ipv6_prefix_list_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        address = ET.SubElement(ipv6, "address")
        ipv6_prefix_list_rmm = ET.SubElement(address, "ipv6-prefix-list-rmm")
        ipv6_prefix_list_rmm.text = kwargs.pop('ipv6_prefix_list_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_address_ipv6_acl_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        address = ET.SubElement(ipv6, "address")
        ipv6_acl_rmm = ET.SubElement(address, "ipv6-acl-rmm")
        ipv6_acl_rmm.text = kwargs.pop('ipv6_acl_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_next_hop_ipv6_prefix_list_rmm_n(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        next_hop = ET.SubElement(ipv6, "next-hop")
        ipv6_prefix_list_rmm_n = ET.SubElement(next_hop, "ipv6-prefix-list-rmm-n")
        ipv6_prefix_list_rmm_n.text = kwargs.pop('ipv6_prefix_list_rmm_n')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_route_source_ipv6_prefix_list_rmrs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        route_source = ET.SubElement(ipv6, "route-source")
        ipv6_prefix_list_rmrs = ET.SubElement(route_source, "ipv6-prefix-list-rmrs")
        ipv6_prefix_list_rmrs.text = kwargs.pop('ipv6_prefix_list_rmrs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_address_prefix_list_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        address = ET.SubElement(ip, "address")
        prefix_list_rmm = ET.SubElement(address, "prefix-list-rmm")
        prefix_list_rmm.text = kwargs.pop('prefix_list_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_address_acl_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        address = ET.SubElement(ip, "address")
        acl_rmm = ET.SubElement(address, "acl-rmm")
        acl_rmm.text = kwargs.pop('acl_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_next_hop_prefix_list_rmm_n(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        next_hop = ET.SubElement(ip, "next-hop")
        prefix_list_rmm_n = ET.SubElement(next_hop, "prefix-list-rmm-n")
        prefix_list_rmm_n.text = kwargs.pop('prefix_list_rmm_n')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_route_source_prefix_list_rmrs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        route_source = ET.SubElement(ip, "route-source")
        prefix_list_rmrs = ET.SubElement(route_source, "prefix-list-rmrs")
        prefix_list_rmrs.text = kwargs.pop('prefix_list_rmrs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_extcommunity_extcommunity_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        extcommunity = ET.SubElement(match, "extcommunity")
        extcommunity_num = ET.SubElement(extcommunity, "extcommunity-num")
        extcommunity_num.text = kwargs.pop('extcommunity_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_metric_metric_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        metric = ET.SubElement(match, "metric")
        metric_rmm = ET.SubElement(metric, "metric-rmm")
        metric_rmm.text = kwargs.pop('metric_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_route_type_route_type_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        route_type = ET.SubElement(match, "route-type")
        route_type_rmm = ET.SubElement(route_type, "route-type-rmm")
        route_type_rmm.text = kwargs.pop('route_type_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_as_path_as_path_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        as_path = ET.SubElement(match, "as-path")
        as_path_access_list_name = ET.SubElement(as_path, "as-path-access-list-name")
        as_path_access_list_name.text = kwargs.pop('as_path_access_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_community_community_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        community = ET.SubElement(match, "community")
        community_access_list_name = ET.SubElement(community, "community-access-list-name")
        community_access_list_name.text = kwargs.pop('community_access_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_next_hop_next_hop_filter_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        next_hop = ET.SubElement(match, "next-hop")
        next_hop_filter_val = ET.SubElement(next_hop, "next-hop-filter-val")
        next_hop_filter_val.text = kwargs.pop('next_hop_filter_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_protocol_static_container_static(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        protocol = ET.SubElement(match, "protocol")
        protocol_static_container = ET.SubElement(protocol, "protocol-static-container")
        static = ET.SubElement(protocol_static_container, "static")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_bgp_protocol_container_protocol_bgp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        protocol = ET.SubElement(match, "protocol")
        bgp_protocol_container = ET.SubElement(protocol, "bgp-protocol-container")
        protocol_bgp = ET.SubElement(bgp_protocol_container, "protocol-bgp")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_bgp_protocol_container_bgp_route_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        protocol = ET.SubElement(match, "protocol")
        bgp_protocol_container = ET.SubElement(protocol, "bgp-protocol-container")
        bgp_route_type = ET.SubElement(bgp_protocol_container, "bgp-route-type")
        bgp_route_type.text = kwargs.pop('bgp_route_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_dscp_dscp_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        dscp = ET.SubElement(ip, "dscp")
        dscp_rms = ET.SubElement(dscp, "dscp-rms")
        dscp_rms.text = kwargs.pop('dscp_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_interface_null0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        interface = ET.SubElement(ip, "interface")
        null0 = ET.SubElement(interface, "null0")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_hop_peer_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_hop = ET.SubElement(ip, "next-hop")
        peer_address = ET.SubElement(next_hop, "peer-address")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_globl_next_global_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        globl = ET.SubElement(ip, "global")
        next_global_hop = ET.SubElement(globl, "next-global-hop")
        next_hop = ET.SubElement(next_global_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_ip_next_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_ip = ET.SubElement(ip, "next-ip")
        next_hop = ET.SubElement(next_ip, "next-hop")
        next_hop = ET.SubElement(next_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_vrf_next_vrf_list_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_vrf = ET.SubElement(ip, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        next_hop_key = ET.SubElement(next_vrf_list, "next-hop")
        next_hop_key.text = kwargs.pop('next_hop')
        vrf = ET.SubElement(next_vrf_list, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_vrf_next_vrf_list_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_vrf = ET.SubElement(ip, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        vrf_key = ET.SubElement(next_vrf_list, "vrf")
        vrf_key.text = kwargs.pop('vrf')
        next_hop = ET.SubElement(next_vrf_list, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_interface_ipv6_null0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        interface = ET.SubElement(ipv6, "interface")
        ipv6_null0 = ET.SubElement(interface, "ipv6-null0")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_globl_next_global_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        globl = ET.SubElement(ipv6, "global")
        next_global_hop = ET.SubElement(globl, "next-global-hop")
        next_hop = ET.SubElement(next_global_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_ip_next_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        next_ip = ET.SubElement(ipv6, "next-ip")
        next_hop = ET.SubElement(next_ip, "next-hop")
        next_hop = ET.SubElement(next_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_vrf_next_vrf_list_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        next_vrf = ET.SubElement(ipv6, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        next_hop_key = ET.SubElement(next_vrf_list, "next-hop")
        next_hop_key.text = kwargs.pop('next_hop')
        vrf = ET.SubElement(next_vrf_list, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_vrf_next_vrf_list_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        next_vrf = ET.SubElement(ipv6, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        vrf_key = ET.SubElement(next_vrf_list, "vrf")
        vrf_key.text = kwargs.pop('vrf')
        next_hop = ET.SubElement(next_vrf_list, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_extcommunity_rt_ASN_NN_rt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        extcommunity = ET.SubElement(set, "extcommunity")
        rt = ET.SubElement(extcommunity, "rt")
        ASN_NN_rt = ET.SubElement(rt, "ASN-NN-rt")
        ASN_NN_rt.text = kwargs.pop('ASN_NN_rt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_extcommunity_soo_ASN_NN_soo(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        extcommunity = ET.SubElement(set, "extcommunity")
        soo = ET.SubElement(extcommunity, "soo")
        ASN_NN_soo = ET.SubElement(soo, "ASN-NN-soo")
        ASN_NN_soo.text = kwargs.pop('ASN_NN_soo')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_community_set_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        community = ET.SubElement(set, "community")
        set_community_expr = ET.SubElement(community, "set-community-expr")
        set_community_expr.text = kwargs.pop('set_community_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_delta_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric = ET.SubElement(set, "metric")
        delta_rms = ET.SubElement(metric, "delta-rms")
        delta_rms.text = kwargs.pop('delta_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_metric_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric = ET.SubElement(set, "metric")
        metric_rms = ET.SubElement(metric, "metric-rms")
        metric_rms.text = kwargs.pop('metric_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_distance_dist_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        distance = ET.SubElement(set, "distance")
        dist_rms = ET.SubElement(distance, "dist-rms")
        dist_rms.text = kwargs.pop('dist_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_route_type_route_type_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        route_type = ET.SubElement(set, "route-type")
        route_type_rms = ET.SubElement(route_type, "route-type-rms")
        route_type_rms.text = kwargs.pop('route_type_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_tag_tag_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        tag = ET.SubElement(set, "tag")
        tag_rms = ET.SubElement(tag, "tag-rms")
        tag_rms.text = kwargs.pop('tag_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_weight_weight_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        weight = ET.SubElement(set, "weight")
        weight_value = ET.SubElement(weight, "weight-value")
        weight_value.text = kwargs.pop('weight_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_as_path_aspath_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        as_path = ET.SubElement(set, "as-path")
        aspath_tag = ET.SubElement(as_path, "aspath-tag")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_as_path_prepend(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        as_path = ET.SubElement(set, "as-path")
        prepend = ET.SubElement(as_path, "prepend")
        prepend.text = kwargs.pop('prepend')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_automatic_tag_tag_empty(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        automatic_tag = ET.SubElement(set, "automatic-tag")
        tag_empty = ET.SubElement(automatic_tag, "tag-empty")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_comm_list_comm_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        comm_list = ET.SubElement(set, "comm-list")
        comm_list_name = ET.SubElement(comm_list, "comm-list-name")
        comm_list_name.text = kwargs.pop('comm_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_comm_list_match_comm_delete(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        comm_list = ET.SubElement(set, "comm-list")
        match_comm_delete = ET.SubElement(comm_list, "match-comm-delete")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_half_life(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        half_life = ET.SubElement(dampening, "half-life")
        half_life.text = kwargs.pop('half_life')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_reuse(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        reuse = ET.SubElement(dampening, "reuse")
        reuse.text = kwargs.pop('reuse')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        suppress = ET.SubElement(dampening, "suppress")
        suppress.text = kwargs.pop('suppress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_max_suppress_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        max_suppress_time = ET.SubElement(dampening, "max-suppress-time")
        max_suppress_time.text = kwargs.pop('max_suppress_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_local_preference_local_preference_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        local_preference = ET.SubElement(set, "local-preference")
        local_preference_value = ET.SubElement(local_preference, "local-preference-value")
        local_preference_value.text = kwargs.pop('local_preference_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_origin_origin_igp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        origin = ET.SubElement(set, "origin")
        origin_igp = ET.SubElement(origin, "origin-igp")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_origin_origin_incomplete(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        origin = ET.SubElement(set, "origin")
        origin_incomplete = ET.SubElement(origin, "origin-incomplete")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_external(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        external = ET.SubElement(metric_type, "external")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_internal(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        internal = ET.SubElement(metric_type, "internal")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_type_1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        type_1 = ET.SubElement(metric_type, "type-1")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_type_2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        type_2 = ET.SubElement(metric_type, "type-2")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_continue_holder_cont(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        continue_holder = ET.SubElement(content, "continue-holder")
        cont = ET.SubElement(continue_holder, "continue")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_continue_holder_continue_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        continue_holder = ET.SubElement(content, "continue-holder")
        continue_val = ET.SubElement(continue_holder, "continue-val")
        continue_val.text = kwargs.pop('continue_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_filter_change_update_delay_holder_filter_change_update_delay_filter_delay_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_filter_change_update_delay_holder = ET.SubElement(config, "hide-filter-change-update-delay-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        filter_change_update_delay = ET.SubElement(hide_filter_change_update_delay_holder, "filter-change-update-delay")
        filter_delay_value = ET.SubElement(filter_change_update_delay, "filter-delay-value")
        filter_delay_value.text = kwargs.pop('filter_delay_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        name = ET.SubElement(route_map, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_action_rm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        action_rm = ET.SubElement(route_map, "action-rm")
        action_rm.text = kwargs.pop('action_rm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_instance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance = ET.SubElement(route_map, "instance")
        instance.text = kwargs.pop('instance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        vrf = ET.SubElement(match, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_address_ipv6_prefix_list_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        address = ET.SubElement(ipv6, "address")
        ipv6_prefix_list_rmm = ET.SubElement(address, "ipv6-prefix-list-rmm")
        ipv6_prefix_list_rmm.text = kwargs.pop('ipv6_prefix_list_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_address_ipv6_acl_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        address = ET.SubElement(ipv6, "address")
        ipv6_acl_rmm = ET.SubElement(address, "ipv6-acl-rmm")
        ipv6_acl_rmm.text = kwargs.pop('ipv6_acl_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_next_hop_ipv6_prefix_list_rmm_n(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        next_hop = ET.SubElement(ipv6, "next-hop")
        ipv6_prefix_list_rmm_n = ET.SubElement(next_hop, "ipv6-prefix-list-rmm-n")
        ipv6_prefix_list_rmm_n.text = kwargs.pop('ipv6_prefix_list_rmm_n')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ipv6_route_source_ipv6_prefix_list_rmrs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ipv6 = ET.SubElement(match, "ipv6")
        route_source = ET.SubElement(ipv6, "route-source")
        ipv6_prefix_list_rmrs = ET.SubElement(route_source, "ipv6-prefix-list-rmrs")
        ipv6_prefix_list_rmrs.text = kwargs.pop('ipv6_prefix_list_rmrs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_address_prefix_list_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        address = ET.SubElement(ip, "address")
        prefix_list_rmm = ET.SubElement(address, "prefix-list-rmm")
        prefix_list_rmm.text = kwargs.pop('prefix_list_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_address_acl_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        address = ET.SubElement(ip, "address")
        acl_rmm = ET.SubElement(address, "acl-rmm")
        acl_rmm.text = kwargs.pop('acl_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_next_hop_prefix_list_rmm_n(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        next_hop = ET.SubElement(ip, "next-hop")
        prefix_list_rmm_n = ET.SubElement(next_hop, "prefix-list-rmm-n")
        prefix_list_rmm_n.text = kwargs.pop('prefix_list_rmm_n')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_ip_route_source_prefix_list_rmrs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        ip = ET.SubElement(match, "ip")
        route_source = ET.SubElement(ip, "route-source")
        prefix_list_rmrs = ET.SubElement(route_source, "prefix-list-rmrs")
        prefix_list_rmrs.text = kwargs.pop('prefix_list_rmrs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_extcommunity_extcommunity_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        extcommunity = ET.SubElement(match, "extcommunity")
        extcommunity_num = ET.SubElement(extcommunity, "extcommunity-num")
        extcommunity_num.text = kwargs.pop('extcommunity_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_metric_metric_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        metric = ET.SubElement(match, "metric")
        metric_rmm = ET.SubElement(metric, "metric-rmm")
        metric_rmm.text = kwargs.pop('metric_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_route_type_route_type_rmm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        route_type = ET.SubElement(match, "route-type")
        route_type_rmm = ET.SubElement(route_type, "route-type-rmm")
        route_type_rmm.text = kwargs.pop('route_type_rmm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_as_path_as_path_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        as_path = ET.SubElement(match, "as-path")
        as_path_access_list_name = ET.SubElement(as_path, "as-path-access-list-name")
        as_path_access_list_name.text = kwargs.pop('as_path_access_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_community_community_access_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        community = ET.SubElement(match, "community")
        community_access_list_name = ET.SubElement(community, "community-access-list-name")
        community_access_list_name.text = kwargs.pop('community_access_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_next_hop_next_hop_filter_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        next_hop = ET.SubElement(match, "next-hop")
        next_hop_filter_val = ET.SubElement(next_hop, "next-hop-filter-val")
        next_hop_filter_val.text = kwargs.pop('next_hop_filter_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_protocol_static_container_static(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        protocol = ET.SubElement(match, "protocol")
        protocol_static_container = ET.SubElement(protocol, "protocol-static-container")
        static = ET.SubElement(protocol_static_container, "static")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_bgp_protocol_container_protocol_bgp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        protocol = ET.SubElement(match, "protocol")
        bgp_protocol_container = ET.SubElement(protocol, "bgp-protocol-container")
        protocol_bgp = ET.SubElement(bgp_protocol_container, "protocol-bgp")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_match_protocol_bgp_protocol_container_bgp_route_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        match = ET.SubElement(content, "match")
        protocol = ET.SubElement(match, "protocol")
        bgp_protocol_container = ET.SubElement(protocol, "bgp-protocol-container")
        bgp_route_type = ET.SubElement(bgp_protocol_container, "bgp-route-type")
        bgp_route_type.text = kwargs.pop('bgp_route_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_dscp_dscp_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        dscp = ET.SubElement(ip, "dscp")
        dscp_rms = ET.SubElement(dscp, "dscp-rms")
        dscp_rms.text = kwargs.pop('dscp_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_interface_null0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        interface = ET.SubElement(ip, "interface")
        null0 = ET.SubElement(interface, "null0")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_hop_peer_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_hop = ET.SubElement(ip, "next-hop")
        peer_address = ET.SubElement(next_hop, "peer-address")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_globl_next_global_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        globl = ET.SubElement(ip, "global")
        next_global_hop = ET.SubElement(globl, "next-global-hop")
        next_hop = ET.SubElement(next_global_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_ip_next_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_ip = ET.SubElement(ip, "next-ip")
        next_hop = ET.SubElement(next_ip, "next-hop")
        next_hop = ET.SubElement(next_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_vrf_next_vrf_list_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_vrf = ET.SubElement(ip, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        next_hop_key = ET.SubElement(next_vrf_list, "next-hop")
        next_hop_key.text = kwargs.pop('next_hop')
        vrf = ET.SubElement(next_vrf_list, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ip_next_vrf_next_vrf_list_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ip = ET.SubElement(set, "ip")
        next_vrf = ET.SubElement(ip, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        vrf_key = ET.SubElement(next_vrf_list, "vrf")
        vrf_key.text = kwargs.pop('vrf')
        next_hop = ET.SubElement(next_vrf_list, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_interface_ipv6_null0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        interface = ET.SubElement(ipv6, "interface")
        ipv6_null0 = ET.SubElement(interface, "ipv6-null0")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_globl_next_global_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        globl = ET.SubElement(ipv6, "global")
        next_global_hop = ET.SubElement(globl, "next-global-hop")
        next_hop = ET.SubElement(next_global_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_ip_next_hop_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        next_ip = ET.SubElement(ipv6, "next-ip")
        next_hop = ET.SubElement(next_ip, "next-hop")
        next_hop = ET.SubElement(next_hop, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_vrf_next_vrf_list_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        next_vrf = ET.SubElement(ipv6, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        next_hop_key = ET.SubElement(next_vrf_list, "next-hop")
        next_hop_key.text = kwargs.pop('next_hop')
        vrf = ET.SubElement(next_vrf_list, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_ipv6_next_vrf_next_vrf_list_next_hop(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        ipv6 = ET.SubElement(set, "ipv6")
        next_vrf = ET.SubElement(ipv6, "next-vrf")
        next_vrf_list = ET.SubElement(next_vrf, "next-vrf-list")
        vrf_key = ET.SubElement(next_vrf_list, "vrf")
        vrf_key.text = kwargs.pop('vrf')
        next_hop = ET.SubElement(next_vrf_list, "next-hop")
        next_hop.text = kwargs.pop('next_hop')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_extcommunity_rt_ASN_NN_rt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        extcommunity = ET.SubElement(set, "extcommunity")
        rt = ET.SubElement(extcommunity, "rt")
        ASN_NN_rt = ET.SubElement(rt, "ASN-NN-rt")
        ASN_NN_rt.text = kwargs.pop('ASN_NN_rt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_extcommunity_soo_ASN_NN_soo(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        extcommunity = ET.SubElement(set, "extcommunity")
        soo = ET.SubElement(extcommunity, "soo")
        ASN_NN_soo = ET.SubElement(soo, "ASN-NN-soo")
        ASN_NN_soo.text = kwargs.pop('ASN_NN_soo')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_community_set_community_expr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        community = ET.SubElement(set, "community")
        set_community_expr = ET.SubElement(community, "set-community-expr")
        set_community_expr.text = kwargs.pop('set_community_expr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_delta_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric = ET.SubElement(set, "metric")
        delta_rms = ET.SubElement(metric, "delta-rms")
        delta_rms.text = kwargs.pop('delta_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_metric_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric = ET.SubElement(set, "metric")
        metric_rms = ET.SubElement(metric, "metric-rms")
        metric_rms.text = kwargs.pop('metric_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_distance_dist_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        distance = ET.SubElement(set, "distance")
        dist_rms = ET.SubElement(distance, "dist-rms")
        dist_rms.text = kwargs.pop('dist_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_route_type_route_type_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        route_type = ET.SubElement(set, "route-type")
        route_type_rms = ET.SubElement(route_type, "route-type-rms")
        route_type_rms.text = kwargs.pop('route_type_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_tag_tag_rms(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        tag = ET.SubElement(set, "tag")
        tag_rms = ET.SubElement(tag, "tag-rms")
        tag_rms.text = kwargs.pop('tag_rms')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_weight_weight_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        weight = ET.SubElement(set, "weight")
        weight_value = ET.SubElement(weight, "weight-value")
        weight_value.text = kwargs.pop('weight_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_as_path_aspath_tag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        as_path = ET.SubElement(set, "as-path")
        aspath_tag = ET.SubElement(as_path, "aspath-tag")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_as_path_prepend(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        as_path = ET.SubElement(set, "as-path")
        prepend = ET.SubElement(as_path, "prepend")
        prepend.text = kwargs.pop('prepend')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_automatic_tag_tag_empty(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        automatic_tag = ET.SubElement(set, "automatic-tag")
        tag_empty = ET.SubElement(automatic_tag, "tag-empty")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_comm_list_comm_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        comm_list = ET.SubElement(set, "comm-list")
        comm_list_name = ET.SubElement(comm_list, "comm-list-name")
        comm_list_name.text = kwargs.pop('comm_list_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_comm_list_match_comm_delete(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        comm_list = ET.SubElement(set, "comm-list")
        match_comm_delete = ET.SubElement(comm_list, "match-comm-delete")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_half_life(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        half_life = ET.SubElement(dampening, "half-life")
        half_life.text = kwargs.pop('half_life')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_reuse(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        reuse = ET.SubElement(dampening, "reuse")
        reuse.text = kwargs.pop('reuse')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        suppress = ET.SubElement(dampening, "suppress")
        suppress.text = kwargs.pop('suppress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_dampening_max_suppress_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        dampening = ET.SubElement(set, "dampening")
        max_suppress_time = ET.SubElement(dampening, "max-suppress-time")
        max_suppress_time.text = kwargs.pop('max_suppress_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_local_preference_local_preference_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        local_preference = ET.SubElement(set, "local-preference")
        local_preference_value = ET.SubElement(local_preference, "local-preference-value")
        local_preference_value.text = kwargs.pop('local_preference_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_origin_origin_igp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        origin = ET.SubElement(set, "origin")
        origin_igp = ET.SubElement(origin, "origin-igp")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_origin_origin_incomplete(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        origin = ET.SubElement(set, "origin")
        origin_incomplete = ET.SubElement(origin, "origin-incomplete")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_external(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        external = ET.SubElement(metric_type, "external")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_internal(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        internal = ET.SubElement(metric_type, "internal")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_type_1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        type_1 = ET.SubElement(metric_type, "type-1")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_set_metric_type_type_2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        set = ET.SubElement(content, "set")
        metric_type = ET.SubElement(set, "metric-type")
        type_2 = ET.SubElement(metric_type, "type-2")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_continue_holder_cont(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        continue_holder = ET.SubElement(content, "continue-holder")
        cont = ET.SubElement(continue_holder, "continue")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_routemap_holder_route_map_content_continue_holder_continue_val(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_routemap_holder = ET.SubElement(config, "hide-routemap-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        route_map = ET.SubElement(hide_routemap_holder, "route-map")
        name_key = ET.SubElement(route_map, "name")
        name_key.text = kwargs.pop('name')
        action_rm_key = ET.SubElement(route_map, "action-rm")
        action_rm_key.text = kwargs.pop('action_rm')
        instance_key = ET.SubElement(route_map, "instance")
        instance_key.text = kwargs.pop('instance')
        content = ET.SubElement(route_map, "content")
        continue_holder = ET.SubElement(content, "continue-holder")
        continue_val = ET.SubElement(continue_holder, "continue-val")
        continue_val.text = kwargs.pop('continue_val')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def hide_filter_change_update_delay_holder_filter_change_update_delay_filter_delay_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        hide_filter_change_update_delay_holder = ET.SubElement(config, "hide-filter-change-update-delay-holder", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
        filter_change_update_delay = ET.SubElement(hide_filter_change_update_delay_holder, "filter-change-update-delay")
        filter_delay_value = ET.SubElement(filter_change_update_delay, "filter-delay-value")
        filter_delay_value.text = kwargs.pop('filter_delay_value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        