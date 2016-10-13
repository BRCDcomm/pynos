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

from pynos.versions.base.yang.brocade_ras import brocade_ras


class RAS(object):
    """
    RAS class containing all RAS methods and attributes.
    """

    def __init__(self, callback):
        """RAS init method.
        Args:
            callback: Callback function that will be called for each action.
        Returns:
            RAS Object
        Raises:
            None
        """
        self._callback = callback
        self._ras = brocade_ras(callback=pynos.utilities.return_xml)

    def enable_support_autoupload(self, **kwargs):
        """Set Spanning Tree state.

        Args:
            enabled (bool): Is Autoupload enabled? (True, False).
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.
        Examples:
                >>> import pynos.device
                >>> switches = ['10.24.39.211', '10.24.39.203']
                >>> auth = ('admin', 'password')
                >>> for switch in switches:
                ...     conn = (switch, '22')
                ...     with pynos.device.Device(conn=conn, auth=auth) as dev:
                ...         enabled = True
                ...         output = dev.ras.enable_support_autoupload(
                ...         enabled=enabled)
                ...         enabled = False
                ...         output = dev.ras.enable_support_autoupload(
                ...         enabled=enabled)
        """
        enabled = kwargs.pop('enabled')
        callback = kwargs.pop('callback', self._callback)

        if not isinstance(enabled, bool):
            raise ValueError('%s must be `True` or `False`.' % repr(enabled))

        state_args = dict()
        autoupload_state = getattr(self._ras, 'support_autoupload_enable')
        config = autoupload_state(**state_args)
        if not enabled:
            shutdown = config.find('.//*enable')
            shutdown.set('operation', 'delete')
        return callback(config)
