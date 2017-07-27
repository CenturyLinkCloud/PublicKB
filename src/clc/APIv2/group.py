"""
Group related functions.  

These group related functions generally align one-for-one with published API calls categorized in the group category

API v2 - https://t3n.zendesk.com/forums/21013480-Groups

Groups object variables:
	
	groups.alias

Group object variables:

	group.id
	group.name
	group.description
	group.type
	group.status
	group.server_count
	group.created_by
	group.created_date - POSIX time
	group.modified_by
	group.modified_date - POSIX time
	group.dirty - bool indicating whether server object is different than cloud object

Group object variables available but access subject to change with future releases:

	group.custom_fields

"""

# vCur:

# vNext:
# TODO - Update group
# TODO - Get Group Billing Details
# TODO - Statistics - Pending API spec error 500
# TODO - Links: scheduledActivities, upcomingScheduledActivities, horizontalAutoscalePolicyMapping, defaults
# TODO - find group - recursively search to find and return specific group
# TODO - async operations need to return a work queue class item for further followup
# TODO - server power actions - these take a list of server names which we know
# TODO - horizontalAutoscalePolicyMapping, scheduledActivities, upcomingScheduledActivities
# TODO - archiveGroupAction
# TODO - Groups search by customfields
# TODO - Update Get in templates, etc. to raise error on failure


import re
import json
import clc


class Groups(object):

	def __init__(self,groups_lst,alias=None):

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		self.groups = []
		for group in groups_lst:
			self.groups.append(Group(id=group['id'],alias=self.alias,group_obj=group))


	def Get(self,key):
		"""Get group by providing name, ID, description or other unique key.

		If key is not unique and finds multiple matches only the first
		will be returned

		>>> clc.v2.Datacenter().Groups().Get("Default Group")
		<clc.APIv2.group.Group object at 0x1065e5250>

		"""

		for group in self.groups:
			if group.id.lower() == key.lower():  return(group)
			elif group.name.lower() == key.lower():  return(group)
			elif group.description.lower() == key.lower():  return(group)

		raise(clc.CLCException("Group not found"))	# No Match


	def Search(self,key):
		"""Search group list by providing partial name, ID, description or other key.

		>>> clc.v2.Datacenter().Groups().Search("Default Group")
		[<clc.APIv2.group.Group object at 0x1065b0f50>, <clc.APIv2.group.Group object at 0x1065b0d10>]

		"""

		results = []
		for group in self.groups:
			if group.id.lower().find(key.lower()) != -1:  results.append(group)
			elif group.name.lower().find(key.lower()) != -1:  results.append(group)
			elif group.description.lower().find(key.lower()) != -1:  results.append(group)

		return(results)



class Group(object):

	@staticmethod
	def GetAll(root_group_id,alias=None):  
		"""Gets a list of groups within a given account.

		>>> clc.v2.Group.GetAll("wa1-4416")
		[<clc.APIv2.group.Group object at 0x1065b0190>, <clc.APIv2.group.Group object at 0x1065b0dd0>]

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
		else:  self.Refresh()


	def __getattr__(self,var):
		key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		elif key in self.data['changeInfo']:  return(self.data['changeInfo'][key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


	def Refresh(self):
		"""Reloads the group object to synchronize with cloud representation.
		
		>>> clc.v2.Group("wa-1234").Refresh()
		
		"""

		self.dirty = False
		self.data = clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id))

		self.data['changeInfo']['createdDate'] = clc.v2.time_utils.ZuluTSToSeconds(self.data['changeInfo']['createdDate'])
		self.data['changeInfo']['modifiedDate'] = clc.v2.time_utils.ZuluTSToSeconds(self.data['changeInfo']['modifiedDate'])


	def Defaults(self,key):
		"""Returns default configurations for resources deployed to this group.

		If specified key is not defined returns None.

		# {"cpu":{"inherited":false},"memoryGB":{"inherited":false},"networkId":{"inherited":false},
		# "primaryDns":{"value":"172.17.1.26","inherited":true},"secondaryDns":{"value":"172.17.1.27","inherited":true},
		# "templateName":{"value":"WIN2012DTC-64","inherited":false}}
		"""

		if not hasattr(self,'defaults'):  self.defaults = clc.v2.API.Call('GET','groups/%s/%s/defaults' % (self.alias,self.id))
		try:
			return(self.defaults[key]['value'])
		except:
			return(None)
		

	def Subgroups(self):
		"""Returns a Groups object containing all child groups.

		>>> clc.v2.Group("wa1-4416").Subgroups()
		<clc.APIv2.group.Groups object at 0x105fa27d0>

		"""

		return(Groups(alias=self.alias,groups_lst=self.data['groups']))


	def Servers(self):
		"""Returns a Servers object containing all servers within the group.

		>>> clc.v2.Group("wa1-4416").Servers()
		<clc.APIv2.server.Servers object at 0x1065b0f10>

		"""

		return(clc.v2.Servers(alias=self.alias,servers_lst=[obj['id'] for obj in self.data['links'] if obj['rel']=='server']))


	def Archive(self):  return(self.Servers().Archive())
	def Pause(self):  return(self.Servers().Pause())
	def ShutDown(self):  return(self.Servers().ShutDown())
	def Reboot(self):  return(self.Servers().Reboot())
	def Reset(self):  return(self.Servers().Reset())
	def PowerOn(self):  return(self.Servers().PowerOn())
	def PowerOff(self):  return(self.Servers().PowerOff())
	def StartMaintenance(self):  return(self.Servers().StartMaintenance())
	def StopMaintenance(self):  return(self.Servers().StopMaintenance())


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

		return(clc.v2.Requests(clc.v2.API.Call('DELETE','groups/%s/%s' % (self.alias,self.id),{}),alias=self.alias))
	

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

