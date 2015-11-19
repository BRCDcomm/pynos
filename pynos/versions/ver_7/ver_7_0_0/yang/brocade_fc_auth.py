#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_fc_auth(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def fcsp_sa_fcsp_auth_proto_auth_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        proto = ET.SubElement(auth, "proto")
        auth_type = ET.SubElement(proto, "auth-type")
        auth_type.text = kwargs.pop('auth_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        proto = ET.SubElement(auth, "proto")
        group = ET.SubElement(proto, "group")
        group.text = kwargs.pop('group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_hash(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        proto = ET.SubElement(auth, "proto")
        hash = ET.SubElement(proto, "hash")
        hash.text = kwargs.pop('hash')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_policy_switch(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        policy = ET.SubElement(auth, "policy")
        switch = ET.SubElement(policy, "switch")
        switch.text = kwargs.pop('switch')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_defined_policy_policies_policy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        defined_policy = ET.SubElement(secpolicy, "defined-policy")
        policies = ET.SubElement(defined_policy, "policies")
        policy = ET.SubElement(policies, "policy")
        policy.text = kwargs.pop('policy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_defined_policy_policies_member_entry_member(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        defined_policy = ET.SubElement(secpolicy, "defined-policy")
        policies = ET.SubElement(defined_policy, "policies")
        policy_key = ET.SubElement(policies, "policy")
        policy_key.text = kwargs.pop('policy')
        member_entry = ET.SubElement(policies, "member-entry")
        member = ET.SubElement(member_entry, "member")
        member.text = kwargs.pop('member')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_active_policy_policies_policy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        active_policy = ET.SubElement(secpolicy, "active-policy")
        policies = ET.SubElement(active_policy, "policies")
        policy = ET.SubElement(policies, "policy")
        policy.text = kwargs.pop('policy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_active_policy_policies_member_entry_member(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        active_policy = ET.SubElement(secpolicy, "active-policy")
        policies = ET.SubElement(active_policy, "policies")
        policy_key = ET.SubElement(policies, "policy")
        policy_key.text = kwargs.pop('policy')
        member_entry = ET.SubElement(policies, "member-entry")
        member = ET.SubElement(member_entry, "member")
        member.text = kwargs.pop('member')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_auth_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        proto = ET.SubElement(auth, "proto")
        auth_type = ET.SubElement(proto, "auth-type")
        auth_type.text = kwargs.pop('auth_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_group(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        proto = ET.SubElement(auth, "proto")
        group = ET.SubElement(proto, "group")
        group.text = kwargs.pop('group')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_proto_hash(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        proto = ET.SubElement(auth, "proto")
        hash = ET.SubElement(proto, "hash")
        hash.text = kwargs.pop('hash')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def fcsp_sa_fcsp_auth_policy_switch(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        fcsp_sa = ET.SubElement(config, "fcsp-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        fcsp = ET.SubElement(fcsp_sa, "fcsp")
        auth = ET.SubElement(fcsp, "auth")
        policy = ET.SubElement(auth, "policy")
        switch = ET.SubElement(policy, "switch")
        switch.text = kwargs.pop('switch')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_defined_policy_policies_policy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        defined_policy = ET.SubElement(secpolicy, "defined-policy")
        policies = ET.SubElement(defined_policy, "policies")
        policy = ET.SubElement(policies, "policy")
        policy.text = kwargs.pop('policy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_defined_policy_policies_member_entry_member(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        defined_policy = ET.SubElement(secpolicy, "defined-policy")
        policies = ET.SubElement(defined_policy, "policies")
        policy_key = ET.SubElement(policies, "policy")
        policy_key.text = kwargs.pop('policy')
        member_entry = ET.SubElement(policies, "member-entry")
        member = ET.SubElement(member_entry, "member")
        member.text = kwargs.pop('member')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_active_policy_policies_policy(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        active_policy = ET.SubElement(secpolicy, "active-policy")
        policies = ET.SubElement(active_policy, "policies")
        policy = ET.SubElement(policies, "policy")
        policy.text = kwargs.pop('policy')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def secpolicy_sa_secpolicy_active_policy_policies_member_entry_member(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        secpolicy_sa = ET.SubElement(config, "secpolicy-sa", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
        secpolicy = ET.SubElement(secpolicy_sa, "secpolicy")
        active_policy = ET.SubElement(secpolicy, "active-policy")
        policies = ET.SubElement(active_policy, "policies")
        policy_key = ET.SubElement(policies, "policy")
        policy_key.text = kwargs.pop('policy')
        member_entry = ET.SubElement(policies, "member-entry")
        member = ET.SubElement(member_entry, "member")
        member.text = kwargs.pop('member')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        