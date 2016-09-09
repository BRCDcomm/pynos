"""
Copyright 2016 Brocade Communications Systems, Inc.

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

from pynos.versions.base.system import System as BaseSystem
from pynos.versions.ver_7.ver_7_1_0.yang.brocade_rbridge import brocade_rbridge
import xml.etree.ElementTree as ET
import pynos.utilities


class System(BaseSystem):
    """System class containing all system level methods and attributes.
    """

    def __init__(self, callback):
        super(System, self).__init__(callback)
        self._rbridge = brocade_rbridge(callback=pynos.utilities.return_xml)

    def maintenance_mode(self, **kwargs):
        """Configures maintenance mode on the device

        Args:
            rbridge_id (str): The rbridge ID of the device on which
            Maintenance mode
                will be configured in a VCS fabric.

            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `rbridge_id` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.202', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.maintenance_mode(rbridge_id='226')
            ...     output = dev.system.maintenance_mode(rbridge_id='226',
            ...     get=True)
            ...     assert output == True
            ...     output = dev.system.maintenance_mode(rbridge_id='226',
            ...     delete=True)
            ...     output = dev.system.maintenance_mode(rbridge_id='226',
            ...     get=True)
            ...     assert output == False
        """
        is_get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        rbridge_id = kwargs.pop('rbridge_id')
        callback = kwargs.pop('callback', self._callback)
        rid_args = dict(rbridge_id=rbridge_id)
        rid = getattr(self._rbridge,
                      'rbridge_id_system_mode_maintenance')
        config = rid(**rid_args)
        if is_get_config:
            maint_mode = callback(config, handler='get_config')
            mode = maint_mode.data_xml
            root = ET.fromstring(mode)
            namespace = 'urn:brocade.com:mgmt:brocade-rbridge'
            for rbridge_id_node in root.findall('{%s}rbridge-id' % namespace):
                system_mode = rbridge_id_node.find(
                    '{%s}system-mode' % namespace)
                if system_mode is not None:
                    return True
                else:
                    return False
        if delete:
            config.find('.//*maintenance').set('operation', 'delete')
        return callback(config)
