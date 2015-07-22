#!/usr/bin/env python

"""
Poll interface in/out octets for every 5 mintutes for 60 minutes. Produce
an SVG graph from the data.
"""

from pynet_dev import devices, get_host_details, snmp_get_v3
import line_chart
import time



def get_int_stats(router, stat, int_index):

	int_oids_d = {
		'in_octets' : '1.3.6.1.2.1.2.2.1.10',
		'out_octets' : '1.3.6.1.2.1.2.2.1.16',
		'in_ucast_pkts' : '1.3.6.1.2.1.2.2.1.11',
		'out_ucast_pkts' : '1.3.6.1.2.1.2.2.1.17'
	}

	if stat not in int_oids_d:
		print 'Invalid stat'
		return

	int_index = int(int_index)

	# Update stat dic with int_index
	oid = int_oids_d[stat]
	oid = '{}.{}'.format(oid, str(int_index))

	print oid
	value = snmp_get_v3(router, oid, valueonly=True)
	return int(value)


def main():

	# Get device details
	router = (get_host_details(devices, hostname='pynet-rtr1'))[0]

	# Fa4
	int_index = 5

	graph_stats = {
		'in_octets' : [],
		'out_octets': [],
		'in_ucast_pkts': [],
		'out_ucast_pkts': []
	}

	base_values_d = {}

	# Run every 5 minutes for 1 hour
	for counter in range(0, 29):
		print 'time:', counter

		# Grab SNMP data for each stat
		for stat in ("in_octets", "out_octets", "in_ucast_pkts", "out_ucast_pkts"):

			print get_int_stats(router, stat, int_index)
			# SNMP Get
			snmp_value = get_int_stats(router, stat, int_index)

			base_value = base_values_d.get(stat)
			if base_value:
				# Calculate and store delta from base value to new value
				graph_stats[stat].append(int(snmp_value) - base_value)
				print 'delta:', graph_stats[stat][-1]


			graph_stats[stat].append(snmp_value)

		time.sleep(300)

	print graph_stats
	line_chart.line(graph_stats)





if __name__ == '__main__':
	main()