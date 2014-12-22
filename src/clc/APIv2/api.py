# -*- coding: utf-8 -*-
"""Private class that executes API calls."""

import requests
import xml.etree.ElementTree
import clc
import os
import sys


class API():
	
	# requests module includes cacert.pem which is visible when run as installed module.
	# pyinstall single-file deployment needs cacert.pem packaged along and referenced.
	# This module proxies between the two based on whether the cacert.pem exists in
	# the expected runtime directory.
	#
	# https://github.com/kennethreitz/requests/issues/557
	# http://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
	#
	@staticmethod
	def _ResourcePath(relative):
		if os.path.isfile(os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),relative)):
			# Pyinstall packaged windows file
			return(os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),relative))
		else:
			return(True)


	@staticmethod
	def _Login_v2():
		if not clc.V2_API_USERNAME or not clc.V2_API_PASSWD:
			clc.v1.output.Status('ERROR',3,'V2 API username and password not provided')
			raise(clc.APIV2NotEnabled)
			
		r = requests.post("%s%s" % (clc.defaults.ENDPOINT_URL_V2,"/authentication/login"), 
						  data={'username': clc.v2.V2_API_USERNAME, 'password': clc.v2.V2_API_PASSWD},
						  headers={'content-type': 'application/json'},
						  verify=API._ResourcePath('clc/cacert.pem'))

		if r.status_code == 200:
			clc.LOGIN_TOKEN_V2 = r.json()['bearerToken']
			clc.ALIAS = r.json()['accountAlias']
		elif r.status_code == 400:
			raise(Exception("Invalid V2 API login.  %s" % (r.json()['message'])))
		else:
			raise(Exception("Error logging into V2 API.  Response code %s. message %s" % (r.status_code,r.json()['message'])))


	@staticmethod
	def v2_call(method,url,payload):
		"""Execute v2 API call.

		:param url: URL paths associated with the API call
		:param payload: dict containing all parameters to submit with POST call

		:returns: decoded API json result
		"""
		if not clc._LOGIN_TOKEN_V2:  clc.API._Login_v2()

		r = requests.request(method,"%s%s" % (clc.defaults.ENDPOINT_URL_V2,url), 
		                     params=payload, 
							 headers={'content-type': 'application/json', 'Bearer': clc._LOGIN_TOKEN_V2},
							 verify=API._ResourcePath('clc/cacert.pem'))

		try:
			if int(r.json()['StatusCode']) == 0:  
				if clc.args:  clc.v1.output.Status('SUCCESS',2,'%s' % (r.json()['Message']))
				return(r.json())
			else:
				if clc.args:  clc.v1.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % (url,r.json()['StatusCode'],r.json()['Message']))
				raise(Exception("Error calling %s.   Status code %s.  %s" % (url,r.json()['StatusCode'],r.json()['Message'])))
		except:
			raise
			if clc.args:  clc.v1.output.Status('ERROR',3,'Error calling %s.  Server response %s' % (url,r.status_code))


