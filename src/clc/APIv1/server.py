"""
Server related functions.

These server related functions generally align one-for-one with published API calls categorized in the server category

API v1 - http://www.centurylinkcloud.com/api-docs/v1/#server
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
		if alias is None:  alias = clc.v1.Account.GetAlias()

		results = []
		for server in servers:
			r = clc.v1.API.Call('post','Server/GetServer', {'AccountAlias': alias, 'Name': server })
			if int(r['StatusCode']) == 0:  results.append(r['Server'])

		return(results)


	@staticmethod
	def GetServers(location,group=None,alias=None,name_groups=False):
		"""Gets a deep list of all Servers for a given Hardware Group and its sub groups, or all Servers for a given location.

		https://t3n.zendesk.com/entries/21735513-Get-All-Servers

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		payload = {'AccountAlias': alias }
		if group:  payload['HardwareGroupUUID'] = clc.v1.Group.GetGroupUUID(group,alias,location)
		else:  payload['Location'] = location

		try:
			r = clc.v1.API.Call('post','Server/GetAllServers', payload)
			if name_groups:  r['Servers'] = clc.v1.Group.NameGroups(r['Servers'],'HardwareGroupUUID')
			if int(r['StatusCode']) == 0:  return(r['Servers'])
		except Exception as e:
			if str(e)=="Hardware does not exist for location":  return([])
			else:  raise


	@staticmethod
	def GetAllServers(alias=None,name_groups=False):
		"""Gets a deep list of all Servers in all groups and datacenters.

		:param alias: short code for a particular account.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		servers = []
		clc.v1.Account.GetLocations()
		for location in clc.LOCATIONS:
			try:
				r = clc.v1.API.Call('post','Server/GetAllServers', {'AccountAlias': alias, 'Location': location }, hide_errors=[5,] )
				if name_groups:  r['Servers'] = clc.v1.Group.NameGroups(r['Servers'],'HardwareGroupUUID')
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
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()

		r = clc.v1.API.Call('post','Server/ListAvailableServerTemplates', { 'AccountAlias': alias, 'Location': location } )
		return(r['Templates'])


	@staticmethod
	def GetTemplateID(alias,location,name):
		"""Given a template name return the unique OperatingSystem ID.

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param name: template name
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()

		r = Server.GetTemplates(alias,location)
		for row in r:
			if row['Name'].lower() == name.lower():  return(row['OperatingSystem'])
		else:
			if clc.args:  clc.v1.output.Status("ERROR",3,"Template %s not found in account %s datacenter %s" % (name,alias,location))
			raise Exception("Template not found")


	# TODO - implement custom fields
	@staticmethod
	def Create(name,template,cpu,ram,backup_level,group,alias=None,location=None,network='',description='',password=''):
		"""Gets the list of Templates available to the account and location.

		https://www.centurylinkcloud.com/api-docs/v1/#server-create-server

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
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		if re.match("^\d+$",group):  groups_uuid = group
		else:  groups_uuid = clc.v1.Group.GetGroupUUID(group,alias,location)

		r = clc.v1.API.Call('post','Server/CreateServer', 
		                    { 'AccountAlias': alias, 'LocationAlias': location, 'Description': description, 'Template': template,
							  'Alias': name, 'HardwareGroupUUID': groups_uuid, 'ServerType': 1, 'ServiceLevel': Server.backup_level_stoi[backup_level], 
							  'Cpu': cpu, 'MemoryGB': ram, 'ExtraDriveGB': 0, 'Network': network, 'Password': password })
		if int(r['StatusCode']) == 0:  return(r)


	@staticmethod
	def ConvertToTemplate(server,template,password=None,alias=None):
		"""Converts an existing server into a template.

		http://www.centurylinkcloud.com/api-docs/v1/#server-convert-server-to-template

		:param server: source server to convert
		:param template: name of destination template
		:param password: source server password (optional - will lookup password if None)
		:param alias: short code for a particular account.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if password is None:  password = clc.v1.Server.GetCredentials([server,],alias)[0]['Password']

		r = clc.v1.API.Call('post','Server/ConvertServerToTemplate', 
		                    { 'AccountAlias': alias, 'Name': server, 'Password': password, 'TemplateAlias': template })
		return(r)



	@staticmethod
	def _ServerActions(action,alias,servers):
		"""Archives the specified servers.

		:param action: the server action url to exec against
		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		results = []
		for server in servers:
			r = clc.v1.API.Call('post','Server/%sServer' % (action), {'AccountAlias': alias, 'Name': server })
			if int(r['StatusCode']) == 0:  results.append(r)
		return(results)


	@staticmethod
	def Archive(servers,alias=None):
		"""Archives the specified servers.

		https://t3n.zendesk.com/entries/21016957-Archive-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Archive",alias,servers))


	@staticmethod
	def Poweron(servers,alias=None):
		"""Powers on the specified servers.

		https://t3n.zendesk.com/entries/20985206-Power-On-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("PowerOn",alias,servers))


	@staticmethod
	def Poweroff(servers,alias=None):
		"""Powers off the specified servers.

		https://t3n.zendesk.com/entries/21005353-Power-Off-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("PowerOff",alias,servers))


	@staticmethod
	def Reboot(servers,alias=None):
		"""Reboots the specified servers.

		https://t3n.zendesk.com/entries/20998347-Reboot-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Reboot",alias,servers))


	@staticmethod
	def Reset(servers,alias=None):
		"""Resets the specified servers.

		https://t3n.zendesk.com/entries/21005363-Reset-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Reset",alias,servers))


	@staticmethod
	def Shutdown(servers,alias=None):
		"""Shuts down the specified servers.

		https://t3n.zendesk.com/entries/23126728-Shutdown-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Shutdown",alias,servers))


	@staticmethod
	def Snapshot(servers,alias=None):
		"""Initiates a server snapshot.

		https://t3n.zendesk.com/entries/23106211-Snapshot-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Snapshot",alias,servers))


	@staticmethod
	def Delete(servers,alias=None):
		"""Deletes the specified servers and releases all associated resources.

		https://t3n.zendesk.com/entries/21016852-Delete-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Delete",alias,servers))


	@staticmethod
	def Pause(servers,alias=None):
		"""Pauses the specified servers and releases all associated resources.

		https://t3n.zendesk.com/entries/21005343-Pause-Server

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		return(Server._ServerActions("Pause",alias,servers))


	@staticmethod
	def GetCredentials(servers,alias=None):
		"""Gets the credentials for the specified servers.

		https://t3n.zendesk.com/entries/21053657-Get-Server-Credentials

		:param alias: short code for a particular account.  If none will use account's default alias
		:param servers: list of server names
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		results = []
		for server in servers:
			r = clc.v1.API.Call('post','Server/GetServerCredentials', {'AccountAlias': alias, 'Name': server })
			if int(r['StatusCode']) == 0:  results.append(r)
		return(results)


	@staticmethod
	def GetDisks(server,alias=None,guest_names=True):
		"""Returns list of disks configured for the server

		https://t3n.zendesk.com/entries/23087091-List-Disks

		:param alias: short code for a particular account.  If none will use account's default alias
		:param server: server name
		:param guest_names: query guest disk names and mount points
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()

		r = clc.v1.API.Call('post','Server/ListDisks', { 'AccountAlias': alias, 'Name': server, 'QueryGuestDiskNames': guest_names } )
		return(r['Disks'])


