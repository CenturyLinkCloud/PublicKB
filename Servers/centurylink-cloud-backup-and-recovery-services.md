{{{
  "title": "CenturyLink Cloud Backup Services",
  "date": "3-22-2016",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Table of Contents

* [Overview](#overview)
* [Audience](#audience)
* [Exclusions](#exclusions)
* [Simple Backup Service](#simple-backup-service)
* [Managed Backup](#managed-backup)
* [Marketplace Provider Program Partners](#marketplace-provider-program-partners)
* [Comparison Matrix](#comparison-matrix)

### Overview
Data is the lifeblood of any organization—and keeping that data safely backed up and accessible in the event of file corruption is crucial. On top of that, organizations have different data retention policies that govern how long certain types of information should be backed up and where it should be physically hosted.  Customers easily backup and restore data with a wide range of [CenturyLink Cloud](//www.ctl.io) and [Marketplace Provider Program Partners.](//www.ctl.io/marketplace/program/)

### Audience
* CenturyLink Customers

### Exclusions
* Disaster Recovery and Business Continuity Service Offerings

### [Simple Backup Service](//www.ctl.io/simple-backup-service/)
For servers running in the public cloud, Simple Backup Service offers the ultimate in reliability and convenience. Just point-and-click to create backup policies that meet your requirements, then apply them to servers in the CenturyLink Cloud.

From there, Simple Backup Service does the rest for you—data is automatically backed up in secure object storage and retained according to the policy. Restores are simple too—just click on a “point-in-time” backup event, and the data will be automatically restored within minutes.

**Peace of Mind Reliability & Security**
* The Simple Backup Service “just works”—backup operations are completely automated. Data is transferred from your server to secure object storage over the Internet. The backups are stored for as long as you specify.
* Restores are simple—just select the point-in-time backup you want to restore from, click and it’s done.
* Data in transit between the client and the backup infrastructure uses a secure TLS (transport layer security) connection. All backups are fully encrypted for storage and decrypted upon restore.

**Comply with Enterprise Data Retention Policies**
* Create and apply policies for data retention that match common corporate guidelines.
* Customize every aspect of your data backups—including location, frequency of backup, and retention period.
* Supports data sovereignty, with backup sites in the US, Canada, the EU and APAC.
* Store data for as long as required—days, month, or years.

**Flexible & Easy to Use**
* The Simple Backup Service is integrated with the Control Portal, and API accessible.
* Point-and-click to install the backup agent—no need to SSH or RDP to get started.
* Pay-as-you-go billing—estimates of charges for the service are included in the Control Portal as well.
* Keep backups efficient, by specifying only the file paths you need. Only files in those paths will be backed up. Configure folders to exclude as well.
* Supports both virtual machines and Bare Metal cloud servers on the CenturyLink Platform.

### [Managed Backup](//www.ctl.io/managed-services/backup/)
For workloads requiring advanced backup capabilities, CenturyLink offers Managed Backup services featuring Symantec NetBackup. Quickly provision servers with advanced backup features with a single click. The service includes: file and folder level backups and restores, encryption at rest, 2-week retention periods and replication to a secondary site.

Managed Backup is a superior alternative to many do-it-yourself options. Why? No significant work is required by users, no wasted spend on infrastructure, and no need to write any code or connect to APIs. In addition, there are no setup fees and no bandwidth charges for the service.

**Managed Backup Highlights**
* Self-Service: Upon creation of a server, or even after a server has already been provisioned, managed backup services can be turned on and off. The backup service runs automatically from there.
* Restore: Restores can be performed at the file and folder level. And data can be restored from any daily backup performed in the current 14 day window.
* Encryption: Data is encrypted at rest on backup infrastructure using the Blowfish algorithm.
* NetBackup Agent Access: Manage the details of your backups from the NetBackup agent, with restores available upon request.
* Digital Offsite Vaulting (“DOV”): Data is backed up at a secondary facility, offering geographic diversity for enterprise systems. Using DOV, data is transferred and retained at a CenturyLink data center different than where the data backup originated (this is done via a secure, private CenturyLink network connection). Customer data is retained on disk for two weeks, with other options available upon request.
* Supported Operating Systems:
  * Managed Microsoft Windows Server 2008 R2
  * Managed Microsoft Windows Server 2012 R2
  * Managed Red Hat Enterprise Linux 5
  * Managed Red Hat Enterprise Linux 6
  * Managed Red Hat Enterprise Linux 7
* [Available Locations](../General/CenturyLinkCloud/centuryLink-cloud-feature-availability-matrix.md)

### [Marketplace Provider Program Partners](//www.ctl.io/marketplace/program)
The CenturyLink Marketplace Provider Program is designed to provide additional value within CenturyLink’s enterprise cloud computing platform through partnerships with innovative cloud technology and service providers. By integrating their technology into CenturyLink Cloud, our technology partners can take advantage of a differentiated, digital route-to-market: presented as part of a enterprise-grade automation platform which powers one of the largest pools of IT infrastructure in the world.

**Marketplace Provider Program Partners Highlights**
* Bring Your Own License (BYOL)
* Customer implemented and Operated
* Complete control over the backup environment
* Leverage existing, proven technology deployed in other operating environments outside CenturyLink cloud
* Implement your own Encryption standards
* Advanced feature sets such as Hot backup agents for MS SQL and Hyper-V Integration on Bare Metal
* [List of Partners](../Ecosystem Partners/General/ecosystem-partner-list.md)

### Comparison Matrix

**Product**|**Availability**|**Data Storage**|**Cost Model**|**Integration**|**Support**
-----------|----------------|-------------------|----------------|--------------|---------------|-----------
Simple Backup Service|<ul><li>Global</li><li>Virtual and Bare Metal Servers</li></ul>|<ul><li>Supports data sovereignty</li><li>Stored in customer selected Geo-redundant Object Storage</li><li>Built-in Encryption</li></ul>|Pay as you go (per GB)|<ul><li>Self-Service & API Accessible</li><li>File System Agent</li><li>Supports all Operating System Templates on the platform</li></ul>|CenturyLink Provided Support
Managed Backup|<ul><li>Six Locations</li><li>**Managed** Virtual Servers</li></ul>|<ul><li>Supports data sovereignty</li><li>Digital Vaulting to specific locations</li><li>Built-in Encryption</li></ul>|Tiered pricing model based on average protected storage|<ul><li>Customer provisioned, CenturyLink Managed</li><li>File System Agent</li><li>Supports **Managed** Windows 2008/2012 R2 and RHEL 5/6/7</li></ul>|CenturyLink Provided Support
Marketplace Provider Program Partners|<ul><li>Global</li><li>Virtual and Bare Metal Servers</li></ul>|<ul><li>Supports data sovereignty</li><li>Stored in customer selected Geo-redundant Object Storage</li><li>Customer Defined Encryption</li></ul>|Bring your own license (BYOL)|<ul><li>Customer provisioned and Operated</li><li>File System, Hypervisor & Hot Backup Agents</li><li>Supports all Operating System Templates on the platform</li></ul>|Partner Provided Software Support
