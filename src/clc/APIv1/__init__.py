# -*- coding: utf-8 -*-
"""
CenturyLink Cloud Python SDK and CLI tool.

The CenturyLink Cloud Python SDK provides close to a one-to-one mapping between
the v1/v2 API calls within the library.

The CLI portion and other console entry points enable interactive and batch execution
of commands against the CenturyLink Cloud API in a platform independent manner.

CenturyLink Cloud: http://www.CenturyLinkCloud.com
Package Github page: https://github.com/CenturyLinkCloud/clc-python-sdk

API Documentaton v1: http://www.centurylinkcloud.com/api-docs/v1/

"""

from clc.APIv1.shell import Args, ExecCommand
from clc.APIv1.account import Account
from clc.APIv1.user import User
from clc.APIv1.group import Group
from clc.APIv1.server import Server
from clc.APIv1.network import Network
from clc.APIv1.billing import Billing
from clc.APIv1.queue import Queue
from clc.APIv1.blueprint import Blueprint
from clc.APIv1.api import API


####### module/object vars #######
_LOGIN_COOKIE_V1 = False

_V1_ENABLED = False
_LOGINS = 0
_BLUEPRINT_FTP_URL = False

_GROUP_MAPPING = {}

# Disable warnings
try:
	import requests
	requests.packages.urllib3.disable_warnings()
except:
	pass


class output:
	
	@staticmethod
	def Status(status,level,message):
		pass


def SetCredentials(api_key,api_passwd):
	"""Establish API key and password associated with APIv1 commands."""
	global V1_API_KEY
	global V1_API_PASSWD
	global _V1_ENABLED
	_V1_ENABLED = True
	V1_API_KEY = api_key
	V1_API_PASSWD = api_passwd

