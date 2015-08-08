#!/usr/bin/env python
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


class LLDP(object):
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
        self._callback = callback

    @property
    def neighbors(self):
        """list[dict]: A list of dictionary items describing the operational
        state of LLDP.
        """
        urn = "{urn:brocade.com:mgmt:brocade-lldp-ext}"

        result = []

        request_lldp = ET.Element(
            'get-lldp-neighbor-detail',
            xmlns="urn:brocade.com:mgmt:brocade-lldp-ext"
        )

        lldp_result = self._callback(request_lldp, 'get')

        for item in lldp_result.findall('%slldp-neighbor-detail' % urn):
            local_int_name = item.find('%slocal-interface-name' % urn).text
            local_int_mac = item.find('%slocal-interface-mac' % urn).text
            remote_int_name = item.find('%sremote-interface-name' % urn).text
            remote_int_mac = item.find('%sremote-interface-mac' % urn).text
            remote_chas_id = item.find('%sremote-chassis-id' % urn).text
            try:
                remote_sys_name = item.find('%sremote-system-name' % urn).text
            except AttributeError:
                remote_sys_name = ''

            if 'Fo ' in local_int_name:
                local_int_name = local_int_name.replace(
                    'Fo ',
                    'FortyGigabitEthernet '
                )

            item_results = {'local-int-name': local_int_name,
                            'local-int-mac': local_int_mac,
                            'remote-int-name': remote_int_name,
                            'remote-int-mac': remote_int_mac,
                            'remote-chassis-id': remote_chas_id,
                            'remote-system-name': remote_sys_name}
            result.append(item_results)

        return result
