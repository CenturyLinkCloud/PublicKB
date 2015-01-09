# CenturyLink Cloud APIV2 Python SDK

This repository contains a Python SDK to interact with the ***CenturyLink Cloud*** API.  The SDK documented at this page aligns to the to API [V2](https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-).  The API does not yet have full coverage of all cloud functions.  As the API matures this SDK
will follow suit.

## Contents

* [Quick Start](#quick-start)
* [Authentication](#authentication)
* [Account](#account) - Account level activities
* [Datacenter](#datacenter) - View and interact with geographic specific datacenter components
* [Group](#group) - `Groups` and `Group` classes.  Logical organization around assets by group which can contain sub-groups or servers
* [Server](#server) - `Servers` and `Server` classes.  Cloud servers
* [Queue](#queue) - Interface to work queue for async operations


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
* account.isManaged

### clc.v2.Account.GetAlias() (static)
Return specified alias or if None the alias associated with the provided credentials.


```python
>>> clc.v2.Account.GetAlias()
u'BTDI'
```


### clc.v2.Account.GetLocation() (static)
Return specified location or if None the default location associated with the provided credentials and alias.

```python
>>> clc.v2.Account.GetLocation()
u'WA1'
```


### clc.v2.Account(alias=None)
Create `Account` object associated with provided alias (or default alias if none provided).

```python
>>> clc.v2.Account()
<clc.APIv2.account.Account instance at 0x1065a2e60>
```


### clc.v2.ParentAccount()
Return `Account` object associated with the parent of the current account.
Returns None if already at top-level account.

```python
>>> clc.v2.Account()
<clc.APIv2.account.Account instance at 0x1065a2e60>
```

### clc.v2.PrimaryDatacenter()
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


### clc.v2.Datacenter.Datacenters(alias=None) (static)
Return all cloud locations available to the calling alias.

```python
>>> clc.v2.Datacenter.Datacenters(alias=None)
[<clc.APIv2.datacenter.Datacenter instance at 0x101462fc8>, <clc.APIv2.datacenter.Datacenter instance at 0x101464320>]
```

### clc.v2.Datacenter(location=None,name=None,alias=None)
Create new `Datacenter` object associated with supplied location and alias.  If neither are provided
use the default values associated with the supplied credentials.

```python
>>> clc.v2.Datacenter()
<clc.APIv2.datacenter.Datacenter instance at 0x1065a2fc8>
>>> print _
WA1
```


### clc.v2.Datacenter.RootGroup()
Returns `Group` object for datacenter root group.

```python
>>> clc.v2.Datacenter().RootGroup()
<clc.APIv2.group.Group object at 0x105feacd0>
>>> print _
WA1 Hardware
```


### clc.v2.Datacenter.Groups()
Returns `Groups` object for datacenter root group.

```python
>>> clc.v2.Datacenter().Groups()
<clc.APIv2.group.Groups object at 0x1065abc50>
```


### clc.v2.Datacenter.Networks()
Returns a `Networks` object associated with the datacenter.

```python
>>> clc.v2.Datacenter().Networks()
<clc.APIv2.network.Networks object at 0x105fea7d0>
```


### clc.v2.Datacenter.Templates()
Returns a `Templates` object associated with the datacenter.

```python
>>> clc.v2.Datacenter().Templates()
<clc.APIv2.template.Templates object at 0x1065abc90>
```



## Group

[Groups pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.groups.html)
[Group pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.group.html)

### Class variables

Object variables:

* group.id
* group.name
* group.description
* group.type
* group.status
* group.server_count

Object variables available but access subject to change with future releases:

* group.custom_fields
* group.change_info


### clc.v2.Groups(groups_lst,alias=None)
`Groups` object constructor.  If no alias is provided will use the default associated with the API
credentials in use.  `groups_lst` is a list of group objects retrieved from API.  Usually no need to call this constructor directly.


### clc.v2.Groups.Get(key)
Returns a `Group` object matching the provided key.  Match is against name, ID, or description.
If key is not unique and finds multiple matches only the first will be returned

```python
>>> clc.v2.Datacenter().Groups().Get("Default Group")
<clc.APIv2.group.Group object at 0x1065e5250>
```


### clc.v2.Groups.Search(key)
Returns a list of `Group` objects with partial matches to the provided key.  Match is against name, ID, or description.

```python
>>> clc.v2.Datacenter().Groups().Get("Default Group")
<clc.APIv2.group.Group object at 0x1065e5250>
```


### clc.v2.Group.GetAll(root_group_id,alias=None) (static)
Given a group ID and optional alias returns a list of `Group` objects associated with that group.

*Subject to deprecation in future release.*

```python
>>> clc.v2.Group.GetAll("wa1-4416")
[<clc.APIv2.group.Group object at 0x1065b0190>, <clc.APIv2.group.Group object at 0x1065b0dd0>]
```


### clc.v2.Group(id,alias=None,group_obj=None)
Create a new `Group` object.  If alias is not provided will use default value associated with the account.
If `group_obj` is not provided will perform and API query to get group definition.  `group_obj` is a list of
group definitions from the API and is not generally used by user functions.

```python
>> clc.v2.Group(id="wa1-1798")
<clc.APIv2.group.Group object at 0x109188b90>
```


### clc.v2.Create()
Creates a new group and returns a `Group` object.

```python
>>> clc.v2.Datacenter(location="WA1").RootGroup().Create("Test3","Description3")
<clc.APIv2.group.Group object at 0x10cc76c90>
>>> print _
Test5
```


### clc.v2.Delete()
Deletes group.  Returns a `Requests` object.

```python
>>> clc.v2.Group("wa1-4416").Create(name="Test6")
<clc.APIv2.group.Group object at 0x1041937d0>
>>> clc.v2.Group(_.id).Delete().WaitUntilComplete()
0
```


### clc.v2.Subgroups()
Returns a `Groups` object containing all child groups.

```python
>>> clc.v2.Group("wa1-4416").Subgroups()
<clc.APIv2.group.Groups object at 0x105fa27d0>
```


### clc.v2.Servers()
Returns a `Servers` object containing all servers within the group.

```python
>>> clc.v2.Group("wa1-4416").Servers()
<clc.APIv2.server.Servers object at 0x1065b0f10>
```


### clc.v2.Account()
Returns the `Account` object that owns this group.

```python
>>> clc.v2.Group(alias="BTDI",id="wa1-837").Account()
<clc.APIv2.account.Account instance at 0x108789878>
>>> print _
BTDI
```



## Server

[Servers pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.servers.html)
[Server pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.server.html)


### Class variables

Object variables:

    server.id
    server.description
    server.cpu
    server.power_state
    server.memory
    server.storage
    server.group_id
    server.is_template
    server.location_id
    server.name
    server.os
    server.os_type
    server.status
    server.type
    server.storage_type
    server.in_maintenance_mode
    server.reserved_drive_paths
    server.adding_cpu_requires_reboot
    server.adding_memory_requires_reboot

Object variables available but access subject to change with future releases:

    server.custom_fields
    server.change_info
    server.alert_policies
    server.ip_addresses


### clc.v2.Servers(servers_lst,alias=None)
`Servers` object constructor.  If no alias is provided will use the default associated with the API
credentials in use.  `servers_lst` is a list of server names. 

Note this behaves differently than the other container classes like Groups where the *_lst
parameter can fully define the object.  All we have is the server name on construction.
We will lazily create server objects as needed since each requires a seperate API call.

```python
>>> clc.v2.Servers(["NY1BTDIPHYP0101","NY1BTDIWEB0101"])
<clc.APIv2.server.Servers object at 0x105fa27d0>
```


### clc.v2.Servers.Servers(cached=True)
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

### Operations: clc.v2.Servers.Pause(), ShutDown, Reboot, Reset, PowerOn, PowerOff, StartMaintenance, StopMaintenance
All above operations methods behave in the same manner.  They apply the operation command to all
servers in the object.  All are asynchronous methods so they return a `Requests` object.

```python
>>> clc.v2.Servers(["NY1BTDIPHYP0101","NY1BTDIWEB0101"]).Pause()
<clc.APIv2.queue.Requests object at 0x105fea7d0>
>>> _.WaitUntilComplete()
0
```



## Queue

[Queue pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.queue.html)



