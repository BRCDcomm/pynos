#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_aaa(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def aaa_config_aaa_authentication_login_first(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        authentication = ET.SubElement(aaa, "authentication")
        login = ET.SubElement(authentication, "login")
        first = ET.SubElement(login, "first")
        first.text = kwargs.pop('first')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_authentication_login_second(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        authentication = ET.SubElement(aaa, "authentication")
        login = ET.SubElement(authentication, "login")
        second = ET.SubElement(login, "second")
        second.text = kwargs.pop('second')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_accounting_exec_defaultacc_start_stop_server_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        accounting = ET.SubElement(aaa, "accounting")
        exec_el = ET.SubElement(accounting, "exec")
        defaultacc = ET.SubElement(exec_el, "defaultacc")
        start_stop = ET.SubElement(defaultacc, "start-stop")
        server_type = ET.SubElement(start_stop, "server-type")
        server_type.text = kwargs.pop('server_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_accounting_commands_defaultacc_start_stop_server_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        accounting = ET.SubElement(aaa, "accounting")
        commands = ET.SubElement(accounting, "commands")
        defaultacc = ET.SubElement(commands, "defaultacc")
        start_stop = ET.SubElement(defaultacc, "start-stop")
        server_type = ET.SubElement(start_stop, "server-type")
        server_type.text = kwargs.pop('server_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name = ET.SubElement(username, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_user_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        user_password = ET.SubElement(username, "user-password")
        user_password.text = kwargs.pop('user_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        encryption_level = ET.SubElement(username, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        role = ET.SubElement(username, "role")
        role.text = kwargs.pop('role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_desc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        desc = ET.SubElement(username, "desc")
        desc.text = kwargs.pop('desc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(username, "enable")
        enable.text = kwargs.pop('enable')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_expire(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        expire = ET.SubElement(username, "expire")
        expire.text = kwargs.pop('expire')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_access_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        access_time = ET.SubElement(username, "access-time")
        access_time.text = kwargs.pop('access_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_end_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        end_time = ET.SubElement(username, "end-time")
        end_time.text = kwargs.pop('end_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def service_password_encryption(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        service = ET.SubElement(config, "service", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        password_encryption = ET.SubElement(service, "password-encryption")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def role_name_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        role = ET.SubElement(config, "role", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name = ET.SubElement(role, "name")
        name = ET.SubElement(name, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def role_name_desc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        role = ET.SubElement(config, "role", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name = ET.SubElement(role, "name")
        name_key = ET.SubElement(name, "name")
        name_key.text = kwargs.pop('name')
        desc = ET.SubElement(name, "desc")
        desc.text = kwargs.pop('desc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        hostname = ET.SubElement(host, "hostname")
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_auth_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        auth_port = ET.SubElement(host, "auth-port")
        auth_port.text = kwargs.pop('auth_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        protocol = ET.SubElement(host, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        key = ET.SubElement(host, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        encryption_level = ET.SubElement(host, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        retries = ET.SubElement(host, "retries")
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        timeout = ET.SubElement(host, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        hostname = ET.SubElement(host, "hostname")
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        port = ET.SubElement(host, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        protocol = ET.SubElement(host, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        key = ET.SubElement(host, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        encryption_level = ET.SubElement(host, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        retries = ET.SubElement(host, "retries")
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        timeout = ET.SubElement(host, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_tacacs_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        tacacs_source_ip = ET.SubElement(tacacs_server, "tacacs-source-ip")
        tacacs_source_ip.text = kwargs.pop('tacacs_source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        hostname = ET.SubElement(host, "hostname")
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        port = ET.SubElement(host, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        retries = ET.SubElement(host, "retries")
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        timeout = ET.SubElement(host, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_basedn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        basedn = ET.SubElement(host, "basedn")
        basedn.text = kwargs.pop('basedn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_maprole_group_ad_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        maprole = ET.SubElement(ldap_server, "maprole")
        group = ET.SubElement(maprole, "group")
        ad_group = ET.SubElement(group, "ad-group")
        ad_group.text = kwargs.pop('ad_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_maprole_group_switch_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        maprole = ET.SubElement(ldap_server, "maprole")
        group = ET.SubElement(maprole, "group")
        ad_group_key = ET.SubElement(group, "ad-group")
        ad_group_key.text = kwargs.pop('ad_group')
        switch_role = ET.SubElement(group, "switch-role")
        switch_role.text = kwargs.pop('switch_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_min_length(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        min_length = ET.SubElement(password_attributes, "min-length")
        min_length.text = kwargs.pop('min_length')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_max_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        max_retry = ET.SubElement(password_attributes, "max-retry")
        max_retry.text = kwargs.pop('max_retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_max_lockout_duration(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        max_lockout_duration = ET.SubElement(password_attributes, "max-lockout-duration")
        max_lockout_duration.text = kwargs.pop('max_lockout_duration')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        upper = ET.SubElement(character_restriction, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        lower = ET.SubElement(character_restriction, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_numeric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        numeric = ET.SubElement(character_restriction, "numeric")
        numeric.text = kwargs.pop('numeric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_special_char(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        special_char = ET.SubElement(character_restriction, "special-char")
        special_char.text = kwargs.pop('special_char')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_admin_lockout_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        admin_lockout_enable = ET.SubElement(password_attributes, "admin-lockout-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_login(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        login = ET.SubElement(banner, "login")
        login.text = kwargs.pop('login')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_motd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        motd = ET.SubElement(banner, "motd")
        motd.text = kwargs.pop('motd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_incoming(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        incoming = ET.SubElement(banner, "incoming")
        incoming.text = kwargs.pop('incoming')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index = ET.SubElement(rule, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        action = ET.SubElement(rule, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        operation = ET.SubElement(rule, "operation")
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        role = ET.SubElement(rule, "role")
        role.text = kwargs.pop('role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_container_cmds_enumList(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        container_cmds = ET.SubElement(cmdlist, "container-cmds")
        enumList = ET.SubElement(container_cmds, "enumList")
        enumList.text = kwargs.pop('enumList')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_d_interface_fcoe_leaf_interface_fcoe_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_d = ET.SubElement(cmdlist, "interface-d")
        interface_fcoe_leaf = ET.SubElement(interface_d, "interface-fcoe-leaf")
        interface = ET.SubElement(interface_fcoe_leaf, "interface")
        fcoe_leaf = ET.SubElement(interface, "fcoe-leaf")
        fcoe_leaf.text = kwargs.pop('fcoe_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_e_interface_te_leaf_interface_tengigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_e = ET.SubElement(cmdlist, "interface-e")
        interface_te_leaf = ET.SubElement(interface_e, "interface-te-leaf")
        interface = ET.SubElement(interface_te_leaf, "interface")
        tengigabitethernet_leaf = ET.SubElement(interface, "tengigabitethernet-leaf")
        tengigabitethernet_leaf.text = kwargs.pop('tengigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_h_interface_ge_leaf_interface_gigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_h = ET.SubElement(cmdlist, "interface-h")
        interface_ge_leaf = ET.SubElement(interface_h, "interface-ge-leaf")
        interface = ET.SubElement(interface_ge_leaf, "interface")
        gigabitethernet_leaf = ET.SubElement(interface, "gigabitethernet-leaf")
        gigabitethernet_leaf.text = kwargs.pop('gigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_j_interface_pc_leaf_interface_port_channel_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_j = ET.SubElement(cmdlist, "interface-j")
        interface_pc_leaf = ET.SubElement(interface_j, "interface-pc-leaf")
        interface = ET.SubElement(interface_pc_leaf, "interface")
        port_channel_leaf = ET.SubElement(interface, "port-channel-leaf")
        port_channel_leaf.text = kwargs.pop('port_channel_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_l_interface_vlan_leaf_interface_vlan_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_l = ET.SubElement(cmdlist, "interface-l")
        interface_vlan_leaf = ET.SubElement(interface_l, "interface-vlan-leaf")
        interface = ET.SubElement(interface_vlan_leaf, "interface")
        vlan_leaf = ET.SubElement(interface, "vlan-leaf")
        vlan_leaf.text = kwargs.pop('vlan_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_m_interface_management_leaf_interface_management_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_m = ET.SubElement(cmdlist, "interface-m")
        interface_management_leaf = ET.SubElement(interface_m, "interface-management-leaf")
        interface = ET.SubElement(interface_management_leaf, "interface")
        management_leaf = ET.SubElement(interface, "management-leaf")
        management_leaf.text = kwargs.pop('management_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_o_interface_loopback_leaf_interface_loopback_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_o = ET.SubElement(cmdlist, "interface-o")
        interface_loopback_leaf = ET.SubElement(interface_o, "interface-loopback-leaf")
        interface = ET.SubElement(interface_loopback_leaf, "interface")
        loopback_leaf = ET.SubElement(interface, "loopback-leaf")
        loopback_leaf.text = kwargs.pop('loopback_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_q_interface_ve_leaf_interface_ve_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_q = ET.SubElement(cmdlist, "interface-q")
        interface_ve_leaf = ET.SubElement(interface_q, "interface-ve-leaf")
        interface = ET.SubElement(interface_ve_leaf, "interface")
        ve_leaf = ET.SubElement(interface, "ve-leaf")
        ve_leaf.text = kwargs.pop('ve_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_s_interface_fc_leaf_interface_fibrechannel_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_s = ET.SubElement(cmdlist, "interface-s")
        interface_fc_leaf = ET.SubElement(interface_s, "interface-fc-leaf")
        interface = ET.SubElement(interface_fc_leaf, "interface")
        fibrechannel_leaf = ET.SubElement(interface, "fibrechannel-leaf")
        fibrechannel_leaf.text = kwargs.pop('fibrechannel_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_u_interface_fe_leaf_interface_fortygigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_u = ET.SubElement(cmdlist, "interface-u")
        interface_fe_leaf = ET.SubElement(interface_u, "interface-fe-leaf")
        interface = ET.SubElement(interface_fe_leaf, "interface")
        fortygigabitethernet_leaf = ET.SubElement(interface, "fortygigabitethernet-leaf")
        fortygigabitethernet_leaf.text = kwargs.pop('fortygigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_w_interface_he_leaf_interface_hundredgigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_w = ET.SubElement(cmdlist, "interface-w")
        interface_he_leaf = ET.SubElement(interface_w, "interface-he-leaf")
        interface = ET.SubElement(interface_he_leaf, "interface")
        hundredgigabitethernet_leaf = ET.SubElement(interface, "hundredgigabitethernet-leaf")
        hundredgigabitethernet_leaf.text = kwargs.pop('hundredgigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def root_sa_root_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        root_sa = ET.SubElement(config, "root-sa", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        root = ET.SubElement(root_sa, "root")
        enable = ET.SubElement(root, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def root_sa_root_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        root_sa = ET.SubElement(config, "root-sa", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        root = ET.SubElement(root_sa, "root")
        access = ET.SubElement(root, "access")
        access.text = kwargs.pop('access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        alias = ET.SubElement(alias_config, "alias")
        name = ET.SubElement(alias, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_alias_expansion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        alias = ET.SubElement(alias_config, "alias")
        name_key = ET.SubElement(alias, "name")
        name_key.text = kwargs.pop('name')
        expansion = ET.SubElement(alias, "expansion")
        expansion.text = kwargs.pop('expansion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        user = ET.SubElement(alias_config, "user")
        name = ET.SubElement(user, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        user = ET.SubElement(alias_config, "user")
        name_key = ET.SubElement(user, "name")
        name_key.text = kwargs.pop('name')
        alias = ET.SubElement(user, "alias")
        name = ET.SubElement(alias, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_alias_expansion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        user = ET.SubElement(alias_config, "user")
        name_key = ET.SubElement(user, "name")
        name_key.text = kwargs.pop('name')
        alias = ET.SubElement(user, "alias")
        name_key = ET.SubElement(alias, "name")
        name_key.text = kwargs.pop('name')
        expansion = ET.SubElement(alias, "expansion")
        expansion.text = kwargs.pop('expansion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_authentication_login_first(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        authentication = ET.SubElement(aaa, "authentication")
        login = ET.SubElement(authentication, "login")
        first = ET.SubElement(login, "first")
        first.text = kwargs.pop('first')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_authentication_login_second(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        authentication = ET.SubElement(aaa, "authentication")
        login = ET.SubElement(authentication, "login")
        second = ET.SubElement(login, "second")
        second.text = kwargs.pop('second')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_accounting_exec_defaultacc_start_stop_server_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        accounting = ET.SubElement(aaa, "accounting")
        exec_el = ET.SubElement(accounting, "exec")
        defaultacc = ET.SubElement(exec_el, "defaultacc")
        start_stop = ET.SubElement(defaultacc, "start-stop")
        server_type = ET.SubElement(start_stop, "server-type")
        server_type.text = kwargs.pop('server_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def aaa_config_aaa_accounting_commands_defaultacc_start_stop_server_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        aaa_config = ET.SubElement(config, "aaa-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        aaa = ET.SubElement(aaa_config, "aaa")
        accounting = ET.SubElement(aaa, "accounting")
        commands = ET.SubElement(accounting, "commands")
        defaultacc = ET.SubElement(commands, "defaultacc")
        start_stop = ET.SubElement(defaultacc, "start-stop")
        server_type = ET.SubElement(start_stop, "server-type")
        server_type.text = kwargs.pop('server_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name = ET.SubElement(username, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_user_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        user_password = ET.SubElement(username, "user-password")
        user_password.text = kwargs.pop('user_password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        encryption_level = ET.SubElement(username, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        role = ET.SubElement(username, "role")
        role.text = kwargs.pop('role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_desc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        desc = ET.SubElement(username, "desc")
        desc.text = kwargs.pop('desc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        enable = ET.SubElement(username, "enable")
        enable.text = kwargs.pop('enable')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_expire(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        expire = ET.SubElement(username, "expire")
        expire.text = kwargs.pop('expire')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_access_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        access_time = ET.SubElement(username, "access-time")
        access_time.text = kwargs.pop('access_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def username_end_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        username = ET.SubElement(config, "username", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name_key = ET.SubElement(username, "name")
        name_key.text = kwargs.pop('name')
        end_time = ET.SubElement(username, "end-time")
        end_time.text = kwargs.pop('end_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def service_password_encryption(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        service = ET.SubElement(config, "service", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        password_encryption = ET.SubElement(service, "password-encryption")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def role_name_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        role = ET.SubElement(config, "role", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name = ET.SubElement(role, "name")
        name = ET.SubElement(name, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def role_name_desc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        role = ET.SubElement(config, "role", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        name = ET.SubElement(role, "name")
        name_key = ET.SubElement(name, "name")
        name_key.text = kwargs.pop('name')
        desc = ET.SubElement(name, "desc")
        desc.text = kwargs.pop('desc')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        hostname = ET.SubElement(host, "hostname")
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_auth_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        auth_port = ET.SubElement(host, "auth-port")
        auth_port.text = kwargs.pop('auth_port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        protocol = ET.SubElement(host, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        key = ET.SubElement(host, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        encryption_level = ET.SubElement(host, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        retries = ET.SubElement(host, "retries")
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def radius_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        radius_server = ET.SubElement(config, "radius-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(radius_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        timeout = ET.SubElement(host, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        hostname = ET.SubElement(host, "hostname")
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        port = ET.SubElement(host, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        protocol = ET.SubElement(host, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        key = ET.SubElement(host, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_encryption_level(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        encryption_level = ET.SubElement(host, "encryption-level")
        encryption_level.text = kwargs.pop('encryption_level')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        retries = ET.SubElement(host, "retries")
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(tacacs_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        timeout = ET.SubElement(host, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def tacacs_server_tacacs_source_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        tacacs_server = ET.SubElement(config, "tacacs-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        tacacs_source_ip = ET.SubElement(tacacs_server, "tacacs-source-ip")
        tacacs_source_ip.text = kwargs.pop('tacacs_source_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_hostname(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        hostname = ET.SubElement(host, "hostname")
        hostname.text = kwargs.pop('hostname')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf = ET.SubElement(host, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        port = ET.SubElement(host, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_retries(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        retries = ET.SubElement(host, "retries")
        retries.text = kwargs.pop('retries')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        timeout = ET.SubElement(host, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_host_basedn(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        host = ET.SubElement(ldap_server, "host")
        hostname_key = ET.SubElement(host, "hostname")
        hostname_key.text = kwargs.pop('hostname')
        use_vrf_key = ET.SubElement(host, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        basedn = ET.SubElement(host, "basedn")
        basedn.text = kwargs.pop('basedn')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_maprole_group_ad_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        maprole = ET.SubElement(ldap_server, "maprole")
        group = ET.SubElement(maprole, "group")
        ad_group = ET.SubElement(group, "ad-group")
        ad_group.text = kwargs.pop('ad_group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def ldap_server_maprole_group_switch_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        ldap_server = ET.SubElement(config, "ldap-server", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        maprole = ET.SubElement(ldap_server, "maprole")
        group = ET.SubElement(maprole, "group")
        ad_group_key = ET.SubElement(group, "ad-group")
        ad_group_key.text = kwargs.pop('ad_group')
        switch_role = ET.SubElement(group, "switch-role")
        switch_role.text = kwargs.pop('switch_role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_min_length(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        min_length = ET.SubElement(password_attributes, "min-length")
        min_length.text = kwargs.pop('min_length')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_max_retry(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        max_retry = ET.SubElement(password_attributes, "max-retry")
        max_retry.text = kwargs.pop('max_retry')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_max_lockout_duration(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        max_lockout_duration = ET.SubElement(password_attributes, "max-lockout-duration")
        max_lockout_duration.text = kwargs.pop('max_lockout_duration')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        upper = ET.SubElement(character_restriction, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        lower = ET.SubElement(character_restriction, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_numeric(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        numeric = ET.SubElement(character_restriction, "numeric")
        numeric.text = kwargs.pop('numeric')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_character_restriction_special_char(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        character_restriction = ET.SubElement(password_attributes, "character-restriction")
        special_char = ET.SubElement(character_restriction, "special-char")
        special_char.text = kwargs.pop('special_char')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def password_attributes_admin_lockout_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        password_attributes = ET.SubElement(config, "password-attributes", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        admin_lockout_enable = ET.SubElement(password_attributes, "admin-lockout-enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_login(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        login = ET.SubElement(banner, "login")
        login.text = kwargs.pop('login')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_motd(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        motd = ET.SubElement(banner, "motd")
        motd.text = kwargs.pop('motd')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def banner_incoming(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        banner = ET.SubElement(config, "banner", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        incoming = ET.SubElement(banner, "incoming")
        incoming.text = kwargs.pop('incoming')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index = ET.SubElement(rule, "index")
        index.text = kwargs.pop('index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        action = ET.SubElement(rule, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        operation = ET.SubElement(rule, "operation")
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_role(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        role = ET.SubElement(rule, "role")
        role.text = kwargs.pop('role')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_container_cmds_enumList(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        container_cmds = ET.SubElement(cmdlist, "container-cmds")
        enumList = ET.SubElement(container_cmds, "enumList")
        enumList.text = kwargs.pop('enumList')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_d_interface_fcoe_leaf_interface_fcoe_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_d = ET.SubElement(cmdlist, "interface-d")
        interface_fcoe_leaf = ET.SubElement(interface_d, "interface-fcoe-leaf")
        interface = ET.SubElement(interface_fcoe_leaf, "interface")
        fcoe_leaf = ET.SubElement(interface, "fcoe-leaf")
        fcoe_leaf.text = kwargs.pop('fcoe_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_e_interface_te_leaf_interface_tengigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_e = ET.SubElement(cmdlist, "interface-e")
        interface_te_leaf = ET.SubElement(interface_e, "interface-te-leaf")
        interface = ET.SubElement(interface_te_leaf, "interface")
        tengigabitethernet_leaf = ET.SubElement(interface, "tengigabitethernet-leaf")
        tengigabitethernet_leaf.text = kwargs.pop('tengigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_h_interface_ge_leaf_interface_gigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_h = ET.SubElement(cmdlist, "interface-h")
        interface_ge_leaf = ET.SubElement(interface_h, "interface-ge-leaf")
        interface = ET.SubElement(interface_ge_leaf, "interface")
        gigabitethernet_leaf = ET.SubElement(interface, "gigabitethernet-leaf")
        gigabitethernet_leaf.text = kwargs.pop('gigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_j_interface_pc_leaf_interface_port_channel_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_j = ET.SubElement(cmdlist, "interface-j")
        interface_pc_leaf = ET.SubElement(interface_j, "interface-pc-leaf")
        interface = ET.SubElement(interface_pc_leaf, "interface")
        port_channel_leaf = ET.SubElement(interface, "port-channel-leaf")
        port_channel_leaf.text = kwargs.pop('port_channel_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_l_interface_vlan_leaf_interface_vlan_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_l = ET.SubElement(cmdlist, "interface-l")
        interface_vlan_leaf = ET.SubElement(interface_l, "interface-vlan-leaf")
        interface = ET.SubElement(interface_vlan_leaf, "interface")
        vlan_leaf = ET.SubElement(interface, "vlan-leaf")
        vlan_leaf.text = kwargs.pop('vlan_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_m_interface_management_leaf_interface_management_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_m = ET.SubElement(cmdlist, "interface-m")
        interface_management_leaf = ET.SubElement(interface_m, "interface-management-leaf")
        interface = ET.SubElement(interface_management_leaf, "interface")
        management_leaf = ET.SubElement(interface, "management-leaf")
        management_leaf.text = kwargs.pop('management_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_o_interface_loopback_leaf_interface_loopback_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_o = ET.SubElement(cmdlist, "interface-o")
        interface_loopback_leaf = ET.SubElement(interface_o, "interface-loopback-leaf")
        interface = ET.SubElement(interface_loopback_leaf, "interface")
        loopback_leaf = ET.SubElement(interface, "loopback-leaf")
        loopback_leaf.text = kwargs.pop('loopback_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_q_interface_ve_leaf_interface_ve_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_q = ET.SubElement(cmdlist, "interface-q")
        interface_ve_leaf = ET.SubElement(interface_q, "interface-ve-leaf")
        interface = ET.SubElement(interface_ve_leaf, "interface")
        ve_leaf = ET.SubElement(interface, "ve-leaf")
        ve_leaf.text = kwargs.pop('ve_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_s_interface_fc_leaf_interface_fibrechannel_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_s = ET.SubElement(cmdlist, "interface-s")
        interface_fc_leaf = ET.SubElement(interface_s, "interface-fc-leaf")
        interface = ET.SubElement(interface_fc_leaf, "interface")
        fibrechannel_leaf = ET.SubElement(interface, "fibrechannel-leaf")
        fibrechannel_leaf.text = kwargs.pop('fibrechannel_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_u_interface_fe_leaf_interface_fortygigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_u = ET.SubElement(cmdlist, "interface-u")
        interface_fe_leaf = ET.SubElement(interface_u, "interface-fe-leaf")
        interface = ET.SubElement(interface_fe_leaf, "interface")
        fortygigabitethernet_leaf = ET.SubElement(interface, "fortygigabitethernet-leaf")
        fortygigabitethernet_leaf.text = kwargs.pop('fortygigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def rule_command_cmdlist_interface_w_interface_he_leaf_interface_hundredgigabitethernet_leaf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        rule = ET.SubElement(config, "rule", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        index_key = ET.SubElement(rule, "index")
        index_key.text = kwargs.pop('index')
        command = ET.SubElement(rule, "command")
        cmdlist = ET.SubElement(command, "cmdlist")
        interface_w = ET.SubElement(cmdlist, "interface-w")
        interface_he_leaf = ET.SubElement(interface_w, "interface-he-leaf")
        interface = ET.SubElement(interface_he_leaf, "interface")
        hundredgigabitethernet_leaf = ET.SubElement(interface, "hundredgigabitethernet-leaf")
        hundredgigabitethernet_leaf.text = kwargs.pop('hundredgigabitethernet_leaf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def root_sa_root_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        root_sa = ET.SubElement(config, "root-sa", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        root = ET.SubElement(root_sa, "root")
        enable = ET.SubElement(root, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def root_sa_root_access(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        root_sa = ET.SubElement(config, "root-sa", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        root = ET.SubElement(root_sa, "root")
        access = ET.SubElement(root, "access")
        access.text = kwargs.pop('access')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        alias = ET.SubElement(alias_config, "alias")
        name = ET.SubElement(alias, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_alias_expansion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        alias = ET.SubElement(alias_config, "alias")
        name_key = ET.SubElement(alias, "name")
        name_key.text = kwargs.pop('name')
        expansion = ET.SubElement(alias, "expansion")
        expansion.text = kwargs.pop('expansion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        user = ET.SubElement(alias_config, "user")
        name = ET.SubElement(user, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_alias_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        user = ET.SubElement(alias_config, "user")
        name_key = ET.SubElement(user, "name")
        name_key.text = kwargs.pop('name')
        alias = ET.SubElement(user, "alias")
        name = ET.SubElement(alias, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def alias_config_user_alias_expansion(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        alias_config = ET.SubElement(config, "alias-config", xmlns="urn:brocade.com:mgmt:brocade-aaa")
        user = ET.SubElement(alias_config, "user")
        name_key = ET.SubElement(user, "name")
        name_key.text = kwargs.pop('name')
        alias = ET.SubElement(user, "alias")
        name_key = ET.SubElement(alias, "name")
        name_key.text = kwargs.pop('name')
        expansion = ET.SubElement(alias, "expansion")
        expansion.text = kwargs.pop('expansion')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        