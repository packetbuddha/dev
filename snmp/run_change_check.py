#!/usr/bin/env python

"""
Detect if the running config has changed. If so, send an email including
the router hostname and timestamp of the change.
"""

from pynet_dev import devices, get_host_details
from snmp_helper import snmp_get_oid_v3, snmp_extract
import pprint
import os.path
import pickle


# Get a list of the devices we want to query
routers_l = get_host_details(devices, model='881')

oid_run_last_change = '1.3.6.1.4.1.9.9.43.1.1.1.0'
oid_run_last_save = '1.3.6.1.4.1.9.9.43.1.1.2.0'
oid_start_last_save = '1.3.6.1.4.1.9.9.43.1.1.3.0'

def snmp_get_v3(device, oid):
	"""
	Params:
		device : dict : a device entry
	Returns:
		A tuple containing the hostname and the snmp value
	"""

	snmp_result = snmp_get_oid_v3((device['ip_address'], device['snmp_port']),(device['snmp_username'],
		device['snmp_auth_key'], device['snmp_encrypt_key']), oid)

	snmp_value = snmp_extract(snmp_result)

	return (device['hostname'], snmp_value)


def read_run_change(device, file):
	"""
	Param:
		device : dict : a device entry
		file : str : file path

	Returns:
		A tuple containing the hostname and the last written value
	"""

	with open(file, 'rwb+') as f:
		line = pickle.load(f)
		if line:
			if line[0] == device['hostname']:
				return line
		else:
			return

def write_run_change(device, file, value):
	"""
	Param:
		hostname : str : device hostname
		value : int : value
		file : str : file path

	Returns:
		A tuple containing the hostname and the last written value
	"""

	with open(file, 'rwb+') as f:
		pickle.dump((device['hostname'], value), f)






results_current = {}
file = '/var/tmp/run_change_data.pkl'

for device in routers_l:

	# Grab current SNMP value
	current_run_last_change = snmp_get_v3(device, oid_run_last_change)

	if results_current:
		print 'current value:', results_current
	else:
		print 'No SNMP value available for', device['hostname']

	# Grab last recorded value
	results_last = read_run_change(device, file)

	if results_last:
		print 'recorded value:', results_last
	else:
		print 'No recorded value available for', device['hostname']
		write_run_change(device, file, results_current)












"""
- check file if we have a recorded run_last_change value
- if not, create an entry using the latest timestamp
- if one exists, compare with current timestamp
- if the current one is larger (later), we return True
- if the current one is smaller (earlier), we return False
	Param:
		run_last_change : int : timestamp of running config change

	Returns:
		BOOL depending on if the current change is later than the last recorded change

"""