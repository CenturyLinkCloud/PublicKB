"""
Network related functions.  

These network related functions generally align one-for-one with published API calls categorized in the network category

Networks object variables:

Network object variables:

	network.name
	network.id
	network.type
	network.alias

"""

import clc

class Networks(object):

	def __init__(self,networks_lst):
		self.networks = []
		for network in networks:
			self.network.append(Network(network))



class Network(object):

	def __init__(self,id,alias=None,network_obj=None):
		"""Create Nework object.

		>>> clc.v2.Group(id="wa1-1798")
		<clc.APIv2.group.Group object at 0x109188b90>

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if group_obj:  self.data = group_obj
		else:  self.data = clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id),{})


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def __str__(self):
		return(self.data['id'])

