#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_terminal(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def terminal_cfg_line_sessionid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        terminal_cfg = ET.SubElement(config, "terminal-cfg", xmlns="urn:brocade.com:mgmt:brocade-terminal")
        line = ET.SubElement(terminal_cfg, "line")
        sessionid = ET.SubElement(line, "sessionid")
        sessionid.text = kwargs.pop('sessionid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def terminal_cfg_line_exec_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        terminal_cfg = ET.SubElement(config, "terminal-cfg", xmlns="urn:brocade.com:mgmt:brocade-terminal")
        line = ET.SubElement(terminal_cfg, "line")
        sessionid_key = ET.SubElement(line, "sessionid")
        sessionid_key.text = kwargs.pop('sessionid')
        exec_timeout = ET.SubElement(line, "exec-timeout")
        exec_timeout.text = kwargs.pop('exec_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def terminal_cfg_line_sessionid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        terminal_cfg = ET.SubElement(config, "terminal-cfg", xmlns="urn:brocade.com:mgmt:brocade-terminal")
        line = ET.SubElement(terminal_cfg, "line")
        sessionid = ET.SubElement(line, "sessionid")
        sessionid.text = kwargs.pop('sessionid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def terminal_cfg_line_exec_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        terminal_cfg = ET.SubElement(config, "terminal-cfg", xmlns="urn:brocade.com:mgmt:brocade-terminal")
        line = ET.SubElement(terminal_cfg, "line")
        sessionid_key = ET.SubElement(line, "sessionid")
        sessionid_key.text = kwargs.pop('sessionid')
        exec_timeout = ET.SubElement(line, "exec-timeout")
        exec_timeout.text = kwargs.pop('exec_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        