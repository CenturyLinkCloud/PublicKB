"""
Network related functions.

These network related functions generally align one-for-one with published API calls categorized in the network category

API v1 - https://t3n.zendesk.com/forums/20587856-Network
API v2 - n/a
"""

import clc

class Network:

	@staticmethod
	def GetNetworks(alias=None,location=None):
		"""Gets the list of Networks mapped to the account in the specified datacenter.

		https://t3n.zendesk.com/entries/21024721-Get-Networks

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides.  If none will use account's primary datacenter
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		r = clc.v1.API.Call('post','Network/GetAccountNetworks', { 'AccountAlias': alias, 'Location': location })
		if int(r['StatusCode']) == 0:  return(r['Networks'])


	@staticmethod
	def GetNetworkDetails(network,alias=None,location=None):
		"""Gets the details for a Network and its IP Addresses.

		https://t3n.zendesk.com/entries/21726312-Get-Network-Details

		:param network: network name
		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides.  If none will use account's primary datacenter
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		r = clc.v1.API.Call('post','Network/GetNetworkDetails', { 'AccountAlias': alias, 'Location': location, 'Name': network })
		if int(r['StatusCode']) == 0:  return(r['NetworkDetails']['IPAddresses'])


	#@staticmethod
	#def Create(alias,location,parent,group,description=''):
	##	if alias is None:  alias = clc.v1.Account.GetAlias()
	#	if description is None: description = ''
	#	# TODO - if no parent then assume default group "%s Hardware" % (locaiton)

	#	parents_id = Group.GetGroupID(alias,location,parent)

	#	r = clc.v1.API.Call('post','Group/CreateHardwareGroup',
	#	                    {'AccountAlias': alias, 'ParentID': parents_id, 'Name': group, 'Description': description })
	#	if int(r['StatusCode']) == 0:  return(r['Group'])


