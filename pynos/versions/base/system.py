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
        self._rbridge = brocade_rbridge(callback=pynos.utilities.return_xml)

    @property
    def uptime(self):
        """dict: device uptime
        """
        namespace = 'urn:brocade.com:mgmt:brocade-system'
        get_system_uptime = ET.Element('get-system-uptime', xmlns=namespace)
        results = self._callback(get_system_uptime, handler='get')
        system_uptime = dict(days=results.find('.//{%s}days' % namespace).text,
                             hours=results.find('.//{%s}hours' %
                                                namespace).text,
                             minutes=results.find('.//{%s}minutes' %
                                                  namespace).text,
                             seconds=results.find('.//{%s}seconds' %
                                                  namespace).text)
        return system_uptime

    def chassis_name(self, **kwargs):
        """Get device's chassis name/Model.

        Args:
            rbridge_id (str): The rbridge ID of the device
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `rbridge_id` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.chassis_name(rbridge_id='225')
            ...     assert output == 'VDX6740'
        """
        namespace = "urn:brocade.com:mgmt:brocade-rbridge"
        rbridge_id = kwargs.pop('rbridge_id', '1')
        chassis_name = ' '
        callback = kwargs.pop('callback', self._callback)
        rid_args = dict(rbridge_id=rbridge_id, chassis_name=chassis_name)
        rid = getattr(self._rbridge,
                      'rbridge_id_switch_attributes_chassis_name')
        config = rid(**rid_args)
        output = callback(config, handler='get_config')
        chassis_name = output.data.find('.//{%s}chassis-name' % namespace).text
        return chassis_name

    def router_id(self, **kwargs):
        """Configures device's Router ID.

        Args:
            router_id (str): Router ID for the device.
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            callback (function): A function executed upon completion of the
                method.  The only parameter passed to `callback` will be the
                ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `router_id` is not specified.

        Examples:
            >>> import pynos.device
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.router_id(router_id='10.24.39.211',
            ...     rbridge_id='225')
            ...     dev.system.router_id() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        router_id = kwargs.pop('router_id')
        rbridge_id = kwargs.pop('rbridge_id', '1')
        callback = kwargs.pop('callback', self._callback)
        rid_args = dict(rbridge_id=rbridge_id, router_id=router_id)
        config = self._rbridge.rbridge_id_ip_rtm_config_router_id(**rid_args)
        return callback(config)

    def rbridge_id(self, **kwargs):
        """Configures device's rbridge ID. Setting this property will need
        a switch reboot

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
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
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.rbridge_id(rbridge_id='225')
            ...     output = dev.system.rbridge_id(rbridge_id='225', get=True)
            ...     dev.system.rbridge_id() # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            KeyError
        """
        is_get_config = kwargs.pop('get', False)
        if not is_get_config:
            rbridge_id = kwargs.pop('rbridge_id')
        else:
            rbridge_id = ''
        callback = kwargs.pop('callback', self._callback)
        rid_args = dict(rbridge_id=rbridge_id)
        rid = getattr(self._rbridge,
                      'rbridge_id_rbridge_id')
        config = rid(**rid_args)
        if is_get_config:
            return callback(config, handler='get_config')
        return callback(config)

    def host_name(self, **kwargs):
        """Configures device's host name.

        Args:
            rbridge_id (str): The rbridge ID of the device on which BGP will be
                configured in a VCS fabric.
            host_name (str): The host name of the device.
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
            >>> conn = ('10.24.39.211', '22')
            >>> auth = ('admin', 'password')
            >>> with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...     output = dev.system.host_name(rbridge_id='225',
            ...     host_name='sw0')
            ...     output = dev.system.host_name(rbridge_id='225', get=True)
            ...     try:
            ...         conf = output.data.find('.//{*}host-name').text
            ...     except AttributeError:
            ...         conf = None
            ...     assert conf == 'sw0'
        """
        is_get_config = kwargs.pop('get', False)
        rbridge_id = kwargs.pop('rbridge_id')
        if not is_get_config:
            host_name = kwargs.pop('host_name', 'sw0')
        else:
            host_name = ' '
        callback = kwargs.pop('callback', self._callback)
        rid_args = dict(rbridge_id=rbridge_id, host_name=host_name)
        rid = getattr(self._rbridge,
                      'rbridge_id_switch_attributes_host_name')
        config = rid(**rid_args)
        if is_get_config:
            return callback(config, handler='get_config')
        return callback(config)
