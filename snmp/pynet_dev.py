#!/usr/bin/env python

import pprint
from snmp_helper import snmp_get_oid_v3, snmp_extract

devices = {
    'pynet-rtr1' : {'hostname' : 'pynet-rtr1', 'vendor' : 'cisco', 'model' : '881', 'snmp_port' : 7961,
        'ssh_port' : 22, 'api_port' : 15002, 'ip_address' : '50.242.94.227',
        'snmp_community' : 'galileo', 'snmp_username' : 'pysnmp',
        'snmp_auth_key' : 'galileo1', 'snmp_encrypt_key' : 'galileo1'},
    'pynet-rtr2' : {'hostname' : 'pynet-rtr2', 'vendor' : 'cisco', 'model' : '881', 'snmp_port' : 8061,
        'ssh_port' : 8022, 'api_port' : 8002, 'ip_address' : '50.242.94.227',
        'snmp_community' : 'galileo', 'snmp_username' : 'pysnmp',
        'snmp_auth_key' : 'galileo1', 'snmp_encrypt_key' : 'galileo1'},
    'pynet-sw1' : {'hostname' : 'pynet-sw1', 'vendor' : 'Arista', 'model' : 'vEOS switch',
        'snmp_port' : None, 'ssh_port' : 8222, 'api_port' : 8243,
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo',
        'snmp_username' : 'pysnmp', 'snmp_auth_key' : 'galileo1',
        'snmp_encrypt_key' : 'galileo1'},
    'pynet-sw2' : {'hostname' : 'pynet-sw2', 'vendor' : 'Arista', 'model' : 'vEOS switch',
        'snmp_port' : None, 'ssh_port' : 8322, 'api_port' : 8343,
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo',
        'snmp_username' : 'pysnmp', 'snmp_auth_key' : 'galileo1',
        'snmp_encrypt_key' : 'galileo1'},
    'pynet-sw3' : {'hostname' : 'pynet-sw3', 'vendor' : 'Arista', 'model' : 'vEOS switch',
        'snmp_port' : None, 'ssh_port' : 8422, 'api_port' : 8443,
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo',
        'snmp_username' : 'pysnmp', 'snmp_auth_key' : 'galileo1',
        'snmp_encrypt_key' : 'galileo1'},
    'pynet-sw4' : {'hostname' : 'pynet-sw4', 'vendor' : 'Arista', 'model' : 'vEOS switch',
        'snmp_port' : None, 'ssh_port' : 8522, 'api_port' : 8543,
        'ip_address' : '50.242.94.227', 'snmp_community' : 'galileo',
        'snmp_username' : 'pysnmp', 'snmp_auth_key' : 'galileo1',
        'snmp_encrypt_key' : 'galileo1'}
}

def snmp_get_v3(device, oid, valueonly=False):
	"""
	Params:
		device : dict : a device entry
	Returns:
		A tuple containing the hostname and the snmp value
	"""

	print device

	snmp_result = snmp_get_oid_v3((device['ip_address'], device['snmp_port']),(device['snmp_username'],
		device['snmp_auth_key'], device['snmp_encrypt_key']), oid)

	snmp_value = snmp_extract(snmp_result)

	if valueonly:
		return(snmp_value)
	else:
		return (device['hostname'], snmp_value)


def get_host_details(devices, debug=False, **kvargs):
	"""
	Params:
		devices : dict : device details
		kvargs : keyword arguments : any number of key, values for matching.
			A successful match includes all given key, values.
	Return:
		List of dict entries matching given match params
	"""

	if not len(kvargs):
		return

	else:
		if debug and kvargs: pprint.pprint(kvargs)

		results = []
		for key, value in devices.items():
			match = []
			for arg_key, arg_value in kvargs.items():
				if debug: print 'searching for', arg_key, arg_value
				if arg_key in value:
					if debug: print 'comparing', value[arg_key], 'with', arg_value
					if value[arg_key] == arg_value:
						match.append(True)
					else:
						match.append(False)
					if debug: print 'match', match
				else:
					print 'arg_key not in this device'
					continue

			if debug: print 'Done comparing args'

			if False in match:
				continue
			else:
				value.update({'hostname' : key})
				results.append(value)

		return results


