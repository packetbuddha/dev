#!/usr/bin/env python

devices = { 
    'pynet-rtr1' : { 'vendor' : 'cisco', 'model' : '881', 'snmp_port' : 7961, 
        'ssh_port' : 22, 'api_port' : 15002, 'ip_address' : '50.242.94.227',
        'snmp_community' : 'galileo'},
    'pynet-rtr2' : { 'vendor' : 'cisco', 'model' : '881',
        'snmp_port' : 8061, 
        'ssh_port' : 8022, 'api_port' : 8002, 'ip_address' : '50.242.94.227',
        'snmp_community' : 'galileo'},
    'pynet-sw1' : { 'vendor' : 'Arista', 'model' : 'vEOS switch', 
        'snmp_port' : None, 'ssh_port' : 8222, 'api_port' : 8243, 
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo'},
    'pynet-sw2' : { 'vendor' : 'Arista', 'model' : 'vEOS switch', 
        'snmp_port' : None, 'ssh_port' : 8322, 'api_port' : 8343, 
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo'},
    'pynet-sw3' : { 'vendor' : 'Arista', 'model' : 'vEOS switch', 
        'snmp_port' : None, 'ssh_port' : 8422, 'api_port' : 8443, 
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo'},
    'pynet-sw4' : { 'vendor' : 'Arista', 'model' : 'vEOS switch',
        'snmp_port' : None, 'ssh_port' : 8522, 'api_port' : 8543, 
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo'}
}

