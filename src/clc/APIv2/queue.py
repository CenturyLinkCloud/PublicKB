"""
Queue related functions.  

These queue related functions generally align one-for-one with published API calls categorized in the queue category

API v2 - https://t3n.zendesk.com/forums/21772620-Queue

Server object variables:


"""


import time
import sys
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
		exception_lst = []
		for r in requests_lst:
			if 'server' in r:  
				context_key = "server"
				context_val = r['server']
			else:  raise(Exception("Unknown context"))

			if not r['isQueued']:  
				# If we're dealing with a list of responses and we have an error with one I'm not sure how
				# folks would expect this to behave.  If server is already in desired state thus the request
				# fails that shouldn't be an exception.  If we're running against n tasks and just one has an
				# issue we need a reasonable way to report on the error but also follow the remaining tasks.
				#
				# For no-op failures we just won't create an object and our queue wait time will be faster.
				# For actual failures we'll wait until all tasks have reached a conclusion then .....
				if r['errorMessage'] == "The server already in desired state.":  pass
				else:
					raise(clc.CLCException("%s '%s' not added to queue: %s" % (context_key,context_val,r['errorMessage'])))

			self.requests.append(Request(r['id'],alias=self.alias,request_obj={'context_key': context_key, 'context_val': context_val}))



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
			self.data['status'] = clc.v2.API.Call('GET','operations/%s/status/%s' % (self.alias,self.id),{},debug=True)
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
			print status
			if status == 'executing':
				if not self.time_executed:  self.time_executed = time.time()
			elif status == 'succeeded': 
				self.time_completed = time.time()
			elif status in ("failed", "resumed" or "unknown"): 
				# TODO - need to ID best reaction for resumed status (e.g. manual intervention)
				self.time_completed = time.time()
				raise(clc.CLCException("%s %s execution %s" % (self.context_key,self.context_val,status)))

			sys.sleep(poll_freq)


	def Server(self):
		"""Return server associated with this request."""
		if self.context_key == 'server':  return(clc.v2.Server(id=self.context_val,alias=self.alias))
		else:  raise(clc.CLCException("%s object not server" % self.context_key))


	def __str__(self):
		return(self.id)

