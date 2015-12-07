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

from pynos.versions.ver_6.ver_6_0_1.bgp import BGP as BaseBGP
import pynos.utilities


class BGP(BaseBGP):
    """
    The BGP class holds all relevent methods and attributes for the BGP
    capabilities of the NOS device.

    Attributes:
        None
    """
    def bfd(self, **kwargs):
        """Configure BFD for BGP globally.

        Args:
            rbridge_id (str): Rbridge to configure.  (1, 225, etc)
            tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            rx (str): BFD receive interval in milliseconds (300, 500, etc)
            multiplier (str): BFD multiplier.  (3, 7, 5, etc)
            delete (bool): True if BFD configuration should be deleted.
                Default value will be False if not specified.
            get (bool): Get config instead of editing config. (True, False)
            callback (function): A function executed upon completion of the
                 method.  The only parameter passed to `callback` will be the
                 ``ElementTree`` `config`.

        Returns:
            Return value of `callback`.

        Raises:
            KeyError: if `tx`, `rx`, or `multiplier` is not passed.

        Examples:
            >>> import pynos.device
            >>> switches = ['10.24.39.230']
            >>> auth = ('admin', 'password')
            >>> for switch in switches:
            ...    conn = (switch, '22')
            ...    with pynos.device.Device(conn=conn, auth=auth) as dev:
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230')
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', get=True)
            ...        output = dev.bgp.bfd(rx='300', tx='300', multiplier='3',
            ...        rbridge_id='230', delete=True)
        """
        kwargs['min_tx'] = kwargs.pop('tx')
        kwargs['min_rx'] = kwargs.pop('rx')
        kwargs['delete'] = kwargs.pop('delete', False)
        callback = kwargs.pop('callback', self._callback)
        bfd_tx = self._bfd_tx(**kwargs)
        bfd_rx = self._bfd_rx(**kwargs)
        bfd_multiplier = self._bfd_multiplier(**kwargs)
        if kwargs.pop('get', False):
            return self._get_bfd(bfd_tx, bfd_rx, bfd_multiplier)
        config = pynos.utilities.merge_xml(bfd_tx, bfd_rx)
        config = pynos.utilities.merge_xml(config, bfd_multiplier)
        return callback(config)

    def _bfd_tx(self, **kwargs):
        """Return the BFD minimum transmit interval XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            min_tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_'\
            'bfd_interval_min_tx'
        bfd_tx = getattr(self._rbridge, method_name)
        config = bfd_tx(**kwargs)
        if kwargs['delete']:
            tag = 'min-tx'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _bfd_rx(self, **kwargs):
        """Return the BFD minimum receive interval XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            min_rx (str): BFD receive interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_'\
            'bfd_interval_min_rx'
        bfd_rx = getattr(self._rbridge, method_name)
        config = bfd_rx(**kwargs)
        if kwargs['delete']:
            tag = 'min-rx'
            config.find('.//*%s' % tag).set('operation', 'delete')
            pass
        return config

    def _bfd_multiplier(self, **kwargs):
        """Return the BFD multiplier XML.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            min_tx (str): BFD transmit interval in milliseconds (300, 500, etc)
            delete (bool): Remove the configuration if ``True``.

        Returns:
            XML to be passed to the switch.

        Raises:
            None
        """
        method_name = 'rbridge_id_router_router_bgp_router_bgp_attributes_'\
            'bfd_interval_multiplier'
        bfd_multiplier = getattr(self._rbridge, method_name)
        config = bfd_multiplier(**kwargs)
        if kwargs['delete']:
            tag = 'multiplier'
            config.find('.//*%s' % tag).set('operation', 'delete')
        return config

    def _get_bfd(self, tx, rx, multiplier):
        """Get and merge the `bfd` config from global BGP.

        You should not use this method.
        You probably want `BGP.bfd`.

        Args:
            tx: XML document with the XML to get the transmit interval.
            rx: XML document with the XML to get the receive interval.
            multiplier: XML document with the XML to get the interval
                multiplier.

        Returns:
            Merged XML document.

        Raises:
            None
        """
        tx = self._callback(tx, handler='get_config')
        rx = self._callback(rx, handler='get_config')
        multiplier = self._callback(multiplier, handler='get_config')
        tx = pynos.utilities.return_xml(str(tx))
        rx = pynos.utilities.return_xml(str(rx))
        multiplier = pynos.utilities.return_xml(str(multiplier))
        config = pynos.utilities.merge_xml(tx, rx)
        return pynos.utilities.merge_xml(config, multiplier)
