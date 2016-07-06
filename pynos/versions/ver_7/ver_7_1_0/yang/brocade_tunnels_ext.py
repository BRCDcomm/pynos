#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_tunnels_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_tunnel_info_input_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        page_cursor = ET.SubElement(input, "page-cursor")
        page_cursor.text = kwargs.pop('page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_id_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_id = ET.SubElement(filter_type, "filter-by-id")
        id = ET.SubElement(filter_by_id, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_mode_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_mode = ET.SubElement(filter_type, "filter-by-mode")
        mode = ET.SubElement(filter_by_mode, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_gateway_gw_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_gateway = ET.SubElement(filter_type, "filter-by-gateway")
        gw_name = ET.SubElement(filter_by_gateway, "gw-name")
        gw_name.text = kwargs.pop('gw_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_sip_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_sip = ET.SubElement(filter_type, "filter-by-sip")
        src_ip = ET.SubElement(filter_by_sip, "src-ip")
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_dip_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_dip = ET.SubElement(filter_type, "filter-by-dip")
        dest_ip = ET.SubElement(filter_by_dip, "dest-ip")
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_cfg_src_config_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_cfg_src = ET.SubElement(filter_type, "filter-by-cfg-src")
        config_src = ET.SubElement(filter_by_cfg_src, "config-src")
        config_src.text = kwargs.pop('config_src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_site_site_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_site = ET.SubElement(filter_type, "filter-by-site")
        site_name = ET.SubElement(filter_by_site, "site-name")
        site_name.text = kwargs.pop('site_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_adm_state_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_adm_state = ET.SubElement(filter_type, "filter-by-adm-state")
        admin_state = ET.SubElement(filter_by_adm_state, "admin-state")
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_opr_state_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_opr_state = ET.SubElement(filter_type, "filter-by-opr-state")
        oper_state = ET.SubElement(filter_by_opr_state, "oper-state")
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_bfd_state_bfd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_bfd_state = ET.SubElement(filter_type, "filter-by-bfd-state")
        bfd_state = ET.SubElement(filter_by_bfd_state, "bfd-state")
        bfd_state.text = kwargs.pop('bfd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        id = ET.SubElement(tunnel, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        mode = ET.SubElement(tunnel, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        src_ip = ET.SubElement(tunnel, "src-ip")
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        dest_ip = ET.SubElement(tunnel, "dest-ip")
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        vrf = ET.SubElement(tunnel, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_config_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        config_src = ET.SubElement(tunnel, "config-src")
        config_src.text = kwargs.pop('config_src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        admin_state = ET.SubElement(tunnel, "admin-state")
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        oper_state = ET.SubElement(tunnel, "oper-state")
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_bfd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        bfd_state = ET.SubElement(tunnel, "bfd-state")
        bfd_state.text = kwargs.pop('bfd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_has_conflicts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        has_conflicts = ET.SubElement(tunnel, "has-conflicts")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_next_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        next_page_cursor = ET.SubElement(output, "next-page-cursor")
        next_page_cursor.text = kwargs.pop('next_page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        page_cursor = ET.SubElement(input, "page-cursor")
        page_cursor.text = kwargs.pop('page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_filter_type_filter_by_id_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_id = ET.SubElement(filter_type, "filter-by-id")
        id = ET.SubElement(filter_by_id, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_filter_type_filter_by_mode_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_mode = ET.SubElement(filter_type, "filter-by-mode")
        mode = ET.SubElement(filter_by_mode, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_filter_type_filter_by_gateway_gw_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_gateway = ET.SubElement(filter_type, "filter-by-gateway")
        gw_name = ET.SubElement(filter_by_gateway, "gw-name")
        gw_name.text = kwargs.pop('gw_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        id = ET.SubElement(tunnel_stat, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_tx_frames(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        tx_frames = ET.SubElement(tunnel_stat, "tx-frames")
        tx_frames.text = kwargs.pop('tx_frames')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_tx_bytes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        tx_bytes = ET.SubElement(tunnel_stat, "tx-bytes")
        tx_bytes.text = kwargs.pop('tx_bytes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_rx_frames(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        rx_frames = ET.SubElement(tunnel_stat, "rx-frames")
        rx_frames.text = kwargs.pop('rx_frames')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_rx_bytes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        rx_bytes = ET.SubElement(tunnel_stat, "rx-bytes")
        rx_bytes.text = kwargs.pop('rx_bytes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_next_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        next_page_cursor = ET.SubElement(output, "next-page-cursor")
        next_page_cursor.text = kwargs.pop('next_page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        page_cursor = ET.SubElement(input, "page-cursor")
        page_cursor.text = kwargs.pop('page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_id_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_id = ET.SubElement(filter_type, "filter-by-id")
        id = ET.SubElement(filter_by_id, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_mode_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_mode = ET.SubElement(filter_type, "filter-by-mode")
        mode = ET.SubElement(filter_by_mode, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_gateway_gw_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_gateway = ET.SubElement(filter_type, "filter-by-gateway")
        gw_name = ET.SubElement(filter_by_gateway, "gw-name")
        gw_name.text = kwargs.pop('gw_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_sip_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_sip = ET.SubElement(filter_type, "filter-by-sip")
        src_ip = ET.SubElement(filter_by_sip, "src-ip")
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_dip_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_dip = ET.SubElement(filter_type, "filter-by-dip")
        dest_ip = ET.SubElement(filter_by_dip, "dest-ip")
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_cfg_src_config_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_cfg_src = ET.SubElement(filter_type, "filter-by-cfg-src")
        config_src = ET.SubElement(filter_by_cfg_src, "config-src")
        config_src.text = kwargs.pop('config_src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_site_site_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_site = ET.SubElement(filter_type, "filter-by-site")
        site_name = ET.SubElement(filter_by_site, "site-name")
        site_name.text = kwargs.pop('site_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_adm_state_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_adm_state = ET.SubElement(filter_type, "filter-by-adm-state")
        admin_state = ET.SubElement(filter_by_adm_state, "admin-state")
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_opr_state_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_opr_state = ET.SubElement(filter_type, "filter-by-opr-state")
        oper_state = ET.SubElement(filter_by_opr_state, "oper-state")
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_input_filter_type_filter_by_bfd_state_bfd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        input = ET.SubElement(get_tunnel_info, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_bfd_state = ET.SubElement(filter_type, "filter-by-bfd-state")
        bfd_state = ET.SubElement(filter_by_bfd_state, "bfd-state")
        bfd_state.text = kwargs.pop('bfd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        id = ET.SubElement(tunnel, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        mode = ET.SubElement(tunnel, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_src_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        src_ip = ET.SubElement(tunnel, "src-ip")
        src_ip.text = kwargs.pop('src_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_dest_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        dest_ip = ET.SubElement(tunnel, "dest-ip")
        dest_ip.text = kwargs.pop('dest_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        vrf = ET.SubElement(tunnel, "vrf")
        vrf.text = kwargs.pop('vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_config_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        config_src = ET.SubElement(tunnel, "config-src")
        config_src.text = kwargs.pop('config_src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        admin_state = ET.SubElement(tunnel, "admin-state")
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        oper_state = ET.SubElement(tunnel, "oper-state")
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_bfd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        bfd_state = ET.SubElement(tunnel, "bfd-state")
        bfd_state.text = kwargs.pop('bfd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_tunnel_has_conflicts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        tunnel = ET.SubElement(output, "tunnel")
        has_conflicts = ET.SubElement(tunnel, "has-conflicts")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_info_output_next_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_info = ET.Element("get_tunnel_info")
        config = get_tunnel_info
        output = ET.SubElement(get_tunnel_info, "output")
        next_page_cursor = ET.SubElement(output, "next-page-cursor")
        next_page_cursor.text = kwargs.pop('next_page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        page_cursor = ET.SubElement(input, "page-cursor")
        page_cursor.text = kwargs.pop('page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_filter_type_filter_by_id_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_id = ET.SubElement(filter_type, "filter-by-id")
        id = ET.SubElement(filter_by_id, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_filter_type_filter_by_mode_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_mode = ET.SubElement(filter_type, "filter-by-mode")
        mode = ET.SubElement(filter_by_mode, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_input_filter_type_filter_by_gateway_gw_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        input = ET.SubElement(get_tunnel_statistics, "input")
        filter_type = ET.SubElement(input, "filter-type")
        filter_by_gateway = ET.SubElement(filter_type, "filter-by-gateway")
        gw_name = ET.SubElement(filter_by_gateway, "gw-name")
        gw_name.text = kwargs.pop('gw_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        id = ET.SubElement(tunnel_stat, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_tx_frames(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        tx_frames = ET.SubElement(tunnel_stat, "tx-frames")
        tx_frames.text = kwargs.pop('tx_frames')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_tx_bytes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        tx_bytes = ET.SubElement(tunnel_stat, "tx-bytes")
        tx_bytes.text = kwargs.pop('tx_bytes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_rx_frames(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        rx_frames = ET.SubElement(tunnel_stat, "rx-frames")
        rx_frames.text = kwargs.pop('rx_frames')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_tunnel_stat_rx_bytes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        tunnel_stat = ET.SubElement(output, "tunnel-stat")
        rx_bytes = ET.SubElement(tunnel_stat, "rx-bytes")
        rx_bytes.text = kwargs.pop('rx_bytes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_tunnel_statistics_output_next_page_cursor(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_tunnel_statistics = ET.Element("get_tunnel_statistics")
        config = get_tunnel_statistics
        output = ET.SubElement(get_tunnel_statistics, "output")
        next_page_cursor = ET.SubElement(output, "next-page-cursor")
        next_page_cursor.text = kwargs.pop('next_page_cursor')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        