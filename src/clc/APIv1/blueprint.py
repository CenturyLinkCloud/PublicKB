"""
Blueprint related functions.

These Blueprint related functions generally align one-for-one with published API calls categorized in the Blueprint category

API v1 - https://t3n.zendesk.com/forums/20242326-Blueprint
API v2 - n/a
"""

import re
import os
import ftplib
import urlparse
if os.name == 'posix':  import curses
import operator
import clc

class Blueprint:


	visibility_stoi = { 'Public': 1, 'Private': 2, 'Shared': 3}
	classification_stoi = { 'System': 1, 'Script': 2, 'Scripts': 2, 'Software': 3}

	#@staticmethod
	#def List(type='All'):
	#	r = clc.v1.API.Call('post','Queue/ListQueueRequests',{'ItemStatusType': Queue.item_status_type_map[type] })
	#	if int(r['StatusCode']) == 0:  return(r['Requests'])


	@staticmethod
	def GetStatus(request_id,location=None,alias=None,silent=False):
		"""Gets the status of the specified Blueprint deployment.

		https://t3n.zendesk.com/entries/20561586-Get-Deployment-Status

		:param request_id: the int ID of the Blueprint Deployment to retrieve status for.
		:param alias: short code for a particular account.  If none will use account's default alias
		:param location: datacenter where group resides
		:param silent: disable status output when executed within CLI runtime
		"""
		if alias is None:  alias = clc.v1.Account.GetAlias()
		if location is None:  location = clc.v1.Account.GetLocation()
		r = clc.v1.API.Call('post','Blueprint/GetBlueprintStatus',{'AccountAlias': alias, 'RequestID': request_id, 'LocationAlias': location },silent=silent)
		if int(r['StatusCode']) == 0:  return(r)


	@staticmethod
	def GetPackages(classification,visibility):
		"""Gets a list of Blueprint Packages filtered by classification and visibility.

		https://t3n.zendesk.com/entries/20411357-Get-Packages

		:param classification: package type filter (System, Script, Software)
		:param visibility: package visibility filter (Public, Private, Shared)
		"""
		r = clc.v1.API.Call('post','Blueprint/GetPackages',
							{'Classification': Blueprint.classification_stoi[classification],'Visibility': Blueprint.visibility_stoi[visibility]})
		if int(r['StatusCode']) == 0:  return(r['Packages'])


	@staticmethod
	def GetAllPackages(classification):
		"""Gets a list of all Blueprint Packages with a given classification.

		https://t3n.zendesk.com/entries/20411357-Get-Packages

		:param classification: package type filter (System, Script, Software)
		"""
		packages = []
		for visibility in Blueprint.visibility_stoi.keys():
			try:
				for r in Blueprint.GetPackages(classification,visibility):  packages.append(dict(r.items()+{'Visibility':visibility}.items()))
			except:
				pass
		if len(packages):  return(packages)


	@staticmethod
	def GetAllSystemPackages():
		"""Returns list of all System packages."""
		return(Blueprint.GetAllPackages("System"))


	@staticmethod
	def GetAllScriptsPackages():
		"""Returns list of all Script packages."""
		return(Blueprint.GetAllPackages("Scripts"))


	@staticmethod
	def GetAllSoftwarePackages():
		"""Returns list of all Software packages."""
		return(Blueprint.GetAllPackages("Software"))


	@staticmethod
	def GetPendingPackages():
		"""Returns list of packages pending publishing."""
		r = clc.v1.API.Call('post','Blueprint/GetPendingPackages',{})
		if int(r['StatusCode']) == 0:  return(r['Packages'])


	@staticmethod
	def PackageUpload(package,ftp_url):
		"""Uploads specified zip package to cloud endpoint.

		See URL below for description on how to properly create a package:
		https://t3n.zendesk.com/entries/20348448-Blueprints-Script-and-Software-Package-Management

		:param package: path to zip file containing package.manifest and supporting scripts
		:param ftp_url: ftp URL including credentials of the form ftp://user:password@hostname
		"""
		#o = urlparse.urlparse(ftp_url)
		# Very weak URL checking
		#if o.scheme.lower() != "ftp":  
		#	clc.v1.output.Status('ERROR',2,'Invalid FTP URL')
		#	return

		# Confirm file exists 
		if not os.path.isfile(package):
			clc.v1.output.Status('ERROR',2,'Package file (%s) not found' % (package))
			return

		m = re.search("ftp://(?P<user>.+?):(?P<passwd>.+?)@(?P<host>.+)",ftp_url)
		try:
			ftp = ftplib.FTP(m.group('host'),m.group('user'),m.group('passwd'))
			file = open(package,'rb')   
			filename = re.sub(".*/","",package)
			ftp.storbinary("STOR %s" % (filename),file)
			file.close()
			ftp.quit()
			clc.v1.output.Status('SUCCESS',2,'Blueprint package %s Uploaded' % (filename))
		except Exception as e:
			clc.v1.output.Status('ERROR',2,'FTP error %s: %s' % (ftp_url,str(e)))

		return({})


	@staticmethod
	def PackagePublish(package,classification,visibility,os):
		"""Publishes a Blueprint Package for use within the Blueprint Designer.

		https://t3n.zendesk.com/entries/20426453-Publish-Package

		:param package: path to zip file containing package.manifest and supporting scripts
		:param classification: package type (System, Script, Software)
		:param visibility: package visibility filter (Public, Private, Shared)
		:param os: list of ints containing Operating System template IDs
		"""
		r = clc.v1.API.Call('post','Blueprint/PublishPackage',
							{'Classification': Blueprint.classification_stoi[classification], 'Name': package, 'OperatingSystems': os, 
							 'Visibility': Blueprint.visibility_stoi[visibility]})
		if int(r['StatusCode']) == 0:  return(r)


	# TODO - fix this mess
	@staticmethod
	def _DrawPublishPackageUIPosix(scr,linux_lst,windows_lst):
		scr.addstr(0,2,"Select all Operating Systems to be associated with this Blueprint Package: ")
		scr.addstr(1,2,"('q' when selection is complete)")

		max_pos = 0
		max_col1_len = 0
		pos = 2
		keys = linux_lst.keys()
		keys.sort
		for t in sorted(linux_lst.items(),key = lambda x :x[1]['Description']):
			l = t[0]
			l_f = "(%s)" % (l)
			if len(linux_lst[l]['Description'])>max_col1_len:
				max_col1_len = len(linux_lst[l]['Description'])
			pos += 1
			if linux_lst[l]['selected']:  scr.addstr(pos,1,"%s %s" % (l_f.ljust(4),linux_lst[l]['Description']),curses.A_BOLD)
			else:  scr.addstr(pos,1,"%s %s" % (l_f.ljust(4),linux_lst[l]['Description']))
		max_pos = pos
		pos = 2
		for t in sorted(windows_lst.items(),key = lambda x :x[1]['Description']):
			l = t[0]
			l_f = "(%s)" % (l)
			pos += 1
			if windows_lst[l]['selected']:  scr.addstr(pos,max_col1_len+9,"%s %s" % (l_f.ljust(4),windows_lst[l]['Description']),curses.A_BOLD)
			else:  scr.addstr(pos,max_col1_len+9,"%s %s" % (l_f.ljust(4),windows_lst[l]['Description']))

		if pos>max_pos:  max_pos = pos
		scr.addstr(max_pos+2,2,"	  ")
		scr.addstr(max_pos+2,2,"> ")
		scr.refresh()

		return(scr.getstr())


	# TODO - fix this mess
	@staticmethod
	def _DrawPublishPackageUI(linux_lst,windows_lst):
		print("\nSelect all Operating Systems to be associated with this Blueprint Package: ")
		print("'q' when selection is complete)\n")

		for items_lst in (linux_lst,windows_lst):
			for t in sorted(items_lst.items(),key = lambda x :x[1]['Description']):
				l = t[0]
				l_f = "(%s)" % (l)
				if items_lst[l]['selected']:  print "[x] %s %s" % (l_f.ljust(4),items_lst[l]['Description'])
				else:  print "[ ] %s %s" % (l_f.ljust(4),items_lst[l]['Description'])

		print "\n"
		return(raw_input(" > "))


	# TODO - fix this mess
	@staticmethod
	def PackagePublishUI(package,type,visibility):
		"""Publishes a Blueprint Package for use within the Blueprint Designer after interactive OS selection.

		Interactive selection of one or more operating systems by name.

		:param package: path to zip file containing package.manifest and supporting scripts
		:param classification: package type (System, Script, Software)
		:param visibility: package visibility filter (Public, Private, Shared)
		"""
		# fetch OS list
		linux_lst = {'L': {'selected': False, 'Description': 'All Linux'}}
		windows_lst = {'W': {'selected': False, 'Description': 'All Windows'}}
		for r in clc.v1.Server.GetTemplates():
			r['selected'] = False
			if re.search("Windows",r['Description']):  windows_lst[str(r['OperatingSystem'])] = r
			elif re.search("CentOS|RedHat|Ubuntu",r['Description']):  linux_lst[str(r['OperatingSystem'])] = r


		# Get selections
		if os.name=='posix':
			scr = curses.initscr()
			curses.cbreak(); 
		while True:
			if os.name=='posix':  c = Blueprint._DrawPublishPackageUIPosix(scr,linux_lst,windows_lst)
			else:  c = Blueprint._DrawPublishPackageUI(linux_lst,windows_lst)
			if c.lower() == 'q':  break
			elif c.lower() == 'l':  
				for l in linux_lst:  linux_lst[l]['selected'] = not linux_lst[l]['selected']
			elif c.lower() == 'w':  
				for l in windows_lst:  windows_lst[l]['selected'] = not windows_lst[l]['selected']
			elif c in linux_lst:  linux_lst[c]['selected'] = not linux_lst[c]['selected']
			elif c in windows_lst:  windows_lst[c]['selected'] = not windows_lst[c]['selected']
		if os.name=='posix':
			curses.nocbreak(); curses.echo(); curses.endwin()

		# Extract selections
		ids = []
		for l in dict(linux_lst.items()+windows_lst.items()).values():
			if l['selected'] and 'OperatingSystem' in l:  ids.append(str(l['OperatingSystem']))
		clc.v1.output.Status('SUCCESS',2,'Selected operating system IDs: %s' % (" ".join(ids)))

		return(Blueprint.PackagePublish(package,type,visibility,ids))



