"""
Queue related functions.  

These queue related functions generally align one-for-one with published API calls categorized in the queue category

API v2 - https://t3n.zendesk.com/forums/21772620-Queue

Server object variables:


"""

# TODO - implement wait until

import json
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
		for r in requests_lst:
			if 'server' in r:  
				context_key = "server"
				context_val = r['server']
			else:  raise(Exception("Unknown context"))

			if not r['isQueued']:  raise(clc.CLCException("%s '%s' not added to queue: %s" % (context_val,context_key,r['errorMessage'])))

			self.requests.append(Request(id,alias=self.alias,request_obj={'context_key': context_key, 'context_val': context_val}))



class Request(object):

	def __init__(self,id,alias=None,request_obj=None):
		"""Create Request object.

		https://t3n.zendesk.com/entries/43699144-Get-Status

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if server_obj:  self.data = server_obj
		else:  self.data = {'context_key': None, 'context_val': None}
		self.data = dict({'status': None}.items() + self.data.items())


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		elif var in self.data['details']:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Status(self,cached=False):
		if not cached or not self.data['status']:  
			self.data['status'] = clc.v2.API.Call('GET','/operations/%s/status/%s' % (self.alias,self.id),{},debug=True)
		return(self.data['status'])
		

	def WaitUntilComplete(self,poll_freq=2):
		"""Poll until status is completed.

		If status is 'notStarted' or 'executing' continue polling.
		If status is 'succeeded' return
		Else raise exception

		"""


	def Server(self):
		"""Return server associated with this request."""
		if self.context_key == 'server':  return(clc.v2.Server(id=self.context_val,alias=self.alias))
		else:  raise(clc.CLCException("%s object not server" % self.context_key))


	def __str__(self):
		return(self.id)

