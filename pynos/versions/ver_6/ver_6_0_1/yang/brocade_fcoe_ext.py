#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fcoe_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def fcoe_get_interface_input_fcoe_intf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        input = ET.SubElement(fcoe_get_interface, "input")
        fcoe_intf_name = ET.SubElement(input, "fcoe-intf-name")
        fcoe_intf_name.text = kwargs.pop('fcoe_intf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        input = ET.SubElement(fcoe_get_interface, "input")
        fcoe_intf_rbridge_id = ET.SubElement(input, "fcoe-intf-rbridge-id")
        fcoe_intf_rbridge_id.text = kwargs.pop('fcoe_intf_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_include_stats(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        input = ET.SubElement(fcoe_get_interface, "input")
        fcoe_intf_include_stats = ET.SubElement(input, "fcoe-intf-include-stats")
        fcoe_intf_include_stats.text = kwargs.pop('fcoe_intf_include_stats')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_fcoe_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id.text = kwargs.pop('fcoe_intf_fcoe_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_port_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-type")
        fcoe_intf_port_type.text = kwargs.pop('fcoe_intf_port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_config_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_config_port_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-config-port-type")
        fcoe_intf_config_port_type.text = kwargs.pop('fcoe_intf_config_port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_port_state = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-state")
        fcoe_intf_port_state.text = kwargs.pop('fcoe_intf_port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_fabric_map_name = ET.SubElement(fcoe_intf_list, "fcoe-intf-fabric-map-name")
        fcoe_intf_fabric_map_name.text = kwargs.pop('fcoe_intf_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_eth_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_eth_port_id = ET.SubElement(fcoe_intf_list, "fcoe-intf-eth-port-id")
        fcoe_intf_eth_port_id.text = kwargs.pop('fcoe_intf_eth_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        interface_type = ET.SubElement(fcoe_intf_list, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        interface_name = ET.SubElement(fcoe_intf_list, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_admin_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_admin_status = ET.SubElement(fcoe_intf_list, "fcoe-intf-admin-status")
        fcoe_intf_admin_status.text = kwargs.pop('fcoe_intf_admin_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_peer_fcf_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_peer_fcf_mac = ET.SubElement(fcoe_intf_list, "fcoe-intf-peer-fcf-mac")
        fcoe_intf_peer_fcf_mac.text = kwargs.pop('fcoe_intf_peer_fcf_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_device_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_device_count = ET.SubElement(fcoe_intf_list, "fcoe-intf-device-count")
        fcoe_intf_device_count.text = kwargs.pop('fcoe_intf_device_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_ifindex = ET.SubElement(fcoe_intf_list, "fcoe-intf-ifindex")
        fcoe_intf_ifindex.text = kwargs.pop('fcoe_intf_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_wwn = ET.SubElement(fcoe_intf_list, "fcoe-intf-wwn")
        fcoe_intf_wwn.text = kwargs.pop('fcoe_intf_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_enode_bind_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_enode_bind_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-enode-bind-type")
        fcoe_intf_enode_bind_type.text = kwargs.pop('fcoe_intf_enode_bind_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_bind_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_port_bind_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-bind-type")
        fcoe_intf_port_bind_type.text = kwargs.pop('fcoe_intf_port_bind_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_enode_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_enode_mac_address = ET.SubElement(fcoe_intf_list, "fcoe-intf-enode-mac-address")
        fcoe_intf_enode_mac_address.text = kwargs.pop('fcoe_intf_enode_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_vlan_disc_req(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_vlan_disc_req = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-vlan-disc-req")
        fcoe_intf_rx_vlan_disc_req.text = kwargs.pop('fcoe_intf_rx_vlan_disc_req')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_disc_solicitations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_disc_solicitations = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-disc-solicitations")
        fcoe_intf_rx_disc_solicitations.text = kwargs.pop('fcoe_intf_rx_disc_solicitations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_flogi(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_flogi = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-flogi")
        fcoe_intf_rx_flogi.text = kwargs.pop('fcoe_intf_rx_flogi')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_fdiscs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_fdiscs = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-fdiscs")
        fcoe_intf_rx_fdiscs.text = kwargs.pop('fcoe_intf_rx_fdiscs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_logo(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_logo = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-logo")
        fcoe_intf_rx_logo.text = kwargs.pop('fcoe_intf_rx_logo')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_errors = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-errors")
        fcoe_intf_rx_errors.text = kwargs.pop('fcoe_intf_rx_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_vlan_disc_resp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_vlan_disc_resp = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-vlan-disc-resp")
        fcoe_intf_tx_vlan_disc_resp.text = kwargs.pop('fcoe_intf_tx_vlan_disc_resp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_disc_sol_adv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_disc_sol_adv = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-disc-sol-adv")
        fcoe_intf_tx_disc_sol_adv.text = kwargs.pop('fcoe_intf_tx_disc_sol_adv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_disc_unsol_adv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_disc_unsol_adv = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-disc-unsol-adv")
        fcoe_intf_tx_disc_unsol_adv.text = kwargs.pop('fcoe_intf_tx_disc_unsol_adv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_enode_ka(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_enode_ka = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-enode-ka")
        fcoe_intf_rx_enode_ka.text = kwargs.pop('fcoe_intf_rx_enode_ka')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_vnport_ka(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_vnport_ka = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-vnport-ka")
        fcoe_intf_rx_vnport_ka.text = kwargs.pop('fcoe_intf_rx_vnport_ka')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_accepts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_accepts = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-accepts")
        fcoe_intf_tx_accepts.text = kwargs.pop('fcoe_intf_tx_accepts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_ls_rjt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_ls_rjt = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-ls-rjt")
        fcoe_intf_tx_ls_rjt.text = kwargs.pop('fcoe_intf_tx_ls_rjt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_time_since_last_change(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_time_since_last_change = ET.SubElement(fcoe_intf_list, "fcoe-intf-time-since-last-change")
        fcoe_intf_time_since_last_change.text = kwargs.pop('fcoe_intf_time_since_last_change')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_last_counters_cleared(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_last_counters_cleared = ET.SubElement(fcoe_intf_list, "fcoe-intf-last-counters-cleared")
        fcoe_intf_last_counters_cleared.text = kwargs.pop('fcoe_intf_last_counters_cleared')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_cvls(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_cvls = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-cvls")
        fcoe_intf_tx_cvls.text = kwargs.pop('fcoe_intf_tx_cvls')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_total_interfaces(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_total_interfaces = ET.SubElement(output, "fcoe-intf-total-interfaces")
        fcoe_intf_total_interfaces.text = kwargs.pop('fcoe_intf_total_interfaces')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_interface = ET.SubElement(input, "fcoe-login-interface")
        fcoe_login_interface.text = kwargs.pop('fcoe_login_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_vfid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_vfid = ET.SubElement(input, "fcoe-login-vfid")
        fcoe_login_vfid.text = kwargs.pop('fcoe_login_vfid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_vlan = ET.SubElement(input, "fcoe-login-vlan")
        fcoe_login_vlan.text = kwargs.pop('fcoe_login_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_rbridge_id = ET.SubElement(input, "fcoe-login-rbridge-id")
        fcoe_login_rbridge_id.text = kwargs.pop('fcoe_login_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_session_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac.text = kwargs.pop('fcoe_login_session_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_fcoe_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_fcoe_interface_name = ET.SubElement(fcoe_login_list, "fcoe-login-fcoe-interface-name")
        fcoe_login_fcoe_interface_name.text = kwargs.pop('fcoe_login_fcoe_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_interface_name = ET.SubElement(fcoe_login_list, "fcoe-login-interface-name")
        fcoe_login_interface_name.text = kwargs.pop('fcoe_login_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        interface_type = ET.SubElement(fcoe_login_list, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        interface_name = ET.SubElement(fcoe_login_list, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_device_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_device_wwn = ET.SubElement(fcoe_login_list, "fcoe-login-device-wwn")
        fcoe_login_device_wwn.text = kwargs.pop('fcoe_login_device_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_device_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_device_mac = ET.SubElement(fcoe_login_list, "fcoe-login-device-mac")
        fcoe_login_device_mac.text = kwargs.pop('fcoe_login_device_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_direct_attached(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_direct_attached = ET.SubElement(fcoe_login_list, "fcoe-login-direct-attached")
        fcoe_login_direct_attached.text = kwargs.pop('fcoe_login_direct_attached')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_connected_peer_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_connected_peer_type = ET.SubElement(fcoe_login_list, "fcoe-login-connected-peer-type")
        fcoe_login_connected_peer_type.text = kwargs.pop('fcoe_login_connected_peer_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_total_logins(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_total_logins = ET.SubElement(output, "fcoe-login-total-logins")
        fcoe_login_total_logins.text = kwargs.pop('fcoe_login_total_logins')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        input = ET.SubElement(fcoe_get_interface, "input")
        fcoe_intf_name = ET.SubElement(input, "fcoe-intf-name")
        fcoe_intf_name.text = kwargs.pop('fcoe_intf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        input = ET.SubElement(fcoe_get_interface, "input")
        fcoe_intf_rbridge_id = ET.SubElement(input, "fcoe-intf-rbridge-id")
        fcoe_intf_rbridge_id.text = kwargs.pop('fcoe_intf_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_input_fcoe_intf_include_stats(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        input = ET.SubElement(fcoe_get_interface, "input")
        fcoe_intf_include_stats = ET.SubElement(input, "fcoe-intf-include-stats")
        fcoe_intf_include_stats.text = kwargs.pop('fcoe_intf_include_stats')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_fcoe_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id.text = kwargs.pop('fcoe_intf_fcoe_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_port_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-type")
        fcoe_intf_port_type.text = kwargs.pop('fcoe_intf_port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_config_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_config_port_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-config-port-type")
        fcoe_intf_config_port_type.text = kwargs.pop('fcoe_intf_config_port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_port_state = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-state")
        fcoe_intf_port_state.text = kwargs.pop('fcoe_intf_port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_fabric_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_fabric_map_name = ET.SubElement(fcoe_intf_list, "fcoe-intf-fabric-map-name")
        fcoe_intf_fabric_map_name.text = kwargs.pop('fcoe_intf_fabric_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_eth_port_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_eth_port_id = ET.SubElement(fcoe_intf_list, "fcoe-intf-eth-port-id")
        fcoe_intf_eth_port_id.text = kwargs.pop('fcoe_intf_eth_port_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        interface_type = ET.SubElement(fcoe_intf_list, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        interface_name = ET.SubElement(fcoe_intf_list, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_admin_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_admin_status = ET.SubElement(fcoe_intf_list, "fcoe-intf-admin-status")
        fcoe_intf_admin_status.text = kwargs.pop('fcoe_intf_admin_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_peer_fcf_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_peer_fcf_mac = ET.SubElement(fcoe_intf_list, "fcoe-intf-peer-fcf-mac")
        fcoe_intf_peer_fcf_mac.text = kwargs.pop('fcoe_intf_peer_fcf_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_device_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_device_count = ET.SubElement(fcoe_intf_list, "fcoe-intf-device-count")
        fcoe_intf_device_count.text = kwargs.pop('fcoe_intf_device_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_ifindex(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_ifindex = ET.SubElement(fcoe_intf_list, "fcoe-intf-ifindex")
        fcoe_intf_ifindex.text = kwargs.pop('fcoe_intf_ifindex')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_wwn = ET.SubElement(fcoe_intf_list, "fcoe-intf-wwn")
        fcoe_intf_wwn.text = kwargs.pop('fcoe_intf_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_enode_bind_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_enode_bind_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-enode-bind-type")
        fcoe_intf_enode_bind_type.text = kwargs.pop('fcoe_intf_enode_bind_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_port_bind_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_port_bind_type = ET.SubElement(fcoe_intf_list, "fcoe-intf-port-bind-type")
        fcoe_intf_port_bind_type.text = kwargs.pop('fcoe_intf_port_bind_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_enode_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_enode_mac_address = ET.SubElement(fcoe_intf_list, "fcoe-intf-enode-mac-address")
        fcoe_intf_enode_mac_address.text = kwargs.pop('fcoe_intf_enode_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_vlan_disc_req(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_vlan_disc_req = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-vlan-disc-req")
        fcoe_intf_rx_vlan_disc_req.text = kwargs.pop('fcoe_intf_rx_vlan_disc_req')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_disc_solicitations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_disc_solicitations = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-disc-solicitations")
        fcoe_intf_rx_disc_solicitations.text = kwargs.pop('fcoe_intf_rx_disc_solicitations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_flogi(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_flogi = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-flogi")
        fcoe_intf_rx_flogi.text = kwargs.pop('fcoe_intf_rx_flogi')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_fdiscs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_fdiscs = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-fdiscs")
        fcoe_intf_rx_fdiscs.text = kwargs.pop('fcoe_intf_rx_fdiscs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_logo(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_logo = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-logo")
        fcoe_intf_rx_logo.text = kwargs.pop('fcoe_intf_rx_logo')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_errors = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-errors")
        fcoe_intf_rx_errors.text = kwargs.pop('fcoe_intf_rx_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_vlan_disc_resp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_vlan_disc_resp = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-vlan-disc-resp")
        fcoe_intf_tx_vlan_disc_resp.text = kwargs.pop('fcoe_intf_tx_vlan_disc_resp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_disc_sol_adv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_disc_sol_adv = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-disc-sol-adv")
        fcoe_intf_tx_disc_sol_adv.text = kwargs.pop('fcoe_intf_tx_disc_sol_adv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_disc_unsol_adv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_disc_unsol_adv = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-disc-unsol-adv")
        fcoe_intf_tx_disc_unsol_adv.text = kwargs.pop('fcoe_intf_tx_disc_unsol_adv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_enode_ka(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_enode_ka = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-enode-ka")
        fcoe_intf_rx_enode_ka.text = kwargs.pop('fcoe_intf_rx_enode_ka')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_rx_vnport_ka(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_rx_vnport_ka = ET.SubElement(fcoe_intf_list, "fcoe-intf-rx-vnport-ka")
        fcoe_intf_rx_vnport_ka.text = kwargs.pop('fcoe_intf_rx_vnport_ka')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_accepts(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_accepts = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-accepts")
        fcoe_intf_tx_accepts.text = kwargs.pop('fcoe_intf_tx_accepts')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_ls_rjt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_ls_rjt = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-ls-rjt")
        fcoe_intf_tx_ls_rjt.text = kwargs.pop('fcoe_intf_tx_ls_rjt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_time_since_last_change(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_time_since_last_change = ET.SubElement(fcoe_intf_list, "fcoe-intf-time-since-last-change")
        fcoe_intf_time_since_last_change.text = kwargs.pop('fcoe_intf_time_since_last_change')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_last_counters_cleared(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_last_counters_cleared = ET.SubElement(fcoe_intf_list, "fcoe-intf-last-counters-cleared")
        fcoe_intf_last_counters_cleared.text = kwargs.pop('fcoe_intf_last_counters_cleared')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_list_fcoe_intf_tx_cvls(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_list = ET.SubElement(output, "fcoe-intf-list")
        fcoe_intf_fcoe_port_id_key = ET.SubElement(fcoe_intf_list, "fcoe-intf-fcoe-port-id")
        fcoe_intf_fcoe_port_id_key.text = kwargs.pop('fcoe_intf_fcoe_port_id')
        fcoe_intf_tx_cvls = ET.SubElement(fcoe_intf_list, "fcoe-intf-tx-cvls")
        fcoe_intf_tx_cvls.text = kwargs.pop('fcoe_intf_tx_cvls')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_interface_output_fcoe_intf_total_interfaces(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_interface = ET.Element("fcoe_get_interface")
        config = fcoe_get_interface
        output = ET.SubElement(fcoe_get_interface, "output")
        fcoe_intf_total_interfaces = ET.SubElement(output, "fcoe-intf-total-interfaces")
        fcoe_intf_total_interfaces.text = kwargs.pop('fcoe_intf_total_interfaces')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_interface = ET.SubElement(input, "fcoe-login-interface")
        fcoe_login_interface.text = kwargs.pop('fcoe_login_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_vfid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_vfid = ET.SubElement(input, "fcoe-login-vfid")
        fcoe_login_vfid.text = kwargs.pop('fcoe_login_vfid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_vlan = ET.SubElement(input, "fcoe-login-vlan")
        fcoe_login_vlan.text = kwargs.pop('fcoe_login_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_input_fcoe_login_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        input = ET.SubElement(fcoe_get_login, "input")
        fcoe_login_rbridge_id = ET.SubElement(input, "fcoe-login-rbridge-id")
        fcoe_login_rbridge_id.text = kwargs.pop('fcoe_login_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_session_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac.text = kwargs.pop('fcoe_login_session_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_fcoe_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_fcoe_interface_name = ET.SubElement(fcoe_login_list, "fcoe-login-fcoe-interface-name")
        fcoe_login_fcoe_interface_name.text = kwargs.pop('fcoe_login_fcoe_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_interface_name = ET.SubElement(fcoe_login_list, "fcoe-login-interface-name")
        fcoe_login_interface_name.text = kwargs.pop('fcoe_login_interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        interface_type = ET.SubElement(fcoe_login_list, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        interface_name = ET.SubElement(fcoe_login_list, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_device_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_device_wwn = ET.SubElement(fcoe_login_list, "fcoe-login-device-wwn")
        fcoe_login_device_wwn.text = kwargs.pop('fcoe_login_device_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_device_mac(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_device_mac = ET.SubElement(fcoe_login_list, "fcoe-login-device-mac")
        fcoe_login_device_mac.text = kwargs.pop('fcoe_login_device_mac')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_direct_attached(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_direct_attached = ET.SubElement(fcoe_login_list, "fcoe-login-direct-attached")
        fcoe_login_direct_attached.text = kwargs.pop('fcoe_login_direct_attached')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_list_fcoe_login_connected_peer_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_list = ET.SubElement(output, "fcoe-login-list")
        fcoe_login_session_mac_key = ET.SubElement(fcoe_login_list, "fcoe-login-session-mac")
        fcoe_login_session_mac_key.text = kwargs.pop('fcoe_login_session_mac')
        fcoe_login_connected_peer_type = ET.SubElement(fcoe_login_list, "fcoe-login-connected-peer-type")
        fcoe_login_connected_peer_type.text = kwargs.pop('fcoe_login_connected_peer_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcoe_get_login_output_fcoe_login_total_logins(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcoe_get_login = ET.Element("fcoe_get_login")
        config = fcoe_get_login
        output = ET.SubElement(fcoe_get_login, "output")
        fcoe_login_total_logins = ET.SubElement(output, "fcoe-login-total-logins")
        fcoe_login_total_logins.text = kwargs.pop('fcoe_login_total_logins')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        