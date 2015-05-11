"""
Group related functions.

These group related functions generally align one-for-one with published API calls categorized in the group category

API v1 - http://www.centurylinkcloud.com/api-docs/v2/#groups
"""

import clc

class Group:

	@staticmethod
	def GetGroupUUID(group,alias=None,location=None):
		"""Given a group name return the unique group ID.

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		r = Group.GetGroups(location,alias)
		for row in r:
			if row['Name'] == group:  return(row['UUID'])
		else:
			if clc.args:  clc.v1.output.Status("ERROR",3,"Group %s not found in account %s datacenter %s" % (group,alias,location))
			raise Exception("Group not found")


	# TODO - not yet implemented
	@staticmethod
	def NameGroups(data_arr,id_key):
		"""Get group name associated with ID.

		TODO - not yet implemented
		"""
		new_data_arr = []
		for data in data_arr:
			try:
				data_arr[id_key] = clc._GROUP_MAPPING[data[id_key]]
			except:
				pass
			new_data_arr.append(data)
		if clc.args:  clc.v1.output.Status("ERROR",2,"Group name conversion not yet implemented")
		return(new_data_arr)


	@staticmethod
	def GetGroups(location=None,alias=None):
		"""Return all of alias' groups in the given location.

		http://www.centurylinkcloud.com/api-docs/v2/#groups-get-group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		r = clc.v1.API.Call('post','Group/GetGroups',{'AccountAlias': alias, 'Location': location})
		for group in r['HardwareGroups']:  clc._GROUP_MAPPING[group['UUID']] = group['Name']
		if int(r['StatusCode']) == 0:  return(r['HardwareGroups'])


	@staticmethod
	def Create(group,parent=None,description='',alias=None,location=None):
		"""Creates a new group

		https://t3n.zendesk.com/entries/20979861-Create-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param parent: groups can be nested - name of parent group.  If None will be a toplevel group in the datacenter
		:param descrption: optional group description
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		if description is None: description = ''
		if parent is None:  parent = "%s Hardware" % (location)

		parents_uuid = Group.GetGroupUUID(parent,alias,location)

		r = clc.v1.API.Call('post','Group/CreateHardwareGroup',
		                    {'AccountAlias': alias, 'ParentUUID': parents_uuid, 'Name': group, 'Description': description })
		if int(r['StatusCode']) == 0:  return(r['Group'])


	@staticmethod
	def _GroupActions(action,group,alias,location):
		"""Applies group level actions.

		:param action: the server action url to exec against
		:param group: group name
		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter location.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		groups_uuid = Group.GetGroupUUID(group,alias,location)

		r = clc.v1.API.Call('post','Group/%sHardwareGroup' % (action), {'UUID': groups_uuid, 'AccountAlias': alias })
		return(r)


	@staticmethod
	def Delete(group,alias=None,location=None):
		"""Deletes the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/20999933-Delete-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		return(Group._GroupActions("Delete",group,alias,location))


	@staticmethod
	def Pause(group,alias=None,location=None):
		"""Pauses the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/20996052-Pause-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		return(Group._GroupActions("Pause",group,alias,location))


	@staticmethod
	def Poweron(group,alias=None,location=None):
		"""Powers on the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/20996102-Power-On-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		return(Group._GroupActions("Poweron",group,alias,location))


	@staticmethod
	def Archive(group,alias=None,location=None):
		"""Archives the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/21004506-Archive-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		return(Group._GroupActions("Archive",group,alias,location))


	# TODO - cannot find groups ID since not listed for archived groups
	#@staticmethod
	#def Restore(alias,location,group):
	#	if alias is None:  alias = clc.v1.Account.GetAlias()
	#	groups_id = Group.GetGroupID(alias,location,group)
	#	r = clc.v1.API.Call('post','Group/RestoreHardwareGroup',{'AccountAlias': alias, 'ID': groups_id})
	#	if int(r['StatusCode']) == 0:  return(r)



