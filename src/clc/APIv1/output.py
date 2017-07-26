# -*- coding: utf-8 -*-
"""Output formatting helper functions.  Used in conjunction with CLI."""

import os
import sys
import shutil
import time
import terminal_size
import prettytable
from clint.textui import colored, puts, indent, progress
import clc


def sec_to_time(secs):
    hrs = secs / 3600
    secs -= 3600*hrs
    mins = secs / 60
    secs -= 60*mins

    return("%d:%02d:%02d" % (hrs,mins,secs))


def Table(data_arr,keys,opts={}):
	if type(data_arr) != list:  data_arr = [data_arr]

	# TODO - doesn't take into account row data that is too long.  
	#        need to back out of verticle or build data in list
	#        then determine format
	max_width = len("   ".join(keys))
	console_width = terminal_size.get_terminal_size()[0]

	if max_width<console_width:
		return(Cols(data_arr,keys,opts))
	else:
		return(Rows(data_arr,keys,opts))


# TODO add sorting
def Rows(data_arr,keys,opts={}):
	max_key_len = 0
	for key in keys: 
		if len(key)>max_key_len:  max_key_len = len(key)

	table = ''
	i = 0
	for line in data_arr:
		i += 1
		table += "\n  ******************* %s. ********************\n" % (i)
		for key in keys: table += "%s:  %s\n" % (key.rjust(max_key_len+2),line[key])

	return(table)


# TODO - optional sorting, filtering, format type
def Cols(data_arr,keys,opts={}):
	table = prettytable.PrettyTable(keys)

	for line in data_arr:
		row = []
		for key in keys: row.append(line[key])
		table.add_row(row)

	table.align = 'l'
	table.sortby = keys[0]
	return(table)


# TSV w/o headers
def Text(data_arr,keys,opts={}):
	rows = []

	for line in data_arr:
		row = []
		for key in keys: 
			if isinstance(line[key], (basestring, int, long, float)):  row.append(str(line[key]).replace("	"," "))
			else:  
				str_line = []
				for a in line[key]:  str_line.append(str(a))
				row.append(", ".join(str_line).replace(",",""))
		rows.append("	".join(row))

	return("\n".join(rows))


# TODO - Use CSV module?
def Csv(data_arr,keys,opts={'no_header': False}):
	csv = []
	if not opts['no_header']:  csv.append(",".join(keys))

	for line in data_arr:
		row = []
		for key in keys: 
			if isinstance(line[key], (basestring, int, long, float)):  row.append(str(line[key]).replace(","," "))
			else:  
				str_line = []
				for a in line[key]:  str_line.append(str(a))
				row.append(" ".join(str_line).replace(",",""))
		csv.append(",".join(row))

	return("\n".join(csv))


def Json(data_arr,keys,opts={}):
	print keys
	new_data_arr = []
	for data_dict in data_arr:
		for key in data_dict.keys():
			if key not in keys:  data_dict.pop(key,None)
		new_data_arr.append(data_dict)

	return(new_data_arr)


def Status(status,level,message):
	if clc.args.GetArgs().quiet<level:
		if os.name=='posix':
			success_mark = '✔ '
			error_mark = '✖  '
		else:
			success_mark = '/'
			error_mark = 'x '

		if status == 'SUCCESS':  puts("%s %s" % (colored.green(success_mark),message.encode('utf-8')))
		elif status == 'ERROR' and level<3:  puts("%s%s" % (colored.red(error_mark),message.encode('utf-8')))
		elif status == 'ERROR':  puts("%s" % (colored.red(error_mark+message.encode('utf-8'))))


def RequestQueueProgress(request_id):
	request_details = clc.Queue.GetStatus(request_id,silent=True)
	p = progress.Bar(label="%s  " % (request_details['RequestTitle']), expected_size=100)
	while True:
		p.show(request_details['PercentComplete'])
		if request_details['CurrentStatus'] in ('Succeeded','Failed'): break
		time.sleep(2)
		request_details = clc.v1.Queue.GetStatus(request_id,silent=True)
	p.done()
	if request_details['CurrentStatus'] == 'Succeeded':  Status('SUCCESS',1,"%s - %s" % (request_details['RequestTitle'],request_details['ProgressDesc']))
	elif request_details['CurrentStatus'] == 'Failed':  Status('ERROR',3,"%s - %s" % (request_details['RequestTitle'],request_details['ProgressDesc']))


def RequestBlueprintProgress(request_id,location,alias,quiet=False):
	time_start = time.time()
	time_task_start = time_start
	request_details = clc.v1.Blueprint.GetStatus(request_id,location,alias,silent=True)
	description = request_details['Description']
	Status('SUCCESS',1,request_details['Description'])
	if not quiet:  p = progress.Bar(expected_size=100)
	while True:
		if description != request_details['Description']:
			description = request_details['Description']
			if not quiet:  sys.stdout.write("\033[K")	# clear line
			Status('SUCCESS',1,"%s - %s" % (request_details['Description'],sec_to_time(int(time.time()-time_task_start))))
			time_task_start = time.time()
		if not quiet:  p.show(request_details['PercentComplete'])
		if request_details['CurrentStatus'] in ('Succeeded','Failed'): break
		time.sleep(2)
		request_details = clc.v1.Blueprint.GetStatus(request_id,location,alias,silent=True)
	#p.done()
	if not quiet:  sys.stdout.write("\033[K")	# clear line
	duration_secs = int(time.time()-time_start)
	if request_details['CurrentStatus'] == 'Succeeded':  Status('SUCCESS',1,"%s - %s" % (request_details['Description'],sec_to_time(duration_secs)))
	elif request_details['CurrentStatus'] == 'Failed':  Status('ERROR',3,"%s - %s" % (request_details['Description'],sec_to_time(duration_secs)))

	servers = []
	for server in request_details['Servers']:  servers.append({'Server': server})
	return(servers)

