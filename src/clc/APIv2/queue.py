"""
Queue related functions.  

These queue related functions generally align one-for-one with published API calls categorized in the queue category

API v2 - https://t3n.zendesk.com/forums/21772620-Queue

Requests object variables:

	requests.requests
	requests.error_requests
	requests.success_requests


"""

# TODO - Do something with timing info from Request and Requests?

import re
import time
import clc


class Queue(object):
	pass



class Requests(object):

	def __init__(self,requests_lst,alias=None):
		"""Create Requests object.

		Treats one or more requests as an atomic unit.
		e.g. if performing a simulated group operation then succeed
		or fail as a group

		"""

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		self.requests = []
		self.error_requests = []
		self.success_requests = []

		# Some requests_lst responses look different than others depending on the call (Create snapshot vs. delete snapshot)
		# Add min-wrapper onto those missing it
		if requests_lst is None:  raise(Exception("Unexpected requests response"))
		elif 'isQueued' in requests_lst:  requests_lst = [requests_lst]
		elif 'href' in requests_lst: requests_lst = [{'isQueued': True, 'links': [requests_lst]}]

		for r in requests_lst:

			if 'server' in r and len(r['server'])<6:  
				# Hopefully this captures only new server builds, TODO find a better way to ID these
				for link in r['links']:
					if re.search("/v2/servers/",link['href']):
						context_key = "newserver"
						context_val = link['href']
						break
			elif 'server' in r:  
				context_key = "server"
				context_val = r['server']
			else:  
				context_key = "Unknown"
				context_val = "Unknown"

			if r['isQueued']:  
				self.requests.append(Request([obj['id'] for obj in r['links'] if obj['rel']=='status'][0],
				                             alias=self.alias,request_obj={'context_key': context_key, 'context_val': context_val}))
			else:
				# If we're dealing with a list of responses and we have an error with one I'm not sure how
				# folks would expect this to behave.  If server is already in desired state thus the request
				# fails that shouldn't be an exception.  If we're running against n tasks and just one has an
				# issue we need a reasonable way to report on the error but also follow the remaining tasks.
				#
				# For no-op failures we just won't create an object and our queue wait time will be faster.
				# For actual failures we'll wait until all tasks have reached a conclusion then .....
				if r['errorMessage'] == "The server already in desired state.":  pass
				elif r['errorMessage'] == "The operation cannot be queued because the server cannot be found or it is not in a valid state.":
					raise(Exception("do we pass on this or take action? %s" % r['errorMessage']))
				else:
					# TODO - need to ID other reasons for not queuing and known reasons don't raise out of the
					#        entire process
					raise(clc.CLCException("%s '%s' not added to queue: %s" % (context_key,context_val,r['errorMessage'])))


	def __add__(self,obj):
		if type(obj) is int:  return(self)	# we get this with a sum() call - ignore the first argument
		if self.alias != obj.alias:  raise(ArithmeticError("Cannot add Requests operating on different aliases"))

		new_obj = Requests([],alias=self.alias)
		new_obj.requests = obj.requests+self.requests
		new_obj.success_requests = obj.success_requests+self.success_requests
		new_obj.error_requests = obj.error_requests+self.error_requests

		return(new_obj)


	def __radd__(self,obj):  return(self.__add__(obj))


	def WaitUntilComplete(self,poll_freq=2):
		"""Poll until all request objects have completed.

		If status is 'notStarted' or 'executing' continue polling.
		If status is 'succeeded' then success
		Else log as error

		poll_freq option is in seconds

		Returns an Int the number of unsuccessful requests.  This behavior is subject to change.

		>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').PowerOn().WaitUntilComplete()
		0

		"""

		while len(self.requests):
			cur_requests = []
			for request in self.requests:
				status = request.Status()
				if status in ('notStarted','executing','resumed'):  cur_requests.append(request)
				elif status == 'succeeded':  self.success_requests.append(request)
				elif status in ("failed", "unknown"): self.error_requests.append(request)

			self.requests = cur_requests
			time.sleep(poll_freq)	# alternately - sleep for the delta between start time and 2s

		# Is this the best approach?  Non-zero indicates some error.  Exception seems the wrong approach for
		# a partial failure
		return(len(self.error_requests))



class Request(object):

	def __init__(self,id,alias=None,request_obj=None):
		"""Create Request object.

		https://t3n.zendesk.com/entries/43699144-Get-Status

		"""

		self.id = id

		self.time_created = time.time()
		self.time_executed = None
		self.time_completed = None

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if request_obj:  self.data = request_obj
		else:  self.data = {'context_key': None, 'context_val': None}
		self.data = dict({'status': None}.items() + self.data.items())


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Status(self,cached=False):
		if not cached or not self.data['status']:  
			try:
				self.data['status'] = clc.v2.API.Call('GET','operations/%s/status/%s' % (self.alias,self.id),{})['status']
			except clc.APIFailedResponse as e:
				if e.response_status_code == 500:  pass
				else:  raise(e)
		return(self.data['status'])
		

	def WaitUntilComplete(self,poll_freq=2):
		"""Poll until status is completed.

		If status is 'notStarted' or 'executing' continue polling.
		If status is 'succeeded' return
		Else raise exception

		poll_freq option is in seconds

		"""
		while not self.time_completed:
			status = self.Status()
			if status == 'executing':
				if not self.time_executed:  self.time_executed = time.time()
			elif status == 'succeeded': 
				self.time_completed = time.time()
			elif status in ("failed", "resumed" or "unknown"): 
				# TODO - need to ID best reaction for resumed status (e.g. manual intervention)
				self.time_completed = time.time()
				raise(clc.CLCException("%s %s execution %s" % (self.context_key,self.context_val,status)))

			time.sleep(poll_freq)


	def Server(self):
		"""Return server associated with this request.

		>>> d = clc.v2.Datacenter()
		>>> q = clc.v2.Server.Create(name="api2",cpu=1,memory=1,group_id=d.Groups().Get("Default Group").id,template=d.Templates().Search("centos-6-64")[0].id,network_id=d.Networks().networks[0].id,ttl=4000)
		>>> q.WaitUntilComplete()
		0
		>>> q.success_requests[0].Server()
		<clc.APIv2.server.Server object at 0x1095a8390>
		>>> print _
		VA1BTDIAPI214
		
		"""
		if self.context_key == 'newserver':
			server_id = clc.v2.API.Call('GET', self.context_val)['id']
			return(clc.v2.Server(id=server_id,alias=self.alias))
		elif self.context_key == 'server':  
			return(clc.v2.Server(id=self.context_val,alias=self.alias))
		else:  raise(clc.CLCException("%s object not server" % self.context_key))


	def __str__(self):
		return(self.id)

