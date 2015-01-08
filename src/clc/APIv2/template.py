"""
Template related functions.  

Templates object variables:

Template object variables:

	template.name
	template.id (alias of name)

"""



import clc

class Templates(object):

	def __init__(self,templates_lst):
		self.templates = []
		for template in templates_lst:
			self.templates.append(Template(id=template['name'],template_obj=template))


	def Get(self,key):
		"""Get template by providing name, ID, or other unique key.

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for template in self.templates:
			if template.id == key:  return(template)


class Template(object):

	def __init__(self,id,template_obj=None):
		"""Create Template object."""

		self.id = id
		self.data = template_obj


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def __str__(self):
		return(self.id)

