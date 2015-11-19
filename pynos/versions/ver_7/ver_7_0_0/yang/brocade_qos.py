#!/usr/bin/env python
import xml.etree.ElementTree as ET


class brocade_qos(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def qos_map_dscp_mutation_dscp_mutation_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation_map_name = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name.text = kwargs.pop('dscp_mutation_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation_map_name_key = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name_key.text = kwargs.pop('dscp_mutation_map_name')
        mark = ET.SubElement(dscp_mutation, "mark")
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation_map_name_key = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name_key.text = kwargs.pop('dscp_mutation_map_name')
        mark = ET.SubElement(dscp_mutation, "mark")
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        to = ET.SubElement(mark, "to")
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_dscp_traffic_class_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class_map_name = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name.text = kwargs.pop('dscp_traffic_class_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class_map_name_key = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name_key.text = kwargs.pop('dscp_traffic_class_map_name')
        mark = ET.SubElement(dscp_traffic_class, "mark")
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class_map_name_key = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name_key.text = kwargs.pop('dscp_traffic_class_map_name')
        mark = ET.SubElement(dscp_traffic_class, "mark")
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        to = ET.SubElement(mark, "to")
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_dscp_cos_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos_map_name = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name.text = kwargs.pop('dscp_cos_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos_map_name_key = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name_key.text = kwargs.pop('dscp_cos_map_name')
        mark = ET.SubElement(dscp_cos, "mark")
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos_map_name_key = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name_key.text = kwargs.pop('dscp_cos_map_name')
        mark = ET.SubElement(dscp_cos, "mark")
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        to = ET.SubElement(mark, "to")
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name = ET.SubElement(cos_mutation, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos0 = ET.SubElement(cos_mutation, "cos0")
        cos0.text = kwargs.pop('cos0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos1 = ET.SubElement(cos_mutation, "cos1")
        cos1.text = kwargs.pop('cos1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos2 = ET.SubElement(cos_mutation, "cos2")
        cos2.text = kwargs.pop('cos2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos3 = ET.SubElement(cos_mutation, "cos3")
        cos3.text = kwargs.pop('cos3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos4 = ET.SubElement(cos_mutation, "cos4")
        cos4.text = kwargs.pop('cos4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos5 = ET.SubElement(cos_mutation, "cos5")
        cos5.text = kwargs.pop('cos5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos6 = ET.SubElement(cos_mutation, "cos6")
        cos6.text = kwargs.pop('cos6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos7 = ET.SubElement(cos_mutation, "cos7")
        cos7.text = kwargs.pop('cos7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name = ET.SubElement(cos_traffic_class, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos0 = ET.SubElement(cos_traffic_class, "cos0")
        cos0.text = kwargs.pop('cos0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos1 = ET.SubElement(cos_traffic_class, "cos1")
        cos1.text = kwargs.pop('cos1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos2 = ET.SubElement(cos_traffic_class, "cos2")
        cos2.text = kwargs.pop('cos2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos3 = ET.SubElement(cos_traffic_class, "cos3")
        cos3.text = kwargs.pop('cos3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos4 = ET.SubElement(cos_traffic_class, "cos4")
        cos4.text = kwargs.pop('cos4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos5 = ET.SubElement(cos_traffic_class, "cos5")
        cos5.text = kwargs.pop('cos5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos6 = ET.SubElement(cos_traffic_class, "cos6")
        cos6.text = kwargs.pop('cos6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos7 = ET.SubElement(cos_traffic_class, "cos7")
        cos7.text = kwargs.pop('cos7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_profile_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id = ET.SubElement(red_profile, "profile-id")
        profile_id.text = kwargs.pop('profile_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_min_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        min_threshold = ET.SubElement(red_profile, "min-threshold")
        min_threshold.text = kwargs.pop('min_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_max_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        max_threshold = ET.SubElement(red_profile, "max-threshold")
        max_threshold.text = kwargs.pop('max_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_drop_probability(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        drop_probability = ET.SubElement(red_profile, "drop-probability")
        drop_probability.text = kwargs.pop('drop_probability')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class0 = ET.SubElement(dwrr, "dwrr-traffic-class0")
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class1 = ET.SubElement(dwrr, "dwrr-traffic-class1")
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class2 = ET.SubElement(dwrr, "dwrr-traffic-class2")
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class3 = ET.SubElement(dwrr, "dwrr-traffic-class3")
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class4 = ET.SubElement(dwrr, "dwrr-traffic-class4")
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class5 = ET.SubElement(dwrr, "dwrr-traffic-class5")
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class6 = ET.SubElement(dwrr, "dwrr-traffic-class6")
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class7 = ET.SubElement(dwrr, "dwrr-traffic-class7")
        dwrr_traffic_class7.text = kwargs.pop('dwrr_traffic_class7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_priority_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        priority_number = ET.SubElement(strict_priority, "priority-number")
        priority_number.text = kwargs.pop('priority_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_scheduler_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        scheduler_type = ET.SubElement(strict_priority, "scheduler-type")
        scheduler_type.text = kwargs.pop('scheduler_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class0 = ET.SubElement(strict_priority, "dwrr-traffic-class0")
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class1 = ET.SubElement(strict_priority, "dwrr-traffic-class1")
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class2 = ET.SubElement(strict_priority, "dwrr-traffic-class2")
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class3 = ET.SubElement(strict_priority, "dwrr-traffic-class3")
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class4 = ET.SubElement(strict_priority, "dwrr-traffic-class4")
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class5 = ET.SubElement(strict_priority, "dwrr-traffic-class5")
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class6 = ET.SubElement(strict_priority, "dwrr-traffic-class6")
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class_last(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class_last = ET.SubElement(strict_priority, "dwrr-traffic-class-last")
        dwrr_traffic_class_last.text = kwargs.pop('dwrr_traffic_class_last')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class0 = ET.SubElement(threshold, "traffic-class0")
        traffic_class0.text = kwargs.pop('traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class1 = ET.SubElement(threshold, "traffic-class1")
        traffic_class1.text = kwargs.pop('traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class2 = ET.SubElement(threshold, "traffic-class2")
        traffic_class2.text = kwargs.pop('traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class3 = ET.SubElement(threshold, "traffic-class3")
        traffic_class3.text = kwargs.pop('traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class4 = ET.SubElement(threshold, "traffic-class4")
        traffic_class4.text = kwargs.pop('traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class5 = ET.SubElement(threshold, "traffic-class5")
        traffic_class5.text = kwargs.pop('traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class6 = ET.SubElement(threshold, "traffic-class6")
        traffic_class6.text = kwargs.pop('traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class7 = ET.SubElement(threshold, "traffic-class7")
        traffic_class7.text = kwargs.pop('traffic_class7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_rate_limit_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        rate_limit = ET.SubElement(multicast, "rate-limit")
        limit = ET.SubElement(rate_limit, "limit")
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_rate_limit_burst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        rate_limit = ET.SubElement(multicast, "rate-limit")
        burst = ET.SubElement(rate_limit, "burst")
        burst.text = kwargs.pop('burst')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_auto_qos_set_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        auto_qos = ET.SubElement(nas, "auto-qos")
        set = ET.SubElement(auto_qos, "set")
        cos = ET.SubElement(set, "cos")
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_auto_qos_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        auto_qos = ET.SubElement(nas, "auto-qos")
        set = ET.SubElement(auto_qos, "set")
        dscp = ET.SubElement(set, "dscp")
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        server_ip = ET.SubElement(nas, "server-ip")
        server_ip = ET.SubElement(server_ip, "server-ip")
        server_ip.text = kwargs.pop('server_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_vrf_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        server_ip = ET.SubElement(nas, "server-ip")
        server_ip_key = ET.SubElement(server_ip, "server-ip")
        server_ip_key.text = kwargs.pop('server_ip')
        vrf = ET.SubElement(server_ip, "vrf")
        vrf_name = ET.SubElement(vrf, "vrf-name")
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_vlan_vlan_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        server_ip = ET.SubElement(nas, "server-ip")
        server_ip_key = ET.SubElement(server_ip, "server-ip")
        server_ip_key.text = kwargs.pop('server_ip')
        vlan = ET.SubElement(server_ip, "vlan")
        vlan_number = ET.SubElement(vlan, "vlan-number")
        vlan_number.text = kwargs.pop('vlan_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_dscp_mutation_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation_map_name = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name.text = kwargs.pop('dscp_mutation_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation_map_name_key = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name_key.text = kwargs.pop('dscp_mutation_map_name')
        mark = ET.SubElement(dscp_mutation, "mark")
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_mutation_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_mutation = ET.SubElement(map, "dscp-mutation")
        dscp_mutation_map_name_key = ET.SubElement(dscp_mutation, "dscp-mutation-map-name")
        dscp_mutation_map_name_key.text = kwargs.pop('dscp_mutation_map_name')
        mark = ET.SubElement(dscp_mutation, "mark")
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        to = ET.SubElement(mark, "to")
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_dscp_traffic_class_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class_map_name = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name.text = kwargs.pop('dscp_traffic_class_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class_map_name_key = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name_key.text = kwargs.pop('dscp_traffic_class_map_name')
        mark = ET.SubElement(dscp_traffic_class, "mark")
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_traffic_class_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_traffic_class = ET.SubElement(map, "dscp-traffic-class")
        dscp_traffic_class_map_name_key = ET.SubElement(dscp_traffic_class, "dscp-traffic-class-map-name")
        dscp_traffic_class_map_name_key.text = kwargs.pop('dscp_traffic_class_map_name')
        mark = ET.SubElement(dscp_traffic_class, "mark")
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        to = ET.SubElement(mark, "to")
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_dscp_cos_map_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos_map_name = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name.text = kwargs.pop('dscp_cos_map_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_mark_dscp_in_values(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos_map_name_key = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name_key.text = kwargs.pop('dscp_cos_map_name')
        mark = ET.SubElement(dscp_cos, "mark")
        dscp_in_values = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values.text = kwargs.pop('dscp_in_values')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_dscp_cos_mark_to(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        dscp_cos = ET.SubElement(map, "dscp-cos")
        dscp_cos_map_name_key = ET.SubElement(dscp_cos, "dscp-cos-map-name")
        dscp_cos_map_name_key.text = kwargs.pop('dscp_cos_map_name')
        mark = ET.SubElement(dscp_cos, "mark")
        dscp_in_values_key = ET.SubElement(mark, "dscp-in-values")
        dscp_in_values_key.text = kwargs.pop('dscp_in_values')
        to = ET.SubElement(mark, "to")
        to.text = kwargs.pop('to')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name = ET.SubElement(cos_mutation, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos0 = ET.SubElement(cos_mutation, "cos0")
        cos0.text = kwargs.pop('cos0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos1 = ET.SubElement(cos_mutation, "cos1")
        cos1.text = kwargs.pop('cos1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos2 = ET.SubElement(cos_mutation, "cos2")
        cos2.text = kwargs.pop('cos2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos3 = ET.SubElement(cos_mutation, "cos3")
        cos3.text = kwargs.pop('cos3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos4 = ET.SubElement(cos_mutation, "cos4")
        cos4.text = kwargs.pop('cos4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos5 = ET.SubElement(cos_mutation, "cos5")
        cos5.text = kwargs.pop('cos5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos6 = ET.SubElement(cos_mutation, "cos6")
        cos6.text = kwargs.pop('cos6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_mutation_cos7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_mutation = ET.SubElement(map, "cos-mutation")
        name_key = ET.SubElement(cos_mutation, "name")
        name_key.text = kwargs.pop('name')
        cos7 = ET.SubElement(cos_mutation, "cos7")
        cos7.text = kwargs.pop('cos7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name = ET.SubElement(cos_traffic_class, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos0 = ET.SubElement(cos_traffic_class, "cos0")
        cos0.text = kwargs.pop('cos0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos1 = ET.SubElement(cos_traffic_class, "cos1")
        cos1.text = kwargs.pop('cos1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos2 = ET.SubElement(cos_traffic_class, "cos2")
        cos2.text = kwargs.pop('cos2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos3 = ET.SubElement(cos_traffic_class, "cos3")
        cos3.text = kwargs.pop('cos3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos4 = ET.SubElement(cos_traffic_class, "cos4")
        cos4.text = kwargs.pop('cos4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos5 = ET.SubElement(cos_traffic_class, "cos5")
        cos5.text = kwargs.pop('cos5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos6 = ET.SubElement(cos_traffic_class, "cos6")
        cos6.text = kwargs.pop('cos6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_map_cos_traffic_class_cos7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        map = ET.SubElement(qos, "map")
        cos_traffic_class = ET.SubElement(map, "cos-traffic-class")
        name_key = ET.SubElement(cos_traffic_class, "name")
        name_key.text = kwargs.pop('name')
        cos7 = ET.SubElement(cos_traffic_class, "cos7")
        cos7.text = kwargs.pop('cos7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_profile_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id = ET.SubElement(red_profile, "profile-id")
        profile_id.text = kwargs.pop('profile_id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_min_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        min_threshold = ET.SubElement(red_profile, "min-threshold")
        min_threshold.text = kwargs.pop('min_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_max_threshold(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        max_threshold = ET.SubElement(red_profile, "max-threshold")
        max_threshold.text = kwargs.pop('max_threshold')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_red_profile_drop_probability(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        red_profile = ET.SubElement(qos, "red-profile")
        profile_id_key = ET.SubElement(red_profile, "profile-id")
        profile_id_key.text = kwargs.pop('profile_id')
        drop_probability = ET.SubElement(red_profile, "drop-probability")
        drop_probability.text = kwargs.pop('drop_probability')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class0 = ET.SubElement(dwrr, "dwrr-traffic-class0")
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class1 = ET.SubElement(dwrr, "dwrr-traffic-class1")
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class2 = ET.SubElement(dwrr, "dwrr-traffic-class2")
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class3 = ET.SubElement(dwrr, "dwrr-traffic-class3")
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class4 = ET.SubElement(dwrr, "dwrr-traffic-class4")
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class5 = ET.SubElement(dwrr, "dwrr-traffic-class5")
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class6 = ET.SubElement(dwrr, "dwrr-traffic-class6")
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_multicast_scheduler_dwrr_dwrr_traffic_class7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        multicast = ET.SubElement(queue, "multicast")
        scheduler = ET.SubElement(multicast, "scheduler")
        dwrr = ET.SubElement(scheduler, "dwrr")
        dwrr_traffic_class7 = ET.SubElement(dwrr, "dwrr-traffic-class7")
        dwrr_traffic_class7.text = kwargs.pop('dwrr_traffic_class7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_priority_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        priority_number = ET.SubElement(strict_priority, "priority-number")
        priority_number.text = kwargs.pop('priority_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_scheduler_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        scheduler_type = ET.SubElement(strict_priority, "scheduler-type")
        scheduler_type.text = kwargs.pop('scheduler_type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class0 = ET.SubElement(strict_priority, "dwrr-traffic-class0")
        dwrr_traffic_class0.text = kwargs.pop('dwrr_traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class1 = ET.SubElement(strict_priority, "dwrr-traffic-class1")
        dwrr_traffic_class1.text = kwargs.pop('dwrr_traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class2 = ET.SubElement(strict_priority, "dwrr-traffic-class2")
        dwrr_traffic_class2.text = kwargs.pop('dwrr_traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class3 = ET.SubElement(strict_priority, "dwrr-traffic-class3")
        dwrr_traffic_class3.text = kwargs.pop('dwrr_traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class4 = ET.SubElement(strict_priority, "dwrr-traffic-class4")
        dwrr_traffic_class4.text = kwargs.pop('dwrr_traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class5 = ET.SubElement(strict_priority, "dwrr-traffic-class5")
        dwrr_traffic_class5.text = kwargs.pop('dwrr_traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class6 = ET.SubElement(strict_priority, "dwrr-traffic-class6")
        dwrr_traffic_class6.text = kwargs.pop('dwrr_traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_queue_scheduler_strict_priority_dwrr_traffic_class_last(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        queue = ET.SubElement(qos, "queue")
        scheduler = ET.SubElement(queue, "scheduler")
        strict_priority = ET.SubElement(scheduler, "strict-priority")
        dwrr_traffic_class_last = ET.SubElement(strict_priority, "dwrr-traffic-class-last")
        dwrr_traffic_class_last.text = kwargs.pop('dwrr_traffic_class_last')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class0(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class0 = ET.SubElement(threshold, "traffic-class0")
        traffic_class0.text = kwargs.pop('traffic_class0')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class1(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class1 = ET.SubElement(threshold, "traffic-class1")
        traffic_class1.text = kwargs.pop('traffic_class1')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class2(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class2 = ET.SubElement(threshold, "traffic-class2")
        traffic_class2.text = kwargs.pop('traffic_class2')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class3(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class3 = ET.SubElement(threshold, "traffic-class3")
        traffic_class3.text = kwargs.pop('traffic_class3')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class4(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class4 = ET.SubElement(threshold, "traffic-class4")
        traffic_class4.text = kwargs.pop('traffic_class4')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class5(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class5 = ET.SubElement(threshold, "traffic-class5")
        traffic_class5.text = kwargs.pop('traffic_class5')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class6(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class6 = ET.SubElement(threshold, "traffic-class6")
        traffic_class6.text = kwargs.pop('traffic_class6')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_threshold_traffic_class7(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        threshold = ET.SubElement(multicast, "threshold")
        traffic_class7 = ET.SubElement(threshold, "traffic-class7")
        traffic_class7.text = kwargs.pop('traffic_class7')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_rate_limit_limit(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        rate_limit = ET.SubElement(multicast, "rate-limit")
        limit = ET.SubElement(rate_limit, "limit")
        limit.text = kwargs.pop('limit')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def qos_rcv_queue_multicast_rate_limit_burst(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        qos = ET.SubElement(config, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
        rcv_queue = ET.SubElement(qos, "rcv-queue")
        multicast = ET.SubElement(rcv_queue, "multicast")
        rate_limit = ET.SubElement(multicast, "rate-limit")
        burst = ET.SubElement(rate_limit, "burst")
        burst.text = kwargs.pop('burst')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_auto_qos_set_cos(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        auto_qos = ET.SubElement(nas, "auto-qos")
        set = ET.SubElement(auto_qos, "set")
        cos = ET.SubElement(set, "cos")
        cos.text = kwargs.pop('cos')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_auto_qos_set_dscp(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        auto_qos = ET.SubElement(nas, "auto-qos")
        set = ET.SubElement(auto_qos, "set")
        dscp = ET.SubElement(set, "dscp")
        dscp.text = kwargs.pop('dscp')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_server_ip(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        server_ip = ET.SubElement(nas, "server-ip")
        server_ip = ET.SubElement(server_ip, "server-ip")
        server_ip.text = kwargs.pop('server_ip')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_vrf_vrf_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        server_ip = ET.SubElement(nas, "server-ip")
        server_ip_key = ET.SubElement(server_ip, "server-ip")
        server_ip_key.text = kwargs.pop('server_ip')
        vrf = ET.SubElement(server_ip, "vrf")
        vrf_name = ET.SubElement(vrf, "vrf-name")
        vrf_name.text = kwargs.pop('vrf_name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def nas_server_ip_vlan_vlan_number(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        nas = ET.SubElement(config, "nas", xmlns="urn:brocade.com:mgmt:brocade-qos")
        server_ip = ET.SubElement(nas, "server-ip")
        server_ip_key = ET.SubElement(server_ip, "server-ip")
        server_ip_key.text = kwargs.pop('server_ip')
        vlan = ET.SubElement(server_ip, "vlan")
        vlan_number = ET.SubElement(vlan, "vlan-number")
        vlan_number.text = kwargs.pop('vlan_number')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        