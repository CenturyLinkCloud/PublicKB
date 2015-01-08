"""
Server related functions.  

These server related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613150-Servers

Server object variables:

	server.id
	server.description
	server.cpu
	server.power_state
	server.memory
	server.storage
	server.group_id
	server.is_template
	server.location_id
	server.name
	server.os
	server.os_type
	server.status
	server.type
	server.storage_type
	server.in_maintenance_mode

"""

# TODO - details: ipaddresses, alertpolicies, customfields
# TODO - links - billing, statistics, activites, public IPs, alert policies, anti-affinit, autoscale, ip address
# TODO - changeInfo
# TODO - Update Public IP Address
# TODO - Remove Public IP Address
# TODO - Get Public IP Address
# TODO - Add Public IP Address
# TODO - Create Server
# TODO - remove constructor server_obj if not used
# TODO - implement Servers class to support operations on multiple servers.  Group ops can line into this directly.
# TODO - create server capture and resolve alias via uuid
# TODO - Clone server method - clones selve as a new server

import re
import math
import json
import clc

class Server(object):


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

		# API call switches between GB and MB.  Change to all references are in GB and we drop the units
		self.data['details']['memoryGB'] = int(math.floor(self.data['details']['memoryMB']/1024))


	def __getattr__(self,var):
		if var in ('memory','storage'):  key = var+'GB'
		else:  key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		elif key in self.data['details']:  return(self.data['details'][key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


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

	
	def Credentials(self):
		return(clc.v2.API.Call('GET','servers/%s/%s/credentials' % (self.alias,self.name)))


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
	def StartMaintenance(self):  return(self._Operation('startMaintenance'))
	def StopMaintenance(self):  return(self._Operation('stopMaintenance'))


	def GetSnapshots(self):
		return([obj['name'] for obj in self.data['details']['snapshots']])


	def ExecutePackage(self,package_id,parameters={}):
		"""Execute an existing Bluerprint package on the server.

		https://t3n.zendesk.com/entries/59727040-Execute-Package

		Requires package ID, currently only available by browsing control and browsing
		for the package itself.  The UUID parameter is the package ID we need.

		>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT06'). \
		           ExecutePackage(package_id="77ab3844-579d-4c8d-8955-c69a94a2ba1a",parameters={}). \
				   WaitUntilComplete()
		0

		"""

		return(clc.v2.Requests(clc.v2.API.Call('POST','operations/%s/servers/executePackage' % (self.alias),
		                                       json.dumps({'servers': [self.id], 'package': {'packageId': package_id, 'parameters': parameters}}))))


	def DeleteSnapshot(self,names=None):
		"""Removes an existing Hypervisor level snapshot.

		Supply one or more snapshot names to delete them concurrently.
		If no snapshot names are supplied will delete all existing snapshots.

		>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').DeleteSnapshot().WaitUntilComplete()
		0

		"""

		if names is None:  names = self.GetSnapshots()

		requests_lst = []
		for name in names:
			name_links = [obj['links'] for obj in self.data['details']['snapshots'] if obj['name']==name][0]
			requests_lst.append(clc.v2.Requests(clc.v2.API.Call('DELETE',[obj['href'] for obj in name_links if obj['rel']=='delete'][0])))
			
		return(sum(requests_lst))


	def RestoreSnapshot(self,name=None):
		"""Restores an existing Hypervisor level snapshot.

		Supply snapshot name to restore
		If no snapshot name is supplied will restore the first snapshot found

		>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').RestoreSnapshot().WaitUntilComplete()
		0

		"""

		if not len(self.data['details']['snapshots']):  raise(clc.CLCException("No snapshots exist"))
		if name is None:  name = self.GetSnapshots()[0]

		name_links = [obj['links'] for obj in self.data['details']['snapshots'] if obj['name']==name][0]
		return(clc.v2.Requests(clc.v2.API.Call('POST',[obj['href'] for obj in name_links if obj['rel']=='restore'][0])))


	@staticmethod
	def Create(name,cpu,memory,template,group_id,network_id,alias=None,password=None,ip_address=None,
	           storage_type="standard",type="standard",primary_dns=None,secondary_dns=None,
			   additional_disks=[],custom_fields=[],ttl=None,managed_os=False,description=None,
			   source_server_password=None,cpu_autoscale_policy_id=None,anti_affinity_policy_id=None,
			   packages=[]):  
		"""Creates a new server.

		https://t3n.zendesk.com/entries/59565550-Create-Server

		# Show get NW
		# Show get tpl

		"""

		if not alias:  alias = clc.v2.Account.GetAlias()

		if not description:  description = name
		if type.lower() not in ("standard","hyperscale"):  raise(clc.CLCException("Invalid type"))
		if storage_type.lower() not in ("standard","premium"):  raise(clc.CLCException("Invalid storage_type"))
		if storage_type.lower() == "premium" and type.lower() == "hyperscale":  raise(clc.CLCException("Invalid type/storage_type combo"))
		# TODO - validate custom_fields as a list of dicts with an id and a value key
		# TODO - validate template exists
		# TODO - validate additional_disks as a list of dicts with a path, sizeGB, and type (partitioned,raw) keys
		# TODO - validate addition_disks path not in template reserved paths
		# TODO - validate antiaffinity policy id set only with type=hyperscale
		# TODO - parse ttl from seconds to "2014-12-17T01:17:17Z" format

		return(clc.v2.Requests(r = clc.v2.API.Call('POST','servers/%s' % (alias),
		         json.dumps({'name': name, 'description': description, 'groupId': group_id, 'sourceServerId': template,
							 'isManagedOS': managed_os, 'primaryDNS': primary_dns, 'secondaryDNS': secondary_dns, 
							 'networkId': network_id, 'ipAddress': ip_address, 'password': password,
							 'sourceServerPassword': source_server_password, 'cpu': cpu, 'cpuAutoscalePolicyId': cpu_autoscale_policy_id,
							 'memoryGB': memory, 'type': type, 'storageType': storage_type, 'antiAffinityPolicyId': anti_affinity_policy_id,
							 'customFields': custom_fields, 'additionalDisks': additional_disks, 'ttl': ttl, 'packages': packages}))))


	def Clone(self,network_id,name=None,cpu=None,memory=None,group_id=None,alias=None,password=None,ip_address=None,
	          storage_type="standard",type="standard",primary_dns=None,secondary_dns=None,
			  additional_disks=None,custom_fields=None,ttl=None,managed_os=False,description=None,
			  source_server_password=None,cpu_autoscale_policy_id=None,anti_affinity_policy_id=None,
			  packages=[],count=1):  
		"""Creates one or more clones of existing server.

		https://t3n.zendesk.com/entries/59565550-Create-Server

		* - network_id is currently a required parameter.  This will change to optional once APIs are available to
		    return the network id of self.
		* - if no password is supplied will reuse the password of self.  Is this the expected behavior?  Take note
		    there is no way to for a system generated password with this pattern since we cannot leave as None
		* - any DNS settings from self aren't propogated to clone since they are unknown at system level and
		    the clone process will touch them
		* - no change to the disk layout we will clone all
		* - clone will not replicate managed OS setting from self so this must be explicitly set

		# Show get NW
		# Show get tpl

		"""

		if not name:  name = re.search("%s(.+)\d{2}$" % self.alias,self.name).group(1)
		if not description and self.description:  description = self.description
		if not cpu:  cpu = self.cpu
		if not memory:  cpu = self.memory
		if not group_id:  group_id = self.group_id
		if not alias:  alias = self.alias
		if not source_server_password: source_server_password = self.Credentials()['password']
		if not password: password = source_server_password	# is this the expected behavior?
		if not storage_type:  storage_type = self.storage_type
		if not type:  type = self.type
		if not custom_fields and len(self.custom_fields): custom_fields = self.custom_fields
		if not description:  description = self.description
		# TODO - #if not cpu_autoscale_policy_id:  cpu_autoscale_policy_id = 
		# TODO - #if not anti_affinity_policy_id:  anti_affinity_policy_id =

		# TODO - need to get network_id of self

		requests_lst = []
		for i in range(1,count):
			requests_lst.append(Server.Create( \
			            self,name,cpu,memory,group_id,network_id,alias,password,ip_address,storage_type,
						type,primary_dns,secondary_dns,additional_disks,custom_fields,ttl,managed_os,description,
                        source_server_password,cpu_autoscale_policy_id,anti_affinity_policy_id,packages=[]))

		return(sum(requests_lst))


#	def Update(self):
#		"""Update group
#
#		*TODO* API not yet documented
#
#		"""
#		raise(Exception("Not implemented"))
#
#
	def Delete(self):
		"""Delete server.

		https://t3n.zendesk.com/entries/59220824-Delete-Server
		
		"""
		return(clc.v2.Requests(clc.v2.API.Call('DELETE','servers/%s/%s' % (self.alias,self.id))))


	def __str__(self):
		return(self.data['name'])

