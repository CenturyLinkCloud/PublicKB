"""
Datacenter related functions.  

These datacenter related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613140-Datacenters
"""

# TODO Get Data Center Deployment Capabilities
# TODO Get Data Center Group
# TODO Get Data Center List

import clc

class Datacenter:

	@staticmethod
	def GetDatacenters(alias=None):
		"""Return all cloud locations available to the calling alias.

		>>> 
		
		"""
		r = clc.v2.API.Call('post','datacenters/%s' % alias,{})

		#if r['Success'] != True: 
		#	if clc.args:  clc.v1.output.Status('ERROR',3,'Error calling %s.   Status code %s.  %s' % ('Account/GetLocations',r['StatusCode'],r['Message']))
		#	raise Exception('Error calling %s.   Status code %s.  %s' % ('Account/GetLocations',r['StatusCode'],r['Message']))
		#elif int(r['StatusCode']) == 0:  
		#	clc.LOCATIONS = [x['Alias'] for x in r['Locations']]
		#	return(r['Locations'])



