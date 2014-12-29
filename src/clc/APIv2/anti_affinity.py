"""
Anti-affinity related functions.  

These Anti-affinity related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21645944-Account
"""

# TODO - Delete Anti-Affinity Policy
# TODO - Update Anti-Affinity Policy
# TODO - Create Anti-Affinity Policy
# TODO - Get Anti-Affinity Policies.  Convenience functions to filter by location
# TODO - Get Anti-Affinity Policy


import clc

class AntiAffinity(object):

	@staticmethod
	def GetAll(alias=None):  
		"""Gets a list of anti-affinity policies within a given account.

		https://t3n.zendesk.com/entries/44657214-Get-Anti-Affinity-Policies

		"""
		if not alias:  alias = clc.v2.Account.GetAlias()
		r = clc.v2.API.Call('GET','antiAffinityPolicies/%s' % alias,{})

	
	#def GetLocation(location=None,alias=None):


	def __init__(self,id,name=None,location=None,


