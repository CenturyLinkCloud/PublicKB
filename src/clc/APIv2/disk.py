"""
Disk related functions.  

Disks object variables:

Disk object variables:

	disk.id 
	disk.partition_paths - list of mounts paths
	disk.size - disk size in GB

"""
	#{u'id': u'0:0', u'partitionPaths': [], u'sizeGB': 1}


import clc


class Disks(object):

	def __init__(self,server,disks_lst):
		self.server = server
		self.disks = []
		for disk in disks_lst:
			self.disks.append(Disk(id=disk['id'],parent=self,disk_obj=disk))


	def Get(self,key):
		"""Get disk by providing mount point or ID

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for disk in self.disks:
			if disk.id == key:  return(disk)
			elif key in disk.partition_paths:  return(disk)


	def Search(self,key):
		"""Search disk list by partial mount point or ID

		"""

		results = []
		for disk in self.disks:
			if disk.id.lower().find(key.lower()) != -1:  results.append(disk)
			# TODO - search in list to match partial mount points
			elif key.lower() in disk.partition_paths:  results.append(disk)

		return(results)



class Disk(object):

	def __init__(self,id,parent,disk_obj=None):
		"""Create Disk object."""

		self.id = id
		self.server = server
		self.alias = alias
		self.size = disk_obj['sizeGB']
		self.data = disk_obj


	def Grow(self,size):
		"""Grow disk to the newly specified size.

		Size must be less than 1024 and must be greater than the current size.

		"""

		if size>1024:  raise(clc.CLCException("Cannot grow disk beyond 1024GB"))
		if size<=self.size:  raise(clc.CLCException("New size must exceed current disk size"))

		#0: {op: "set", member: "disks",…}
		#value: [{diskId: "0:0", sizeGB: 1, type: "raw"}, {diskId: "0:1", sizeGB: 2, type: "raw"},…]
		#	0: {diskId: "0:0", sizeGB: 1, type: "raw"}
		#	1: {diskId: "0:1", sizeGB: 2, type: "raw"}
		#	2: {diskId: "0:2", sizeGB: 272, type: "raw"}
		return(clc.v2.Requests(clc.v2.API.Call('PATCH','servers/%s/%s' % (self.alias,self.server),
		                                       json.dumps([{"op": "set", "member": "disks", "value": [{'diskId': self.id, 'sizeGB': size}]}]))))


	def Delete(self):
		requests.append(clc.v2.Requests(clc.v2.API.Call('PATCH','servers/%s/%s' % (self.alias,self.server),json.dumps([{"op": "set", "member": key, "value": locals()[key]}]))))


	def __getattr__(self,var):
		key = re.sub("_(.)",lambda pat: pat.group(1).upper(),var)

		if key in self.data:  return(self.data[key])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,key)))


	def __str__(self):
		return(self.id)

