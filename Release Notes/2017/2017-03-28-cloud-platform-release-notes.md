{{{ "title": "Cloud Platform - Release Notes: March 28, 2017", "date": "3-28-2017", "author": "Marco Paolillo", "attachments": [], "contentIsHTML": false }}}

### Enhancements (5)

* __Cloud Application Manager__

  * Deployment Policy and Script boxes support for Microsoft Azure Provider

    Currently, the Microsoft Azure ARM provider allows users to deploy infrastructure and cloud native services using Microsoft Azure templates. With this enhancement, users can create Deployment Policies and run Script boxes on infrastructure provisioned using Microsoft Azure Provider. The new feature lets you deploy virtual machines (VMs) using the deployment policy boxes.

    In order for you to leverage the new feature, you have to synchronize the Azure ARM provider. After the synchronization is complete, the Configuration tab will list all the operating systems that can be deployed.

  * Workspace Dashboard View

    A new Dashboard view was added that provides real-time information about the workspace, such as instances deployed, boxes, providers and team members that are collaborating.

    In addition, you can monitor provider usage and lifecycle events, and make a search based on the date of the events.


  * Renaming of Microsoft Azure Provider

    As you are aware, Cloud Application Manager supports both Azure Classic and Microsoft Azure as providers. Starting ​3/28/2017​, you will see a change in how they are identified within Cloud Application Manager. We are making this change to be consistent with the language Microsoft uses to communicate with their customers


  * Dependency on Lumen Cloud for Microsoft Azure Customers

    For users who are interested in signing up a new Microsoft Azure account as part of the Lumen Reseller Program, starting ​3/28/2017​, you are no longer required to key-in your Lumen Cloud credentials. That requirement has been removed. At the same time, going forward only ​Organization Administrators​ will have the ability to sign up for a new Microsoft Azure account from Lumen. If you are an Organization Administrator, you will continue to see an option to sign up for a new Microsoft Azure Account when you create a new ​Microsoft Azure​ provider.


  * Usage-based billing

    With the launch of Cloud Application Manager https://news.centurylink.com/news/centurylink-advances-multi-cloud-management-strategy-with-launch-of-cloud-application-manager​ we are also making changes to our billing model for the Application Lifecycle Management module (former ElasticBox core features). As communicated earlier, with the retirement of Developer edition, all customers get the “​enterprise edition​” features but have an option to buy either the Cloud edition (hosted version) or the Datacenter edition (appliance version). For the Cloud edition, we are moving from ​a per-user based​ model to​ a per-instance based​ model. For the Datacenter edition, we are moving from the ​per-user based model to ​a fixed cost​ model. Cloud Application Manager customers who have signed up after 2/28/2017, as communicated and published at www.ctl.io/cloud-application-manager/#Pricing​ and the change takes effect starting ​3/30/2017​.


  * Self-service ticketing Portal

    Starting ​3/30/2017​ you will have access to a self-service ticketing portal to open/view tickets with Lumen support. The new ticketing portal is our interface for managing tickets, alerts and changes for Cloud Application Manager, Managed Hosting and Dedicated Cloud customers. Your Cloud Application Manager credentials will allow you to single sign-on to the ticketing portal. You can also directly access the ticketing portal at https://managedservices.ctl.io/msp/oauth/login​ which will redirect you to provide your Cloud Application Manager credentials. Once authenticated, you will be logged-in to the ticketing portal. As always you can reach out to Lumen Support via phone and email as published here https://www.ctl.io/cloud-application-manager/support/



* __US-West Region for Object Storage now available__

   In order to bring access to Object Storage within closer proximity to our users preferred deployment region for infrastructure, the US-West region for object storage is now available. This region accompanies the US-East and Canada regions that are already available.

   For information on utilizing Lumen Object Storage via the Control Portal in this or other regions, please see: https://www.ctl.io/knowledge-base/object-storage/using-object-storage-from-the-control-portal/

   For information on utilizing Lumen Object Storage via APIs in this or other regions, please see: https://www.ctl.io/knowledge-base/object-storage/using-object-storage-via-rest-api-aws-sdk/


* __MySQL v5.7__

   Both the Database as a Service and the Managed Database products now support MySQL v5.7. This update includes security improvements as well as many other features described at: https://dev.mysql.com/doc/refman/5.7/en/mysql-nutshell.html


