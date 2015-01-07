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

# TODO - Create Snapshot - if snapshot exists then remove otherwise snapshot will fail.  parameter to force removal if exists else raise exception
# TODO - details: ipaddresses, alertpolicies, customfields, snapshots
# TODO - links - billing, statistics, activites, public IPs, alert policies, anti-affinit, autoscale, credentials, ip address
# TODO - changeInfo
# TODO - Update Public IP Address
# TODO - Delete Server
# TODO - Remove Public IP Address
# TODO - Get Public IP Address
# TODO - Add Public IP Address
# TODO - Execute Package
# TODO - Set Maintenance Mode
# TODO - Start Maintenance Mode
# TODO - Stop Maintenance Mode
# TODO - Create Server
# TODO - remove constructor server_obj if not used

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

		# successful creation
		>>> clc.v2.Server("CA3BTDICNTRLM01")
		<clc.APIv2.server.Server object at 0x10c28fe50>
		>>> print _
		CA3BTDICNTRLM01

		# error.  API returns 404 when server does not exist, we raise exception
		>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT01')
		clc.CLCException: Server does not exist

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if server_obj:  self.data = server_obj
		else:  
			try:
				self.data = clc.v2.API.Call('GET','servers/%s/%s' % (self.alias,self.id),{})
			except clc.APIFailedResponse as e:
				if e.response_status_code==404:  raise(clc.CLCException("Server does not exist"))


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		elif var in self.data['details']:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Account(self):
		"""Return account object for account containing this server.

		>>> clc.v2.Server("CA3BTDICNTRLM01").Account()
		<clc.APIv2.account.Account instance at 0x108789878>
		>>> print _
		BTDI
		
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

	
	def _Operation(self,operation):
		"""Execute specified operations task against one or more servers.

		Returns a clc.v2.Requests object.  If error due to server(s) already being in
		the requested state this is not raised as an error at this level.
		>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').PowerOn().WaitUntilComplete()
		0

		"""

		try:
			return(clc.v2.Requests(clc.v2.API.Call('POST','operations/%s/servers/%s' % (self.alias,operation),'["%s"]' % self.id),alias=self.alias))
		except clc.APIFailedResponse as e:
			# Most likely a queue add error presented as a 400.  Let Requests parse this
			return(clc.v2.Requests(e.response_json,alias=self.alias))


	def Pause(self):  return(self._Operation('pause'))
	def ShutDown(self):  return(self._Operation('shutDown'))
	def Reboot(self):  return(self._Operation('reboot'))
	def Reset(self):  return(self._Operation('reset'))
	def PowerOn(self):  return(self._Operation('powerOn'))
	def PowerOff(self):  return(self._Operation('powerOff'))


	def Snapshot(self,expiration_days=7):
		"""Take a Hypervisor level snapshot retained for between 1 and 10 days (7 is default).

		"""

		return(clc.v2.Requests(clc.v2.API.Call('POST','operations/%s/servers/createSnapshot' % (self.alias),
		                                       {'serverIds': self.id, 'snapshotExpirationDays': expiration_days})))


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
#		"""Delete server.
#		
#		"""
#		#status = {u'href': u'/v2/operations/btdi/status/wa1-126437', u'id': u'wa1-126437', u'rel': u'status'}
#		status = clc.v2.API.Call('DELETE','groups/%s/%s' % (self.alias,self.id),{})


	def __str__(self):
		return(self.data['name'])

