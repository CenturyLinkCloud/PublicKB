"""
Anti-affinity related functions.  

These Anti-affinity related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21645944-Account
"""

# TODO - Delete Anti-Affinity Policy
# TODO - Update Anti-Affinity Policy
# TODO - Create Anti-Affinity Policy


import clc

class AntiAffinity(object):

	@staticmethod
	def GetAll(alias=None,location=None):  
		"""Gets a list of anti-affinity policies within a given account.

		https://t3n.zendesk.com/entries/44657214-Get-Anti-Affinity-Policies

		>>> clc.v2.AntiAffinity.GetAll()
		[<clc.APIv2.anti_affinity.AntiAffinity object at 0x10c65e910>, <clc.APIv2.anti_affinity.AntiAffinity object at 0x10c65ec90>]

		"""
		if not alias:  alias = clc.v2.Account.GetAlias()

		policies = []
		for r in clc.v2.API.Call('GET','antiAffinityPolicies/%s' % alias,{}):
			if location and r['location'].lower()!=location.lower():  continue
			servers = [obj['id'] for obj in r['links'] if obj['rel'] == "server"]
			policies.append(AntiAffinity(id=r['id'],name=r['name'],location=r['location'],servers=servers))

		return(policies)

	
	@staticmethod
	def GetLocation(location=None,alias=None):
		"""Returns a list of anti-affinity policies within a specific location.

		>>> clc.v2.AntiAffinity.GetLocation("VA1")
		[<clc.APIv2.anti_affinity.AntiAffinity object at 0x105eeded0>]

		"""
		return(AntiAffinity.GetAll(alias=alias,location=location))


	def __init__(self,id,alias=None,name=None,location=None,servers=None):
		"""Create AntiAffinity object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call

		https://t3n.zendesk.com/entries/44658344-Get-Anti-Affinity-Policy

		>>> clc.v2.AntiAffinity(id="f5b5e523ed8e4604842ec417d5502510")
		<clc.APIv2.anti_affinity.AntiAffinity object at 0x104753690>

		"""

		self.id = id

		if not alias:  alias = clc.v2.Account.GetAlias()

		if name:
			self.name = name
			self.location = location
			self.servers = servers
		else:
			r = clc.v2.API.Call('GET','antiAffinityPolicies/%s/%s' % (alias,self.id),{})
			self.name = r['name']
			self.location = r['location']
			self.servers = [obj['id'] for obj in r['links'] if obj['rel'] == "server"]


	def __str__(self):
		pass

