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

        Examples:
            >>> import pynos.utilities
            >>> import xml.etree.ElementTree as ET
            >>> pynos.utilities.print_xml_string(ET.Element('config'))
            '<config />'
            >>> ele = pynos.utilities.return_xml(
            ... ['hodor']) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            AttributeError
    """
    print(ET.tostring(element_tree))
