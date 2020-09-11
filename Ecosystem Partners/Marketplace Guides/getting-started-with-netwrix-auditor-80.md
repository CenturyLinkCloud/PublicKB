{{{
  "title": "Getting Started with Netwrix Auditor",
  "date": "04-09-2016",
  "author": "Netwrix Corporation",
  "attachments": [],
  "contentIsHTML": false
}}}

![Netwrix logo](../../images/netwrix-logo.png)

### Partner Profile
Netwrix Corporation provides IT auditing software that delivers complete visibility into IT infrastructure changes and data access, including who changed what, when and where each change was made, and who has access to what. Over 150,000 IT departments worldwide rely on Netwrix to audit IT infrastructure changes and data access, prepare reports required for passing compliance audits, and increase the efficiency of IT operations. Founded in 2006, Netwrix has earned more than 70 industry awards and was named to both the Inc. 5000 and Deloitte Technology Fast 500 lists of the fastest growing companies in the U.S.

For more information, visit [Netwrix](http://www.netwrix.com/).

### Technology Profile
Netwrix Auditor is a visibility and governance platform that enables control over changes, configurations and access in hybrid cloud IT environments to protect unstructured data regardless of its location. The platform provides security analytics to detect anomalies in user behavior and investigate threat patterns before a data breach occurs.

Netwrix Auditor includes applications for Active Directory, Exchange, Office 365, Windows file servers, EMC storage devices, NetApp filer appliances, SharePoint, SQL Server, VMware and Windows Server. Empowered with the RESTful API and user activity video recording, the platform delivers visibility and control across all of your on-premises or cloud-based IT systems in a unified way.

### Description
Through the CenturyLink Blueprint integration, Netwrix provides a solution to deploy and configure Netwrix Auditor platform.

For more information, please visit [Netwrix](http://www.netwrix.com/).

### Contact Netwrix
Phone: 1-949-407-5125 | Toll-free: 888-638-9749 | [Contact Us](https://start.netwrix.com/netwrix_auditor_blueprint.html)

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Netwrix Auditor Blueprint on CenturyLink Cloud.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.

### Important Notes
* For full featured auditing we recommend to have the Microsoft Active Directory set up in the same VLAN as the deployed Netwrix Auditor Blueprint.
* The Blueprint is configured for minimal footprint with hardware configuration sufficient for evaluation. However, in production environments, we suggest extending resources to 2CPUs and 8GB RAM. Also data drive N: should be increased up to 2TB. In addition, for adequate performance external MS SQL should be used.
* The Netwrix Auditor Blueprint comes with 20 days evaluation license. To apply for full licenses please [__fill in this form__](https://start.netwrix.com/netwrix_auditor_blueprint.html)

### Installing Netwrix Auditor
1. Search for "Netwrix" in the Blueprints Library.
2. Select "Netwrix Auditor 8 BYOL".
3. Click `deploy blueprint`.
4. Populate the resulting page.
5. Click `next: step 2`.
6. Click `deploy blueprint`.

Your Blueprint will deploy in about 15 minutes. When you receive a confirmation email, you can then begin to config your Auditor software.

### First Steps in Configuration
1. Please join the Netwrix Auditor server into your AD domain and __after reboot login as the Domain Admin__.(__Note:__ You may note a "Unexpected Shutdown" upon login, this can be safely ignored.)

2. Open Netwrix Auditor Administrative Console and Select a Managed Object to configure such as Active Directory or Office 365.

3. You will then be prompted for information specif to each object.(__Note:__ If you did not provide your domain credetnatils during configuration you will need to change the Default Data Processing account under "Settings > Data Collection".)

4. Continue to follow the wizard.

5. Navigate to the "AuditArchive" in the Netwrix Auditor Adminstrative consle and slect the Link “Apply these Audit Database settings to all Managed Objects” in the Default SQL Server settings.

6. If you wish to receive email notifications and alerts, please update Default SMTP settings in "Email Notifications". (located under "Settings-> Data Collection".)

7. To change default location and retention settings of the file system component of the audit archive go to "AuditArchive-> Long-Term Archive” and replace the default “N:\ProgramData\Netwrix Auditor\Data” with the desired location.

### Using Netwrix Auditor
Here is an example of [how to configure Managed Object for Active Directory](http://www.netwrix.com/download/QuickStart/Netwrix_Auditor_for_Active_Directory_Quick_Start_Guide.pdf#page=10).

To get detailed information on Netwrix Auditor configuration and usage please refer to the [Netwrix Auditor Installation and Configuration Guide](http://www.netwrix.com/download/documents/Netwrix_Auditor_Installation_Configuration_Guide.pdf) and [Netwrix Auditor Administrator's Guide](http://www.netwrix.com/download/documents/Netwrix_Auditor_Administrator_Guide.pdf).

### Frequently Asked Questions

#### Where do I obtain my Netwrix License?
Existing CenturyLink Customers can contact their Account Representative for help obtaining a Netwrix license, or contact Netwrix directly:
* Web - [http://www.netwrix.com](https://start.netwrix.com/netwrix_auditor_blueprint.html)
* Phone: 1-949-910-9556 | Toll-free: 888-638-9749 ext 2812

#### Who should I contact for support?
* For issues regarding the Netwrix Auditor software, please contact Netwrix:
* Web - [http://www.netwrix.com](http://www.netwrix.com/support.html)

* For issues related to CenturyLink cloud infrastructure (VMs, storage, network, etc.), or if you experience a problem deploying the partner template, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new).
