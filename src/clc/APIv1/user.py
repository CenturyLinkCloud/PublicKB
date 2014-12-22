"""
User related functions.

These user related functions generally align one-for-one with published API calls categorized in the user category

API v1 - https://t3n.zendesk.com/forums/21512156-Users
API v2 - n/a
"""

import clc

class User:

	user_role_stoi = { 'ServerAdministrator': 2, 'BillingManager': 3, 'DNSManager': 8, 'AccountAdministrator': 9,
	                   'AccountViewer': 10, 'NetworkManager': 12, 'SecurityManager': 13, 'ServerOperator': 14}


	@staticmethod
	def _UserRoleList_itos(roles):
		role_s = []
		for role_i in roles:
			role_s.append(next((s for s, i in User.user_role_stoi.items() if i == role_i), None))

		return(role_s)


	@staticmethod
	def GetUserDetails(user, alias=None):
		"""Gets the details of a specific user associated with a given account.
		
		https://t3n.zendesk.com/entries/22427672-GetUserDetails

		:param alias: short code for a particular account.  If none will use account's default alias
		:param user: user name, which is typically an email address
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		r = clc.v1.API.Call('post','User/GetUserDetails',{'AccountAlias': alias, 'UserName': user })
		if int(r['StatusCode']) == 0:  
			r['UserDetails']['Roles'] = User._UserRoleList_itos(r['UserDetails']['Roles'])
			return(r['UserDetails'])


	@staticmethod
	def GetUsers(alias=None):
		"""Gets all of users assigned to a given account.
		
		https://t3n.zendesk.com/entries/22427662-GetUsers

		:param alias: short code for a particular account.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		r = clc.v1.API.Call('post','User/GetUsers',{'AccountAlias': alias})
		if int(r['StatusCode']) == 0:  
			return(r['Users'])


	@staticmethod
	def DeleteUser(user):
		"""Delete user associated with a given account.
		
		https://t3n.zendesk.com/entries/22454068-DeleteUser

		:param user: user name, which is typically an email address
		"""
		r = clc.v1.API.Call('post','User/DeleteUser',{'UserName': user})


	@staticmethod
	def SuspendUser(user):
		"""Suspend user associated with a given account.
		
		https://t3n.zendesk.com/entries/22422271-SuspendUser

		:param user: user name, which is typically an email address
		"""
		r = clc.v1.API.Call('post','User/SuspendUser',{'UserName': user})


	@staticmethod
	def UnsuspendUser(user):
		"""Unsuspend user associated with a given account.
		
		https://t3n.zendesk.com/entries/21560785-UnsuspendUser

		:param user: user name, which is typically an email address
		"""
		r = clc.v1.API.Call('post','User/UnsuspendUser',{'UserName': user})


	# TODO refactor payload validation/building
	@staticmethod
	def CreateUser(user, email, first_name, last_name, roles, alias=None):
		"""Create new user within a given account.
		
		https://t3n.zendesk.com/entries/22441967-CreateUser

		:param user: user name, which is typically an email address
		:param email: email address.  Password credentials are emailed to this address on account creation
		:param first_name: first name
		:param last_name: surname
		:param roles: list of roles (ServerAdministrator, BillingManager, DNSManager, AccountAdministrator,  AccountViewer, NetworkManager, SecurityManager, ServerOperator)
		:param alias: short code for a particular account.  If none will use account's default alias
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		payload = {'AccountAlias': alias, 'Roles': [] }
		if user is not None:  payload['UserName'] = user
		if email is not None:  payload['EmailAddress'] = email
		if first_name is not None:  payload['FirstName'] = first_name
		if last_name is not None:  payload['LastName'] = last_name
		if roles is not None:
			for role in roles:  payload['Roles'].append(User.user_role_stoi[role])
		r = clc.v1.API.Call('post','User/CreateUser',payload)
		if int(r['StatusCode']) == 0:  
			r['UserDetails']['Roles'] = User._UserRoleList_itos(r['UserDetails']['Roles'])
			return(r['UserDetails'])


	# TODO refactor payload validation/building
	@staticmethod
	def UpdateUser(user, email, first_name, last_name, roles,alias=None):
		"""Update existing user within a given account.
		
		https://t3n.zendesk.com/entries/22454018-UpdateUser

		:param alias: short code for a particular account.  If none will use account's default alias
		:param user: user name, which is typically an email address
		:param email: email address.  Password credentials are emailed to this address on account creation
		:param first_name: first name
		:param last_name: surname
		:param roles: list of roles (ServerAdministrator, BillingManager, DNSManager, AccountAdministrator,  AccountViewer, NetworkManager, SecurityManager, ServerOperator)
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		payload = {'AccountAlias': alias, 'Roles': [] }
		if user is not None:  payload['UserName'] = user
		if email is not None:  payload['EmailAddress'] = email
		if first_name is not None:  payload['FirstName'] = first_name
		if last_name is not None:  payload['LastName'] = last_name
		if roles is not None:
			for role in roles:  payload['Roles'].append(User.user_role_stoi[role])
		r = clc.v1.API.Call('post','User/UpdateUser',payload)
		if int(r['StatusCode']) == 0:  
			r['UserDetails']['Roles'] = User._UserRoleList_itos(r['UserDetails']['Roles'])
			return(r['UserDetails'])



