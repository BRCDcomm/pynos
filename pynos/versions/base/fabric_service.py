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


class FabricService(object):
    """
    FabricService class containing all VCS Fabric methods and attributes.
    """

    def __init__(self, callback):
        """FabricService init method.

        Args:
            callback: Callback function that will be called for each action.

        Returns:
            FabricService Object

        Raises:
            None
        """
        self._callback = callback

    @property
    def trill_links(self):
        """dict: trill link details
        """
        urn = "{urn:brocade.com:mgmt:brocade-fabric-service}"
        namespace = 'urn:brocade.com:mgmt:brocade-fabric-service'
        get_links_info = ET.Element('show-linkinfo', xmlns=namespace)
        results = self._callback(get_links_info, handler='get')
        result = []
        for item in results.findall('%sshow-link-info' % urn):
            source_rbridge_id = item.find('%slinkinfo-rbridgeid' % urn).text
            source_switch_wwn = item.find('%slinkinfo-wwn' % urn).text
            for link in item.findall('%slinkinfo-isl' % urn):
                dest_rbridge_id = link.find(
                    '%slinkinfo-isllink-destdomain' % urn).text
                source_interface = link.find(
                    '%slinkinfo-isllink-srcport-interface' % urn).text
                dest_interface = link.find(
                    '%slinkinfo-isllink-destport-interface' % urn).text
                link_cost = link.find('%slinkinfo-isl-linkcost' % urn).text
                link_cost_count = link.find(
                    '%slinkinfo-isllink-costcount' % urn).text

                item_results = {'source-rbridgeid': source_rbridge_id,
                                'source-switch-wwn': source_switch_wwn,
                                'dest-rbridgeid': dest_rbridge_id,
                                'source-interface': source_interface,
                                'dest-interface': dest_interface,
                                'link-cost': link_cost,
                                'link-costcount': link_cost_count}

                result.append(item_results)

        return result
