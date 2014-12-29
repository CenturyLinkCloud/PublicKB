"""
Account related functions.  

These account related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21645944-Account
"""

# TODO - Delete Anti-Affinity Policy
# TODO - Update Anti-Affinity Policy
# TODO - Create Anti-Affinity Policy
# TODO - Get Anti-Affinity Policies
# TODO - Get Anti-Affinity Policy


import clc

class Account:

	@staticmethod
	def GetAlias():  
		"""Return specified alias or if none the alias associated with the provided credentials."""
		if not clc.ALIAS:  clc.v2.API._Login()
		return(clc.ALIAS)


	@staticmethod
	def GetLocation():  
		"""Return specified location or if none the default location associated with the provided credentials and alias."""
		if not clc.LOCATION:  clc.v2.API._Login()
		return(clc.LOCATION)


