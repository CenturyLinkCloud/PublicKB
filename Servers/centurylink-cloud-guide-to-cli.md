{{{
  "title": "CenturyLink Cloud Guide to CLI",
  "date": "01-19-2017",
  "author": "Gavin Lai",
  "attachments": [],
  "contentIsHTML": false
}}}
### Table of contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Keywords](#keywords)
* [Use Case Scenarios](#use-case-scenarios)
* [Installation of CenturyLink Cloud CLI](#installation-of-centurylink-cloud-cli)
* [READ commands](#read-commands)
* [Billing and Accounting](#billing-and-accounting)
* [Commands change the environment](#commands-change-the-environment)
* [Advanced Usage(Wait/Execute packages)](#advanced-usage)
  * [Network/Firewall](#networkfirewall)
  * [Snapshot](#snapshot)
  * [Site to Site VPN](#site-to-site-vpn)
* [Application Services control](#application-services-control)
  * [Relational Database Service](#relational-database-service)
  * [Intrusion Prevention Service](#intrusion-prevention-service)
  * [Patching Service](#patching-service)
  * [Storage](#storage)
  * [Simple Backup Service](#simple-backup-service)
  * [Webhooks](#webhooks)
* [Support](#support)

### Overview

There are two CLI interfaces available on CenturyLink Cloud, GO based
CLI for API v2 [(explains here, currently version 1.1)](https://github.com/CenturyLinkCloud/clc-go-cli) and [Python based CLI for API v1 and v2](//github.com/CenturyLinkCloud/clc-python-sdk)

For accounts, users, [API v1](//ca.ctl.io/api-docs/v1/u5o/) provides the access to this information. For the rest of the data, [API v2](//www.ctl.io/api-docs/v2/) can be used to access this information.

The Python based SDK is crossed platform, the CLI can be ran on any Python 2.7 environment.  For detail usage of Python CLI and download, please see its [GitHub repository](//github.com/CenturyLinkCloud/clc-python-sdk).  The pre-complied windows CLI executable can be downloaded from [here](//github.com/CenturyLinkCloud/clc-python-sdk/raw/master/src/dist/clc-cli.exe).
The GO based CLI can be run on Mac OSX, Linux and Windows. For release notes and download page, please see the [CenturyLink Cloud CLI GitHub release page](//github.com/CenturyLinkCloud/clc-go-cli/releases).  
The resources available on both tools will output similar results, at this time, certain functions are only available on API v1, hence the need of both tools to capture all the functionalities of the platform.

Comparison of the two CLI tools:

| CLI         |   Python            | Go                  |
| ---------   | ------------------- | -----------------   |
| API version | Mostly v1 (some v2) |         v2          |
| Resources     |  accounts <br> billing <br> blueprints <br> groups <br> networks <br> queue <br> servers <br> users <br>         |   alert-policy <br> anti-affinity-policy <br> autoscale-policy <br> backup <br> billing <br> crossdc-firewall-policy <br> custom-fields <br> data-center <br> db <br> firewall-policy <br> group <br> ips <br> load-balancer <br> load-balancer-pool <br> login <br> network <br> os-patch <br> server <br> site-to-site-vpn <br> version <br> wait <br> webhook <br>     |




### Prerequisites
-   Access to the CenturyLink Cloud platform as an authorized user
-   Understanding of CenturyLink Cloud portal
-   Scripting knowledge will help on fully utilizing the CLI
-   Python 2.7 installed in the environment for Python based CLI
-   API user account [please see this KB for detail](//www.ctl.io/knowledge-base/accounts-&-users/creating-users/)

### Keywords
When running commands (GO CLI command/Python CLI command)
-   alias - Account Alias, it can be found in the top left corner of the portal
-   name - name of the server or group, when creating a new server, the length limit is 6 characters
-   data-center - name of the data centers (e.g. IL1, VA1, CA1)
-   network-name/network - name of the VLAN, [they can be listed using CLI](#read-commands)
-   type - server typee
-   storage-type/backup-level - storage type, current option is standard
-   group-name/group - name of the group within the account
-   configuration-id - ID of bare metal from output of `clc data-center get-baremetal-capabilities`

Output and error message
-   alias - In both the output and error messages, alias can be server name/account/data-center alias
-   name - depending on the query, it can me server name, location, account name etc


### Use Case Scenarios
This tool enables system administrators to interface with CenturyLink Cloud without programming with the API or the using the Control Portal.  Automation can be achieved using scripting and other automation tools.

### Installation of CenturyLink Cloud CLI

***In order to make easy distintion between the two CLIs, clc-cli is the Python based tool and clc is the GO based tool.***

**Python Based CLI**

Installation instruction is available [here](//github.com/CenturyLinkCloud/clc-python-sdk).  If pip is installed, then the following command will installed the CenturyLink Cloud Python SDK and CLI:
```
pip install clc-sdk
```
For authentication, it can be several way, please see the [README page of the CLI](//github.com/CenturyLinkCloud/clc-python-sdk/).  In order to use a system configuration file, a clc.ini (Windows) or clc_config (POSIX) needs to be created.  An example is shown below:
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


**GO Based CLI**

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
    alert-policy
    anti-affinity-policy
    autoscale-policy
    backup
    billing
    crossdc-firewall-policy
    custom-fields
    data-center
    db
    firewall-policy
    group
    ips
    load-balancer
    load-balancer-pool
    login
    network
    os-patch
    server
    site-to-site-vpn
    version
    wait
    webhook

```

**Logging into the CenturyLink account**

Using command without a configuration file:
```
clc-cli --v1-api-key xxxxxxxxxxxxxxxxx --v1-api-passwd xxxxxxxxxxxxx  Commands
```
```
clc login –user username –password
```
Or setup the configuration file as described in [Installation of CenturyLink Cloud CLI](#installation-of-centurylink-cloud-cli)

**Output Format**

For output (with --format for clc-cli or –-output for clc), there are several options:
‘JSON, TEXT, TABLE’, and 'csv'.

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
***Version for Support purposes***

**Show the current version**
```
clc version
```
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
**List all data centers**
```
clc-cli accounts locations
```
```
clc data-centers list
```

**List all servers in the account**
```
clc-cli servers list
```
```
clc server list
```

**For a particular data center**
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
**List hostname of all servers in a datacenter**
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

**All OS/templates available in a DC**
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

**Show Bare Metal Server available in a DC**
```
clc data-center get-baremetal-capabilities --data-center CA1
```

**Show all “active” servers**
```
clc server list --all --filter status=active --output table
```

**Who/when created a server**
```
clc server list --all --filter name=CA3ABCDADM01 --query change-info.{created-by,created-date}
```

**Display power state and hostname**
```
clc-cli --cols Name PowerState --config config.ini servers list-all
```
```
clc server list --all --query details.{power-state,host-name}
```

**Display power state and Display Name**
For Windows command:
```
clc server list --all --query Display-Name,details | findstr "DisplayName PowerState"
```
In Linux:
```
clc server list --all --query Display-Name,details | grep -e DisplayName -e PowerState
```

**All paused servers (or started and stopped)**
For Windows command:
```
clc server list --all --query details.{power-state,host-name} --output text | find "paused"
```
For Linux or MacOSX:
```
clc server list --all --query details.{power-state,host-name} --output text | grep "paused"
```

**Server name with number of CPUs and memory (in MB)**
```
clc server list --all --query "details.{cpu,memoryMB,host-name}" --output text
```

**Find IP addresses with server name**
```
clc-cli -f text --cols Name IPAddress --config.ini servers list-all
```
```
clc server list --all --query "details.{host-name,ipAddresses}" --output text
```

**List all groups**
```
clc-cli group list
```
```
clc group list –all
```

**Find all empty groups**
```
clc group list --filter 'servers-count=0'
```

**Find all groups with servers**
```
clc group list --filter 'servers-count>0'
```

**List all network in a datacenter**
```
clc-cli networks list --location ca3
```
```
clc network list --data-center ca3 --output table
```
**Query the above result with Name, Description and Gateway**
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
**Get billing for a group**
```
clc group get-billing-details --group-name Test
```
*Output contains:*

*ArchiveCost, CurrentHour, MonthToDate, MonthlyEstimate, TemplateCost*

**Get Billing for a server**
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

**From a Master account to look in a sub-account**
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

**List group and server in a specific account**
```
clc-cli groups list --alias ABCD
```
```
clc group list –account-alias ABCD
```
```
clc server list –account-alias ABCD
```
**List shared load balancer and load balanced pool**
```
clc load-balancer list --data-center ca2
```
```
clc load-balancer-pool list --data-center ca2 --load-balancer-name CLITest
```
**List all cross data center firewall rule for an account or data center**
```
clc crossdc-firewall-policy list --destination-acount-alias XXXX
```
```
clc crossdc-firewall-policy list --data-center CA1
```

### Commands change the environment
(**Warning**: use with care)

***Create***

**Create a user**
```
clc-cli users create --alias ABCD --user "new.test" --email new.test@abcd.com --first-name new --last-name test --roles AccountViewer
```
*Possible roles: ServerAdministrator,BillingManager,DNSManager,AccountAdministrator,AccountViewer,NetworkManager,SecurityManager,ServerOperator*

**Create a group**
```
clc-cli groups create --location CA3 --alias ABCD --parnet DevOps --group TestingCLI --description "Testing group"
```
```
clc group create --name "TestCA3" --description "Test Servers" --parent-group-name "CA3 Hardware"
```

**Create a server**
```
clc-cli servers create --alias ABCD --location CA3 --group TestingCLI --name test1 --template UBUNTU-14-64-TEMPLATE --backup-level Standard --cpu 1 --ram 1 --network vlan_771_10.xxx.yyy
```
```
clc server create --name test1 --description "test" --group-name TestingCLI --template-name UBUNTU-14-64-TEMPLATE --root-password xxxxxxxxx
--network-name vlan_771_10.xxx.yyy --cpu 1 --memory-gb 1 --type standard --storage-type standard --additional-disks sizeGB=50,type=raw
```

**Create a bare metal server**
```
clc server create --name test1 --group-name "My Test" --root-password xxxxxxxxx --network-name "vlan_1000_10.xxx.yyy" --type bareMetal --configuration-id 2516e341b960652f01563933d72523d9c222a437 --os-type windows2012R2DataCenter_64Bit
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
**Create a new Shared Load Balancer in a datacenter (initially disabled)**
```
clc load-balancer create --data-center CA2 --name WebStore --description "For online store" --status disabled
```
Output:
```
{
    "Description": "For online store",
    "Id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "IpAddress": "www.xxx.yyy.zzz",
    "Name": "WebStore",
    "Pools": [],
    "Status": "disabled"
}
```
**Create a new Load Balacner Pool**
```
clc load-balancer-pool create --data-center ca2 --load-balancer-name CLITest --port 80 --method roundrobin --persistence standard

```
**Adding servers in the load balanced pool**
```
clc load-balancer update-nodes --data-center CA2 --load-balancer-name CLITest --pool-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx --nodes "ip-address"="10.xxx.yyy.zzz","Private-Port"=443 "ip-address"="10.xxx.yyy.zzz","Private-Port"=443,"Status"=disabled


```
***Delete***

**Delete a server**
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
**Delete a Load Balanced pool**
```
clc load-balancer-pool delete --data-center CA2 --load-balancer-name CLITest --pool-id xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Advanced Usage
**Wait**
The option allows the previous command finishes before running the next command
```
clc wait
```
**Execute a package**
CLI can execute a script or package (requires package ID and parameters for executing the package)
Package ID can be found using:

- [API](//www.ctl.io/api-docs/v1/#blueprint)

- UUID (Package ID) as part of the URL under the control portal (Orchestration->scripts/package->script_required)(example: https://control.ctl.io/Blueprints/Packages/Details?uuid=c3c6642e-24e1-4c37-b56a-1cf1476ee360&classification=Script&type=AccountLibrary)

```
clc server execute-package --server-ids CA2ABCDMYSQLU01 --package "package-id=fcddbdf6-f5cc-4038-a088-b4e572ae2e22,parameters=xxxx yyyy"
```
### Network/Firewall
**Adding a public IP address to a server**

  - NATing with an existing private IP with UDP port 4040 open
  ```
  clc server add-public-ip-address --server-name CA3ABCD2TSQL01  --internal-ip-address 10.110.23.16 --ports port=4040,protocol=udp
  ```
  - Nating with a new private IP with TCP port range 8080 to 8090 open
  ```
  clc server add-public-ip-address --server-name CA3ABCD2TSQL01 --ports port=8080,portTo=8090,protocol=tcp
  ```
  - Update a public IP port and source IP restriction
  ```
  clc server update-public-ip-address --server-name CA3ABCD2TSQL01 --public-ip xxx.xxx.xxx.xxx --ports port=8080,portTo=8085,protocol=tcp --source-restrictions "CIDR=xxx.xxx.xxx.xxx/32"
  ```
  - Update a public IP port and define **multiple** IP restrictions
  ```
  clc server update-public-ip-address --server-name CA3CCVANET4701 --public-ip xxx.xxx.xxx.xxx --ports port=8080,portTo=8085,protocol=tcp --source-restrictions "CIDR=xxx.xxx.xxx.xxx/32" "CIDR=xxx.xxx.xxx.xxx/24"
  ```

**Adding a secondary network card on a server**
Please refer to the [Add or Remove Network Interface to Server using Go CLI](../Network/add-or-remove-network-interface-to-server-using-go-cli.md)

**Create firewall rule with port tcp/22 between VLANs**
```
clc firewall-policy create --data-center CA1 --destination-account abcd --sources "10.aaa.bbb.0/24" --destinations "10.xxx.yyy.0/24" --ports tcp/22
```
**Create a cross DC firewall policy with the same or sub account(initially disabled, can be enabled using update option)**
```
clc crossdc-firewall-policy create --data-center CA2 --destination-account-id abcd --destination-location-id va1 --destination-cidr "10.aaa.bbb.0/24" --source-cidr "10.xxx.yyy.0/24" --enabled false
```
### Snapshot
**Create a snapshot for a server (maximum 10 days expiration)**
```
clc server create-snapshot --server-ids CA3ABCDTAKE02 --snapshot-expiration-days 2
```
**Find the snapshot ID**
```
clc server get --server-name CA3ABCDTAKE02 --query details.snapshots.id --output text
```
**Delete a snapshot from a server**
(Snapshot ID can be retrieved from `clc server get` command)
```
clc server delete-snapshot --server-name CA3ABCDTAKE02 --snapshot-id 1
```
### Site to Site VPN
**Create Site to Site VPN**
```
clc site-to-site-vpn create --local "alias=CA2,subnets=10.x.x.0/24" --remote "siteName=NH,deviceType=pfsense,address=76.x.x.x,subnets=192.168.1.0/24" --ipsec "encryption=aes128,hashing=sha1_96,protocol=esp,pfs=group2,lifetime=28800" --ike "encryption=aes128,hashing=sha1_96,diffieHellmanGroup=group2,preSharedKey=b7fd0390436a4556a17c42f79d782eb9,lifetime=28800,mode=main,deadPeerDetection=false,natTraversal=false,remoteIdentity=false"
```
### Scripting
**Create a json file for repeat usage of frequent use commands**

For the example below, servername.json is created to list all the hostname of all servers in the account:
```
clc server list --all --query details.host-name --generate-cli-skeleton > servername.json
```
To use the file,
```
clc server list --from-file servername.json
```

### Application Services control
Relational Database Service,Intrusion Prevention Service, Patching Service and Simple Backup Service can be managed from the GO based CLI.  
The following examples show the basic functions of what can be done from the CLI.

### Relational Database Service
For Relational DB, cli can manage creation, deletion, failover, notification and listing of different resources.  The `--help` option can be used to find out more on the options.  For details of Relational Database Service, please see this [knowledge article](../Database/rdbs-mysql-getting-started.md).

**Listing all the available data centers for this service**
```
clc db list-datacenters
```
**Listing database instances in a data center**
```
clc db list --data-center IL1
```
**Querying the ID of the database**
```
clc db list --data-center VA1 --query ID --output text
```
**Creating a new database with replication**
```
clc db create --instance-type MYSQL_REPLICATION --external-id yourdb --machine-config "cpu=1,memory=2,storage=15" --backup-retention-days 5 --users "name=admin,password=XXXX" --data-center IL1
```
Once created, an output similar to below would include the IP address, the certificate and a summary of the configuration:
```
{
    "BackupRetentionDays": 2,
    "BackupTime": "0:0",
    "Backups": null,
    "Certificate": "-----BEGIN CERTIFICATE-----\xxxxxxxxxxxx\n-----END CERTIFICATE-----",
    "ExternalId": "yourdb",
    "Host": "yourdb.il1.rdbs.ctl.io",
    "Id": 3185,
    "InstanceType": "MySQL",
    "Instances": null,
    "Location": "IL1",
    "OptionGroup": "",
    "ParameterGroup": "",
    "Port": XXXXX,
    "Servers": [
        {
            "Alias": "IL1DBXXXXXXX",
            "Attributes": {
                "INTERNAL_IP": "xx.xx.xx.xx"
            },
            "Connections": 362,
            "Cpu": 1,
            "Id": XXXX,
            "Location": "il1",
            "Memory": 2,
            "Storage": 10
        }
    ],
    "Status": "Configuring",
    "Users": [
        {
            "name": "admin",
            "password": "XXXX"
        }
    ]
}
```
**Create notifications (options are 'CPU_UTILIZATION' or 'MEMORY_UTILIZATION'
or 'STORAGE_UTILIZATION' to email or SMS) for the database instance**
```
clc db create-notification  --subscription-id 3185 --destination-type SMS --location xxxxxxxxx --notifications NotificationType=MEMORY_UTILIZATION
```

### Intrusion Prevention Service
For details of Intrusion Prevention Service, please see [here](../Security/getting-started-with-ips.md).

**Install Intrusion Prevention Service on a host** (`uninstall` to uninstall)
```
clc ips install --server-name CA3ABCDTAKE02
```
**Set the notification (options: Webhook, Slack, syslog and Email) with email**
```
clc ips set-notifications --server-name CA3ABCDTAKE02 --notification-destinations '"type-code"="EMAIL","email-address"="monitor@abcd.com"'
```

### Patching Service
With patching, it is part of patching best practice to have roll back plan.  This can be done via a snapshot, in case of bad patch or application issue, it can be reverted quickly.  
**Patching a server (either Windows2012 or RedHat):**
```
clc os-patch apply --server-ids CA3ABCDTAKE02 --os-type Windows2012
```
**List the patching status or result:**
```
clc os-patch list --server-name CA3ABCDTAKE02
```
**Sample outputs**
Patching is running:
```
[
    {
        "End_time": "",
        "Execution_id": "CA3-XXXXX",
        "Init_messages": [
            {
                "End_time": "",
                "Init_begin_message": "Invoking SUS API",
                "Init_end_message": "",
                "Start_time": "2016-04-05 04:14:14"
            }
        ],
        "Start_time": "2016-04-05 04:14:10",
        "Status": "RUNNING"
    }
]
```
Completed patching output:
```
[
    {
        "End_time": "2016-04-05 04:34:14",
        "Execution_id": "CA3-XXXXX,
        "Init_messages": [
            {
                "End_time": "2016-04-05 04:34:12",
                "Init_begin_message": "Invoking SUS API",
                "Init_end_message": "Update Process Complete. There are 0 update
s to install",
                "Start_time": "2016-04-05 04:31:51"
            },
            {
                "End_time": "2016-04-05 04:28:11",
                "Init_begin_message": "Invoking SUS API",
                "Init_end_message": "Updates Downloaded Successfully downloaded
4 updates to install##https://support.microsoft.com/en-us/kb/3127231 https://sup
port.microsoft.com/en-us/kb/3122660 https://support.microsoft.com/en-us/kb/30987
85 https://support.microsoft.com/en-us/kb/3135998##",
                "Start_time": "2016-04-05 04:25:15"
            },
        ],
        "Start_time": "2016-04-05 04:14:10",
        "Status": "COMPLETED"
    }
]
```
**Review of the a patching execution**
```
clc os-patch list-details --server-name CA3ABCDTAKE02 --execution-id CA3-XXXXX
```
**Sample Output:**
```
{
    "Begin_message": "Update Process BEGIN",
    "Duration": "20m 4s",
    "End_message": "Updating Complete",
    "End_time": "2016-04-05 04:34:14",
    "Execution_id": "CA3-XXXXX",
    "Patches": [
        {
            "End_time": "2016-04-05 04:28:26",
            "Patch_begin_message": "Installing Security Update for Microsoft .NE
T Framework 4.6 and 4.6.1 for Windows 8.1 and Server 2012 R2 for x64 (KB3135998)
",
            "Patch_end_message": "Result Code: 2",
            "Start_time": "2016-04-05 04:28:26",
            "Status": "COMPLETED"
        },
                      .
                      .
                      .
        {
            "End_time": "2016-04-05 04:16:32",
            "Patch_begin_message": "Installing Update for Windows Server 2012 R2
 (KB3084905)",
            "Patch_end_message": "Result Code: 2",
            "Start_time": "2016-04-05 04:16:32",
            "Status": "COMPLETED"
        }
    ],
    "Start_time": "2016-04-05 04:14:10",
    "Status": "COMPLETED"
}
```
### Storage
Currently only works on MacOSX and Linux CLI, fixes for Windows version is pending:
**Adding a new 20GB disk to an existing server**
```
clc server update '{"ServerId": "CA3ABCDSVR01","Disks" : {"Keep" : [{ "DiskId": "0:0", "SizeGB": 1},{ "DiskId": "0:1", "SizeGB": 2},{ "DiskId": "0:2", "SizeGB": 16},{ "SizeGB": 20}]}}'
```
**Increase Disk 0:3 size to 40 GB**
```
clc server update '{"ServerId": "CA3ABCDSVR01","Disks" : {"Keep" : [{ "DiskId": "0:0", "SizeGB": 1},{ "DiskId": "0:1", "SizeGB": 2},{ "DiskId": "0:2", "SizeGB": 16},{ "DiskId": "0:3", "SizeGB": 40}]}}'
```
**Removing Disk 0:3 from the server (Backup data before removal)**
```
clc server update '{"ServerId": "CA3ABCDSVR01","Disks" : {"Keep" : [{ "DiskId": "0:0", "SizeGB": 1},{ "DiskId": "0:1", "SizeGB": 2},{ "DiskId": "0:2", "SizeGB": 16}]}}'
```

### Simple Backup Service
Simple Backup Service provides a set and forget backup solution to CenturyLink Cloud customers, to learn more, please refer to this [knowledge article](../Backup/simple-backup-service-how-it-works.md).  With CLI access to Simple Backup Service, it gives customers more management flexibility on managing their backup.

**Create a backup policy:**
```
clc backup create-account-policy --name CLICreated --os-type Windows --paths "c:\\users" e:\\" --excluded-directory-paths "e:\\temp" --backup-interval-hours 24 --retention-days 2
```
**Update an existing backup policy** (adding /data, excluding /data/tmp and changing interval to 48 hours, retention days cannot be changed)
```
clc backup update-account-policy --policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --name Linux-backup --os-type Linux --backup-interval-hours 48 --retention-days 7 --paths "/opt/local" "/usr/local" "/data" --excluded-directory-paths "/usr/local/tmp" "/data/tmp" --status ACTIVE
```
**Apply a policy to a server**
```
clc backup apply-policy --account-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --server-name CA3ABCDTAKE02 --storage-region CANADA
```
**Unapply a policy to a server**
```
clc backup unapply-policy --account-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --server-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
**Enable/Disable a policy on a server** (Status: ACTIVE/INACTIVE)
```
clc backup update-server-policy --account-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --server-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --status INACTIVE
```
**List various objects in Simple Backup Service**

***List of datacenters and storage regions***
```
clc backup get-data-centers
```
```
clc backup get-regions
```
***List of servers in a datacenter***
```
clc backup get-servers --data-center-name "CA3 - Canada (Toronto)"
```
***List of supported OS***
```
clc backup get-os-types
```
***List of available/applied policies in the account***
```
clc backup get-account-policies --account-alias ABCD
```
```
clc backup get-account-policy --policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
```
clc backup get-applied-account-policies --policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
```
clc backup get-applied-server-policies --server-name CA3ABCDTAKE02
```
```
clc backup get-allowed-account-policies --server-name CA3ABCDTAKE02
```
***List of restore points/data***
```
clc backup get-stored-data --account-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --server-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --search-date 2016-04-07
```
```
clc backup get-restore-point-details --account-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --server-policy-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  --backup-finished-start-date 2016-02-06 --backup-finished-end-date 2016-04-07 --sort-by retentionExpiredDate
```

### Utilization Report

CenturyLink Cloud stores the utilization report of a server for the past 14 days.  The statistics include CPU, Memory, Disk usage and Network.  There are three options of retrieving statistics:
- latest (returns a single data point that reflects the last monitoring data collected)
- hourly (returns data points for each sampleInterval value between the start and end times provided)
- realtime (returns data from the last 4 hours, available in smaller increments)

***Request a realtime statistics realtime from the Test group***
```
clc group get-monitoring-statistics --group-name Test --type realtime --start "2017-09-11 12:00:00" --sample-interval "01:00:00"
```
***Request statistics from September 1 to 7th in CSV format***
```
clc group get-monitoring-statistics --group-name Test --type hourly --start "2017-09-01 00:00:00" --end "2017-09-07 00:00:00" --sample-interval "01:00:00" --output csv
```
***Reuqest statistics realtime (last 4 hours) in 30 minutes interval***

### Webhook (only avaiable until version v1.1.0-rc.2)
CLI can be used to configure webhooks, this enable customers to leverage the alert notification webhook services built into CenturyLink Cloud with 3rd party web apps or services.  The current event list are: "Account.Created", "Account.Delted", "Account.Updated", "Alert.Notificiation", "Server.Created", "Server.Deleted", "Server.Updated", "User.Created", "User.Deleted", "User.Updated".  To learn more on setup webhook in CenturyLink Cloud, please see [Configuring Webhooks and Consuming Notificatios](../General/CenturyLinkCloud/consuming-webhook-alerts-with-3rd-party-web-apps.md).

***List all current webhook***
```
clc webhook list
```
***Create a new webhook notification***
```
clc webhook add-targeturi --event Server.Created --target-uri "https://zapier.com/hooks/catch/your-zpaier-id/"
```
***Delete an event notification***
```
clc webhook delete --event Server.Created
```
***Update and existing notification***
```
clc update --event Server.Deleted --recursive true --target-uri "https://zapier.com/hooks/catch/your-zpaier-id/"
```

### Support
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying any Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](//t3n.zendesk.com/tickets/new).
* For CLI bugs, please visit [CenturyLink Cloud CLI Github](//github.com/CenturyLinkCloud/clc-go-cli/issues) and [CenturyLink Cloud Python SDK](//github.com/CenturyLinkCloud/clc-python-sdk/issues)
