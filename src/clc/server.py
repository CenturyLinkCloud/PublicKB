"""
Server related functions.

These server related functions generally align one-for-one with published API calls categorized in the server category

API v1 - https://t3n.zendesk.com/forums/20578872-Server
API v2 - https://t3n.zendesk.com/forums/21613150-Servers
"""

import re
import clc

class Server:

	backup_level_stoi = { 'Standard': 2, 'Premium': 1 }


	@staticmethod
	def GetServerDetails(alias,servers):
		"""Gets estimated costs for a group of servers.

		https://t3n.zendesk.com/entries/21741917-Get-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param server: name of server to queury
		"""
		if alias is None:  alias = clc.Account.GetAlias()

		results = []
		for server in servers:
			r = clc.API.v1_call('post','Server/GetServer', {'AccountAlias': alias, 'Name': server })
			if int(r['StatusCode']) == 0:  results.append(r['Server'])

		return(results)


	@staticmethod
	def GetServers(alias,location,group,name_groups=False):
		"""Gets a deep list of all Servers for a given Hardware Group and its sub groups, or all Servers for a given location.

		https://t3n.zendesk.com/entries/21735513-Get-All-Servers

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		payload = {'AccountAlias': alias }
		if group:  payload['HardwareGroupID'] = clc.Group.GetGroupID(alias,location,group)
		else:  payload['Location'] = location
		r = clc.API.v1_call('post','Server/GetAllServers', payload)
		if name_groups:  r['Servers'] = clc.Group.NameGroups(r['Servers'],'HardwareGroupID')
		if int(r['StatusCode']) == 0:  return(r['Servers'])


	@staticmethod
	def GetAllServers(alias=None,name_groups=False):
		"""Gets a deep list of all Servers in all groups and datacenters.

		:param alias: short code for a particular account.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		servers = []
		clc.Account.GetLocations()
		for location in clc.LOCATIONS:
			try:
				r = clc.API.v1_call('post','Server/GetAllServers', {'AccountAlias': alias, 'Location': location }, hide_errors=[5,] )
				if name_groups:  r['Servers'] = clc.Group.NameGroups(r['Servers'],'HardwareGroupID')
				if int(r['StatusCode']) == 0:  servers += r['Servers']
			except:
				pass
		return(servers)


	@staticmethod
	def GetTemplates(alias=None,location=None):
		"""Gets the list of Templates available to the account and location.

		https://t3n.zendesk.com/entries/23102683-List-Available-Server-Templates

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		if location is None:  location = clc.Account.GetLocation()

		r = clc.API.v1_call('post','Server/ListAvailableServerTemplates', { 'AccountAlias': alias, 'Location': location } )
		return(r['Templates'])


	@staticmethod
	def GetTemplateID(alias,location,name):
		"""Given a template name return the unique OperatingSystem ID.

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param name: template name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		if location is None:  location = clc.Account.GetLocation()

		r = Server.GetTemplates(alias,location)
		for row in r:
			if row['Name'].lower() == name.lower():  return(row['OperatingSystem'])
		else:
			if clc.args:  clc.output.Status("ERROR",3,"Template %s not found in account %s datacenter %s" % (name,alias,location))
			raise Exception("Template not found")


	# TODO - implement custom fields
	@staticmethod
	def Create(alias,location,name,template,cpu,ram,backup_level,group, network='',description='',password=''):
		"""Gets the list of Templates available to the account and location.

		https://t3n.zendesk.com/entries/21006677-Create-Server

		:param alias: short code for a particular account.  If None will use account's default alias
		:param location: datacenter where group resides.  If None will use account's default location
		:param name: server name up to 6 character string that' embedded in final server hostname
		:param template: template name for the server template to base build off
		:param cpu: int number of CPUs from 1-16
		:param ram: int RAM from 1-128
		:param backup_level: Standard or Premium
		:param group: name of group or group ID for server to belong to
		:param network: name of the network to which to deploy the server.  If your account has not yet been assigned a network, leave this blank and one will be assigned automatically
		:param description: optional description for the server.  If None the server name will be used.
		:param password: optional administrator password.  If None the system will generate one
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		if location is None:  location = clc.Account.GetLocation()
		if re.match("^\d+$",group):  groups_id = group
		else:  groups_id = clc.Group.GetGroupID(alias,location,group)

		r = clc.API.v1_call('post','Server/CreateServer', 
		                    { 'AccountAlias': alias, 'LocationAlias': location, 'Description': description, 'Template': template,
							  'Alias': name, 'HardwareGroupID': groups_id, 'ServerType': 1, 'ServiceLevel': Server.backup_level_stoi[backup_level], 
							  'Cpu': cpu, 'MemoryGB': ram, 'ExtraDriveGB': 0, 'Network': network, 'Password': password })
		if int(r['StatusCode']) == 0:  return(r)


	@staticmethod
	def Delete(alias,servers):
		"""Deletes the specified servers and releases all associated resources.

		https://t3n.zendesk.com/entries/21016852-Delete-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		results = []
		for server in servers:
			r = clc.API.v1_call('post','Server/DeleteServer', {'AccountAlias': alias, 'Name': server })
			if int(r['StatusCode']) == 0:  results.append(r)
		return(results)


	@staticmethod
	def GetCredentials(alias,servers):
		"""Gets the credentials for the specified servers.

		https://t3n.zendesk.com/entries/21053657-Get-Server-Credentials

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		results = []
		for server in servers:
			r = clc.API.v1_call('post','Server/GetServerCredentials', {'AccountAlias': alias, 'Name': server })
			if int(r['StatusCode']) == 0:  results.append(r)
		return(results)


