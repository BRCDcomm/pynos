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
from __future__ import print_function
import xml.etree.ElementTree as ET
import re


def return_xml(element_tree):
    """Return an XML Element.

        Args:
            element_tree (Element): XML Element to be returned.  If sent as a
                ``str``, this function will attempt to convert it to an
                ``Element``.

        Returns:
            Element: An XML Element.

        Raises:
            TypeError: if `element_tree` is not of type ``Element`` and it
                cannot be converted from a ``str``.

        Examples:
            >>> import pynos.utilities
            >>> import xml.etree.ElementTree as ET
            >>> ele = pynos.utilities.return_xml(ET.Element('config'))
            >>> assert isinstance(ele, ET.Element)
            >>> ele = pynos.utilities.return_xml('<config />')
            >>> assert isinstance(ele, ET.Element)
            >>> ele = pynos.utilities.return_xml(
            ... ['hodor']) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            TypeError
    """
    if isinstance(element_tree, ET.Element):
        return element_tree
    try:
        return ET.fromstring(element_tree)
    except TypeError:
        raise TypeError('{} takes either {} or {} type.'
                        .format(repr(return_xml.__name__),
                                repr(str.__name__),
                                repr(ET.Element.__name__)))


def print_xml_string(element_tree):
    """Prints the string representation of an XML Element.

        Args:
            element_tree (Element): XML Element to be returned.  If sent as a
                ``str``, this function will attempt to convert it to an
                ``Element``.

        Returns:
            Element: An XML Element.

        Raises:
            AttributeError: if `element_tree` is not of type ``Element``.

        Examples:
            >>> import pynos.utilities
            >>> import xml.etree.ElementTree as ET
            >>> pynos.utilities.print_xml_string(ET.Element('config'))
            <config />
            >>> pynos.utilities.print_xml_string(
            ... ['hodor']) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
    """
    print(ET.tostring(element_tree))


def valid_vlan_id(vlan_id, extended=True):
    """Validates a VLAN ID.

    Args:
        vlan_id (integer): VLAN ID to validate.  If passed as ``str``, it will
            be cast to ``int``.
        extended (bool): If the VLAN ID range should be considered extended
            for Virtual Fabrics.

    Returns:
        bool: ``True`` if it is a valid VLAN ID.  ``False`` if not.

    Raises:
        None

    Examples:
        >>> import pynos.utilities
        >>> vlan = '565'
        >>> pynos.utilities.valid_vlan_id(vlan)
        True
        >>> extended = False
        >>> vlan = '6789'
        >>> pynos.utilities.valid_vlan_id(vlan, extended=extended)
        False
        >>> pynos.utilities.valid_vlan_id(vlan)
        True
    """
    minimum_vlan_id = 1
    maximum_vlan_id = 4095
    if extended:
        maximum_vlan_id = 8191
    return minimum_vlan_id <= int(vlan_id) <= maximum_vlan_id


def valid_interface(int_type, name):
    if int_type == 'port_channel':
        return valid_port_channel_name(name)
    else:
        return valid_physical_name(name)


def valid_port_channel_name(name):
    return re.search(r'^[0-9]{1,4}$', name) is not None


def valid_physical_name(name):
    return re.search(r'^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}$', name) is not None
