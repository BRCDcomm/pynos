"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import xml.etree.ElementTree as ET
from pynos.versions.base.yang.brocade_rbridge import brocade_rbridge
import pynos.utilities


class Firmware(object):
    """
    System class containing all system level methods and attributes.
    """

    def __init__(self, callback):
        """System init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            System Object

        Raises:
            None
        """
        self._callback = callback
        self._rbridge = brocade_rbridge(callback=pynos.utilities.return_xml)

    def download(self, protocol, host, user, password,
                 file_name, rbridge='all'):
        """
        Download firmware to device
        """
        urn = "{urn:brocade.com:mgmt:brocade-firmware}"
        request_fwdl = self.get_firmware_download_request(protocol, host,
                                                          user, password,
                                                          file_name, rbridge)
        response = self._callback(request_fwdl, 'get')
        fwdl_result = None
        for item in response.findall('%scluster-output' % urn):
            fwdl_result = item.find('%sfwdl-msg' % urn).text
        if not fwdl_result:
            fwdl_result = response.find('%sfwdl-cmd-msg' % urn).text
        return fwdl_result

    def download_status(self, ip_address, session_id=None):
        urn = "{urn:brocade.com:mgmt:brocade-firmware}"
        status_request = ET.Element(
            "fwdl-status", xmlns="urn:brocade.com:mgmt:brocade-firmware")
        response = self._callback(status_request, 'get')
        fwdl_status = ''
        for item in response.findall('%sfwdl-entries' % urn):
            fwdl_status = item.find('%smessage' % urn).text
        return fwdl_status

    @staticmethod
    def get_firmware_download_request(protocol, host, user_name, password,
                                      file_name, rbridge):
        request_ver = ET.Element("firmware-download",
                                 xmlns="urn:brocade.com:mgmt:brocade-firmware")
        protocol = ET.SubElement(request_ver, protocol)
        user = ET.SubElement(protocol, "user")
        user.text = user_name
        passwords = ET.SubElement(protocol, "password")
        passwords.text = password
        host_ip = ET.SubElement(protocol, "host")
        host_ip.text = host
        directory = ET.SubElement(protocol, "directory")
        directory.text = file_name
        rbridge_id = ET.SubElement(request_ver, "rbridge-id")
        rbridge_id.text = rbridge
        ET.SubElement(request_ver, "coldboot")
        return request_ver
