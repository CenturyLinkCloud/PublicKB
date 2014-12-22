"""
Queue related functions.

These queue related functions generally align one-for-one with published API calls categorized in the queue category

API v1 - https://t3n.zendesk.com/forums/20201591-Queue
API v2 - https://t3n.zendesk.com/forums/21772620-Queue
"""

import clc

class Queue:

	item_status_type_map = { 'All': 1, 'Pending': 2, 'Complete': 3, 'Error': 4 }


	@staticmethod
	def List(type='All'):
		"""List of Queued requests and their current status details.

		https://t3n.zendesk.com/entries/20350251-List-Queue-Requests

		:param type: list items in the queue filtered by status (All, Pending, Complete, Error)
		"""
		r = clc.v1.API.Call('post','Queue/ListQueueRequests',{'ItemStatusType': Queue.item_status_type_map[type] })
		if int(r['StatusCode']) == 0:  return(r['Requests'])


	@staticmethod
	def GetStatus(request_id,silent=False):
		"""Gets the status of the specified Blueprint deployment.

		https://t3n.zendesk.com/entries/20345638-Get-Request-Status

		:param request_id: the Request ID returned by any of the operations which Queues an async request to perform any given task
		:param silent: optionally disable all status messages when run in CLI mode
		"""
		r = clc.v1.API.Call('post','Queue/GetRequestStatus',{'RequestID': request_id},silent=silent)
		if int(r['StatusCode']) == 0:  return(r['RequestDetails'])



