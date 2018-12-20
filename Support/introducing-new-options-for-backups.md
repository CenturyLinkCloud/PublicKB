{{{
  "title": "Introducing New Options for Backups, Plus An Update on the Retirement of Standard & Premium Backup Features",
  "date": "9-21-2016",
  "author": "Jared Ruckle",
  "attachments": []
}}}

This article was updated June 1, 2016 to confirm the retirement of Standard & Premium backup features in the platform as communicated previously. Article was previously updated on May 4, 2016; article was first posted on February 22, 2016.

### Introducing New Options for Backups, Plus an Update on the Retirement of Standard & Premium Backup Features

Late last year, CenturyLink notified customers that the backup features associated with “Standard” and “Premium” storage were to be retired in 2016.

UPDATE - JUNE 1, 2016: Standard & Premium backup features are now retired. Please ensure your data is backed up and protected as needed.  There is no impact to the persistent storage attached to servers.

The [Simple Backup Service is CenturyLink Cloud's backup solution](https://www.ctl.io/simple-backup-service/). This integrated service offers file-level backup protection, with highly customizable retention policies. The service will be available in all CenturyLink Cloud locations, with backup locations around the world.

In addition, we reduced the price of block storage on April 1, two full months **before** the retirement of Standard & Premium backup features.

To assist customers during this transition, here are answers to a few common questions we’ve received from customers.

### Why is CenturyLink making this change?

In short, customers have told us that they want more flexibility and control over their backups, including:
* Custom retention policies: “I don’t want to be limited to 5 or 14 days”
* Custom frequency: “I want to adjust how often I back up, not just once a day”
* More location options: “I want to choose where my backups are stored”
* More control over the files backed up: “I don’t want to be constrained to just snapshots; only certain apps and data require backup”
* The freedom to opt-out of backups entirely for certain servers, to help lower costs

Another reason: a lack of usage of the Standard and Premium backup services, particularly restores. A very small number of restores have been requested in the last 12 months. Consequently, CenturyLink has focused on building and supporting products that offer more self-service features.

### Is the price of storage going to drop? If so, by how much?

Yes – since storage no longer includes bundled backup, price reductions for block storage have been in place effective April 1, 2016.

### Will I still be able to take snapshots manually?

Yes. Snapshots are a useful feature for very specific scenarios – such as right before making impactful changes to your systems. Users can still perform [snapshots on-demand and as scheduled tasks](../Servers/creating-and-managing-server-snapshots.md). [The CenturyLink Cloud CLI can also help automate this task](https://www.ctl.io/knowledge-base/servers/centurylink-cloud-guide-to-cli/).

### Is my team required to take action in order to protect my data after this change?

Yes.  There are several options presented below. It is important to know that if your team does not choose to implement one of the options below - or utilize their own backup solution - data will not be protected against loss or corruption.

### What happens to my backup data from Standard and Premium?

Customers will no longer have access to their backup data from Standard and Premium storage features after May 31, 2016. Data from Standard and Premium backups are not carried over or otherwise migrated to the Simple Backup Service, or any other backup product. The Standard and Premium backup data will be inaccessible via Control or the APIs after May 31, 2016. Customers requiring access to this data should request backup restores as soon as possible via ticket at help@ctl.io.

### What is the Simple Backup Service?

The [Simple Backup Service](https://www.ctl.io/simple-backup-service/) is a new product that performs scheduled backups of data from your servers and stores them in secure object storage for customized retention periods. Users can configure and manage backup policies (frequency, retention, and paths) via the Control Portal. The details and reports of the backups can be viewed via the Control Portal as well.

In addition, users can initiate a restore of files and folders from a given point in time.

### Can I get started with Simple Backup right now?

Yes! Review [this helpful Getting Started Guide](../Backup/getting-started-with-simple-backup.md) to get familiar with the service.

Second, profile your applications. What level of data protection do your VMs need?  What InfoSec data retention policies are in play? Are there some VMs that don't even need backup?

Third, consider the following timeline to protect your VMs with the Simple Backup Service in the coming weeks:

#### Week 1
* Configure policies that match your data retention policies. You can create policies that feature 5 days of retention, as well as 14 days of retention – just like Standard and Premium.
* Apply these policies to a few test servers, and verify that the backup frequency and retention period meet your business needs.
* Experiment with other elements of the Simple Backup UI.

#### Week 2
* For users with large volumes of servers: familiarize yourself with the [Simple Backup APIs](https://www.ctl.io/api-docs/v2/#simple-backup). This will be the most efficient way to apply policies to many VMs.
* Consider data sovereignty implications, and ensure that backups do not cross geographic lines that may violate applicable regulations.

#### Week 3
* Apply backup policies to remaining VMs.

#### Week 4
* Ensure that all VMs that need to be protected, are protected, either with Simple Backup or with another mechanism.

### How does the Simple Backup Service compare to other options are available on CenturyLink Cloud?

The answer varies depending on the workload and your requirements. Along those lines, We’ve partnered with several companies who have in turn integrated their technology with our platform as Certified Ecosystem partners. We summarized a few of these below. They all have a few things in common, namely:
* Proven features for common enterprise use cases
* Automated deployment
* Beta programs, PoCs, or evaluation licenses to help you try each service with little risk
* CenturyLink Cloud SLAs that cover the underlying compute, storage, and network capabilities of each product

**None of these solutions provide VM-level snapshots, but you may find these options superior because of the choice, flexibility, and reliability they provide. Further, almost all of them offer self-service capabilities for the most common DR and backup scenarios, including restores.**

#### Simple Backup Service, from CenturyLink
* When to use it: To back up and protect files against corruption
* Requirements: Outbound Internet access for servers; administrative credentials need to be stored in the Control Portal for automated deployment (manual deployment can be performed if credentials are not stored in the Control Portal)
* Cost: $0.10 GB / mo; Self-service restores will be priced at $0.10 per GB restored
* Licensing: None
* Availability: GA on March 29, 2016
* Deployment Time: Instant – agents are installed locally on each server once a backup policy is applied to a given server
* Support Model: Supported by CenturyLink (since the product is integrated into the Control Portal), with an integrated support experience
* Getting Started: Review the [the product page](https://www.ctl.io/simple-backup-service/), then login to the Control Portal to get started.
* Other resources:
  * [Simple Backup Service API Documentation](https://www.ctl.io/api-docs/v2/#simple-backup)
  * [Powershell Script for the bulk application of Simple Backup Policies for all Servers in an Account](https://github.com/MattSchwabbyCLC/CLCSBSDeployment)

#### Safe Haven, from CenturyLink
* When to use it: Disaster Recovery between CenturyLink Cloud locations, with customized RTO/RPO targets.
* Cost: $40 per VM, per month for licensing. In addition, storage fees for the “replica” site in CenturyLink Cloud apply. Compute resources are not incurred unless a test is underway, or in the event of a disaster.
* Licensing: None
* Availability: GA
* Deployment Time: Days
* Support Model: Supported by CenturyLink (since the product is integrated into the Control Portal); on-boarding from CenturyLink is also included
* To Get Started: Contact your account team, or [visit the product page](https://www.ctl.io/disaster-recovery/)
* Other resources:
  * [This section of the Knowledge Base](https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-3/#1) has additional articles on Safe Haven.

#### CommVault
* When to use it: Data and file backup, with many powerful features and capabilities to protect data across a variety of platforms, and to host data across a variety of storage media. OS-level images are supported.
* Requirements: Detailed in [this Knowledge Base article: Getting Started with CommVault Storage Blueprint](../Ecosystem Partners/Marketplace Guides/getting-started-with-commvault-storage-blueprint.md)
* Cost: Based on the amount of storage protected. Pricing is available upon request, and evaluation licenses are available. Compute resources are required to run CommVault “control” servers in CenturyLink Cloud.
* Licensing: Bring your own license (BYOL), available from CommVault
* Availability: GA
* Deployment Time: Days
* Support Model: Software is supported by CommVault; CenturyLink Cloud supports the underlying infrastructure via our standard SLAs
* To Get Started: 30-day evaluation licenses are available, please contact your CenturyLink account team, or [CommVault for additional information](http://www.commvault.com/contact-us).
* Other resources:
  * [Getting Started with CommVault Storage Blueprint](../Ecosystem Partners/Marketplace Guides/getting-started-with-commvault-storage-blueprint.md)


#### Managed Backup
* When to use it: File-based backup, using the Symantec NetBackup offering
* Requirements: Virtual machines running in supported locations (UC1, VA1, IL1, GB3, SG1, CA3)
* Cost: Tiered pricing
* Availability: GA, in selected sites
* Deployment Time: Self-service, if you have a Master Service Agreement in place with CenturyLink. Refer to [the FAQs to learn more](../Managed Services/managed-backup-frequently-asked-questions.md).
* Support Model: Supported by CenturyLink (since the product is integrated into the Control Portal)
* To Get Started: Contact Vision Solutions directly via email at [CenturyLinkInfo@visionsolutions.com](mailto:CenturyLinkInfo@visionsolutions.com); evaluation licenses are available.
* Other resources:
  * [Managed Backup - Product Page](https://www.ctl.io/managed-services/backup/)
  * [Enabling & Disabling Managed Backup](../Managed Services/enabling-and-disabling-managed-backup.md)
  * [Managed Backup FAQs](../Managed Services/managed-backup-frequently-asked-questions.md)

### Summary
This information should give you a good starting point to investigate specialized solutions that can meet your business requirements. If there’s more details or information you would require, please let us know via [help@ctl.io](mailto:help@ctl.io).
