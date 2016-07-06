#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_notification_stream(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def BGPSessionState_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_BGPPeerIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        BGPPeerIpAddress = ET.SubElement(BGPSessionState, "BGPPeerIpAddress")
        BGPPeerIpAddress.text = kwargs.pop('BGPPeerIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_BGPPeerState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        BGPPeerState = ET.SubElement(BGPSessionState, "BGPPeerState")
        BGPPeerState.text = kwargs.pop('BGPPeerState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_BGPNeighborIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        BGPNeighborIpAddress = ET.SubElement(BGPNeighborPrefixExceeded, "BGPNeighborIpAddress")
        BGPNeighborIpAddress.text = kwargs.pop('BGPNeighborIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_neighborPrefixLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        neighborPrefixLimit = ET.SubElement(BGPNeighborPrefixExceeded, "neighborPrefixLimit")
        neighborPrefixLimit.text = kwargs.pop('neighborPrefixLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_RIBRouteLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        RIBRouteLimit = ET.SubElement(RIBSystemRouteLimitExceeded, "RIBRouteLimit")
        RIBRouteLimit.text = kwargs.pop('RIBRouteLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_RIBNextHopLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        RIBNextHopLimit = ET.SubElement(RIBNextHopLimitExceeded, "RIBNextHopLimit")
        RIBNextHopLimit.text = kwargs.pop('RIBNextHopLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_TunnelDestinationIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        TunnelDestinationIpAddress = ET.SubElement(VxLANTunnelState, "TunnelDestinationIpAddress")
        TunnelDestinationIpAddress.text = kwargs.pop('TunnelDestinationIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_TunnelState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        TunnelState = ET.SubElement(VxLANTunnelState, "TunnelState")
        TunnelState.text = kwargs.pop('TunnelState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_OSPFNeighborIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        OSPFNeighborIpAddress = ET.SubElement(OSPFNeighborState, "OSPFNeighborIpAddress")
        OSPFNeighborIpAddress.text = kwargs.pop('OSPFNeighborIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_NeighborState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        NeighborState = ET.SubElement(OSPFNeighborState, "NeighborState")
        NeighborState.text = kwargs.pop('NeighborState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_NewMasterIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        NewMasterIpAddress = ET.SubElement(VRRPNewMaster, "NewMasterIpAddress")
        NewMasterIpAddress.text = kwargs.pop('NewMasterIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_VRRPSessionId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        VRRPSessionId = ET.SubElement(VRRPNewMaster, "VRRPSessionId")
        VRRPSessionId.text = kwargs.pop('VRRPSessionId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_VRFName(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        VRFName = ET.SubElement(RIBVRFRouteLimitExceeded, "VRFName")
        VRFName.text = kwargs.pop('VRFName')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_RIBVRFRouteLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        RIBVRFRouteLimit = ET.SubElement(RIBVRFRouteLimitExceeded, "RIBVRFRouteLimit")
        RIBVRFRouteLimit.text = kwargs.pop('RIBVRFRouteLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_ARPLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        ARPLimit = ET.SubElement(ARPLimitExceeded, "ARPLimit")
        ARPLimit.text = kwargs.pop('ARPLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_NDLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        NDLimit = ET.SubElement(NDLimitExceeded, "NDLimit")
        NDLimit.text = kwargs.pop('NDLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPSessionState, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_BGPPeerIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        BGPPeerIpAddress = ET.SubElement(BGPSessionState, "BGPPeerIpAddress")
        BGPPeerIpAddress.text = kwargs.pop('BGPPeerIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPSessionState_BGPPeerState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPSessionState = ET.SubElement(config, "BGPSessionState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        BGPPeerState = ET.SubElement(BGPSessionState, "BGPPeerState")
        BGPPeerState.text = kwargs.pop('BGPPeerState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(BGPNeighborPrefixExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_BGPNeighborIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        BGPNeighborIpAddress = ET.SubElement(BGPNeighborPrefixExceeded, "BGPNeighborIpAddress")
        BGPNeighborIpAddress.text = kwargs.pop('BGPNeighborIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def BGPNeighborPrefixExceeded_neighborPrefixLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        BGPNeighborPrefixExceeded = ET.SubElement(config, "BGPNeighborPrefixExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        neighborPrefixLimit = ET.SubElement(BGPNeighborPrefixExceeded, "neighborPrefixLimit")
        neighborPrefixLimit.text = kwargs.pop('neighborPrefixLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBSystemRouteLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBSystemRouteLimitExceeded_RIBRouteLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBSystemRouteLimitExceeded = ET.SubElement(config, "RIBSystemRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        RIBRouteLimit = ET.SubElement(RIBSystemRouteLimitExceeded, "RIBRouteLimit")
        RIBRouteLimit.text = kwargs.pop('RIBRouteLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBNextHopLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBNextHopLimitExceeded_RIBNextHopLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBNextHopLimitExceeded = ET.SubElement(config, "RIBNextHopLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        RIBNextHopLimit = ET.SubElement(RIBNextHopLimitExceeded, "RIBNextHopLimit")
        RIBNextHopLimit.text = kwargs.pop('RIBNextHopLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VxLANTunnelState, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_TunnelDestinationIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        TunnelDestinationIpAddress = ET.SubElement(VxLANTunnelState, "TunnelDestinationIpAddress")
        TunnelDestinationIpAddress.text = kwargs.pop('TunnelDestinationIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VxLANTunnelState_TunnelState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VxLANTunnelState = ET.SubElement(config, "VxLANTunnelState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        TunnelState = ET.SubElement(VxLANTunnelState, "TunnelState")
        TunnelState.text = kwargs.pop('TunnelState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(OSPFNeighborState, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_OSPFNeighborIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        OSPFNeighborIpAddress = ET.SubElement(OSPFNeighborState, "OSPFNeighborIpAddress")
        OSPFNeighborIpAddress.text = kwargs.pop('OSPFNeighborIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def OSPFNeighborState_NeighborState(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        OSPFNeighborState = ET.SubElement(config, "OSPFNeighborState", xmlns="http://brocade.com/ns/brocade-notification-stream")
        NeighborState = ET.SubElement(OSPFNeighborState, "NeighborState")
        NeighborState.text = kwargs.pop('NeighborState')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(VRRPNewMaster, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_NewMasterIpAddress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        NewMasterIpAddress = ET.SubElement(VRRPNewMaster, "NewMasterIpAddress")
        NewMasterIpAddress.text = kwargs.pop('NewMasterIpAddress')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def VRRPNewMaster_VRRPSessionId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        VRRPNewMaster = ET.SubElement(config, "VRRPNewMaster", xmlns="http://brocade.com/ns/brocade-notification-stream")
        VRRPSessionId = ET.SubElement(VRRPNewMaster, "VRRPSessionId")
        VRRPSessionId.text = kwargs.pop('VRRPSessionId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(RIBVRFRouteLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_VRFName(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        VRFName = ET.SubElement(RIBVRFRouteLimitExceeded, "VRFName")
        VRFName.text = kwargs.pop('VRFName')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def RIBVRFRouteLimitExceeded_RIBVRFRouteLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        RIBVRFRouteLimitExceeded = ET.SubElement(config, "RIBVRFRouteLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        RIBVRFRouteLimit = ET.SubElement(RIBVRFRouteLimitExceeded, "RIBVRFRouteLimit")
        RIBVRFRouteLimit.text = kwargs.pop('RIBVRFRouteLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(ARPLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ARPLimitExceeded_ARPLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ARPLimitExceeded = ET.SubElement(config, "ARPLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        ARPLimit = ET.SubElement(ARPLimitExceeded, "ARPLimit")
        ARPLimit.text = kwargs.pop('ARPLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchIdentifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchIdentifier = ET.SubElement(originator_switch_info, "switchIdentifier")
        switchIdentifier.text = kwargs.pop('switchIdentifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchVcsId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchVcsId = ET.SubElement(originator_switch_info, "switchVcsId")
        switchVcsId.text = kwargs.pop('switchVcsId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchIpV4Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchIpV4Address = ET.SubElement(originator_switch_info, "switchIpV4Address")
        switchIpV4Address.text = kwargs.pop('switchIpV4Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_originator_switch_info_switchIpV6Address(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        originator_switch_info = ET.SubElement(NDLimitExceeded, "originator-switch-info")
        switchIpV6Address = ET.SubElement(originator_switch_info, "switchIpV6Address")
        switchIpV6Address.text = kwargs.pop('switchIpV6Address')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def NDLimitExceeded_NDLimit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        NDLimitExceeded = ET.SubElement(config, "NDLimitExceeded", xmlns="http://brocade.com/ns/brocade-notification-stream")
        NDLimit = ET.SubElement(NDLimitExceeded, "NDLimit")
        NDLimit.text = kwargs.pop('NDLimit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        