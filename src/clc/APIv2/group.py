"""
Group related functions.  

These group related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21013480-Groups
"""

# TODO - Get Group Billing Details
# TODO - Get Group Monitoring Statistics
# TODO - find group - recursively search to find and return specific group


import json
import clc

class Group(object):
"""Group object.

Class variables:

	group.id
	group.name
	group.description
	group.type
	group.status
	group.serverCount

"""

	@staticmethod
	def GetAll(root_group_id,alias=None):  
		"""Gets a list of groups within a given account.


		"""

		if not alias:  alias = clc.v2.Account.GetAlias()

		groups = []
		for r in clc.v2.API.Call('GET','groups/%s/%s' % (alias,root_group_id),{})['groups']:
			groups.append(Group(id=r['id'],alias=alias,group_obj=r))
		
		return(groups)


	@staticmethod
	def Create(name,alias=None,location=None):  
		"""Creates a new group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def __init__(self,id,alias=None,group_obj=None):
		"""Create Group object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call


		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if group_obj:  self.data = group_obj
		else:  self.data = json.loads(clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id),{}))


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Update(self):
		"""Update group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def Delete(self):
		"""Delete group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def __str__(self):
		return(self.data['name'])

