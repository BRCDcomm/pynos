#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_tunnels(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def nsx_controller_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name = ET.SubElement(nsx_controller, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        address = ET.SubElement(connection_addr, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        port = ET.SubElement(connection_addr, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_method(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        method = ET.SubElement(connection_addr, "method")
        method.text = kwargs.pop('method')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_reconnect_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        reconnect_interval = ET.SubElement(nsx_controller, "reconnect-interval")
        reconnect_interval.text = kwargs.pop('reconnect_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(nsx_controller, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name = ET.SubElement(overlay_gateway, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_gw_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        gw_type = ET.SubElement(overlay_gateway, "gw-type")
        gw_type.text = kwargs.pop('gw_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_ve_ve_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        ip = ET.SubElement(overlay_gateway, "ip")
        interface = ET.SubElement(ip, "interface")
        ve = ET.SubElement(interface, "ve")
        ve_id = ET.SubElement(ve, "ve-id")
        ve_id.text = kwargs.pop('ve_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_ve_vrrp_extended_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        ip = ET.SubElement(overlay_gateway, "ip")
        interface = ET.SubElement(ip, "interface")
        ve = ET.SubElement(interface, "ve")
        vrrp_extended_group = ET.SubElement(ve, "vrrp-extended-group")
        vrrp_extended_group.text = kwargs.pop('vrrp_extended_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_loopback_loopback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        ip = ET.SubElement(overlay_gateway, "ip")
        interface = ET.SubElement(ip, "interface")
        loopback = ET.SubElement(interface, "loopback")
        loopback_id = ET.SubElement(loopback, "loopback-id")
        loopback_id.text = kwargs.pop('loopback_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_rbridge_id_rb_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        rb_add = ET.SubElement(rbridge_id, "rb-add")
        rb_add.text = kwargs.pop('rb_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_rbridge_id_rb_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        rb_remove = ET.SubElement(rbridge_id, "rb-remove")
        rb_remove.text = kwargs.pop('rb_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_vlan_vid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        vlan = ET.SubElement(attach, "vlan")
        mac_key = ET.SubElement(vlan, "mac")
        mac_key.text = kwargs.pop('mac')
        vid = ET.SubElement(vlan, "vid")
        vid.text = kwargs.pop('vid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_vlan_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        vlan = ET.SubElement(attach, "vlan")
        vid_key = ET.SubElement(vlan, "vid")
        vid_key.text = kwargs.pop('vid')
        mac = ET.SubElement(vlan, "mac")
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_mapping_vid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        map = ET.SubElement(overlay_gateway, "map")
        vlan_vni_mapping = ET.SubElement(map, "vlan-vni-mapping")
        vid = ET.SubElement(vlan_vni_mapping, "vid")
        vid.text = kwargs.pop('vid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_mapping_vni(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        map = ET.SubElement(overlay_gateway, "map")
        vlan_vni_mapping = ET.SubElement(map, "vlan-vni-mapping")
        vid_key = ET.SubElement(vlan_vni_mapping, "vid")
        vid_key.text = kwargs.pop('vid')
        vni = ET.SubElement(vlan_vni_mapping, "vni")
        vni.text = kwargs.pop('vni')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_auto(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        map = ET.SubElement(overlay_gateway, "map")
        vlan = ET.SubElement(map, "vlan")
        vni = ET.SubElement(vlan, "vni")
        auto = ET.SubElement(vni, "auto")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name = ET.SubElement(site, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_tunnel_dst_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        tunnel_dst = ET.SubElement(site, "tunnel-dst")
        address = ET.SubElement(tunnel_dst, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_extend_vlan_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        extend = ET.SubElement(site, "extend")
        vlan = ET.SubElement(extend, "vlan")
        add = ET.SubElement(vlan, "add")
        add.text = kwargs.pop('add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_extend_vlan_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        extend = ET.SubElement(site, "extend")
        vlan = ET.SubElement(extend, "vlan")
        remove = ET.SubElement(vlan, "remove")
        remove.text = kwargs.pop('remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_mac_learning_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        mac_learning = ET.SubElement(site, "mac-learning")
        protocol = ET.SubElement(mac_learning, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd_enable = ET.SubElement(site, "bfd-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_min_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        interval = ET.SubElement(params, "interval")
        min_tx = ET.SubElement(interval, "min-tx")
        min_tx.text = kwargs.pop('min_tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_min_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        interval = ET.SubElement(params, "interval")
        min_rx = ET.SubElement(interval, "min-rx")
        min_rx.text = kwargs.pop('min_rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_multiplier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        interval = ET.SubElement(params, "interval")
        multiplier = ET.SubElement(interval, "multiplier")
        multiplier.text = kwargs.pop('multiplier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_bfd_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        bfd_shutdown = ET.SubElement(params, "bfd-shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        shutdown = ET.SubElement(site, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_stats_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(overlay_gateway, "enable")
        statistics = ET.SubElement(enable, "statistics")
        stats_direction = ET.SubElement(statistics, "stats-direction")
        stats_direction.text = kwargs.pop('stats_direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_vlan_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(overlay_gateway, "enable")
        statistics = ET.SubElement(enable, "statistics")
        vlan_action = ET.SubElement(statistics, "vlan-action")
        vlan_action.text = kwargs.pop('vlan_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_vlan_list(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(overlay_gateway, "enable")
        statistics = ET.SubElement(enable, "statistics")
        vlan_list = ET.SubElement(statistics, "vlan-list")
        vlan_list.text = kwargs.pop('vlan_list')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session = ET.SubElement(monitor, "session")
        session.text = kwargs.pop('session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        direction = ET.SubElement(monitor, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_remote_endpoint(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        remote_endpoint = ET.SubElement(monitor, "remote-endpoint")
        remote_endpoint.text = kwargs.pop('remote_endpoint')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        vlan_leaf = ET.SubElement(monitor, "vlan-leaf")
        vlan_leaf.text = kwargs.pop('vlan_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_add_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        vlan_add_remove = ET.SubElement(monitor, "vlan-add-remove")
        vlan_add_remove.text = kwargs.pop('vlan_add_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        vlan_range = ET.SubElement(monitor, "vlan-range")
        vlan_range.text = kwargs.pop('vlan_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name.text = kwargs.pop('sflow_profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_remote_endpoint(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        sflow_remote_endpoint = ET.SubElement(sflow, "sflow-remote-endpoint")
        sflow_remote_endpoint.text = kwargs.pop('sflow_remote_endpoint')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_vlan_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        sflow_vlan_action = ET.SubElement(sflow, "sflow-vlan-action")
        sflow_vlan_action.text = kwargs.pop('sflow_vlan_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_vlan_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        sflow_vlan_range = ET.SubElement(sflow, "sflow-vlan-range")
        sflow_vlan_range.text = kwargs.pop('sflow_vlan_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_in_cg_mac_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        in_cg = ET.SubElement(mac, "in")
        mac_acl_in_name = ET.SubElement(in_cg, "mac-acl-in-name")
        mac_acl_in_name.text = kwargs.pop('mac_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_in_cg_mac_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        in_cg = ET.SubElement(mac, "in")
        mac_acl_in_dir = ET.SubElement(in_cg, "mac-acl-in-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_out_mac_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        out = ET.SubElement(mac, "out")
        mac_acl_out_name = ET.SubElement(out, "mac-acl-out-name")
        mac_acl_out_name.text = kwargs.pop('mac_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_out_mac_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        out = ET.SubElement(mac, "out")
        mac_acl_out_dir = ET.SubElement(out, "mac-acl-out-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_in_cg_ipv4_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        in_cg = ET.SubElement(ipv4, "in")
        ipv4_acl_in_name = ET.SubElement(in_cg, "ipv4-acl-in-name")
        ipv4_acl_in_name.text = kwargs.pop('ipv4_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_in_cg_ipv4_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        in_cg = ET.SubElement(ipv4, "in")
        ipv4_acl_in_dir = ET.SubElement(in_cg, "ipv4-acl-in-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_out_ipv4_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        out = ET.SubElement(ipv4, "out")
        ipv4_acl_out_name = ET.SubElement(out, "ipv4-acl-out-name")
        ipv4_acl_out_name.text = kwargs.pop('ipv4_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_out_ipv4_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        out = ET.SubElement(ipv4, "out")
        ipv4_acl_out_dir = ET.SubElement(out, "ipv4-acl-out-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_in_cg_ipv6_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        in_cg = ET.SubElement(ipv6, "in")
        ipv6_acl_in_name = ET.SubElement(in_cg, "ipv6-acl-in-name")
        ipv6_acl_in_name.text = kwargs.pop('ipv6_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_in_cg_ipv6_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        in_cg = ET.SubElement(ipv6, "in")
        ipv6_acl_in_dir = ET.SubElement(in_cg, "ipv6-acl-in-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_out_ipv6_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        out = ET.SubElement(ipv6, "out")
        ipv6_acl_out_name = ET.SubElement(out, "ipv6-acl-out-name")
        ipv6_acl_out_name.text = kwargs.pop('ipv6_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_out_ipv6_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        out = ET.SubElement(ipv6, "out")
        ipv6_acl_out_dir = ET.SubElement(out, "ipv6-acl-out-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(overlay_gateway, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name = ET.SubElement(ovsdb_server, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(ovsdb_server, "name")
        name_key.text = kwargs.pop('name')
        port = ET.SubElement(ovsdb_server, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(ovsdb_server, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(ovsdb_server, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name = ET.SubElement(nsx_controller, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        address = ET.SubElement(connection_addr, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        port = ET.SubElement(connection_addr, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_connection_addr_method(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        connection_addr = ET.SubElement(nsx_controller, "connection-addr")
        method = ET.SubElement(connection_addr, "method")
        method.text = kwargs.pop('method')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_reconnect_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        reconnect_interval = ET.SubElement(nsx_controller, "reconnect-interval")
        reconnect_interval.text = kwargs.pop('reconnect_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nsx_controller_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nsx_controller = ET.SubElement(config, "nsx-controller", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(nsx_controller, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(nsx_controller, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name = ET.SubElement(overlay_gateway, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_gw_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        gw_type = ET.SubElement(overlay_gateway, "gw-type")
        gw_type.text = kwargs.pop('gw_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_ve_ve_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        ip = ET.SubElement(overlay_gateway, "ip")
        interface = ET.SubElement(ip, "interface")
        ve = ET.SubElement(interface, "ve")
        ve_id = ET.SubElement(ve, "ve-id")
        ve_id.text = kwargs.pop('ve_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_ve_vrrp_extended_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        ip = ET.SubElement(overlay_gateway, "ip")
        interface = ET.SubElement(ip, "interface")
        ve = ET.SubElement(interface, "ve")
        vrrp_extended_group = ET.SubElement(ve, "vrrp-extended-group")
        vrrp_extended_group.text = kwargs.pop('vrrp_extended_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_ip_interface_loopback_loopback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        ip = ET.SubElement(overlay_gateway, "ip")
        interface = ET.SubElement(ip, "interface")
        loopback = ET.SubElement(interface, "loopback")
        loopback_id = ET.SubElement(loopback, "loopback-id")
        loopback_id.text = kwargs.pop('loopback_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_rbridge_id_rb_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        rb_add = ET.SubElement(rbridge_id, "rb-add")
        rb_add.text = kwargs.pop('rb_add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_rbridge_id_rb_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        rbridge_id = ET.SubElement(attach, "rbridge-id")
        rb_remove = ET.SubElement(rbridge_id, "rb-remove")
        rb_remove.text = kwargs.pop('rb_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_vlan_vid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        vlan = ET.SubElement(attach, "vlan")
        mac_key = ET.SubElement(vlan, "mac")
        mac_key.text = kwargs.pop('mac')
        vid = ET.SubElement(vlan, "vid")
        vid.text = kwargs.pop('vid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_attach_vlan_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        attach = ET.SubElement(overlay_gateway, "attach")
        vlan = ET.SubElement(attach, "vlan")
        vid_key = ET.SubElement(vlan, "vid")
        vid_key.text = kwargs.pop('vid')
        mac = ET.SubElement(vlan, "mac")
        mac.text = kwargs.pop('mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_mapping_vid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        map = ET.SubElement(overlay_gateway, "map")
        vlan_vni_mapping = ET.SubElement(map, "vlan-vni-mapping")
        vid = ET.SubElement(vlan_vni_mapping, "vid")
        vid.text = kwargs.pop('vid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_mapping_vni(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        map = ET.SubElement(overlay_gateway, "map")
        vlan_vni_mapping = ET.SubElement(map, "vlan-vni-mapping")
        vid_key = ET.SubElement(vlan_vni_mapping, "vid")
        vid_key.text = kwargs.pop('vid')
        vni = ET.SubElement(vlan_vni_mapping, "vni")
        vni.text = kwargs.pop('vni')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_map_vlan_vni_auto(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        map = ET.SubElement(overlay_gateway, "map")
        vlan = ET.SubElement(map, "vlan")
        vni = ET.SubElement(vlan, "vni")
        auto = ET.SubElement(vni, "auto")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name = ET.SubElement(site, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_tunnel_dst_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        tunnel_dst = ET.SubElement(site, "tunnel-dst")
        address = ET.SubElement(tunnel_dst, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_extend_vlan_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        extend = ET.SubElement(site, "extend")
        vlan = ET.SubElement(extend, "vlan")
        add = ET.SubElement(vlan, "add")
        add.text = kwargs.pop('add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_extend_vlan_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        extend = ET.SubElement(site, "extend")
        vlan = ET.SubElement(extend, "vlan")
        remove = ET.SubElement(vlan, "remove")
        remove.text = kwargs.pop('remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_mac_learning_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        mac_learning = ET.SubElement(site, "mac-learning")
        protocol = ET.SubElement(mac_learning, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd_enable = ET.SubElement(site, "bfd-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_min_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        interval = ET.SubElement(params, "interval")
        min_tx = ET.SubElement(interval, "min-tx")
        min_tx.text = kwargs.pop('min_tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_min_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        interval = ET.SubElement(params, "interval")
        min_rx = ET.SubElement(interval, "min-rx")
        min_rx.text = kwargs.pop('min_rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_interval_multiplier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        interval = ET.SubElement(params, "interval")
        multiplier = ET.SubElement(interval, "multiplier")
        multiplier.text = kwargs.pop('multiplier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_bfd_params_bfd_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        bfd = ET.SubElement(site, "bfd")
        params = ET.SubElement(bfd, "params")
        bfd_shutdown = ET.SubElement(params, "bfd-shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_site_shutdown(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        site = ET.SubElement(overlay_gateway, "site")
        name_key = ET.SubElement(site, "name")
        name_key.text = kwargs.pop('name')
        shutdown = ET.SubElement(site, "shutdown")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_stats_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(overlay_gateway, "enable")
        statistics = ET.SubElement(enable, "statistics")
        stats_direction = ET.SubElement(statistics, "stats-direction")
        stats_direction.text = kwargs.pop('stats_direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_vlan_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(overlay_gateway, "enable")
        statistics = ET.SubElement(enable, "statistics")
        vlan_action = ET.SubElement(statistics, "vlan-action")
        vlan_action.text = kwargs.pop('vlan_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_enable_statistics_vlan_list(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(overlay_gateway, "enable")
        statistics = ET.SubElement(enable, "statistics")
        vlan_list = ET.SubElement(statistics, "vlan-list")
        vlan_list.text = kwargs.pop('vlan_list')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session = ET.SubElement(monitor, "session")
        session.text = kwargs.pop('session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_direction(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        direction = ET.SubElement(monitor, "direction")
        direction.text = kwargs.pop('direction')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_remote_endpoint(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        remote_endpoint = ET.SubElement(monitor, "remote-endpoint")
        remote_endpoint.text = kwargs.pop('remote_endpoint')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        vlan_leaf = ET.SubElement(monitor, "vlan-leaf")
        vlan_leaf.text = kwargs.pop('vlan_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_add_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        vlan_add_remove = ET.SubElement(monitor, "vlan-add-remove")
        vlan_add_remove.text = kwargs.pop('vlan_add_remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_monitor_vlan_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        monitor = ET.SubElement(overlay_gateway, "monitor")
        session_key = ET.SubElement(monitor, "session")
        session_key.text = kwargs.pop('session')
        vlan_range = ET.SubElement(monitor, "vlan-range")
        vlan_range.text = kwargs.pop('vlan_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name.text = kwargs.pop('sflow_profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_remote_endpoint(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        sflow_remote_endpoint = ET.SubElement(sflow, "sflow-remote-endpoint")
        sflow_remote_endpoint.text = kwargs.pop('sflow_remote_endpoint')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_vlan_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        sflow_vlan_action = ET.SubElement(sflow, "sflow-vlan-action")
        sflow_vlan_action.text = kwargs.pop('sflow_vlan_action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_sflow_sflow_vlan_range(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        sflow = ET.SubElement(overlay_gateway, "sflow")
        sflow_profile_name_key = ET.SubElement(sflow, "sflow-profile-name")
        sflow_profile_name_key.text = kwargs.pop('sflow_profile_name')
        sflow_vlan_range = ET.SubElement(sflow, "sflow-vlan-range")
        sflow_vlan_range.text = kwargs.pop('sflow_vlan_range')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_in_cg_mac_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        in_cg = ET.SubElement(mac, "in")
        mac_acl_in_name = ET.SubElement(in_cg, "mac-acl-in-name")
        mac_acl_in_name.text = kwargs.pop('mac_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_in_cg_mac_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        in_cg = ET.SubElement(mac, "in")
        mac_acl_in_dir = ET.SubElement(in_cg, "mac-acl-in-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_out_mac_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        out = ET.SubElement(mac, "out")
        mac_acl_out_name = ET.SubElement(out, "mac-acl-out-name")
        mac_acl_out_name.text = kwargs.pop('mac_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_mac_out_mac_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        mac = ET.SubElement(access_lists, "mac")
        out = ET.SubElement(mac, "out")
        mac_acl_out_dir = ET.SubElement(out, "mac-acl-out-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_in_cg_ipv4_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        in_cg = ET.SubElement(ipv4, "in")
        ipv4_acl_in_name = ET.SubElement(in_cg, "ipv4-acl-in-name")
        ipv4_acl_in_name.text = kwargs.pop('ipv4_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_in_cg_ipv4_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        in_cg = ET.SubElement(ipv4, "in")
        ipv4_acl_in_dir = ET.SubElement(in_cg, "ipv4-acl-in-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_out_ipv4_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        out = ET.SubElement(ipv4, "out")
        ipv4_acl_out_name = ET.SubElement(out, "ipv4-acl-out-name")
        ipv4_acl_out_name.text = kwargs.pop('ipv4_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv4_out_ipv4_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv4 = ET.SubElement(access_lists, "ipv4")
        out = ET.SubElement(ipv4, "out")
        ipv4_acl_out_dir = ET.SubElement(out, "ipv4-acl-out-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_in_cg_ipv6_acl_in_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        in_cg = ET.SubElement(ipv6, "in")
        ipv6_acl_in_name = ET.SubElement(in_cg, "ipv6-acl-in-name")
        ipv6_acl_in_name.text = kwargs.pop('ipv6_acl_in_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_in_cg_ipv6_acl_in_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        in_cg = ET.SubElement(ipv6, "in")
        ipv6_acl_in_dir = ET.SubElement(in_cg, "ipv6-acl-in-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_out_ipv6_acl_out_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        out = ET.SubElement(ipv6, "out")
        ipv6_acl_out_name = ET.SubElement(out, "ipv6-acl-out-name")
        ipv6_acl_out_name.text = kwargs.pop('ipv6_acl_out_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_access_lists_ipv6_out_ipv6_acl_out_dir(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        access_lists = ET.SubElement(overlay_gateway, "access-lists")
        ipv6 = ET.SubElement(access_lists, "ipv6")
        out = ET.SubElement(ipv6, "out")
        ipv6_acl_out_dir = ET.SubElement(out, "ipv6-acl-out-dir")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def overlay_gateway_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        overlay_gateway = ET.SubElement(config, "overlay-gateway", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(overlay_gateway, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(overlay_gateway, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name = ET.SubElement(ovsdb_server, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(ovsdb_server, "name")
        name_key.text = kwargs.pop('name')
        port = ET.SubElement(ovsdb_server, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ovsdb_server_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ovsdb_server = ET.SubElement(config, "ovsdb-server", xmlns="urn:brocade.com:mgmt:brocade-tunnels")
        name_key = ET.SubElement(ovsdb_server, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(ovsdb_server, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        