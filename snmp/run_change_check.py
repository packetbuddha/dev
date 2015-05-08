#!/usr/bin/env python

"""
Detect if the running config has changed. If so, send an email including
the router hostname and timestamp of the change.
"""

from pynet_dev import devices, get_host_details
from snmp_helper import snmp_get_oid_v3, snmp_extract
import pprint


routers_l = get_host_details(devices, model='881', snmp_port=8061)
#pprint.pprint(routers_l)

oid_run_last_change = '1.3.6.1.4.1.9.9.43.1.1.1.0'
oid_run_last_save = '1.3.6.1.4.1.9.9.43.1.1.2.0'
oid_start_last_save = '1.3.6.1.4.1.9.9.43.1.1.3.0'

for router in routers_l:
	print router.keys()
	print router.values()['ip_address']

#	host = router['pynet-rtr1']['ip_address']
#	snmp_port = devices['pynet-rtr1']['snmp_port']
#	snmp_comm = devices['pynet-rtr1']['snmp_community']






