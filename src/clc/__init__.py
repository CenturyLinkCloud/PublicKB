# -*- coding: utf-8 -*-
"""
CenturyLink Cloud CLI tool and Python SDK.

The CenturyLink Cloud Python SDK provides close to a one-to-one mapping between
the v1/v2 API calls within the library.

The CLI portion and other console entry points enable interactive and batch execution
of commands against the CenturyLink Cloud API in a platform independent manner.

CenturyLink Cloud: http://www.CenturyLinkCloud.com
Package Github page: https://github.com/hk1232/clc

API Documentaton v1: https://t3n.zendesk.com/categories/20012068-API-v1-0
API Documentaton v2: https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-

"""

from clc.shell import Args, ExecCommand
from clc.account import Account
from clc.user import User
from clc.group import Group
from clc.server import Server
from clc.network import Network
from clc.billing import Billing
from clc.queue import Queue
from clc.blueprint import Blueprint
from clc.api import API


####### module/object vars #######
_V1_API_KEY = False
_V1_API_PASSWD = False
_V2_API_USERNAME = False
_V2_API_PASSWD = False

args = False

_LOGIN_COOKIE_V1 = False
_LOGIN_TOKEN_V2 = False

_LOGINS = 0
_ALIAS = False
_LOCATION = False
_BLUEPRINT_FTP_URL = False

_GROUP_MAPPING = {}

LOCATIONS = ['CA1','CA2','CA3','DE1','GB1','GB3','IL1','NY1','UC1','UT1','VA1','WA1']	# point in time snapshot - exec Account.GetLocations for current

class CLCException(Exception):
	pass
class AccountDoesNotExistException(CLCException):
	pass
class AccountDeletedException(CLCException):
	pass
class AccountLoginException(CLCException):
    pass

class output:
	
	@staticmethod
	def Status(status,level,message):
		pass


