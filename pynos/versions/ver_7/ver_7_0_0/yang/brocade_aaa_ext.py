#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_aaa_ext(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def user_session_info_output_user_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        user_session_info = ET.Element("user_session_info")
        config = user_session_info
        output = ET.SubElement(user_session_info, "output")
        user_role = ET.SubElement(output, "user-role")
        user_role.text = kwargs.pop('user_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def user_session_info_output_user_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        user_session_info = ET.Element("user_session_info")
        config = user_session_info
        output = ET.SubElement(user_session_info, "output")
        user_role = ET.SubElement(output, "user-role")
        user_role.text = kwargs.pop('user_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        