#!/usr/bin/env python

import pygal

## for key, value in data.items():
## 	print key, value
## 	for i, v in enumerate(value):
## #		print i, v
## 		value[i] = int(v)


def line(data):

	#data = {'in_octets': [152271406, 152275270, 152279297, 152283161, 152287025, 152291052, 152294916, 152298780, 152302807, 152306671], 'in_ucast_pkts': [832266, 832278, 832302, 832326, 832350, 832374, 832398, 832422, 832459, 832470], 'out_octets': [345346343, 345350307, 345354614, 345358958, 345362922, 345367229, 345371193, 345375157, 345379844, 345383808], 'out_ucast_pkts': [856136, 856148, 856172, 856196, 856220, 856244, 856268, 856292, 856329, 856340]}


	# Make a list of the data keys
	keys = [y for y in data.keys()]

	max_count = 0

	# Determine the largest data set
	for key in keys:
		count = len(data[key])
		if count > max_count:
			max_count = count

	x_labels = [str(x) for x in range(5, ((max_count + 1) * 5), 5)]

	line_chart = pygal.Line(include_x_axis=True)
	line_chart.title = 'Test'
	line_chart.x_labels = x_labels
	#line_chart.y_labels = y_labels

	for key, value in data.items():
		print str(key), value
		line_chart.add(key, value)

	#line_chart.add('in_octets', [152271406, 152275270, 152279297, 152283161, 152287025, 152291052, 152294916, 152298780, 152302807, 152306671])

	line_chart.render_to_file('./test.svg')



if __name__ == '__main__':
	line()