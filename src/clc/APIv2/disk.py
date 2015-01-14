"""
Disk related functions.  

Disks object variables:

Disk object variables:

	disk.name
	disk.id (alias of name)

"""


import clc


class Disks(object):

	def __init__(self,disks_lst):
		self.disks = []
		for disk in disks_lst:
			self.disks.append(Disk(id=disk['id'],disk_obj=disk))


	def Get(self,key):
		"""Get disk by providing mount point or ID

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for disk in self.disks:
			if disk.id == key:  return(disk)
			elif key in disk.partition_paths:  return(disk)


	def Search(self,key):
		"""Search disk list by providing partial mount point or ID

		"""

		results = []
		for disk in self.disks:
			if disk.id.lower().find(key.lower()) != -1:  results.append(disk)
			elif disk.name.lower().find(key.lower()) != -1:  results.append(disk)

		return(results)


class Disk(object):

	#{u'id': u'0:0', u'partitionPaths': [], u'sizeGB': 1}
	def __init__(self,id,disk_obj=None):
		"""Create Disk object."""

		self.id = id
		self.data = disk_obj


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def __str__(self):
		return(self.id)

