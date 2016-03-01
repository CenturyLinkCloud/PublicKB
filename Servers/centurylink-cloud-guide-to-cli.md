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
CLI for API v2 [(explains here)](//github.com/CenturyLinkCloud/clc-go-cli) and [Python based CLI for API v1 and v2](//github.com/CenturyLinkCloud/clc-python-sdk)

For accounts, users, [API v1](//ca.ctl.io/api-docs/v1/u5o/) provides the access to this information. For the rest of the data, [API v2](//www.ctl.io/api-docs/v2/) can be used to access this information.

The Python based SDK is crossed platform, the CLI can be ran on any Python 2.7 environment.  For detail usage of Python CLI and download, please see its [GitHub repository](//github.com/CenturyLinkCloud/clc-python-sdk/blob/master/README_CLI.md).  The pre-complied windows CLI executable can be downloaded from [here](//github.com/CenturyLinkCloud/clc-python-sdk/raw/master/src/dist/clc-cli.exe).
The GO based CLI can be run on Mac OSX, Linux and Windows. For download page, please see the [CenturyLink Cloud CLI GitHub release page](//github.com/CenturyLinkCloud/clc-go-cli/releases).  
The resources available on both tools will output similar results, at this time, certain functions are only available on API v1, hence the need of both tools to capture all the functionalities of the platform.

Comparison of the two CLI tools:

| CLI         |   Python            | Go                  |
| ---------   | ------------------- | -----------------   |
| API version | Mostly v1 (some v2) |         v2          |
| Resources     |  accounts <br> billing <br> blueprints <br> groups <br> networks <br> queue <br> servers <br> users <br>         |   alert-policy <br> anti-affinity-policy <br> autoscale-policy <br> billing <br> custom-fields <br> data-center <br> firewall-policy <br> group <br> load-balancer <br> load-balancer-pool <br> login <br> network <br> server <br> wait <br>      |




### Prerequisites
-   Access to the CenturyLink Cloud platform as an authorized user
-   Understanding of CenturyLink Cloud portal
-   Scripting knowledge will help on fully utilizing the CLI
-   Python 2.7 installed in the environment for Python based CLI
-   API user account [please see this KB for detail](//www.ctl.io/knowledge-base/accounts-&-users/creating-users/)

### Use Case Scenarios
This tool enables system administrators to interface with CenturyLink Cloud without programming with the API or the using the Control Portal.  Automation can be achieved using scripting and other automation tools.

### Installation of CenturyLink Cloud CLI

***In order to make easy distintion between the two CLIs, clc-cli is the Python based tool and clc is the GO based tool.***

**Python Based CLI:**

Installation instruction is available [here](//github.com/CenturyLinkCloud/clc-python-sdk).  If pip is installed, then the following command will installed the CenturyLink Cloud Python SDK and CLI:
```
pip install clc-sdk
```
For authentication, it can be several way, please see the [README page of the CLI](//github.com/CenturyLinkCloud/clc-python-sdk/blob/master/README_CLI.md#authentication).  In order to use a system configuration file, a clc.ini (Windows) or clc_config (POSIX) needs to be created.  An example is shown below:
```
[global]
V1_API_KEY=
V1_API_PASSWD=

V2_API_USERNAME=
V2_API_PASSWD=

blueprint_ftp_url=ftp://user:password@ftp_fqdn
```
The CLI command is clc in Linux or MacOSX and clc-cli for Windows.
`clc-cli` --help will print out the help message,

```
usage: clc-cli.exe [-h] [--cols [COL [COL ...]]] [--config CONFIG] [--v1-api-key KEY] [--v1-api-passwd PASSWORD]                    [--v2-api-username USERNAME] [--v2-api-passwd PASSWORD] [--async] [--quiet] [--verbose] [--format {json,table,text,csv}]                    {accounts,users,servers,groups,billing,networks,queue,blueprints} ...

CLI tool for interacting with CenturyLink Cloud API.  
optional arguments:
  -h, --help                  show this help message and exit
  --cols [COL [COL ...]]      Include only specific columns in the output
  --config CONFIG, -c         CONFIG Ini config file
  --v1-api-key KEY            V1 API key
  --v1-api-passwd PASSWORD    V1 API password
  --v2-api-username USERNAME  V2 API username
  --v2-api-passwd PASSWORD    V2 API password
  --async                     Return immediately after queueing long-running calls
  --quiet, -q                 Supress status output (repeat up to 2 times)
  --verbose, -v               Increase verbosity
  --format {json,table,text,csv}, -f {json,table,text,csv}  Output result format (table is default)

Commands:
  {accounts,users,servers,groups,billing,networks,queue,blueprints}
    accounts            Account level activities (list, create, modify)
    users               User level activities (list, create, modify)
    servers             Server level activities (list, create, modify)
    groups              Group level activities (list, create, modify)
    billing             Billing activities
    networks            Network activities
    queue               Work queue
    blueprints          Blueprints

```


**GO Based CLI:**

Installation is simple for the GO based CLI. Download the executable and run it. The detail
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

`clc -–help` will print out the help message, --help works on options
of the command as well.

Output of `clc -–help`:

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

Using command without a configuration file:
```
clc-cli --v1-api-key xxxxxxxxxxxxxxxxx --v1-api-passwd xxxxxxxxxxxxx  Commands
```
```
clc login –user username –password
```
Or setup the configuration file as described in [Installation of CenturyLink Cloud CLI](#installation-of-centurylink-cloud-cli)

**Output Format:**

For output (with --format for clc-cli or –-output for clc), there are several options:
‘JSON, TEXT, TABLE’, an additional option ‘csv’ for clc-cli.

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
csv:
```
HardwareGroupUUID,Name,Description,Cpu,MemoryGB,Status,TotalDiskSpaceGB,ServerType,OperatingSystem,PowerState,Location,IPAddress
123456789abcdef123456789abcdef,CA3ABCDCEPHST05,TEST,2,4,Archived,76,1,47,Stopped,CA3,10.x.x.x
```

### READ commands
(No changes made with the following commands)

***List and Find***

**List all accounts**
```
clc-cli accounts list
```
**List details of an account**
```
clc-cli accounts get -alias ABCD
```
**List all users in an account**
```
clc-cli users lists
```
**Get detail of a user**
```
clc-cli users get --alias ABCD --user "demo.user"
```
**List all data centers:**
```
clc-cli accounts locations
```
```
clc data-centers list
```

**List all servers in the account:**
```
clc-cli servers list
```
```
clc server list
```

**For a particular data center:**
```
clc-cli servers list --location CA3
```
```
clc server list –-data-center ca1
```

Or
```
clc server list -–filter “LocationID”=”CA3”
```
**List hostname of all servers in a datacenter:**
```
clc-cli --cols Name --config config.ini servers list --location CA3
```
```
clc server list --all --filter location-id=CA3 --query details.host-name
```
or
```
clc server list –all --query location-id=ca3
```

**Find all the hyperscale (or standard/baremetal) server in the
account:**
```
clc server list --all --filter type=hyperscale --query details.host-name
```

**All OS/templates available in a DC:**
```
clc data-center get-deployment-capabilities --data-center CA3 --query templates.name --output text
```

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
WIN2012R2DTC-64
```

**Show all “active” servers :**
```
clc server list --all --filter status=active --output table
```

**Who/when created a server:**
```
clc server list --all --filter name=CA3ABCDADM01 --query change-info.{created-by,created-date}
```

**Display power state and hostname:**
```
clc-cli --cols Name PowerState --config.ini servers list-all
```
```
clc server list --all --query details.{power-state,host-name}
```

**All paused servers (or started and stopped):**
For Windows command:
```
clc server list --all --query details.{power-state,host-name} --output text | find "paused"
```
For Linux or MacOSX:
```
clc server list --all --query details.{power-state,host-name} --output text | grep "paused"
```

**Server name with number of CPUs and memory (in MB):**
```
clc server list --all --query "details.{cpu,memoryMB,host-name}" --output text
```

**Find IP addresses with server name:**
```
clc-cli -f text --cols Name IPAddress --config.ini servers list-all
```
```
clc server list --all --query "details.{host-name,ipAddresses}" --output text
```

**List all groups:**
```
clc-cli group list
```
```
clc group list –all
```

**Find all empty groups:**
```
clc group list --filter 'servers-count=0'
```

**Find all groups with servers:**
```
clc group list --filter 'servers-count>0'
```

**List all network in a datacenter:**
```
clc-cli networks list --location ca3
```
```
clc network list --data-center ca3 --output table
```
**Query the above result with Name, Description and Gateway:**
```
clc network list --data-center ca3 --query Name,Description,Gateway --output table
```
**List all jobs in the queue**
```
clc-cli queue list
```
**List Blueprints (all, scripts, software and system)**
```
clc-cli blueprints list
clc-cli blueprints list-scripts
clc-cli blueprints list-software
clc-cli blueprints list-system
```

### Billing and Accounting

**Get Month to Date billing on the account**
```
clc-cli billing account-summary
```
**Get invoice for a month**
```
clc billing get-invoice-data --year 2015 --month 12
```

**Narrow down the output with locations**
```
clc billing get-invoice-data --year 2015 --month 12 --query LineItems.{ServiceLocation,UnitCost} --output json
```
**Get billing for a group:**
```
clc group get-billing-details --group-name Test
```
*Output contains:*

*ArchiveCost, CurrentHour, MonthToDate, MonthlyEstimate, TemplateCost*

**Get Billing for a server:**
```
clc-cli billing server-estimate --server CA3ABCDTEST104
```
For Windows:
```
clc group get-billing-details --group-name ceph --output text | find “hostname”
```
For Linux or MacOSX:
```
clc group get-billing-details --group-name ceph --output text | grep “hostname”
```

**From a Master account to look in a sub-account:**
```
clc-cli account get --alias SUBA
cli-cli users list --alias SUBA
clc-cli servers list --alias SUBA
clc-cli networks list --alias SUBA
clc-cli groups list --location CA3 --alias SUBA
clc-cli billing account-summary --alias SUBA
```
```
clc server list --account-alias SUBA
clc network list --account-alias SUBA
clc group list --data-center CA3 --account-alias SUBA
clc billing get-invoice-data --account-alias SUBA --year 2016 --month 1
```

**List group and server in a specific account:**
```
clc-cli groups list --alias ABCD
```
```
clc group list –account-alias ABCD
```
```
clc server list –account-alias ABCD
```

### Commands change the environment
(**Warning**: use with care)

***Create***

**Create a user**
```
clc-cli users create --alias ABCD --user "new.test" --email new.test@abcd.com --first-name new --last-name test --roles AccountViewer
```
*Possible roles: ServerAdministrator,BillingManager,DNSManager,AccountAdministrator,AccountViewer,NetworkManager,SecurityManager,ServerOperator*

**Create a group:**
```
clc-cli groups create --location CA3 --alias ABCD --parnet DevOps --group TestingCLI --description "Testing group"
```
```
clc group create --name "TestCA3" --description "Test Servers" --parent-group-name "CA3 Hardware"
```

**Create a server:**
```
clc-cli servers create --alias ABCD --location CA3 --group TestingCLI --name test1 --template UBUNTU-14-64-TEMPLATE --backup-level Standard --cpu 1 --ram 1 --network vlan_771_10.56.171
```
```
clc server create --name test1 --description "test" --group-name TestingCLI --template-name UBUNTU-14-64-TEMPLATE --root-password xxxxxxxxx
--network-name vlan_771_10.56.171 --cpu 1 --memory-gb 1 --type standard --storage-type standard --additional-disks sizeGB=50,type=raw
```

**Create a new VLAN in a datacenter**
```
clc network create --data-center ca3
```
Output:
```
{
    "Href": "",
    "Id": "",
    "Name": "",
    "Rel": "",
    "Verbs": null
}
```

***Delete***

**Delete a server:**
```
clc-cli servers delete --server CA3ABCDTEST106
```
```
clc server delete --server-name CA3ABCD2TSQL01
```
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
clc-cli groups delete --group TestGroup
```
```
clc group delete -–group-name TestGroup
```


### Advanced Usage

**Adding a secondary network card on a server**
Please refer to the [Add or Remove Network Interface to Server using Go CLI](../Network/add-or-remove-network-interface-to-server-using-go-cli.md)

**Create firewall rule with port tcp/22 between VLANs:**
```
clc firewall-policy create --data-center CA1 --destination-account abcd --sources "10.56.250.0/24" --destinations "10.56.171.0/24" --ports tcp/22
```

**Create a json file for repeat usage of frequent use commands**

For the example below, servername.json is created to list all the hostname of all servers in the account:
```
clc server list --all --query details.host-name --generate-cli-skeleton > servername.json
```
To use the file,
```
clc server list --from-file servername.json
```

### Support
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying any Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](//t3n.zendesk.com/tickets/new).
* For CLI bugs, please visit [CenturyLink Cloud CLI Github](//github.com/CenturyLinkCloud/clc-go-cli/issues) and [CenturyLink Cloud Python SDK](//github.com/CenturyLinkCloud/clc-python-sdk/issues)
