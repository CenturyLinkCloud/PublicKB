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
>>> clc.SetCredentialsV1("api_key","api_password")

>>> clc.SetCredentialsV2("test@example.com","control_portal_password")
```


### Accounts

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
```
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
Retrieve administrative credentials for specified server(s).  Easily specify alternate output formats or limit to just the password column using the global formatting options.

```python
```

#### Create
Create new server. Depending on command line options the command can return immediately or can display build status in real-time.  When build completes returns server name.

```python
```

#### List Disks
List all disks associated with the servere also querying the guest for disk names and mount points.

```python
```

#### Misc Asynchronous server operations
These asynchronous operations can be run on one more more servers.  Currently implemented are:
*pause, delete, archive, poweron, poweroff, reset, shutdown, snapshot*.  Rather than waiting for process to 
complete execute asynchronously and return a job ID.
```
> clc --async --config config.ini servers delete --server WA1BTDICLITST01
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Server queued for deletion
+-----------+------------+----------------------------+
| RequestID | StatusCode | Message                    |
+-----------+------------+----------------------------+
| 122265    | 0          | Server queued for deletion |
+-----------+------------+----------------------------+
```

### Groups
Usage
```
> clc --config config.ini groups
usage: clc groups [-h] {pause,create,list,poweron,archive,delete} ...
```

#### List
List all groups in the specified datacenter or if none specified the primary location associated with the provided API credentials.
```
> clc --config config.ini groups list --location WA1
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
+-------+---------------------------+----------+---------------+
| ID    | Name                      | ParentID | IsSystemGroup |
+-------+---------------------------+----------+---------------+
| 837   | WA1 Hardware              | 557      | True          |
| 1003  | Production                | 837      | False         |
| 1045  | Development               | 837      | False         |
| 1798  | Archive                   | 837      | True          |
| 1799  | Templates                 | 837      | True          |
| 2486  | Intranet Applications     | 837      | False         |
| 2487  | Web Services              | 1003     | False         |
| 3111  | AW Review                 | 2486     | False         |
| 3728  | RLS Group                 | 2486     | False         |
| 4416  | Default Group             | 837      | False         |
| 5476  | Corporate IT              | 3728     | False         |
| 5477  | Marketing                 | 5476     | False         |
| 5478  | Operations                | 5476     | False         |
| 5479  | Public Websites           | 5476     | False         |
| 5480  | R&D                       | 5476     | False         |
| 5481  | Shared Infrastructure     | 5476     | False         |
| 5482  | Sales                     | 5476     | False         |
| 5483  | Extranet                  | 5476     | False         |
| 5484  | Collaboration             | 5483     | False         |
+-------+---------------------------+----------+---------------+
```

#### Create
Create new group rooted under the specified parent group or if none is specified will be a top-level group in the specified location.  Like all longer-running calls this can be executed asynchronously (as in example below) which returns immediately with a job ID or it can be executed in real time.
```
> clc --config config.ini groups create --location WA1 --group 'CLI Test' --description 'CLI Test Group'
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  Group successfully created.
+-------+----------+----------+
| ID    | Name     | ParentID |
+-------+----------+----------+
| 33725 | CLI Test | 837      |
+-------+----------+----------+
```

#### Pause
Pause all servers in the specified group and its sub-groups.
```
> clc --async --config config.ini groups pause --location WA1 --group 'CLI Test'
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  Group queued for pause
+-----------+------------+------------------------+
| RequestID | StatusCode | Message                |
+-----------+------------+------------------------+
| 122271    | 0          | Group queued for pause |
+-----------+------------+------------------------+
```

#### Poweron
Power on all servers in the specified group and its sub-groups.
```
> clc --async --config config.ini groups poweron --location WA1 --group 'CLI Test'
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  Group queued for power on
+-----------+------------+---------------------------+
| RequestID | StatusCode | Message                   |
+-----------+------------+---------------------------+
| 122270    | 0          | Group queued for power on |
+-----------+------------+---------------------------+
```

#### Archive
Archive all servers in specified group and sub-groups.
```
> clc --async --config config.ini groups archive --location WA1 --group 'CLI Test'
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  Group queued for archive
+-----------+------------+--------------------------+
| RequestID | StatusCode | Message                  |
+-----------+------------+--------------------------+
| 122272    | 0          | Group queued for archive |
+-----------+------------+--------------------------+
```

#### Delete
Delete the specified group and all associated servers.
```
> clc --async --config config.ini groups delete --location WA1 --group 'CLI Test'
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  Group successfully queued for deletion.
+-----------+------------+-----------------------------------------+
| RequestID | StatusCode | Message                                 |
+-----------+------------+-----------------------------------------+
| 122273    | 0          | Group successfully queued for deletion. |
+-----------+------------+-----------------------------------------+
```

### Billing
Usage
```
> clc --async --config config.ini billing
usage: clc billing [-h] {account-summary,group-estimate,server-estimate,group-summaries}  ...
```

