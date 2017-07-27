# -*- coding: utf-8 -*-
"""
CenturyLink Cloud Python SDK and CLI tool.

The CenturyLink Cloud Python SDK provides close to a one-to-one mapping between
the v1/v2 API calls within the library.

The CLI portion and other console entry points enable interactive and batch execution
of commands against the CenturyLink Cloud API in a platform independent manner.

CenturyLink Cloud: http://www.CenturyLinkCloud.com
Package Github page: https://github.com/CenturyLinkCloud/clc-python-sdk

API Documentaton v1: https://t3n.zendesk.com/categories/20012068-API-v1-0
API Documentaton v2: https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-

"""

import APIv1 as v1
import APIv2 as v2
import defaults
import requests


####### module/object vars #######
V1_API_KEY = False
V1_API_PASSWD = False
V2_API_USERNAME = False
V2_API_PASSWD = False

ALIAS = False
LOCATION = False

args = False

_SSL_VERIFY = True

_LOGIN_COOKIE_V1 = False
_LOGIN_TOKEN_V2 = False

_V1_ENABLED = False
_V2_ENABLED = False
_LOGINS = 0
_BLUEPRINT_FTP_URL = False
_REQUESTS_SESSION = requests.Session()

_GROUP_MAPPING = {}

LOCATIONS = ['CA1','CA2','CA3','DE1','GB1','GB3','IL1','NY1','UC1','UT1','VA1','WA1']	# point in time snapshot - exec Account.GetLocations for current

def SetRequestsSession(session):
	"""Provide a custom requests session for the SDK to use when invoking the API"""
	global _REQUESTS_SESSION
	_REQUESTS_SESSION = session


class CLCException(Exception):
	pass
class APIV1NotEnabled(CLCException):
	pass
class APIV2NotEnabled(CLCException):
	pass
class AccountDoesNotExistException(CLCException):
	pass
class AccountDeletedException(CLCException):
	pass
class AccountLoginException(CLCException):
    pass
class InvalidAPIResponseException(CLCException):
    pass
class APIFailedResponse(CLCException):
	pass

