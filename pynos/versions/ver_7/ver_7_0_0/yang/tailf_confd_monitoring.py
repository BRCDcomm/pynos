#!/usr/bin/env python
import xml.etree.ElementTree as ET


class tailf_confd_monitoring(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def confd_state_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        version = ET.SubElement(confd_state, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_smp_number_of_threads(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        smp = ET.SubElement(confd_state, "smp")
        number_of_threads = ET.SubElement(smp, "number-of-threads")
        number_of_threads.text = kwargs.pop('number_of_threads')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_epoll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        epoll = ET.SubElement(confd_state, "epoll")
        epoll.text = kwargs.pop('epoll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_daemon_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        daemon_status = ET.SubElement(confd_state, "daemon-status")
        daemon_status.text = kwargs.pop('daemon_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_read_only_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        read_only_mode = ET.SubElement(confd_state, "read-only-mode")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_upgrade_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        upgrade_mode = ET.SubElement(confd_state, "upgrade-mode")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        ha = ET.SubElement(confd_state, "ha")
        mode = ET.SubElement(ha, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_node_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        ha = ET.SubElement(confd_state, "ha")
        node_id = ET.SubElement(ha, "node-id")
        node_id.text = kwargs.pop('node_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_master_node_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        ha = ET.SubElement(confd_state, "ha")
        master_node_id = ET.SubElement(ha, "master-node-id")
        master_node_id.text = kwargs.pop('master_node_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name = ET.SubElement(data_model, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_revision(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        revision = ET.SubElement(data_model, "revision")
        revision.text = kwargs.pop('revision')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_namespace(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        namespace = ET.SubElement(data_model, "namespace")
        namespace.text = kwargs.pop('namespace')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_prefix(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        prefix = ET.SubElement(data_model, "prefix")
        prefix.text = kwargs.pop('prefix')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_exported_exported_to_all_exported_to_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        exported = ET.SubElement(data_model, "exported")
        exported_to_all = ET.SubElement(exported, "exported-to-all")
        exported_to_all = ET.SubElement(exported_to_all, "exported-to-all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        tcp = ET.SubElement(listen, "tcp")
        ip = ET.SubElement(tcp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        tcp = ET.SubElement(listen, "tcp")
        port = ET.SubElement(tcp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_ssh_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        ssh = ET.SubElement(listen, "ssh")
        ip = ET.SubElement(ssh, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_ssh_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        ssh = ET.SubElement(listen, "ssh")
        port = ET.SubElement(ssh, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_cli_listen_ssh_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        cli = ET.SubElement(confd_state, "cli")
        listen = ET.SubElement(cli, "listen")
        ssh = ET.SubElement(listen, "ssh")
        ip = ET.SubElement(ssh, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_cli_listen_ssh_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        cli = ET.SubElement(confd_state, "cli")
        listen = ET.SubElement(cli, "listen")
        ssh = ET.SubElement(listen, "ssh")
        port = ET.SubElement(ssh, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        tcp = ET.SubElement(listen, "tcp")
        ip = ET.SubElement(tcp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        tcp = ET.SubElement(listen, "tcp")
        port = ET.SubElement(tcp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_ssl_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        ssl = ET.SubElement(listen, "ssl")
        ip = ET.SubElement(ssl, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_ssl_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        ssl = ET.SubElement(listen, "ssl")
        port = ET.SubElement(ssl, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        tcp = ET.SubElement(listen, "tcp")
        ip = ET.SubElement(tcp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        tcp = ET.SubElement(listen, "tcp")
        port = ET.SubElement(tcp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_ssl_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        ssl = ET.SubElement(listen, "ssl")
        ip = ET.SubElement(ssl, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_ssl_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        ssl = ET.SubElement(listen, "ssl")
        port = ET.SubElement(ssl, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_listen_udp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        listen = ET.SubElement(snmp, "listen")
        udp = ET.SubElement(listen, "udp")
        ip = ET.SubElement(udp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_listen_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        listen = ET.SubElement(snmp, "listen")
        udp = ET.SubElement(listen, "udp")
        port = ET.SubElement(udp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        version = ET.SubElement(snmp, "version")
        v1 = ET.SubElement(version, "v1")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v2c(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        version = ET.SubElement(snmp, "version")
        v2c = ET.SubElement(version, "v2c")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        version = ET.SubElement(snmp, "version")
        v3 = ET.SubElement(version, "v3")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_engine_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        engine_id = ET.SubElement(snmp, "engine-id")
        engine_id.text = kwargs.pop('engine_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id = ET.SubElement(callpoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(callpoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id = ET.SubElement(validationpoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(validationpoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id = ET.SubElement(actionpoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(actionpoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id = ET.SubElement(snmp_inform_callback, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(snmp_inform_callback, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id = ET.SubElement(snmp_notification_subscription, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(snmp_notification_subscription, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id = ET.SubElement(error_formatting_callback, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(error_formatting_callback, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id = ET.SubElement(typepoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(typepoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name = ET.SubElement(notification_stream_replay, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_replay_support(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        replay_support = ET.SubElement(notification_stream_replay, "replay-support")
        replay_support.text = kwargs.pop('replay_support')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        error = ET.SubElement(notification_stream_replay, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        enabled = ET.SubElement(authentication_callback, "enabled")
        enabled.text = kwargs.pop('enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        error = ET.SubElement(authentication_callback, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        enabled = ET.SubElement(authorization_callbacks, "enabled")
        enabled.text = kwargs.pop('enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        error = ET.SubElement(authorization_callbacks, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name = ET.SubElement(datastore, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_transaction_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        transaction_id = ET.SubElement(datastore, "transaction-id")
        transaction_id.text = kwargs.pop('transaction_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_write_queue(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        write_queue = ET.SubElement(datastore, "write-queue")
        write_queue.text = kwargs.pop('write_queue')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_filename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        filename = ET.SubElement(datastore, "filename")
        filename.text = kwargs.pop('filename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_disk_size(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        disk_size = ET.SubElement(datastore, "disk-size")
        disk_size.text = kwargs.pop('disk_size')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_ram_size(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        ram_size = ET.SubElement(datastore, "ram-size")
        ram_size.text = kwargs.pop('ram_size')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_read_locks(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        read_locks = ET.SubElement(datastore, "read-locks")
        read_locks.text = kwargs.pop('read_locks')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_write_lock_set(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        write_lock_set = ET.SubElement(datastore, "write-lock-set")
        write_lock_set.text = kwargs.pop('write_lock_set')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_subscription_lock_set(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        subscription_lock_set = ET.SubElement(datastore, "subscription-lock-set")
        subscription_lock_set.text = kwargs.pop('subscription_lock_set')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_waiting_for_replication_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        waiting_for_replication_sync = ET.SubElement(datastore, "waiting-for-replication-sync")
        waiting_for_replication_sync.text = kwargs.pop('waiting_for_replication_sync')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        priority = ET.SubElement(pending_subscription_sync, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_notification_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        notification = ET.SubElement(pending_subscription_sync, "notification")
        client_name = ET.SubElement(notification, "client-name")
        client_name.text = kwargs.pop('client_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_time_remaining(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        time_remaining = ET.SubElement(pending_subscription_sync, "time-remaining")
        time_remaining.text = kwargs.pop('time_remaining')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_notification_queue_notification_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_notification_queue = ET.SubElement(datastore, "pending-notification-queue")
        notification = ET.SubElement(pending_notification_queue, "notification")
        priority = ET.SubElement(notification, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_notification_queue_notification_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_notification_queue = ET.SubElement(datastore, "pending-notification-queue")
        notification = ET.SubElement(pending_notification_queue, "notification")
        client_name = ET.SubElement(notification, "client-name")
        client_name.text = kwargs.pop('client_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        name = ET.SubElement(client, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        info = ET.SubElement(client, "info")
        info.text = kwargs.pop('info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        type = ET.SubElement(client, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        datastore = ET.SubElement(client, "datastore")
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_lock(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        lock = ET.SubElement(client, "lock")
        lock.text = kwargs.pop('lock')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        datastore = ET.SubElement(subscription, "datastore")
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_twophase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        twophase = ET.SubElement(subscription, "twophase")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        priority = ET.SubElement(subscription, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        id = ET.SubElement(subscription, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        path = ET.SubElement(subscription, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        error = ET.SubElement(subscription, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        version = ET.SubElement(confd_state, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_smp_number_of_threads(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        smp = ET.SubElement(confd_state, "smp")
        number_of_threads = ET.SubElement(smp, "number-of-threads")
        number_of_threads.text = kwargs.pop('number_of_threads')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_epoll(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        epoll = ET.SubElement(confd_state, "epoll")
        epoll.text = kwargs.pop('epoll')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_daemon_status(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        daemon_status = ET.SubElement(confd_state, "daemon-status")
        daemon_status.text = kwargs.pop('daemon_status')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_read_only_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        read_only_mode = ET.SubElement(confd_state, "read-only-mode")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_upgrade_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        upgrade_mode = ET.SubElement(confd_state, "upgrade-mode")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_mode(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        ha = ET.SubElement(confd_state, "ha")
        mode = ET.SubElement(ha, "mode")
        mode.text = kwargs.pop('mode')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_node_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        ha = ET.SubElement(confd_state, "ha")
        node_id = ET.SubElement(ha, "node-id")
        node_id.text = kwargs.pop('node_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_ha_master_node_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        ha = ET.SubElement(confd_state, "ha")
        master_node_id = ET.SubElement(ha, "master-node-id")
        master_node_id.text = kwargs.pop('master_node_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name = ET.SubElement(data_model, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_revision(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        revision = ET.SubElement(data_model, "revision")
        revision.text = kwargs.pop('revision')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_namespace(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        namespace = ET.SubElement(data_model, "namespace")
        namespace.text = kwargs.pop('namespace')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_prefix(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        prefix = ET.SubElement(data_model, "prefix")
        prefix.text = kwargs.pop('prefix')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_loaded_data_models_data_model_exported_exported_to_all_exported_to_all(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        loaded_data_models = ET.SubElement(confd_state, "loaded-data-models")
        data_model = ET.SubElement(loaded_data_models, "data-model")
        name_key = ET.SubElement(data_model, "name")
        name_key.text = kwargs.pop('name')
        exported = ET.SubElement(data_model, "exported")
        exported_to_all = ET.SubElement(exported, "exported-to-all")
        exported_to_all = ET.SubElement(exported_to_all, "exported-to-all")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        tcp = ET.SubElement(listen, "tcp")
        ip = ET.SubElement(tcp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        tcp = ET.SubElement(listen, "tcp")
        port = ET.SubElement(tcp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_ssh_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        ssh = ET.SubElement(listen, "ssh")
        ip = ET.SubElement(ssh, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_netconf_listen_ssh_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        netconf = ET.SubElement(confd_state, "netconf")
        listen = ET.SubElement(netconf, "listen")
        ssh = ET.SubElement(listen, "ssh")
        port = ET.SubElement(ssh, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_cli_listen_ssh_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        cli = ET.SubElement(confd_state, "cli")
        listen = ET.SubElement(cli, "listen")
        ssh = ET.SubElement(listen, "ssh")
        ip = ET.SubElement(ssh, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_cli_listen_ssh_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        cli = ET.SubElement(confd_state, "cli")
        listen = ET.SubElement(cli, "listen")
        ssh = ET.SubElement(listen, "ssh")
        port = ET.SubElement(ssh, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        tcp = ET.SubElement(listen, "tcp")
        ip = ET.SubElement(tcp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        tcp = ET.SubElement(listen, "tcp")
        port = ET.SubElement(tcp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_ssl_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        ssl = ET.SubElement(listen, "ssl")
        ip = ET.SubElement(ssl, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_webui_listen_ssl_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        webui = ET.SubElement(confd_state, "webui")
        listen = ET.SubElement(webui, "listen")
        ssl = ET.SubElement(listen, "ssl")
        port = ET.SubElement(ssl, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_tcp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        tcp = ET.SubElement(listen, "tcp")
        ip = ET.SubElement(tcp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_tcp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        tcp = ET.SubElement(listen, "tcp")
        port = ET.SubElement(tcp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_ssl_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        ssl = ET.SubElement(listen, "ssl")
        ip = ET.SubElement(ssl, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_rest_listen_ssl_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        rest = ET.SubElement(confd_state, "rest")
        listen = ET.SubElement(rest, "listen")
        ssl = ET.SubElement(listen, "ssl")
        port = ET.SubElement(ssl, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_listen_udp_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        listen = ET.SubElement(snmp, "listen")
        udp = ET.SubElement(listen, "udp")
        ip = ET.SubElement(udp, "ip")
        ip.text = kwargs.pop('ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_listen_udp_port(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        listen = ET.SubElement(snmp, "listen")
        udp = ET.SubElement(listen, "udp")
        port = ET.SubElement(udp, "port")
        port.text = kwargs.pop('port')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        version = ET.SubElement(snmp, "version")
        v1 = ET.SubElement(version, "v1")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v2c(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        version = ET.SubElement(snmp, "version")
        v2c = ET.SubElement(version, "v2c")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_version_v3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        version = ET.SubElement(snmp, "version")
        v3 = ET.SubElement(version, "v3")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_snmp_engine_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        snmp = ET.SubElement(confd_state, "snmp")
        engine_id = ET.SubElement(snmp, "engine-id")
        engine_id.text = kwargs.pop('engine_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id = ET.SubElement(callpoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(callpoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_callpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        callpoint = ET.SubElement(callpoints, "callpoint")
        id_key = ET.SubElement(callpoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(callpoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id = ET.SubElement(validationpoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(validationpoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_validationpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        validationpoint = ET.SubElement(callpoints, "validationpoint")
        id_key = ET.SubElement(validationpoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(validationpoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id = ET.SubElement(actionpoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(actionpoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_actionpoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        actionpoint = ET.SubElement(callpoints, "actionpoint")
        id_key = ET.SubElement(actionpoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(actionpoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id = ET.SubElement(snmp_inform_callback, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_inform_callback, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_inform_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_inform_callback = ET.SubElement(callpoints, "snmp-inform-callback")
        id_key = ET.SubElement(snmp_inform_callback, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(snmp_inform_callback, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id = ET.SubElement(snmp_notification_subscription, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(snmp_notification_subscription, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_snmp_notification_subscription_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        snmp_notification_subscription = ET.SubElement(callpoints, "snmp-notification-subscription")
        id_key = ET.SubElement(snmp_notification_subscription, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(snmp_notification_subscription, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id = ET.SubElement(error_formatting_callback, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(error_formatting_callback, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_error_formatting_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        error_formatting_callback = ET.SubElement(callpoints, "error-formatting-callback")
        id_key = ET.SubElement(error_formatting_callback, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(error_formatting_callback, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id = ET.SubElement(typepoint, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        registration_type = ET.SubElement(typepoint, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_typepoint_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        typepoint = ET.SubElement(callpoints, "typepoint")
        id_key = ET.SubElement(typepoint, "id")
        id_key.text = kwargs.pop('id')
        error = ET.SubElement(typepoint, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name = ET.SubElement(notification_stream_replay, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_replay_support(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        replay_support = ET.SubElement(notification_stream_replay, "replay-support")
        replay_support.text = kwargs.pop('replay_support')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        registration_type = ET.SubElement(notification_stream_replay, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_notification_stream_replay_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        notification_stream_replay = ET.SubElement(callpoints, "notification-stream-replay")
        name_key = ET.SubElement(notification_stream_replay, "name")
        name_key.text = kwargs.pop('name')
        error = ET.SubElement(notification_stream_replay, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        enabled = ET.SubElement(authentication_callback, "enabled")
        enabled.text = kwargs.pop('enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        registration_type = ET.SubElement(authentication_callback, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authentication_callback_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authentication_callback = ET.SubElement(callpoints, "authentication-callback")
        error = ET.SubElement(authentication_callback, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_enabled(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        enabled = ET.SubElement(authorization_callbacks, "enabled")
        enabled.text = kwargs.pop('enabled')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_daemon_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        daemon = ET.SubElement(registration_type, "daemon")
        daemon = ET.SubElement(daemon, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        path = ET.SubElement(range, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_lower(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        lower = ET.SubElement(range, "lower")
        lower.text = kwargs.pop('lower')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_upper(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        upper = ET.SubElement(range, "upper")
        upper.text = kwargs.pop('upper')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_default(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        default = ET.SubElement(range, "default")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        id = ET.SubElement(daemon, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        name = ET.SubElement(daemon, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_range_range_daemon_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        range = ET.SubElement(registration_type, "range")
        range = ET.SubElement(range, "range")
        daemon = ET.SubElement(range, "daemon")
        error = ET.SubElement(daemon, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_registration_type_file_file(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        registration_type = ET.SubElement(authorization_callbacks, "registration-type")
        file = ET.SubElement(registration_type, "file")
        file = ET.SubElement(file, "file")
        file.text = kwargs.pop('file')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_callpoints_authorization_callbacks_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        callpoints = ET.SubElement(internal, "callpoints")
        authorization_callbacks = ET.SubElement(callpoints, "authorization-callbacks")
        error = ET.SubElement(authorization_callbacks, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name = ET.SubElement(datastore, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_transaction_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        transaction_id = ET.SubElement(datastore, "transaction-id")
        transaction_id.text = kwargs.pop('transaction_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_write_queue(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        write_queue = ET.SubElement(datastore, "write-queue")
        write_queue.text = kwargs.pop('write_queue')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_filename(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        filename = ET.SubElement(datastore, "filename")
        filename.text = kwargs.pop('filename')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_disk_size(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        disk_size = ET.SubElement(datastore, "disk-size")
        disk_size.text = kwargs.pop('disk_size')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_ram_size(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        ram_size = ET.SubElement(datastore, "ram-size")
        ram_size.text = kwargs.pop('ram_size')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_read_locks(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        read_locks = ET.SubElement(datastore, "read-locks")
        read_locks.text = kwargs.pop('read_locks')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_write_lock_set(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        write_lock_set = ET.SubElement(datastore, "write-lock-set")
        write_lock_set.text = kwargs.pop('write_lock_set')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_subscription_lock_set(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        subscription_lock_set = ET.SubElement(datastore, "subscription-lock-set")
        subscription_lock_set.text = kwargs.pop('subscription_lock_set')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_waiting_for_replication_sync(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        waiting_for_replication_sync = ET.SubElement(datastore, "waiting-for-replication-sync")
        waiting_for_replication_sync.text = kwargs.pop('waiting_for_replication_sync')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        priority = ET.SubElement(pending_subscription_sync, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_notification_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        notification = ET.SubElement(pending_subscription_sync, "notification")
        client_name = ET.SubElement(notification, "client-name")
        client_name.text = kwargs.pop('client_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_subscription_sync_time_remaining(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_subscription_sync = ET.SubElement(datastore, "pending-subscription-sync")
        time_remaining = ET.SubElement(pending_subscription_sync, "time-remaining")
        time_remaining.text = kwargs.pop('time_remaining')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_notification_queue_notification_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_notification_queue = ET.SubElement(datastore, "pending-notification-queue")
        notification = ET.SubElement(pending_notification_queue, "notification")
        priority = ET.SubElement(notification, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_datastore_pending_notification_queue_notification_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        datastore = ET.SubElement(cdb, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        pending_notification_queue = ET.SubElement(datastore, "pending-notification-queue")
        notification = ET.SubElement(pending_notification_queue, "notification")
        client_name = ET.SubElement(notification, "client-name")
        client_name.text = kwargs.pop('client_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        name = ET.SubElement(client, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_info(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        info = ET.SubElement(client, "info")
        info.text = kwargs.pop('info')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        type = ET.SubElement(client, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        datastore = ET.SubElement(client, "datastore")
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_lock(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        lock = ET.SubElement(client, "lock")
        lock.text = kwargs.pop('lock')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_datastore(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        datastore = ET.SubElement(subscription, "datastore")
        datastore.text = kwargs.pop('datastore')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_twophase(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        twophase = ET.SubElement(subscription, "twophase")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_priority(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        priority = ET.SubElement(subscription, "priority")
        priority.text = kwargs.pop('priority')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        id = ET.SubElement(subscription, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_path(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        path = ET.SubElement(subscription, "path")
        path.text = kwargs.pop('path')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def confd_state_internal_cdb_client_subscription_error(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        confd_state = ET.SubElement(config, "confd-state", xmlns="http://tail-f.com/yang/confd-monitoring")
        internal = ET.SubElement(confd_state, "internal")
        cdb = ET.SubElement(internal, "cdb")
        client = ET.SubElement(cdb, "client")
        subscription = ET.SubElement(client, "subscription")
        error = ET.SubElement(subscription, "error")
        error.text = kwargs.pop('error')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        