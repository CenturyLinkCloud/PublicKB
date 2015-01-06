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
	def _Login():
		"""Login to retrieve bearer token and set default accoutn and location aliases."""
		if not clc.v2.V2_API_USERNAME or not clc.v2.V2_API_PASSWD:
			clc.v1.output.Status('ERROR',3,'V2 API username and password not provided')
			raise(clc.APIV2NotEnabled)
			
		r = requests.post("%s%s" % (clc.defaults.ENDPOINT_URL_V2,"authentication/login"), 
						  data={"username": clc.v2.V2_API_USERNAME, "password": clc.v2.V2_API_PASSWD},
						  verify=API._ResourcePath('clc/cacert.pem'))

		if r.status_code == 200:
			clc._LOGIN_TOKEN_V2 = r.json()['bearerToken']
			clc.ALIAS = r.json()['accountAlias']
			clc.LOCATION = r.json()['locationAlias']
		elif r.status_code == 400:
			raise(Exception("Invalid V2 API login.  %s" % (r.json()['message'])))
		else:
			raise(Exception("Error logging into V2 API.  Response code %s. message %s" % (r.status_code,r.json()['message'])))


	@staticmethod
	def Call(method,url,payload,debug=False):
		"""Execute v2 API call.

		:param url: URL paths associated with the API call
		:param payload: dict containing all parameters to submit with POST call

		:returns: decoded API json result
		"""
		if not clc._LOGIN_TOKEN_V2:  API._Login()

		r = requests.request(method,"%s%s" % (clc.defaults.ENDPOINT_URL_V2,url), 
							 headers={'content-type': 'application/json', 'Authorization': "Bearer %s" % clc._LOGIN_TOKEN_V2},
		                     params=payload, 
							 verify=API._ResourcePath('clc/cacert.pem'))

		if debug:
			print "Request: %s %s%s" % (method,clc.defaults.ENDPOINT_URL_V2,url)
			print "\tpayload=%s" % payload
			print "Response: status_code: %s" % r.status_code
			print r.text

		if r.status_code>=200 and r.status_code<300:
			try:
				return(r.json())
			except:
				return({})
		else:
			try:
				raise(clc.APIFailedResponse("Response code %s.  %s. %s %s" % (r.status_code,r.json()['message'],method,"%s%s" % (clc.defaults.ENDPOINT_URL_V2,url))))
			except clc.APIFailedResponse:
				pass
			except:
				raise(clc.APIFailedResponse("Response code %s. %s. %s %s" % (r.status_code,r.text,method,"%s%s" % (clc.defaults.ENDPOINT_URL_V2,url))))


