{{{
"title": "Cloud Platform - Release Notes: June 25, 2019",
"date": "06-25-2019",
"author": "Matthew Ordman",
"keywords":["lumen", "cam", "ams", "msa", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Public Cloud IaaS](https://www.ctl.io/cloud-platform/)

##### Windows 2019 unmanaged availability

Lumen Public Cloud Platform now offers the ability to create unmanaged Windows 2019 DataCenter Edition VMs. This is part of our ongoing efforts to improve the Lumen Public Cloud offerings.

#### SafeHaven

##### 5.2.0 release

The release includes:

* Enhancements on SafeHaven Replication Module (SBD)
* Fix for the bug which caused replication corruption for some environments.
* Improvements on SBD logs rotation to prevent accidental deletion of logs.
* Better handling of replication over unstable WAN network.
* Updated ansible version for automated installation of windows replication agent.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Terraform template boxes on Lumen Private Cloud on vCloud Foundation providers

Application Lifecycle Management now extends its Terraform template support to the provider types based on VMWare vCloud platform. In addition to the existing support for AWS, Azure, Google Cloud and Lumen Cloud provider types, both vCloud and Lumen Private Cloud on vCloud Foundation provider types will now be eligible for deploying a Terraform template box when configuring a Terraform deployment policy box.

#### [Managed Services Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/)

##### Support for CentOS and Ubuntu Operating Systems

Managed Services Anywhere now includes support for additional operating systems:  CentOS 6 & 7 and Ubuntu 14, 16 and 18.  Customers deploying these Operating Systems on MSA enabled providers, will now enjoy all the benefits of [Managed Services Anywhere](https://www.ctl.io/legal/cloud-application-manager/service-guide/) on those OSes.

### Announcements (2)

#### [Public Cloud IaaS](https://www.ctl.io/cloud-platform/)

##### Managed Backup

This communication is an important announcement regarding the end of sale for Lumen Cloud Managed Backup.

Effective today, 06/25/2019 Lumen Cloud Managed Backup is no longer available for purchase. There is no action necessary for current Lumen Cloud Managed Backup customers. The features and functionality of the Cloud Managed Backup offer will not change, and all existing subscriptions will still continue to function. You will not be able to add Managed Backup to new servers, but it can be removed from existing servers.

##### Windows 2008 Vulnerability

Microsoft announced CVE-2019-0708, a critical flaw in Remote Desktop Services that enables unauthenticated remote code execution in May.  As part our ongoing efforts to improve security and availability of all Lumen Cloud resources, we have patched Windows 2008 images so that all net new VM's will adhere to the latest updates.

In all cases, Lumen still recommends that you install the updates for this vulnerability as soon as possible on existing 2008 VM's. Where able, migrate applications to a newer version of Windows as Windows 2008 is going end of support Jan 2020. For responses to FAQs regarding Windows 2008 support please see [this Knowledge Base article](../../Support/windows-2008-end-of-vendor-support-faq.md).
