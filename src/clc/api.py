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
			clc.output.Status('ERROR',3,'V2 API username and password not provided')
			raise(Exception("V2 API username and password not provided"))
			
		r = requests.post("%s%s" % (clc.defaults.ENDPOINT_URL_V2,"/authentication/login"), 
						  data={'username': clc.V2_API_USERNAME, 'password': clc.V2_API_PASSWD},
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
	def _Login_v1():
		if not clc.V1_API_KEY or not clc.V1_API_PASSWD:
			clc.output.Status('ERROR',3,'V1 API key and password not provided')
			raise(Exception("V1 API key and password not provided"))

		clc._LOGINS += 1

		r = requests.post("%s%s" % (clc.defaults.ENDPOINT_URL_V1,"/Auth/logon"),
						  params={'APIKey': clc.V1_API_KEY, 'Password': clc.V1_API_PASSWD},
						  verify=API._ResourcePath('clc/cacert.pem'))

		try:
			resp = xml.etree.ElementTree.fromstring(r.text)
			if resp.attrib['StatusCode'] == '0':
				if clc.args:  clc.output.Status('SUCCESS',1,'Logged into v1 API')
				clc._LOGIN_COOKIE_V1 = r.cookies
			else:
				if clc.args:  clc.output.Status('ERROR',3,'Error logging into v1 API.  %s' % resp.attrib['Message'])
				raise(Exception("Error logging into V1 API.  Status code %s. %s" % (resp.attrib['StatusCode'],resp.attrib['Message'])))
		except:
			if clc.args:  clc.output.Status('ERROR',3,'Error logging into v1 API.  Server response %s' % (r.status_code))


	@staticmethod
	def v1_call(method,url,payload,silent=False,hide_errors=[],recursion_cnt=0):
		"""Execute v1 API call.

		:param url: URL paths associated with the API call
		:param payload: dict containing all parameters to submit with POST call
		:param hide_errors: list of API error codes to ignore.  These are not http error codes but returned from the API itself
		:param recursion_cnt: recursion counter.  This call is recursed if we experience a transient error

		:returns: decoded API json result
		"""
		if not clc._LOGIN_COOKIE_V1:  clc.API._Login_v1()

		r = requests.request(method,"%s%s/JSON" % (clc.defaults.ENDPOINT_URL_V1,url), 
		                     params=payload, 
							 headers={'content-type': 'application/json'},
		                     cookies=clc._LOGIN_COOKIE_V1,
							 verify=API._ResourcePath('clc/cacert.pem'))

		try:
			if int(r.json()['StatusCode']) == 0:  
				if clc.args and not silent:  clc.output.Status('SUCCESS',2,'%s' % (r.json()['Message']))
				return(r.json())
			elif int(r.json()['StatusCode']) in hide_errors:
				return(r.json())
			elif int(r.json()['StatusCode']) == 2:  
				# Account is deleted
				#raise clc.AccountDeletedException(r.json()['Message'])
				if clc.args and not silent:  clc.output.Status('ERROR',3,'%s' % (r.json()['Message']))
				raise Exception(r.json()['Message'])
			elif int(r.json()['StatusCode']) == 5:  
				# Account or datacenter does not exist
				raise clc.AccountDoesNotExistException(r.json()['Message'])
			elif int(r.json()['StatusCode']) == 100 and recursion_cnt<2:  
				# Not logged in - this is a transient failure
				clc._LOGIN_COOKIE_V1 = False
				return(clc.API.v1_call(method,url,payload,silent,hide_errors,recursion_cnt+1))
			elif int(r.json()['StatusCode']) == 100:  
				# Not logged in - this keeps recurring - bail
				raise clc.AccountLoginException(r.json()['Message'])
			else:
				if clc.args and (not hide_errors or not silent):  clc.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % (url,r.json()['StatusCode'],r.json()['Message']))
				raise Exception('Error calling %s.   Status code %s.  %s' % (url,r.json()['StatusCode'],r.json()['Message']))
		#except clc.AccountDeletedException, clc.AccountLoginException:
		except clc.CLCException:
			raise
		except:
			if clc.args and (not hide_errors or not silent):  clc.output.Status('ERROR',3,'Error calling %s.  Server response %s' % (url,r.status_code))
			#print "Request:  %s %s  params=%s" % (method,"%s%s/JSON" % (clc.defaults.ENDPOINT_URL_V1,url),payload)
			#print "Response: %s" % (r.text)
			#print r.url
			#print url
			#print payload
			#print r.text
			raise Exception('Error calling %s.  Server response %s' % (url,r.status_code))


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
				if clc.args:  clc.output.Status('SUCCESS',2,'%s' % (r.json()['Message']))
				return(r.json())
			else:
				if clc.args:  clc.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % (url,r.json()['StatusCode'],r.json()['Message']))
				raise(Exception("Error calling %s.   Status code %s.  %s" % (url,r.json()['StatusCode'],r.json()['Message'])))
		except:
			raise
			if clc.args:  clc.output.Status('ERROR',3,'Error calling %s.  Server response %s' % (url,r.status_code))


