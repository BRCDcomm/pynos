#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf_monitoring(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def netconf_state_datastores_datastore_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name = ET.SubElement(datastore, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_global_lock_global_lock_locked_by_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        global_lock = ET.SubElement(lock_type, "global-lock")
        global_lock = ET.SubElement(global_lock, "global-lock")
        locked_by_session = ET.SubElement(global_lock, "locked-by-session")
        locked_by_session.text = kwargs.pop('locked_by_session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_global_lock_global_lock_locked_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        global_lock = ET.SubElement(lock_type, "global-lock")
        global_lock = ET.SubElement(global_lock, "global-lock")
        locked_time = ET.SubElement(global_lock, "locked-time")
        locked_time.text = kwargs.pop('locked_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_lock_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        lock_id = ET.SubElement(partial_lock, "lock-id")
        lock_id.text = kwargs.pop('lock_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_locked_by_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        lock_id_key = ET.SubElement(partial_lock, "lock-id")
        lock_id_key.text = kwargs.pop('lock_id')
        locked_by_session = ET.SubElement(partial_lock, "locked-by-session")
        locked_by_session.text = kwargs.pop('locked_by_session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_locked_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        lock_id_key = ET.SubElement(partial_lock, "lock-id")
        lock_id_key.text = kwargs.pop('lock_id')
        locked_time = ET.SubElement(partial_lock, "locked-time")
        locked_time.text = kwargs.pop('locked_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_transaction_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        transaction_id = ET.SubElement(datastore, "transaction-id", xmlns="http://tail-f.com/yang/netconf-monitoring")
        transaction_id.text = kwargs.pop('transaction_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_identifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        identifier = ET.SubElement(schema, "identifier")
        identifier.text = kwargs.pop('identifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        version = ET.SubElement(schema, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_format(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        format = ET.SubElement(schema, "format")
        format.text = kwargs.pop('format')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_namespace(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        namespace = ET.SubElement(schema, "namespace")
        namespace.text = kwargs.pop('namespace')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id = ET.SubElement(session, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_transport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        transport = ET.SubElement(session, "transport")
        transport.text = kwargs.pop('transport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        username = ET.SubElement(session, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        source_host = ET.SubElement(session, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_login_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        login_time = ET.SubElement(session, "login-time")
        login_time.text = kwargs.pop('login_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_in_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        in_rpcs = ET.SubElement(session, "in-rpcs")
        in_rpcs.text = kwargs.pop('in_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_in_bad_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        in_bad_rpcs = ET.SubElement(session, "in-bad-rpcs")
        in_bad_rpcs.text = kwargs.pop('in_bad_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_out_rpc_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        out_rpc_errors = ET.SubElement(session, "out-rpc-errors")
        out_rpc_errors.text = kwargs.pop('out_rpc_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_out_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        out_notifications = ET.SubElement(session, "out-notifications")
        out_notifications.text = kwargs.pop('out_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_netconf_start_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        netconf_start_time = ET.SubElement(statistics, "netconf-start-time")
        netconf_start_time.text = kwargs.pop('netconf_start_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_bad_hellos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_bad_hellos = ET.SubElement(statistics, "in-bad-hellos")
        in_bad_hellos.text = kwargs.pop('in_bad_hellos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_sessions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_sessions = ET.SubElement(statistics, "in-sessions")
        in_sessions.text = kwargs.pop('in_sessions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_dropped_sessions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        dropped_sessions = ET.SubElement(statistics, "dropped-sessions")
        dropped_sessions.text = kwargs.pop('dropped_sessions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_rpcs = ET.SubElement(statistics, "in-rpcs")
        in_rpcs.text = kwargs.pop('in_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_bad_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_bad_rpcs = ET.SubElement(statistics, "in-bad-rpcs")
        in_bad_rpcs.text = kwargs.pop('in_bad_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_out_rpc_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        out_rpc_errors = ET.SubElement(statistics, "out-rpc-errors")
        out_rpc_errors.text = kwargs.pop('out_rpc_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_out_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        out_notifications = ET.SubElement(statistics, "out-notifications")
        out_notifications.text = kwargs.pop('out_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name = ET.SubElement(file, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_creator(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        creator = ET.SubElement(file, "creator")
        creator.text = kwargs.pop('creator')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_created(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        created = ET.SubElement(file, "created")
        created.text = kwargs.pop('created')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        context = ET.SubElement(file, "context")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_identifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        input = ET.SubElement(get_schema, "input")
        identifier = ET.SubElement(input, "identifier")
        identifier.text = kwargs.pop('identifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        input = ET.SubElement(get_schema, "input")
        version = ET.SubElement(input, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_format(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        input = ET.SubElement(get_schema, "input")
        format = ET.SubElement(input, "format")
        format.text = kwargs.pop('format')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name = ET.SubElement(datastore, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_global_lock_global_lock_locked_by_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        global_lock = ET.SubElement(lock_type, "global-lock")
        global_lock = ET.SubElement(global_lock, "global-lock")
        locked_by_session = ET.SubElement(global_lock, "locked-by-session")
        locked_by_session.text = kwargs.pop('locked_by_session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_global_lock_global_lock_locked_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        global_lock = ET.SubElement(lock_type, "global-lock")
        global_lock = ET.SubElement(global_lock, "global-lock")
        locked_time = ET.SubElement(global_lock, "locked-time")
        locked_time.text = kwargs.pop('locked_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_lock_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        lock_id = ET.SubElement(partial_lock, "lock-id")
        lock_id.text = kwargs.pop('lock_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_locked_by_session(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        lock_id_key = ET.SubElement(partial_lock, "lock-id")
        lock_id_key.text = kwargs.pop('lock_id')
        locked_by_session = ET.SubElement(partial_lock, "locked-by-session")
        locked_by_session.text = kwargs.pop('locked_by_session')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_locks_lock_type_partial_lock_partial_lock_locked_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        locks = ET.SubElement(datastore, "locks")
        lock_type = ET.SubElement(locks, "lock-type")
        partial_lock = ET.SubElement(lock_type, "partial-lock")
        partial_lock = ET.SubElement(partial_lock, "partial-lock")
        lock_id_key = ET.SubElement(partial_lock, "lock-id")
        lock_id_key.text = kwargs.pop('lock_id')
        locked_time = ET.SubElement(partial_lock, "locked-time")
        locked_time.text = kwargs.pop('locked_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_datastores_datastore_transaction_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        datastores = ET.SubElement(netconf_state, "datastores")
        datastore = ET.SubElement(datastores, "datastore")
        name_key = ET.SubElement(datastore, "name")
        name_key.text = kwargs.pop('name')
        transaction_id = ET.SubElement(datastore, "transaction-id", xmlns="http://tail-f.com/yang/netconf-monitoring")
        transaction_id.text = kwargs.pop('transaction_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_identifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        identifier = ET.SubElement(schema, "identifier")
        identifier.text = kwargs.pop('identifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        version = ET.SubElement(schema, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_format(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        format = ET.SubElement(schema, "format")
        format.text = kwargs.pop('format')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_schemas_schema_namespace(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        schemas = ET.SubElement(netconf_state, "schemas")
        schema = ET.SubElement(schemas, "schema")
        identifier_key = ET.SubElement(schema, "identifier")
        identifier_key.text = kwargs.pop('identifier')
        version_key = ET.SubElement(schema, "version")
        version_key.text = kwargs.pop('version')
        format_key = ET.SubElement(schema, "format")
        format_key.text = kwargs.pop('format')
        namespace = ET.SubElement(schema, "namespace")
        namespace.text = kwargs.pop('namespace')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id = ET.SubElement(session, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_transport(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        transport = ET.SubElement(session, "transport")
        transport.text = kwargs.pop('transport')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        username = ET.SubElement(session, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_source_host(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        source_host = ET.SubElement(session, "source-host")
        source_host.text = kwargs.pop('source_host')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_login_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        login_time = ET.SubElement(session, "login-time")
        login_time.text = kwargs.pop('login_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_in_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        in_rpcs = ET.SubElement(session, "in-rpcs")
        in_rpcs.text = kwargs.pop('in_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_in_bad_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        in_bad_rpcs = ET.SubElement(session, "in-bad-rpcs")
        in_bad_rpcs.text = kwargs.pop('in_bad_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_out_rpc_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        out_rpc_errors = ET.SubElement(session, "out-rpc-errors")
        out_rpc_errors.text = kwargs.pop('out_rpc_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_sessions_session_out_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        sessions = ET.SubElement(netconf_state, "sessions")
        session = ET.SubElement(sessions, "session")
        session_id_key = ET.SubElement(session, "session-id")
        session_id_key.text = kwargs.pop('session_id')
        out_notifications = ET.SubElement(session, "out-notifications")
        out_notifications.text = kwargs.pop('out_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_netconf_start_time(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        netconf_start_time = ET.SubElement(statistics, "netconf-start-time")
        netconf_start_time.text = kwargs.pop('netconf_start_time')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_bad_hellos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_bad_hellos = ET.SubElement(statistics, "in-bad-hellos")
        in_bad_hellos.text = kwargs.pop('in_bad_hellos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_sessions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_sessions = ET.SubElement(statistics, "in-sessions")
        in_sessions.text = kwargs.pop('in_sessions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_dropped_sessions(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        dropped_sessions = ET.SubElement(statistics, "dropped-sessions")
        dropped_sessions.text = kwargs.pop('dropped_sessions')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_rpcs = ET.SubElement(statistics, "in-rpcs")
        in_rpcs.text = kwargs.pop('in_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_in_bad_rpcs(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        in_bad_rpcs = ET.SubElement(statistics, "in-bad-rpcs")
        in_bad_rpcs.text = kwargs.pop('in_bad_rpcs')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_out_rpc_errors(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        out_rpc_errors = ET.SubElement(statistics, "out-rpc-errors")
        out_rpc_errors.text = kwargs.pop('out_rpc_errors')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_statistics_out_notifications(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        statistics = ET.SubElement(netconf_state, "statistics")
        out_notifications = ET.SubElement(statistics, "out-notifications")
        out_notifications.text = kwargs.pop('out_notifications')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name = ET.SubElement(file, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_creator(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        creator = ET.SubElement(file, "creator")
        creator.text = kwargs.pop('creator')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_created(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        created = ET.SubElement(file, "created")
        created.text = kwargs.pop('created')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def netconf_state_files_file_context(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        netconf_state = ET.SubElement(config, "netconf-state", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring")
        files = ET.SubElement(netconf_state, "files", xmlns="http://tail-f.com/yang/netconf-monitoring")
        file = ET.SubElement(files, "file")
        name_key = ET.SubElement(file, "name")
        name_key.text = kwargs.pop('name')
        context = ET.SubElement(file, "context")
        context.text = kwargs.pop('context')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_identifier(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        input = ET.SubElement(get_schema, "input")
        identifier = ET.SubElement(input, "identifier")
        identifier.text = kwargs.pop('identifier')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_version(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        input = ET.SubElement(get_schema, "input")
        version = ET.SubElement(input, "version")
        version.text = kwargs.pop('version')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_schema_input_format(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_schema = ET.Element("get_schema")
        config = get_schema
        input = ET.SubElement(get_schema, "input")
        format = ET.SubElement(input, "format")
        format.text = kwargs.pop('format')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        