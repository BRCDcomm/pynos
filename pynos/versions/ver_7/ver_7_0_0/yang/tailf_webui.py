#!/usr/bin/env python
import xml.etree.ElementTree as ET


class tailf_webui(object):
    """Auto generated class.
    """
    def __init__(self, **kwargs):
        self._callback = kwargs.pop('callback')

            
    def webui_schematics_panels_panel_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name = ET.SubElement(panel, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_title(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        title = ET.SubElement(properties, "title")
        title.text = kwargs.pop('title')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        description = ET.SubElement(properties, "description")
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_width(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        width = ET.SubElement(properties, "width")
        width.text = kwargs.pop('width')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_height(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        height = ET.SubElement(properties, "height")
        height.text = kwargs.pop('height')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id = ET.SubElement(component, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_top(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        top = ET.SubElement(properties, "top")
        top.text = kwargs.pop('top')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_left(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        left = ET.SubElement(properties, "left")
        left.text = kwargs.pop('left')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_width(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        width = ET.SubElement(properties, "width")
        width.text = kwargs.pop('width')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_height(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        height = ET.SubElement(properties, "height")
        height.text = kwargs.pop('height')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_z_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        z_index = ET.SubElement(properties, "z-index")
        z_index.text = kwargs.pop('z_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_image_image_image(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        component_type = ET.SubElement(properties, "component-type")
        image = ET.SubElement(component_type, "image")
        image = ET.SubElement(image, "image")
        image = ET.SubElement(image, "image")
        image.text = kwargs.pop('image')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_link_link_text(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        component_type = ET.SubElement(properties, "component-type")
        link = ET.SubElement(component_type, "link")
        link = ET.SubElement(link, "link")
        text = ET.SubElement(link, "text")
        text.text = kwargs.pop('text')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_link_link_link(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        component_type = ET.SubElement(properties, "component-type")
        link = ET.SubElement(component_type, "link")
        link = ET.SubElement(link, "link")
        link = ET.SubElement(link, "link")
        link.text = kwargs.pop('link')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        assets = ET.SubElement(schematics, "assets")
        asset = ET.SubElement(assets, "asset")
        name = ET.SubElement(asset, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_asset_type_image_base_64_image(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        assets = ET.SubElement(schematics, "assets")
        asset = ET.SubElement(assets, "asset")
        name_key = ET.SubElement(asset, "name")
        name_key.text = kwargs.pop('name')
        asset_type = ET.SubElement(asset, "asset-type")
        image = ET.SubElement(asset_type, "image")
        base_64_image = ET.SubElement(image, "base-64-image")
        base_64_image.text = kwargs.pop('base_64_image')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_asset_type_image_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        assets = ET.SubElement(schematics, "assets")
        asset = ET.SubElement(assets, "asset")
        name_key = ET.SubElement(asset, "name")
        name_key.text = kwargs.pop('name')
        asset_type = ET.SubElement(asset, "asset-type")
        image = ET.SubElement(asset_type, "image")
        type = ET.SubElement(image, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username = ET.SubElement(user_profile, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_profile_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        profile = ET.SubElement(user_profile, "profile")
        key = ET.SubElement(profile, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_profile_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        profile = ET.SubElement(user_profile, "profile")
        key_key = ET.SubElement(profile, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(profile, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_saved_query_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        saved_query = ET.SubElement(user_profile, "saved-query")
        key = ET.SubElement(saved_query, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_saved_query_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        saved_query = ET.SubElement(user_profile, "saved-query")
        key_key = ET.SubElement(saved_query, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(saved_query, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_data_store_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        data_store = ET.SubElement(data_stores, "data-store")
        key = ET.SubElement(data_store, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_data_store_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        data_store = ET.SubElement(data_stores, "data-store")
        key_key = ET.SubElement(data_store, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(data_store, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_saved_query_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        saved_query = ET.SubElement(data_stores, "saved-query")
        key = ET.SubElement(saved_query, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_saved_query_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        saved_query = ET.SubElement(data_stores, "saved-query")
        key_key = ET.SubElement(saved_query, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(saved_query, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name = ET.SubElement(panel, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_title(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        title = ET.SubElement(properties, "title")
        title.text = kwargs.pop('title')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_description(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        description = ET.SubElement(properties, "description")
        description.text = kwargs.pop('description')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_width(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        width = ET.SubElement(properties, "width")
        width.text = kwargs.pop('width')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_properties_height(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        properties = ET.SubElement(panel, "properties")
        height = ET.SubElement(properties, "height")
        height.text = kwargs.pop('height')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_id(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id = ET.SubElement(component, "id")
        id.text = kwargs.pop('id')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_top(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        top = ET.SubElement(properties, "top")
        top.text = kwargs.pop('top')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_left(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        left = ET.SubElement(properties, "left")
        left.text = kwargs.pop('left')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_width(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        width = ET.SubElement(properties, "width")
        width.text = kwargs.pop('width')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_height(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        height = ET.SubElement(properties, "height")
        height.text = kwargs.pop('height')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_z_index(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        z_index = ET.SubElement(properties, "z-index")
        z_index.text = kwargs.pop('z_index')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_image_image_image(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        component_type = ET.SubElement(properties, "component-type")
        image = ET.SubElement(component_type, "image")
        image = ET.SubElement(image, "image")
        image = ET.SubElement(image, "image")
        image.text = kwargs.pop('image')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_link_link_text(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        component_type = ET.SubElement(properties, "component-type")
        link = ET.SubElement(component_type, "link")
        link = ET.SubElement(link, "link")
        text = ET.SubElement(link, "text")
        text.text = kwargs.pop('text')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_panels_panel_components_component_properties_component_type_link_link_link(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        panels = ET.SubElement(schematics, "panels")
        panel = ET.SubElement(panels, "panel")
        name_key = ET.SubElement(panel, "name")
        name_key.text = kwargs.pop('name')
        components = ET.SubElement(panel, "components")
        component = ET.SubElement(components, "component")
        id_key = ET.SubElement(component, "id")
        id_key.text = kwargs.pop('id')
        properties = ET.SubElement(component, "properties")
        component_type = ET.SubElement(properties, "component-type")
        link = ET.SubElement(component_type, "link")
        link = ET.SubElement(link, "link")
        link = ET.SubElement(link, "link")
        link.text = kwargs.pop('link')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_name(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        assets = ET.SubElement(schematics, "assets")
        asset = ET.SubElement(assets, "asset")
        name = ET.SubElement(asset, "name")
        name.text = kwargs.pop('name')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_asset_type_image_base_64_image(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        assets = ET.SubElement(schematics, "assets")
        asset = ET.SubElement(assets, "asset")
        name_key = ET.SubElement(asset, "name")
        name_key.text = kwargs.pop('name')
        asset_type = ET.SubElement(asset, "asset-type")
        image = ET.SubElement(asset_type, "image")
        base_64_image = ET.SubElement(image, "base-64-image")
        base_64_image.text = kwargs.pop('base_64_image')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_schematics_assets_asset_asset_type_image_type(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        schematics = ET.SubElement(webui, "schematics")
        assets = ET.SubElement(schematics, "assets")
        asset = ET.SubElement(assets, "asset")
        name_key = ET.SubElement(asset, "name")
        name_key.text = kwargs.pop('name')
        asset_type = ET.SubElement(asset, "asset-type")
        image = ET.SubElement(asset_type, "image")
        type = ET.SubElement(image, "type")
        type.text = kwargs.pop('type')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_username(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username = ET.SubElement(user_profile, "username")
        username.text = kwargs.pop('username')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_profile_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        profile = ET.SubElement(user_profile, "profile")
        key = ET.SubElement(profile, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_profile_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        profile = ET.SubElement(user_profile, "profile")
        key_key = ET.SubElement(profile, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(profile, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_saved_query_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        saved_query = ET.SubElement(user_profile, "saved-query")
        key = ET.SubElement(saved_query, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_user_profile_saved_query_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        user_profile = ET.SubElement(data_stores, "user-profile")
        username_key = ET.SubElement(user_profile, "username")
        username_key.text = kwargs.pop('username')
        saved_query = ET.SubElement(user_profile, "saved-query")
        key_key = ET.SubElement(saved_query, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(saved_query, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_data_store_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        data_store = ET.SubElement(data_stores, "data-store")
        key = ET.SubElement(data_store, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_data_store_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        data_store = ET.SubElement(data_stores, "data-store")
        key_key = ET.SubElement(data_store, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(data_store, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_saved_query_key(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        saved_query = ET.SubElement(data_stores, "saved-query")
        key = ET.SubElement(saved_query, "key")
        key.text = kwargs.pop('key')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        
    def webui_data_stores_saved_query_value(self, **kwargs):
        """Auto Generated Code
        """
        config = ET.Element("config")
        webui = ET.SubElement(config, "webui", xmlns="http://tail-f.com/ns/webui")
        data_stores = ET.SubElement(webui, "data-stores")
        saved_query = ET.SubElement(data_stores, "saved-query")
        key_key = ET.SubElement(saved_query, "key")
        key_key.text = kwargs.pop('key')
        value = ET.SubElement(saved_query, "value")
        value.text = kwargs.pop('value')

        callback = kwargs.pop('callback', self._callback)
        return callback(config)
        