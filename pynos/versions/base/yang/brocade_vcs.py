#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_vcs(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def vcsmode_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsmode = ET.SubElement(config, "vcsmode", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        vcs_mode = ET.SubElement(vcsmode, "vcs-mode")
        vcs_mode.text = kwargs.pop('vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcsmode_vcs_cluster_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsmode = ET.SubElement(config, "vcsmode", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        vcs_cluster_mode = ET.SubElement(vcsmode, "vcs-cluster-mode")
        vcs_cluster_mode.text = kwargs.pop('vcs_cluster_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def local_node_swbd_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        local_node = ET.SubElement(config, "local-node", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        swbd_number = ET.SubElement(local_node, "swbd-number")
        swbd_number.text = kwargs.pop('swbd_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_output_last_config_update_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time = ET.Element("get_last_config_update_time")
        config = get_last_config_update_time
        output = ET.SubElement(get_last_config_update_time, "output")
        last_config_update_time = ET.SubElement(output, "last-config-update-time")
        last_config_update_time.text = kwargs.pop('last_config_update_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_principal_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        principal_switch_wwn = ET.SubElement(output, "principal-switch-wwn")
        principal_switch_wwn.text = kwargs.pop('principal_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_co_ordinator_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        co_ordinator_wwn = ET.SubElement(output, "co-ordinator-wwn")
        co_ordinator_wwn.text = kwargs.pop('co_ordinator_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_cluster_type_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_cluster_type_info = ET.SubElement(output, "vcs-cluster-type-info")
        vcs_cluster_type_info.text = kwargs.pop('vcs_cluster_type_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_guid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_guid = ET.SubElement(output, "vcs-guid")
        vcs_guid.text = kwargs.pop('vcs_guid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_virtual_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        virtual_ip_address = ET.SubElement(output, "virtual-ip-address")
        virtual_ip_address.text = kwargs.pop('virtual_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_total_nodes_in_cluster(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        total_nodes_in_cluster = ET.SubElement(output, "total-nodes-in-cluster")
        total_nodes_in_cluster.text = kwargs.pop('total_nodes_in_cluster')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_nodes_disconnected_from_cluster(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        nodes_disconnected_from_cluster = ET.SubElement(output, "nodes-disconnected-from-cluster")
        nodes_disconnected_from_cluster.text = kwargs.pop('nodes_disconnected_from_cluster')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_cluster_generic_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        cluster_generic_status = ET.SubElement(output, "cluster-generic-status")
        cluster_generic_status.text = kwargs.pop('cluster_generic_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_cluster_specific_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        cluster_specific_status = ET.SubElement(output, "cluster-specific-status")
        cluster_specific_status.text = kwargs.pop('cluster_specific_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_num = ET.SubElement(vcs_node_info, "node-num")
        node_num.text = kwargs.pop('node_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_serial_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_serial_num = ET.SubElement(vcs_node_info, "node-serial-num")
        node_serial_num.text = kwargs.pop('node_serial_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_condition(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_condition = ET.SubElement(vcs_node_info, "node-condition")
        node_condition.text = kwargs.pop('node_condition')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_status = ET.SubElement(vcs_node_info, "node-status")
        node_status.text = kwargs.pop('node_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_hw_sync_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_hw_sync_state = ET.SubElement(vcs_node_info, "node-hw-sync-state")
        node_hw_sync_state.text = kwargs.pop('node_hw_sync_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_vcs_mode = ET.SubElement(vcs_node_info, "node-vcs-mode")
        node_vcs_mode.text = kwargs.pop('node_vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_vcs_id = ET.SubElement(vcs_node_info, "node-vcs-id")
        node_vcs_id.text = kwargs.pop('node_vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_rbridge_id = ET.SubElement(vcs_node_info, "node-rbridge-id")
        node_rbridge_id.text = kwargs.pop('node_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_is_principal(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_is_principal = ET.SubElement(vcs_node_info, "node-is-principal")
        node_is_principal.text = kwargs.pop('node_is_principal')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_co_ordinator(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        co_ordinator = ET.SubElement(vcs_node_info, "co-ordinator")
        co_ordinator.text = kwargs.pop('co_ordinator')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switch_mac = ET.SubElement(vcs_node_info, "node-switch-mac")
        node_switch_mac.text = kwargs.pop('node_switch_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switch_wwn = ET.SubElement(vcs_node_info, "node-switch-wwn")
        node_switch_wwn.text = kwargs.pop('node_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_switch_fcf_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        switch_fcf_mac = ET.SubElement(vcs_node_info, "switch-fcf-mac")
        switch_fcf_mac.text = kwargs.pop('switch_fcf_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_internal_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_internal_ip_address = ET.SubElement(vcs_node_info, "node-internal-ip-address")
        node_internal_ip_address.text = kwargs.pop('node_internal_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_public_ip_addresses_node_public_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_public_ip_addresses = ET.SubElement(vcs_node_info, "node-public-ip-addresses")
        node_public_ip_address = ET.SubElement(node_public_ip_addresses, "node-public-ip-address")
        node_public_ip_address.text = kwargs.pop('node_public_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_public_ipv6_addresses_node_public_ipv6_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_public_ipv6_addresses = ET.SubElement(vcs_node_info, "node-public-ipv6-addresses")
        node_public_ipv6_address = ET.SubElement(node_public_ipv6_addresses, "node-public-ipv6-address")
        node_public_ipv6_address.text = kwargs.pop('node_public_ipv6_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_firmware_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        firmware_version = ET.SubElement(vcs_node_info, "firmware-version")
        firmware_version.text = kwargs.pop('firmware_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_swbd_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_swbd_number = ET.SubElement(vcs_node_info, "node-swbd-number")
        node_swbd_number.text = kwargs.pop('node_swbd_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switchname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switchname = ET.SubElement(vcs_node_info, "node-switchname")
        node_switchname.text = kwargs.pop('node_switchname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switchtype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switchtype = ET.SubElement(vcs_node_info, "node-switchtype")
        node_switchtype.text = kwargs.pop('node_switchtype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_state = ET.SubElement(vcs_node_info, "node-state")
        node_state.text = kwargs.pop('node_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_fabric_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_fabric_state = ET.SubElement(vcs_node_info, "node-fabric-state")
        node_fabric_state.text = kwargs.pop('node_fabric_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_principal_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        principal_switch_wwn = ET.SubElement(vcs_details, "principal-switch-wwn")
        principal_switch_wwn.text = kwargs.pop('principal_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_co_ordinator_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        co_ordinator_wwn = ET.SubElement(vcs_details, "co-ordinator-wwn")
        co_ordinator_wwn.text = kwargs.pop('co_ordinator_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_local_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        local_switch_wwn = ET.SubElement(vcs_details, "local-switch-wwn")
        local_switch_wwn.text = kwargs.pop('local_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        node_vcs_mode = ET.SubElement(vcs_details, "node-vcs-mode")
        node_vcs_mode.text = kwargs.pop('node_vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        node_vcs_type = ET.SubElement(vcs_details, "node-vcs-type")
        node_vcs_type.text = kwargs.pop('node_vcs_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        node_vcs_id = ET.SubElement(vcs_details, "node-vcs-id")
        node_vcs_id.text = kwargs.pop('node_vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_rbridge_context_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs_rbridge_context = ET.Element("vcs_rbridge_context")
        config = vcs_rbridge_context
        input = ET.SubElement(vcs_rbridge_context, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_input_xpath_strings_xpath_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        input = ET.SubElement(get_last_config_update_time_for_xpaths, "input")
        xpath_strings = ET.SubElement(input, "xpath-strings")
        xpath_string = ET.SubElement(xpath_strings, "xpath-string")
        xpath_string.text = kwargs.pop('xpath_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_output_last_config_update_time_for_xpaths_xpath_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        output = ET.SubElement(get_last_config_update_time_for_xpaths, "output")
        last_config_update_time_for_xpaths = ET.SubElement(output, "last-config-update-time-for-xpaths")
        xpath_string = ET.SubElement(last_config_update_time_for_xpaths, "xpath-string")
        xpath_string.text = kwargs.pop('xpath_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_output_last_config_update_time_for_xpaths_last_config_update_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        output = ET.SubElement(get_last_config_update_time_for_xpaths, "output")
        last_config_update_time_for_xpaths = ET.SubElement(output, "last-config-update-time-for-xpaths")
        xpath_string_key = ET.SubElement(last_config_update_time_for_xpaths, "xpath-string")
        xpath_string_key.text = kwargs.pop('xpath_string')
        last_config_update_time = ET.SubElement(last_config_update_time_for_xpaths, "last-config-update-time")
        last_config_update_time.text = kwargs.pop('last_config_update_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ip_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual = ET.SubElement(vcs, "virtual")
        ip = ET.SubElement(virtual, "ip")
        address = ET.SubElement(ip, "address")
        address = ET.SubElement(address, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ip_address_inband_interface_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual = ET.SubElement(vcs, "virtual")
        ip = ET.SubElement(virtual, "ip")
        address = ET.SubElement(ip, "address")
        address_key = ET.SubElement(address, "address")
        address_key.text = kwargs.pop('address')
        inband = ET.SubElement(address, "inband")
        interface = ET.SubElement(inband, "interface")
        ve = ET.SubElement(interface, "ve")
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ipv6_address_ipv6address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual = ET.SubElement(vcs, "virtual")
        ipv6 = ET.SubElement(virtual, "ipv6")
        address = ET.SubElement(ipv6, "address")
        ipv6address = ET.SubElement(address, "ipv6address")
        ipv6address.text = kwargs.pop('ipv6address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_fabric_vfab_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual_fabric = ET.SubElement(vcs, "virtual-fabric")
        vfab_enable = ET.SubElement(virtual_fabric, "vfab-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcsmode_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsmode = ET.SubElement(config, "vcsmode", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        vcs_mode = ET.SubElement(vcsmode, "vcs-mode")
        vcs_mode.text = kwargs.pop('vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcsmode_vcs_cluster_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcsmode = ET.SubElement(config, "vcsmode", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        vcs_cluster_mode = ET.SubElement(vcsmode, "vcs-cluster-mode")
        vcs_cluster_mode.text = kwargs.pop('vcs_cluster_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def local_node_swbd_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        local_node = ET.SubElement(config, "local-node", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        swbd_number = ET.SubElement(local_node, "swbd-number")
        swbd_number.text = kwargs.pop('swbd_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_output_last_config_update_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time = ET.Element("get_last_config_update_time")
        config = get_last_config_update_time
        output = ET.SubElement(get_last_config_update_time, "output")
        last_config_update_time = ET.SubElement(output, "last-config-update-time")
        last_config_update_time.text = kwargs.pop('last_config_update_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_principal_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        principal_switch_wwn = ET.SubElement(output, "principal-switch-wwn")
        principal_switch_wwn.text = kwargs.pop('principal_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_co_ordinator_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        co_ordinator_wwn = ET.SubElement(output, "co-ordinator-wwn")
        co_ordinator_wwn.text = kwargs.pop('co_ordinator_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_cluster_type_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_cluster_type_info = ET.SubElement(output, "vcs-cluster-type-info")
        vcs_cluster_type_info.text = kwargs.pop('vcs_cluster_type_info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_guid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_guid = ET.SubElement(output, "vcs-guid")
        vcs_guid.text = kwargs.pop('vcs_guid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_virtual_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        virtual_ip_address = ET.SubElement(output, "virtual-ip-address")
        virtual_ip_address.text = kwargs.pop('virtual_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_total_nodes_in_cluster(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        total_nodes_in_cluster = ET.SubElement(output, "total-nodes-in-cluster")
        total_nodes_in_cluster.text = kwargs.pop('total_nodes_in_cluster')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_nodes_disconnected_from_cluster(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        nodes_disconnected_from_cluster = ET.SubElement(output, "nodes-disconnected-from-cluster")
        nodes_disconnected_from_cluster.text = kwargs.pop('nodes_disconnected_from_cluster')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_cluster_generic_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        cluster_generic_status = ET.SubElement(output, "cluster-generic-status")
        cluster_generic_status.text = kwargs.pop('cluster_generic_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_cluster_specific_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        cluster_specific_status = ET.SubElement(output, "cluster-specific-status")
        cluster_specific_status.text = kwargs.pop('cluster_specific_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_num = ET.SubElement(vcs_node_info, "node-num")
        node_num.text = kwargs.pop('node_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_serial_num(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_serial_num = ET.SubElement(vcs_node_info, "node-serial-num")
        node_serial_num.text = kwargs.pop('node_serial_num')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_condition(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_condition = ET.SubElement(vcs_node_info, "node-condition")
        node_condition.text = kwargs.pop('node_condition')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_status = ET.SubElement(vcs_node_info, "node-status")
        node_status.text = kwargs.pop('node_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_hw_sync_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_hw_sync_state = ET.SubElement(vcs_node_info, "node-hw-sync-state")
        node_hw_sync_state.text = kwargs.pop('node_hw_sync_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_vcs_mode = ET.SubElement(vcs_node_info, "node-vcs-mode")
        node_vcs_mode.text = kwargs.pop('node_vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_vcs_id = ET.SubElement(vcs_node_info, "node-vcs-id")
        node_vcs_id.text = kwargs.pop('node_vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_rbridge_id = ET.SubElement(vcs_node_info, "node-rbridge-id")
        node_rbridge_id.text = kwargs.pop('node_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_is_principal(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_is_principal = ET.SubElement(vcs_node_info, "node-is-principal")
        node_is_principal.text = kwargs.pop('node_is_principal')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_co_ordinator(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        co_ordinator = ET.SubElement(vcs_node_info, "co-ordinator")
        co_ordinator.text = kwargs.pop('co_ordinator')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switch_mac = ET.SubElement(vcs_node_info, "node-switch-mac")
        node_switch_mac.text = kwargs.pop('node_switch_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switch_wwn = ET.SubElement(vcs_node_info, "node-switch-wwn")
        node_switch_wwn.text = kwargs.pop('node_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_switch_fcf_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        switch_fcf_mac = ET.SubElement(vcs_node_info, "switch-fcf-mac")
        switch_fcf_mac.text = kwargs.pop('switch_fcf_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_internal_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_internal_ip_address = ET.SubElement(vcs_node_info, "node-internal-ip-address")
        node_internal_ip_address.text = kwargs.pop('node_internal_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_public_ip_addresses_node_public_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_public_ip_addresses = ET.SubElement(vcs_node_info, "node-public-ip-addresses")
        node_public_ip_address = ET.SubElement(node_public_ip_addresses, "node-public-ip-address")
        node_public_ip_address.text = kwargs.pop('node_public_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_public_ipv6_addresses_node_public_ipv6_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_public_ipv6_addresses = ET.SubElement(vcs_node_info, "node-public-ipv6-addresses")
        node_public_ipv6_address = ET.SubElement(node_public_ipv6_addresses, "node-public-ipv6-address")
        node_public_ipv6_address.text = kwargs.pop('node_public_ipv6_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_firmware_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        firmware_version = ET.SubElement(vcs_node_info, "firmware-version")
        firmware_version.text = kwargs.pop('firmware_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_swbd_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_swbd_number = ET.SubElement(vcs_node_info, "node-swbd-number")
        node_swbd_number.text = kwargs.pop('node_swbd_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switchname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switchname = ET.SubElement(vcs_node_info, "node-switchname")
        node_switchname.text = kwargs.pop('node_switchname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_switchtype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_switchtype = ET.SubElement(vcs_node_info, "node-switchtype")
        node_switchtype.text = kwargs.pop('node_switchtype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_state = ET.SubElement(vcs_node_info, "node-state")
        node_state.text = kwargs.pop('node_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_vcs_output_vcs_nodes_vcs_node_info_node_fabric_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_vcs = ET.Element("show_vcs")
        config = show_vcs
        output = ET.SubElement(show_vcs, "output")
        vcs_nodes = ET.SubElement(output, "vcs-nodes")
        vcs_node_info = ET.SubElement(vcs_nodes, "vcs-node-info")
        node_fabric_state = ET.SubElement(vcs_node_info, "node-fabric-state")
        node_fabric_state.text = kwargs.pop('node_fabric_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_principal_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        principal_switch_wwn = ET.SubElement(vcs_details, "principal-switch-wwn")
        principal_switch_wwn.text = kwargs.pop('principal_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_co_ordinator_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        co_ordinator_wwn = ET.SubElement(vcs_details, "co-ordinator-wwn")
        co_ordinator_wwn.text = kwargs.pop('co_ordinator_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_local_switch_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        local_switch_wwn = ET.SubElement(vcs_details, "local-switch-wwn")
        local_switch_wwn.text = kwargs.pop('local_switch_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        node_vcs_mode = ET.SubElement(vcs_details, "node-vcs-mode")
        node_vcs_mode.text = kwargs.pop('node_vcs_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        node_vcs_type = ET.SubElement(vcs_details, "node-vcs-type")
        node_vcs_type.text = kwargs.pop('node_vcs_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_vcs_details_output_vcs_details_node_vcs_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_vcs_details = ET.Element("get_vcs_details")
        config = get_vcs_details
        output = ET.SubElement(get_vcs_details, "output")
        vcs_details = ET.SubElement(output, "vcs-details")
        node_vcs_id = ET.SubElement(vcs_details, "node-vcs-id")
        node_vcs_id.text = kwargs.pop('node_vcs_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_rbridge_context_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs_rbridge_context = ET.Element("vcs_rbridge_context")
        config = vcs_rbridge_context
        input = ET.SubElement(vcs_rbridge_context, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_input_xpath_strings_xpath_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        input = ET.SubElement(get_last_config_update_time_for_xpaths, "input")
        xpath_strings = ET.SubElement(input, "xpath-strings")
        xpath_string = ET.SubElement(xpath_strings, "xpath-string")
        xpath_string.text = kwargs.pop('xpath_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_output_last_config_update_time_for_xpaths_xpath_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        output = ET.SubElement(get_last_config_update_time_for_xpaths, "output")
        last_config_update_time_for_xpaths = ET.SubElement(output, "last-config-update-time-for-xpaths")
        xpath_string = ET.SubElement(last_config_update_time_for_xpaths, "xpath-string")
        xpath_string.text = kwargs.pop('xpath_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_last_config_update_time_for_xpaths_output_last_config_update_time_for_xpaths_last_config_update_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_last_config_update_time_for_xpaths = ET.Element("get_last_config_update_time_for_xpaths")
        config = get_last_config_update_time_for_xpaths
        output = ET.SubElement(get_last_config_update_time_for_xpaths, "output")
        last_config_update_time_for_xpaths = ET.SubElement(output, "last-config-update-time-for-xpaths")
        xpath_string_key = ET.SubElement(last_config_update_time_for_xpaths, "xpath-string")
        xpath_string_key.text = kwargs.pop('xpath_string')
        last_config_update_time = ET.SubElement(last_config_update_time_for_xpaths, "last-config-update-time")
        last_config_update_time.text = kwargs.pop('last_config_update_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ip_address_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual = ET.SubElement(vcs, "virtual")
        ip = ET.SubElement(virtual, "ip")
        address = ET.SubElement(ip, "address")
        address = ET.SubElement(address, "address")
        address.text = kwargs.pop('address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ip_address_inband_interface_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual = ET.SubElement(vcs, "virtual")
        ip = ET.SubElement(virtual, "ip")
        address = ET.SubElement(ip, "address")
        address_key = ET.SubElement(address, "address")
        address_key.text = kwargs.pop('address')
        inband = ET.SubElement(address, "inband")
        interface = ET.SubElement(inband, "interface")
        ve = ET.SubElement(interface, "ve")
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_ipv6_address_ipv6address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual = ET.SubElement(vcs, "virtual")
        ipv6 = ET.SubElement(virtual, "ipv6")
        address = ET.SubElement(ipv6, "address")
        ipv6address = ET.SubElement(address, "ipv6address")
        ipv6address.text = kwargs.pop('ipv6address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def vcs_virtual_fabric_vfab_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        vcs = ET.SubElement(config, "vcs", xmlns="urn:brocade.com:mgmt:brocade-vcs")
        virtual_fabric = ET.SubElement(vcs, "virtual-fabric")
        vfab_enable = ET.SubElement(virtual_fabric, "vfab-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        