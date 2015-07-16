#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf_notifications(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def netconf_config_change_changed_by_server_or_user_server_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        server = ET.SubElement(server_or_user, "server")
        server = ET.SubElement(server, "server")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        username = ET.SubElement(by_user, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        session_id = ET.SubElement(by_user, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        source_host = ET.SubElement(by_user, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        datastore = ET.SubElement(netconf_config_change, "datastore")
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_edit_target(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        edit = ET.SubElement(netconf_config_change, "edit")
        target = ET.SubElement(edit, "target")
        target.text = kwargs.pop('target')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_edit_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        edit = ET.SubElement(netconf_config_change, "edit")
        operation = ET.SubElement(edit, "operation")
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_server_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        server = ET.SubElement(server_or_user, "server")
        server = ET.SubElement(server, "server")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        username = ET.SubElement(by_user, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        session_id = ET.SubElement(by_user, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        source_host = ET.SubElement(by_user, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        username = ET.SubElement(netconf_session_start, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        session_id = ET.SubElement(netconf_session_start, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        source_host = ET.SubElement(netconf_session_start, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        username = ET.SubElement(netconf_session_end, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        session_id = ET.SubElement(netconf_session_end, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        source_host = ET.SubElement(netconf_session_end, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_killed_by(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        killed_by = ET.SubElement(netconf_session_end, "killed-by")
        killed_by.text = kwargs.pop('killed_by')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_termination_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        termination_reason = ET.SubElement(netconf_session_end, "termination-reason")
        termination_reason.text = kwargs.pop('termination_reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        username = ET.SubElement(netconf_confirmed_commit, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        session_id = ET.SubElement(netconf_confirmed_commit, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        source_host = ET.SubElement(netconf_confirmed_commit, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_confirm_event(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        confirm_event = ET.SubElement(netconf_confirmed_commit, "confirm-event")
        confirm_event.text = kwargs.pop('confirm_event')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        timeout = ET.SubElement(netconf_confirmed_commit, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_server_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        server = ET.SubElement(server_or_user, "server")
        server = ET.SubElement(server, "server")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        username = ET.SubElement(by_user, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        session_id = ET.SubElement(by_user, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_changed_by_server_or_user_by_user_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_config_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        source_host = ET.SubElement(by_user, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        datastore = ET.SubElement(netconf_config_change, "datastore")
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_edit_target(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        edit = ET.SubElement(netconf_config_change, "edit")
        target = ET.SubElement(edit, "target")
        target.text = kwargs.pop('target')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_config_change_edit_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_config_change = ET.SubElement(config, "netconf-config-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        edit = ET.SubElement(netconf_config_change, "edit")
        operation = ET.SubElement(edit, "operation")
        operation.text = kwargs.pop('operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_server_server(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        server = ET.SubElement(server_or_user, "server")
        server = ET.SubElement(server, "server")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        username = ET.SubElement(by_user, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        session_id = ET.SubElement(by_user, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_capability_change_changed_by_server_or_user_by_user_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_capability_change = ET.SubElement(config, "netconf-capability-change", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        changed_by = ET.SubElement(netconf_capability_change, "changed-by")
        server_or_user = ET.SubElement(changed_by, "server-or-user")
        by_user = ET.SubElement(server_or_user, "by-user")
        source_host = ET.SubElement(by_user, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        username = ET.SubElement(netconf_session_start, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        session_id = ET.SubElement(netconf_session_start, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_start_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_start = ET.SubElement(config, "netconf-session-start", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        source_host = ET.SubElement(netconf_session_start, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        username = ET.SubElement(netconf_session_end, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        session_id = ET.SubElement(netconf_session_end, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        source_host = ET.SubElement(netconf_session_end, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_killed_by(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        killed_by = ET.SubElement(netconf_session_end, "killed-by")
        killed_by.text = kwargs.pop('killed_by')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_session_end_termination_reason(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_session_end = ET.SubElement(config, "netconf-session-end", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        termination_reason = ET.SubElement(netconf_session_end, "termination-reason")
        termination_reason.text = kwargs.pop('termination_reason')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        username = ET.SubElement(netconf_confirmed_commit, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        session_id = ET.SubElement(netconf_confirmed_commit, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        source_host = ET.SubElement(netconf_confirmed_commit, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_confirm_event(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        confirm_event = ET.SubElement(netconf_confirmed_commit, "confirm-event")
        confirm_event.text = kwargs.pop('confirm_event')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_confirmed_commit_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_confirmed_commit = ET.SubElement(config, "netconf-confirmed-commit", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-notifications")
        timeout = ET.SubElement(netconf_confirmed_commit, "timeout")
        timeout.text = kwargs.pop('timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        