* __SafeHaven 4.0.1__

  * New Features and Enhancements

    * Introduce using Linux VMs as recovery proxy servers for protected Windows servers
    * Add support to 64bit Windows Server 2008 R1 with the conditions
      * Manual LRA installation only
      * Only support 64bit version
      * Requires Powershell v2
    * Enhanced hard quota managing policy for Local Cache protection groups
    * New Windows tool to report on amount of IOs for a given period
    * Improved support for MANUAL site
    * Improved E-Mail Reporting and Management
    * Enhanced WAN data replication performance
    * Add support for NAT (does not work with the hairpin problem)


  * Support Matrix

    * OS
      * Windows (64bit only): Windows2008R1, Windows2008R2, Win2012R1, Win2012R2
      * Linux (32bit and 64bit): RHEL (CentOS)-5/6/7, Ubuntu-12/14/16, openSUSE-11/13

    * Data Center Types
      * VMware vSphere
      * CLC
      * MANUAL

    * Data Protection Types
      * Local Replica
      * Local Cache

      * Limits of standard deployments (SRN on 2 CPUs, 4GB RAM)

|MAXIMUM OF ITEM | LIMIT	| COMMENTS |
|:------------------------------------------------ | :-----: | :--------------------------------- |
| Number of Sites per CMS |	8 |     |
| Number of SRNs per CMS	| 64 |     |
| Number of Disks attached to SRN as storage pools | 12	| CLC default limit of disks per VM is 15 |
| Number of Protected Disks (in protected VMs) per SRN | 20 |             |
| Number of Disks per Protected Windows Guest	| 16	| Maximum number of disks (including iSCSI LUNs) per Windows server is 32 |
| Total Storage per Windows Guest | 9TB	 | CLC default limit is 4TB |
| Total Storage per Linux Guest	| 9TB	 | CLC default limit is 4TB |
| Total Storage per SRN	 | 32TB	  | CLC default limit is 4TB |
| Number of Protection Group per SRN |	10 |	16 is the absolute limit
| Number of Protected VMs per SRN |	10 |      |
| Number of PGs per CMS |	320 |    |
| Number of Protected VMs per CMS |	320 |      |
| Capacity per Disk |	9TB |	CLC default limit is 1TB |
| Capacity per PG |	9TB |	GUI limits numbers to 9999GB |
| VMs per PG |	5 |        |
| Minimum number of CPU per protected Windows VM |	2 |	single core might work but might have problems in some cases |

  * Currently, CLC limits a VM to 15 disks, a total of 4TB capacity and a maximum of 1TB per disk capacity.
    * With [special requests](https://www.ctl.io/knowledge-base/support/submitting-custom-requests/) to the Custom Requests team, they can typically accommodate up to 12TB per VM with maximum individual disk capacity limited to 4TB.  
    * The CLC default limits might change in the near future.


  * Known Limitations

   * We do not support Windows VMs using E1000E NIC
   * Linux VM onboarding: we do not support the protected guest running on a different subnet from the SRN iSCSI IP.

  * Password Limitations

    * CMS root password: no constrains
    * SRN root password: ' (single quote) and ^ are legitimate Linux characters but not supported by SH-4.0. GUI will warn about it.
    * SafeHaven user password: no constrains
    * Windows Ansible password: not supporting " (double quote)
    * Email SSMTP password (#227): not supporting  # : = and   (space)
    * vSphere password (#420): password cannot have space at the beginning or the end.
    * CLC password: no constrains


  * Download Links

    * SHBase-4.0.1-Mar-20-2017.ova: OVA to be imported to private VMware vSphere envrionment as templates for SRN/CMS appliances - https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova
    * Debian Package for CMS/SRN: to be used in the installer or GUI to update from SH-4.0.0 - https://download.safehaven.ctl.io/SH-4.0.1/safehaven-4.0.1.deb
    * GUI Package: zip file containing the JRE, runs on any Windows platform - https://download.safehaven.ctl.io/SH-4.0.1/SafeHavenConsole-4.0.1.zip
       * SafeHavenClient.4.0.1_win32.jar: to replace existing SafeHavenClient.jar inside the already downloaded 4.0.0 GUI folder - https://download.safehaven.ctl.io/SH-4.0.1/SafeHavenClient.4.0.1_win32.jar

    * Windows Downloads:
      * Driver Installer - https://download.safehaven.ctl.io/SH-4.0.1/safehaven_windows_driver-4.0.1.exe
      * MakeStub.exe - https://download.safehaven.ctl.io/SH-4.0.1/MakeStub-4.0.1.exe

    * Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM - https://download.safehaven.ctl.io/SH-4.0.1/makestub_for_windows.sh
    * Linux Onboarding Script - https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4/linux-onboarding-releases/


* __MSSQL DBaaS Beta__

    The MSSQL DBaaS Beta program is now available in the following data centers: CA3, GB3, IL1, NY1, SG1, UC1 and VA1.
