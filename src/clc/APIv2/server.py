"""
Server related functions.  

These server related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613150-Servers

Server object variables:

	server.id
	server.description
	server.cpu
	server.memoryMB
	server.powerState
	server.storageGB
	server.groupId
	server.isTemplate
	server.locationId
	server.name
	server.os
	server.osType
	server.status
	server.type
	server.storageType
	server.inMaintenanceMode

"""

# TODO - details: ipaddresses, alertpolicies, customfields, snapshots


import json
import clc

class Server(object):

#	@staticmethod
#	def GetAll(root_group_id,alias=None):  
#		"""Gets a list of groups within a given account.
#
#		"""
#
#		if not alias:  alias = clc.v2.Account.GetAlias()
#
#		groups = []
#		for r in clc.v2.API.Call('GET','groups/%s/%s' % (alias,root_group_id),{})['groups']:
#			groups.append(Group(id=r['id'],alias=alias,server_obj=r))
#		
#		return(groups)



	def __init__(self,id,alias=None,server_obj=None):
		"""Create Server object.

		https://t3n.zendesk.com/entries/32859214-Get-Server

		#If parameters are populated then create object location.  
		#Else if only id is supplied issue a Get Policy call

		>>> clc.v2.Server("CA3BTDICNTRLM01")
		<clc.APIv2.server.Server object at 0x10c28fe50>
		>>> print _
		CA3BTDICNTRLM01

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if server_obj:  self.data = server_obj
		else:  self.data = clc.v2.API.Call('GET','servers/%s/%s' % (self.alias,self.id),{})
		#import pprint
		#pprint.pprint(self.data)


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		elif var in self.data['details']:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Account(self):
		"""Return account object for account containing this server.


		"""

		return(clc.v2.Account(alias=self.alias))


	def Group(self):
		"""Return group object for group containing this server.

		>>> clc.v2.Server("CA3BTDICNTRLM01").Group()
		<clc.APIv2.group.Group object at 0x10b07b7d0>
		>>> print _
		Ansible Managed Servers

		"""

		return(clc.v2.Group(id=self.groupId,alias=self.alias))


#	def Create(self,name,description=None):  
#		"""Creates a new group
#
#		*TODO* 
#
#		"""
#
#		if not description:  description = name
#
#		#clc.v2.API.Call('POST','groups/%s' % (self.alias),{'name': name, 'description': description, 'parentGroupId': self.id},debug=True)
#		raise(Exception("Not implemented"))
#
#
#	def Update(self):
#		"""Update group
#
#		*TODO* API not yet documented
#
#		"""
#		raise(Exception("Not implemented"))
#
#
#	def Delete(self):
#		"""Delete group."""
#		#status = {u'href': u'/v2/operations/btdi/status/wa1-126437', u'id': u'wa1-126437', u'rel': u'status'}
#		status = clc.v2.API.Call('DELETE','groups/%s/%s' % (self.alias,self.id),{})


	def __str__(self):
		return(self.data['name'])

