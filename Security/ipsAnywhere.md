{{{ "title": "Install IPS Anywhere",
        "date": "1-11-2016",
        "author": "Client-Security",
        "attachments": [],
        "contentIsHTML": false,
        "sticky": false }}}

# IPS-API

The IPS-API is a RESTful api.
IPS or Intrusion Prevention Service will require you to have two things.
You will need a server with Administration credentials.
You will also need an account on the CenturyLink Cloud Platform [CenturyLink Cloud](https://www.ctl.io/)

## Install

Installs an IPS agent on the designated host. 
This host can be on any service provider with the ability to make a cURL command.
This cURL command will pull down a script and install the Intrusion Prevention Agent. 
It will also configure the agent to activate and be in contact with the manager.

##### Structure

>curl https://api.client-security.ctl.io/ips/scripts/install.sh | CLC_USERNAME=your.clc.account CLC_PASSWORD=your.clc.password CLOUD_PROVIDER=your.cloud.provider HOST_NAME=your.host.name bash

##### Content Properties

| **Name**      | **Type** | **Description**                                    | **REQ.**|
|---------------|----------|----------------------------------------------------|---------|
|CLC_USERNAME   |String    |A valid username with CenturyLink                   |No       |
|CLC_PASSWORD   |String    |The CenturyLink password linked to above User       |No       |
|CLOUD_PROVIDER |String    |The value for your cloud provider                   |No       |
|HOST_NAME      |String    |Value for server/VM name *                          |No       |

* Hostname will default to a cli command >hostname -f 

###### Cloud Provider Values

| **Name**      | **Type** | **Description**                            | **REQ.**|
|---------------|----------|--------------------------------------------|---------|
|CLC            |String    |CenturyLink Cloud                           |No       |
|CTL_DCC        |String    |CenturyLink Dedicated Cloud Compute         |No       |
|CTL_VPDC       |String    |CenturyLink Virtual Private Data Center     |No       |
|AWS            |String    |Amazon Web Services                         |No       |
|AZURE          |String    |Microsoft Azure                             |No       |
|OTHER          |String    |Default value if none are submitted         |No       |