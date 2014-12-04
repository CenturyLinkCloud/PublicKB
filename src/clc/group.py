"""
Group related functions.

These group related functions generally align one-for-one with published API calls categorized in the group category

API v1 - https://t3n.zendesk.com/forums/20568588-Group
API v2 - https://t3n.zendesk.com/forums/21013480-Groups
"""

import clc

class Group:

	@staticmethod
	def GetGroupID(alias,location,group):
		"""Given a group name return the unique group ID.

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		r = Group.GetGroups(alias,location)
		for row in r:
			if row['Name'] == group:  return(row['ID'])
		else:
			if clc.args:  clc.output.Status("ERROR",3,"Group %s not found in account %s datacenter %s" % (group,alias,location))
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
		if clc.args:  clc.output.Status("ERROR",2,"Group name conversion not yet implemented")
		return(new_data_arr)


	@staticmethod
	def GetGroups(alias,location):
		"""Return all of alias' groups in the given location.

		https://t3n.zendesk.com/entries/20979826-Get-Groups

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		r = clc.API.v1_call('post','Group/GetGroups',{'AccountAlias': alias, 'Location': location})
		for group in r['HardwareGroups']:  clc._GROUP_MAPPING[group['ID']] = group['Name']
		if int(r['StatusCode']) == 0:  return(r['HardwareGroups'])


	@staticmethod
	def Create(alias,location,parent,group,description=''):
		"""Creates a new group

		https://t3n.zendesk.com/entries/20979861-Create-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param parent: groups can be nested - name of parent group.  If None will be a toplevel group in the datacenter
		:param descrption: optional group description
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		if description is None: description = ''
		# TODO - if no parent then assume default group "%s Hardware" % (location)

		parents_id = Group.GetGroupID(alias,location,parent)

		r = clc.API.v1_call('post','Group/CreateHardwareGroup',
		                    {'AccountAlias': alias, 'ParentID': parents_id, 'Name': group, 'Description': description })
		if int(r['StatusCode']) == 0:  return(r['Group'])


	@staticmethod
	def Delete(alias,location,group):
		"""Deletes the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/20999933-Delete-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		groups_id = Group.GetGroupID(alias,location,group)
		r = clc.API.v1_call('post','Group/DeleteHardwareGroup',{'AccountAlias': alias, 'ID': groups_id})
		if int(r['StatusCode']) == 0:  return(r)


	@staticmethod
	def Pause(alias,location,group):
		"""Pauses the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/20996052-Pause-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		groups_id = Group.GetGroupID(alias,location,group)
		r = clc.API.v1_call('post','Group/PauseHardwareGroup',{'AccountAlias': alias, 'ID': groups_id})
		if int(r['StatusCode']) == 0:  return(r)


	@staticmethod
	def Poweron(alias,location,group):
		"""Powers on the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/20996102-Power-On-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		groups_id = Group.GetGroupID(alias,location,group)
		r = clc.API.v1_call('post','Group/PoweronHardwareGroup',{'AccountAlias': alias, 'ID': groups_id})
		if int(r['StatusCode']) == 0:  return(r)


	@staticmethod
	def Archive(alias,location,group):
		"""Archives the Hardware Group along with all child groups and servers.

		https://t3n.zendesk.com/entries/21004506-Archive-Hardware-Group

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.Account.GetAlias()
		groups_id = Group.GetGroupID(alias,location,group)
		r = clc.API.v1_call('post','Group/ArchiveHardwareGroup',{'AccountAlias': alias, 'ID': groups_id})
		if int(r['StatusCode']) == 0:  return(r)


	# TODO - cannot find groups ID since not listed for archived groups
	#@staticmethod
	#def Restore(alias,location,group):
	#	if alias is None:  alias = clc.Account.GetAlias()
	#	groups_id = Group.GetGroupID(alias,location,group)
	#	r = clc.API.v1_call('post','Group/RestoreHardwareGroup',{'AccountAlias': alias, 'ID': groups_id})
	#	if int(r['StatusCode']) == 0:  return(r)



