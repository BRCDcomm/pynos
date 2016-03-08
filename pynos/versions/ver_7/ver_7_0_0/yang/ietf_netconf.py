#!/usr/bin/env python
import xml.etree.ElementTree as ET


class ietf_netconf(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def get_config_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        candidate = ET.SubElement(config_source, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        running = ET.SubElement(config_source, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        startup = ET.SubElement(config_source, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_default_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        default_operation = ET.SubElement(input, "default-operation")
        default_operation.text = kwargs.pop('default_operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_test_option(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        test_option = ET.SubElement(input, "test-option")
        test_option.text = kwargs.pop('test_option')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_error_option(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        error_option = ET.SubElement(input, "error-option")
        error_option.text = kwargs.pop('error_option')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_edit_content_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        edit_content = ET.SubElement(input, "edit-content")
        url = ET.SubElement(edit_content, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        url = ET.SubElement(config_target, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        candidate = ET.SubElement(config_source, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        running = ET.SubElement(config_source, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        startup = ET.SubElement(config_source, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        url = ET.SubElement(config_source, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def delete_config_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        delete_config = ET.Element("delete_config")
        config = delete_config
        input = ET.SubElement(delete_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def delete_config_input_target_config_target_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        delete_config = ET.Element("delete_config")
        config = delete_config
        input = ET.SubElement(delete_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        url = ET.SubElement(config_target, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        input = ET.SubElement(lock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        input = ET.SubElement(lock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        input = ET.SubElement(lock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        input = ET.SubElement(unlock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        input = ET.SubElement(unlock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        input = ET.SubElement(unlock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get = ET.Element("get")
        config = get
        input = ET.SubElement(get, "input")
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def kill_session_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        kill_session = ET.Element("kill_session")
        config = kill_session
        input = ET.SubElement(kill_session, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_confirmed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        confirmed = ET.SubElement(input, "confirmed")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_confirm_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        confirm_timeout = ET.SubElement(input, "confirm-timeout")
        confirm_timeout.text = kwargs.pop('confirm_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_persist(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        persist = ET.SubElement(input, "persist")
        persist.text = kwargs.pop('persist')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_persist_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        persist_id = ET.SubElement(input, "persist-id")
        persist_id.text = kwargs.pop('persist_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cancel_commit_input_persist_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cancel_commit = ET.Element("cancel_commit")
        config = cancel_commit
        input = ET.SubElement(cancel_commit, "input")
        persist_id = ET.SubElement(input, "persist-id")
        persist_id.text = kwargs.pop('persist_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        candidate = ET.SubElement(config_source, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        running = ET.SubElement(config_source, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        startup = ET.SubElement(config_source, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        url = ET.SubElement(config_source, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        candidate = ET.SubElement(config_source, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        running = ET.SubElement(config_source, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        startup = ET.SubElement(config_source, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_config_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get_config = ET.Element("get_config")
        config = get_config
        input = ET.SubElement(get_config, "input")
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_default_operation(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        default_operation = ET.SubElement(input, "default-operation")
        default_operation.text = kwargs.pop('default_operation')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_test_option(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        test_option = ET.SubElement(input, "test-option")
        test_option.text = kwargs.pop('test_option')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_error_option(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        error_option = ET.SubElement(input, "error-option")
        error_option.text = kwargs.pop('error_option')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def edit_config_input_edit_content_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        edit_config = ET.Element("edit_config")
        config = edit_config
        input = ET.SubElement(edit_config, "input")
        edit_content = ET.SubElement(input, "edit-content")
        url = ET.SubElement(edit_content, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_target_config_target_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        url = ET.SubElement(config_target, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        candidate = ET.SubElement(config_source, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        running = ET.SubElement(config_source, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        startup = ET.SubElement(config_source, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_source_config_source_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        url = ET.SubElement(config_source, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def copy_config_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        copy_config = ET.Element("copy_config")
        config = copy_config
        input = ET.SubElement(copy_config, "input")
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def delete_config_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        delete_config = ET.Element("delete_config")
        config = delete_config
        input = ET.SubElement(delete_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def delete_config_input_target_config_target_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        delete_config = ET.Element("delete_config")
        config = delete_config
        input = ET.SubElement(delete_config, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        url = ET.SubElement(config_target, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        input = ET.SubElement(lock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        input = ET.SubElement(lock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def lock_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        lock = ET.Element("lock")
        config = lock
        input = ET.SubElement(lock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        input = ET.SubElement(unlock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        candidate = ET.SubElement(config_target, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        input = ET.SubElement(unlock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        running = ET.SubElement(config_target, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def unlock_input_target_config_target_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        unlock = ET.Element("unlock")
        config = unlock
        input = ET.SubElement(unlock, "input")
        target = ET.SubElement(input, "target")
        config_target = ET.SubElement(target, "config-target")
        startup = ET.SubElement(config_target, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def get_input_with_defaults(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        get = ET.Element("get")
        config = get
        input = ET.SubElement(get, "input")
        with_defaults = ET.SubElement(input, "with-defaults", xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults")
        with_defaults.text = kwargs.pop('with_defaults')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def kill_session_input_session_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        kill_session = ET.Element("kill_session")
        config = kill_session
        input = ET.SubElement(kill_session, "input")
        session_id = ET.SubElement(input, "session-id")
        session_id.text = kwargs.pop('session_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_confirmed(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        confirmed = ET.SubElement(input, "confirmed")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_confirm_timeout(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        confirm_timeout = ET.SubElement(input, "confirm-timeout")
        confirm_timeout.text = kwargs.pop('confirm_timeout')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_persist(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        persist = ET.SubElement(input, "persist")
        persist.text = kwargs.pop('persist')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def commit_input_persist_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        commit = ET.Element("commit")
        config = commit
        input = ET.SubElement(commit, "input")
        persist_id = ET.SubElement(input, "persist-id")
        persist_id.text = kwargs.pop('persist_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def cancel_commit_input_persist_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        cancel_commit = ET.Element("cancel_commit")
        config = cancel_commit
        input = ET.SubElement(cancel_commit, "input")
        persist_id = ET.SubElement(input, "persist-id")
        persist_id.text = kwargs.pop('persist_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_candidate_candidate(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        candidate = ET.SubElement(config_source, "candidate")
        candidate = ET.SubElement(candidate, "candidate")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_running_running(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        running = ET.SubElement(config_source, "running")
        running = ET.SubElement(running, "running")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_startup_startup(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        startup = ET.SubElement(config_source, "startup")
        startup = ET.SubElement(startup, "startup")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def validate_input_source_config_source_url_url(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        validate = ET.Element("validate")
        config = validate
        input = ET.SubElement(validate, "input")
        source = ET.SubElement(input, "source")
        config_source = ET.SubElement(source, "config-source")
        url = ET.SubElement(config_source, "url")
        url = ET.SubElement(url, "url")
        url.text = kwargs.pop('url')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        