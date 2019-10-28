{{{
  "title": "Managed Operating System - Frequently Asked Questions",
  "date": "10-29-2019",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

Here are a few frequently asked questions for our [CenturyLink Cloud Managed Operating System Services](//www.ctl.io/managed-services/operating-system/).

**What is included in the Managed OS service?**

CenturyLink’s Managed OS service helps you spend less time on the IT tasks that don’t contribute immediately to your daily goals. To this end, here are the tasks performed on your behalf with our Managed OS service:

* Vendor Management – CenturyLink maintains ownership and management responsibility for your OS, freeing you from managing OS-level functions, SPLAs and license keys.
* Access Management – We take responsibility for user policies, administration and password management enforcement.
* Configuration Management – We confirm the initial install and basic functionality using an OS image built on vendor-recommended best-practices and years of industry experience.
* Change Management – We provide access to OS-level change data performed by CenturyLink staff, along with robust ITIL-based internal change control.
* Patch/Update Management – With support available for all critical and vendor-recommended patches, we ensure only OS vendor-recommended patches are installed. Please see the [patching article](../Managed Services/managed-os-operating-system-patching-and-update-processes.md) for more details.
* Security – We secure the OS with industry-standard anti-virus protection, regular virus and malware signature updates, and additional OS-level hardening to mitigate risk.

**What is not included in the Managed OS service?**

It would be impossible to create an all-inclusive list of everything a product is not, but this section addresses some current or often-asked items.

* Backups are not a part of the Managed OS service, but backups have been an available feature on Standard and Premium storage for all virtual machines. Effective May 1, 2016, the backup features associated with Standard and Premium storage will be retired.  On this date, the data on your storage volumes will no longer be backed up by default. It is highly recommended that you make arrangements to activate [Simple Backup Service](../Backup/getting-started-with-simple-backup.md) for your Managed VMs.

**What do I pay for a managed VM?**

Customers pay for managed operating system and managed applications on an hourly  basis. For managed OS, customers pay the management charge whenever the server is powered on. Licensing fees continue whether the server is powered on or off.

For managed applications, customers pay the management charge for as long as the managed application is on the server (whether the server is powered on or off).

Please review the [cloud pricing catalog](//www.ctl.io/pricing) for the billing type of each managed product!

**How do I create a Managed VM?**

Please review the articles dedicated to:
* [making a new server a managed server](../Managed Services/created-a-managed-server-now-what.md)
* [converting an existing server to a managed server](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md)

**Why don’t I see an option for Managed OS in the CenturyLink Cloud Control Panel?**

We have discontinued the consumption of Managed OS from within the CenturyLink Cloud Control Portal. Existing CenturyLink Cloud users of this service may continue to use provisioned instances, but new customers of Managed OS must consume it as part of a [Managed Services Anywhere](//www.ctl.io/managed-services-anywhere/) package.

**What if I'm looking for Managed OS on other platforms?**

Managed OS is just one of many services available with [Managed Services Anywhere](//www.ctl.io/managed-services-anywhere/).

**What are the network requirements for making a managed vm?**

In order for the Make Managed blueprint to succeed, the server in question has to be able to connect to an api endpoint, as well as the internal network specific to the Managed Server service in a given datacenter. If the blueprint fails due to an error indicating a network issue, customers should check the firewall settings on the server they want to make managed, making them more permissive to allow the blueprint to complete successfully. You can work with the Managed Services team to have firewall settings configured as desired after a successful conversion.

Additionally, if a customer has a Cloud Network Service set up, and the server they would like to make managed is in a vlan that is part of this configuration, we will need to assist with updating the configuration to allow traffic from the management network over this connection. Submit a ticket to help@ctl.io with details of both the blueprint error and the Cloud Network Service connection and our engineers will be happy to assist.

**Is there anything that I cannot do in the Control Portal with a managed VM?**

A managed server cannot be cloned, archived, or converted to a template. You cannot restore a managed server as an unmanaged server. Also, the "time to live" option is not available when creating a new managed server. At this time, you cannot create a managed server within a Cloud Blueprint.

**How do I log into my server?**

To access your managed VM, you will need your Local Account server name and password, unless you have created a Managed Active Directory Domain or are using a CenturyLink Shared Active Directory Domain.

The Local Account user name is the full server name, and the password credential is available in your CenturyLink Cloud Control Portal using the “*click to authenticate*” link on the server overview page. **Please note that the user name and password for your Server is not the same user name and password for the Cloud Control Portal.**

Once you have obtained your password, you may access Windows environments using Remote Desktop and RHEL environments using SSH. For more detailed information about accessing your server for the first time, please see the articles for [Windows Server](managed-windows-server-connecting-to-your-server-with-remote-desktop.md) or [RHEL](managed-red-hat-connecting-to-your-server-with-ssh.md).

**What should I do if I have trouble connecting via Remote Desktop?**

If you have difficulty connecting via RDP, be sure you are connecting from an IP that has TCP Port 3389 allowed on the <em>inbound</em> firewall. If you have a firewall at your location, you will need to have TCP port 3389 opened for *outbound* traffic. The firewall rule-set can be reviewed with your primary CenturyLink order contact or Consulting Engineer. Note that you should NEVER manage your remote servers through public IP address, and ONLY access servers through a secure tunnel like client VPN or site to site VPN!

If you connect and find that the system disconnects you immediately, you should ensure you are using the latest Remote Desktop client and that your client machine is fully patched. For additional support, please contact the Client Service Center at 1-888-638-6771 and choose menu option 2.

**How can I have my VM patched?**

An important component of OS administration and management is keeping the system up-to-date. Please see the [patching article](../Managed Services/managed-os-operating-system-patching-and-update-processes.md) for more details.

**How can I transfer files to my server using Remote Desktop?**

Files can be transferred by simply drag and drop in Windows Explorer from your remote desktop session.

* Configuring Remote Desktop for files transfer:
* Run Remote Desktop Connection (Start Menu/All Programs/Accessories).
* Enter the IP Address of the server.
* Click Options, then select Local Resources tab.
* Under Local devices and resources, click on More…
* Click on the “+”next to Drives, then select the local drive on your client which you would like to copy files from.
* Click Ok when done.
* Click Connect to initiate the connection.
* After connection is established, in your remote desktop session, open Windows Explorer (Start Menu/All Programs/Accessories)
* Local drive will show as Driver Letter on Hostname format, e.g. C on MyPC, process to copy files to or from your local drive

**Who do I contact if I have trouble with my Managed VM?**

The CenturyLink Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at the numbers below, or send email to request@centurylink.com for Managed OS issues. If there is an incident, email can be sent to incident@centurylink.com.

* US: 888.638.6771
* UK: +44.118.322.6100
* Singapore: +65.6305.8099

**How is Managed Support different than Platform Support?**

Your [Platform support](https://www.ctl.io/support/) options are distinct from Managed Support for a variety of reasons. You will find that public, platform support handles issues below the Operating System layer and some form of it is provided, regardless what flavor you choose, regardless what data center you choose. However, Managed Support is provided at your option within specific data centers for specific Operating Systems and Applications on CenturyLink Cloud (as well as other managed hosting products in the broader [CenturyLink Product Catalog](http://www.centurylink.com/business/enterprise/). Different teams with different skills sets are required and different methods are employed by each team.

The contact methods described above will connect you with the Managed Support teams as quickly as possible. If you contact the NOC for an issue regarding a Managed Server that is not related to the platform, you will be politely asked to use the aforementioned contact methods. If you wish to contact the Managed Support team for a platform issue, please review this [support article](../Support/how-do-i-report-a-support-issue.md) for guidance.

**How can I remove Managed Services from a VM?**

Currently, the only way to remove Managed Services from a VM once it has been deployed is to delete the VM and to create a new server that is unmanaged. This process should be followed for managed operating systems as well as for managed applications.

**How can I tell my _managed_ VMs from my _unmanaged_ VMs in the CenturyLink Cloud Control portal?**

Managed VMs will be noted with a green CenturyLink logo in front of the server name. This notation is intended to make it easier to locate managed VMs from within a list of all Cloud VMs you have created.

**My VM shows under construction in Control, but shows that the build has completed successfully?**

On Managed VMs, there are additional tasks that is being processed in the background in order to fully integrate into the Managed system, once this is complete Control will reflect it as active and manageable. Please see the following articles for additional details:

* [making a new server a managed server](../Managed Services/created-a-managed-server-now-what.md)
* [converting an existing server to a managed server](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md)

**What are the shared CenturyLink Managed Active Directory Domains?**

CenturyLink has two shared Managed Active Directory environments, one of which your server will be joined to when it goes through the "Make Managed" process if you don't specify a customer-owned Managed Active Directory domain for it to join.  The two shared Managed Active Directory domains are named <em>na.msmps.net</em> and <em>cadmi.net</em>.

**Can I join Managed Servers to my own domain?**

Yes, customers may elect to join a Managed Server to their own domain instead of a CenturyLink Shared Active Directory Domain.  As a pre-requisite to joining Managed Servers to a *dedicated* customer domain, you must first deploy [Managed Active Directory](getting-started-with-managed-active-directory.md) in the CenturyLink Cloud.

**Can _unmanaged_ Servers be converted to _Managed_ (or vice versa)?**

Servers **can** be converted from unmanaged to managed by executing the "Managed RHEL for CPI" (for Red Hat servers) or "Managed WIN for CPI" (for Windows servers) Blueprints in the library. Customers **cannot** go from a managed server to an unmanaged server.

**What Anti-Virus is provided for Windows Servers and how often is it updated?**

McAfee 5.02 is the default, standard Anti-Virus for Managed Windows Servers and is updated daily. Any managed servers with Windows OS deployed prior to November 21, 2015 use an older version. If you would like to use a different Anti-Virus, please contact your CenturyLink sales representative to discuss Advanced Services.

**How do I Set Get Anti-Virus on a Managed RedHat Server?**

Anti-virus is not standard for Managed RHEL. Please contact your CenturyLink sales representative to discuss Advanced Services.
