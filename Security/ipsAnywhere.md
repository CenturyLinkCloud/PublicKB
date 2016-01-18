{{{ "title": "IPS - CLI Install & Uninstall",
        "date": "1-11-2016",
        "author": "Client-Security",
        "attachments": [],
        "contentIsHTML": false,
        "sticky": false }}}

The IPS-API is a RESTful api.
IPS or Intrusion Prevention Service will require you to have two things:

* A server with Administration credentials.
* An account on the [CenturyLink Cloud Platform](https://www.ctl.io/)

### Supported Managed Operating Systems
Current supported operating systems can be found here [Operating System Support](../Security/supported-ips-oses.md)

### Install

Installs an IPS agent on your server. 
This server needs the ability to make an outbound cURL command over port 443.
This cURL command will pull down a script and install the IPS agent. 
The script will configure and activate the agent.
The agent will communicate with our security manager.
Billing subscription will be activated.

##### Structure

>curl https://api.client-security.ctl.io/ips/scripts/install.sh | CLC_USERNAME=your.clc.account CLC_PASSWORD=your.clc.password CLOUD_PROVIDER=your.cloud.provider HOST_NAME=your.host.name bash

##### Content Properties

| **Name**      | **Type** | **Description**                                    | **REQ.**|
|---------------|----------|----------------------------------------------------|---------|
|CLC_USERNAME   |String    |A valid username with CenturyLink                   |Yes      |
|CLC_PASSWORD   |String    |The CenturyLink password linked to above User       |Yes      |
|CLOUD_PROVIDER |String    |The value for your cloud provider                   |No       |
|HOST_NAME      |String    |Value for server/VM name                            |No       |

* Hostname will default to a cli command >hostname -f 

###### Cloud Provider Values

| **Name**      | **Description**                            |
|---------------|--------------------------------------------|
|CLC            |CenturyLink Cloud                           |
|CTL_DCC        |CenturyLink Dedicated Cloud Compute         |
|CTL_VPDC       |CenturyLink Virtual Private Data Center     |
|AWS            |Amazon Web Services                         |
|AZURE          |Microsoft Azure                             |
|OTHER          |Default value if none are submitted         |

### Uninstall

Uninstalls an IPS agent from your server.
This server needs the ability to make an outbound cURL command over port 443.
This will remove the IPS agent from your server.
Billing subscription will be inactivated.

##### Structure

>curl https://api.client-security.ctl.io/ips/scripts/uninstall.sh | CLC_USERNAME=your.clc.account CLC_PASSWORD=your.clc.password bash

##### Content Properties

| **Name**      | **Type** | **Description**                                    | **REQ.**|
|---------------|----------|----------------------------------------------------|---------|
|CLC_USERNAME   |String    |A valid username with CenturyLink                   |Yes      |
|CLC_PASSWORD   |String    |The CenturyLink password linked to above User       |Yes      |