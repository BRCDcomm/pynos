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
import pynos.utilities

from pynos.versions.base.interface import Interface as InterfaceBase
from pynos.versions.ver_6.ver_6_0_1.yang.brocade_mac_address_table \
    import brocade_mac_address_table


class Interface(InterfaceBase):
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a NOS device.
    Attributes:
        None
    """

    def __init__(self, callback):
        """
        Interface init function.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            Interface Object
        Raises:
            None
        """
        super(Interface, self).__init__(callback)
        self._mac_address_table = brocade_mac_address_table(
            callback=pynos.utilities.return_xml
        )

    def mac_move_detect_enable(self, **kwargs):
        """Enable mac move detect enable on vdx switches
        Args:
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac-move-detect-enable.
                           (True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.mac_move_detect_enable()
            ...     output = dev.interface.mac_move_detect_enable(get=True)
            ...     output = dev.interface.mac_move_detect_enable(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        mac_move = getattr(self._mac_address_table,
                           'mac_address_table_mac_move_mac_move_'
                           'detect_enable')

        config = mac_move()
        if kwargs.pop('get', False):
            output = callback(config, handler='get_config')
            item = output.data.find('.//{*}mac-move-detect-enable')
            if item is not None:
                return True
            else:
                return None
        if kwargs.pop('delete', False):
            config.find('.//*mac-move-detect-enable').set('operation',
                                                          'delete')
        return callback(config)

    def mac_move_limit(self, **kwargs):
        """Configure mac move limit on vdx switches
        Args:
            mac_move_limit: set the limit of mac move limit
            get (bool): Get config instead of editing config. (True, False)
            delete (bool): True, delete the mac move limit.(True, False)
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.
        Returns:
            Return value of `callback`.
        Raises:
            None
        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.interface.mac_move_limit()
            ...     output = dev.interface.mac_move_limit(get=True)
            ...     output = dev.interface.mac_move_limit(delete=True)
        """

        callback = kwargs.pop('callback', self._callback)
        get_config = kwargs.pop('get', False)
        delete = kwargs.pop('delete', False)
        if not get_config:
            if not delete:
                mac_move_limit = kwargs.pop('mac_move_limit')
                mac_move = getattr(self._mac_address_table,
                                   'mac_address_table_mac_move_'
                                   'mac_move_limit')
                config = mac_move(mac_move_limit=mac_move_limit)
            else:
                mac_move = getattr(self._mac_address_table,
                                   'mac_address_table_mac_move_'
                                   'mac_move_limit')
                config = mac_move(mac_move_limit='')
                config.find('.//*mac-move-limit').set('operation',
                                                      'delete')
            return callback(config)

        if get_config:
            mac_move = getattr(self._mac_address_table,
                               'mac_address_table_mac_move_mac'
                               '_move_limit')
            config = mac_move(mac_move_limit='')
            output = callback(config, handler='get_config')
            if output.data.find('.//{*}mac-move-limit') is not None:
                limit = output.data.find('.//{*}mac-move-limit').text
                if limit is not None:
                    return limit
                else:
                    return None
            else:
                limit_default = "20"
                return limit_default
