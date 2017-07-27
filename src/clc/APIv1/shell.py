"""Command-line interface to the CenturyLink Cloud (CLC) API."""

import argparse
import ConfigParser
import os
import sys
import clc


class Args:

	def __init__(self):
		import clc.APIv1.output
		clc.args = self
		self.ParseArgs()
		self.ImportIni()
		self.MergeEnvironment()
		self.MergeCommands()


	def ParseArgs(self):
		parser = argparse.ArgumentParser(description="CLI tool for interacting with CenturyLink Cloud API.  http://www.CenturyLinkCloud.com")
		parser_sp1 = parser.add_subparsers(title='Commands',dest='command')

		########## Account ###########
		parser_account = parser_sp1.add_parser('accounts', help='Account level activities (list, create, modify)')
		parser_sp2 = parser_account.add_subparsers(dest='sub_command')

		## Get
		parser_account_get = parser_sp2.add_parser('get', help='Get details on root or specified sub-account')
		parser_account_get.add_argument('--alias', help='Operate on specific account alias')

		## List
		parser_account_list = parser_sp2.add_parser('list', help='Show all accounts')
		parser_account_list.add_argument('--alias', help='Operate on specific account alias')

		## Locations
		parser_account_locations = parser_sp2.add_parser('locations', help='Show all datacenter locations')


		########## User ###########
		parser_user = parser_sp1.add_parser('users', help='User level activities (list, create, modify)')
		parser_sp3 = parser_user.add_subparsers(dest='sub_command')

		## Get
		parser_user_get = parser_sp3.add_parser('get', help='Get details on specified user')
		parser_user_get.add_argument('--alias', help='Operate on specific account alias')
		parser_user_get.add_argument('--user', required=True, help='Operate on specific user')

		## Delete
		parser_user_delete = parser_sp3.add_parser('delete', help='Delete specified user')
		parser_user_delete.add_argument('--user', required=True, help='Operate on specific user')

		## Suspend
		parser_user_suspend = parser_sp3.add_parser('suspend', help='Suspend specified user')
		parser_user_suspend.add_argument('--user', required=True, help='Operate on specific user')

		## Unsuspend
		parser_user_unsuspend = parser_sp3.add_parser('unsuspend', help='Unsuspend specified user')
		parser_user_unsuspend.add_argument('--user', required=True, help='Operate on specific user')

		## List
		parser_user_list = parser_sp3.add_parser('list', help='List all users')
		parser_user_list.add_argument('--alias', help='Operate on specific account alias')

		## Create
		parser_user_create = parser_sp3.add_parser('create', help='Create new user')
		parser_user_create.add_argument('--alias', help='Operate on specific account alias')
		parser_user_create.add_argument('--user', required=True, help='Operate on specific user')
		parser_user_create.add_argument('--email', required=True, help='Email address')
		parser_user_create.add_argument('--first-name', required=True, metavar='NAME', help='First Name')
		parser_user_create.add_argument('--last-name', required=True, metavar='NAME', help='Last Name')
		parser_user_create.add_argument('--roles', nargs='*', choices=['ServerAdministrator','BillingManager','DNSManager','AccountAdministrator',
		                                                            'AccountViewer','NetworkManager','SecurityManager','ServerOperator'], 
									 help='Space delimited list')

		## Update
		parser_user_update = parser_sp3.add_parser('update', help='Update existing user')
		parser_user_update.add_argument('--alias', help='Operate on specific account alias')
		parser_user_update.add_argument('--user', required=True, help='Operate on specific user')
		parser_user_update.add_argument('--email', required=True, help='Email address')
		parser_user_update.add_argument('--first-name', required=True, metavar='NAME', help='First Name')
		parser_user_update.add_argument('--last-name', required=True, metavar='NAME', help='Last Name')
		parser_user_update.add_argument('--roles', nargs='*', choices=['ServerAdministrator','BillingManager','DNSManager','AccountAdministrator',
		                                                               'AccountViewer','NetworkManager','SecurityManager','ServerOperator'], 
					                    help='Space delimited list')


		########## Server ###########
		parser_server = parser_sp1.add_parser('servers', help='Server level activities (list, create, modify)')
		parser_sp4 = parser_server.add_subparsers(dest='sub_command')

		## Get
		parser_server_get = parser_sp4.add_parser('get', help='Get server details')
		parser_server_get.add_argument('--alias', help='Operate on specific account alias')
		parser_server_get.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## List
		parser_server_list = parser_sp4.add_parser('list', help='List all servers in a location or group')
		parser_server_list.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_server_list.add_argument('--group', metavar='NAME', help='Group Name (optional)')
		parser_server_list.add_argument('--alias', help='Operate on specific account alias')
		parser_server_list.add_argument('--name-groups', action="store_true", help='Output group names instead of group IDs')

		## List all
		parser_server_list_all = parser_sp4.add_parser('list-all', help='List all servers associated with alias')
		parser_server_list_all.add_argument('--alias', help='Operate on specific account alias')
		parser_server_list_all.add_argument('--name-groups', action="store_true", help='Output group names instead of group IDs')

		## Get templates
		parser_server_templates = parser_sp4.add_parser('templates', help='List all templates')
		parser_server_templates.add_argument('--alias', help='Operate on specific account alias')
		parser_server_templates.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')

		## Create
		parser_server_create = parser_sp4.add_parser('create', help='Create new server')
		parser_server_create.add_argument('--alias', help='Operate on specific account alias')
		parser_server_create.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_server_create.add_argument('--group', required=True,metavar='NAME', help='Group Name or group ID')
		parser_server_create.add_argument('--name', required=True, help='Server name (up to 6 chars)')
		parser_server_create.add_argument('--description', default='', help='Server description')
		parser_server_create.add_argument('--template', required=True, metavar='NAME', help='Template name')
		parser_server_create.add_argument('--backup-level', default='Standard', choices=['Standard','Premier'], help='Storage backup level')
		parser_server_create.add_argument('--cpu', required=True, help='CPU Count (1-8)')
		parser_server_create.add_argument('--ram', required=True, help='RAM GB (1-128)')
		parser_server_create.add_argument('--network', required=True, help='Network name')
		parser_server_create.add_argument('--password', default='', help='Password (if blank system will generate one)')

		## Delete
		parser_server_delete = parser_sp4.add_parser('delete', help='Delete one or more servers')
		parser_server_delete.add_argument('--alias', help='Operate on specific account alias')
		parser_server_delete.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Archive
		parser_server_archive = parser_sp4.add_parser('archive', help='Archive one or more servers')
		parser_server_archive.add_argument('--alias', help='Operate on specific account alias')
		parser_server_archive.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Poweron
		parser_server_poweron = parser_sp4.add_parser('poweron', help='Power on one or more servers')
		parser_server_poweron.add_argument('--alias', help='Operate on specific account alias')
		parser_server_poweron.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Poweroff
		parser_server_poweroff = parser_sp4.add_parser('poweroff', help='Power off one or more servers')
		parser_server_poweroff.add_argument('--alias', help='Operate on specific account alias')
		parser_server_poweroff.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Reset
		parser_server_reset = parser_sp4.add_parser('reset', help='Reset one or more servers')
		parser_server_reset.add_argument('--alias', help='Operate on specific account alias')
		parser_server_reset.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Restore
		parser_server_restore = parser_sp4.add_parser('restore', help='Restore archived server')
		parser_server_restore.add_argument('--server', required=True, metavar='NAME', help='Archived server name')
		parser_server_restore.add_argument('--group', required=True, metavar='NAME', help='Group Name or ID to restore server to')
		parser_server_restore.add_argument('--alias', required=False, help='Operate on specific account alias')
		#parser_server_restore.add_argument('--location', required=False, metavar='LOCATION', help=argparse.SUPPRESS)
		parser_server_restore.add_argument('--location', required=False, metavar='LOCATION', help='Operate on specific datacenter')

		## Shutdown
		parser_server_shutdown = parser_sp4.add_parser('shutdown', help='Shutdown one or more servers')
		parser_server_shutdown.add_argument('--alias', help='Operate on specific account alias')
		parser_server_shutdown.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Snapshot
		parser_server_snapshot = parser_sp4.add_parser('snapshot', help='Snapshot one or more servers')
		parser_server_snapshot.add_argument('--alias', help='Operate on specific account alias')
		parser_server_snapshot.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Pause
		parser_server_pause = parser_sp4.add_parser('pause', help='Pause one or more servers')
		parser_server_pause.add_argument('--alias', help='Operate on specific account alias')
		parser_server_pause.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Convert to template
		parser_server_converttotemplate = parser_sp4.add_parser('convert-to-template', help='Convert server to template')
		parser_server_converttotemplate.add_argument('--alias', help='Operate on specific account alias')
		parser_server_converttotemplate.add_argument('--server', required=True, metavar='NAME', help='Source server name')
		parser_server_converttotemplate.add_argument('--template', required=True, metavar='NAME', help='Target template name')
		parser_server_converttotemplate.add_argument('--password', required=False, metavar='PASSWORD', help='Source server password')

		## Get Credentials
		parser_server_get_credentials = parser_sp4.add_parser('get-credentials', help='Get server administrator login credentials')
		parser_server_get_credentials.add_argument('--alias', help='Operate on specific account alias')
		parser_server_get_credentials.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Get List Disks
		parser_server_list_disks = parser_sp4.add_parser('list-disks', help='List disks mounted to server')
		parser_server_list_disks.add_argument('--alias', help='Operate on specific account alias')
		parser_server_list_disks.add_argument('--server', nargs='*', required=True, metavar='NAME', help='Server name')

		## Add Disk
		parser_server_add_disk = parser_sp4.add_parser('add-disk', help='Add a disk to server')
		parser_server_add_disk.add_argument('--server', required=True, help='Server name')
		parser_server_add_disk.add_argument('--path', required=False, help='The disk''s path')
		parser_server_add_disk.add_argument('--size', required=True, help='The disk''s size in gigabytes')
		parser_server_add_disk.add_argument('--type', required=False, help='The disk type (partitioned)')


		########## Group ###########
		parser_group = parser_sp1.add_parser('groups', help='Group level activities (list, create, modify)')
		parser_sp5 = parser_group.add_subparsers(dest='sub_command')

		## List
		parser_group_list = parser_sp5.add_parser('list', help='List all groups')
		parser_group_list.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_group_list.add_argument('--alias', help='Operate on specific account alias')

		## Create
		parser_group_create = parser_sp5.add_parser('create', help='Create new group')
		parser_group_create.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_group_create.add_argument('--alias', help='Operate on specific account alias')
		parser_group_create.add_argument('--parent', metavar='NAME', help='Parent group name')
		parser_group_create.add_argument('--group', metavar='NAME', required=True, help='Group name')
		parser_group_create.add_argument('--description', help='Group description')

		## Delete
		parser_group_delete = parser_sp5.add_parser('delete', help='Delete specified group')
		parser_group_delete.add_argument('--alias', help='Operate on specific account alias')
		parser_group_delete.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_group_delete.add_argument('--group', required=True, metavar='NAME', help='Group name')

		## Pause
		parser_group_pause = parser_sp5.add_parser('pause', help='Pause specified group')
		parser_group_pause.add_argument('--alias', help='Operate on specific account alias')
		parser_group_pause.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_group_pause.add_argument('--group', required=True, metavar='NAME', help='Group name')

		## Poweron
		parser_group_poweron = parser_sp5.add_parser('poweron', help='Power on specified group')
		parser_group_poweron.add_argument('--alias', help='Operate on specific account alias')
		parser_group_poweron.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_group_poweron.add_argument('--group', required=True, metavar='NAME', help='Group name')

		## Archive
		parser_group_archive = parser_sp5.add_parser('archive', help='Archive specified group')
		parser_group_archive.add_argument('--alias', help='Operate on specific account alias')
		parser_group_archive.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_group_archive.add_argument('--group', required=True, metavar='NAME', help='Group name')

		## Restore
		# TODO - cannot find groups ID since not listed for archived groups
		#parser_group_list = parser_sp5.add_parser('restore', help='Unarchive specified group')
		#parser_group_list.add_argument('--alias', help='Operate on specific account alias')
		#parser_group_list.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		#parser_group_list.add_argument('--group', required=True, metavar='NAME', help='Group name')


		########## Billing ###########
		parser_group = parser_sp1.add_parser('billing', help='Billing activities')
		parser_sp6 = parser_group.add_subparsers(dest='sub_command')

		## GetGroupEstimate
		parser_billing_group_estimate = parser_sp6.add_parser('group-estimate', help='Group level estimate')
		parser_billing_group_estimate.add_argument('--alias', help='Operate on specific account alias')
		parser_billing_group_estimate.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_billing_group_estimate.add_argument('--group', metavar='NAME', required=True, help='Hardware group Name')

		## GetServerEstimate
		parser_billing_server_estimate = parser_sp6.add_parser('server-estimate', help='Group level estimate')
		parser_billing_server_estimate.add_argument('--alias', help='Operate on specific account alias')
		parser_billing_server_estimate.add_argument('--server', required=True, metavar='NAME', help='Server name')

		## GetGroupSummaries
		parser_group_summaries = parser_sp6.add_parser('group-summaries', help='Get charges for all groups within an account')
		parser_group_summaries.add_argument('--alias', help='Operate on specific account alias')
		parser_group_summaries.add_argument('--date-start', metavar='YYYY-MM-DD', help='Date to start. Defaults to first date of cur month')
		parser_group_summaries.add_argument('--date-end', metavar='YYYY-MM-DD', help='Date to end. Defaults to cur day of cur month')

		## GetAccountSummary
		parser_group_summaries = parser_sp6.add_parser('account-summary', help='Get charge summary for an entire account')
		parser_group_summaries.add_argument('--alias', help='Operate on specific account alias')


		########## Network ###########
		parser_network = parser_sp1.add_parser('networks', help='Network activities')
		parser_sp7 = parser_network.add_subparsers(dest='sub_command')

		## List
		parser_network_list = parser_sp7.add_parser('list', help='List all networks')
		parser_network_list.add_argument('--alias', help='Operate on specific account alias')
		parser_network_list.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')

		## Get
		parser_network_list = parser_sp7.add_parser('get', help='Get network details')
		parser_network_list.add_argument('--alias', help='Operate on specific account alias')
		parser_network_list.add_argument('--location', metavar='LOCATION', help='Operate on specific datacenter')
		parser_network_list.add_argument('--network', required=True, metavar='NAME', help='Network name')


		########## Queue ###########
		parser_queue = parser_sp1.add_parser('queue', help='Work queue')
		parser_sp8 = parser_queue.add_subparsers(dest='sub_command')

		## List
		parser_queue_list = parser_sp8.add_parser('list', help='List all queued activities')
		parser_queue_list.add_argument('--type', default='All', choices=['All','Pending','Complete','Error'], help='Queue items to show')


		########## Blueprints ###########
		parser_blueprints = parser_sp1.add_parser('blueprints', help='Blueprints')
		parser_sp9 = parser_blueprints.add_subparsers(dest='sub_command')

		## Pending
		parser_blueprints_pending = parser_sp9.add_parser('list-pending', help='List all pending packages')

		## List
		parser_blueprints_list = parser_sp9.add_parser('list', help='List active packages')
		parser_blueprints_list.add_argument('--type', default='Script', choices=['System','Script','Software'], help='Package category')
		parser_blueprints_list.add_argument('--visibility', default='Public', choices=['Public','Private','Shared'], help='Package visibility')

		## List-scripts, software, system
		parser_sp9.add_parser('list-system', help='List all system packages of any visibility')
		parser_sp9.add_parser('list-scripts', help='List all script packages of any visibility')
		parser_sp9.add_parser('list-software', help='List all software packages of any visibility')

		## TODO Validate package

		## Upload Package
		parser_blueprints_upload = parser_sp9.add_parser('package-upload', help='Upload specified package')
		parser_blueprints_upload.add_argument('--package', metavar='PACKAGE.zip', required=True, help='Package zipfile')
		parser_blueprints_upload.add_argument('--ftp', metavar='ftp://user:password@server', help='Properly formed FTP URL (ftp://user:password@server)')

		## Publish package
		parser_blueprints_publish = parser_sp9.add_parser('package-publish', help='Publish specified package')
		parser_blueprints_publish.add_argument('--package', metavar='NAME', required=True, help='Package name')
		parser_blueprints_publish.add_argument('--type', default='Script', choices=['System','Script','Software'], help='Package category')
		parser_blueprints_publish.add_argument('--visibility', default='Private', choices=['Public','Private','Shared'], help='Package visibility')
		# TODO - find way to capture explicit OS IDs or OS groupings like "Windows", "Linux", or if none supplied then display collector UI
		parser_blueprints_publish.add_argument('--os', nargs='*', metavar='ID', help='Operating system(s)')

		## TODO uvp (upload, validate, publish shortcut)


		########## Global ###########
		parser.add_argument('--cols', nargs='*', metavar='COL', help='Include only specific columns in the output')
		parser.add_argument('--config', '-c', help='Ini config file')
		parser.add_argument('--v1-api-key', metavar='KEY', help='V1 API key')
		parser.add_argument('--v1-api-passwd', metavar='PASSWORD', help='V1 API password')
		parser.add_argument('--v2-api-username', metavar='USERNAME', help='V2 API username')
		parser.add_argument('--v2-api-passwd', metavar='PASSWORD', help='V2 API password')
		parser.add_argument('--async', action="store_true", default=False, help='Return immediately after queueing long-running calls')
		parser.add_argument('--quiet', '-q', action='count', help='Supress status output (repeat up to 2 times)')
		parser.add_argument('--verbose', '-v', action='count', help='Increase verbosity')
		parser.add_argument('--format', '-f', choices=['json','table','text','csv'], default='table', help='Output result format (table is default)')
		self.args = parser.parse_args()


	def GetCommand(self):  return(self.args.command)
	def GetArgs(self):  return(self.args)


	def ImportIni(self):
		config_file = False
		# Order of preference - cmd line specified, home directory file, or system file
		if self.args.config:
			config_file = self.args.config
			if self.args.config and not os.path.isfile(self.args.config):
				clc.v1.output.Status('ERROR',3,"Config file %s not found" % (self.args.config))
				sys.exit(1)
		elif os.name=='nt':
			if os.path.isfile("%s/clc/clc.ini" % (os.getenv("PROGRAMDATA"))):
				config_file = "%s/clc/clc.ini" % (os.getenv("PROGRAMDATA"))
			elif os.path.isfile("clc.ini"):
				config_file = "clc.ini"
		else:
			if os.path.isfile("%s/.clc" % (os.environ['HOME'])):
				config_file = "%s/.clc" % (os.environ['HOME'])
			elif os.path.isfile("/usr/local/etc/clc_config"):
				config_file = "/usr/local/etc/clc_config"
		if config_file:  
			clc.v1.output.Status('SUCCESS',3,"Reading %s" % (config_file))
			config = ConfigParser.ConfigParser()
			config.read(config_file)

			if config.has_option('global','v1_api_key'):  clc.v1.V1_API_KEY = config.get('global','v1_api_key')
			if config.has_option('global','v1_api_passwd'):  clc.v1.V1_API_PASSWD = config.get('global','v1_api_passwd')
			if config.has_option('global','v2_api_username'):  clc.v2.V2_API_USERNAME = config.get('global','v2_api_username')
			if config.has_option('global','v2_api_passwd'):  clc.v1.V2_API_PASSWD = config.get('global','v2_api_passwd')

			if config.has_option('global','blueprint_ftp_url'):  clc._BLUEPRINT_FTP_URL = config.get('global','blueprint_ftp_url')


	def MergeEnvironment(self):
		if 'V1_API_KEY' in os.environ:  clc.v1.V1_API_KEY = os.environ['V1_API_KEY']
		if 'V1_API_PASSWD' in os.environ:  clc.v1.V1_API_PASSWD = os.environ['V1_API_PASSWD']
		if 'V2_API_USERNAME' in os.environ:  clc.v2.V2_API_USERNAME = os.environ['V2_API_USERNAME']
		if 'V2_API_PASSWD' in os.environ:  clc.v2.V2_API_PASSWD = os.environ['V2_API_PASSWD']


	def MergeCommands(self):
		if self.args.v1_api_key:  clc.v1.V1_API_KEY = self.args.v1_api_key
		if self.args.v1_api_passwd:  clc.v1.V1_API_PASSWD = self.args.v1_api_passwd
		if self.args.v2_api_username:  clc.v2.V2_API_USERNAME = self.args.v2_api_username
		if self.args.v2_api_passwd:  clc.v2.V2_API_PASSWD = self.args.v2_api_passwd