#### Account Summary
Return current billing summary for account.
```
clc --async --config config.ini billing account-summary
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  OK
+----------------+--------------+-----------------+-------------+--------------+
| OneTimeCharges | MonthToDate  | MonthlyEstimate | CurrentHour | PreviousHour |
+----------------+--------------+-----------------+-------------+--------------+
| 0              | 1207.2062446 | 4483.5507101    | 5.0020501   | 5.0020501    |
+----------------+--------------+-----------------+-------------+--------------+
```

#### Group Summaries
Return group-level billing summaries. Optionally specifiy a start and end date to filter the summation term.
```
> clc --async --config config.ini billing group-summaries  --date-start 2014-01-01
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Ok
+-------------------------+---------------+-----------------+-------------+-------------+
| GroupName               | LocationAlias | MonthlyEstimate | MonthToDate | CurrentHour |
+-------------------------+---------------+-----------------+-------------+-------------+
| Corporate IT            | WA1           | 0.09            | 0.09        | 0.0         |
| DAF Groups              | WA1           | 45.56           | 45.56       | 0.12263     |
| Default Group           | CA1           | 160.93          | 160.93      | 0.63197     |
| Default Group           | GB1           | 1119.64         | 1119.64     | 0.0         |
| Default Group           | UC1           | 4.33            | 4.33        | 0.0         |
| Default Group           | UT1           | 186.97          | 186.97      | 0.0         |
| Default Group           | VA1           | 17.5            | 17.5        | 0.0         |
| Default Group           | WA1           | 941.47          | 941.47      | 0.17279     |
| Demo                    | CA1           | 881.05          | 881.05      | 0.99856     |
| Demo                    | CA2           | 1675.73         | 1675.73     | 0.5484      |
| Development             | WA1           | 402.84          | 402.84      | 0.05672     |
| Exchange                | CA2           | 77.88           | 77.88       | 0.0         |
| HYPERSCALE              | NY1           | 1.47            | 1.47        | 0.0         |
| Highly Available System | CA1           | 88.14           | 88.14       | 0.0         |
| Highly Available System | CA2           | 25.72           | 25.72       | 0.0         |
| VM Perf Test            | NY1           | 320.55          | 320.55      | 0.0         |
| Web Applications        | WA1           | 340.46          | 340.46      | 0.1768      |
| Web Services            | WA1           | 408.04          | 408.04      | 0.0         |
| tr-test                 | CA2           | 2.21            | 2.21        | 0.04336     |
+-------------------------+---------------+-----------------+-------------+-------------+
```

#### Group Estimate
Group-level estimate of current run rate for specified group.
```
> clc --async --config config.ini billing group-estimate --group 'Default Group'
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  OK
+-------------+--------------+-----------------+-------------+
| MonthToDate | PreviousHour | MonthlyEstimate | CurrentHour |
+-------------+--------------+-----------------+-------------+
| 2.54        | 0            | 21.26           | 0.02857     |
+-------------+--------------+-----------------+-------------+
```

#### Server Estimate
Server-level estimate of current run rate for specified server.
```
> clc --config config.ini billing server-estimate --server IL1BTDIWEB104
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  OK
+-------------+--------------+-----------------+-------------+
| MonthToDate | PreviousHour | MonthlyEstimate | CurrentHour |
+-------------+--------------+-----------------+-------------+
| 8.33        | 0            | 68.89           | 0.0926      |
+-------------+--------------+-----------------+-------------+
```

### Networks
Usage:
```
> clc --config config.ini networks
usage: clc networks [-h] {list,get} ...
```

#### List
List networks associated with the specified location or if none is specified will be a top-level group in the specified location.
```
> clc --config config.ini networks list --location WA1
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Networks successfully queried.
+--------------------+------------------------------------+-------------+
| Name               | Description                        | Gateway     |
+--------------------+------------------------------------+-------------+
| vlan_946_10.80.146 | Web server network (946_10.80.146) | 10.80.146.1 |
| vlan_948_10.80.148 | vlan_948_10.80.148                 | 10.80.148.1 |
+--------------------+------------------------------------+-------------+
```

#### Get
Retrieve IP allocation summary for specied network.
```
> clc --config config.ini networks get --location WA1 --network vlan_946_10.80.146
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Network details successfully queried.
+----------------+-------------+-----------+-----------------+
| Address        | AddressType | IsClaimed | ServerName      |
+----------------+-------------+-----------+-----------------+
| 10.80.146.100  | RIP         | False     | None            |
| 10.80.146.101  | RIP         | False     | None            |
| 10.80.146.102  | RIP         | False     | None            |
| 10.80.146.103  | RIP         | False     | None            |
...
| 64.94.114.20   | MIP         | True      | WA1BTDISUB01    |
| 66.150.160.42  | MIP         | True      | WA1BTDIJLVB01   |
| 66.150.174.154 | MIP         | True      | WA1BTDIJLVB01   |
| 66.150.174.237 | VIP         | True      | None            |
| 66.150.174.35  | VIP         | True      | None            |
| 70.42.161.159  | MIP         | True      | WA1BTDISAML0101 |
| 70.42.161.165  | MIP         | True      | WA1BTDIJLVB01   |
+----------------+-------------+-----------+-----------------+
```

