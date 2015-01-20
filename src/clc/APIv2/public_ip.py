"""
PublicIP related functions.  

PublicIPs object variables:

PublicIP object variables:

	public_ip.id 
	public_ip.partition_paths - list of mounts paths
	public_ip.size - public_ip size in GB

"""


import re
import time
import json
import clc


class PublicIPs(object):

	def __init__(self,server,public_ips_lst):
		self.server = server
		self.public_ips = []
		for public_ip in public_ips_lst:
			self.public_ips.append(PublicIP(id=public_ip['id'],parent=self,public_ip_obj=public_ip))


	def Get(self,key):
		"""Get public_ip by providing mount point or ID

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for public_ip in self.public_ips:
			if public_ip.id == key:  return(public_ip)
			elif key in public_ip.partition_paths:  return(public_ip)


	def Search(self,key):
		"""Search public_ip list by partial mount point or ID

		"""

		results = []
		for public_ip in self.public_ips:
			if public_ip.id.lower().find(key.lower()) != -1:  results.append(public_ip)
			# TODO - search in list to match partial mount points
			elif key.lower() in public_ip.partition_paths:  results.append(public_ip)

		return(results)


	def Add(self,size,path=None,type="partitioned"):
		"""Add new public_ip.

		This request will error if public_ip is protected and cannot be removed (e.g. a system public_ip)

		# Partitioned public_ip
		>>> clc.v2.Server("WA1BTDIX01").PublicIPs().Add(size=20,path=None,type="raw").WaitUntilComplete()
		0

		# Raw public_ip
		>>> clc.v2.Server("WA1BTDIX01").PublicIPs().Add(size=20,path=None,type="raw").WaitUntilComplete()
		0

		"""

		if type=="partitioned" and not path:  raise(clc.CLCException("Must specify path to mount new public_ip"))

		public_ip_set = [{'public_ipId': o.id, 'sizeGB': o.size} for o in self.public_ips]
		public_ip_set.append({'sizeGB': size, 'type': type, 'path': path})
		self.public_ips.append(PublicIP(id=int(time.time()),parent=self,public_ip_obj={'sizeGB': size,'partitionPaths': [path]}))

		self.size = size
		self.server.dirty = True
		return(clc.v2.Requests(clc.v2.API.Call('PATCH','servers/%s/%s' % (self.server.alias,self.server.id),
		                                       json.dumps([{"op": "set", "member": "public_ips", "value": public_ip_set}]))))



class PublicIP(object):

	def __init__(self,id,parent,public_ip_obj=None):
		"""Create PublicIP object."""

		self.id = id
		self.parent = parent
		self.size = public_ip_obj['sizeGB']
		self.data = public_ip_obj


	def Delete(self):
		"""Delete public IP.  

		>>> clc.v2.Server("WA1BTDIX01").PublicIPs().public_ips[2].Delete().WaitUntilComplete()
		0

		"""

		public_ip_set = [{'public_ipId': o.id, 'sizeGB': o.size} for o in self.parent.public_ips if o!=self]
		self.parent.public_ips = [o for o in self.parent.public_ips if o!=self]
		self.parent.server.dirty = True
		return(clc.v2.Requests(clc.v2.API.Call('DELETE','servers/%s/%s/publicIPAddresses/%s' % (self.parent.server.alias,self.parent.server.id,self.id))))


	def __getattr__(self,var):
		key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


	def __str__(self):
		return(self.id)