class ExecCommand():
	def __init__(self):
		import clc.APIv1.output

		try:
			self.Bootstrap()
		except Exception as e:
			clc.v1.output.Status("ERROR",3,"Exiting due to error: %s" % (str(e)))
			sys.exit(1)


	def Bootstrap(self):
		if clc.args.GetCommand() == 'accounts':  self.Account()
		elif clc.args.GetCommand() == 'users':  self.User()
		elif clc.args.GetCommand() == 'groups':  self.Group()
		elif clc.args.GetCommand() == 'servers':  self.Server()
		elif clc.args.GetCommand() == 'billing':  self.Billing()
		elif clc.args.GetCommand() == 'networks':  self.Network()
		elif clc.args.GetCommand() == 'queue':  self.Queue()
		elif clc.args.GetCommand() == 'blueprints':  self.Blueprints()


	def Account(self):
		if clc.args.GetArgs().sub_command == 'list':  self.GetAccounts()
		elif clc.args.GetArgs().sub_command == 'get':  self.GetAccountDetails()
		elif clc.args.GetArgs().sub_command == 'locations':  self.GetLocations()


	def User(self):
		if clc.args.GetArgs().sub_command == 'list':  self.GetUsers()
		elif clc.args.GetArgs().sub_command == 'get':  self.GetUserDetails()
		elif clc.args.GetArgs().sub_command == 'create':  self.CreateUser()
		elif clc.args.GetArgs().sub_command == 'update':  self.UpdateUser()
		elif clc.args.GetArgs().sub_command == 'delete':  self.DeleteUser()
		elif clc.args.GetArgs().sub_command == 'suspend':  self.SuspendUser()
		elif clc.args.GetArgs().sub_command == 'unsuspend':  self.UnsuspendUser()


	def Group(self):
		if clc.args.GetArgs().sub_command == 'list':  self.GetGroups()
		elif clc.args.GetArgs().sub_command == 'create':  self.CreateGroup()
		elif clc.args.GetArgs().sub_command == 'delete':  self.DeleteGroup()
		elif clc.args.GetArgs().sub_command == 'pause':  self.PauseGroup()
		elif clc.args.GetArgs().sub_command == 'archive':  self.ArchiveGroup()
		elif clc.args.GetArgs().sub_command == 'restore':  self.RestoreGroup()
		elif clc.args.GetArgs().sub_command == 'poweron':  self.PoweronGroup()


	def Server(self):
		if clc.args.GetArgs().sub_command == 'list-all':  self.GetAllServers()
		elif clc.args.GetArgs().sub_command == 'list':  self.GetServers()
		elif clc.args.GetArgs().sub_command == 'templates':  self.GetServerTemplates()
		elif clc.args.GetArgs().sub_command == 'get':  self.GetServerDetails()
		elif clc.args.GetArgs().sub_command == 'delete':  self.ServerActions("Delete")
		elif clc.args.GetArgs().sub_command == 'archive':  self.ServerActions("Archive")
		elif clc.args.GetArgs().sub_command == 'poweron':  self.ServerActions("Poweron")
		elif clc.args.GetArgs().sub_command == 'poweroff':  self.ServerActions("Poweroff")
		elif clc.args.GetArgs().sub_command == 'reset':  self.ServerActions("Reset")
		elif clc.args.GetArgs().sub_command == 'restore':  self.RestoreServer()
		elif clc.args.GetArgs().sub_command == 'shutdown':  self.ServerActions("Shutdown")
		elif clc.args.GetArgs().sub_command == 'snapshot':  self.ServerActions("Snapshot")
		elif clc.args.GetArgs().sub_command == 'pause':  self.ServerActions("Pause")
		elif clc.args.GetArgs().sub_command == 'create':  self.CreateServer()
		elif clc.args.GetArgs().sub_command == 'convert-to-template':  self.ConvertToTemplate()
		elif clc.args.GetArgs().sub_command == 'get-credentials':  self.GetServerCredentials()
		elif clc.args.GetArgs().sub_command == 'list-disks':  self.GetServerDisks()
		elif clc.args.GetArgs().sub_command == 'add-disk':  self.AddServerDisk()


	def Network(self):
		if clc.args.GetArgs().sub_command == 'list':  self.GetNetworks()
		elif clc.args.GetArgs().sub_command == 'get':  self.GetNetworkDetails()


	def Billing(self):
		if clc.args.GetArgs().sub_command == 'group-estimate':  self.GetGroupEstimate()
		elif clc.args.GetArgs().sub_command == 'group-summaries':  self.GetGroupSummaries()
		elif clc.args.GetArgs().sub_command == 'account-summary':  self.GetAccountSummary()
		elif clc.args.GetArgs().sub_command == 'server-estimate':  self.GetServerEstimate()


	def Queue(self):
		if clc.args.GetArgs().sub_command == 'list':  self.GetQueue()


	def Blueprints(self):
		if clc.args.GetArgs().sub_command == 'list-pending':  self.GetBlueprintsPending()
		elif clc.args.GetArgs().sub_command == 'list':  self.GetBlueprintsPackages()
		elif clc.args.GetArgs().sub_command == 'list-system':  self.GetBlueprintsSystemPackages()
		elif clc.args.GetArgs().sub_command == 'list-scripts':  self.GetBlueprintsScriptsPackages()
		elif clc.args.GetArgs().sub_command == 'list-software':  self.GetBlueprintsSoftwarePackages()
		elif clc.args.GetArgs().sub_command == 'package-upload':  self.GetBlueprintsPackageUpload()
		elif clc.args.GetArgs().sub_command == 'package-publish':  self.PublishBlueprintsPackage()


	def _GetAlias(self):
		if clc.args.args.alias:  return(clc.args.args.alias)
		else:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS

			return(alias)


	def _GetLocation(self):
		location = None
		try:
			location = clc.args.args.location
		except:
			if not location:
				self.Exec('clc.v1.Account.GetLocation','',supress_output=True)
				location = clc.LOCATION

		return(location)


	def GetAccounts(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		self.Exec('clc.v1.Account.GetAccounts', {'alias': alias}, cols=['AccountAlias','ParentAlias','BusinessName','Location','IsActive'])


	def GetAccountDetails(self):
		self.Exec('clc.v1.Account.GetAccountDetails', {'alias': self._GetAlias()}, cols=['AccountAlias', 'Status', 'City', 'Fax', 'Address1', 'Address2', 'ShareParentNetworks', 'Telephone', 'Country', 'Location', 'BusinessName', 'PostalCode', 'TimeZone', 'StateProvince', 'ParentAlias'])


	def GetLocations(self):
		self.Exec('clc.v1.Account.GetLocations', {}, cols=['Alias', 'Region'])


	def GetUsers(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		self.Exec('clc.v1.User.GetUsers', { 'alias': alias }, cols=['UserName','EmailAddress','FirstName','LastName','Roles'])


	def DeleteUser(self):
		self.Exec('clc.v1.User.DeleteUser', { 'user': clc.args.args.user }, supress_output=True)


	def SuspendUser(self):
		self.Exec('clc.v1.User.SuspendUser', { 'user': clc.args.args.user }, supress_output=True)


	def UnsuspendUser(self):
		self.Exec('clc.v1.User.UnsuspendUser', { 'user': clc.args.args.user }, supress_output=True)


	def GetUserDetails(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		self.Exec('clc.v1.User.GetUserDetails', { 'alias': alias, 'user': clc.args.GetArgs().user}, 
		          cols=['UserName', 'MobileNumber', 'AllowSMS', 'SAMLUserName', 'Status', 'Roles', 'FirstName', 'Title', 
				        'LastName', 'OfficeNumber', 'FaxNumber', 'TimeZoneID', 'AccountAlias', 'EmailAddress', 'AlternateEmailAddress'])


	def CreateUser(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		self.Exec('clc.v1.User.CreateUser', { 'alias': alias, 'user': clc.args.args.user, 'email': clc.args.args.email, 
		                                   'first_name': clc.args.args.first_name, 'last_name': clc.args.args.last_name,
										   'roles': clc.args.args.roles }, 
		          cols=['UserName', 'MobileNumber', 'AllowSMS', 'SAMLUserName', 'Status', 'Roles', 'FirstName', 'Title', 
				        'LastName', 'OfficeNumber', 'FaxNumber', 'TimeZoneID', 'AccountAlias', 'EmailAddress', 'AlternateEmailAddress'])


	def UpdateUser(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		self.Exec('clc.v1.User.UpdateUser', { 'alias': alias, 'user': clc.args.args.user, 'email': clc.args.args.email, 
		                                   'first_name': clc.args.args.first_name, 'last_name': clc.args.args.last_name,
										   'roles': clc.args.args.roles }, 
		          cols=['UserName', 'MobileNumber', 'AllowSMS', 'SAMLUserName', 'Status', 'Roles', 'FirstName', 'Title', 
				        'LastName', 'OfficeNumber', 'FaxNumber', 'TimeZoneID', 'AccountAlias', 'EmailAddress', 'AlternateEmailAddress'])


	def GetGroups(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		self.Exec('clc.v1.Group.GetGroups', { 'alias': alias, 'location': location }, cols=['UUID','Name','ParentUUID','IsSystemGroup'])


	def CreateGroup(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		if not clc.args.args.parent:  parent = "%s Hardware" % (location)
		else:  parent = clc.args.args.parent
		self.Exec('clc.v1.Group.Create', 
		          { 'alias': alias, 'location': location, 'parent': parent, 'group': clc.args.args.group, 
				    'description': clc.args.args.description }, 
		          cols=['UUID','Name','ParentUUID'])


	def DeleteGroup(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		self.Exec('clc.v1.Group.Delete', 
		          { 'alias': alias, 'location': location, 'group': clc.args.args.group },
		          cols=['RequestID','StatusCode','Message'])


	def PauseGroup(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		self.Exec('clc.v1.Group.Pause', 
		          { 'alias': alias, 'location': location, 'group': clc.args.args.group },
		          cols=['RequestID','StatusCode','Message'])


	def PoweronGroup(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		self.Exec('clc.v1.Group.Poweron', 
		          { 'alias': alias, 'location': location, 'group': clc.args.args.group },
		          cols=['RequestID','StatusCode','Message'])


	def ArchiveGroup(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetLocation','',supress_output=True)
			location = clc.LOCATION
		self.Exec('clc.v1.Group.Archive', 
		          { 'alias': alias, 'location': location, 'group': clc.args.args.group },
		          cols=['RequestID','StatusCode','Message'])


	def GetServerDetails(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Server.GetServerDetails', { 'alias': alias, 'servers': clc.args.GetArgs().server },
		              cols=['HardwareGroupUUID', 'Name', 'Description', 'Cpu','MemoryGB','Status','TotalDiskSpaceGB','ServerType','OperatingSystem','PowerState','Location','IPAddress'])


	def GetServerCredentials(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Server.GetCredentials', { 'alias': alias, 'servers': clc.args.GetArgs().server },
		              cols=['Username', 'Password', ])


	def GetServerDisks(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Server.GetDisks', { 'alias': alias, 'server': clc.args.GetArgs().server },
		              cols=['Name', 'ScsiBusID', 'ScsiDeviceID', 'SizeGB' ])


	def AddServerDisk(self):
		if clc.args.args.server:  server = clc.args.args.server
		else: server = None
		if clc.args.args.size:  size = clc.args.args.size
		else: size = None
		if clc.args.args.path:  path = clc.args.args.path
		else: path = None
		if clc.args.args.type:  type = clc.args.args.type
		else: type = None
		clc.v2.Server(server).Disks().Add(size=size, path=path, type=type).WaitUntilComplete()


	def ServerActions(self,action):
		clc.args.args.async = True  # Force async - we can't current deal with multiple queued objects
		r = self.Exec('clc.v1.Server.%s' % (action), { 'alias': self._GetAlias(), 'servers': clc.args.GetArgs().server },
		              cols=['RequestID','StatusCode','Message'])


	def ConvertToTemplate(self):
		r = self.Exec('clc.v1.Server.ConvertToTemplate', 
		              { 'alias': self._GetAlias(), 'server': clc.args.GetArgs().server, 
					    'template': clc.args.GetArgs().template, 'password': clc.args.GetArgs().password },
		              cols=['RequestID','StatusCode','Message'])


	def GetServers(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		if clc.args.args.location:  location = clc.args.args.location
		else:  
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		r = self.Exec('clc.v1.Server.GetServers', { 'alias': alias, 'location': location, 'group': clc.args.args.group, 'name_groups': clc.args.args.name_groups },
		              cols=['HardwareGroupUUID', 'Name', 'Description', 'Cpu','MemoryGB','Status','ServerType','OperatingSystem','PowerState','Location','IPAddress'])


	def GetServerTemplates(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		if clc.args.args.location:  location = clc.args.args.location
		else:  location = None
		r = self.Exec('clc.v1.Server.GetTemplates', { 'alias': alias, 'location': location }, cols=['OperatingSystem', 'Name', 'Description', 'Cpu','MemoryGB','TotalDiskSpaceGB'])


	def GetAllServers(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Server.GetAllServers', { 'alias': alias, 'name_groups': clc.args.args.name_groups },
		              cols=['HardwareGroupUUID', 'Name', 'Description', 'Cpu','MemoryGB','Status','ServerType','OperatingSystem','PowerState','Location','IPAddress'])


	def CreateServer(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		r = self.Exec('clc.v1.Server.Create', 
		              { 'alias': alias, 'location': location, 'group': clc.args.args.group, 'name': clc.args.args.name, 'template': clc.args.args.template,
					    'backup_level': clc.args.args.backup_level, 'cpu': clc.args.args.cpu, 'ram': clc.args.args.ram, 
						'network': clc.args.args.network, 'password': clc.args.args.password, 'description': clc.args.args.description, },
		              cols=['RequestID','StatusCode','Message'])


	def RestoreServer(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		if clc.args.args.location:  location = clc.args.args.location
		else:  location = None
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		r = self.Exec('clc.v1.Server.RestoreServer', 
		              { 'alias': alias, 'location': location, 'group': clc.args.args.group, 'server': clc.args.GetArgs().server },
		              cols=['RequestID','StatusCode','Message'])


	#def RestoreGroup(self):
	#	alias = None
	#	location = None
	#	if clc.args.args.alias:  alias = clc.args.args.alias
	#	if clc.args.args.location:  location = clc.args.args.location
	#	if not alias:
	#		self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
	#		alias = clc.ALIAS
	#	if not location:
	#		self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
	#		location = clc.LOCATION
	#	self.Exec('clc.Group.Restore', 
	#	          { 'alias': alias, 'location': location, 'group': clc.args.args.group },
	#	          cols=['RequestID','StatusCode','Message'])


	def GetGroupEstimate(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		r = self.Exec('clc.v1.Billing.GetGroupEstimate', { 'alias': alias, 'location': location, 'group': clc.args.GetArgs().group }, 
					  cols=['MonthToDate', 'PreviousHour', 'MonthlyEstimate', 'CurrentHour'])


	def GetGroupSummaries(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Billing.GetGroupSummaries', { 'alias': alias, 'date_start': clc.args.GetArgs().date_start, 'date_end': clc.args.GetArgs().date_end },
		              cols=['GroupName', 'LocationAlias', 'MonthlyEstimate', 'MonthToDate',  'CurrentHour'])


	def GetServerEstimate(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Billing.GetServerEstimate', { 'alias': alias, 'server': clc.args.GetArgs().server },
		              cols=['MonthToDate', 'PreviousHour', 'MonthlyEstimate', 'CurrentHour'])


	def GetAccountSummary(self):
		if clc.args.args.alias:  alias = clc.args.args.alias
		else:  alias = None
		r = self.Exec('clc.v1.Billing.GetAccountSummary', { 'alias': alias }, cols=['OneTimeCharges','MonthToDate', 'MonthlyEstimate', 'CurrentHour', 'PreviousHour'])


	def GetNetworks(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		r = self.Exec('clc.v1.Network.GetNetworks', { 'alias': alias, 'location': location }, 
					  cols=['Name', 'Description', 'Gateway'])


	def GetNetworkDetails(self):
		alias = None
		location = None
		if clc.args.args.alias:  alias = clc.args.args.alias
		if clc.args.args.location:  location = clc.args.args.location
		if not alias:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			alias = clc.ALIAS
		if not location:
			self.Exec('clc.v1.Account.GetAlias','',supress_output=True)
			location = clc.LOCATION
		r = self.Exec('clc.v1.Network.GetNetworkDetails', { 'alias': alias, 'location': location, 'network': clc.args.args.network }, 
					  cols=['Address', 'AddressType', 'IsClaimed', 'ServerName'])


	def GetQueue(self):
		r = self.Exec('clc.v1.Queue.List', { 'type': clc.args.args.type }, cols=['RequestID', 'RequestTitle', 'ProgressDesc', 'CurrentStatus', 'StepNumber', 'PercentComplete'])


	def GetBlueprintsPending(self):
		r = self.Exec('clc.v1.Blueprint.GetPendingPackages', { }, cols=['Name'])


	def GetBlueprintsPackages(self):
		r = self.Exec('clc.v1.Blueprint.GetPackages', { 'classification': clc.args.args.type, 'visibility': clc.args.args.visibility }, 
		              cols=['ID','Name'])


	def GetBlueprintsSystemPackages(self):
		r = self.Exec('clc.v1.Blueprint.GetAllSystemPackages', { }, cols=['ID','Name','Visibility'])


	def GetBlueprintsScriptsPackages(self):
		r = self.Exec('clc.v1.Blueprint.GetAllScriptsPackages', { }, cols=['ID','Name','Visibility'])


	def GetBlueprintsSoftwarePackages(self):
		r = self.Exec('clc.v1.Blueprint.GetAllSoftwarePackages', { }, cols=['ID','Name','Visibility'])


	def GetBlueprintsPackageUpload(self):
		if clc.args.args.ftp:  ftp_url = clc.args.args.ftp
		elif clc._BLUEPRINT_FTP_URL:  ftp_url = clc._BLUEPRINT_FTP_URL
			
		try:
			r = self.Exec('clc.v1.Blueprint.PackageUpload', { 'package': clc.args.args.package, 'ftp_url': ftp_url },supress_output=True)
		except UnboundLocalError:
			clc.v1.output.Status('ERROR',2,'FTP URL not defined.  Use --ftp command line arg or set blueprint_ftp_url in ini file')


	def PublishBlueprintsPackage(self):
		clc.args.args.async = True
		if clc.args.args.os is None:
			r = self.Exec('clc.v1.Blueprint.PackagePublishUI', 
			              { 'package': clc.args.args.package, 'classification': clc.args.args.type, 'visibility': clc.args.args.visibility },
						  cols=['RequestID','StatusCode','Message'])
		else:
			r = self.Exec('clc.v1.Blueprint.PackagePublish', 
			              { 'package': clc.args.args.package, 'classification': clc.args.args.type, 'os': clc.args.args.os, 'visibility': clc.args.args.visibility },
						  cols=['RequestID','StatusCode','Message'])


	def Exec(self,function,args=False,cols=None,supress_output=False):
		try:
			if args:  r = eval("%s(**%s)" % (function,args))
			else:  r = eval("%s()" % (function))

			#  Filter results
			if clc.args.args.cols:  cols = clc.args.args.cols

			# Output results
			# TODO - how do we differentiate blueprints vs. queue RequestIDs?
			if r is not None and 'RequestID' in r and not clc.args.args.async:  
				r = clc.v1.output.RequestBlueprintProgress(r['RequestID'],self._GetLocation(),self._GetAlias(),clc.args.args.quiet)
				cols = ['Server']

			if not isinstance(r, list):  r = [r]
			if not supress_output and clc.args.args.format == 'json':  print clc.v1.output.Json(r,cols)
			elif not supress_output and clc.args.args.format == 'table':  print clc.v1.output.Table(r,cols)
			elif not supress_output and clc.args.args.format == 'text':  print clc.v1.output.Text(r,cols)
			elif not supress_output and clc.args.args.format == 'csv':  print clc.v1.output.Csv(r,cols)

			return(r)
		except clc.AccountDeletedException:
			clc.v1.output.Status('ERROR',2,'Unable to process, account in deleted state')
		except clc.AccountLoginException:
			clc.v1.output.Status('ERROR',2,'Transient login error.  Please retry')


