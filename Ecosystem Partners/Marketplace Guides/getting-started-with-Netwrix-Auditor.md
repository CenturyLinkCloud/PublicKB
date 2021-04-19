{{{
  "title": "Getting Started with Netwrix Auditor",
  "date": "11-11-2015",
  "author": "Netwrix Corporation",
  "attachments": [],
  "contentIsHTML": false
}}}

![Netwrix logo](http://../../images/netwrix-logo.png)

### Partner Profile
Netwrix Corporation is the IT auditing company, providing software that maximizes visibility into who changed what, when, where and who has access to what. Over 6,000 customers worldwide rely on Netwrix to audit IT infrastructure changes and data access, prepare reports required for passing compliance audits and increase the efficiency of IT operations.

### Technology Profile
Netwrix Auditor is an IT auditing software that provides actionable audit data about who changed what, when and where and who has access to what. Netwrix Auditor helps organizations prevent security breaches caused by insider attacks, pass compliance audits with far less effort and expense, and keep tabs on what privileged users are doing in the environment. Netwrix Auditor enables auditing of the broadest variety of IT systems, including Active Directory, Exchange, file servers, SharePoint, SQL Server, VMware and Windows Server. It also supports user activity monitoring through video recording with search by metadata capabilities.

### Description
Through the Lumen Blueprint integration, Netwrix provides a solution to deploy and configure Netwrix Auditor platform.

For more information, please visit [Netwrix](http://www.netwrix.com/).

### Contact Netwrix
Phone: 1-949-910-9556 | Toll-free: 888-638-9749 ext 2812 | [Contact Us](https://start.netwrix.com/netwrix_auditor_blueprint.html)

### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Netwrix Auditor Blueprint on Lumen Cloud.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.

### Important Notes
* For full featured auditing we recommend to have the Microsoft Active Directory set up in the same VLAN as the deployed Netwrix Auditor Blueprint.
* The Blueprint is configured for minimal footprint with hardware configuration sufficient for evaluation. However, in production environments, we suggest extending resources to 2CPUs and 8GB RAM. Also data drive N: should be increased up to 2TB. In addition for adequate performance external MS SQL should be used.
* The Netwrix Auditor Blueprint comes with 20 days evaluation license. To apply for full licenses please [__fill in this form__](https://start.netwrix.com/netwrix_auditor_blueprint.html)

### Installing Netwrix Auditor
1. Search for "Netwrix Auditor" in the Blueprints Library.
2. Select "Netwrix Auditor 7 VAP Trial".
3. Click `deploy blueprint`.
4. Populate the resulting page.
5. Click `next: step 2`.
6. Click `deploy blueprint`.

Your blueprint will deploy in about 15 minutes. When you receive a confirmation email, you can then begin to config your Auditor software.

### First Steps in Configuration
1. If you wish to audit Active Directory, please join the Netwrix Auditor server into your AD domain and __after reboot login as the Domain Admin__.

2. Open Netwrix Auditor Administrative Console and configure Audit Database settings (located under "Audit Archive -> Audit Database") by clicking on “Configure” button
   * If you wish to use preinstalled SQL Express - Opt to use existing SQL instance (then click Next and OK several times). OR
   * If you prefer to use external instance of MS SQL with Native Reporting services enabled, please provide the details of your MS SQL server. (Due to limitations of MS-SQL use only NetBIOS domain names in SAMID format (NetBIOSdomainName\user).
   * In order to make Netwrix Auditor Self Audit data available in Netwrix Auditor Client (AuditIntelligence console) click: “Apply these Audit Database settings to all Managed Objects” and after a while videos would become available in Netwrix Auditor Client.

3. Configure Default Data Processing Account (located under "Settings-> Data Collection") Blueprint is preconfigured with local administrator as the current default. If you plan to audit AD, we recommend providing Domain Admin credentials here. (Use domain\user format).

4. If you wish to receive email notifications and alerts, please update Default SMTP settings in "Email Notifications" (located under "Settings-> Data Collection").

5. To change default location and retention settings of the file system component of the audit archive go to  "AuditArchive-> Long-Term Archive” and replace the default “N:\ProgramData\Netwrix Auditor\Data” with the desired location.

### Using Netwrix Auditor
Here is an example of [how to configure Managed Object for Active Directory](http://www.netwrix.com/download/QuickStart/Netwrix_Auditor_for_Active_Directory_Quick_Start_Guide.pdf#page=10).

* To get detailed information on Netwrix Auditor configuration and usage please refer to the [Netwrix Auditor Installation and Configuration Guide](http://www.netwrix.com/download/documents/Netwrix_Auditor_Installation_Configuration_Guide.pdf) and [Netwrix Auditor Administrator's Guide](http://www.netwrix.com/download/documents/Netwrix_Auditor_Administrator_Guide.pdf).

### Frequently Asked Questions

#### Where do I obtain my Netwrix License?
Existing Lumen Customers can contact their Account Representative for help obtaining a Netwrix license, or contact Netwrix directly:
* Web - [http://www.netwrix.com](https://start.netwrix.com/netwrix_auditor_blueprint.html)
* Phone: 1-949-910-9556 | Toll-free: 888-638-9749 ext 2812

#### Who should I contact for support?
* For issues regarding the Netwrix Auditor software, please contact Netwrix:
* Web - [http://www.netwrix.com](http://www.netwrix.com/support.html)
* For issues related to Lumen cloud infrastructure (VMs, storage, network, etc.), or if you experience a problem deploying the partner template, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new).
