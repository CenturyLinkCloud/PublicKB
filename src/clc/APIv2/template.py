"""
Template related functions.  

Templates object variables:

Template object variables:

	template.name
	template.id
	template.type
	template.alias

"""



import clc

class Templates(object):

	def __init__(self,templates_lst):
		self.templates = []
		for template in templates_lst:
			self.templates.append(Template(id=template['templateId'],alias=template['accountID'],template_obj=template))


	def Get(self,key):
		"""Get template by providing name, ID, or other unique key.

		If key is not unique and finds multiple matches only the first
		will be returned
		"""

		for template in self.templates:
			if template.id == key:  return(template)
			if template.name == key:  return(template)


class Template(object):

	def __init__(self,id,alias=None,template_obj=None):
		"""Create Template object."""

		self.id = id
		self.type = type
		self.name = template_obj['name']

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()


	def __str__(self):
		return(self.id)

