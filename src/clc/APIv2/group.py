"""
Group related functions.  

These group related functions generally align one-for-one with published API calls categorized in the group category

API v2 - https://t3n.zendesk.com/forums/21013480-Groups

Group object variables:

	group.id
	group.name
	group.description
	group.type
	group.status
	group.server_count

Group object variables available but access subject to change with future releases:

	group.custom_fields
	group.change_info

"""

# vCur:
# TODO - servers: {u'href': u'/v2/servers/btdi/wa1btdiubuntu02', u'id': u'WA1BTDIUBUNTU02', u'rel': u'server'}

# vNest:
# TODO - Update group
# TODO - Get Group Billing Details
# TODO - Statistics - Pending API spec error 500
# TODO - Links: scheduledActivities, upcomingScheduledActivities, horizontalAutoscalePolicyMapping, defaults
# TODO - find group - recursively search to find and return specific group
# TODO - async operations need to return a work queue class item for further followup
# TODO - use utility class to rewrite timestamps as unixtime
# TODO - server power actions - these take a list of server names which we know
# TODO - horizontalAutoscalePolicyMapping, scheduledActivities, upcomingScheduledActivities
# TODO - Implement Groups class as a collection of groups?
# TODO - archiveGroupAction


import re
import json
import clc

class Group(object):

	@staticmethod
	def GetAll(root_group_id,alias=None):  
		"""Gets a list of groups within a given account.

		"""

		if not alias:  alias = clc.v2.Account.GetAlias()

		groups = []
		for r in clc.v2.API.Call('GET','groups/%s/%s' % (alias,root_group_id),{})['groups']:
			groups.append(Group(id=r['id'],alias=alias,group_obj=r))
		
		return(groups)



	def __init__(self,id,alias=None,group_obj=None):
		"""Create Group object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call

		>>> clc.v2.Group(id="wa1-1798")
		<clc.APIv2.group.Group object at 0x109188b90>

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if group_obj:  self.data = group_obj
		else:  self.data = clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id),{})


	def __getattr__(self,var):
		key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


	def Create(self,name,description=None):  
		"""Creates a new group

		>>> clc.v2.Datacenter(location="WA1").RootGroup().Create("Test3","Description3")
		<clc.APIv2.group.Group object at 0x10cc76c90>
		>>> print _
		Test5

		"""

		if not description:  description = name

		r = clc.v2.API.Call('POST','groups/%s' % (self.alias),{'name': name, 'description': description, 'parentGroupId': self.id})
		return(Group(id=r['id'],alias=self.alias,group_obj=r))


	def Update(self):
		"""Update group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def Delete(self):
		"""Delete group.
		
		>>> clc.v2.Group("wa1-4416").Create(name="Test6")
		<clc.APIv2.group.Group object at 0x1041937d0>
		>>> clc.v2.Group(_.id).Delete().WaitUntilComplete()
		0

		"""

		return(clc.v2.Requests(clc.v2.API.Call('DELETE','groups/%s/%s' % (self.alias,self.id),{})))
	

	def Account(self):
		"""Return account object.

		>>> clc.v2.Group(alias="BTDI",id="wa1-837").Account()
		<clc.APIv2.account.Account instance at 0x108789878>
		>>> print _
		BTDI
		
		"""

		return(clc.v2.Account(alias=self.alias))


	def __str__(self):
		return(self.data['name'])

