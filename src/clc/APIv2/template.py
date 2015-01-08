"""
Template related functions.  

Templates object variables:

Template object variables:

	network.name
	network.id
	network.type
	network.alias

"""


# TODO - create, change, delete NW (need API)
# TODO - get network details (IP range, vlan, etc)
# TODO - find NW by name,id
# TODO - filter NW by alias?


import clc

class Templates(object):

	def __init__(self,networks_lst):
		self.networks = []
		for network in networks_lst:
			self.networks.append(Template(id=network['networkId'],alias=network['accountID'],network_obj=network))


	def Get(self,key):
		"""Get network by providing name, ID, or other unique key.

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for network in self.networks:
			if network.id == key:  return(network)
			if network.name == key:  return(network)


class Template(object):

	def __init__(self,id,alias=None,network_obj=None):
		"""Create Nework object.

		>>> clc.v2.Group(id="wa1-1798")
		<clc.APIv2.group.Group object at 0x109188b90>

		"""

		self.id = id
		self.type = type
		self.name = network_obj['name']

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()


	def __str__(self):
		return(self.id)

