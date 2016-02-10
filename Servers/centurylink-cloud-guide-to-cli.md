{{{
  "title": "CenturyLink Cloud Guide to CLI",
  "date": "02-13-2016",
  "author": "Gavin Lai",
  "attachments": [],
  "contentIsHTML": false
}}}
### Table of contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Use Case Scenarios](#use-case-scenarios)
* [Installation of CenturyLink Cloud CLI](#installation-of-centurylink-cloud-cli)
* [READ commands](#read-commands)
* [Billing and Accounting](#billing-and-accounting)
* [Commands change the environment](#commands-change-the-environment)
* [Advanced usage](#advanced-usage)
* [Support](#support)

### Overview

There are two CLI interfaces available on CenturyLink Cloud, GO based
CLI for API v2 (explains here) and Python based CLI for API v1 and v2.

For accounts, users, groups, [API v1](//github.com/CenturyLinkCloud/clc-python-sdk/blob/master/README_CLI.md) provides the access to this information. For the rest of the data, [API v2](https://www.ctl.io/api-docs/v2/) can be used to access this information.

For detail usage of CLI v1 and download, please see its [GitHub
repository](//github.com/CenturyLinkCloud/clc-python-sdk/blob/master/README_CLI.md).
The windows CLI executable can be downloaded from
[here](//github.com/CenturyLinkCloud/clc-python-sdk/raw/master/src/dist/clc-cli.exe).

The new GO based CLI can be run on Mac OSX, Linux and Windows. For
download page, please see the [CenturyLink Cloud CLI GitHub release
page](//github.com/CenturyLinkCloud/clc-go-cli/releases).

### Prerequisites
-   Access to the CenturyLink Cloud platform as an authorized user
-   Understanding of CenturyLink Cloud portal
-   Scripting knowledge will help on fully utilizing the CLI

### Use Case Scenarios
This tool enables system administrators to interface with CenturyLink Cloud without programming with the API or the using the Control Portal.  Automation can be achieved using scripting and other automation tools.

### Installation of CenturyLink Cloud CLI
Installation is simple. Download the executable and run it. The detail
of the installation steps can be found [here](//github.com/CenturyLinkCloud/clc-go-cli).
A configuration file can be set up with account information, the detail
steps are located [here](//github.com/CenturyLinkCloud/clc-go-cli#set-up-the-configuration-file).

Below is a sample configuration file:
```
user: bob
password: passw0rd
defaultformat: "table"
defaultdatacenter: "CA1"
profiles:
alice:
user: alice
password: pa33w0rd
```

\`clc –help\` will print out the help message, --help works on options
of the command as well.

Output of clc –help:

```

To get full usage information run clc without arguments.
Available resources:

network
alert-policy
custom-fields
login
server
anti-affinity-policy
billing
load-balancer
group
data-center
firewall-policy
load-balancer-pool
wait
autoscale-policy
```

**Logging into the CenturyLink account:**
Login to an account with a configuration file:
```
clc login –user username –password
```
**Output Format:**

For output (with –-output), there are three options:
‘JSON, TEXT, TABLE’
JSON:
```
[
    {
        "CreatedBy": "test.user.abcd",
        "CreatedDate": "2016-01-08 21:08:12"
    }
]
```
Text:
```
test.user.abcd  2016-01-08 21:08:12
```
Table:
```
+----------------+---------------------+
|   CreatedBy    |     CreatedDate     |
+----------------+---------------------+
| test.user.abcd | 2016-01-08 21:08:12 |
+----------------+---------------------+
```
### READ commands  (no changes made):

***List and Find***

**List all data centers:**
```
clc data-centers list```

**List all servers in the account:**
```
clc server list```

**For a particular data center:**
```
clc server list –-data-center ca1```

Or
```
clc server list -–filter “LocationID”=”CA3”```

**List hoatname of all servers in a datacenter:**
```
clc server list --all --filter location-id=CA3 --query details.host-name```
or
```
clc server list –all --query location-id=ca3```

**Find all the hyperscale (or standard/baremetal) server in the
account:**
```
clc server list --all --filter type=hyperscale --query details.host-name```

**All OS/templates available in a DC:**
```
clc data-center get-deployment-capabilities --data-center CA3 --query templates.name --output text```

Example of the output (OS and templates can be used for server installation at a datacenter)
```
CENTOS-5-64-TEMPLATE
CENTOS-6-64-TEMPLATE
CENTOS-7-64-TEMPLATE
DEBIAN-6-64-TEMPLATE
DEBIAN-7-64-TEMPLATE
OPENVPN-CENT6-TEMPLATE
PXE-TEMPLATE
RHEL-5-64-TEMPLATE
RHEL-6-64-TEMPLATE
RHEL-7-64-TEMPLATE
UBUNTU-12-64-TEMPLATE
UBUNTU-14-64-TEMPLATE
WIN2008R2DTC-64
WIN2008R2ENT-64
WIN2008R2STD-64
WIN2012DTC-64
WIN2012R2DTC-64```

**Show all “active” servers :**
```
clc server list --all --filter status=active --output table```

**Who/when created a server:**
```
clc server list --all --filter name=CA2ABCDADM01 --query
change-info.{created-by,created-date}```

**Display power state and hostname:**
```
clc server list --all --query details.{power-state,host-name}```

**All paused servers (or started and stopped):**
For Windows command:
```
clc server list --all --query details.{power-state,host-name} --output text | find "paused"```
For Linux or MacOSX:
```
clc server list --all --query details.{power-state,host-name} --output text | grep "paused" (Linux/MacOSX)```

**Server name with number of CPUs and memory (in MB):**
```
clc server list --all --query "details.{cpu,memoryMB,host-name}"
--output text```

**Find IP addresses with server name:**
```
clc server list --all --query "details.{host-name,ipAddresses}" --output text```

**List all groups:**
```
clc group list –all```

**Find all empty groups:**
```
clc group list --filter 'servers-count=0'```

**Find all groups with servers:**
```
clc group list --filter 'servers-count>0'```

**List all network in a datacenter:**
```
clc network list --data-center ca3 --output table```
**Query the above result with Name, Description and Gateway:**
```
clc network list --data-center ca3 --query Name,Description,Gateway --output table```


### Billing and Accounting

**Get invoice for a month**
```
clc billing get-invoice-data --year 2015 --month 12```

**Narrow down the output with locations**
```
clc billing get-invoice-data --year 2015 --month 12 --query LineItems.{ServiceLocation,UnitCost} --output
json
```
**Get billing for a group:**
```
clc group get-billing-details --group-name Test
```
*Output contains:

*ArchiveCost, CurrentHour, MonthToDate, MonthlyEstimate, TemplateCost *

**Get Billing for a server:**

For Windows:
```
clc group get-billing-details --group-name ceph --output text | find “hostname”
```
For Linux or MacOSX:
```
clc group get-billing-details --group-name ceph --output text | grep “hostname”
```

**From a Master account to look in a sub-account:**

**List group in a specific account:**
```
clc group list –account-alias ABCD```
```
clc server list –account-alias ABCD```

### Commands change the environment:
(**Warning**: use with care)

***Create***

**Create a group:**
```
clc group create --name "TestCA2" --description "Test Servers" --parent-group-name "CA2 Hardware"```

**Create a server:**
```
clc server create --name test1 --description "test" --group-name Test
--template-name UBUNTU-14-64-TEMPLATE --root-password xxxxxxxxx
--network-name vlan\_771\_10.56.171 --cpu 1 --memory-gb 1 --type
standard --storage-type standard --additional-disks sizeGB=50,type=raw```

**Create a new VLAN in a datacenter**
```
clc network create --data-center ca2```

{
    "Href": "",
    "Id": "",
    "Name": "",
    "Rel": "",
    "Verbs": null
}

***Delete***

**Delete a server:**
```
clc server delete --server-name CA3ABCD2TSQL01```
Output looks like below:
```
{
"ErrorMessage": "",
"IsQueued": true,
"Server": "ca3abcd2tsql01"
}
```
**Delete a group** (will delete all servers in this group):
```
clc group delete –group-name TestGroup```


### Advanced Usage

**Create firewall rule with port tcp/22 between VLANs:**
```
C:\Users\test.user\Downloads\clc-20160106>clc firewall-policy create --data-center CA1 --destination-account abcd --sources "10.56.250.0/24" --destinations "10.56.171.0/24" --ports tcp/22```

**Create a json file for repeat usage of frequent use commands**
For the example below, servername.json is created to list all the hostname of all servers in the account:
```
clc server list --all --query details.host-name --generate-cli-skeleton > servername.json```
To use the file,
```
clc server list --from-file servername.json```

### Support
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying any Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](//t3n.zendesk.com/tickets/new).
* For CLI bugs, please visit [CenturyLink Cloud CLI Github](//github.com/CenturyLinkCloud/clc-go-cli)
