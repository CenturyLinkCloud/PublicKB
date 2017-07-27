"""
Billing related functions.

These billing related functions generally align one-for-one with published API calls categorized in the billing category

API v1 - https://t3n.zendesk.com/forums/20616692-Billing
API v2 - n/a
"""

import clc

class Billing:


	@staticmethod
	def GetGroupEstimate(group,alias=None,location=None):
		"""Gets estimated costs for a group of servers.

		https://t3n.zendesk.com/entries/22423906-GetGroupEstimate

		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param group: group name
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		groups_id = clc.Group.GetGroupID(alias,location,group)

		r = clc.v1.API.Call('post','Billing/GetGroupEstimate',{'AccountAlias': alias, 'HardwareGroupID': groups_id})
		if int(r['StatusCode']) == 0:  
			return(r)


	# NOTE - This API isn't returing data as expected
	# NOTE - We aren't returning any of the server-level data here, just group
	@staticmethod
	def GetGroupSummaries(alias=None,date_start=None,date_end=None):
		"""Gets the charges for groups and servers within a given account, and for any date range.

		https://t3n.zendesk.com/entries/22423916-GetGroupSummaries

		:param alias: short code for a particular account.  If none will use account's default alias
		:param date_start: YYYY-MM-DD string for start date.  If None defaults to start of current month
		:param date_end: YYYY-MM-DD string for end date.  If None defaults to current day of current month
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		payload = {'AccountAlias': alias}
		if date_start is not None:  payload['StartDate'] = date_start
		if date_end is not None:  payload['EndDate'] = date_end

		r = clc.v1.API.Call('post','Billing/GetGroupSummaries',payload)
		if int(r['StatusCode']) == 0:  
			return(r['GroupTotals'])


	@staticmethod
	def GetServerEstimate(server,alias=None):
		"""Gets the estimated monthly cost for a given server.

		https://t3n.zendesk.com/entries/22422323-GetServerEstimate

		:param alias: short code for a particular account.  If none will use account's default alias
		:param server: name of server to query
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		r = clc.v1.API.Call('post','Billing/GetServerEstimate',{'AccountAlias': alias, 'ServerName': server})
		if int(r['StatusCode']) == 0:  
			return(r)


	@staticmethod
	def GetAccountSummary(alias=None):
		"""Gets monthly and hourly charges and estimates for a given account or collection of accounts.

		https://t3n.zendesk.com/entries/22408882-GetAccountSummary

		:param alias: short code for a particular account.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		r = clc.v1.API.Call('post','Billing/GetAccountSummary',{'AccountAlias': alias})
		if int(r['StatusCode']) == 0:  
			return(r)



