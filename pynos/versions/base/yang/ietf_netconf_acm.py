#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf_acm(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def nacm_enable_nacm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        enable_nacm = ET.SubElement(nacm, "enable-nacm")
        enable_nacm.text = kwargs.pop('enable_nacm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_read_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        read_default = ET.SubElement(nacm, "read-default")
        read_default.text = kwargs.pop('read_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_write_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        write_default = ET.SubElement(nacm, "write-default")
        write_default.text = kwargs.pop('write_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_exec_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        exec_default = ET.SubElement(nacm, "exec-default")
        exec_default.text = kwargs.pop('exec_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_enable_external_groups(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        enable_external_groups = ET.SubElement(nacm, "enable-external-groups")
        enable_external_groups.text = kwargs.pop('enable_external_groups')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        denied_operations = ET.SubElement(nacm, "denied-operations")
        denied_operations.text = kwargs.pop('denied_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_data_writes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        denied_data_writes = ET.SubElement(nacm, "denied-data-writes")
        denied_data_writes.text = kwargs.pop('denied_data_writes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        denied_notifications = ET.SubElement(nacm, "denied-notifications")
        denied_notifications.text = kwargs.pop('denied_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_groups_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        groups = ET.SubElement(nacm, "groups")
        group = ET.SubElement(groups, "group")
        name = ET.SubElement(group, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_groups_group_gid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        groups = ET.SubElement(nacm, "groups")
        group = ET.SubElement(groups, "group")
        name_key = ET.SubElement(group, "name")
        name_key.text = kwargs.pop('name')
        gid = ET.SubElement(group, "gid", xmlns="http://tail-f.com/yang/acm")
        gid.text = kwargs.pop('gid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name = ET.SubElement(rule_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name = ET.SubElement(rule, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_module_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        module_name = ET.SubElement(rule, "module-name")
        module_name.text = kwargs.pop('module_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_protocol_operation_rpc_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        rule_type = ET.SubElement(rule, "rule-type")
        protocol_operation = ET.SubElement(rule_type, "protocol-operation")
        rpc_name = ET.SubElement(protocol_operation, "rpc-name")
        rpc_name.text = kwargs.pop('rpc_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_notification_notification_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        rule_type = ET.SubElement(rule, "rule-type")
        notification = ET.SubElement(rule_type, "notification")
        notification_name = ET.SubElement(notification, "notification-name")
        notification_name.text = kwargs.pop('notification_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_data_node_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        rule_type = ET.SubElement(rule, "rule-type")
        data_node = ET.SubElement(rule_type, "data-node")
        path = ET.SubElement(data_node, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_access_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        access_operations = ET.SubElement(rule, "access-operations")
        access_operations.text = kwargs.pop('access_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        action = ET.SubElement(rule, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_comment(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        comment = ET.SubElement(rule, "comment")
        comment.text = kwargs.pop('comment')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        context = ET.SubElement(rule, "context", xmlns="http://tail-f.com/yang/acm")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_log_if_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        log_if_permit = ET.SubElement(rule, "log-if-permit", xmlns="http://tail-f.com/yang/acm")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name = ET.SubElement(cmdrule, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        context = ET.SubElement(cmdrule, "context")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_command(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        command = ET.SubElement(cmdrule, "command")
        command.text = kwargs.pop('command')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_access_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        access_operations = ET.SubElement(cmdrule, "access-operations")
        access_operations.text = kwargs.pop('access_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        action = ET.SubElement(cmdrule, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_log_if_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        log_if_permit = ET.SubElement(cmdrule, "log-if-permit")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_comment(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        comment = ET.SubElement(cmdrule, "comment")
        comment.text = kwargs.pop('comment')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_cmd_read_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        cmd_read_default = ET.SubElement(nacm, "cmd-read-default", xmlns="http://tail-f.com/yang/acm")
        cmd_read_default.text = kwargs.pop('cmd_read_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_cmd_exec_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        cmd_exec_default = ET.SubElement(nacm, "cmd-exec-default", xmlns="http://tail-f.com/yang/acm")
        cmd_exec_default.text = kwargs.pop('cmd_exec_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_log_if_default_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        log_if_default_permit = ET.SubElement(nacm, "log-if-default-permit", xmlns="http://tail-f.com/yang/acm")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_enable_nacm(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        enable_nacm = ET.SubElement(nacm, "enable-nacm")
        enable_nacm.text = kwargs.pop('enable_nacm')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_read_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        read_default = ET.SubElement(nacm, "read-default")
        read_default.text = kwargs.pop('read_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_write_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        write_default = ET.SubElement(nacm, "write-default")
        write_default.text = kwargs.pop('write_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_exec_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        exec_default = ET.SubElement(nacm, "exec-default")
        exec_default.text = kwargs.pop('exec_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_enable_external_groups(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        enable_external_groups = ET.SubElement(nacm, "enable-external-groups")
        enable_external_groups.text = kwargs.pop('enable_external_groups')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        denied_operations = ET.SubElement(nacm, "denied-operations")
        denied_operations.text = kwargs.pop('denied_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_data_writes(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        denied_data_writes = ET.SubElement(nacm, "denied-data-writes")
        denied_data_writes.text = kwargs.pop('denied_data_writes')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_denied_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        denied_notifications = ET.SubElement(nacm, "denied-notifications")
        denied_notifications.text = kwargs.pop('denied_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_groups_group_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        groups = ET.SubElement(nacm, "groups")
        group = ET.SubElement(groups, "group")
        name = ET.SubElement(group, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_groups_group_gid(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        groups = ET.SubElement(nacm, "groups")
        group = ET.SubElement(groups, "group")
        name_key = ET.SubElement(group, "name")
        name_key.text = kwargs.pop('name')
        gid = ET.SubElement(group, "gid", xmlns="http://tail-f.com/yang/acm")
        gid.text = kwargs.pop('gid')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name = ET.SubElement(rule_list, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name = ET.SubElement(rule, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_module_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        module_name = ET.SubElement(rule, "module-name")
        module_name.text = kwargs.pop('module_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_protocol_operation_rpc_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        rule_type = ET.SubElement(rule, "rule-type")
        protocol_operation = ET.SubElement(rule_type, "protocol-operation")
        rpc_name = ET.SubElement(protocol_operation, "rpc-name")
        rpc_name.text = kwargs.pop('rpc_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_notification_notification_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        rule_type = ET.SubElement(rule, "rule-type")
        notification = ET.SubElement(rule_type, "notification")
        notification_name = ET.SubElement(notification, "notification-name")
        notification_name.text = kwargs.pop('notification_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_rule_type_data_node_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        rule_type = ET.SubElement(rule, "rule-type")
        data_node = ET.SubElement(rule_type, "data-node")
        path = ET.SubElement(data_node, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_access_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        access_operations = ET.SubElement(rule, "access-operations")
        access_operations.text = kwargs.pop('access_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        action = ET.SubElement(rule, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_comment(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        comment = ET.SubElement(rule, "comment")
        comment.text = kwargs.pop('comment')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        context = ET.SubElement(rule, "context", xmlns="http://tail-f.com/yang/acm")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_rule_log_if_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        rule = ET.SubElement(rule_list, "rule")
        name_key = ET.SubElement(rule, "name")
        name_key.text = kwargs.pop('name')
        log_if_permit = ET.SubElement(rule, "log-if-permit", xmlns="http://tail-f.com/yang/acm")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name = ET.SubElement(cmdrule, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        context = ET.SubElement(cmdrule, "context")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_command(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        command = ET.SubElement(cmdrule, "command")
        command.text = kwargs.pop('command')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_access_operations(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        access_operations = ET.SubElement(cmdrule, "access-operations")
        access_operations.text = kwargs.pop('access_operations')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        action = ET.SubElement(cmdrule, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_log_if_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        log_if_permit = ET.SubElement(cmdrule, "log-if-permit")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_rule_list_cmdrule_comment(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        rule_list = ET.SubElement(nacm, "rule-list")
        name_key = ET.SubElement(rule_list, "name")
        name_key.text = kwargs.pop('name')
        cmdrule = ET.SubElement(rule_list, "cmdrule", xmlns="http://tail-f.com/yang/acm")
        name_key = ET.SubElement(cmdrule, "name")
        name_key.text = kwargs.pop('name')
        comment = ET.SubElement(cmdrule, "comment")
        comment.text = kwargs.pop('comment')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_cmd_read_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        cmd_read_default = ET.SubElement(nacm, "cmd-read-default", xmlns="http://tail-f.com/yang/acm")
        cmd_read_default.text = kwargs.pop('cmd_read_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_cmd_exec_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        cmd_exec_default = ET.SubElement(nacm, "cmd-exec-default", xmlns="http://tail-f.com/yang/acm")
        cmd_exec_default.text = kwargs.pop('cmd_exec_default')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nacm_log_if_default_permit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nacm = ET.SubElement(config, "nacm", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm")
        log_if_default_permit = ET.SubElement(nacm, "log-if-default-permit", xmlns="http://tail-f.com/yang/acm")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        