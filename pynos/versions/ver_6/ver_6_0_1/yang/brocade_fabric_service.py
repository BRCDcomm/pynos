#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fabric_service(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def show_linkinfo_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        input = ET.SubElement(show_linkinfo, "input")
        all = ET.SubElement(input, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid.text = kwargs.pop('linkinfo_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_domain_reachable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_domain_reachable = ET.SubElement(show_link_info, "linkinfo-domain-reachable")
        linkinfo_domain_reachable.text = kwargs.pop('linkinfo_domain_reachable')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_wwn = ET.SubElement(show_link_info, "linkinfo-wwn")
        linkinfo_wwn.text = kwargs.pop('linkinfo_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_version = ET.SubElement(show_link_info, "linkinfo-version")
        linkinfo_version.text = kwargs.pop('linkinfo_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isl_linknumber(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber.text = kwargs.pop('linkinfo_isl_linknumber')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destdomain(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destdomain = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destdomain")
        linkinfo_isllink_destdomain.text = kwargs.pop('linkinfo_isllink_destdomain')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_srcport = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport")
        linkinfo_isllink_srcport.text = kwargs.pop('linkinfo_isllink_srcport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_srcport_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport-type")
        linkinfo_isllink_srcport_type.text = kwargs.pop('linkinfo_isllink_srcport_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_srcport_interface = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport-interface")
        linkinfo_isllink_srcport_interface.text = kwargs.pop('linkinfo_isllink_srcport_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destport = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport")
        linkinfo_isllink_destport.text = kwargs.pop('linkinfo_isllink_destport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destport_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport-type")
        linkinfo_isllink_destport_type.text = kwargs.pop('linkinfo_isllink_destport_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destport_interface = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport-interface")
        linkinfo_isllink_destport_interface.text = kwargs.pop('linkinfo_isllink_destport_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isl_linkcost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isl_linkcost = ET.SubElement(linkinfo_isl, "linkinfo-isl-linkcost")
        linkinfo_isl_linkcost.text = kwargs.pop('linkinfo_isl_linkcost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_costcount(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_costcount = ET.SubElement(linkinfo_isl, "linkinfo-isllink-costcount")
        linkinfo_isllink_costcount.text = kwargs.pop('linkinfo_isllink_costcount')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-type")
        linkinfo_isllink_type.text = kwargs.pop('linkinfo_isllink_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_trunked(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_trunked = ET.SubElement(linkinfo_isl, "linkinfo-trunked")
        linkinfo_trunked.text = kwargs.pop('linkinfo_trunked')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        input = ET.SubElement(show_portindex_interface_info, "input")
        all = ET.SubElement(input, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_portsgroup_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid.text = kwargs.pop('portsgroup_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        port_index = ET.SubElement(show_portindex, "port-index")
        port_index.text = kwargs.pop('port_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        port_index_key = ET.SubElement(show_portindex, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_type = ET.SubElement(show_portindex, "port-type")
        port_type.text = kwargs.pop('port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        port_index_key = ET.SubElement(show_portindex, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_interface = ET.SubElement(show_portindex, "port-interface")
        port_interface.text = kwargs.pop('port_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        input = ET.SubElement(show_fibrechannel_interface_info, "input")
        all = ET.SubElement(input, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_portsgroup_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid.text = kwargs.pop('portsgroup_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_interface = ET.SubElement(show_fibrechannel_info, "port-interface")
        port_interface.text = kwargs.pop('port_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index.text = kwargs.pop('port_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_type = ET.SubElement(show_fibrechannel_info, "port-type")
        port_type.text = kwargs.pop('port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_wwn = ET.SubElement(show_fibrechannel_info, "port-wwn")
        port_wwn.text = kwargs.pop('port_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_remote_port_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        remote_port_wwn = ET.SubElement(show_fibrechannel_info, "remote-port-wwn")
        remote_port_wwn.text = kwargs.pop('remote_port_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_remote_node_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        remote_node_wwn = ET.SubElement(show_fibrechannel_info, "remote-node-wwn")
        remote_node_wwn.text = kwargs.pop('remote_node_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_state = ET.SubElement(show_fibrechannel_info, "port-state")
        port_state.text = kwargs.pop('port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_status = ET.SubElement(show_fibrechannel_info, "port-status")
        port_status.text = kwargs.pop('port_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_status_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_status_message = ET.SubElement(show_fibrechannel_info, "port-status-message")
        port_status_message.text = kwargs.pop('port_status_message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_health(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_health = ET.SubElement(show_fibrechannel_info, "port-health")
        port_health.text = kwargs.pop('port_health')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_trunked(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_trunked = ET.SubElement(show_fibrechannel_info, "port-trunked")
        port_trunked.text = kwargs.pop('port_trunked')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_trunk_master(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_trunk_master = ET.SubElement(show_fibrechannel_info, "port-trunk-master")
        port_trunk_master.text = kwargs.pop('port_trunk_master')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_actual_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_actual_distance = ET.SubElement(show_fibrechannel_info, "port-actual-distance")
        port_actual_distance.text = kwargs.pop('port_actual_distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_desired_credit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_desired_credit = ET.SubElement(show_fibrechannel_info, "port-desired-credit")
        port_desired_credit.text = kwargs.pop('port_desired_credit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_buffer_allocated(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_buffer_allocated = ET.SubElement(show_fibrechannel_info, "port-buffer-allocated")
        port_buffer_allocated.text = kwargs.pop('port_buffer_allocated')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_licensed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_licensed = ET.SubElement(show_fibrechannel_info, "port-licensed")
        port_licensed.text = kwargs.pop('port_licensed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_address = ET.SubElement(show_fibrechannel_info, "port-address")
        port_address.text = kwargs.pop('port_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_fec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_fec = ET.SubElement(show_fibrechannel_info, "port-fec")
        port_fec.text = kwargs.pop('port_fec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_configured_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_configured_speed = ET.SubElement(show_fibrechannel_info, "port-configured-speed")
        port_configured_speed.text = kwargs.pop('port_configured_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_actual_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_actual_speed = ET.SubElement(show_fibrechannel_info, "port-actual-speed")
        port_actual_speed.text = kwargs.pop('port_actual_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_input_rbridge_id_or_all_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        input = ET.SubElement(show_fabric_trunk_info, "input")
        rbridge_id_or_all = ET.SubElement(input, "rbridge-id-or-all")
        rbridge_id = ET.SubElement(rbridge_id_or_all, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_input_rbridge_id_or_all_all_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        input = ET.SubElement(show_fabric_trunk_info, "input")
        rbridge_id_or_all = ET.SubElement(input, "rbridge-id-or-all")
        all = ET.SubElement(rbridge_id_or_all, "all")
        all = ET.SubElement(all, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_group = ET.SubElement(trunk_list_groups, "trunk-list-group")
        trunk_list_group.text = kwargs.pop('trunk_list_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_src_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_src_port = ET.SubElement(trunk_list_member, "trunk-list-src-port")
        trunk_list_src_port.text = kwargs.pop('trunk_list_src_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_interface_type = ET.SubElement(trunk_list_member, "trunk-list-interface-type")
        trunk_list_interface_type.text = kwargs.pop('trunk_list_interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_src_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_src_interface = ET.SubElement(trunk_list_member, "trunk-list-src-interface")
        trunk_list_src_interface.text = kwargs.pop('trunk_list_src_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_nbr_rbridge_id = ET.SubElement(trunk_list_member, "trunk-list-nbr-rbridge-id")
        trunk_list_nbr_rbridge_id.text = kwargs.pop('trunk_list_nbr_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_nbr_port = ET.SubElement(trunk_list_member, "trunk-list-nbr-port")
        trunk_list_nbr_port.text = kwargs.pop('trunk_list_nbr_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_nbr_wwn = ET.SubElement(trunk_list_member, "trunk-list-nbr-wwn")
        trunk_list_nbr_wwn.text = kwargs.pop('trunk_list_nbr_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_is_primary(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_is_primary = ET.SubElement(trunk_list_member, "trunk-list-is-primary")
        trunk_list_is_primary.text = kwargs.pop('trunk_list_is_primary')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fabric_route_mcast_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fabric = ET.SubElement(config, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
        route = ET.SubElement(fabric, "route")
        mcast = ET.SubElement(route, "mcast")
        rbridge_id = ET.SubElement(mcast, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fabric_route_mcast_rbridge_id_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fabric = ET.SubElement(config, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
        route = ET.SubElement(fabric, "route")
        mcast = ET.SubElement(route, "mcast")
        rbridge_id = ET.SubElement(mcast, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        priority = ET.SubElement(rbridge_id, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        input = ET.SubElement(show_linkinfo, "input")
        all = ET.SubElement(input, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid.text = kwargs.pop('linkinfo_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_domain_reachable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_domain_reachable = ET.SubElement(show_link_info, "linkinfo-domain-reachable")
        linkinfo_domain_reachable.text = kwargs.pop('linkinfo_domain_reachable')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_wwn = ET.SubElement(show_link_info, "linkinfo-wwn")
        linkinfo_wwn.text = kwargs.pop('linkinfo_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_version = ET.SubElement(show_link_info, "linkinfo-version")
        linkinfo_version.text = kwargs.pop('linkinfo_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isl_linknumber(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber.text = kwargs.pop('linkinfo_isl_linknumber')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destdomain(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destdomain = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destdomain")
        linkinfo_isllink_destdomain.text = kwargs.pop('linkinfo_isllink_destdomain')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_srcport = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport")
        linkinfo_isllink_srcport.text = kwargs.pop('linkinfo_isllink_srcport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_srcport_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport-type")
        linkinfo_isllink_srcport_type.text = kwargs.pop('linkinfo_isllink_srcport_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_srcport_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_srcport_interface = ET.SubElement(linkinfo_isl, "linkinfo-isllink-srcport-interface")
        linkinfo_isllink_srcport_interface.text = kwargs.pop('linkinfo_isllink_srcport_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destport = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport")
        linkinfo_isllink_destport.text = kwargs.pop('linkinfo_isllink_destport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destport_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport-type")
        linkinfo_isllink_destport_type.text = kwargs.pop('linkinfo_isllink_destport_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_destport_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_destport_interface = ET.SubElement(linkinfo_isl, "linkinfo-isllink-destport-interface")
        linkinfo_isllink_destport_interface.text = kwargs.pop('linkinfo_isllink_destport_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isl_linkcost(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isl_linkcost = ET.SubElement(linkinfo_isl, "linkinfo-isl-linkcost")
        linkinfo_isl_linkcost.text = kwargs.pop('linkinfo_isl_linkcost')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_costcount(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_costcount = ET.SubElement(linkinfo_isl, "linkinfo-isllink-costcount")
        linkinfo_isllink_costcount.text = kwargs.pop('linkinfo_isllink_costcount')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_isllink_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_isllink_type = ET.SubElement(linkinfo_isl, "linkinfo-isllink-type")
        linkinfo_isllink_type.text = kwargs.pop('linkinfo_isllink_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_linkinfo_output_show_link_info_linkinfo_isl_linkinfo_trunked(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_linkinfo = ET.Element("show_linkinfo")
        config = show_linkinfo
        output = ET.SubElement(show_linkinfo, "output")
        show_link_info = ET.SubElement(output, "show-link-info")
        linkinfo_rbridgeid_key = ET.SubElement(show_link_info, "linkinfo-rbridgeid")
        linkinfo_rbridgeid_key.text = kwargs.pop('linkinfo_rbridgeid')
        linkinfo_isl = ET.SubElement(show_link_info, "linkinfo-isl")
        linkinfo_isl_linknumber_key = ET.SubElement(linkinfo_isl, "linkinfo-isl-linknumber")
        linkinfo_isl_linknumber_key.text = kwargs.pop('linkinfo_isl_linknumber')
        linkinfo_trunked = ET.SubElement(linkinfo_isl, "linkinfo-trunked")
        linkinfo_trunked.text = kwargs.pop('linkinfo_trunked')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        input = ET.SubElement(show_portindex_interface_info, "input")
        all = ET.SubElement(input, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_portsgroup_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid.text = kwargs.pop('portsgroup_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        port_index = ET.SubElement(show_portindex, "port-index")
        port_index.text = kwargs.pop('port_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        port_index_key = ET.SubElement(show_portindex, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_type = ET.SubElement(show_portindex, "port-type")
        port_type.text = kwargs.pop('port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_portindex_interface_info_output_show_portindex_interface_show_portindex_port_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_portindex_interface_info = ET.Element("show_portindex_interface_info")
        config = show_portindex_interface_info
        output = ET.SubElement(show_portindex_interface_info, "output")
        show_portindex_interface = ET.SubElement(output, "show-portindex-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_portindex_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_portindex = ET.SubElement(show_portindex_interface, "show-portindex")
        port_index_key = ET.SubElement(show_portindex, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_interface = ET.SubElement(show_portindex, "port-interface")
        port_interface.text = kwargs.pop('port_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_input_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        input = ET.SubElement(show_fibrechannel_interface_info, "input")
        all = ET.SubElement(input, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_portsgroup_rbridgeid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid.text = kwargs.pop('portsgroup_rbridgeid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_interface = ET.SubElement(show_fibrechannel_info, "port-interface")
        port_interface.text = kwargs.pop('port_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index.text = kwargs.pop('port_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_type = ET.SubElement(show_fibrechannel_info, "port-type")
        port_type.text = kwargs.pop('port_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_wwn = ET.SubElement(show_fibrechannel_info, "port-wwn")
        port_wwn.text = kwargs.pop('port_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_remote_port_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        remote_port_wwn = ET.SubElement(show_fibrechannel_info, "remote-port-wwn")
        remote_port_wwn.text = kwargs.pop('remote_port_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_remote_node_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        remote_node_wwn = ET.SubElement(show_fibrechannel_info, "remote-node-wwn")
        remote_node_wwn.text = kwargs.pop('remote_node_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_state = ET.SubElement(show_fibrechannel_info, "port-state")
        port_state.text = kwargs.pop('port_state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_status = ET.SubElement(show_fibrechannel_info, "port-status")
        port_status.text = kwargs.pop('port_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_status_message(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_status_message = ET.SubElement(show_fibrechannel_info, "port-status-message")
        port_status_message.text = kwargs.pop('port_status_message')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_health(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_health = ET.SubElement(show_fibrechannel_info, "port-health")
        port_health.text = kwargs.pop('port_health')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_trunked(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_trunked = ET.SubElement(show_fibrechannel_info, "port-trunked")
        port_trunked.text = kwargs.pop('port_trunked')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_trunk_master(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_trunk_master = ET.SubElement(show_fibrechannel_info, "port-trunk-master")
        port_trunk_master.text = kwargs.pop('port_trunk_master')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_actual_distance(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_actual_distance = ET.SubElement(show_fibrechannel_info, "port-actual-distance")
        port_actual_distance.text = kwargs.pop('port_actual_distance')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_desired_credit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_desired_credit = ET.SubElement(show_fibrechannel_info, "port-desired-credit")
        port_desired_credit.text = kwargs.pop('port_desired_credit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_buffer_allocated(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_buffer_allocated = ET.SubElement(show_fibrechannel_info, "port-buffer-allocated")
        port_buffer_allocated.text = kwargs.pop('port_buffer_allocated')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_licensed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_licensed = ET.SubElement(show_fibrechannel_info, "port-licensed")
        port_licensed.text = kwargs.pop('port_licensed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_address = ET.SubElement(show_fibrechannel_info, "port-address")
        port_address.text = kwargs.pop('port_address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_fec(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_fec = ET.SubElement(show_fibrechannel_info, "port-fec")
        port_fec.text = kwargs.pop('port_fec')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_configured_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_configured_speed = ET.SubElement(show_fibrechannel_info, "port-configured-speed")
        port_configured_speed.text = kwargs.pop('port_configured_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fibrechannel_interface_info_output_show_fibrechannel_interface_show_fibrechannel_info_port_actual_speed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fibrechannel_interface_info = ET.Element("show_fibrechannel_interface_info")
        config = show_fibrechannel_interface_info
        output = ET.SubElement(show_fibrechannel_interface_info, "output")
        show_fibrechannel_interface = ET.SubElement(output, "show-fibrechannel-interface")
        portsgroup_rbridgeid_key = ET.SubElement(show_fibrechannel_interface, "portsgroup-rbridgeid")
        portsgroup_rbridgeid_key.text = kwargs.pop('portsgroup_rbridgeid')
        show_fibrechannel_info = ET.SubElement(show_fibrechannel_interface, "show-fibrechannel-info")
        port_index_key = ET.SubElement(show_fibrechannel_info, "port-index")
        port_index_key.text = kwargs.pop('port_index')
        port_actual_speed = ET.SubElement(show_fibrechannel_info, "port-actual-speed")
        port_actual_speed.text = kwargs.pop('port_actual_speed')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_input_rbridge_id_or_all_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        input = ET.SubElement(show_fabric_trunk_info, "input")
        rbridge_id_or_all = ET.SubElement(input, "rbridge-id-or-all")
        rbridge_id = ET.SubElement(rbridge_id_or_all, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_input_rbridge_id_or_all_all_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        input = ET.SubElement(show_fabric_trunk_info, "input")
        rbridge_id_or_all = ET.SubElement(input, "rbridge-id-or-all")
        all = ET.SubElement(rbridge_id_or_all, "all")
        all = ET.SubElement(all, "all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_group = ET.SubElement(trunk_list_groups, "trunk-list-group")
        trunk_list_group.text = kwargs.pop('trunk_list_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_src_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_src_port = ET.SubElement(trunk_list_member, "trunk-list-src-port")
        trunk_list_src_port.text = kwargs.pop('trunk_list_src_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_interface_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_interface_type = ET.SubElement(trunk_list_member, "trunk-list-interface-type")
        trunk_list_interface_type.text = kwargs.pop('trunk_list_interface_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_src_interface(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_src_interface = ET.SubElement(trunk_list_member, "trunk-list-src-interface")
        trunk_list_src_interface.text = kwargs.pop('trunk_list_src_interface')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_nbr_rbridge_id = ET.SubElement(trunk_list_member, "trunk-list-nbr-rbridge-id")
        trunk_list_nbr_rbridge_id.text = kwargs.pop('trunk_list_nbr_rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_nbr_port = ET.SubElement(trunk_list_member, "trunk-list-nbr-port")
        trunk_list_nbr_port.text = kwargs.pop('trunk_list_nbr_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_nbr_wwn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_nbr_wwn = ET.SubElement(trunk_list_member, "trunk-list-nbr-wwn")
        trunk_list_nbr_wwn.text = kwargs.pop('trunk_list_nbr_wwn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def show_fabric_trunk_info_output_show_trunk_list_trunk_list_groups_trunk_list_member_trunk_list_is_primary(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        show_fabric_trunk_info = ET.Element("show_fabric_trunk_info")
        config = show_fabric_trunk_info
        output = ET.SubElement(show_fabric_trunk_info, "output")
        show_trunk_list = ET.SubElement(output, "show-trunk-list")
        trunk_list_groups = ET.SubElement(show_trunk_list, "trunk-list-groups")
        trunk_list_member = ET.SubElement(trunk_list_groups, "trunk-list-member")
        trunk_list_is_primary = ET.SubElement(trunk_list_member, "trunk-list-is-primary")
        trunk_list_is_primary.text = kwargs.pop('trunk_list_is_primary')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fabric_route_mcast_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fabric = ET.SubElement(config, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
        route = ET.SubElement(fabric, "route")
        mcast = ET.SubElement(route, "mcast")
        rbridge_id = ET.SubElement(mcast, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fabric_route_mcast_rbridge_id_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fabric = ET.SubElement(config, "fabric", xmlns="urn:brocade.com:mgmt:brocade-fabric-service")
        route = ET.SubElement(fabric, "route")
        mcast = ET.SubElement(route, "mcast")
        rbridge_id = ET.SubElement(mcast, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        priority = ET.SubElement(rbridge_id, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        