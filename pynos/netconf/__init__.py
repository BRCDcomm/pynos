#!/usr/bin/env python
'''
Object containing all rendering of actions to NetCONF.
'''
import xml.etree.ElementTree as ET
from ncclient import manager
from ncclient import xml_
from pynos.netconf import interface
from pynos.netconf import bgp
from pynos.netconf import system

class Device(object):
    '''
    Main NetCONF class.
    '''
    def __init__(self, conn, auth):
        self._conn = conn
        self._auth = auth
        self._mgr = None

        self.interface = interface.Interface(self._callback)
        self.bgp = bgp.BGP(self._callback)
        self.system = system.System(self._callback)

        self._connect()

    def _connect(self):
        '''
        Connect to device via netconf.
        '''
        self._mgr = manager.connect(host=self._conn[0],
                                    port=self._conn[1],
                                    username=self._auth[0],
                                    password=self._auth[1])
        self._mgr.timeout = 600

    def _callback(self, call, handler='edit_config', target='running',
                  source='startup'):
        '''
        Callback for interactive calls
        '''
        try:
            call = ET.tostring(call)
            if handler == 'get':
                call_element = xml_.to_ele(call)
                return ET.fromstring(str(self._mgr.dispatch(call_element)))
            if handler == 'edit_config':
                self._mgr.edit_config(target=target, config=call)
            if handler == 'delete_config':
                self._mgr.delete_config(target=target)
            if handler == 'copy_config':
                self._mgr.copy_config(target=target, source=source)
        #TODO: Figure out how this can fail and narrow exception window.
        except Exception, error:
            print error

    @property
    def lldp_neighbors(self):
        '''
        Returns LLDP Neighbors
        '''
        urn = "{urn:brocade.com:mgmt:brocade-lldp-ext}"

        result = []

        request_lldp = ET.Element('get-lldp-neighbor-detail',
                                  xmlns="urn:brocade.com:mgmt:brocade-lldp-ext")

        lldp_result = self._callback(request_lldp, 'get')

        for item in lldp_result.findall('%slldp-neighbor-detail' %urn):
            local_int_name = item.find('%slocal-interface-name' %urn).text
            local_int_mac = item.find('%slocal-interface-mac' %urn).text
            remote_int_name = item.find('%sremote-interface-name' %urn).text
            remote_int_mac = item.find('%sremote-interface-mac' %urn).text
            remote_chas_id = item.find('%sremote-chassis-id' %urn).text
            remote_sys_name = item.find('%sremote-system-name' %urn).text

            if 'Fo ' in local_int_name:
                local_int_name = local_int_name.replace('Fo ',
                                                        'FortyGigabitEthernet ')

            item_results = {'local-int-name' : local_int_name,
                            'local-int-mac' : local_int_mac,
                            'remote-int-name' : remote_int_name,
                            'remote-int-mac' : remote_int_mac,
                            'remote-chassis-id' : remote_chas_id,
                            'remote-system-name' : remote_sys_name,}
            result.append(item_results)

        return result

    @property
    def routing_table(self):
        '''
        Returns current routing table
        '''
        pass
