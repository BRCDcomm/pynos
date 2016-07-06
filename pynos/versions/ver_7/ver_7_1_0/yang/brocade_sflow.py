#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_sflow(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def sflow_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        enable = ET.SubElement(sflow, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_collector_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        collector = ET.SubElement(sflow, "collector")
        collector_port_number_key = ET.SubElement(collector, "collector-port-number")
        collector_port_number_key.text = kwargs.pop('collector_port_number')
        use_vrf_key = ET.SubElement(collector, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        collector_ip_address = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address.text = kwargs.pop('collector_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_collector_port_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        collector = ET.SubElement(sflow, "collector")
        collector_ip_address_key = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address_key.text = kwargs.pop('collector_ip_address')
        use_vrf_key = ET.SubElement(collector, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        collector_port_number = ET.SubElement(collector, "collector-port-number")
        collector_port_number.text = kwargs.pop('collector_port_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        collector = ET.SubElement(sflow, "collector")
        collector_ip_address_key = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address_key.text = kwargs.pop('collector_ip_address')
        collector_port_number_key = ET.SubElement(collector, "collector-port-number")
        collector_port_number_key.text = kwargs.pop('collector_port_number')
        use_vrf = ET.SubElement(collector, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        source_ip = ET.SubElement(sflow, "source-ip")
        source_ip.text = kwargs.pop('source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_polling_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        polling_interval = ET.SubElement(sflow, "polling-interval")
        polling_interval.text = kwargs.pop('polling_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_sample_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        sample_rate = ET.SubElement(sflow, "sample-rate")
        sample_rate.text = kwargs.pop('sample_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_profile_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow_profile = ET.SubElement(config, "sflow-profile", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        profile_name = ET.SubElement(sflow_profile, "profile-name")
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_profile_profile_sampling_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow_profile = ET.SubElement(config, "sflow-profile", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        profile_name_key = ET.SubElement(sflow_profile, "profile-name")
        profile_name_key.text = kwargs.pop('profile_name')
        profile_sampling_rate = ET.SubElement(sflow_profile, "profile-sampling-rate")
        profile_sampling_rate.text = kwargs.pop('profile_sampling_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        enable = ET.SubElement(sflow, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_collector_ip_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        collector = ET.SubElement(sflow, "collector")
        collector_port_number_key = ET.SubElement(collector, "collector-port-number")
        collector_port_number_key.text = kwargs.pop('collector_port_number')
        use_vrf_key = ET.SubElement(collector, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        collector_ip_address = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address.text = kwargs.pop('collector_ip_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_collector_port_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        collector = ET.SubElement(sflow, "collector")
        collector_ip_address_key = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address_key.text = kwargs.pop('collector_ip_address')
        use_vrf_key = ET.SubElement(collector, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        collector_port_number = ET.SubElement(collector, "collector-port-number")
        collector_port_number.text = kwargs.pop('collector_port_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_collector_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        collector = ET.SubElement(sflow, "collector")
        collector_ip_address_key = ET.SubElement(collector, "collector-ip-address")
        collector_ip_address_key.text = kwargs.pop('collector_ip_address')
        collector_port_number_key = ET.SubElement(collector, "collector-port-number")
        collector_port_number_key.text = kwargs.pop('collector_port_number')
        use_vrf = ET.SubElement(collector, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        source_ip = ET.SubElement(sflow, "source-ip")
        source_ip.text = kwargs.pop('source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_polling_interval(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        polling_interval = ET.SubElement(sflow, "polling-interval")
        polling_interval.text = kwargs.pop('polling_interval')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_sample_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow = ET.SubElement(config, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        sample_rate = ET.SubElement(sflow, "sample-rate")
        sample_rate.text = kwargs.pop('sample_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_profile_profile_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow_profile = ET.SubElement(config, "sflow-profile", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        profile_name = ET.SubElement(sflow_profile, "profile-name")
        profile_name.text = kwargs.pop('profile_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def sflow_profile_profile_sampling_rate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        sflow_profile = ET.SubElement(config, "sflow-profile", xmlns="urn:brocade.com:mgmt:brocade-sflow")
        profile_name_key = ET.SubElement(sflow_profile, "profile-name")
        profile_name_key.text = kwargs.pop('profile_name')
        profile_sampling_rate = ET.SubElement(sflow_profile, "profile-sampling-rate")
        profile_sampling_rate.text = kwargs.pop('profile_sampling_rate')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        