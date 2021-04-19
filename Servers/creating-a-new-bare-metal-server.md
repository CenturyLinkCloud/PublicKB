{{{
  "title": "Creating a New Bare Metal Server",
  "date": "9-13-2017",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description
Creating a bare metal server on Lumen Cloud follows a similar flow as [creating a virtual server](../Servers/creating-a-new-enterprise-cloud-server.md), with a few exceptions. The steps below demonstrate how to provision new bare metal machines in the Lumen Cloud. For specifications on which capabilities are supported for bare metal servers as opposed to virtual machines, you may reference the [Server Comparison Matrix](../Servers/server-comparison-matrix.md) for details. For more information on Bare Metal servers in general, please refer to the [Bare Metal FAQ](../Servers/bare-metal-faq.md). 
**IMPORTANT.** Please take note of the section related to data security and recovery in the event of hardware failure in the FAQ's to ensure your achitecture proposal accounts for this when creating a Bare Metal server.

Once you've gone through this KB article and created a new server, you can follow this Getting Started guide to learn [how to securely connect to your new server.](../Servers/getting-started-how-to-securely-connect-to-your-server.md)

### Steps

1. To start the "Create Server" Process, use the **+** icon on the left side of the **Servers** area and choose **+ Server** to bring up the **Create Server** page.

  ![Create a New Bare Metal Server](../images/baremetal-create-2.png)

2. Just like for any server you create, you will first need to select the **data center** to deploy it to and a **group** to put the server in. Then, select the **Bare Metal** option (if it is available in the data center you selected).

  ![Create a New Bare Metal Server](../images/baremetal-create-3.png)

3. After selecting **Bare Metal**, you will be presented with a set of configuration options to choose from - each with a different mix of CPU, memory, and storage capacity. Simply click on the desired configuration (if it is available in the selected data center) to select it for provisioning.

  ![Create a New Bare Metal Server](../images/baremetal-create-4.png)

  You should also notice the warning message that appears regarding no backups or storage redundancy. Customers who require backups for Bare Metal servers should review our [Simple Backup Service](//www.ctl.io/simple-backup-service).

4. Now, choose the operating system for this server. Supported Operating systems are:
  * Windows 2012 R2 Standard Edition
  * Windows 2012 R2 Datacenter Edition
  * Red Hat Enterprise Linux 6
  * Red Hat Enterprise Linux 7
  * CentOS 6
  * CentOS 7
  * Ubuntu 14 LTS
  * Ubuntu 16 LTS

5. Next, you'll need to set the server name, description, and administrator password for this server, just as you do with any Lumen Cloud server. As usual, the name entered is part of a formatted name that is arranged as: **(data center name)** + **(account alias)** + **(user-provided server name)** + **(counter index)**. The administrator password will set the "Administrator" password in Windows or the "root" password in Linux.

  ![Create a New Bare Metal Server](../images/baremetal-create-6.png)

4. Finally, select the account network, primary DNS and secondary DNS for the server, the same as you would for any Lumen Cloud server.

  ![Create a New Bare Metal Server](../images/baremetal-create-7.png)

5. After the server has been provisioned, use the Server Details page to see the details of the server and perform actions on it.

  ![Create a New Bare Metal Server](../images/baremetal-create-8.png)
