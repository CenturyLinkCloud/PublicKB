"""
Account related functions.  

These account related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21645944-Account

Account object variables:

	account.accountAlias (synonym for account.alias)
	account.addressLine1
	account.addressLine2
	account.businessName
	account.city
	account.stateProvince
	account.postalCode
	account.telephone
	account.country
	account.status
	account.primaryDataCenter
	account.isManaged

"""

# TODO - change account
# TODO - delete account
# TODO - list subaccounts
# TODO - get primary datacenter
# TODO - get parent account

import clc

class Account:

	@staticmethod
	def GetAlias():  
		"""Return specified alias or if none the alias associated with the provided credentials.

		>>> clc.v2.Account.GetAlias()
		u'BTDI'
		"""
		if not clc.ALIAS:  clc.v2.API._Login()
		return(clc.ALIAS)


	@staticmethod
	def GetLocation():  
		"""Return specified location or if none the default location associated with the provided credentials and alias.
		
		>>> clc.v2.Account.GetLocation()
		u'WA1'
		"""
		if not clc.LOCATION:  clc.v2.API._Login()
		return(clc.LOCATION)


	def __init__(self,alias=None):
		"""Create account object.
		"""

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		self.data = clc.v2.API.Call('GET','accounts/%s' % (self.alias),{})

	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def __str__(self):
		return(self.data['name'])



