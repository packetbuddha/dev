#!/usr/bin/env python

"""
Detect if the running config has changed. If so, send an email including
the router hostname and timestamp of the change.
"""

from pynet_dev import devices, get_host_details, snmp_get_v3
import pprint
import os.path
import pickle
import sys


# Get a list of the devices we want to query
routers_l = get_host_details(devices, model='881')

oid_run_change = '1.3.6.1.4.1.9.9.43.1.1.1.0'
oid_run_last_save = '1.3.6.1.4.1.9.9.43.1.1.2.0'
oid_start_last_save = '1.3.6.1.4.1.9.9.43.1.1.3.0'


def read_run_change(file):
	"""
	Param:
		file : str : data file path

	Returns:
		A dictionary containing hostnames and value pairs
	"""

	with open(file, 'r') as f:
		try:
			data = pickle.load(f)

			print 'The file {} contains data.'.format(file)
			return data

		except EOFError:
			print 'The file {} does not contain data.'.format(file)
			return

def write_run_change(file, run_change_update):
	"""
	Param:
		run_change_update : dict : dictionary containing new dataset
		file : str : file path

	Returns:
		True if file write succeeds and False if it fails
	"""

	with open(file, 'w') as f:
		try:
			pickle.dump(run_change_update, f)
		except:
			return False

		return True



def check_run_change():
	run_change_current_d = {}
	run_change_update_d = {}


	file = '/var/tmp/run_change_data.pkl'

	# Grab current SNMP value from each device
	for device in routers_l:
		run_change_current = snmp_get_v3(device, oid_run_change)

		if run_change_current:
			# Update current dictionary with current data
			run_change_current_d[run_change_current[0]] = run_change_current[1]
			#print 'current value:', run_change_current_d
		else:
			print 'No SNMP value available for', device['hostname']


	# Grab all recorded data
	run_change_last_d = read_run_change(file)

	if not run_change_last_d: run_change_last_d = {}

	# Look at current values
	for key, value in run_change_current_d.items():
		print 'Working on {} : {}'.format(key, value)

		# if we have previously recorded values, compare with current
		# Check if our key is in the file results
		if key in run_change_last_d:
			print 'Comparing timestamps...current: {} vs last: {}'.format(value, run_change_last_d[key])
			if value > run_change_last_d[key]:
				print 'The running config has been changed since last check, updating...'
				run_change_update_d[key] = value
			else:
				print 'The running config has not changed since last check, nothing to do.'
				run_change_update_d[key] = run_change_last_d[key]

		# We don't have recorded data for this device; add it.
		else:
			print 'No record for that one, adding it.'
			run_change_update_d[key] = value

	if not run_change_update_d == run_change_last_d:
		if write_run_change(file, run_change_update_d):
			print 'File updated.'
		else:
			print 'Error updating file.'


if __name__ == "__main__":
	check_run_change()