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


### clc.v2.Group.Groups(groups_lst,alias=None)
`Groups` object constructor.  If no alias is provided will use the default associated with the API
credentials in use.  `groups_lst` is a list of group objects retrieved from API.  Usually no need to call this constructor directly.


### clc.v2.Group.Groups.Get(key)
Returns a `Group` object matching the provided key.  Match is against name, ID, or description.
If key is not unique and finds multiple matches only the first will be returned

```python
>>> clc.v2.Datacenter().Groups().Get("Default Group")
<clc.APIv2.group.Group object at 0x1065e5250>
```


### clc.v2.Group.Groups.Search(key)
Returns a list of `Group` objects with partial matches to the provided key.  Match is against name, ID, or description.

```python
>>> clc.v2.Datacenter().Groups().Get("Default Group")
<clc.APIv2.group.Group object at 0x1065e5250>
```







## Server

[Server pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.server.html)



## Queue

[Queue pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.queue.html)



## Datacenter

[Datacenter pydocs output](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.APIv2.datacenter.html)



