#!/usr/bin/env python

"""
Detect if the running config has changed. If so, send an email including
the router hostname and timestamp of the change.
"""

from pynet_dev import devices, get_host_details
from snmp_helper import snmp_get_oid_v3
import pprint
            

routers_l = get_host_details(devices, model='881', snmp_port=8061)
pprint.pprint(routers_l)




    



"""
def get_host_details(devices, **kvargs):
    
    Params:
        devices : dict : device details
        kvargs : keyword arguements : any number of host matching parameters
    Return:
        List of dict entries matching given match params
    

    if not len(kvargs):
        return
    
    else:
        pprint.pprint(kvargs)
        results = []
        for key, value in devices.items():
            for val_key, val_val in value.items():
                for arg_key, arg_val in kvargs.items():
                    if arg_key in value:
                        if arg_key == val_key and arg_val == val_val:
                            results.append({key : value})
        return results
"""