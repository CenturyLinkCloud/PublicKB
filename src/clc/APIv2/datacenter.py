"""
Datacenter related functions.  

These datacenter related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613140-Datacenters
"""

import clc

class Datacenter:

	@staticmethod
	def GetDatacenters(alias=None):
		"""Return all cloud locations available to the calling alias.

		>>> 
		
		"""
		r = clc.v2.API.Call('post','datacenters/%s' % alias,{})

		#if r['Success'] != True: 
		#	if clc.args:  clc.v1.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % ('Account/GetLocations',r['StatusCode'],r['Message']))
		#	raise Exception('Error calling %s.   Status code %s.  %s' % ('Account/GetLocations',r['StatusCode'],r['Message']))
		#elif int(r['StatusCode']) == 0:  
		#	clc.LOCATIONS = [x['Alias'] for x in r['Locations']]
		#	return(r['Locations'])


########### Old code ##################

	@staticmethod
	def GetAlias():  
		"""Return specified alias or if none the alias associated with the provided credentials."""
		if not clc.ALIAS:  clc.v2.API._Login
		return(clc.ALIAS)


	@staticmethod
	def GetLocation():  
		"""Return specified location or if none the default location associated with the provided credentials and alias."""
		if not clc.LOCATION:  Account.GetAccounts()
		return(clc.LOCATION)


	@staticmethod
	def GetAccountDetails(alias=None):
		"""Return account details dict associated with the provided alias."""
		if not alias:  alias = Account.GetAlias()
		r = clc.v1.API.Call('post','Account/GetAccountDetails',{'AccountAlias': alias})
		if r['Success'] != True: 
			if clc.args:  clc.v1.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % ('Account/GetAccountDetails',r['StatusCode'],r['Message']))
			raise Exception('Error calling %s.   Status code %s.  %s' % ('Account/GetAccountDetails',r['StatusCode'],r['Message']))
		elif int(r['StatusCode']) == 0:  
			r['AccountDetails']['Status'] = Account.account_status_itos[r['AccountDetails']['Status']]
			return(r['AccountDetails'])


	@staticmethod
	def GetAccounts(alias=None):
		"""Return account inventory dict containing all subaccounts for the given alias.  If None search from default alias."""
		if alias is not None:  payload = {'AccountAlias': alias}
		else:  payload = {}
		r = clc.v1.API.Call('post','Account/GetAccounts',payload)
		if int(r['StatusCode']) == 0:  
			# Assume first response is always the original account.  Not sure if this is reliable
			if not clc.ALIAS:  clc.ALIAS = r['Accounts'][0]['AccountAlias']
			if not clc.LOCATION:  clc.LOCATION = r['Accounts'][0]['Location']

			return(r['Accounts'])



