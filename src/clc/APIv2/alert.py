"""
Alert related functions.  

Alerts object variables:

Alert object variables:

	alert.name
	alert.id (alias of name)
	alert.server (optional server name already mapped to policy)

"""

# TODO - Alerts filter by server, type (RAM, Disk, etc.)
# TODO - Alert map/unmap
# TODO - Alert delete
# TODO - Alert create - missing API spec

import clc


class Alerts(object):

	def __init__(self,alerts_lst,server=None):
		self.alerts = []
		for alert in alerts_lst:
			self.alerts.append(Alert(id=alert['id'],alert_obj=alert,server=server))


	def Get(self,key):
		"""Get alert by providing name, ID, or other unique key.

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for alert in self.alerts:
			if alert.id == key:  return(alert)
			elif alert.name == key:  return(alert)


	def Search(self,key):
		"""Search alert list by providing partial name, ID, or other key.

		"""

		results = []
		for alert in self.alerts:
			if alert.id.lower().find(key.lower()) != -1:  results.append(alert)
			elif alert.name.lower().find(key.lower()) != -1:  results.append(alert)

		return(results)


class Alert(object):

	def __init__(self,id,alert_obj=None,server=None):
		"""Create Alert object."""

		self.id = id
		self.data = alert_obj
		self.server = server


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Unmap(self,servers=[]):
		"""Unmap alert policy from one or more servers.

		If no servers provided and Alert object was created from a server itself this will
		be what is unmapped.

		"""
		# TODO - servers as either str or actual server objects


	def __str__(self):
		return(self.id)

