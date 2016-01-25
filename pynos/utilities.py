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
import lxml
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
    """Validates an interface type and name.

    Args:
        int_type (str): Interface type.  Examples: `gigabitethernet`,
            `tengigabitethernet`, `port_channel`.
        name (str): Port designator.  Examples: `225/0/1`, `1/0/1`, `1`.

    Returns:
        bool: ``True`` if it is a valid interface.  ``False`` if not.

    Raises:
        None

    Examples:
        >>> import pynos.utilities
        >>> int_type = 'tengigabitethernet'
        >>> name = '225/0/1'
        >>> pynos.utilities.valid_interface(int_type, name)
        True
        >>> name = '5/0'
        >>> pynos.utilities.valid_interface(int_type, name)
        False
        >>> int_type = 'port_channel'
        >>> name = '1'
        >>> pynos.utilities.valid_interface(int_type, name)
        True
        >>> int_type = 'port_channel'
        >>> name = '1/0'
        >>> pynos.utilities.valid_interface(int_type, name)
        False
    """

    if int_type == 'port_channel':
        return valid_port_channel_name(name)
    else:
        return valid_physical_name(name)


def valid_port_channel_name(name):
    """Validates a Port-Channel.

    Do not use this method directly.  Use ``valid_interface`` instead.

    Args:
        name (str): Port designator.  Examples: `1`, `768`, `3476`.

    Returns:
        bool: ``True`` if it is a valid port-channel.  ``False`` if not.

    Raises:
        None
    """
    return re.search(r'^[0-9]{1,4}$', name) is not None


def valid_physical_name(name):
    """Validates a physical interface.

    Do not use this method directly.  Use ``valid_interface`` instead.

    Args:
        name (str): Port designator.  Examples: `225/0/1`, `1/0/1`.

    Returns:
        bool: ``True`` if it is a valid physical interface.  ``False`` if not.

    Raises:
        None
    """
    pattern = r'^[0-9]{1,3}/[0-9]{1,3}/[0-9]{1,3}(:[1-4])?$'
    return re.search(pattern, name) is not None


def merge_xml(first_doc, second_doc):
    """Merges two XML documents.

    Args:
        first_doc (str): First XML document.  `second_doc` is merged into this
            document.
        second_doc (str): Second XML document.  It is merged into the first.

    Returns:
        XML Document: The merged document.

    Raises:
        None

    Example:
        >>> import pynos.utilities
        >>> import lxml
        >>> import xml
        >>> x = xml.etree.ElementTree.fromstring('<config />')
        >>> y = lxml.etree.fromstring('<config><hello /></config>')
        >>> x = pynos.utilities.merge_xml(x, y)
    """
    # Adapted from:
    # http://stackoverflow.com/questions/27258013/merge-two-xml-files-python
    # Maps each elements tag to the element from the first document
    if isinstance(first_doc, lxml.etree._Element):
        first_doc = ET.fromstring(lxml.etree.tostring(first_doc))
    if isinstance(second_doc, lxml.etree._Element):
        second_doc = ET.fromstring(lxml.etree.tostring(second_doc))
    mapping = {element.tag: element for element in first_doc}
    for element in second_doc:
        if not len(element):
            # Recursed fully.  This element has no children.
            try:
                # Update the first document's element's text
                mapping[element.tag].text = element.text
            except KeyError:
                # The element doesn't exist
                # add it to the mapping and the root document
                mapping[element.tag] = element
                first_doc.append(element)
        else:
            # This element has children.  Recurse.
            try:
                merge_xml(mapping[element.tag], element)
            except KeyError:
                # The element doesn't exist
                # add it to the mapping and the root document
                mapping[element.tag] = element
                first_doc.append(element)
    return lxml.etree.fromstring(ET.tostring(first_doc))
