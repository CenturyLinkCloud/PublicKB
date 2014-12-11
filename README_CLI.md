# CenturyLink Cloud CLI and Python SDK

The CLI provides a command line interface to functions defined in the [SDK](README_PYTHON_SDK.md).

At present this aligns most closely to [V1](https://t3n.zendesk.com/categories/20012068-API-v1-0) of the [CenturyLink Cloud](http://www.centurylinkcloud.com) API though efforts are in process to merge [V2](https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-) API as it nears full release.

## Contents

* [Usage](#usage) - basic usage, authentication, and configuration files
* [Accounts](#accounts) - Account level activities (list, create, modify)
* [Users](#users) - User level activities (list, create, modify)
* [Servers](#servers) - Server level activities (list, create, modify)
* [Groups](#groups) - Group level activities (list, create, modify)
* [Billing](#billing) - Billing activities
* [Networks](#networks) - Network activities
* [Queue](#queue) - Work queue
* [Blueprints](#blueprints) - Blueprints
* [Global Options](#global-options) - Formatting and execution options


## Usage
If running the Windows pre-compiled executable [clc-cli.exe](https://github.com/CenturyLinkCloud/clc-python-sdk/raw/master/src/dist/clc-cli.exe) note that all examples below will need to be modified since the Windows command line executable is *clc-cli* (to eliminate conflict with the a standard installed PS commandlet.

```
> clc
usage: clc [-h] [--cols [COL [COL ...]]] [--config CONFIG]
              [--v1-api-key KEY] [--v1-api-passwd PASSWORD]
              [--v2-api-username USERNAME] [--v2-api-passwd PASSWORD]
              [--async] [--quiet] [--verbose] [--format {json,table,text,csv}]

              {blueprints,users,billing,servers,queue,accounts,groups,networks}
```

### Global Parameters and General Usage
```
> clc -h
usage: clc [-h] [--cols [COL [COL ...]]] [--config CONFIG]
              [--v1-api-key KEY] [--v1-api-passwd PASSWORD]
              [--v2-api-username USERNAME] [--v2-api-passwd PASSWORD]
              [--async] [--quiet] [--verbose] [--format {json,table,text,csv}]

              {blueprints,users,billing,servers,queue,accounts,groups,networks}
              ...

CLI tool for interacting with CenturyLink Cloud API.
http://www.CenturyLinkCloud.com

optional arguments:
  -h, --help            show this help message and exit
  --cols [COL [COL ...]]
                        Include only specific columns in the output
  --config CONFIG, -c CONFIG
                        Ini config file
  --v1-api-key KEY      V1 API key
  --v1-api-passwd PASSWORD
                        V1 API password
  --v2-api-username USERNAME
                        V2 API username
  --v2-api-passwd PASSWORD
                        V2 API password
  --async               Return immediately after queueing long-running calls
  --quiet, -q           Supress status output (repeat up to 2 times)
  --verbose, -v         Increase verbosity
  --format {json,table,text,csv}, -f {json,table,text,csv}
                        Output result format (table is default)

Commands:
  {blueprints,users,billing,servers,queue,accounts,groups,networks}
    accounts            Account level activities (list, create, modify)
    users               User level activities (list, create, modify)
    servers             Server level activities (list, create, modify)
    groups              Group level activities (list, create, modify)
    billing             Billing activities
    networks            Network activities
    queue               Work queue
    blueprints          Blueprints
```


### Authentication
All commands require authentication which can be accomplished in several ways in increasing order of priority.
* System configuration file at /usr/local/etc/clc_config (POSIX) or %PROGRAMDATA%\clc\clc.ini (Windows)
* User specific configuration file at ~/.clc (POSIX) or .\clc.ini (Windows)
* Specify configuration file with --config / -c command line option
* Define environment variables (V1_API_KEY / V1_API_PASSWD or V2_API_USERNAME / V2_API_PASSWD)
* Pass credentials as command line options

Configuration files follow ini syntax.  Reference the [example.ini](src/example_config.ini) file with all currently accepted fields.

### Accounts
Usage
```
> clc --config config.ini accounts
usage: clc accounts [-h] {list,locations,get} ...
```

#### Listing Accounts
Retrieves deep list of current account and all subaccounts your API credentials have access to.
```
> clc --config config.ini accounts list
✔  Logged into v1 API
✔  Accounts successfully queried.
+--------------+-------------+----------------------------------------+----------+----------+
| AccountAlias | ParentAlias | BusinessName                           | Location | IsActive |
+--------------+-------------+----------------------------------------+----------+----------+
| ABCO         | JWCO        | ABC Oil and Gas                        | IL1      | True     |
| AC01         | MDA         | Account #1                             | WA1      | True     |
| XYZO         | JWCO        | XYZ Oil & Gas                          | NY1      | True     |
| ZAB          | BTDI        | Zabriskie Point                        | IL1      | True     |
+--------------+-------------+----------------------------------------+----------+----------+
```

#### Locations
Retrieves a list of all cloud datacenter locations accessible by provided credentials.
```
> clc --config config.ini accounts locations
✔  Logged into v1 API
✔  Locations successfully queried.
+-------+------------+
| Alias | Region     |
+-------+------------+
| CA1   | Canada     |
| CA2   | Canada     |
| CA3   | Canada     |
| DE1   | Germany    |
| GB1   | Europe     |
| GB3   | Europe     |
| IL1   | US Central |
| NY1   | US East    |
| UC1   | US West    |
| UT1   | US Central |
| VA1   | US East    |
| WA1   | US West    |
+-------+------------+
```

#### Get
Retrieves  details from specific alias or credentials default alias if none is provided.
```
> clc --config config.ini accounts get
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Account details successfully queried.

  ******************* 1. ********************
         AccountAlias:  BTDI
               Status:  Demo
                 City:  Bellevue
                  Fax:  None
             Address1:  110 110th Ave NE
             Address2:  Ste 520
  ShareParentNetworks:  False
            Telephone:  8773884373
              Country:  USA
             Location:  WA1
         BusinessName:  CLC Solutions Demo
           PostalCode:  98004
             TimeZone:  Pacific Standard Time
        StateProvince:  WA
          ParentAlias:  T3N
```

### Users
Usage
```
> clc --config config.ini users
usage: clc users [-h] {unsuspend,suspend,get,create,list,update,delete} ...
```

#### List
List users associated with the alias

```
> clc --config config.ini users list
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Users successfully located.
+----------------------------+-----------------------------------------+-------------+----------------+--------------+
| UserName                   | EmailAddress                            | FirstName   | LastName       | Roles        |
+----------------------------+-----------------------------------------+-------------+----------------+--------------+
| Joe Smith                  | JoeSmith@example.com                    | Joe         | Smith          | [9]          |
| Kim Smith                  | KimSmith@example.com                    | Kim         | Smith          | [9]          |
+----------------------------+-----------------------------------------+-------------+----------------+--------------+
```

#### Create
Create new user account and return account details
```
> clc --config config.ini users create --user test12345 --email test@example.com --first-name Joe \
          --last-name Smith --roles ServerAdministrator BillingManager
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully created.

  ******************* 1. ********************
               UserName:  test12345
           MobileNumber:  None
               AllowSMS:  False
           SAMLUserName:  None
                 Status:  Active
                  Roles:   ['ServerAdministrator', 'BillingManager']
              FirstName:  Joe
                  Title:  None
               LastName:  Smith
           OfficeNumber:  None
              FaxNumber:  None
             TimeZoneID:  Pacific Standard Time
           AccountAlias:  BTDI
           EmailAddress:  test@example.com
  AlternateEmailAddress:  None
```

#### Update
Update existing account and return details
```
> clc --config config.ini users update --user test12345 --email test@example.com --first-name Jenny --last-name Smith --roles ServerAdministrator
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully updated.

  ******************* 1. ********************
               UserName:  test12345
           MobileNumber:  None
               AllowSMS:  False
           SAMLUserName:  None
                 Status:  Active
                  Roles:  ['ServerAdministrator']
              FirstName:  Jenny
                  Title:  None
               LastName:  Smith
           OfficeNumber:  None
              FaxNumber:  None
             TimeZoneID:  Pacific Standard Time
           AccountAlias:  BTDI
           EmailAddress:  test@example.com
  AlternateEmailAddress:  None
  ```

#### Get
Return account details
```
> clc --config config.ini users get --user test12345
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  User successfully located.

  ******************* 1. ********************
               UserName:  test12345
           MobileNumber:  None
               AllowSMS:  False
           SAMLUserName:  None
                 Status:  Active
                  Roles:  ['ServerAdministrator']
              FirstName:  Jenny
                  Title:  None
               LastName:  Smith
           OfficeNumber:  None
              FaxNumber:  None
             TimeZoneID:  Pacific Standard Time
           AccountAlias:  BTDI
           EmailAddress:  test@example.com
  AlternateEmailAddress:  None
```

#### Suspend
```
> clc --config config.ini users suspend --user test12345
✔  Logged into v1 API
✔  User suspended.
```

#### Unsuspend
```
> clc --config config.ini users unsuspend --user test12345
✔  Logged into v1 API
✔  User unsuspended.
```

#### Delete
```
> clc --config config.ini users delete --user test12345
✔  Logged into v1 API
✔  User deleted.
```

### Servers
Usage
```
> clc --config config.ini servers
usage: clc servers [-h] 
	{get,list,list-all,templates,create,delete,archive,pause,poweron,poweroff,reset,shutdown,snapshot,get-credentials,list-disks} ...
```

#### Templates
List all templates available from the specified location or if none specified the primary location associated with the provided API credentials.  These include system templates (available globally) and customer created templates (available in the location where they were created).
```
> clc --config config.ini servers templates
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Successfully retrieved templates
+-----------------+-----------------------------+---------------------------------------------+-----+----------+------------------+
| OperatingSystem | Name                        | Description                                 | Cpu | MemoryGB | TotalDiskSpaceGB |
+-----------------+-----------------------------+---------------------------------------------+-----+----------+------------------+
| 2               | WIN2K3R2STD-32              | Windows 2003 R2 Standard | 32-bit           | 0   | 0        | 16               |
| 3               | WIN2K3R2STD-64              | Windows 2003 R2 Standard | 64-bit           | 0   | 0        | 16               |
| 5               | WIN2008R2STD-64             | Windows 2008 R2 Standard | 64-bit           | 0   | 0        | 60               |
| 15              | WIN2K3R2ENT-32              | Windows 2003 R2 Enterprise | 32-bit         | 0   | 0        | 16               |
| 16              | WIN2K3R2ENT-64              | Windows 2003 R2 Enterprise | 64-bit         | 0   | 0        | 16               |
| 18              | WIN2008R2ENT-64             | Windows 2008 R2 Enterprise | 64-bit         | 0   | 0        | 60               |
| 20              | BOSH-STEMCELL               | BOSH Stemcell Template                      | 0   | 0        | 20               |
| 20              | MICRO-BOSH-STEMCELL         | Stemcell | Micro-BOSH                       | 0   | 0        | 20               |
| 25              | RHEL-5-64-TEMPLATE          | RedHat Enterprise Linux 5 | 64-bit          | 0   | 0        | 17               |
| 26              | WIN2008R2DTC-64             | Windows 2008 R2 Datacenter Edition | 64-bit | 0   | 0        | 60               |
| 27              | WIN2012DTC-64               | Windows 2012 Datacenter Edition | 64-bit    | 0   | 0        | 60               |
| 28              | WIN2012R2DTC-64             | Windows 2012 R2 Datacenter Edition | 64-bit | 0   | 0        | 60               |
| 29              | UBUNTU-10-32-TEMPLATE       | Ubuntu 10 | 32-bit                          | 0   | 0        | 17               |
| 30              | UBUNTU-10-64-TEMPLATE       | Ubuntu 10 | 64-bit                          | 0   | 0        | 17               |
| 30              | UBUNTU-10-64-WF-TEMPLATE    | Web Fabric Ubuntu x64 Template              | 0   | 0        | 17               |
| 30              | UBUNTU-10-64-WF-TEMPLATE-V2 | Web Fabric Ubuntu x64 Template V2           | 0   | 0        | 17               |
| 31              | UBUNTU-12-64-TEMPLATE       | Ubuntu 12 | 64-bit                          | 0   | 0        | 17               |
| 32              | CENTOS-5-32-TEMPLATE        | CentOS 5 | 32-bit                           | 0   | 0        | 17               |
| 33              | CENTOS-5-64-TEMPLATE        | CentOS 5 | 64-bit                           | 0   | 0        | 17               |
| 34              | CENTOS-6-32-TEMPLATE        | CentOS 6 | 32-bit                           | 0   | 0        | 17               |
| 35              | CENTOS-6-64-TEMPLATE        | CentOS 6 | 64-bit                           | 0   | 0        | 17               |
| 36              | DEBIAN-6-64-TEMPLATE        | Debian 6 | 64-bit                           | 0   | 0        | 17               |
| 37              | DEBIAN-7-64-TEMPLATE        | Debian 7 | 64-bit                           | 0   | 0        | 17               |
| 38              | RHEL-6-64-TEMPLATE          | RedHat Enterprise Linux 6 | 64-bit          | 0   | 0        | 17               |
| 40              | PXE-TEMPLATE                | PXE Boot [EXPERIMENTAL]                     | 0   | 0        | 0                |
| 41              | UBUNTU-14-64-TEMPLATE       | Ubuntu 14 | 64-bit                          | 0   | 0        | 17               |
+-----------------+-----------------------------+---------------------------------------------+-----+----------+------------------+
```

#### List
List all servers in the specified location or if none specified the primary location associated with the provided API credentials.
```
> clc --config config.ini servers list
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Successfully retrieved deep view of servers
+-----------------+-----------------+----------------------------------------+-----+----------+----------+------------+-----------------+------------+----------+--------------+
| HardwareGroupID | Name            | Description                            | Cpu | MemoryGB | Status   | ServerType | OperatingSystem | PowerState | Location | IPAddress    |
+-----------------+-----------------+----------------------------------------+-----+----------+----------+------------+-----------------+------------+----------+--------------+
| 1003            | WA1BTDIJLVB01   | John LAMP test platform                | 1   | 2        | Active   | 1          | 20              | Started    | WA1      | 10.80.146.15 |
| 1045            | WA1BTDITEST15   | test                                   | 1   | 1        | Active   | 1          | 5               | Started    | WA1      | 10.81.0.17   |
| 1798            | WA1BTDIWS005101 | demo server                            | 0   | 0        | Archived | 1          | 7               | None       | WA1      | 10.80.146.54 |
| 2487            | WA1BTDISUB01    | 1234                                   | 2   | 1        | Active   | 2          | 6               | Started    | WA1      | 10.80.146.36 |
| 2487            | WA1BTDITESTCH01 | WA1BTDITESTCH01                        | 1   | 2        | Active   | 1          | 5               | Stopped    | WA1      | 10.80.146.30 |
| 3728            | WA1BTDISAML0101 | My ADFS server                         | 1   | 4        | Active   | 1          | 5               | Stopped    | WA1      | 10.80.146.49 |
| 4416            | WA1BTDITEST11   | test                                   | 1   | 1        | Active   | 1          | 7               | Started    | WA1      | 10.80.146.14 |
| 20220           | WA1BTDISQL06    | SQL Server                             | 4   | 15       | Active   | 1          | 5               | Paused     | WA1      | 10.80.146.18 |
| 20220           | WA1BTDITSDEMO02 | Tyce Demo Server 2                     | 2   | 16       | Active   | 1          | 27              | Started    | WA1      | 10.80.148.13 |
+-----------------+-----------------+----------------------------------------+-----+----------+----------+------------+-----------------+------------+----------+--------------+
```

#### List All
Perform a deep list of all servers in all locations.
```
> clc --config config.ini servers list-all
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Locations successfully queried.
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
✔  Successfully retrieved deep view of servers
+-----------------+-----------------+----------------------------------------+-----+----------+-------------------+------------+-----------------+------------+----------+--------------+
| HardwareGroupID | Name            | Description                            | Cpu | MemoryGB | Status            | ServerType | OperatingSystem | PowerState | Location | IPAddress    |
+-----------------+-----------------+----------------------------------------+-----+----------+-------------------+------------+-----------------+------------+----------+--------------+
| 1003            | WA1BTDIJLVB01   | John  LAMP test platform               | 1   | 2        | Active            | 1          | 20              | Started    | WA1      | 10.80.146.15 |
| 1045            | WA1BTDITEST15   | test                                   | 1   | 1        | Active            | 1          | 5               | Started    | WA1      | 10.81.0.17   |
| 1798            | WA1BTDIWS005101 | demo server                            | 0   | 0        | Archived          | 1          | 7               | None       | WA1      | 10.80.146.54 |
| 2487            | WA1BTDISUB01    | 1234                                   | 2   | 1        | Active            | 2          | 6               | Started    | WA1      | 10.80.146.36 |
| 2487            | WA1BTDITESTCH01 | WA1BTDITESTCH01                        | 1   | 2        | Active            | 1          | 5               | Stopped    | WA1      | 10.80.146.30 |
| 3728            | WA1BTDISAML0101 | My ADFS server                         | 1   | 4        | Active            | 1          | 5               | Stopped    | WA1      | 10.80.146.49 |
| 3732            | IL1BTDITEST05   | first                                  | 0   | 0        | Archived          | 1          | 27              | None       | IL1      | 10.90.61.12  |
| 3732            | IL1BTDITEST201  | first                                  | 0   | 0        | Archived          | 1          | 27              | None       | IL1      | 10.90.61.15  |
| 4416            | WA1BTDITEST11   | test                                   | 1   | 1        | Active            | 1          | 7               | Started    | WA1      | 10.80.146.14 |
| 5132            | CA2BTDIKLEBAN01 | Chris  Demo Server                     | 1   | 1        | Active            | 1          | 35              | Stopped    | CA2      | 10.55.60.14  |
| 6559            | CA1BTDIMDA01    | Test for MDA                           | 0   | 0        | Active            | 1          | 28              | None       | CA1      |              |
| 6559            | CA1BTDIMGDOS01  | Derek                                  | 2   | 4        | Active            | 1          | 38              | Started    | CA1      | 10.50.84.12  |
| 6879            | DE1BTDITEST02   | apache test                            | 1   | 1        | UnderConstruction | 1          | 38              | Started    | DE1      | 10.110.81.13 |
| 6884            | DE1BTDI2K1201   | windows 2012                           | 2   | 4        | Active            | 1          | 27              | Started    | DE1      | 10.110.81.12 |
| 9261            | NY1BTDIPHYP0101 | Hyperscale server                      | 2   | 4        | Active            | 1          | 27              | Started    | NY1      | 10.70.171.13 |
| 11703           | UC1BTDISERO2201 | Hyperscale Windows Server              | 2   | 4        | Active            | 1          | 28              | Started    | UC1      | 10.122.16.13 |
| 11894           | VA1BTDIJMB02    | JMB Windows 2012                       | 2   | 16       | Active            | 1          | 28              | Stopped    | VA1      | 10.125.39.22 |
| 11894           | VA1BTDISVMT101  | Test Server                            | 2   | 4        | Active            | 1          | 38              | Stopped    | VA1      | 10.125.39.15 |
| 11894           | VA1BTDISVMT201  | Test Server 2                          | 2   | 16       | Active            | 1          | 27              | Stopped    | VA1      | 10.125.39.19 |
| 11894           | VA1BTDITSDEMO01 | tsdemo                                 | 0   | 0        | Active            | 1          | 38              | None       | VA1      |              |
| 17569           | CA3BTDIAPI01    |  API VM                                | 2   | 8        | Active            | 1          | 38              | Started    | CA3      | 10.100.75.12 |
| 17569           | CA3BTDIKLEBAN01 | hadoop test                            | 1   | 2        | Active            | 1          | 30              | Stopped    | CA3      | 10.100.42.12 |
| 20093           | VA1BTDIJMB01    | Redhat 6                               | 2   | 4        | Active            | 1          | 38              | Started    | VA1      | 10.125.39.13 |
| 20220           | WA1BTDISQL06    | SQL Server                             | 4   | 15       | Active            | 1          | 5               | Paused     | WA1      | 10.80.146.18 |
| 20220           | WA1BTDITSDEMO02 | Tyce Demo Server 2                     | 2   | 16       | Active            | 1          | 27              | Started    | WA1      | 10.80.148.13 |
| 22279           | NY1BTDIWEB0101  | web app server                         | 2   | 4        | Active            | 1          | 28              | Started    | NY1      | 10.70.171.12 |
| 22279           | NY1BTDIWEB0201  | Windows web server                     | 2   | 4        | Active            | 1          | 28              | Stopped    | NY1      | 10.70.171.14 |
| 25730           | GB3BTDIJRDEMO01 | r @gmail.com                           | 11  | 99       | Active            | 1          | 38              | Stopped    | GB3      | 10.105.33.12 |
| 27513           | IL1BTDIDC03     |                                        | 1   | 2        | Active            | 1          | 5               | Started    | IL1      | 10.90.61.13  |
| 29770           | NY1BTDISERDEV01 | development environment                | 2   | 4        | Active            | 1          | 28              | Started    | NY1      | 10.70.239.12 |
| 29770           | NY1BTDISERDEV02 | dev server                             | 2   | 4        | Active            | 1          | 28              | Started    | NY1      | 10.70.239.13 |
| 31544           | IL1BTDIDC04     | Domain Controller                      | 1   | 2        | Active            | 1          | 5               | Started    | IL1      | 10.90.61.16  |
| 32360           | IL1BTDIWEB104   |                                        | 1   | 2        | Active            | 1          | 28              | Started    | IL1      | 10.90.61.14  |
| 33537           | IL1BTDIWEB105   |                                        | 1   | 2        | Active            | 1          | 28              | Stopped    | IL1      | 10.90.61.17  |
+-----------------+-----------------+----------------------------------------+-----+----------+-------------------+------------+-----------------+------------+----------+--------------+
```

#### Get
Retrieve details on one or more servers.  Example below queries for two servers.
```
> clc --config config.ini servers get --server IL1BTDIWEB10{4,5}
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Successfully retrieved server
✔  Successfully retrieved server
+-----------------+---------------+-------------+-----+----------+--------+------------------+------------+-----------------+------------+----------+-------------+
| HardwareGroupID | Name          | Description | Cpu | MemoryGB | Status | TotalDiskSpaceGB | ServerType | OperatingSystem | PowerState | Location | IPAddress   |
+-----------------+---------------+-------------+-----+----------+--------+------------------+------------+-----------------+------------+----------+-------------+
| 32360           | IL1BTDIWEB104 |             | 1   | 2        | Active | 60               | 1          | 28              | Started    | IL1      | 10.90.61.14 |
| 33537           | IL1BTDIWEB105 |             | 1   | 2        | Active | 60               | 1          | 28              | Stopped    | IL1      | 10.90.61.17 |
+-----------------+---------------+-------------+-----+----------+--------+------------------+------------+-----------------+------------+----------+-------------+
```

#### Get Credentials
Retrieve administrative credentials for specified server(s).  Easily specify alternate output formats or limit to just the password column using the global formatting options.
```
> clc --config config.ini servers get-credentials --server IL1BTDIWEB104
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Server credentials retrieved
+---------------+------------------+
| Username      | Password         |
+---------------+------------------+
| administrator | dsalkjsd9rw9pROq |
+---------------+------------------+
```

#### Create
Create new server. Depending on command line options the command can return immediately or can display build status in real-time.  When build completes returns server name.
```
> clc --config config.ini servers create --name CLITST --group 'Default Group' --description 'CLI Test' --template RHEL-6-64-TEMPLATE --backup-level Standard --cpu 1 --ram 1 --network vlan_946_10.80.146
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  Groups successfully listed.
✔  Server queued for creation
✔  Submitted for processing
✔  Execution Started - 0:00:27
[################                ] 50/100 - 00:00:43
```
Output once server build completes
```
...
✔  Execution Started - 0:00:27
✔  Execution Complete - 0:01:45
✔  Execution Complete - 0:02:12
+-----------------+
| Server          |
+-----------------+
| WA1BTDICLITST01 |
+-----------------+
```

#### List Disks
List all disks associated with the servere also querying the guest for disk names and mount points.
```
> clc --config config.ini servers list-disks --server WA1BTDICLITST01
✔  Logged into v1 API
✔  Accounts successfully queried.
✔  OK
+--------+-----------+--------------+--------+
| Name   | ScsiBusID | ScsiDeviceID | SizeGB |
+--------+-----------+--------------+--------+
| (swap) | 0         | 1            | 2      |
| /      | 0         | 2            | 14     |
| /boot  | 0         | 0            | 1      |
+--------+-----------+--------------+--------+
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
Usaage
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

