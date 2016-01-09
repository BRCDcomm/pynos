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
from pynos.versions.ver_7.ver_7_0_0.yang.brocade_lldp_ext \
    import brocade_lldp_ext as brcd_lldp
import pynos.utilities
from pynos.versions.base.lldp import LLDP as BaseLLDP


class LLDP(BaseLLDP):
    """LLDP class containing LLDP methods and attributes.
    """
    def __init__(self, callback):
        """LLDP init method.

        Args:
            callback (function): Callback function that will be called for each
                action.

        Returns:
            LLDP Object

        Raises:
            None
        """
        super(LLDP, self).__init__(callback)
        self._lldp = brcd_lldp(callback=pynos.utilities.return_xml)

    def neighbors(self, **kwargs):

        """list[dict]: A list of dictionary items describing the operational
        state of LLDP.
        """
        urn = "{urn:brocade.com:mgmt:brocade-lldp-ext}"

        result = []
        has_more = ''
        last_ifindex = ''
        rbridge_id = None
        if 'rbridge_id' in kwargs:
            rbridge_id = kwargs.pop('rbridge_id')
        while (has_more == '') or (has_more == 'true'):
            request_lldp = self.get_lldp_neighbors_request(last_ifindex,
                                                           rbridge_id)
            lldp_result = self._callback(request_lldp, 'get')
            has_more = lldp_result.find('%shas-more' % urn).text

            for item in lldp_result.findall('%slldp-neighbor-detail' % urn):
                local_int_name = item.find('%slocal-interface-name' % urn).text
                local_int_mac = item.find('%slocal-interface-mac' % urn).text
                last_ifindex = item.find(
                    '%slocal-interface-ifindex' % urn).text
                remote_int_name = item.find(
                    '%sremote-interface-name' % urn).text
                remote_int_mac = item.find('%sremote-interface-mac' % urn).text
                remote_chas_id = item.find('%sremote-chassis-id' % urn).text
                try:
                    remote_sys_name = item.find(
                        '%sremote-system-name' % urn).text
                except AttributeError:
                    remote_sys_name = ''
                try:
                    remote_sys_desc = item.find('%sremote-system-description' %
                                                urn).text
                except AttributeError:
                    remote_sys_desc = ''
                try:
                    remote_mgmt_addr = item.find(
                        '%sremote-management-address' %
                        urn).text
                except AttributeError:
                    remote_mgmt_addr = ''
                if 'Fo ' in local_int_name:
                    local_int_name = local_int_name.replace(
                        'Fo ',
                        'FortyGigabitEthernet '
                    )
                if 'Te ' in local_int_name:
                    local_int_name = local_int_name.replace(
                        'Te ',
                        'TenGigabitEthernet '
                    )

                item_results = {'local-int-name': local_int_name,
                                'local-int-mac': local_int_mac,
                                'remote-int-name': remote_int_name,
                                'remote-int-mac': remote_int_mac,
                                'remote-chassis-id': remote_chas_id,
                                'remote-system-name': remote_sys_name,
                                'remote-system-description': remote_sys_desc,
                                'remote-management-address': remote_mgmt_addr}
                result.append(item_results)

        return result

    @staticmethod
    def get_lldp_neighbors_request(last_ifindex, rbridge_id):
        """ Creates a new Netconf request based on the last received or if
        rbridge_id is specifed
        ifindex when the hasMore flag is true
        """

        request_lldp = ET.Element(
            'get-lldp-neighbor-detail',
            xmlns="urn:brocade.com:mgmt:brocade-lldp-ext"
        )
        if rbridge_id is not None:
            rbridge_el = ET.SubElement(request_lldp, "rbridge-id")
            rbridge_el.text = rbridge_id
        elif last_ifindex != '':
            last_received_int = ET.SubElement(request_lldp,
                                              "last-rcvd-ifindex")
            last_received_int.text = last_ifindex

        return request_lldp
