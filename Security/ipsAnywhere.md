{{{ "title": "IPS - CLI Install & Uninstall",
        "date": "02-19-2016",
        "author": "Client-Security",
        "attachments": [],
        "contentIsHTML": false,
        "sticky": false }}}

The IPS-API is a RESTful api.
IPS or Intrusion Prevention Service will require you to have two things:

* A server with Administration credentials.
* An account on the [CenturyLink Cloud Platform](https://www.ctl.io/)

For more information, please see the Prerequisites section on our [Getting Started](../Security/getting-started-with-ips.md) page.

### Supported Managed Operating Systems
Current supported operating systems can be found here [Operating System Support](../Security/supported-ips-oses.md)

### Install - Linux

Installs an IPS agent on your server. 
The server needs the ability to make an outbound cURL command over port 443.
The cURL command will download a script and install the IPS agent.
Running the install requires root privileges.
The script will configure and activate the agent. 
The agent will communicate with our security manager.
Billing subscription will be activated.

##### IPS Install Command

>curl https://api.client-security.ctl.io/ips/scripts/install.sh | sudo CLC_USERNAME=your.clc.account CLC_PASSWORD=your.clc.password CLOUD_PROVIDER=your.cloud.provider HOST_NAME=your.host.name bash

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

### Uninstall - Linux

Uninstalls an IPS agent from your server.
This server needs the ability to make an outbound cURL command over port 443.
Running the uninstall requires root privileges.
This will remove the IPS agent from your server.
Billing subscription will be inactivated.

##### IPS Uninstall Command

>curl https://api.client-security.ctl.io/ips/scripts/uninstall.sh | sudo CLC_USERNAME=your.clc.account CLC_PASSWORD=your.clc.password bash

##### Content Properties

| **Name**      | **Type** | **Description**                                    | **REQ.**|
|---------------|----------|----------------------------------------------------|---------|
|CLC_USERNAME   |String    |A valid username with CenturyLink                   |Yes      |
|CLC_PASSWORD   |String    |The CenturyLink password linked to above User       |Yes      |


### Install - Windows
Installs an IPS agent on your server via a PowerShell script.
The server needs the ability to make an outbound call over port 443.
The command will download a PowerShell script and install the IPS agent.
Running the install requires Administrative privileges.
The script will configure and activate the agent. 
The agent will communicate with our security manager.
Billing subscription will be activated.
Note: When the install completes, your RDP session may reset, at which time, you'll need to reconnect to your Windows VM.

##### IPS Install Commands

Command One

> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Command Two

> (New-Object System.Net.WebClient).DownloadFile("https://api.client-security.ctl.io/ips/scripts/install.ps1","$env:temp\install.ps1") ; cd $env:temp ; .\install.ps1 -controlUser "your.clc.account" -controlUserPassword "your.clc.password" -accountAlias "your.clc.account,alias" -cloudProvider "your.cloud.provider"

##### Content Properties

| **Name**      | **Type** | **Description**                                     | **REQ.**|
|---------------|----------|-----------------------------------------------------|---------|
|controlUser   |String    |A valid username with CenturyLink                     |Yes      |
|controlUserPassword   |String    |The CenturyLink password linked to above User |Yes      |
|accountAlias      |String    |Your CenturyLink account alias                    |Yes       |
|cloudProvider |String    |The value for your cloud provider                     |No       |


###### Cloud Provider Values

| **Name**      | **Description**                            |
|---------------|--------------------------------------------|
|CLC            |CenturyLink Cloud                           |
|CTL_DCC        |CenturyLink Dedicated Cloud Compute         |
|CTL_VPDC       |CenturyLink Virtual Private Data Center     |
|AWS            |Amazon Web Services                         |
|AZURE          |Microsoft Azure                             |
|OTHER          |Default value if none are submitted         |

### Uninstall - Windows

Uninstalls an IPS agent from your server.
This server needs the ability to make an outbound call over port 443.
Running the uninstall requires Administrative privileges.
This will remove the IPS agent from your server.
Billing subscription will be inactivated.
Note: When the uninstall completes, your RDP session may reset, at which time, you'll need to reconnect to your Windows VM.

##### IPS Uninstall Commands

Command One

> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Command Two

> (New-Object System.Net.WebClient).DownloadFile("https://api.client-security.ctl.io/ips/scripts/uninstall.ps1","$env:temp\uninstall.ps1") ; cd $env:temp ; .\uninstall.ps1 -controlUser "your.clc.account" -controlUserPassword "your.clc.password"

##### Content Properties

| **Name**      | **Type** | **Description**                                    | **REQ.**|
|---------------|----------|----------------------------------------------------|---------|
|controlUser   |String    |A valid username with CenturyLink                   |Yes      |
|controlUserPassword   |String    |The CenturyLink password linked to above User       |Yes      |

### Configuring IPS Notifications

Next step is to configure your IPS notifications. Please click [here](../Security/configuring-ips-notifications.md) for help with configuring your IPS notifications.
