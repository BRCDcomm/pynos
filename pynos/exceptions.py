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


class InvalidInterfaceName(Exception):
    """Exception for invalid physical interface names.
    """
    pass


class InvalidInterfaceType(Exception):
    """Exception for invalid interface types.
    """
    pass


class InvalidVlanId(Exception):
    """Exception for invalid VLAN IDs.
    """
    pass


class InvalidPortChannelName(Exception):
    """Exception for invalid port-channel interface names.
    """
    pass


class InvalidState(Exception):
    """Exception for invalid states.
    """
    pass


class InvalidAction(Exception):
    """Exception for invalid actions.
    """
    pass


class InvalidMode(Exception):
    """Exception for invalid modes.
    """
    pass


class PynosException(Exception):
    """Exception for unique PyNOS issues with no more specific exception.
    """
    pass
