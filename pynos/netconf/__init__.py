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
import logging
from ncclient import manager
from ncclient import xml_
from pynos.netconf import interface
from pynos.netconf import bgp
from pynos.netconf import system


class Device(object):
    """
    Device object holds the state for a single NOS device.

    Attributes:
        bgp: BGP related actions and attributes.
        interface: Interface related actions and attributes.
        system: System related actions and attributes.
        lldp_neighbors: List of LLDP neighbors and the connection attributes.
    """
    def __init__(self, conn, auth):
        """
        Args:
            conn: A tuple for the IP/Hostname and port of the VDX device you
                intend to connect to. Ex. ('10.0.0.1', '22')
            auth: A tuple for the username and password of the VDX device you
                intend to connect to. Ex. ('admin', 'password')

        Returns:
            Instance of the device object.
        """
        self._conn = conn
        self._auth = auth
        self._mgr = None

        self.interface = interface.Interface(self._callback)
        self.bgp = bgp.BGP(self._callback)
        self.system = system.System(self._callback)

        self._mgr = manager.connect(host=self._conn[0],
                                    port=self._conn[1],
                                    username=self._auth[0],
                                    password=self._auth[1])
        self._mgr.timeout = 600

    def _callback(self, call, handler='edit_config', target='running',
                  source='startup'):
        """
        Callback for NETCONF calls.

        Args:
            call: An Element Tree element containing the XML of the NETCONF
                call you intend to make to the device.
            handler: Type of ncclient call to make.
                get: ncclient dispatch. For custom RPCs.
                edit_config: NETCONF standard edit.
                delete_config: NETCONF standard delete.
                copy_config: NETCONF standard copy.
            target: Target configuration location for action. Only used for
                edit_config, delete_config, and copy_config.
            source: Source of configuration information for copying
                configuration. Only used for copy_config.

        Returns:
            None

        Raises:
            None
        """
        try:
            call = ET.tostring(call)
            if handler == 'get':
                call_element = xml_.to_ele(call)
                return ET.fromstring(str(self._mgr.dispatch(call_element)))
            if handler == 'edit_config':
                self._mgr.edit_config(target=target, config=call)
            if handler == 'delete_config':
                self._mgr.delete_config(target=target)
            if handler == 'copy_config':
                self._mgr.copy_config(target=target, source=source)
        # TODO: Figure out how this can fail and narrow exception window.
        except Exception, error:
            logging.error(error)

    @property
    def connection(self):
        """
        Poll if object is still connected to device in question.

        Args:
            None

        Returns:
            bool: True if connected, False if not.

        Raises:
            None
        """
        return self._mgr.connected

    def reconnect(self):
        """
        Reconnect session with device.

        Args:
            None

        Returns:
            bool: True if reconnect succeeds, False if not.

        Raises:
            None
        """
        self._mgr = manager.connect(host=self._conn[0],
                                    port=self._conn[1],
                                    username=self._auth[0],
                                    password=self._auth[1])
        self._mgr.timeout = 600

        return True
