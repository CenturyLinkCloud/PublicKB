"""
Datacenter related functions.  

These datacenter related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613140-Datacenters
"""

# TODO Get Data Center Deployment Capabilities
# TODO Get Data Center List
# TODO - init link to billing, statistics, scheduled activities

import clc

class Datacenter:

	@staticmethod
	def GetDatacenters(alias=None):
		"""Return all cloud locations available to the calling alias.

		>>> 
		
		"""
		r = clc.v2.API.Call('post','datacenters/%s' % alias,{})




	def __init__(self,alias=None,location=None):
		"""Create Datacenter object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call

		https://t3n.zendesk.com/entries/31026420-Get-Data-Center-Group


		"""

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()
		if location:  self.location = location
		else:  self.location = clc.v2.Account.GetLocation()

		if False:
			# prepopulated info
			self.name = name
			self.location = location
			#self.servers = servers
		else:
			r = clc.v2.API.Call('GET','datacenters/%s/%s' % (self.alias,self.location),{'GroupLinks': 'true'})
			self.id = r['id']
			self.name = r['name']
			self.root_group_id = [obj['id'] for obj in r['links'] if obj['rel'] == "group"][0]
			self.root_group_name = [obj['name'] for obj in r['links'] if obj['rel'] == "group"][0]


	def Groups(self):
		return(clc.v2.Group.GetAll(xxx))


	def __str__(self):
		return(self.name)

