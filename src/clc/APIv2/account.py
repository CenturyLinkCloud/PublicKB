"""
Account related functions.  

These account related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21645944-Account

Account object variables:

	account.account_alias (synonym for account.alias)
	account.address_line1
	account.address_line2
	account.business_name
	account.city
	account.state_province
	account.postal_code
	account.telephone
	account.country
	account.status
	account.primary_data_center
	account.is_managed

"""

# TODO - change account
# TODO - delete account
# TODO - list subaccounts

import re
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

		>>> clc.v2.Account()
		<clc.APIv2.account.Account instance at 0x1065a2e60>

		"""

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		self.data = clc.v2.API.Call('GET','accounts/%s' % (self.alias),{})


	def ParentAccount(self):
		"""Return the parent account object or None if at the root level for provided credentials.

		# sub-account
		>>> clc.v2.Account(alias='KRAP').ParentAccount()
		<clc.APIv2.account.Account instance at 0x10b77ab90>

		# trying to reach above root level
		>>> clc.v2.Account(alias='KRAP').ParentAccount().ParentAccount()
		None
		"""

		return(Account(alias=self.data['parentAlias']))


	def PrimaryDatacenter(self):
		"""Returns the primary datacenter object associated with the account.

		>>> clc.v2.Account(alias='BTDI').PrimaryDatacenter()
		<clc.APIv2.datacenter.Datacenter instance at 0x10a45ce18>
		>>> print _
		WA1

		"""

		return(clc.v2.Datacenter(alias=self.alias,location=self.data['primaryDataCenter']))


	def __getattr__(self,var):
		if var == "primary_datacenter":  key = "primaryDataCenter"
		else:  key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


	def __str__(self):
		return(self.data['accountAlias'])



