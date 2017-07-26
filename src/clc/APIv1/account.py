"""
Account related functions.  

These account related functions generally align one-for-one with published API calls categorized in the account category

API v1 - https://t3n.zendesk.com/forums/21509857-Account
API v2 - https://t3n.zendesk.com/forums/21645944-Account
"""

import clc

class Account:

	account_status_itos = { 1: 'Action', 2: 'Disabled', 3: 'Deleted', 4: 'Demo' }

	@staticmethod
	def GetAlias():  
		"""Return specified alias or if none the alias associated with the provided credentials."""
		if not clc.ALIAS:  Account.GetAccounts()
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
	def GetLocations():
		"""Return all cloud locations available to the calling alias."""
		r = clc.v1.API.Call('post','Account/GetLocations',{})
		if r['Success'] != True: 
			if clc.args:  clc.v1.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % ('Account/GetLocations',r['StatusCode'],r['Message']))
			raise Exception('Error calling %s.   Status code %s.  %s' % ('Account/GetLocations',r['StatusCode'],r['Message']))
		elif int(r['StatusCode']) == 0:  
			clc.LOCATIONS = [x['Alias'] for x in r['Locations']]
			return(r['Locations'])


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



