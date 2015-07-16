#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_nameserver(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_nameserver_detail_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        input = ET.SubElement(get_nameserver_detail, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid.text = kwargs.pop('nameserver_portid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_portname = ET.SubElement(show_nameserver, "nameserver-portname")
        nameserver_portname.text = kwargs.pop('nameserver_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_nodename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_nodename = ET.SubElement(show_nameserver, "nameserver-nodename")
        nameserver_nodename.text = kwargs.pop('nameserver_nodename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_scr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_scr = ET.SubElement(show_nameserver, "nameserver-scr")
        nameserver_scr.text = kwargs.pop('nameserver_scr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_fc4s(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_fc4s = ET.SubElement(show_nameserver, "nameserver-fc4s")
        nameserver_fc4s.text = kwargs.pop('nameserver_fc4s')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portsymb(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_portsymb = ET.SubElement(show_nameserver, "nameserver-portsymb")
        nameserver_portsymb.text = kwargs.pop('nameserver_portsymb')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_nodesymb(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_nodesymb = ET.SubElement(show_nameserver, "nameserver-nodesymb")
        nameserver_nodesymb.text = kwargs.pop('nameserver_nodesymb')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_fabric_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_fabric_portname = ET.SubElement(show_nameserver, "nameserver-fabric-portname")
        nameserver_fabric_portname.text = kwargs.pop('nameserver_fabric_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_permanent_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_permanent_portname = ET.SubElement(show_nameserver, "nameserver-permanent-portname")
        nameserver_permanent_portname.text = kwargs.pop('nameserver_permanent_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_devicetype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_devicetype = ET.SubElement(show_nameserver, "nameserver-devicetype")
        nameserver_devicetype.text = kwargs.pop('nameserver_devicetype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_index = ET.SubElement(show_nameserver, "nameserver-index")
        nameserver_index.text = kwargs.pop('nameserver_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_porttype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_porttype = ET.SubElement(show_nameserver, "nameserver-porttype")
        nameserver_porttype.text = kwargs.pop('nameserver_porttype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_cos = ET.SubElement(show_nameserver, "nameserver-cos")
        nameserver_cos.text = kwargs.pop('nameserver_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_sharearea(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_sharearea = ET.SubElement(show_nameserver, "nameserver-sharearea")
        nameserver_sharearea.text = kwargs.pop('nameserver_sharearea')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_redirect(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_redirect = ET.SubElement(show_nameserver, "nameserver-redirect")
        nameserver_redirect.text = kwargs.pop('nameserver_redirect')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_xlatedomain(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_xlatedomain = ET.SubElement(show_nameserver, "nameserver-xlatedomain")
        nameserver_xlatedomain.text = kwargs.pop('nameserver_xlatedomain')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_connected_via_ag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_connected_via_ag = ET.SubElement(show_nameserver, "nameserver-connected-via-ag")
        nameserver_connected_via_ag.text = kwargs.pop('nameserver_connected_via_ag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_ag_base_device(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_ag_base_device = ET.SubElement(show_nameserver, "nameserver-ag-base-device")
        nameserver_ag_base_device.text = kwargs.pop('nameserver_ag_base_device')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_real(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_real = ET.SubElement(show_nameserver, "nameserver-real")
        nameserver_real.text = kwargs.pop('nameserver_real')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_cascaded(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_cascaded = ET.SubElement(show_nameserver, "nameserver-cascaded")
        nameserver_cascaded.text = kwargs.pop('nameserver_cascaded')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_input_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        input = ET.SubElement(get_nameserver_detail, "input")
        rbridge_id = ET.SubElement(input, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid.text = kwargs.pop('nameserver_portid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_portname = ET.SubElement(show_nameserver, "nameserver-portname")
        nameserver_portname.text = kwargs.pop('nameserver_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_nodename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_nodename = ET.SubElement(show_nameserver, "nameserver-nodename")
        nameserver_nodename.text = kwargs.pop('nameserver_nodename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_scr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_scr = ET.SubElement(show_nameserver, "nameserver-scr")
        nameserver_scr.text = kwargs.pop('nameserver_scr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_fc4s(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_fc4s = ET.SubElement(show_nameserver, "nameserver-fc4s")
        nameserver_fc4s.text = kwargs.pop('nameserver_fc4s')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_portsymb(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_portsymb = ET.SubElement(show_nameserver, "nameserver-portsymb")
        nameserver_portsymb.text = kwargs.pop('nameserver_portsymb')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_nodesymb(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_nodesymb = ET.SubElement(show_nameserver, "nameserver-nodesymb")
        nameserver_nodesymb.text = kwargs.pop('nameserver_nodesymb')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_fabric_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_fabric_portname = ET.SubElement(show_nameserver, "nameserver-fabric-portname")
        nameserver_fabric_portname.text = kwargs.pop('nameserver_fabric_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_permanent_portname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_permanent_portname = ET.SubElement(show_nameserver, "nameserver-permanent-portname")
        nameserver_permanent_portname.text = kwargs.pop('nameserver_permanent_portname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_devicetype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_devicetype = ET.SubElement(show_nameserver, "nameserver-devicetype")
        nameserver_devicetype.text = kwargs.pop('nameserver_devicetype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_index = ET.SubElement(show_nameserver, "nameserver-index")
        nameserver_index.text = kwargs.pop('nameserver_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_porttype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_porttype = ET.SubElement(show_nameserver, "nameserver-porttype")
        nameserver_porttype.text = kwargs.pop('nameserver_porttype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_cos = ET.SubElement(show_nameserver, "nameserver-cos")
        nameserver_cos.text = kwargs.pop('nameserver_cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_sharearea(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_sharearea = ET.SubElement(show_nameserver, "nameserver-sharearea")
        nameserver_sharearea.text = kwargs.pop('nameserver_sharearea')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_redirect(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_redirect = ET.SubElement(show_nameserver, "nameserver-redirect")
        nameserver_redirect.text = kwargs.pop('nameserver_redirect')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_xlatedomain(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_xlatedomain = ET.SubElement(show_nameserver, "nameserver-xlatedomain")
        nameserver_xlatedomain.text = kwargs.pop('nameserver_xlatedomain')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_connected_via_ag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_connected_via_ag = ET.SubElement(show_nameserver, "nameserver-connected-via-ag")
        nameserver_connected_via_ag.text = kwargs.pop('nameserver_connected_via_ag')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_ag_base_device(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_ag_base_device = ET.SubElement(show_nameserver, "nameserver-ag-base-device")
        nameserver_ag_base_device.text = kwargs.pop('nameserver_ag_base_device')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_real(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_real = ET.SubElement(show_nameserver, "nameserver-real")
        nameserver_real.text = kwargs.pop('nameserver_real')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_nameserver_detail_output_show_nameserver_nameserver_cascaded(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_nameserver_detail = ET.Element("get_nameserver_detail")
        config = get_nameserver_detail
        output = ET.SubElement(get_nameserver_detail, "output")
        show_nameserver = ET.SubElement(output, "show-nameserver")
        nameserver_portid_key = ET.SubElement(show_nameserver, "nameserver-portid")
        nameserver_portid_key.text = kwargs.pop('nameserver_portid')
        nameserver_cascaded = ET.SubElement(show_nameserver, "nameserver-cascaded")
        nameserver_cascaded.text = kwargs.pop('nameserver_cascaded')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        