"""
Network related functions.  

These network related functions generally align one-for-one with published API calls categorized in the network category

Networks object variables:

	networks.networks - list of all n etworks

Network object variables:

	network.name
	network.id
	network.type
	network.alias

"""


# TODO - create, change, delete NW  - pending API spec
# TODO - get network details (IP range, vlan, etc) - pending API spec
# TODO - filter NW by alias?


import clc

class Networks(object):

	def __init__(self,networks_lst):
		self.networks = []
		for network in networks_lst:
			self.networks.append(Network(id=network['networkId'],alias=network['accountID'],network_obj=network))


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
		self.name = network_obj['name']

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()


	def __str__(self):
		return(self.id)

