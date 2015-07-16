#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_system_monitor(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def system_monitor_fan_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        threshold = ET.SubElement(fan, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        threshold = ET.SubElement(fan, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        alert = ET.SubElement(fan, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        alert = ET.SubElement(fan, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        threshold = ET.SubElement(power, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        threshold = ET.SubElement(power, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        alert = ET.SubElement(power, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        alert = ET.SubElement(power, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_temp_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        temp = ET.SubElement(system_monitor, "temp")
        threshold = ET.SubElement(temp, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_temp_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        temp = ET.SubElement(system_monitor, "temp")
        threshold = ET.SubElement(temp, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        threshold = ET.SubElement(cid_card, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        threshold = ET.SubElement(cid_card, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        alert = ET.SubElement(cid_card, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        alert = ET.SubElement(cid_card, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_sfp_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor, "sfp")
        alert = ET.SubElement(sfp, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_sfp_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor, "sfp")
        alert = ET.SubElement(sfp, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_compact_flash_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        compact_flash = ET.SubElement(system_monitor, "compact-flash")
        threshold = ET.SubElement(compact_flash, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_compact_flash_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        compact_flash = ET.SubElement(system_monitor, "compact-flash")
        threshold = ET.SubElement(compact_flash, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_MM_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        MM = ET.SubElement(system_monitor, "MM")
        threshold = ET.SubElement(MM, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_MM_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        MM = ET.SubElement(system_monitor, "MM")
        threshold = ET.SubElement(MM, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        threshold = ET.SubElement(LineCard, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        threshold = ET.SubElement(LineCard, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        alert = ET.SubElement(LineCard, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        alert = ET.SubElement(LineCard, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_SFM_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        SFM = ET.SubElement(system_monitor, "SFM")
        threshold = ET.SubElement(SFM, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_SFM_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        SFM = ET.SubElement(system_monitor, "SFM")
        threshold = ET.SubElement(SFM, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_fru_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fru = ET.SubElement(system_monitor_mail, "fru")
        enable = ET.SubElement(fru, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_fru_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fru = ET.SubElement(system_monitor_mail, "fru")
        email_list = ET.SubElement(fru, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_sfp_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor_mail, "sfp")
        enable = ET.SubElement(sfp, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_sfp_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor_mail, "sfp")
        email_list = ET.SubElement(sfp, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_security_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        security = ET.SubElement(system_monitor_mail, "security")
        enable = ET.SubElement(security, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_security_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        security = ET.SubElement(system_monitor_mail, "security")
        email_list = ET.SubElement(security, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_interface_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        interface = ET.SubElement(system_monitor_mail, "interface")
        enable = ET.SubElement(interface, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_interface_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        interface = ET.SubElement(system_monitor_mail, "interface")
        email_list = ET.SubElement(interface, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_relay_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        relay = ET.SubElement(system_monitor_mail, "relay")
        host_ip = ET.SubElement(relay, "host-ip")
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_relay_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        relay = ET.SubElement(system_monitor_mail, "relay")
        host_ip_key = ET.SubElement(relay, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        domain_name = ET.SubElement(relay, "domain-name")
        domain_name.text = kwargs.pop('domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        threshold = ET.SubElement(fan, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        threshold = ET.SubElement(fan, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        alert = ET.SubElement(fan, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_fan_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fan = ET.SubElement(system_monitor, "fan")
        alert = ET.SubElement(fan, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        threshold = ET.SubElement(power, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        threshold = ET.SubElement(power, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        alert = ET.SubElement(power, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_power_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        power = ET.SubElement(system_monitor, "power")
        alert = ET.SubElement(power, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_temp_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        temp = ET.SubElement(system_monitor, "temp")
        threshold = ET.SubElement(temp, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_temp_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        temp = ET.SubElement(system_monitor, "temp")
        threshold = ET.SubElement(temp, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        threshold = ET.SubElement(cid_card, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        threshold = ET.SubElement(cid_card, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        alert = ET.SubElement(cid_card, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_cid_card_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        cid_card = ET.SubElement(system_monitor, "cid-card")
        alert = ET.SubElement(cid_card, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_sfp_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor, "sfp")
        alert = ET.SubElement(sfp, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_sfp_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor, "sfp")
        alert = ET.SubElement(sfp, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_compact_flash_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        compact_flash = ET.SubElement(system_monitor, "compact-flash")
        threshold = ET.SubElement(compact_flash, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_compact_flash_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        compact_flash = ET.SubElement(system_monitor, "compact-flash")
        threshold = ET.SubElement(compact_flash, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_MM_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        MM = ET.SubElement(system_monitor, "MM")
        threshold = ET.SubElement(MM, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_MM_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        MM = ET.SubElement(system_monitor, "MM")
        threshold = ET.SubElement(MM, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        threshold = ET.SubElement(LineCard, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        threshold = ET.SubElement(LineCard, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_alert_state(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        alert = ET.SubElement(LineCard, "alert")
        state = ET.SubElement(alert, "state")
        state.text = kwargs.pop('state')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_LineCard_alert_action(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        LineCard = ET.SubElement(system_monitor, "LineCard")
        alert = ET.SubElement(LineCard, "alert")
        action = ET.SubElement(alert, "action")
        action.text = kwargs.pop('action')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_SFM_threshold_marginal_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        SFM = ET.SubElement(system_monitor, "SFM")
        threshold = ET.SubElement(SFM, "threshold")
        marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
        marginal_threshold.text = kwargs.pop('marginal_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_SFM_threshold_down_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor = ET.SubElement(config, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        SFM = ET.SubElement(system_monitor, "SFM")
        threshold = ET.SubElement(SFM, "threshold")
        down_threshold = ET.SubElement(threshold, "down-threshold")
        down_threshold.text = kwargs.pop('down_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_fru_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fru = ET.SubElement(system_monitor_mail, "fru")
        enable = ET.SubElement(fru, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_fru_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        fru = ET.SubElement(system_monitor_mail, "fru")
        email_list = ET.SubElement(fru, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_sfp_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor_mail, "sfp")
        enable = ET.SubElement(sfp, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_sfp_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        sfp = ET.SubElement(system_monitor_mail, "sfp")
        email_list = ET.SubElement(sfp, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_security_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        security = ET.SubElement(system_monitor_mail, "security")
        enable = ET.SubElement(security, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_security_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        security = ET.SubElement(system_monitor_mail, "security")
        email_list = ET.SubElement(security, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_interface_enable(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        interface = ET.SubElement(system_monitor_mail, "interface")
        enable = ET.SubElement(interface, "enable")

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_interface_email_list_email(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        interface = ET.SubElement(system_monitor_mail, "interface")
        email_list = ET.SubElement(interface, "email-list")
        email = ET.SubElement(email_list, "email")
        email.text = kwargs.pop('email')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_relay_host_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        relay = ET.SubElement(system_monitor_mail, "relay")
        host_ip = ET.SubElement(relay, "host-ip")
        host_ip.text = kwargs.pop('host_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def system_monitor_mail_relay_domain_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        system_monitor_mail = ET.SubElement(config, "system-monitor-mail", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
        relay = ET.SubElement(system_monitor_mail, "relay")
        host_ip_key = ET.SubElement(relay, "host-ip")
        host_ip_key.text = kwargs.pop('host_ip')
        domain_name = ET.SubElement(relay, "domain-name")
        domain_name.text = kwargs.pop('domain_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        