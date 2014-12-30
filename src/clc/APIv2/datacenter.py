"""
Datacenter related functions.  

These datacenter related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613140-Datacenters

Datacenter object variables:

	datacenter.id
	datacenter.name
	datacenter.location

"""

# TODO Get Data Center Deployment Capabilities
# TODO - init link to billing, statistics, scheduled activities

import clc

class Datacenter:

	@staticmethod
	def GetDatacenters(alias=None):
		"""Return all cloud locations available to the calling alias.

		>>> clc.v2.Datacenter.GetDatacenters(alias=None)
		[<clc.APIv2.datacenter.Datacenter instance at 0x101462fc8>, <clc.APIv2.datacenter.Datacenter instance at 0x101464320>]

		"""
		if not alias:  alias = clc.v2.Account.GetAlias()

		datacenters = []
		for r in clc.v2.API.Call('GET','datacenters/%s' % alias,{}):
			datacenters.append(Datacenter(location=r['id'],name=r['name'],alias=alias))

		return(datacenters)


	def __init__(self,location=None,name=None,alias=None):
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
			self.name = r['name']
			self.root_group_id = [obj['id'] for obj in r['links'] if obj['rel'] == "group"][0]
			self.root_group_name = [obj['name'] for obj in r['links'] if obj['rel'] == "group"][0]


	def Groups(self):
		"""Returns groups object rooted at this datacenter.

		>>> wa1 = clc.v2.Datacenter.GetDatacenters()[0]
		>>> wa1.Groups()
		[<clc.APIv2.group.Group object at 0x10144f290>, <clc.APIv2.group.Group object at 0x10144f210>]

		"""

		return(clc.v2.Group.GetAll(root_group_id=self.root_group_id,alias=self.alias))


	def __str__(self):
		return(self.location)

