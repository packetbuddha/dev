#!/usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import cmdgen

host= '50.242.94.227'
snmp_comm = 'galileo'
rtr1_snmp = '7961' 
rtr1_snmp = '8061' 

oids = {
    'mib2_desc' : '1.3.6.1.2.1.1.1.0',
    'mib2_name' : '1.3.6.1.2.1.1.5.0'
    }

snmp_port = [rtr1_snmp, rtr1_snmp]


cmdGen = cmdgen.CommandGenerator()

def get_oid(host, port, snmp_comm, oid):
    (errorIndication, errorStatus, errorIndex, snmp_data) = cmdGen.getCmd(
        cmdgen.CommunityData(snmp_comm),        
        cmdgen.UdpTransportTarget((host, port)),
        oid,
        lookupNames=True, lookupValues=True
    )

    if errorIndication:
        print(errIndication)
    else:
        if errorStatus:
            print(errorStatus, errorIndex)

        else:
            return snmp_data 

for port in snmp_port:
    for name, oid in oids.items():
        result = get_oid(host, port, snmp_comm, oid)
        
        print 'Host:', host, 'Port:', port, name + ':', result[0][1].prettyPrint()

