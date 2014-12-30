"""
Group related functions.  

These group related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21013480-Groups
"""

# TODO - Get Group
# TODO - Get Group Billing Details
# TODO - Get Group Monitoring Statistics

# TODO - GetLocation ignoring: computelimits, networklimits, horizontalAutoscalePolicyMapping, scheduledActivities

import clc

class Group(object):

	@staticmethod
	def GetAll(root_group_id,alias=None):  
		"""Gets a list of groups within a given account.


		"""

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		groups = []
		for r in clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,root_group_id),{})['groups']:
			groups.append(Group(id=r['id'],alias=alias,json_defn=r))
		
		return(groups)


	@staticmethod
	def Create(name,alias=None,location=None):  
		"""Creates a new group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def __init__(self,id,alias=None,json_defn=None):
		"""Create Group object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call


		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if not json_defn:  json_defn = clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id),{})
		self.data = json.loads(json_defn)


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

