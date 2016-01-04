{{{
  "title": "Getting Started with SoftNAS Cloud File Gateway - Appliance",
  "date": "12-29-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Technology Profile

<img src="../../images/softnas/softnas_logo.png" style="border:0;float:right;max-width: 150px;">

SoftNAS, LLC is a leading storage software company that provides Simply Powerful agile storage software that protects business data in the cloud.

SoftNAS is the #1 best-selling NAS in the cloud and believes that storage can be both powerful and frictionless, providing customers with the
enterprise-grade, software-defined NAS storage required to safely and reliably operate business-critical IT systems and applications in the cloud.

http://www.softnas.com


##### Customer Support

| Sales Contact  | Support Contact  |
|:- |:- |
| sales@softnas.com<br>(888) 801-7524 Option 1<br>&nbsp;  | support@softnas.com<br>(888) 801-7524 Option 4<br>[Support Web](https://www.softnas.com/wp/support/)  |


### Description

SoftNAS has integrated their Cloud File Gateway and NAS technology with the CenturyLink Cloud platform, publishing their virtual appliance as
a CenturyLink Cloud Partner Template. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid
time-to-value for this encryption solution.

For more information including whitepapers and data sheets, please view the product information and documentation on
[SoftNAS website](https://www.softnas.com/wp/support/documentation/).


### Solution Overview

SoftNAS Cloud is an enterprise-grade, full-featured cloud NAS filer and cloud storage gateway. Safely migrate business-critical applications to
the CenturyLink Cloud without a physical storage appliance. Quick and easy to deploy, any IT professional can install and configure SoftNAS in
minutes without specialized training. High-availability is included at no extra cost for CenturyLink Cloud users who deploy the two requisite instances.

SoftNAS Cloud runs as a Linux-based, 64-bit CentOS redistribution guest OS, treated as a VM in a virtual server environment. In many use cases, storage
devices are attached to the physical hardware layer, then presented to SoftNAS Cloud as a VM running Linux.

SoftNAS Cloud operates on an industry-standard Linux platform, and uses a derivative of the Zettabyte File System (ZFS). This makes SoftNAS Cloud able
to leverage many ZFS features and add layers of functionality for NAS solutions in virtual computing and cloud computing.

An Apache webserver provides robust, secure access along with Secure Shell (SSH). Storage is accessible via TCP/IP protocols including NFS v3,
NFS v4, SMB/CIFS (Microsoft Windows File Shares), and iSCSI.

SoftNAS Cloud is packaged with a primary administration interface called SoftNAS StorageCenter, which provides commercial-grade storage
administration and management functionalities for businesses of all sizes.

SoftNAS Cloud File Gateway is now available for CenturyLink Cloud Users to deploy to their account. The SoftNAS appliance comes with a free trial
that let's you use up to 100GB without having to purchase a license. In order to purchase a license or entitlement, please visit
https://www.softnas.com/wp/pricing/ or contact sales@softnas.com

### Key Features

* NFS, CIFS and iSCSI support
* Connects to popular Cloud Storage services
* 99.999% reliability with cross-zone high-availability with SNAP HA(tm)
* Cross-region block replication with SnapReplicate(tm)
* Active Directory integration
* Compression, deduplication, thin-provisioning
* Easy set-up and configuration wizards, intuitive admin interface (StorageCenter)


### Audience

CenturyLink Cloud Users, Storage Administrators, IT Managers


### Prerequisites

* Access to the CenturyLink Cloud platform as an authorized user
* control.ctl.io account with password authentication (two factor authentication not yet supported)


### Steps to Deploy a New SoftNAS Appliance

1. **Locate the Blueprint in the Blueprint Library**

 Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for "SoftNAS Appliance" in the keyword search on the right side of the page.

  <img src="../../images/softnas/blueprint_tile.png" style="border:0;max-width:250px;">

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="../../images/bpimager/deploy_parameters.png">

  * **Control User Password** - The password associated with your control.ctl.io login

4. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the **deploy blueprint** button. You will see the deployment details stating the Blueprint is queued for execution.

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive a number of emails.  The first will indicate the server has been deployed and the second will come a few minutes later once the appliance has been fully activated.  If you do not receive an email like the one shown below you may have had a deployment error - review the *Blueprint Build Log* to for error messages.

  <div style="float:left;width:45%;margin-left:1em;">
    *Email #1: Appliance deploy started*
    <img src="../../images/bpimager/appliance_deploy_started.png" style="border:0;width:100%;">
  </div>
  <div style="float:right;width:45%;margin-right:1em;">
    *Email #2: Appliance deploy complete*
    <img src="../../images/bpimager/appliance_deploy_complete.png" style="border:0;width:100%;">
  </div>
  <br style="clear:both;">

  Wait for the second email indicating your appliance is ready for use before attempting to access the resource.

8. **Accessing Your Appliance**

  1. Access your appliance by navigating to the server's private IP address with your web browser over https (e.g. https://youripaddress/).
  2. Login to the SoftNAS web console with the username `softnas` and password `Pass4W0rd`
  3. Follow the on-screen instructions to accept the SoftNAS user agreements and proceed to using the service. Documentation is available within the application, as well as a helpful checklist to get started.
  4. Add storage to the SoftNAS VM by using Control Portal
    * Navigate to the SoftNAS server in the Control Portal
    * Click on Edit Storage button
    * Add a Partition and size appropriately
    * Click the Save button
    * Wait for the storage to be added
  5. Login to the SoftNAS Cloud Gateway and configure the new storage.

  For more information on how to use the SoftNAS solution, please visit: [http://www.softnas.com/support/](http://www.softnas.com/support/)

9. **Allowing Access from Public Internet** (optional)

  [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for ports below:
  - For administrative access and use, open the following ports:
    * TCP Ports: 443
    * UDP Ports: 1
    * ICMP: All

  - For CIFS Sharing, open the following ports:
    * TCP 137, 138, 139, 445
    * TCP 389 for Active Directory
    * TCP 445 for NetBIOS Post-Windows 2000 (CIFS)
    * TCP 901 for SWAT

  - For NFS Sharing, open the following ports:
    * TCP 111, 2010-2014, 2049
    * UDP 111, 2010-2014, 2049

  - For iSCSI Sharing, open the following ports:
    * TCP 3260


### Pricing

The costs listed above in the above steps are for the infrastructure only.

After deploying this Blueprint, you may secure entitlements to the technology using the following steps:

 * Email: sales@softnas.com


### Frequently Asked Questions

**Where do I obtain my license?**

Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a SoftNAS license, or contact SoftNAS directly:
- Contact SoftNAS Sales via Email: [sales@softnas.com](mailto:sales@softnas.com)
- Contact SoftNAS Sales via Phone: 1-888-801-7524, Option 1


**Who should I contact for support?**

* For issues related to accessing the SoftNAS partner template, setup of devices, volumes, pools or high availability, or for any licensing concerns, please visit the SoftNAS Support Website: http://www.SoftNAS.com/support
* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).


**What components are included in the SoftNAS licensing or entitlements?**

Customers are provided access to the SoftNAS virtual Appliance and support service for the software.  Clients are still responsible for CenturyLink Cloud infrastructure services (compute, memory, storage, support etc) on top of the SoftNAS Licensing and support services.  These are not bundled with SoftNAS services or products.
