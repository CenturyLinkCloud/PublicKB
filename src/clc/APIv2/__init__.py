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


####### module/object vars #######
V2_API_USERNAME = False
V2_API_PASSWD = False

_V2_ENABLED = False
_LOGINS = 0
_BLUEPRINT_FTP_URL = False

def SetCredentialsV2(api_username,api_passwd):
	"""Establish API username and password associated with APIv2 commands."""
	global V2_API_USERNAME
	global V2_API_PASSWD
	global _V2_ENABLED
	_V2_ENABLED = True
	V2_API_USERNAME = api_username
	V2_API_PASSWD = api_passwd


