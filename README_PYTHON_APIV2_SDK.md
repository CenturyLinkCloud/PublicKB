# CenturyLink Cloud APIV2 Python SDK

This repository contains a Python SDK to interact with the ***CenturyLink Cloud*** API.  The SDK documented at this page aligns to the to API [V2](https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-).  The API does not yet have full coverage of all cloud functions.  As the API matures this SDK
will follow suit.

## Contents

* [Quick Start](#quick-start)
* [Authentication](#authentication)
* [Account](#account) - Account level activities
* [Datacenter](#datacenter) - View and interact with geographic specific datacenter components
* [Groups](#groups) and [Group](#group) - `Groups` and `Group` classes.  Logical organization around assets by group which can contain sub-groups or servers
* [Servers](#servers) and [Server](#server) - `Servers` and `Server` classes.  Cloud servers
* [Requests](#requests) and [Request](#request) - `Requests` and `Request` classes.  Interface to work queue for async operations


## Quick Start

First some basic stuff:

```python

# Set credentials.  These are the same credentials used to login to the web UI (https://control.tier3.com)
clc.v2.SetCredentials("username","password")

# Get Account Detail
account = clc.v2.Account()
print "%s\n%s\n%s\n%s, %s %s" % (account.business_name,
                                 account.address_line1,
                                 account.address_line2,
                                 account.city,
                                 account.state_province,
                                 account.postal_code)

# Get detail on default datacenter
datacenter = account.PrimaryDatacenter()  # also available directly as clc.v2.Datacenter()

# Get group by name
default_group = datacenter.Groups().Get("Default Group")

# Create new server and block until complete
clc.v2.Server.Create(name="api2",cpu=1,memory=1,
                     group_id=default_group.id,
                     template=datacenter.Templates().Search("centos-6-64")[0].id,
                     network_id=datacenter.Networks().networks[0].id).WaitUntilComplete()

```

Now let us do some more advanced work covering a software development lifecycle.  
Our testing team has reports of problems in the VA1 production site:

```python

# Get VA1 datacenter and all servers in the VA1 group
va1 = clc.v2.Datacenter("VA1")
va1_prod_servers = va1.Groups().Get("Production").Servers()

# Create a test group and clone production so we can QA bug 1234
va1_qa_group = va1.RootGroup().Create("QA-1234")
for server in va1_prod_servers.servers:
    server.Clone(group_id=va1_qa_group.id,network_id=va1.Networks().networks[0].id)


# Take snapshot of prod before deploying code
va1_prod_servers.CreateSnapshot().WaitUntilComplete()

# Deploy updated application via Blueprint package
va1_prod_servers.ExecutePackage(package_id="77ab3844-579d-4c8d-8955-c69a94a2ba1a",parameters={}). \
              WaitUntilComplete()

# Cleanup test environment
va1_qa_group.Delete().WaitUntilComplete()


```

No need to block on queued actions before supplying additional requests.  Build out one of every
template in our catalog and wait for completion.

```python

# Create group to hold all new servers
catalog_group = va1.RootGroup().Create("Build Entire Catalog")

# Build each server, keeping track of its build ID
# Set a 2 hour TTL so these servers do not hang around
requests = []
for template in va1.Templates().templates:
    requests.append(clc.v2.Server.Create(name="CAT",cpu=2,memory=4,ttl=7200,
                                         group_id=catalog_group.id,
                                         template=template.id,
                                         network_id=va1.Networks().networks[0].id))

# Wait for all parallel builds to complete
sum(requests).WaitUntilComplete()

```

## Authentication

### clc.v2.SetCredentials
```python
clc.v2.SetCredentials( username, password )
```

All API calls require authentication using your API V2 credentials. 
Login itself is made lazily when the first API call requiring credentials is issued.

```python
>>> import clc
>>> clc.v2.SetCredentials("username","password")
```



## Account

[Account pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.account.html)

### Class variables

* account.account_alias (synonym for account.alias)
* account.address_line1
* account.address_line2
* account.business_name
* account.city
* account.state_province
* account.postal_code
* account.telephone
* account.country
* account.status
* account.primary_data_center
* account.is_managed

### clc.v2.Account.GetAlias (static)
```python
clc.v2.Account.GetAlias()
```

Return specified alias or if None the alias associated with the provided credentials.


```python
>>> clc.v2.Account.GetAlias()
u'BTDI'
```


### clc.v2.Account.GetLocation (static)
```python
clc.v2.Account.GetLocation()
```

Return specified location or if None the default location associated with the provided credentials and alias.

```python
>>> clc.v2.Account.GetLocation()
u'WA1'
```


### clc.v2.Account
```python
clc.v2.Account.GetAccount( alias=None )
```

Create `Account` object associated with provided alias (or default alias if none provided).

```python
>>> clc.v2.Account()
<clc.APIv2.account.Account instance at 0x1065a2e60>
```


### clc.v2.ParentAccount
```python
clc.v2.Account.ParentAccount()
```

Return `Account` object associated with the parent of the current account.
Returns None if already at top-level account.

```python
>>> clc.v2.Account()
<clc.APIv2.account.Account instance at 0x1065a2e60>
```

### clc.v2.PrimaryDatacenter
```python
clc.v2.Account.PrimaryDatacenter()
```

Returns `Datacenter` object associated with the primary datacetner.

```python
>>> clc.v2.Account(alias='BTDI').PrimaryDatacenter()
<clc.APIv2.datacenter.Datacenter instance at 0x10a45ce18>
>>> print _
WA1
```



## Datacenter

[Datacenter pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.datacenter.html)

### Class variables

* datacenter.id (alias for location)
* datacenter.name
* datacenter.location
* datacenter.supports_premium_storage
* datacenter.supports_shared_load_balancer


### clc.v2.Datacenter.Datacenters
```python
clc.v2.Datacenter.Datacenters ( alias=None)
```

Return all cloud locations available to the calling alias.

```python
>>> clc.v2.Datacenter.Datacenters(alias=None)
[<clc.APIv2.datacenter.Datacenter instance at 0x101462fc8>, <clc.APIv2.datacenter.Datacenter instance at 0x101464320>]
```

### clc.v2.Datacenter
```python
clc.v2.Datacenter( location=None, name=None, alias=None)
```

Create new `Datacenter` object associated with supplied location and alias.  If neither are provided
use the default values associated with the supplied credentials.

```python
>>> clc.v2.Datacenter()
<clc.APIv2.datacenter.Datacenter instance at 0x1065a2fc8>
>>> print _
WA1
```


### clc.v2.Datacenter.RootGroup
```python
clc.v2.RootGroup()
```

Returns `Group` object for datacenter root group.

```python
>>> clc.v2.Datacenter().RootGroup()
<clc.APIv2.group.Group object at 0x105feacd0>
>>> print _
WA1 Hardware
```


### clc.v2.Datacenter.Groups
```python
clc.v2.Groups()
```

Returns `Groups` object for datacenter root group.

```python
>>> clc.v2.Datacenter().Groups()
<clc.APIv2.group.Groups object at 0x1065abc50>
```


### clc.v2.Datacenter.Networks
```python
clc.v2.Networks()
```

Returns a `Networks` object associated with the datacenter.

```python
>>> clc.v2.Datacenter().Networks()
<clc.APIv2.network.Networks object at 0x105fea7d0>
```


### clc.v2.Datacenter.Templates
```python
clc.v2.Templates()
```

Returns a `Templates` object associated with the datacenter.

```python
>>> clc.v2.Datacenter().Templates()
<clc.APIv2.template.Templates object at 0x1065abc90>
```



## Groups

[Groups pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.group.html)


### clc.v2.Groups
```python
clc.v2.Groups( groups_lst, alias=None )
```

`Groups` object constructor.  If no alias is provided will use the default associated with the API
credentials in use.  `groups_lst` is a list of group objects retrieved from API.  Usually no need to call this constructor directly.


### clc.v2.Groups.Get
```python
clc.v2.Groups.Get( key )
```

Returns a `Group` object matching the provided key.  Match is against name, ID, or description.
If key is not unique and finds multiple matches only the first will be returned

```python
>>> clc.v2.Datacenter().Groups().Get("Default Group")
<clc.APIv2.group.Group object at 0x1065e5250>
```


### clc.v2.Groups.Search
```python
clc.v2.Groups.Search( key )
```

Returns a list of `Group` objects with partial matches to the provided key.  Match is against name, ID, or description.

```python
>>> clc.v2.Datacenter().Groups().Get("Default Group")
<clc.APIv2.group.Group object at 0x1065e5250>
```



## Group

[Group pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.group.html)

### Class variables

Object variables:

* group.id
* group.name
* group.description
* group.type
* group.status
* group.server_count
* group.created_by
* group.created_date
* group.modified_by
* group.modified_date
* group.dirty - bool indicating whether server object is different than cloud object

Object variables available but access subject to change with future releases:

* group.custom_fields


### clc.v2.Group.GetAll (static)
```python
clc.v2.Group.GetAll( root_group_id, alias=None )
```

Given a group ID and optional alias returns a list of `Group` objects associated with that group.

*Subject to deprecation in future release.*

```python
>>> clc.v2.Group.GetAll("wa1-4416")
[<clc.APIv2.group.Group object at 0x1065b0190>, <clc.APIv2.group.Group object at 0x1065b0dd0>]
```


### clc.v2.Group
```python
clc.v2.Group( id, alias=None, group_obj=None )
```

Create a new `Group` object.  If alias is not provided will use default value associated with the account.
If `group_obj` is not provided will perform and API query to get group definition.  `group_obj` is a list of
group definitions from the API and is not generally used by user functions.

```python
>> clc.v2.Group(id="wa1-1798")
<clc.APIv2.group.Group object at 0x109188b90>
```


### clc.v2.Group.Create
```python
clc.v2.Group( name, description=None )
```

Creates a new group and returns a `Group` object.

```python
>>> clc.v2.Datacenter(location="WA1").RootGroup().Create("Test3","Description3")
<clc.APIv2.group.Group object at 0x10cc76c90>
>>> print _
Test5
```


### clc.v2.Group.Refresh
```python
clc.v2.Group.Refresh()
```

Reloads the group object to synchronize with cloud representation.

```python
>>> clc.v2.Group("wa-123").Refresh()
```


### clc.v2.Group.Delete
```python
clc.v2.Group.Delete()
```

Deletes group.  Returns a `Requests` object.

```python
>>> clc.v2.Group("wa1-4416").Create(name="Test6")
<clc.APIv2.group.Group object at 0x1041937d0>
>>> clc.v2.Group(_.id).Delete().WaitUntilComplete()
0
```


### Operations: clc.v2.Group.Pause, ShutDown, Reboot, Reset, PowerOn, PowerOff, Archive, StartMaintenance, StopMaintenance
```python
clc.v2.Group.Pause()
```

All above operations methods behave in the same manner.  They apply the operation command to all
servers in the object.  All are asynchronous methods so they return a `Requests` object.

```python
>>> clc.v2.Group("wa-123").Pause()
<clc.APIv2.queue.Requests object at 0x105fea7d0>
>>> _.WaitUntilComplete()
0
```


### clc.v2.Group.Defaults
```python
clc.v2.Group.Defaults( key )
```

Returns default configurations for resources deployed to this group.

If specified key is not defined returns None.


### clc.v2.Group.Subgroups
```python
clc.v2.Group.Subgroups()
```

Returns a `Groups` object containing all child groups.

```python
>>> clc.v2.Group("wa1-4416").Subgroups()
<clc.APIv2.group.Groups object at 0x105fa27d0>
```


### clc.v2.Group.Servers
```python
clc.v2.Group.Servers()
```

Returns a `Servers` object containing all servers within the group.

```python
>>> clc.v2.Group("wa1-4416").Servers()
<clc.APIv2.server.Servers object at 0x1065b0f10>
```


### clc.v2.Group.Account
```python
clc.v2.Group.Account()
```

Returns the `Account` object that owns this group.

```python
>>> clc.v2.Group(alias="BTDI",id="wa1-837").Account()
<clc.APIv2.account.Account instance at 0x108789878>
>>> print _
BTDI
```



## Servers

[Servers pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.server.html)


### clc.v2.Servers
```python
clc.v2.Servers( servers_lst, alias=None )
```

`Servers` object constructor.  If no alias is provided will use the default associated with the API
credentials in use.  `servers_lst` is a list of server names. 

Note this behaves differently than the other container classes like Groups where the *_lst
parameter can fully define the object.  All we have is the server name on construction.
We will lazily create server objects as needed since each requires a seperate API call.

```python
>>> clc.v2.Servers(["NY1BTDIPHYP0101","NY1BTDIWEB0101"])
<clc.APIv2.server.Servers object at 0x105fa27d0>
```


### clc.v2.Servers.Servers
```python
clc.v2.Servers( cached=True )
```

Returns a list of `Server` objects.  If cached is set to True then the servers
list will not be refreshed if it has already been called in this instance.  

Note that building this list may be time intensive as each server currently requires a seperate
API call.

```python
>>> clc.v2.Servers(["NY1BTDIPHYP0101","NY1BTDIWEB0101"]).Servers()
[<clc.APIv2.server.Server object at 0x1065b0d50>, <clc.APIv2.server.Server object at 0x1065b0e50>]
>>> print _[0]
NY1BTDIPHYP0101
```


### Operations: clc.v2.Servers.Pause, ShutDown, Reboot, Reset, PowerOn, PowerOff, Archive, StartMaintenance, StopMaintenance
```python
clc.v2.Servers.Pause()
```

All above operations methods behave in the same manner.  They apply the operation command to all
servers in the object.  All are asynchronous methods so they return a `Requests` object.

```python
>>> clc.v2.Servers(["NY1BTDIPHYP0101","NY1BTDIWEB0101"]).Pause()
<clc.APIv2.queue.Requests object at 0x105fea7d0>
>>> _.WaitUntilComplete()
0
```



## Server

[Server pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.server.html)


### Class variables

Object variables:

* server.id
* server.description
* server.cpu
* server.power_state
* server.memory
* server.storage
* server.group_id
* server.is_template
* server.location_id
* server.name
* server.os
* server.os_type
* server.status
* server.type
* server.storage_type
* server.in_maintenance_mode
* server.reserved_drive_paths
* server.adding_cpu_requires_reboot
* server.adding_memory_requires_reboot
* server.created_by
* server.created_date
* server.modified_by
* server.modified_date
* server.dirty - whether changes have been made to the cloud server but not reflected in server object

Object variables available but access subject to change with future releases:

* server.custom_fields
* server.alert_policies
* server.ip_addresses


### clc.v2.Server.Create (Static)
```python
clc.v2.Server.Create(name, template, group_id, network_id, cpu=None, memory=None, alias=None,
                     password=None, ip_address=None, storage_type="standard", type="standard",
					 primary_dns=None, secondary_dns=None, additional_disks=[], custom_fields=[],
					 ttl=None, managed_os=False, description=None, source_server_password=None,
					 cpu_autoscale_policy_id=None, anti_affinity_policy_id=None, packages=[])
```

Creates a new server.  See also class method to clone server.

`cpu` and `memory` are optional and if not provided we pull from the default server size values associated with
the provided `group_id`.

Set ttl as number of seconds before server is to be terminated.  Must be >3600

```python
>>> d = clc.v2.Datacenter()
>>> clc.v2.Server.Create(name="api2",cpu=1,memory=1,group_id="wa1-4416",
                         template=d.Templates().Search("centos-6-64")[0].id,
                         network_id=d.Networks().networks[0].id).WaitUntilComplete()
0
```


### clc.v2.Server
```python
clc.v2.Server( id, alias=None, server_obj=None )
```

Create new `Server` object.  If `alias` is None then the alias associated with supplied credentials
is used.  `server_obj` is an API object containing server definitions - is is not typically called by
end user code.

***Note the `server_obj` parameter may be deprecated in future versions***

```python
# successful creation
>>> clc.v2.Server("CA3BTDICNTRLM01")
<clc.APIv2.server.Server object at 0x10c28fe50>
>>> print _
CA3BTDICNTRLM01

# error.  API returns 404 when server does not exist, we raise exception
>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT01')
clc.CLCException: Server does not exist
```


### clc.v2.Server.Credentials
```python
clc.v2.Server.Credentials()
```

Returns the administrative credentials for this server.

```python
>>> clc.v2.Server("NY1BTDIPHYP0101").Credentials()
{u'userName': u'administrator', u'password': u'dszkjh498s^'}
```


### clc.v2.Server.Change
```python
Change( cpu=None, memory=None, description=None, group_id=None ):
```
Change existing server object.

One more more fields can be set and method will return with a requests
object for all queued activities.  This is a convenience function - all
each of these changes requires a seperate API call.  Some API calls are synchronous
(e.g. changing group ID or password) while others are async.

```python
>>> clc.v2.Server("WA1BTDICHANGE01").Change(cpu=1,memory=3,description="new description",group_id="new-id").WaitUntilComplete()
```


### clc.v2.Server.SetCPU, SetMemory, SetDescription, SetGroup
```python
clc.v2.Server.SetCPU( value )
```

Change one attribute about a server.

```python
>>> clc.v2.Server("WA1BTDICHANGE01").SetCPU(1)
```


### clc.v3.Server.SetPassword
```python
clc.v2.Server.SetPassword( password )
```
Request change of password.

The API request requires supplying the current password.  For this we issue a call
to retrieve the credentials so note there will be an activity log for retrieving the
credentials associated with any SetPassword entry

```python
>>> clc.v2.Server("WA1BTDICHANGE01").SetPassword("newpassword")
```


### Operations: clc.v2.Server.Pause, ShutDown, Reboot, Reset, PowerOn, PowerOff, Archive, StartMaintenance, StopMaintenance
```python
clc.v2.Server.Pause()
```

All above operations methods behave in the same manner.  They apply the operation command to the server
All are asynchronous methods so they return a `Requests` object.  Execute specified operations task against the server.

***Note if API indicates error due to server(s) already being in the requested state this is not raised as 
an error at this level.

```python
>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').PowerOn().WaitUntilComplete()
0
```


### clc.v2.Server.Refresh
```python
clc.v2.Server.Refresh()
```

Reloads the server object to synchronize with cloud representation.

```python
>>> clc.v2.Server("CA3BTDICNTRLM01").Refresh()
```


### clc.v2.Server.Disks
```python
clc.v2.Server.Disks()
```

Returns a `Disks` object representing all the disks associated with this server.
See the [disks](#disks) section for details on interacting with these objects.

```python
>>> clc.v2.Server("CA3BTDICNTRLM01").Disks()
<clc.APIv2.disk.Disks object at 0x10feea190>
```


### clc.v2.Server.GetSnapshots
```python
clc.v2.Server.GetSnapshots()
```

Returns a list of all existing Hypervisor level snapshots associated with this server.

```python
>>> clc.v2.Server("WA1BTDIAPI219").GetSnapshots()
[u'2015-01-10.02:10:38']
```


### clc.v2.Server.CreateSnapshot
```python
clc.v2.Server.CreateSnapshot( delete_existing=True, expiration_days=7 )
```

Take a Hypervisor level snapshot retained for between 1 and 10 days (7 is default).
Currently only one snapshop may exist at a time, thus will delete snapshots if one already
exists before taking this snapshot.

```python
>>> clc.v2.Server("WA1BTDIAPI219").CreateSnapshot(2)
<clc.APIv2.queue.Requests object at 0x10d106cd0>
>>> _.WaitUntilComplete()
0
```


### clc.v2.Server.DeleteSnapshots
```python
clc.v2.Server.CreateSnapshot( names=None )
```

Removes existing Hypervisor level snapshots.

Supply one or more snapshot names to delete them concurrently.
If no snapshot names are supplied will delete all existing snapshots.

```python
>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').DeleteSnapshot().WaitUntilComplete()
0
```


### clc.v2.Server.Alerts
```python
clc.v2.Server.Alerts()
```

Returns an `Alerts` object containing all alerts mapped to this server.

```python
>>> clc.v2.Server("NY1BTDIPHYP0101").Alerts()
<clc.APIv2.alert.Alerts object at 0x1065b0150>
```


### clc.v2.Server.RestoreSnapshot
```python
clc.v2.Server.RestoreSnapshots( name=None)
```

Restores an existing Hypervisor level snapshot.

Supply snapshot name to restore
If no snapshot name is supplied will restore the first snapshot found

```python
>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').RestoreSnapshot().WaitUntilComplete()
0
```


### clc.v2.Server.Delete
```python
clc.v2.Server.Delete()
```

Deletes the server.

```python
>>> clc.v2.Server("WA1BTDIAPI219").Delete().WaitUntilComplete()
0
```


### clc.v2.Server.Clone
Creates one or more clones of existing server.
```python
clc.v2.Server.Clone( network_id, group_id, name=None, cpu=None, memory=None,
                     alias=None, password=None, ip_address=None, storage_type=None,
					 type=None, primary_dns=None, secondary_dns=None, custom_fields=None,
					 ttl=None, managed_os=False, description=None, source_server_password=None,
					 cpu_autoscale_policy_id=None, anti_affinity_policy_id=None, packages=[], count=1)
```


Set ttl as number of seconds before server is to be terminated.

* network_id is currently a required parameter.  This will change to optional once APIs are available to return the network id of self.
* if no password is supplied will reuse the password of self.  Is this the expected behavior?  Take note there is no way to for a system generated password with this pattern since we cannot leave as None
* any DNS settings from self are not propogated to clone since they are unknown at system level and the clone process will touch them
* no change to the disk layout we will clone all
* clone will not replicate managed OS setting from self so this must be explicitly set

```python
>>> d = clc.v2.Datacenter()
>>> clc.v2.Server(alias='BTDI',id='WA1BTDIAPI207').Clone(network_id=d.Networks().networks[0].id,count=2)
0
```


### clc.v2.Server.Account
```python
clc.v2.Server.Account()
```

Returns the `Account` object that owns this server.

```python
>>> clc.v2.Server("CA3BTDICNTRLM01").Account()
<clc.APIv2.account.Account instance at 0x108789878>
>>> print _
BTDI
```


### clc.v2.Server.Group
```python
clc.v2.Server.Group()
```

Returns the `Group` object that owns this server.

```python
>>> clc.v2.Server("CA3BTDICNTRLM01").Group()
<clc.APIv2.group.Group object at 0x10b07b7d0>
>>> print _
Ansible Managed Servers
```



## Request

[Requests pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.request.html)


### Class variables

Object variables:

* requests.requests
* requests.error_requests
* requests.success_requests

### clc.v2.Requests
```python
clc.v2.Requests( requests_lst, alias=None )
```

Create `Requests` object.


### clc.v2.Requests.WaitUntilComplete(poll_freq=2):
```python
clc.v2.Requests.WaitUntilComplete( poll_freq=2 )
```

Block until all `Request` objects have completed. 

If status is 'notStarted' or 'executing' continue polling.
If status is 'succeeded' then success
Else log as error

poll_freq option is in seconds

Returns an Int the number of unsuccessful requests.  This behavior is subject to change.
`requests.successs_requests` and `requests.error_requests` are lists containing `Request`
objects in a completed state.

```python
>>> clc.v2.Server(alias='BTDI',id='WA1BTDIKRT02').PowerOn().WaitUntilComplete()
0
```


## Request

[Request pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.request.html)


### Class variables

Object variables:

* request.id
* request.alias
* request.time_created
* request.time_executed
* request.time_completed


### clc.v2.Request(id,alias=None,request_obj=None)
```python
clc.v2.Request( id, alias=None, request_obj=None )
```

Create a `Request` object.


### clc.v2.Request.Status
```python
clc.v2.Request.Status( cached=False
```

Return the current status for an existing request.  If `cached` is set to True and an existing
status is known then no API call will be made to refresh the status.


### clc.v2.Request.WaitUntilComplete
```python
clc.v2.Request.WaitUntilComplete( poll_freq=2 )
```

Create a `Request` object.
Poll until status is completed.

If status is 'notStarted' or 'executing' continue polling.
If status is 'succeeded' return
Else raise exception

poll_freq option is in seconds

As status option changes the following class variables are populated:
* request.time_created
* request.time_executed
* request.time_completed


