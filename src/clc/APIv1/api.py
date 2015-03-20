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
		if not clc._SSL_VERIFY:  return(clc._SSL_VERIFY)
		if os.path.isfile(os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),relative)):
			# Pyinstall packaged windows file
			return(os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),relative))
		else:
			return(True)


	@staticmethod
	def _DebugRequest(request,response):
		print('{}\n{}\n{}\n\n{}\n'.format(
			'-----------REQUEST-----------',
			request.method + ' ' + request.url,
			'\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
			request.body,
		))

		print('{}\n{}\n\n{}'.format(
			'-----------RESPONSE-----------',
			'status: ' + str(response.status_code),
			response.text
		))


	@staticmethod
	def _Login():
		if not clc.v1.V1_API_KEY or not clc.v1.V1_API_PASSWD:
			clc.v1.output.Status('ERROR',3,'V1 API key and password not provided')
			raise(clc.v1.APIV1NotEnabled)

		clc._LOGINS += 1

		r = requests.post("%s%s" % (clc.defaults.ENDPOINT_URL_V1,"/Auth/logon"),
						  params={'APIKey': clc.v1.V1_API_KEY, 'Password': clc.v1.V1_API_PASSWD},
						  verify=API._ResourcePath('clc/cacert.pem'))

		try:
			resp = xml.etree.ElementTree.fromstring(r.text)
			if resp.attrib['StatusCode'] == '0':
				if clc.args:  clc.v1.output.Status('SUCCESS',1,'Logged into v1 API')
				clc._LOGIN_COOKIE_V1 = r.cookies
			else:
				if clc.args:  clc.v1.output.Status('ERROR',3,'Error logging into v1 API.  %s' % resp.attrib['Message'])
				raise(Exception("Error logging into V1 API.  Status code %s. %s" % (resp.attrib['StatusCode'],resp.attrib['Message'])))
		except:
			if clc.args:  clc.v1.output.Status('ERROR',3,'Error logging into v1 API.  Server response %s' % (r.status_code))


	@staticmethod
	def Call(method,url,payload,silent=False,hide_errors=[],recursion_cnt=0,debug=False):
		"""Execute v1 API call.

		:param url: URL paths associated with the API call
		:param payload: dict containing all parameters to submit with POST call
		:param hide_errors: list of API error codes to ignore.  These are not http error codes but returned from the API itself
		:param recursion_cnt: recursion counter.  This call is recursed if we experience a transient error

		:returns: decoded API json result
		"""
		if not clc._LOGIN_COOKIE_V1:  API._Login()

		r = requests.request(method,"%s%s/JSON" % (clc.defaults.ENDPOINT_URL_V1,url), 
							 params=payload, 
							 headers={'content-type': 'application/json'},
							 cookies=clc._LOGIN_COOKIE_V1,
							 verify=API._ResourcePath('clc/cacert.pem'))

		if debug:
			API._DebugRequest(request=requests.Request(method,"%s%s/JSON" % (clc.defaults.ENDPOINT_URL_V1,url),
                              data=payload,headers={}).prepare(),response=r)

		try:
			if int(r.json()['StatusCode']) == 0:  
				if clc.args and not silent:  clc.v1.output.Status('SUCCESS',2,'%s' % (r.json()['Message']))
				return(r.json())
			elif int(r.json()['StatusCode']) in hide_errors:
				return(r.json())
			elif int(r.json()['StatusCode']) == 2:  
				# Account is deleted
				#raise clc.v1.Account.eletedException(r.json()['Message'])
				if clc.args and not silent:  clc.v1.output.Status('ERROR',3,'%s' % (r.json()['Message']))
				raise Exception(r.json()['Message'])
			elif int(r.json()['StatusCode']) == 5:  
				# Account or datacenter does not exist
				raise clc.v1.AccountDoesNotExistException(r.json()['Message'])
			elif int(r.json()['StatusCode']) == 100 and recursion_cnt<2:  
				# Not logged in - this is a transient failure
				clc._LOGIN_COOKIE_V1 = False
				return(clc.v1.API.Call(method,url,payload,silent,hide_errors,recursion_cnt+1))
			elif int(r.json()['StatusCode']) == 100:  
				# Not logged in - this keeps recurring - bail
				raise clc.v1.AccountLoginException(r.json()['Message'])
			else:
				if clc.args and (not hide_errors or not silent):  clc.v1.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % (url,r.json()['StatusCode'],r.json()['Message']))
				raise Exception('Error calling %s.   Status code %s.  %s' % (url,r.json()['StatusCode'],r.json()['Message']))
		#except clc.v1.Account.eletedException, clc.v1.Account.oginException:
		except clc.CLCException:
			raise
		except:
			if clc.args and (not hide_errors or not silent):  clc.v1.output.Status('ERROR',3,'Error calling %s.  Server response %s' % (url,r.status_code))
			#print "Request:  %s %s  params=%s" % (method,"%s%s/JSON" % (clc.defaults.ENDPOINT_URL_V1,url),payload)
			#print "Response: %s" % (r.text)
			#print r.url
			#print url
			#print payload
			#print r.text
			raise Exception('Error calling %s.  Server response %s' % (url,r.status_code))

