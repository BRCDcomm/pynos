#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_lag(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_port_channel_detail_input_last_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        input = ET.SubElement(get_port_channel_detail, "input")
        last_aggregator_id = ET.SubElement(input, "last-aggregator-id")
        last_aggregator_id.text = kwargs.pop('last_aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggregator_id = ET.SubElement(lacp, "aggregator-id")
        aggregator_id.text = kwargs.pop('aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggregator_type = ET.SubElement(lacp, "aggregator-type")
        aggregator_type.text = kwargs.pop('aggregator_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_isvlag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        isvlag = ET.SubElement(lacp, "isvlag")
        isvlag.text = kwargs.pop('isvlag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggregator_mode = ET.SubElement(lacp, "aggregator-mode")
        aggregator_mode.text = kwargs.pop('aggregator_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_admin_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        admin_key = ET.SubElement(lacp, "admin-key")
        admin_key.text = kwargs.pop('admin_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        oper_key = ET.SubElement(lacp, "oper-key")
        oper_key.text = kwargs.pop('oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_actor_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_system_id = ET.SubElement(lacp, "actor-system-id")
        actor_system_id.text = kwargs.pop('actor_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_system_id = ET.SubElement(lacp, "partner-system-id")
        partner_system_id.text = kwargs.pop('partner_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        system_priority = ET.SubElement(lacp, "system-priority")
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_oper_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_priority = ET.SubElement(lacp, "partner-oper-priority")
        partner_oper_priority.text = kwargs.pop('partner_oper_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_rx_link_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        rx_link_count = ET.SubElement(lacp, "rx-link-count")
        rx_link_count.text = kwargs.pop('rx_link_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_tx_link_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        tx_link_count = ET.SubElement(lacp, "tx-link-count")
        tx_link_count.text = kwargs.pop('tx_link_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_individual_agg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        individual_agg = ET.SubElement(lacp, "individual-agg")
        individual_agg.text = kwargs.pop('individual_agg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_ready_agg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        ready_agg = ET.SubElement(lacp, "ready-agg")
        ready_agg.text = kwargs.pop('ready_agg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_key = ET.SubElement(lacp, "partner-oper-key")
        partner_oper_key.text = kwargs.pop('partner_oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        rbridge_id = ET.SubElement(aggr_member, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        interface_type = ET.SubElement(aggr_member, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        interface_name = ET.SubElement(aggr_member, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_actor_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        actor_port = ET.SubElement(aggr_member, "actor-port")
        actor_port.text = kwargs.pop('actor_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        sync = ET.SubElement(aggr_member, "sync")
        sync.text = kwargs.pop('sync')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        input = ET.SubElement(get_portchannel_info_by_intf, "input")
        interface_type = ET.SubElement(input, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        input = ET.SubElement(get_portchannel_info_by_intf, "input")
        interface_name = ET.SubElement(input, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        interface_type = ET.SubElement(lacp, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        interface_name = ET.SubElement(lacp, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_port = ET.SubElement(lacp, "actor-port")
        actor_port.text = kwargs.pop('actor_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_admin_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        admin_key = ET.SubElement(lacp, "admin-key")
        admin_key.text = kwargs.pop('admin_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        oper_key = ET.SubElement(lacp, "oper-key")
        oper_key.text = kwargs.pop('oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_system_id = ET.SubElement(lacp, "actor-system-id")
        actor_system_id.text = kwargs.pop('actor_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_system_id = ET.SubElement(lacp, "partner-system-id")
        partner_system_id.text = kwargs.pop('partner_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        system_priority = ET.SubElement(lacp, "system-priority")
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_priority = ET.SubElement(lacp, "partner-oper-priority")
        partner_oper_priority.text = kwargs.pop('partner_oper_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_priority = ET.SubElement(lacp, "actor-priority")
        actor_priority.text = kwargs.pop('actor_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_receive_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        receive_machine_state = ET.SubElement(lacp, "receive-machine-state")
        receive_machine_state.text = kwargs.pop('receive_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_periodic_transmission_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        periodic_transmission_machine_state = ET.SubElement(lacp, "periodic-transmission-machine-state")
        periodic_transmission_machine_state.text = kwargs.pop('periodic_transmission_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_mux_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        mux_machine_state = ET.SubElement(lacp, "mux-machine-state")
        mux_machine_state.text = kwargs.pop('mux_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        admin_state = ET.SubElement(lacp, "admin-state")
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        oper_state = ET.SubElement(lacp, "oper-state")
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_state = ET.SubElement(lacp, "partner-oper-state")
        partner_oper_state.text = kwargs.pop('partner_oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_port = ET.SubElement(lacp, "partner-oper-port")
        partner_oper_port.text = kwargs.pop('partner_oper_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_chip_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_chip_number = ET.SubElement(lacp, "actor-chip-number")
        actor_chip_number.text = kwargs.pop('actor_chip_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_max_deskew(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_max_deskew = ET.SubElement(lacp, "actor-max-deskew")
        actor_max_deskew.text = kwargs.pop('actor_max_deskew')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_chip_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_chip_number = ET.SubElement(lacp, "partner-chip-number")
        partner_chip_number.text = kwargs.pop('partner_chip_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_max_deskew(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_max_deskew = ET.SubElement(lacp, "partner-max-deskew")
        partner_max_deskew.text = kwargs.pop('partner_max_deskew')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_brcd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_brcd_state = ET.SubElement(lacp, "actor-brcd-state")
        actor_brcd_state.text = kwargs.pop('actor_brcd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_brcd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_brcd_state = ET.SubElement(lacp, "partner-brcd-state")
        partner_brcd_state.text = kwargs.pop('partner_brcd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id.text = kwargs.pop('group_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_port_channel_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        port_channel = ET.SubElement(port_channel_redundancy_group, "port-channel")
        name = ET.SubElement(port_channel, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_port_channel_port_channel_active(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        port_channel = ET.SubElement(port_channel_redundancy_group, "port-channel")
        name_key = ET.SubElement(port_channel, "name")
        name_key.text = kwargs.pop('name')
        port_channel_active = ET.SubElement(port_channel, "port-channel-active")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        activate = ET.SubElement(port_channel_redundancy_group, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_input_last_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        input = ET.SubElement(get_port_channel_detail, "input")
        last_aggregator_id = ET.SubElement(input, "last-aggregator-id")
        last_aggregator_id.text = kwargs.pop('last_aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggregator_id = ET.SubElement(lacp, "aggregator-id")
        aggregator_id.text = kwargs.pop('aggregator_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggregator_type = ET.SubElement(lacp, "aggregator-type")
        aggregator_type.text = kwargs.pop('aggregator_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_isvlag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        isvlag = ET.SubElement(lacp, "isvlag")
        isvlag.text = kwargs.pop('isvlag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggregator_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggregator_mode = ET.SubElement(lacp, "aggregator-mode")
        aggregator_mode.text = kwargs.pop('aggregator_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_admin_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        admin_key = ET.SubElement(lacp, "admin-key")
        admin_key.text = kwargs.pop('admin_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        oper_key = ET.SubElement(lacp, "oper-key")
        oper_key.text = kwargs.pop('oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_actor_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_system_id = ET.SubElement(lacp, "actor-system-id")
        actor_system_id.text = kwargs.pop('actor_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_system_id = ET.SubElement(lacp, "partner-system-id")
        partner_system_id.text = kwargs.pop('partner_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        system_priority = ET.SubElement(lacp, "system-priority")
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_oper_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_priority = ET.SubElement(lacp, "partner-oper-priority")
        partner_oper_priority.text = kwargs.pop('partner_oper_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_rx_link_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        rx_link_count = ET.SubElement(lacp, "rx-link-count")
        rx_link_count.text = kwargs.pop('rx_link_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_tx_link_count(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        tx_link_count = ET.SubElement(lacp, "tx-link-count")
        tx_link_count.text = kwargs.pop('tx_link_count')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_individual_agg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        individual_agg = ET.SubElement(lacp, "individual-agg")
        individual_agg.text = kwargs.pop('individual_agg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_ready_agg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        ready_agg = ET.SubElement(lacp, "ready-agg")
        ready_agg.text = kwargs.pop('ready_agg')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_partner_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_key = ET.SubElement(lacp, "partner-oper-key")
        partner_oper_key.text = kwargs.pop('partner_oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        rbridge_id = ET.SubElement(aggr_member, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        interface_type = ET.SubElement(aggr_member, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        interface_name = ET.SubElement(aggr_member, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_actor_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        actor_port = ET.SubElement(aggr_member, "actor-port")
        actor_port.text = kwargs.pop('actor_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_lacp_aggr_member_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        lacp = ET.SubElement(output, "lacp")
        aggr_member = ET.SubElement(lacp, "aggr-member")
        sync = ET.SubElement(aggr_member, "sync")
        sync.text = kwargs.pop('sync')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_port_channel_detail_output_has_more(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_port_channel_detail = ET.Element("get_port_channel_detail")
        config = get_port_channel_detail
        output = ET.SubElement(get_port_channel_detail, "output")
        has_more = ET.SubElement(output, "has-more")
        has_more.text = kwargs.pop('has_more')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_input_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        input = ET.SubElement(get_portchannel_info_by_intf, "input")
        interface_type = ET.SubElement(input, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_input_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        input = ET.SubElement(get_portchannel_info_by_intf, "input")
        interface_name = ET.SubElement(input, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        interface_type = ET.SubElement(lacp, "interface-type")
        interface_type.text = kwargs.pop('interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_interface_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        interface_name = ET.SubElement(lacp, "interface-name")
        interface_name.text = kwargs.pop('interface_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_port = ET.SubElement(lacp, "actor-port")
        actor_port.text = kwargs.pop('actor_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_admin_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        admin_key = ET.SubElement(lacp, "admin-key")
        admin_key.text = kwargs.pop('admin_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_oper_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        oper_key = ET.SubElement(lacp, "oper-key")
        oper_key.text = kwargs.pop('oper_key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_system_id = ET.SubElement(lacp, "actor-system-id")
        actor_system_id.text = kwargs.pop('actor_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_system_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_system_id = ET.SubElement(lacp, "partner-system-id")
        partner_system_id.text = kwargs.pop('partner_system_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_system_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        system_priority = ET.SubElement(lacp, "system-priority")
        system_priority.text = kwargs.pop('system_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_priority = ET.SubElement(lacp, "partner-oper-priority")
        partner_oper_priority.text = kwargs.pop('partner_oper_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_priority = ET.SubElement(lacp, "actor-priority")
        actor_priority.text = kwargs.pop('actor_priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_receive_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        receive_machine_state = ET.SubElement(lacp, "receive-machine-state")
        receive_machine_state.text = kwargs.pop('receive_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_periodic_transmission_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        periodic_transmission_machine_state = ET.SubElement(lacp, "periodic-transmission-machine-state")
        periodic_transmission_machine_state.text = kwargs.pop('periodic_transmission_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_mux_machine_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        mux_machine_state = ET.SubElement(lacp, "mux-machine-state")
        mux_machine_state.text = kwargs.pop('mux_machine_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_admin_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        admin_state = ET.SubElement(lacp, "admin-state")
        admin_state.text = kwargs.pop('admin_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        oper_state = ET.SubElement(lacp, "oper-state")
        oper_state.text = kwargs.pop('oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_state = ET.SubElement(lacp, "partner-oper-state")
        partner_oper_state.text = kwargs.pop('partner_oper_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_oper_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_oper_port = ET.SubElement(lacp, "partner-oper-port")
        partner_oper_port.text = kwargs.pop('partner_oper_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_chip_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_chip_number = ET.SubElement(lacp, "actor-chip-number")
        actor_chip_number.text = kwargs.pop('actor_chip_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_max_deskew(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_max_deskew = ET.SubElement(lacp, "actor-max-deskew")
        actor_max_deskew.text = kwargs.pop('actor_max_deskew')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_chip_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_chip_number = ET.SubElement(lacp, "partner-chip-number")
        partner_chip_number.text = kwargs.pop('partner_chip_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_max_deskew(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_max_deskew = ET.SubElement(lacp, "partner-max-deskew")
        partner_max_deskew.text = kwargs.pop('partner_max_deskew')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_actor_brcd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        actor_brcd_state = ET.SubElement(lacp, "actor-brcd-state")
        actor_brcd_state.text = kwargs.pop('actor_brcd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_portchannel_info_by_intf_output_lacp_partner_brcd_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_portchannel_info_by_intf = ET.Element("get_portchannel_info_by_intf")
        config = get_portchannel_info_by_intf
        output = ET.SubElement(get_portchannel_info_by_intf, "output")
        lacp = ET.SubElement(output, "lacp")
        partner_brcd_state = ET.SubElement(lacp, "partner-brcd-state")
        partner_brcd_state.text = kwargs.pop('partner_brcd_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_group_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id.text = kwargs.pop('group_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_port_channel_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        port_channel = ET.SubElement(port_channel_redundancy_group, "port-channel")
        name = ET.SubElement(port_channel, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_port_channel_port_channel_active(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        port_channel = ET.SubElement(port_channel_redundancy_group, "port-channel")
        name_key = ET.SubElement(port_channel, "name")
        name_key.text = kwargs.pop('name')
        port_channel_active = ET.SubElement(port_channel, "port-channel-active")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_channel_redundancy_group_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_channel_redundancy_group = ET.SubElement(config, "port-channel-redundancy-group", xmlns="urn:brocade.com:mgmt:brocade-lag")
        group_id_key = ET.SubElement(port_channel_redundancy_group, "group-id")
        group_id_key.text = kwargs.pop('group_id')
        activate = ET.SubElement(port_channel_redundancy_group, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        