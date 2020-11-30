
{{{
  "title": "Deploy Microsoft BizTalk Server 2013 R2 Server on Windows",
  "date": "10/27/2015",
  "author": "Terawe",
  "attachments": [],
  "contentIsHTML": false
}}}
![](../../images/microsoft.png)

![](../../images/terawe.png)
### Technology Profile
BizTalk Server is a Microsoft Server product for integration and connectivity with a multitude of systems, applications and services. BizTalk Server 2013 is the eight major  release of this enterprise ready product that can aid organizations tremendously in connecting disparate systems inside and outside the organization. It provides numerous adapters and has a robust, durable, and scalable messaging infrastructure. In addition to integration capabilities, BizTalk also provides strong durable messaging, a rules engine, EDI connectivity, Business Activity Monitoring (BAM), Windows Azure connectivity and RFID capabilities.

### Description
This KB article describes the options for installing and configuring BizTalk 2013 R2 Server in a distributed topology on the Lumen Cloud using Blueprints.

The following software is installed by the BizTalk Server 2013 R2 Distributed Blueprint:

* Microsoft SQL Server 2012 Standard

* Microsoft BizTalk Server 2013 R2 Standard

* Microsoft Enterprise Single Sign on

The BizTalk Server 2013 R2 Distributed Blueprint will add the required Windows Server Roles to enable a server to host an Active Directory (AD) and Domain Name Server (DNS).

This Blueprint requires an existing server running Microsoft Windows 2012 R2 Datacenter Edition 64-bit.

#### Blueprint - BizTalk Server 2013 R2 Distributed
This Blueprint installs SQL Server followed by Enterprise Single Sign on and finally the BizTalk Server 2013 R2. Once the installs have completed, the BizTalk server is configured and a copy of the configuration command script is copied to the C:\Temp\ConfigureBTS.cmd for reference.

### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should be able to deploy a BizTalk Server 2013 R2 Distributed Blueprint on three existing servers running Microsoft Windows 2012 R2 Datacenter Edition 64-bit.

### Prerequisite
Access to the Lumen Cloud platform as an authorized user.

#### Steps to Deploy Blueprint
1. Provision three new servers using the steps below.
   * Login to the Control Portal. From the Nav Menu on the left, click **Create > Server**.
   * Set 'data center', 'group member of', 'operating system', 'server name', 'description', 'admin/root password' and 'confirm password'.
   * Set 'cpu', 'memory' and 'network'.
   * Then click the `create server` button.
   * This will kick off the server provisioning process and load a page to allow you to track the progress.

Note: the server names should indicate the role the server will assume.

2. Locate the BizTalk Server 2013 R2 Distributed Blueprint.
   * From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Locate and click on the 'BizTalk Server 2013 R2 Distributed' Blueprint.
   * Click the `deploy blueprint` button.

3. Customize the Blueprint.
   * Set the AD/DNS Server properties for the AD/DNS server.
      * 'Execute on Server' - set to the provisioned AD/DNS server name
      * 'Execute on Server' - set to the provisioned AD/DNS server name
      * 'Domain Name'  - set to your domain name
      * 'Net BIOS Name' - set to your domain Net BIOS name
      * 'Safe Mode Admin Password' - set to your domain administrator password
      * 'Confirm Safe Mode Admin Password' - set to your domain administrator password

   * Set the SQL Server properties for the SQL Server and Enterprise Single Signon server.
      * 'Execute on Server' - set to the provisioned SQL/SSO server name
      * 'SA Password' - SQL System Administrators password
      * 'Confirm SA Password' - Confirm SQL System Administrators password
      * 'SQL Version' - '2012 Standard' or 'Enterprise'
      * 'Database Engine Services' - check this feature
      * 'Management Tools' - check this feature
      * 'Connectivity Components' - check this feature

   * Set the ENTSSO Server properties.
      * 'Execute on Server' - set to the provisioned SQL/SSO server name
      * 'Company Name' - set to your company name
      * 'User Name' - set to your name

   * Set the Join SQL/ENTSSO server to the domain.
      * 'Execute on Server' - set to the provisioned SQL/SSO server name
      * 'Domain Name' - Set to the new Domain Name
      * 'DNS Server Name' - set to the AD/DNS server name
      * 'DNS Primary IP Address' - set to the IP addres of the AD/DNS server
      * 'Domain Admin Password' - set to your domain administrator password
      * 'Confirm Domain Admin Password' - set to your domain administrator password

	4. Set the BTS Runtime server properties.
     * 'Execute on Server' - set to the provisioned BizTalk Runtime server name
     * 'Execute on Server' - set to the provisioned BizTalk Runtime server name
     * 'Company Name' - set to your company name
     * 'User Name' - set to your name
     * 'Execute on Server' - set to the provisioned BizTalk Runtime server name
     * 'Domain Name' - Set to the new Domain Name
     * 'DNS Server Name' - set to the AD/DNS server name
     * 'DNS Primary IP Address' - set to the IP address of the AD/DNS server
     * 'Domain Admin Password' - set to your domain administrator password
     * 'Confirm Domain Admin Password' - set to your domain administrator password

5. Review and Confirm the Blueprint.
   * Verify your configuration details.

6. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

7. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.

8. Configure BizTalk Server.
   * For information about installing and configuring BizTalk Server in general please see the following Microsoft documentation.
   * [Installation Overview for BizTalk Server 2013 and 2013 R2](https://msdn.microsoft.com/en-us/library/jj248688.aspx)
   * [Install BizTalk Server 2010 and BAM in a Multi-Computer Environment](http://social.technet.microsoft.com/wiki/contents/articles/1837.install-biztalk-server-2010-and-bam-in-a-multi-computer-environment.aspx)

### Access your BTS 2013 server
To access your BTS 2013 server from a computer outside the Lumen Cloud network use the OpenVPN client as specified here: [How To Configure Client VPN](https://www.ctl.io/knowledge-base/network/how-to-configure-client-vpn/)

### Pricing
The costs associated with this Blueprint deployment include Lumen Cloud infrastructure usage. Additional licensing costs may apply for Microsoft software, including Windows Server, BTS 2013 Server and SQL Server.

### Terawe
Lumen Cloud works with [Terawe](http://terawe.com), a Microsoft Cloud and Hosting partner, to provide new  cloud offerings to our customers for various Microsoft products.

Terawe is a software technology company that provides world-class sustainable solutions and services for customers. With key initiatives spanning industry verticals in education and hosting, along with in-depth expertise including Cloud, Data Platform, Mobility, Big Data and Business Intelligence, we create compelling solutions for customers at the highest efficiency and quality.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).

* For issues related to deploying the Terawe BTS Blueprints on Lumen Cloud please email
[support@terawe.com](mailto:support@terawe.com).
