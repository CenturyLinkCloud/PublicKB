"""
Network related functions.  

These network related functions generally align one-for-one with published API calls categorized in the network category

Networks object variables:

	networks.networks - list of all networks

Network object variables:

	network.name
	network.id
	network.type
	network.alias
	network.vlan
	network.netmask
	network.cidr
	network.type
	network.gateway
	network.description

"""


# TODO - create, change, delete NW  - pending API spec
# TODO - get network details (IP range, vlan, etc) - pending API spec
# TODO - filter NW by alias?


import re
import clc

class Networks(object):

	def __init__(self,alias=None,location=None,networks_lst=None):
		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		self.networks = []
		if networks_lst:
			for network in networks_lst:
				self.networks.append(Network(id=network['networkId'],alias=network['accountID'],network_obj=network))
		elif location:
			self._Load(location)
		else:
			raise(clc.CLCException("Networks object requires location or networks_lst"))


	def _Load(self,location):
		"""Load all networks associated with the given location.

		https://www.centurylinkcloud.com/api-docs/v2/#get-network-list#request
		"""

		# https://api.ctl.io/v2-experimental/networks/ALIAS/WA1
		for network in clc.v2.API.Call('GET','/v2-experimental/networks/%s/%s' % (self.alias,location),{}):
			self.networks.append(Network(id=network['id'],alias=self.alias,network_obj=network))


	def Get(self,key):
		"""Get network by providing name, ID, or other unique key.

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for network in self.networks:
			if network.id == key:  return(network)
			if network.name == key:  return(network)


class Network(object):

	def __init__(self,id,alias=None,network_obj=None):
		"""Create Network object."""

		self.id = id
		self.type = type
		self.dirty = False
		self.data = network_obj
		if network_obj:  self.name = network_obj['name']
		#else:
		#	try:
		#		self.Refresh()
		#	except clc.APIFailedResponse as e:
		#		if e.response_status_code==404:  raise(clc.CLCException("Network does not exist"))

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()


#	# TODO - untested below.  API still in experimental spec.  Need to update API.Call
#	def Refresh(self):
#		"""Reloads the network object to synchronize with cloud representation.
#
#		>>> clc.v2.Network("f58148729bd94b02ae8b652f5c5feba3").Refresh()
#
#		"""
#
#		self.dirty = False
#		#GET https://api.ctl.io/v2-experimental/networks/{accountAlias}/{dataCenter}/{Network}?ipAddresses=none|claimed|free|all
#		self.data = clc.v2.API.Call('GET','servers/%s/%s' % (self.alias,self.id),{})
#
#		try:
#			self.data['changeInfo']['createdDate'] = clc.v2.time_utils.ZuluTSToSeconds(self.data['changeInfo']['createdDate'])
#			self.data['changeInfo']['modifiedDate'] = clc.v2.time_utils.ZuluTSToSeconds(self.data['changeInfo']['modifiedDate'])
#
#			# API call switches between GB and MB.  Change to all references are in GB and we drop the units
#			self.data['details']['memoryGB'] = int(math.floor(self.data['details']['memoryMB']/1024))
#		except:
#			pass


	def __getattr__(self,var):
		key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		elif key in self.data['changeInfo']:  return(self.data['changeInfo'][key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


	def __str__(self):
		return(self.id)