### Queue
Usage:
```
> clc --config config.ini queue
usage: clc queue [-h] {list} ...
```

#### List
List items in the work queue.  Specify a type to filter the list.
```
> clc --config config.ini queue list --type Pending
✔  Logged into v1 API
✔  1 Queue requests were found for your account
+-----------+-----------------------------+--------------+---------------+------------+-----------------+
| RequestID | RequestTitle                | ProgressDesc | CurrentStatus | StepNumber | PercentComplete |
+-----------+-----------------------------+--------------+---------------+------------+-----------------+
| 15567     | WA1BTDIDB03 (via Blueprint) | Run Sysprep  | Executing     | 10         | 45              |
+-----------+-----------------------------+--------------+---------------+------------+-----------------+
```

### Blueprints
Usage:
```
> clc --config config.ini blueprints
usage: clc blueprints [-h] {list-system,list-software,list,package-upload,package-publish,list-pending,list-scripts} ...
```


#### List System, Software, and Script Packages
List all packages in inventory, optionally filtering by package classification (System, Script, Software) and visibility (Public, Private, Shared).
```
> clc --config config.ini blueprints list-system
✔  Logged into v1 API
✔  Success
✔  Success
✔  Success
+-------+-----------------------+------------+
| ID    | Name                  | Visibility |
+-------+-----------------------+------------+
| 2     | Add Disk              | Public     |
| 3     | Add IP Address        | Public     |
| 4     | Add Public IP Address | Public     |
| 5     | Snapshot Server       | Public     |
| 6     | Reboot Server         | Public     |
| 10210 | Revert Snapshot       | Public     |
| 10211 | Delete Snapshot       | Public     |
| 10468 | Add Raw Disk          | Public     |
+-------+-----------------------+------------+
```
#### Package Upload
Upload properly formatted package zip file using the ftp credentials provided in the command line or the configuration file.
```
> clc --config config.ini blueprints package-upload --package /home/resark/t/uploadtest.zip \
           --ftp 'ftp://username:password@FTP-CA1.tier3.com'
✔  Blueprint package uploadtest.zip Uploaded
```

#### Listing Pending Packages
List all packages which have been uploaded but not yet submitted for publishing.
```
> clc --config config.ini blueprints list-pending
✔  Logged into v1 API
✔  Success
+-----------------+
| Name            |
+-----------------+
| uploadtest.zip  |
+-----------------+
```

#### Package Publish
Publish the specified package.  Specify clasification (Script, Software), visibility (Public, Private, Shared) and optionally one or more supported operating systems.  If no operating systems listed will allow selection of prefered OS.
```
>  clc --config config.ini blueprints package-publish --type Script --visibility Private --package uploadtest.zip
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Successfully retrieved templates
✔  Selected operating system IDs: 25 38
✔  Success
+-----------+------------+---------+
| RequestID | StatusCode | Message |
+-----------+------------+---------+
| 14097     | 0          | Success |
+-----------+------------+---------+
```

### Global Options

#### --async
All long running operations return a work ID from the API rather than an immediate result.  Using the --async option ends CLI execution once the request has been successfully submitted and returns this work ID.  Default behavior is synchronous where the CLI will wait for the submitted job to complete and display any applicable results before terminating.  Where supported this is animated with a progress bar.

#### --format {json,table,text,csv}
The fault output format uses hunan readable tables.  If the number of columns is too wide for the console screen this moves to a one key per for format as demonstrated below.
```
> clc --config config.ini users get --user test345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.

  ******************* 1. ********************
               UserName:  test345
           MobileNumber:  None
               AllowSMS:  False
           SAMLUserName:  None
                 Status:  Active
                  Roles:  []
              FirstName:  dave
                  Title:  None
               LastName:  b
           OfficeNumber:  None
              FaxNumber:  None
             TimeZoneID:  Pacific Standard Time
           AccountAlias:  BTDI
           EmailAddress:  test@example.com
  AlternateEmailAddress:  None
  
> clc --cols UserName AccountAlias --config config.ini users get --user test345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.
+----------+--------------+
| UserName | AccountAlias |
+----------+--------------+
| test345  | BTDI         |
+----------+--------------+
```

JSON, plain text, and CSV options are also available.
```
> clc --cols UserName AccountAlias --format json --config config.ini users get --user test345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.
['UserName', 'AccountAlias']
[{u'UserName': u'test345', u'AccountAlias': u'BTDI'}]

> clc --cols UserName AccountAlias --format text --config config.ini users get --user test345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.
test345	BTDI

> clc --cols UserName AccountAlias --format csv --config config.ini users get --user test345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.
UserName,AccountAlias
test345,BTDI
111
```

#### -cols [COL [COL ...]] - Include only specific columns in the output
By default almost all columns reoturned by the API are included in the response.  Use this option to filter the columns that are displayed.
```
> clc --cols UserName AccountAlias --config config.ini users get --user test345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.
+----------+--------------+
| UserName | AccountAlias |
+----------+--------------+
| test345  | BTDI         |
+----------+--------------+
```

