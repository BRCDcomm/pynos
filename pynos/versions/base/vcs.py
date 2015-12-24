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


class VCS(object):
    """
    VCS class containing all VCS methods and attributes.
    """

    def __init__(self, callback):
        """VCS init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            VCS Object

        Raises:
            None
        """
        self._callback = callback

    @property
    def vcs_nodes(self):
        """dict: vcs node details
        """
        urn = "{urn:brocade.com:mgmt:brocade-vcs}"
        namespace = 'urn:brocade.com:mgmt:brocade-vcs'
        show_vcs = ET.Element('show-vcs', xmlns=namespace)
        results = self._callback(show_vcs, handler='get')
        result = []
        for nodes in results.findall('%svcs-nodes' % urn):
            for item in nodes.findall('%svcs-node-info' % urn):
                serial_number = item.find('%snode-serial-num' % urn).text
                node_status = item.find('%snode-status' % urn).text
                vcs_id = item.find('%snode-vcs-id' % urn).text
                rbridge_id = item.find('%snode-rbridge-id' % urn).text
                switch_mac = item.find('%snode-switch-mac' % urn).text
                switch_wwn = item.find('%snode-switch-wwn' % urn).text
                switch_name = item.find('%snode-switchname' % urn).text
                node_is_principal = item.find('%snode-is-principal' % urn).text
                switch_ip = ''
                for switch_ip_addr in item.findall(
                        '%snode-public-ip-addresses' % urn):
                    switch_ip = switch_ip_addr.find(
                        '%snode-public-ip-address' % urn).text
                    break
                item_results = {'node-serial-num': serial_number,
                                'node-status': node_status,
                                'node-vcs-id': vcs_id,
                                'node-rbridge-id': rbridge_id,
                                'node-switch-mac': switch_mac,
                                'node-switch-wwn': switch_wwn,
                                'node-switch-ip': switch_ip,
                                'node-switchname': switch_name,
                                'node-is-principal': node_is_principal}

                result.append(item_results)

        return result
