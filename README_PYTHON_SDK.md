# CenturyLink Cloud CLI and Python SDK

This repository contains a Python SDK and a command line CLI (based on the SDK) to interact with the ***CenturyLink Cloud*** API.  At present this aligns most closely to [V1](https://t3n.zendesk.com/categories/20012068-API-v1-0) of the CenturyLink Cloud API though efforts are in process to merge [V2](https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-) API as it nears full release.

## Contents

* [Accounts](#accounts) - Account level activities: [list](#listing-accounts), 
* [Users](#users) - User level activities (list, create, modify)
* [Servers](#servers) - Server level activities (list, create, modify)
* [Groups](#groups) - Group level activities (list, create, modify)
* [Billing](#billing) - Billing activities
* [Networks](#networks) - Network activities
* [Queue](#queue) - Work queue
* [Blueprints](#blueprints) - Blueprints
* [Global Options](#global-options) - Formatting and execution options



### Authentication
All API calls require authentication.  Depending on the API calls being made you will need to login using either V1, V2, or both V1/V2 credentials.
Most most calls currently leverage V1 credentials.  Where the same capability exists with either V1 or V2 API and only one set of credentials
is provided the SDK will automatically select the appropriate version of the API to call.

```python
>>> import clc
>>> clc.v1.SetCredentialsV1("api_key","api_password")

>>> clc.v2.SetCredentialsV2("test@example.com","control_portal_password")
```


### Accounts

[Account pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.account.html)

#### Default Alias and Location
Each API token is associated with a specific account alias and each alias has a primary datacenter location.
Get the default alias and location with these calls.  These calls are often made within the SDK itself in
functions where alias and location are optional.

```python
>>> clc.Account.GetAlias()
u'BTDI'
>>> clc.Account.GetLocation()
u'WA1'
```

#### Get Accounts
Retrieves deep list of current account and all subaccounts your API credentials have access to.
The first result is the root account within the list followed by all other accounts.  Account relationship
can nbe determined by reviewing the ParentAlias field associated with each result set.

```python
>>> clc.Account.GetAccounts(alias="BTDI")
[{u'AccountAlias': u'BTDI',
  u'BusinessName': u'CLC Solutions Demo',
  u'IsActive': True,
  u'Location': u'WA1',
  u'ParentAlias': u'T3N'},
 {u'AccountAlias': u'QATI',
  u'BusinessName': u'QATier3',
  u'IsActive': True,
  u'Location': u'WA1',
  u'ParentAlias': u'BTDI'},
 {u'AccountAlias': u'T3DE',
  u'BusinessName': u'DE1 Test Account',
  u'IsActive': True,
  u'Location': u'DE1',
  u'ParentAlias': u'BTDI'}]
```

#### Locations
Retrieves a list of all cloud datacenter locations accessible by provided credentials.
```python
>>> clc.Account.GetLocations()
[{u'Alias': u'WA1', u'Region': u'US West'},
 {u'Alias': u'UT1', u'Region': u'US Central'},
 {u'Alias': u'IL1', u'Region': u'US Central'},
 {u'Alias': u'NY1', u'Region': u'US East'},
 {u'Alias': u'GB1', u'Region': u'Europe'},
 {u'Alias': u'CA1', u'Region': u'Canada'},
 {u'Alias': u'CA2', u'Region': u'Canada'},
 {u'Alias': u'DE1', u'Region': u'Germany'},
 {u'Alias': u'UC1', u'Region': u'US West'},
 {u'Alias': u'VA1', u'Region': u'US East'},
 {u'Alias': u'CA3', u'Region': u'Canada'},
 {u'Alias': u'GB3', u'Region': u'Europe'}]
```

#### Get Account Details
Retrieves  details from specific alias or credentials default alias if none is provided.

```python
>>> clc.Account.GetAccountDetails(alias="BTDI")
{u'AccountAlias': u'BTDI',
 u'Address1': u'110 110th Ave NE',
 u'Address2': u'Ste 520',
 u'BusinessName': u'CLC Solutions Demo',
 u'City': u'Bellevue',
 u'Country': u'USA',
 u'Fax': None,
 u'Location': u'WA1',
 u'ParentAlias': u'T3N',
 u'PostalCode': u'98004',
 u'ShareParentNetworks': False,
 u'StateProvince': u'WA',
 u'Status': 'Demo',
 u'Telephone': u'8773884373',
 u'TimeZone': u'Pacific Standard Time'}
```

### Users

[User pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.user.html)

#### List Users
List all users associated with the specified alias.

```python
>>> pprint.pprint(clc.User.GetUsers(alias="BTDI"))
[{u'AccountAlias': u'BTDI',
  u'AllowSMS': True,
  u'AlternateEmailAddress': None,
  u'EmailAddress': u'JoeSmith@example.com',
  u'FaxNumber': None,
  u'FirstName': u'Joe',
  u'LastName': u'Smith',
  u'MobileNumber': u'202-555-5555',
  u'OfficeNumber': None,
  u'Roles': [9],
  u'SAMLUserName': None,
  u'Status': u'Active',
  u'TimeZoneID': None,
  u'Title': u'Sr Product Manager',
  u'UserName': u'joesmith'},
 {u'AccountAlias': u'BTDI',
  u'AllowSMS': True,
  u'AlternateEmailAddress': None,
  u'EmailAddress': u'KimSmith@example.com',
  u'FaxNumber': None,
  u'FirstName': u'Kim',
  u'LastName': u'Smith',
  u'MobileNumber': u'202-555-5555',
  u'OfficeNumber': None,
  u'Roles': [9],
  u'SAMLUserName': None,
  u'Status': u'Active',
  u'TimeZoneID': None,
  u'Title': u'Developer Manager',
  u'UserName': u'Kimsmith'},]
```

#### Create User
Create new user account and return account details.  Alias is optional.

```python
>>> clc.User.CreateUser(user="test12665",email="JoeSmith@example.com",first_name="Joe",last_name="Smith",roles=["ServerAdministrator",],alias="BTDI")
{u'AccountAlias': u'BTDI',
 u'AllowSMS': False,
 u'AlternateEmailAddress': None,
 u'EmailAddress': u'JoeSmith@example.com',
 u'FaxNumber': None,
 u'FirstName': u'Joe',
 u'LastName': u'Smith',
 u'MobileNumber': None,
 u'OfficeNumber': None,
 u'Roles': ['ServerAdministrator'],
 u'SAMLUserName': None,
 u'Status': u'Active',
 u'TimeZoneID': u'Pacific Standard Time',
 u'Title': None,
 u'UserName': u'test12665'}
```

#### Update Existing User
Update existing account and return details

```python
>>> clc.User.UpdateUser(user="test12665",email="JennySmith@example.com",first_name="Jenny",last_name="Smith",roles=["ServerAdministrator",],alias="BTDI")
{u'AccountAlias': u'BTDI',
 u'AllowSMS': False,
 u'AlternateEmailAddress': None,
 u'EmailAddress': u'JennySmith@example.com',
 u'FaxNumber': None,
 u'FirstName': u'Jenny',
 u'LastName': u'Smith',
 u'MobileNumber': None,
 u'OfficeNumber': None,
 u'Roles': ['ServerAdministrator'],
 u'SAMLUserName': None,
 u'Status': u'Active',
 u'TimeZoneID': u'Pacific Standard Time',
 u'Title': None,
 u'UserName': u'test12665'}
```

#### Get
Return user details

```python
>>> clc.User.GetUserDetails("joesmith")
{u'AccountAlias': u'BTDI',
 u'AllowSMS': False,
 u'AlternateEmailAddress': None,
 u'EmailAddress': u'JoeSmith@example.com',
 u'FaxNumber': None,
 u'FirstName': u'Joe',
 u'LastName': u'Smith',
 u'MobileNumber': None,
 u'OfficeNumber': None,
 u'Roles': ['AccountAdministrator'],
 u'SAMLUserName': None,
 u'Status': u'Active',
 u'TimeZoneID': u'Pacific Standard Time',
 u'Title': None,
 u'UserName': u'joesmith'}
```

#### Suspend, Unsuspend, Delete Users
Account status modifications return no results.

```python
>>> pprint.pprint(clc.User.SuspendUser("test12665"))
None
>>> pprint.pprint(clc.User.UnsuspendUser("test12665"))
None
>>> pprint.pprint(clc.User.DeleteUser("test12665"))
None
```

### Servers

[Server pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.server.html)

#### Templates
List all templates available from the specified location or if Nnone specified the primary location associated with the provided API credentials.  These include system templates (available globally) and customer created templates (available in the location where they were created).

```python
>>> clc.Server.GetTemplates(alias=None,location=None)
[{u'Cpu': 0,
  u'Description': u'CentOS 5 | 32-bit',
  u'DiskCount': 3,
  u'ID': 0,
  u'Location': u'WA1',
  u'MemoryGB': 0,
  u'Name': u'CENTOS-5-32-TEMPLATE',
  u'OperatingSystem': 32,
  u'TotalDiskSpaceGB': 17},
  u'Description': u'Windows 2012 R2 Datacenter Edition | 64-bit',
  u'DiskCount': 1,
  u'ID': 0,
  u'Location': u'WA1',
  u'MemoryGB': 0,
  u'Name': u'WIN2012R2DTC-64',
  u'OperatingSystem': 28,
  u'TotalDiskSpaceGB': 60}]
```

#### Get Template ID
Each template has a unique Int ID.  Given a name get this ID.

```python
>>> clc.Server.GetTemplateID(alias=None, location=None, name='WIN2012DTC-64')
27
```

#### List
List all servers in the specified location.

```python
>>> clc.Server.GetServers(location='WA1',group=None,alias=None)
[{u'Cpu': 2,
  u'CustomFields': [],
  u'DateModified': u'/Date(1418190460000)/',
  u'Description': u'App server',
  u'DiskCount': 1,
  u'DnsName': u'wa1btdisub01',
  u'HardwareGroupID': 2487,
  u'ID': -1,
  u'IPAddress': u'10.80.146.36',
  u'IPAddresses': [{u'Address': u'10.80.136.13', u'AddressType': u'RIP'},
                   {u'Address': u'10.80.136.36', u'AddressType': u'RIP'},
                   {u'Address': u'64.93.174.20', u'AddressType': u'MIP'}],
  u'InMaintenanceMode': False,
  u'IsHyperscale': False,
  u'IsTemplate': False,
  u'Location': u'WA1',
  u'MemoryGB': 1,
  u'ModifiedBy': u'JoeSmith@example.com',
  u'Name': u'WA1BTDISUB01',
  u'OperatingSystem': 6,
  u'PowerState': u'Started',
  u'ServerType': 2,
  u'ServiceLevel': 2,
  u'Status': u'Active',
  u'TotalDiskSpaceGB': 16},
 {u'Cpu': 1,
  u'CustomFields': [{u'CustomFieldID': -1,
                     u'ID': u'88e35072c1e14d479e09fa4f60a401f0',
                     u'Name': u'Cost Center',
                     u'Type': u'Text',
                     u'Value': u'IT-DEV'},
                    {u'CustomFieldID': -1,
                     u'ID': u'ed02166d55bc4ee4857b7ce248962dca',
                     u'Name': u'CMDB ID',
                     u'Type': u'Text',
                     u'Value': u'1100003'}],
  u'DateModified': u'/Date(1410821481000)/',
  u'Description': u'Web server',
  u'DiskCount': 1,
  u'DnsName': None,
  u'HardwareGroupID': 3728,
  u'ID': -1,
  u'IPAddress': u'10.80.146.49',
  u'IPAddresses': [{u'Address': u'72.42.151.159', u'AddressType': u'MIP'},
                   {u'Address': u'10.80.136.49', u'AddressType': u'RIP'},
                   {u'Address': u'10.80.136.50', u'AddressType': u'RIP'}],
  u'InMaintenanceMode': False,
  u'IsHyperscale': False,
  u'IsTemplate': False,
  u'Location': u'WA1',
  u'MemoryGB': 4,
  u'ModifiedBy': u'JoeSmith@example.com',
  u'Name': u'WA1BTDISAML0101',
  u'OperatingSystem': 5,
  u'PowerState': u'Stopped',
  u'ServerType': 1,
  u'ServiceLevel': 2,
  u'Status': u'Active',
  u'TotalDiskSpaceGB': 50}]
```

#### List All
Perform a deep list of all servers in all locations.

```python
>>> clc.Server.GetAllServers(alias=None)
.
. (same output as above)
.
```

#### Get
Retrieve details on one or more servers.

```python
>>> clc.Server.GetServerDetails(alias=None, servers=['UC1BTDISERO2201',])
[{u'Cpu': 2,
  u'CustomFields': [],
  u'DateModified': u'/Date(1413312404000)/',
  u'Description': u'Hyperscale Windows Server',
  u'DiskCount': 1,
  u'DnsName': u'uc1btdisero2201',
  u'HardwareGroupID': 11703,
  u'ID': -1,
  u'IPAddress': u'10.121.16.13',
  u'IPAddresses': [{u'Address': u'10.121.16.13', u'AddressType': u'RIP'}],
  u'InMaintenanceMode': False,
  u'IsHyperscale': True,
  u'IsTemplate': False,
  u'Location': u'UC1',
  u'MemoryGB': 4,
  u'ModifiedBy': u'JoeSmith@example.com',
  u'Name': u'UC1BTDISERO2201',
  u'OperatingSystem': 28,
  u'PowerState': u'Started',
  u'ServerType': 1,
  u'ServiceLevel': 2,
  u'Status': u'Active',
  u'TotalDiskSpaceGB': 60}]
```

#### Get Credentials
Retrieve administrative credentials for specified server(s). 

```python
>>> pprint.pprint(clc.Server.GetCredentials(servers=['WA1BTDITSTSER01',],alias=None))
[{u'Message': u'Server credentials retrieved',
  u'Password': u'#A$zids90djvRhH)',
  u'StatusCode': 0,
  u'Success': True,
  u'Username': u'administrator'}]
```

#### Create
Create new server. This is an asynchronous activity so a RequestID is returned which can be used to follow progress.

```python
>>> clc.Server.Create(alias=None,location='WA1',name='TSTSER',template='CENTOS-5-32-TEMPLATE',cpu=1,ram=1,backup_level='Standard',
                      group='Default Group', network='vlan_948_10.80.148',description='Test server',password='')
{u'Message': u'Server queued for creation',
 u'RequestID': 123586,
 u'StatusCode': 0,
 u'Success': True}
```

#### List Disks
List all disks associated with the servere also querying the guest for disk names and mount points.

```python
>>> clc.Server.GetDisks(server='UC1BTDISERO2201',alias=None,guest_names=True)
[{u'Name': u'C:\\', u'ScsiBusID': u'0', u'ScsiDeviceID': u'0', u'SizeGB': 60}]
```

#### Misc Asynchronous server operations
These asynchronous operations can be run on one more more servers.  Currently implemented are:
*pause, delete, archive, poweron, poweroff, reset, shutdown, snapshot*.  Rather than waiting for process to 
complete execute asynchronously and return a job ID.

```python
>>> clc.Server.Snapshot(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for snapshot',
  u'RequestID': 123587,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Poweroff(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for power off',
  u'RequestID': 123588,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Poweron(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Group queued for power on',
  u'RequestID': 123589,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Reset(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for reset',
  u'RequestID': 123590,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Reboot(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for reboot',
  u'RequestID': 123591,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Shutdown(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for shutdown',
  u'RequestID': 123592,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Pause(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for pause',
  u'RequestID': 123593,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Archive(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for archive',
  u'RequestID': 123595,
  u'StatusCode': 0,
  u'Success': True}]

>>> clc.Server.Delete(servers=['WA1BTDITSTSER01',],alias=None)
[{u'Message': u'Server queued for deletion',
  u'RequestID': 123594,
  u'StatusCode': 0,
  u'Success': True}]
```

### Groups

[Groups pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.group.html)

#### Get Group ID
Lookup unique Int group ID given name.

```python
>>> clc.Group.GetGroupID(group="Default Group",alias=None,location=None)
5132
```

#### List
List all groups in the specified datacenter or if None specified the primary location associated with the provided API credentials.
```
>>> clc.Group.GetGroups(alias=None,location='WA1')
[{u'ID': 837,
  u'IsSystemGroup': True,
  u'Name': u'WA1 Hardware',
  u'ParentID': 557},
 {u'ID': 1798, u'IsSystemGroup': True, u'Name': u'Archive', u'ParentID': 837},
 {u'ID': 4416,
  u'IsSystemGroup': False,
  u'Name': u'Default Group',
  u'ParentID': 837},
 {u'ID': 33853,
  u'IsSystemGroup': False,
  u'Name': u'Test dev',
  u'ParentID': 4416},
 {u'ID': 1045,
  u'IsSystemGroup': False,
  u'Name': u'Development',
  u'ParentID': 837}]
```

#### Create
Create new group rooted under the specified parent group or if None is specified will be a top-level group in the specified location.  

```python
>>> clc.Group.Create(group="Test Group",parent="WA1 Hardware",description='sdk test',alias=None,location='WA1')
{u'ID': 34051,
 u'IsSystemGroup': False,
 u'Name': u'Test Group',
 u'ParentID': 837}
```

#### Misc Asynchronous group operations
These asynchronous operations can be run on the specified group.  Currently implemented are:
*pause, delete, archive, poweron*.  Rather than waiting for process to complete executes asynchronously 
and returns a job ID.

```python
>>> clc.Group.Pause(group="Test Group",alias=None,location='WA1')
{u'Message': u'Group queued for pause',
 u'RequestID': 123909,
 u'StatusCode': 0,
 u'Success': True}
>>> clc.Group.Poweron(group="Test Group",alias=None,location='WA1')
{u'Message': u'Group queued for power on',
 u'RequestID': 123910,
 u'StatusCode': 0,
 u'Success': True}
>>> clc.Group.Archive(group="Test Group",alias=None,location='WA1')
{u'Message': u'Group queued for archive',
 u'RequestID': 123911,
 u'StatusCode': 0,
 u'Success': True}
>>> clc.Group.Delete(group="Test Group",alias=None,location='WA1')
{u'Message': u'Group successfully queued for deletion.',
 u'RequestID': 123912,
 u'StatusCode': 0,
 u'Success': True}
```


### Billing

[Billing pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.billing.html)

#### Account Summary
Return current billing summary for account.

```python
>>> clc.Billing.GetAccountSummary(alias='BTDI')
{u'CurrentHour': 4.4367719,
 u'Message': u'OK',
 u'MonthToDate': 2592.1229057,
 u'MonthToDateTotal': 2592.1229057,
 u'MonthlyEstimate': 4211.5525992,
 u'OneTimeCharges': 0,
 u'PreviousHour': 4.4367719,
 u'StatusCode': 0,
 u'Success': True}
```

#### Group Summaries
Return group-level billing summaries. Optionally specifiy a start and end date (YYYY-MM-DD) to filter the summation term.
If None specified returns summary beginning with first day of current month ending on the current date.

```python
>>> clc.Billing.GetGroupSummaries(alias='BTDI',date_start='2014-01-01',date_end=None)
[{u'CurrentHour': 0.1038,
  u'GroupID': 4416,
  u'GroupName': u'Default Group',
  u'LocationAlias': u'WA1',
  u'MonthToDate': 941.47,
  u'MonthlyEstimate': 941.47,
  u'ServerTotals': [{u'CurrentHour': 0.0,
                     u'MonthToDate': 302.15,
                     u'MonthlyEstimate': 302.15,
                     u'ServerName': u'WA1BTDITEST11'}]},
 {u'CurrentHour': 0.401,
  u'GroupID': 1003,
  u'GroupName': u'Production',
  u'LocationAlias': u'VA1',
  u'MonthToDate': 3147.62,
  u'MonthlyEstimate': 3147.62,
  u'ServerTotals': [{u'CurrentHour': 0.0,
                     u'MonthToDate': 866.0,
                     u'MonthlyEstimate': 866.0,
                     u'ServerName': u'VA1BTDIAPITST58'}]}]
```

#### Group Estimate
Group-level estimate of current run rate for specified group.

```python
>>> clc.Billing.GetGroupEstimate(group='Default Group',alias='BTDI',location='WA1')
{u'CurrentHour': 0.00357,
 u'Message': u'OK',
 u'MonthToDate': 6.58,
 u'MonthlyEstimate': 7.88,
 u'PreviousHour': 0,
 u'StatusCode': 0,
 u'Success': True}
```

#### Server Estimate
Server-level estimate of current run rate for specified server.

```python
>>> clc.Billing.GetServerEstimate(server='IL1BTDIWEB104',alias='BTDI')
{u'CurrentHour': 0.0926,
 u'Message': u'OK',
 u'MonthToDate': 35.1,
 u'MonthlyEstimate': 68.89,
 u'PreviousHour': 0,
 u'StatusCode': 0,
 u'Success': True}
```


### Networks

[Network pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.network.html)

#### List

List networks associated with the specified location or if None is specified will be a top-level group in the specified location.
```python
>>> clc.Network.GetNetworks(alias='BTDI')
[{u'AccountAlias': u'BTDI',
  u'Description': u'Web server network (946_10.80.144)',
  u'Gateway': u'10.80.144.1',
  u'Location': u'WA1',
  u'Name': u'vlan_946_10.80.144'},
 {u'AccountAlias': u'BTDI',
  u'Description': u'vlan_948_10.80.146',
  u'Gateway': u'10.80.146.1',
  u'Location': u'WA1',
  u'Name': u'vlan_948_10.80.146'}]
```

#### Get
Retrieve IP allocation summary for specied network.

```python
>>> pprint.pprint(clc.Network.GetNetworkDetails(alias='BTDI',network='vlan_948_10.80.148'))
[{u'Address': u'66.150.174.123',
  u'AddressType': u'MIP',
  u'IsClaimed': True,
  u'ServerName': u'WA1BTDITSDEMO02'},
 {u'Address': u'10.80.146.12',
  u'AddressType': u'RIP',
  u'IsClaimed': True,
  u'ServerName': u'WA1BTDIUBUNTU02'},
 .
 .
 .
 {u'Address': u'10.80.146.228',
  u'AddressType': u'RIP',
  u'IsClaimed': False,
  u'ServerName': None},
 {u'Address': u'10.80.146.229',
  u'AddressType': u'RIP',
  u'IsClaimed': False,
  u'ServerName': None}]
```

### Queue

#### List
List items in the work queue.  Specify a type to filter the list (All, Pending, Complete, or Error)

```python
>>> clc.Queue.List(type='Error')
[{u'CurrentStatus': u'Failed',
  u'PercentComplete': 50,
  u'ProgressDesc': u'Unexpected error while processing the request.',
  u'RequestID': 37847,
  u'RequestTitle': u"Delete cross data center firewall policy '290' between 10.80.146.0/24 and 10.91.124.0/24.",
  u'StatusDate': u'/Date(1417239472590)/',
  u'StepNumber': 1},
 {u'CurrentStatus': u'Failed',
  u'PercentComplete': 0,
  u'ProgressDesc': u'ERROR: Power On Server',
  u'RequestID': 20327,
  u'RequestTitle': u'Power On Server: WA1BTDIDJB101',
  u'StatusDate': u'/Date(1326494970980)/',
  u'StepNumber': 1}]

>>> clc.Queue.List(type='Pending')
[{u'CurrentStatus': u'Executing',
  u'PercentComplete': 45,
  u'ProgressDesc': u'Run Sysprep',
  u'RequestID': 15567,
  u'RequestTitle': u'WA1BTDIDB03 (via Blueprint)',
  u'StatusDate': u'/Date(1314169350723)/',
  u'StepNumber': 10}]
```

### Blueprints

[Blueprint pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.blueprint.html)

#### List Status of Currently Executing Blueprint
Given a request ID get real-time status on blueprint deployment.  Throughout the deployment cycle data within the response will
very as more is known (e.g. server names are unavailable until assigned shortly after execution begins).

```python
>>> clc.Blueprint.GetStatus(request_id=124091,location='WA1',alias='BTDI',silent=False)
{u'CurrentStatus': u'NotStarted',
 u'Description': u'Submitted for processing',
 u'Message': u'Success',
 u'PercentComplete': 0,
 u'RequestID': 124091,
 u'Servers': [],
 u'StatusCode': 0,
 u'StatusDate': u'/Date(1418757403520)/',
 u'Step': u'0',
 u'Success': True}

>>> clc.Blueprint.GetStatus(request_id=124091,location='WA1',alias='BTDI',silent=False)
{u'CurrentStatus': u'Executing',
 u'Description': u'Execution Started',
 u'Message': u'Success',
 u'PercentComplete': 33,
 u'RequestID': 124091,
 u'Servers': [u'WA1BTDIKEITH01'],
 u'StatusCode': 0,
 u'StatusDate': u'/Date(1418757422287)/',
 u'Step': u'1',
 u'Success': True}

>>> clc.Blueprint.GetStatus(request_id=124091,location='WA1',alias='BTDI',silent=False)
{u'CurrentStatus': u'Failed',
 u'Description': u'Error Building Blueprint',
 u'Message': u'Success',
 u'PercentComplete': 77,
 u'RequestID': 124091,
 u'Servers': [u'WA1BTDIKEITH01'],
 u'StatusCode': 0,
 u'StatusDate': u'/Date(1418757923657)/',
 u'Step': u'0',
 u'Success': True}
```

#### List System, Software, and Script Packages
List all packages in inventory, optionally filtering by package classification (System, Script, Software) and visibility (Public, Private, Shared).

```python
>>> clc.Blueprint.GetAllSystemPackages()
[{u'Classification': 1,
  u'ID': 2,
  u'Name': u'Add Disk',
  'Visibility': 'Public'},
 {u'Classification': 1,
  u'ID': 5,
  u'Name': u'Snapshot Server',
  'Visibility': 'Public'}]

>>> clc.Blueprint.GetAllScriptsPackages()

>>> clc.Blueprint.GetAllSoftwarePackages()
```

#### Package Upload
Upload properly formatted package zip file using the ftp credentials provided in the command line or the configuration file.

```python
>>> clc.Blueprint.PackageUpload('uploadtest.zip','ftp://user:passwd@ftpserver'))
{}
```

#### Listing Pending Packages
List all packages which have been uploaded but not yet submitted for publishing.

```python
>>> clc.Blueprint.GetPendingPackages()
[{u'Classification': 0, u'ID': 0, u'Name': u'param2.zip'},
 {u'Classification': 0, u'ID': 0, u'Name': u'uploadtest.zip'}]
```

#### Package Publish
Publish the specified package.  Specify clasification (Script, Software), visibility (Public, Private, Shared) and optionally one or more supported operating systems.  If no operating systems listed will allow selection of prefered OS.

```python
>>> clc.Blueprint.PackagePublish(package='uploadtest.zip',classification='Script',visibility='Private',os=[30,])
{u'Message': u'Success',
 u'RequestID': 124094,
 u'StatusCode': 0,
 u'Success': True}
```

