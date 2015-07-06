#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Inc.

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


class System(object):
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

    @property
    def uptime(self):
        """dict: device uptime
        """
        namespace = 'urn:brocade.com:mgmt:brocade-system'
        get_system_uptime = ET.Element('get-system-uptime', xmlns=namespace)
        results = self._callback(get_system_uptime, handler='get')
        system_uptime = dict(days=results.find('{%s}days' % namespace),
                             hours=results.find('{%s}hours' % namespace),
                             minutes=results.find('{%s}minutes' % namespace),
                             seconds=results.find('{%s}seconds' % namespace))
        return system_uptime
