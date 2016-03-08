#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_snmp(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def snmp_server_context_context_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        context = ET.SubElement(snmp_server, "context")
        context_name = ET.SubElement(context, "context-name")
        context_name.text = kwargs.pop('context_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_context_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        context = ET.SubElement(snmp_server, "context")
        context_name_key = ET.SubElement(context, "context-name")
        context_name_key.text = kwargs.pop('context_name')
        vrf_name = ET.SubElement(context, "vrf-name")
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community = ET.SubElement(community, "community")
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        groupname = ET.SubElement(community, "groupname")
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_ipv4_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        ipv4_acl = ET.SubElement(community, "ipv4-acl")
        ipv4_acl.text = kwargs.pop('ipv4_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_ipv6_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        ipv6_acl = ET.SubElement(community, "ipv6-acl")
        ipv6_acl.text = kwargs.pop('ipv6_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username = ET.SubElement(user, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        groupname = ET.SubElement(user, "groupname")
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_auth(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        auth = ET.SubElement(user, "auth")
        auth.text = kwargs.pop('auth')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_auth_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        auth_password = ET.SubElement(user, "auth-password")
        auth_password.text = kwargs.pop('auth_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_priv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        priv = ET.SubElement(user, "priv")
        priv.text = kwargs.pop('priv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_priv_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        priv_password = ET.SubElement(user, "priv-password")
        priv_password.text = kwargs.pop('priv_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_encrypted(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        encrypted = ET.SubElement(user, "encrypted")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_ipv4_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        ipv4_acl = ET.SubElement(user, "ipv4-acl")
        ipv4_acl.text = kwargs.pop('ipv4_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_ipv6_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        ipv6_acl = ET.SubElement(user, "ipv6-acl")
        ipv6_acl.text = kwargs.pop('ipv6_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        hostip = ET.SubElement(v3host, "hostip")
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username = ET.SubElement(v3host, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        udp_port = ET.SubElement(v3host, "udp-port")
        udp_port.text = kwargs.pop('udp_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_notifytype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        notifytype = ET.SubElement(v3host, "notifytype")
        notifytype.text = kwargs.pop('notifytype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_engineid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        engineid = ET.SubElement(v3host, "engineid")
        engineid.text = kwargs.pop('engineid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_severity_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        severity_level = ET.SubElement(v3host, "severity-level")
        severity_level.text = kwargs.pop('severity_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        use_vrf = ET.SubElement(v3host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_source_interface_source_interface_type_loopback_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        source_interface = ET.SubElement(v3host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        loopback = ET.SubElement(source_interface_type, "loopback")
        loopback = ET.SubElement(loopback, "loopback")
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_source_interface_source_interface_type_ve_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        source_interface = ET.SubElement(v3host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        ve = ET.SubElement(source_interface_type, "ve")
        ve = ET.SubElement(ve, "ve")
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        ip = ET.SubElement(host, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        version = ET.SubElement(host, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community = ET.SubElement(host, "community")
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        udp_port = ET.SubElement(host, "udp-port")
        udp_port.text = kwargs.pop('udp_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_severity_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        severity_level = ET.SubElement(host, "severity-level")
        severity_level.text = kwargs.pop('severity_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_source_interface_source_interface_type_loopback_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        source_interface = ET.SubElement(host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        loopback = ET.SubElement(source_interface_type, "loopback")
        loopback = ET.SubElement(loopback, "loopback")
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_source_interface_source_interface_type_ve_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        source_interface = ET.SubElement(host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        ve = ET.SubElement(source_interface_type, "ve")
        ve = ET.SubElement(ve, "ve")
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_contact(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        contact = ET.SubElement(agtconfig, "contact")
        contact.text = kwargs.pop('contact')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_location(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        location = ET.SubElement(agtconfig, "location")
        location.text = kwargs.pop('location')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_sys_descr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        sys_descr = ET.SubElement(agtconfig, "sys-descr")
        sys_descr.text = kwargs.pop('sys_descr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_enable_trap_trap_flag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        enable = ET.SubElement(snmp_server, "enable")
        trap = ET.SubElement(enable, "trap")
        trap_flag = ET.SubElement(trap, "trap-flag")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_engineID_drop_engineID_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        engineID_drop = ET.SubElement(snmp_server, "engineID-drop")
        engineID = ET.SubElement(engineID_drop, "engineID")
        local = ET.SubElement(engineID, "local")
        local.text = kwargs.pop('local')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_viewname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        view = ET.SubElement(snmp_server, "view")
        mibtree_key = ET.SubElement(view, "mibtree")
        mibtree_key.text = kwargs.pop('mibtree')
        viewname = ET.SubElement(view, "viewname")
        viewname.text = kwargs.pop('viewname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_mibtree(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        view = ET.SubElement(snmp_server, "view")
        viewname_key = ET.SubElement(view, "viewname")
        viewname_key.text = kwargs.pop('viewname')
        mibtree = ET.SubElement(view, "mibtree")
        mibtree.text = kwargs.pop('mibtree')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_mibtree_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        view = ET.SubElement(snmp_server, "view")
        viewname_key = ET.SubElement(view, "viewname")
        viewname_key.text = kwargs.pop('viewname')
        mibtree_key = ET.SubElement(view, "mibtree")
        mibtree_key.text = kwargs.pop('mibtree')
        mibtree_access = ET.SubElement(view, "mibtree-access")
        mibtree_access.text = kwargs.pop('mibtree_access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        group_name = ET.SubElement(group, "group-name")
        group_name.text = kwargs.pop('group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version = ET.SubElement(group, "group-version")
        group_version.text = kwargs.pop('group_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_auth_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        group_auth_mode = ET.SubElement(group, "group-auth-mode")
        group_auth_mode.text = kwargs.pop('group_auth_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_read(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        read = ET.SubElement(group, "read")
        read.text = kwargs.pop('read')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_write(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        write = ET.SubElement(group, "write")
        write.text = kwargs.pop('write')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_notify(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        notify = ET.SubElement(group, "notify")
        notify.text = kwargs.pop('notify')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_mib_community_map_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        mib = ET.SubElement(snmp_server, "mib")
        community_map = ET.SubElement(mib, "community-map")
        community = ET.SubElement(community_map, "community")
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_mib_community_map_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        mib = ET.SubElement(snmp_server, "mib")
        community_map = ET.SubElement(mib, "community-map")
        community_key = ET.SubElement(community_map, "community")
        community_key.text = kwargs.pop('community')
        context = ET.SubElement(community_map, "context")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_context_context_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        context = ET.SubElement(snmp_server, "context")
        context_name = ET.SubElement(context, "context-name")
        context_name.text = kwargs.pop('context_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_context_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        context = ET.SubElement(snmp_server, "context")
        context_name_key = ET.SubElement(context, "context-name")
        context_name_key.text = kwargs.pop('context_name')
        vrf_name = ET.SubElement(context, "vrf-name")
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community = ET.SubElement(community, "community")
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        groupname = ET.SubElement(community, "groupname")
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_ipv4_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        ipv4_acl = ET.SubElement(community, "ipv4-acl")
        ipv4_acl.text = kwargs.pop('ipv4_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_community_ipv6_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        community = ET.SubElement(snmp_server, "community")
        community_key = ET.SubElement(community, "community")
        community_key.text = kwargs.pop('community')
        ipv6_acl = ET.SubElement(community, "ipv6-acl")
        ipv6_acl.text = kwargs.pop('ipv6_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username = ET.SubElement(user, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_groupname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        groupname = ET.SubElement(user, "groupname")
        groupname.text = kwargs.pop('groupname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_auth(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        auth = ET.SubElement(user, "auth")
        auth.text = kwargs.pop('auth')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_auth_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        auth_password = ET.SubElement(user, "auth-password")
        auth_password.text = kwargs.pop('auth_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_priv(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        priv = ET.SubElement(user, "priv")
        priv.text = kwargs.pop('priv')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_priv_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        priv_password = ET.SubElement(user, "priv-password")
        priv_password.text = kwargs.pop('priv_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_encrypted(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        encrypted = ET.SubElement(user, "encrypted")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_ipv4_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        ipv4_acl = ET.SubElement(user, "ipv4-acl")
        ipv4_acl.text = kwargs.pop('ipv4_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_user_ipv6_acl(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        user = ET.SubElement(snmp_server, "user")
        username_key = ET.SubElement(user, "username")
        username_key.text = kwargs.pop('username')
        ipv6_acl = ET.SubElement(user, "ipv6-acl")
        ipv6_acl.text = kwargs.pop('ipv6_acl')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        hostip = ET.SubElement(v3host, "hostip")
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username = ET.SubElement(v3host, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        udp_port = ET.SubElement(v3host, "udp-port")
        udp_port.text = kwargs.pop('udp_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_notifytype(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        notifytype = ET.SubElement(v3host, "notifytype")
        notifytype.text = kwargs.pop('notifytype')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_engineid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        engineid = ET.SubElement(v3host, "engineid")
        engineid.text = kwargs.pop('engineid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_severity_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        severity_level = ET.SubElement(v3host, "severity-level")
        severity_level.text = kwargs.pop('severity_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        use_vrf = ET.SubElement(v3host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_source_interface_source_interface_type_loopback_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        source_interface = ET.SubElement(v3host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        loopback = ET.SubElement(source_interface_type, "loopback")
        loopback = ET.SubElement(loopback, "loopback")
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_v3host_source_interface_source_interface_type_ve_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        v3host = ET.SubElement(snmp_server, "v3host")
        hostip_key = ET.SubElement(v3host, "hostip")
        hostip_key.text = kwargs.pop('hostip')
        username_key = ET.SubElement(v3host, "username")
        username_key.text = kwargs.pop('username')
        source_interface = ET.SubElement(v3host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        ve = ET.SubElement(source_interface_type, "ve")
        ve = ET.SubElement(ve, "ve")
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        ip = ET.SubElement(host, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        version = ET.SubElement(host, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community = ET.SubElement(host, "community")
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        udp_port = ET.SubElement(host, "udp-port")
        udp_port.text = kwargs.pop('udp_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_severity_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        severity_level = ET.SubElement(host, "severity-level")
        severity_level.text = kwargs.pop('severity_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_source_interface_source_interface_type_loopback_loopback(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        source_interface = ET.SubElement(host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        loopback = ET.SubElement(source_interface_type, "loopback")
        loopback = ET.SubElement(loopback, "loopback")
        loopback.text = kwargs.pop('loopback')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_host_source_interface_source_interface_type_ve_ve(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        host = ET.SubElement(snmp_server, "host")
        ip_key = ET.SubElement(host, "ip")
        ip_key.text = kwargs.pop('ip')
        community_key = ET.SubElement(host, "community")
        community_key.text = kwargs.pop('community')
        source_interface = ET.SubElement(host, "source-interface")
        source_interface_type = ET.SubElement(source_interface, "source-interface-type")
        ve = ET.SubElement(source_interface_type, "ve")
        ve = ET.SubElement(ve, "ve")
        ve.text = kwargs.pop('ve')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_contact(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        contact = ET.SubElement(agtconfig, "contact")
        contact.text = kwargs.pop('contact')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_location(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        location = ET.SubElement(agtconfig, "location")
        location.text = kwargs.pop('location')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_agtconfig_sys_descr(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        agtconfig = ET.SubElement(snmp_server, "agtconfig")
        sys_descr = ET.SubElement(agtconfig, "sys-descr")
        sys_descr.text = kwargs.pop('sys_descr')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_enable_trap_trap_flag(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        enable = ET.SubElement(snmp_server, "enable")
        trap = ET.SubElement(enable, "trap")
        trap_flag = ET.SubElement(trap, "trap-flag")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_engineID_drop_engineID_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        engineID_drop = ET.SubElement(snmp_server, "engineID-drop")
        engineID = ET.SubElement(engineID_drop, "engineID")
        local = ET.SubElement(engineID, "local")
        local.text = kwargs.pop('local')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_viewname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        view = ET.SubElement(snmp_server, "view")
        mibtree_key = ET.SubElement(view, "mibtree")
        mibtree_key.text = kwargs.pop('mibtree')
        viewname = ET.SubElement(view, "viewname")
        viewname.text = kwargs.pop('viewname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_mibtree(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        view = ET.SubElement(snmp_server, "view")
        viewname_key = ET.SubElement(view, "viewname")
        viewname_key.text = kwargs.pop('viewname')
        mibtree = ET.SubElement(view, "mibtree")
        mibtree.text = kwargs.pop('mibtree')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_view_mibtree_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        view = ET.SubElement(snmp_server, "view")
        viewname_key = ET.SubElement(view, "viewname")
        viewname_key.text = kwargs.pop('viewname')
        mibtree_key = ET.SubElement(view, "mibtree")
        mibtree_key.text = kwargs.pop('mibtree')
        mibtree_access = ET.SubElement(view, "mibtree-access")
        mibtree_access.text = kwargs.pop('mibtree_access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        group_name = ET.SubElement(group, "group-name")
        group_name.text = kwargs.pop('group_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version = ET.SubElement(group, "group-version")
        group_version.text = kwargs.pop('group_version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_group_auth_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        group_auth_mode = ET.SubElement(group, "group-auth-mode")
        group_auth_mode.text = kwargs.pop('group_auth_mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_read(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        read = ET.SubElement(group, "read")
        read.text = kwargs.pop('read')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_write(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        write = ET.SubElement(group, "write")
        write.text = kwargs.pop('write')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_group_notify(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        group = ET.SubElement(snmp_server, "group")
        group_name_key = ET.SubElement(group, "group-name")
        group_name_key.text = kwargs.pop('group_name')
        group_version_key = ET.SubElement(group, "group-version")
        group_version_key.text = kwargs.pop('group_version')
        notify = ET.SubElement(group, "notify")
        notify.text = kwargs.pop('notify')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_mib_community_map_community(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        mib = ET.SubElement(snmp_server, "mib")
        community_map = ET.SubElement(mib, "community-map")
        community = ET.SubElement(community_map, "community")
        community.text = kwargs.pop('community')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def snmp_server_mib_community_map_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        snmp_server = ET.SubElement(config, "snmp-server", xmlns="urn:brocade.com:mgmt:brocade-snmp")
        mib = ET.SubElement(snmp_server, "mib")
        community_map = ET.SubElement(mib, "community-map")
        community_key = ET.SubElement(community_map, "community")
        community_key.text = kwargs.pop('community')
        context = ET.SubElement(community_map, "context")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        