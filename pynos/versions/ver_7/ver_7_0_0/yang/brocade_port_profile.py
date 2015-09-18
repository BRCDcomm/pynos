#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_port_profile(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_allow_nonprofiledmacs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        allow = ET.SubElement(port_profile, "allow")
        nonprofiledmacs = ET.SubElement(allow, "nonprofiledmacs")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_basic_basic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport_basic = ET.SubElement(vlan_profile, "switchport-basic")
        basic = ET.SubElement(switchport_basic, "basic")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_mode_vlan_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        mode = ET.SubElement(switchport, "mode")
        vlan_mode = ET.SubElement(mode, "vlan-mode")
        vlan_mode.text = kwargs.pop('vlan_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_vlan_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access = ET.SubElement(switchport, "access")
        vlan = ET.SubElement(access, "vlan")
        name = ET.SubElement(vlan, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_vlan_classification_access_vlan_access_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_vlan_classification = ET.SubElement(switchport, "access-mac-vlan-classification")
        access = ET.SubElement(access_mac_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_mac_address_key = ET.SubElement(vlan, "access-mac-address")
        access_mac_address_key.text = kwargs.pop('access_mac_address')
        access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id.text = kwargs.pop('access_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_vlan_classification_access_vlan_access_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_vlan_classification = ET.SubElement(switchport, "access-mac-vlan-classification")
        access = ET.SubElement(access_mac_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id_key.text = kwargs.pop('access_vlan_id')
        access_mac_address = ET.SubElement(vlan, "access-mac-address")
        access_mac_address.text = kwargs.pop('access_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_group_vlan_classification_access_vlan_access_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
        access = ET.SubElement(access_mac_group_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_mac_group_key = ET.SubElement(vlan, "access-mac-group")
        access_mac_group_key.text = kwargs.pop('access_mac_group')
        access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id.text = kwargs.pop('access_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_group_vlan_classification_access_vlan_access_mac_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
        access = ET.SubElement(access_mac_group_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id_key.text = kwargs.pop('access_vlan_id')
        access_mac_group = ET.SubElement(vlan, "access-mac-group")
        access_mac_group.text = kwargs.pop('access_mac_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        all = ET.SubElement(vlan, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_none(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        none = ET.SubElement(vlan, "none")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        add = ET.SubElement(vlan, "add")
        add.text = kwargs.pop('add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_excpt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        excpt = ET.SubElement(vlan, "except")
        excpt.text = kwargs.pop('excpt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        remove = ET.SubElement(vlan, "remove")
        remove.text = kwargs.pop('remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_add_trunk_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        add = ET.SubElement(vlan, "add")
        trunk_ctag_id_key = ET.SubElement(add, "trunk-ctag-id")
        trunk_ctag_id_key.text = kwargs.pop('trunk_ctag_id')
        trunk_vlan_id = ET.SubElement(add, "trunk-vlan-id")
        trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_add_trunk_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        add = ET.SubElement(vlan, "add")
        trunk_vlan_id_key = ET.SubElement(add, "trunk-vlan-id")
        trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
        trunk_ctag_id = ET.SubElement(add, "trunk-ctag-id")
        trunk_ctag_id.text = kwargs.pop('trunk_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        remove = ET.SubElement(vlan, "remove")
        trunk_ctag_id_key = ET.SubElement(remove, "trunk-ctag-id")
        trunk_ctag_id_key.text = kwargs.pop('trunk_ctag_id')
        trunk_vlan_id = ET.SubElement(remove, "trunk-vlan-id")
        trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        remove = ET.SubElement(vlan, "remove")
        trunk_vlan_id_key = ET.SubElement(remove, "trunk-vlan-id")
        trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
        trunk_ctag_id = ET.SubElement(remove, "trunk-ctag-id")
        trunk_ctag_id.text = kwargs.pop('trunk_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan_classification_native_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        native_vlan_classification = ET.SubElement(trunk, "native-vlan-classification")
        native_vlan_id = ET.SubElement(native_vlan_classification, "native-vlan-id")
        native_vlan_id.text = kwargs.pop('native_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan_classification_native_vlan_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        native_vlan_classification = ET.SubElement(trunk, "native-vlan-classification")
        native_vlan_ctag_id = ET.SubElement(native_vlan_classification, "native-vlan-ctag-id")
        native_vlan_ctag_id.text = kwargs.pop('native_vlan_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        native_vlan = ET.SubElement(trunk, "native-vlan")
        native_vlan.text = kwargs.pop('native_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_fcoe_profile_fcoeport_fcoe_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        fcoe_profile = ET.SubElement(port_profile, "fcoe-profile")
        fcoeport = ET.SubElement(fcoe_profile, "fcoeport")
        fcoe_map_name = ET.SubElement(fcoeport, "fcoe-map-name")
        fcoe_map_name.text = kwargs.pop('fcoe_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_cee(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        cee = ET.SubElement(qos_profile, "cee")
        cee.text = kwargs.pop('cee')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        cos = ET.SubElement(qos, "cos")
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_trust_trust_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        trust = ET.SubElement(qos, "trust")
        trust_cos = ET.SubElement(trust, "trust-cos")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        cos_mutation = ET.SubElement(qos, "cos-mutation")
        cos_mutation.text = kwargs.pop('cos_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        cos_traffic_class = ET.SubElement(qos, "cos-traffic-class")
        cos_traffic_class.text = kwargs.pop('cos_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_flowcontrolglobal_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        flowcontrolglobal = ET.SubElement(flowcontrol, "flowcontrolglobal")
        tx = ET.SubElement(flowcontrolglobal, "tx")
        tx.text = kwargs.pop('tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_flowcontrolglobal_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        flowcontrolglobal = ET.SubElement(flowcontrol, "flowcontrolglobal")
        rx = ET.SubElement(flowcontrolglobal, "rx")
        rx.text = kwargs.pop('rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        pfc = ET.SubElement(flowcontrol, "pfc")
        pfc_cos = ET.SubElement(pfc, "pfc-cos")
        pfc_cos.text = kwargs.pop('pfc_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        pfc = ET.SubElement(flowcontrol, "pfc")
        pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
        pfc_cos_key.text = kwargs.pop('pfc_cos')
        pfc_tx = ET.SubElement(pfc, "pfc-tx")
        pfc_tx.text = kwargs.pop('pfc_tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        pfc = ET.SubElement(flowcontrol, "pfc")
        pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
        pfc_cos_key.text = kwargs.pop('pfc_cos')
        pfc_rx = ET.SubElement(pfc, "pfc-rx")
        pfc_rx.text = kwargs.pop('pfc_rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_mac_access_group_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        mac = ET.SubElement(security_profile, "mac")
        access_group = ET.SubElement(mac, "access-group")
        access_group_name = ET.SubElement(access_group, "access-group-name")
        access_group_name.text = kwargs.pop('access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_mac_access_group_in_cg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        mac = ET.SubElement(security_profile, "mac")
        access_group = ET.SubElement(mac, "access-group")
        in_cg = ET.SubElement(access_group, "in")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ip_access_group_ipv4_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ip = ET.SubElement(security_profile, "ip")
        access_group = ET.SubElement(ip, "access-group")
        ipv4_access_group_name = ET.SubElement(access_group, "ipv4-access-group-name")
        ipv4_access_group_name.text = kwargs.pop('ipv4_access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ip_access_group_ipv4_in(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ip = ET.SubElement(security_profile, "ip")
        access_group = ET.SubElement(ip, "access-group")
        ipv4_in = ET.SubElement(access_group, "ipv4-in")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ipv6_access_group_ipv6_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ipv6 = ET.SubElement(security_profile, "ipv6")
        access_group = ET.SubElement(ipv6, "access-group")
        ipv6_access_group_name = ET.SubElement(access_group, "ipv6-access-group-name")
        ipv6_access_group_name.text = kwargs.pop('ipv6_access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ipv6_access_group_ipv6_in(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ipv6 = ET.SubElement(security_profile, "ipv6")
        access_group = ET.SubElement(ipv6, "access-group")
        ipv6_in = ET.SubElement(access_group, "ipv6-in")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_restrict_flooding_container_restrict_flooding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        restrict_flooding_container = ET.SubElement(port_profile, "restrict-flooding-container")
        restrict_flooding = ET.SubElement(restrict_flooding_container, "restrict-flooding")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(port_profile, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_static_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        static = ET.SubElement(port_profile, "static")
        mac_address = ET.SubElement(static, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_domain_port_profile_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_domain = ET.SubElement(config, "port-profile-domain", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile_domain_name = ET.SubElement(port_profile_domain, "port-profile-domain-name")
        port_profile_domain_name.text = kwargs.pop('port_profile_domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_domain_profile_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_domain = ET.SubElement(config, "port-profile-domain", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile_domain_name_key = ET.SubElement(port_profile_domain, "port-profile-domain-name")
        port_profile_domain_name_key.text = kwargs.pop('port_profile_domain_name')
        profile = ET.SubElement(port_profile_domain, "profile")
        profile_name = ET.SubElement(profile, "profile-name")
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_allow_nonprofiledmacs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        allow = ET.SubElement(port_profile, "allow")
        nonprofiledmacs = ET.SubElement(allow, "nonprofiledmacs")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_basic_basic(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport_basic = ET.SubElement(vlan_profile, "switchport-basic")
        basic = ET.SubElement(switchport_basic, "basic")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_mode_vlan_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        mode = ET.SubElement(switchport, "mode")
        vlan_mode = ET.SubElement(mode, "vlan-mode")
        vlan_mode.text = kwargs.pop('vlan_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_vlan_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access = ET.SubElement(switchport, "access")
        vlan = ET.SubElement(access, "vlan")
        name = ET.SubElement(vlan, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_vlan_classification_access_vlan_access_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_vlan_classification = ET.SubElement(switchport, "access-mac-vlan-classification")
        access = ET.SubElement(access_mac_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_mac_address_key = ET.SubElement(vlan, "access-mac-address")
        access_mac_address_key.text = kwargs.pop('access_mac_address')
        access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id.text = kwargs.pop('access_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_vlan_classification_access_vlan_access_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_vlan_classification = ET.SubElement(switchport, "access-mac-vlan-classification")
        access = ET.SubElement(access_mac_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id_key.text = kwargs.pop('access_vlan_id')
        access_mac_address = ET.SubElement(vlan, "access-mac-address")
        access_mac_address.text = kwargs.pop('access_mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_group_vlan_classification_access_vlan_access_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
        access = ET.SubElement(access_mac_group_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_mac_group_key = ET.SubElement(vlan, "access-mac-group")
        access_mac_group_key.text = kwargs.pop('access_mac_group')
        access_vlan_id = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id.text = kwargs.pop('access_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_access_mac_group_vlan_classification_access_vlan_access_mac_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        access_mac_group_vlan_classification = ET.SubElement(switchport, "access-mac-group-vlan-classification")
        access = ET.SubElement(access_mac_group_vlan_classification, "access")
        vlan = ET.SubElement(access, "vlan")
        access_vlan_id_key = ET.SubElement(vlan, "access-vlan-id")
        access_vlan_id_key.text = kwargs.pop('access_vlan_id')
        access_mac_group = ET.SubElement(vlan, "access-mac-group")
        access_mac_group.text = kwargs.pop('access_mac_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        all = ET.SubElement(vlan, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_none(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        none = ET.SubElement(vlan, "none")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_add(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        add = ET.SubElement(vlan, "add")
        add.text = kwargs.pop('add')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_excpt(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        excpt = ET.SubElement(vlan, "except")
        excpt.text = kwargs.pop('excpt')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_allowed_vlan_remove(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        allowed = ET.SubElement(trunk, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        remove = ET.SubElement(vlan, "remove")
        remove.text = kwargs.pop('remove')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_add_trunk_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        add = ET.SubElement(vlan, "add")
        trunk_ctag_id_key = ET.SubElement(add, "trunk-ctag-id")
        trunk_ctag_id_key.text = kwargs.pop('trunk_ctag_id')
        trunk_vlan_id = ET.SubElement(add, "trunk-vlan-id")
        trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_add_trunk_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        add = ET.SubElement(vlan, "add")
        trunk_vlan_id_key = ET.SubElement(add, "trunk-vlan-id")
        trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
        trunk_ctag_id = ET.SubElement(add, "trunk-ctag-id")
        trunk_ctag_id.text = kwargs.pop('trunk_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        remove = ET.SubElement(vlan, "remove")
        trunk_ctag_id_key = ET.SubElement(remove, "trunk-ctag-id")
        trunk_ctag_id_key.text = kwargs.pop('trunk_ctag_id')
        trunk_vlan_id = ET.SubElement(remove, "trunk-vlan-id")
        trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
        allowed = ET.SubElement(trunk_vlan_classification, "allowed")
        vlan = ET.SubElement(allowed, "vlan")
        remove = ET.SubElement(vlan, "remove")
        trunk_vlan_id_key = ET.SubElement(remove, "trunk-vlan-id")
        trunk_vlan_id_key.text = kwargs.pop('trunk_vlan_id')
        trunk_ctag_id = ET.SubElement(remove, "trunk-ctag-id")
        trunk_ctag_id.text = kwargs.pop('trunk_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan_classification_native_vlan_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        native_vlan_classification = ET.SubElement(trunk, "native-vlan-classification")
        native_vlan_id = ET.SubElement(native_vlan_classification, "native-vlan-id")
        native_vlan_id.text = kwargs.pop('native_vlan_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan_classification_native_vlan_ctag_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        native_vlan_classification = ET.SubElement(trunk, "native-vlan-classification")
        native_vlan_ctag_id = ET.SubElement(native_vlan_classification, "native-vlan-ctag-id")
        native_vlan_ctag_id.text = kwargs.pop('native_vlan_ctag_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_vlan_profile_switchport_trunk_native_vlan(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        vlan_profile = ET.SubElement(port_profile, "vlan-profile")
        switchport = ET.SubElement(vlan_profile, "switchport")
        trunk = ET.SubElement(switchport, "trunk")
        native_vlan = ET.SubElement(trunk, "native-vlan")
        native_vlan.text = kwargs.pop('native_vlan')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_fcoe_profile_fcoeport_fcoe_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        fcoe_profile = ET.SubElement(port_profile, "fcoe-profile")
        fcoeport = ET.SubElement(fcoe_profile, "fcoeport")
        fcoe_map_name = ET.SubElement(fcoeport, "fcoe-map-name")
        fcoe_map_name.text = kwargs.pop('fcoe_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_cee(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        cee = ET.SubElement(qos_profile, "cee")
        cee.text = kwargs.pop('cee')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        cos = ET.SubElement(qos, "cos")
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_trust_trust_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        trust = ET.SubElement(qos, "trust")
        trust_cos = ET.SubElement(trust, "trust-cos")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos_mutation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        cos_mutation = ET.SubElement(qos, "cos-mutation")
        cos_mutation.text = kwargs.pop('cos_mutation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_cos_traffic_class(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        cos_traffic_class = ET.SubElement(qos, "cos-traffic-class")
        cos_traffic_class.text = kwargs.pop('cos_traffic_class')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_flowcontrolglobal_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        flowcontrolglobal = ET.SubElement(flowcontrol, "flowcontrolglobal")
        tx = ET.SubElement(flowcontrolglobal, "tx")
        tx.text = kwargs.pop('tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_flowcontrolglobal_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        flowcontrolglobal = ET.SubElement(flowcontrol, "flowcontrolglobal")
        rx = ET.SubElement(flowcontrolglobal, "rx")
        rx.text = kwargs.pop('rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        pfc = ET.SubElement(flowcontrol, "pfc")
        pfc_cos = ET.SubElement(pfc, "pfc-cos")
        pfc_cos.text = kwargs.pop('pfc_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_tx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        pfc = ET.SubElement(flowcontrol, "pfc")
        pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
        pfc_cos_key.text = kwargs.pop('pfc_cos')
        pfc_tx = ET.SubElement(pfc, "pfc-tx")
        pfc_tx.text = kwargs.pop('pfc_tx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_qos_profile_qos_flowcontrol_pfc_pfc_rx(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        qos_profile = ET.SubElement(port_profile, "qos-profile")
        qos = ET.SubElement(qos_profile, "qos")
        flowcontrol = ET.SubElement(qos, "flowcontrol")
        pfc = ET.SubElement(flowcontrol, "pfc")
        pfc_cos_key = ET.SubElement(pfc, "pfc-cos")
        pfc_cos_key.text = kwargs.pop('pfc_cos')
        pfc_rx = ET.SubElement(pfc, "pfc-rx")
        pfc_rx.text = kwargs.pop('pfc_rx')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_mac_access_group_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        mac = ET.SubElement(security_profile, "mac")
        access_group = ET.SubElement(mac, "access-group")
        access_group_name = ET.SubElement(access_group, "access-group-name")
        access_group_name.text = kwargs.pop('access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_mac_access_group_in_cg(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        mac = ET.SubElement(security_profile, "mac")
        access_group = ET.SubElement(mac, "access-group")
        in_cg = ET.SubElement(access_group, "in")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ip_access_group_ipv4_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ip = ET.SubElement(security_profile, "ip")
        access_group = ET.SubElement(ip, "access-group")
        ipv4_access_group_name = ET.SubElement(access_group, "ipv4-access-group-name")
        ipv4_access_group_name.text = kwargs.pop('ipv4_access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ip_access_group_ipv4_in(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ip = ET.SubElement(security_profile, "ip")
        access_group = ET.SubElement(ip, "access-group")
        ipv4_in = ET.SubElement(access_group, "ipv4-in")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ipv6_access_group_ipv6_access_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ipv6 = ET.SubElement(security_profile, "ipv6")
        access_group = ET.SubElement(ipv6, "access-group")
        ipv6_access_group_name = ET.SubElement(access_group, "ipv6-access-group-name")
        ipv6_access_group_name.text = kwargs.pop('ipv6_access_group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_security_profile_ipv6_access_group_ipv6_in(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        security_profile = ET.SubElement(port_profile, "security-profile")
        ipv6 = ET.SubElement(security_profile, "ipv6")
        access_group = ET.SubElement(ipv6, "access-group")
        ipv6_in = ET.SubElement(access_group, "ipv6-in")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_restrict_flooding_container_restrict_flooding(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile = ET.SubElement(config, "port-profile", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        restrict_flooding_container = ET.SubElement(port_profile, "restrict-flooding-container")
        restrict_flooding = ET.SubElement(restrict_flooding_container, "restrict-flooding")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        name = ET.SubElement(port_profile, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_activate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        activate = ET.SubElement(port_profile, "activate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_global_port_profile_static_mac_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_global = ET.SubElement(config, "port-profile-global", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile = ET.SubElement(port_profile_global, "port-profile")
        name_key = ET.SubElement(port_profile, "name")
        name_key.text = kwargs.pop('name')
        static = ET.SubElement(port_profile, "static")
        mac_address = ET.SubElement(static, "mac-address")
        mac_address.text = kwargs.pop('mac_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_domain_port_profile_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_domain = ET.SubElement(config, "port-profile-domain", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile_domain_name = ET.SubElement(port_profile_domain, "port-profile-domain-name")
        port_profile_domain_name.text = kwargs.pop('port_profile_domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def port_profile_domain_profile_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        port_profile_domain = ET.SubElement(config, "port-profile-domain", xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        port_profile_domain_name_key = ET.SubElement(port_profile_domain, "port-profile-domain-name")
        port_profile_domain_name_key.text = kwargs.pop('port_profile_domain_name')
        profile = ET.SubElement(port_profile_domain, "profile")
        profile_name = ET.SubElement(profile, "profile-name")
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        