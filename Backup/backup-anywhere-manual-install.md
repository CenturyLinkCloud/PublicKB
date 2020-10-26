{{{
  "title": "Simple Backup Anywhere Manual Install",
  "date": "11-6-2019",
  "author": "John Gerger",
  "keywords": ["api", "backup", "clc", "cloud", "portal", "sbs", "storage"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Simple Backup Anywhere

[Simple Backup Service](https://www.ctl.io/simple-backup-service/) provides file and folder level backups and restores. The service is integrated with the [Control Portal](https://control.ctl.io/) and is [API accessible](https://www.ctl.io/api-docs/v2/#simple-backup). That gives you flexibility and ease of use to configure and customize backup policies.

Simple Backup Anywhere extends Simple Backup outside of CenturyLink Cloud to allow users to backup and protect their workloads virtually anywhere outbound internet connectivity is available. Simple Backup Anywhere is available to all the versions of [supported operating systems on CenturyLink Cloud](../Support/supported-operating-systems.md).

### Simple Backup Anywhere Manual Installation Guide

The Simple Backup Agent can be installed manually, or scripted to be installed on multiple systems.

The backup agent can be downloaded from the following locations:

* Windows: https://s3.amazonaws.com/sbs-agent/sbs-windows-install.ps1
* Linux: https://s3.amazonaws.com/sbs-agent/sbs-linux-install.sh

Once downloaded the script needs to be moved to the server and executed. The script will prompt the user for required inputs, or they can be passed into the execution of the script as variables.

Required parameters to install the Simple Backup agent manually are:

* CenturyLink Cloud Account Alias to register the server under
* CenturyLink Cloud user name for the provided Account Alias (parent accounts will not work)
* CenturyLink Cloud password
* Hostname of the server

Inputs variables can also be passed into the instillation script as below if you want to script the install to multiple servers:
Linux-specific:
```
-a {ACCOUNTALIAS}
-u {USERNAME} (not needed if providing BEARER TOKEN)
-p {Password} (not needed if providing BEARER TOKEN)
-b {CLC_BEARER_TOKEN} (not needed if providing user name and password)
-s Use system hostname command
-h {HOSTNAME} (specify a different host identification name)
```
Windows-specific:
```
-ACCOUNTALIAS 		  {ACCOUNTALIAS}
-USERNAME     		  {USERNAME} (not needed if providing BEARER TOKEN)
-PASSWORD 		   	  {PASSWORD} (not needed if providing BEARER TOKEN)
-CLC_BEARER_TOKEN 	  {CLC_BEARER_TOKEN} (not needed if providing user name and password)
-USEHOSTNAME 			  Use system hostname command - use 'yes'
-HOSTNAME 			  {HOSTNAME} (specify a different host identification name)
```
