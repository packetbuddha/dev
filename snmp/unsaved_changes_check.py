#!/usr/bin/env python

# import std lib
import pprint

# import local
from pynet_dev import devices
from snmp_helper import snmp_get_oid, snmp_extract


oid_run_last_change = '1.3.6.1.4.1.9.9.43.1.1.1.0'
oid_run_last_save = '1.3.6.1.4.1.9.9.43.1.1.2.0'
oid_start_last_save = '1.3.6.1.4.1.9.9.43.1.1.3.0'

host = devices['pynet-rtr1']['ip_address']
snmp_port = devices['pynet-rtr1']['snmp_port']
snmp_comm = devices['pynet-rtr1']['snmp_community']

run_last_change = snmp_get_oid((host, snmp_comm, snmp_port),
    oid_run_last_change) 
start_last_save = snmp_get_oid((host, snmp_comm, snmp_port),
    oid_start_last_save) 

current_run_last_change = snmp_extract(run_last_change)
current_start_last_save = snmp_extract(start_last_save)

# uncomment to simulate router reboot
#current_start_last_save = 0
 
print '...the running config was last changed {} minutes ago.'.format(
    int(current_run_last_change)/6000)
print '...the startup config was last saved {} minutes ago.'.format(
    int(current_start_last_save)/6000)

if current_start_last_save == 0:
    print 'The startup config has not been saved since the last reboot.' \
        'The running config may contain unsaved changes.' 
elif current_run_last_change > current_start_last_save:
    print 'The running config contains unsaved changes.'
else:
    print 'The starup config is current.'


