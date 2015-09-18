#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_ras(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def logging_raslog_message_msgId_msgId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId = ET.SubElement(msgId, "msgId")
        msgId.text = kwargs.pop('msgId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_severity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        severity = ET.SubElement(msgId, "severity")
        severity.text = kwargs.pop('severity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        suppress = ET.SubElement(msgId, "suppress")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_syslog(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        syslog = ET.SubElement(msgId, "syslog")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_module_modId_modId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        module = ET.SubElement(raslog, "module")
        modId = ET.SubElement(module, "modId")
        modId = ET.SubElement(modId, "modId")
        modId.text = kwargs.pop('modId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_console(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        console = ET.SubElement(raslog, "console")
        console.text = kwargs.pop('console')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_syslogip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        syslogip = ET.SubElement(syslog_server, "syslogip")
        syslogip.text = kwargs.pop('syslogip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        use_vrf = ET.SubElement(syslog_server, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_secure(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        secure = ET.SubElement(syslog_server, "secure")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        port = ET.SubElement(syslog_server, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_auditlog_clss_clss(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        auditlog = ET.SubElement(logging, "auditlog")
        clss = ET.SubElement(auditlog, "class")
        clss = ET.SubElement(clss, "class")
        clss.text = kwargs.pop('clss')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_facility_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_facility = ET.SubElement(logging, "syslog-facility")
        local = ET.SubElement(syslog_facility, "local")
        local.text = kwargs.pop('local')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_client_localip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_client = ET.SubElement(logging, "syslog-client")
        localip = ET.SubElement(syslog_client, "localip")
        localip.text = kwargs.pop('localip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        switch_attributes = ET.SubElement(system, "switch-attributes")
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_chassis_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        switch_attributes = ET.SubElement(system, "switch-attributes")
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        chassis_name = ET.SubElement(rbridge_id, "chassis-name")
        chassis_name.text = kwargs.pop('chassis_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_host_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        switch_attributes = ET.SubElement(system, "switch-attributes")
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        host_name = ET.SubElement(rbridge_id, "host-name")
        host_name.text = kwargs.pop('host_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_input_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        input = ET.SubElement(bna_config_cmd, "input")
        src = ET.SubElement(input, "src")
        src.text = kwargs.pop('src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_input_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        input = ET.SubElement(bna_config_cmd, "input")
        dest = ET.SubElement(input, "dest")
        dest.text = kwargs.pop('dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        output = ET.SubElement(bna_config_cmd, "output")
        session_id = ET.SubElement(output, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        output = ET.SubElement(bna_config_cmd, "output")
        status = ET.SubElement(output, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        output = ET.SubElement(bna_config_cmd, "output")
        status_string = ET.SubElement(output, "status-string")
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        input = ET.SubElement(bna_config_cmd_status, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_output_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        output = ET.SubElement(bna_config_cmd_status, "output")
        status = ET.SubElement(output, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        output = ET.SubElement(bna_config_cmd_status, "output")
        status_string = ET.SubElement(output, "status-string")
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        hostip = ET.SubElement(autoupload_param, "hostip")
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        username = ET.SubElement(autoupload_param, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        directory = ET.SubElement(autoupload_param, "directory")
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        protocol = ET.SubElement(autoupload_param, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        password = ET.SubElement(autoupload_param, "password")
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        hostip = ET.SubElement(support_param, "hostip")
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        username = ET.SubElement(support_param, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        directory = ET.SubElement(support_param, "directory")
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        protocol = ET.SubElement(support_param, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        password = ET.SubElement(support_param, "password")
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload = ET.SubElement(support, "autoupload")
        enable = ET.SubElement(autoupload, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_ffdc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        ffdc = ET.SubElement(support, "ffdc")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_msgId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId = ET.SubElement(msgId, "msgId")
        msgId.text = kwargs.pop('msgId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_severity(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        severity = ET.SubElement(msgId, "severity")
        severity.text = kwargs.pop('severity')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_suppress(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        suppress = ET.SubElement(msgId, "suppress")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_message_msgId_syslog(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        message = ET.SubElement(raslog, "message")
        msgId = ET.SubElement(message, "msgId")
        msgId_key = ET.SubElement(msgId, "msgId")
        msgId_key.text = kwargs.pop('msgId')
        syslog = ET.SubElement(msgId, "syslog")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_module_modId_modId(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        module = ET.SubElement(raslog, "module")
        modId = ET.SubElement(module, "modId")
        modId = ET.SubElement(modId, "modId")
        modId.text = kwargs.pop('modId')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_raslog_console(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        raslog = ET.SubElement(logging, "raslog")
        console = ET.SubElement(raslog, "console")
        console.text = kwargs.pop('console')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_syslogip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        syslogip = ET.SubElement(syslog_server, "syslogip")
        syslogip.text = kwargs.pop('syslogip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_use_vrf(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        use_vrf = ET.SubElement(syslog_server, "use-vrf")
        use_vrf.text = kwargs.pop('use_vrf')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_secure(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        secure = ET.SubElement(syslog_server, "secure")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_server_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_server = ET.SubElement(logging, "syslog-server")
        syslogip_key = ET.SubElement(syslog_server, "syslogip")
        syslogip_key.text = kwargs.pop('syslogip')
        use_vrf_key = ET.SubElement(syslog_server, "use-vrf")
        use_vrf_key.text = kwargs.pop('use_vrf')
        port = ET.SubElement(syslog_server, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_auditlog_clss_clss(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        auditlog = ET.SubElement(logging, "auditlog")
        clss = ET.SubElement(auditlog, "class")
        clss = ET.SubElement(clss, "class")
        clss.text = kwargs.pop('clss')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_facility_local(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_facility = ET.SubElement(logging, "syslog-facility")
        local = ET.SubElement(syslog_facility, "local")
        local.text = kwargs.pop('local')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def logging_syslog_client_localip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        logging = ET.SubElement(config, "logging", xmlns="urn:brocade.com:mgmt:brocade-ras")
        syslog_client = ET.SubElement(logging, "syslog-client")
        localip = ET.SubElement(syslog_client, "localip")
        localip.text = kwargs.pop('localip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_rbridge_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        switch_attributes = ET.SubElement(system, "switch-attributes")
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        rbridge_id = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id.text = kwargs.pop('rbridge_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_chassis_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        switch_attributes = ET.SubElement(system, "switch-attributes")
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        chassis_name = ET.SubElement(rbridge_id, "chassis-name")
        chassis_name.text = kwargs.pop('chassis_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_switch_attributes_rbridge_id_host_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system = ET.SubElement(config, "system", xmlns="urn:brocade.com:mgmt:brocade-ras")
        switch_attributes = ET.SubElement(system, "switch-attributes")
        rbridge_id = ET.SubElement(switch_attributes, "rbridge-id")
        rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
        rbridge_id_key.text = kwargs.pop('rbridge_id')
        host_name = ET.SubElement(rbridge_id, "host-name")
        host_name.text = kwargs.pop('host_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_input_src(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        input = ET.SubElement(bna_config_cmd, "input")
        src = ET.SubElement(input, "src")
        src.text = kwargs.pop('src')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_input_dest(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        input = ET.SubElement(bna_config_cmd, "input")
        dest = ET.SubElement(input, "dest")
        dest.text = kwargs.pop('dest')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        output = ET.SubElement(bna_config_cmd, "output")
        session_id = ET.SubElement(output, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        output = ET.SubElement(bna_config_cmd, "output")
        status = ET.SubElement(output, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd = ET.Element("bna_config_cmd")
        config = bna_config_cmd
        output = ET.SubElement(bna_config_cmd, "output")
        status_string = ET.SubElement(output, "status-string")
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        input = ET.SubElement(bna_config_cmd_status, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_output_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        output = ET.SubElement(bna_config_cmd_status, "output")
        status = ET.SubElement(output, "status")
        status.text = kwargs.pop('status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def bna_config_cmd_status_output_status_string(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        bna_config_cmd_status = ET.Element("bna_config_cmd_status")
        config = bna_config_cmd_status
        output = ET.SubElement(bna_config_cmd_status, "output")
        status_string = ET.SubElement(output, "status-string")
        status_string.text = kwargs.pop('status_string')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        hostip = ET.SubElement(autoupload_param, "hostip")
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        username = ET.SubElement(autoupload_param, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        directory = ET.SubElement(autoupload_param, "directory")
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        protocol = ET.SubElement(autoupload_param, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_param_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload_param = ET.SubElement(support, "autoupload-param")
        password = ET.SubElement(autoupload_param, "password")
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_hostip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        hostip = ET.SubElement(support_param, "hostip")
        hostip.text = kwargs.pop('hostip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        username = ET.SubElement(support_param, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_directory(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        directory = ET.SubElement(support_param, "directory")
        directory.text = kwargs.pop('directory')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_protocol(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        protocol = ET.SubElement(support_param, "protocol")
        protocol.text = kwargs.pop('protocol')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_support_param_password(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        support_param = ET.SubElement(support, "support-param")
        password = ET.SubElement(support_param, "password")
        password.text = kwargs.pop('password')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_autoupload_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        autoupload = ET.SubElement(support, "autoupload")
        enable = ET.SubElement(autoupload, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def support_ffdc(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        support = ET.SubElement(config, "support", xmlns="urn:brocade.com:mgmt:brocade-ras")
        ffdc = ET.SubElement(support, "ffdc")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        