{{{
  "title": "About Simple Backup Service and the Retirement of Standard & Premium Storage",
  "date": "5-4-2016",
  "author": "Jared Ruckle & Mark Lee",
  "attachments": []
}}}

Article first posted on 10-7-2015

Updated May 4, 2016 to reflect new retirement date of June 1, 2016

Updated April 14, 2016 to reflect the lack of data availability after feature retirement.

Updated on March 29, 2016 to reflect April 1 price drop for block storage, specific dates, as the rollout plan, including the need for customers to create, and apply their own backup policies.

### Description

CenturyLink has introduced a new service, [Simple Backup Service](https://www.ctl.io/simple-backup-service/), and will be retiring the Standard and Premium backup storage products. This Frequently Asked Questions document is meant to provide greater context and clarity about this transition. Additional details, [please refer to this knowledge base article updated May 4, 2016](../Support/introducing-new-options-for-backups.md).

### Why is this change happening?

Many customers want more features in their backups - either in retention period, location of secondary copies, or the freedom to have no backup at all. The [Simple Backup Service](https://www.ctl.io/simple-backup-service/) offers this flexibility.

CenturyLink Cloud will still offer a block storage service for virtual machines and bare metal - but users will no longer have a bundled backup option for existing instances or new servers that they create.

### What does this mean for me?

Your backups on Standard and Premium will continue to function until June 1, 2016. **After that date, your data will no longer be automatically backed up.** In the meantime, assess your backup requirements, and identify servers that require protection. CenturyLink has developed a [short-list of solutions to consider for backup and disaster recovery scenarios](../Support/introducing-new-options-for-backups.md).

### Will my servers be automatically removed from Standard & Premium backup? Is there something I need to do to enable Simple Backup Service?

Yes, servers will be automatically removed from Standard and Premium backup on June 1, 2016. If you would like to have your servers protected with the Simple Backup Service, here are the steps to follow:

* The Simple Backup Service launches March 29 - we recommend trying out the service as soon as possible, [please visit the product page and complete the online form](https://www.ctl.io/simple-backup-service/).
* Customers can then create and apply backup policies to their virtual machines
* Apply policies to a few test machines
* Associate policies across your deployment as desired
* CenturyLink engineers will remove Standard & Premium storage from the Platform (primary block storage will continue to function)
* You will need to associate a Simple Backup Service policy to each server if desired
* Customers can also modify an existing policy or create their own

If you would require additional assistance, please contact us at [help@ctl.io](mailto:help@ctl.io) or reach out to your account manager.

### When is this happening?

The Standard and Premium products will be retired on June 1. **Until then, there are no changes to Standard and Premium storage. However, customers should evaluate the Simple Backup Service and other alternatives in the meantime.**

### What happens to my backup data from Standard and Premium?

Customers will no longer have access to their backup data from Standard and Premium storage features after May 31, 2016. Data from Standard and Premium backups are not carried over or otherwise migrated to the Simple Backup Service, or any other backup product. The Standard and Premium backup data will be inaccessible via Control or the APIs after May 31, 2016. Customers requiring access to this data should request backup restores as soon as possible via ticket at help@ctl.io.

### Will my pricing change?

Yes – the list price for block storage was reduced effective April 1, 2016. However, additional backup costs may be incurred via the Simple Backup Service or other selected solutions.

New prices for block storage are in effect April 1, 2016, two months **before** the retirement of Standard & Premium backup features. Your April and May 2016 invoices will reflect these changes.

### Will I save money with the Simple Backup Service, compared to what I'm paying today?

It depends on several factors, including:

* Backup policies applied to your servers
* The pace of data change on your servers
* The retention period of the backups

We anticipate that the combination of *lower* block storage costs and common Simple Backup Service configurations will be *significantly less expensive* than Premium storage, and *slightly more expensive* than Standard storage. The exact differences of course will depend on your implementation.

### What is the Simple Backup Service?

The [Simple Backup Service](https://www.ctl.io/simple-backup-service/) is a new product that performs regular backups of data from your servers and stores them in secure object storage for customized retention periods. Users can configure and manage backup policies (frequency, retention, and paths) via the Control Portal. The details and reports of the backups can be viewed via the Control Portal as well.

In addition, users can initiate a restore of files and folders from a given point in time.

### How does the Simple Backup Service work?

The customer first defines a backup policy - frequency, retention, path(s) to be backed up, and target region for the backup). When a backup policy is then applied to a server, an agent is installed. The agent begins backing up the appropriate data immediately, as dictated by that policy. Changes to the files in the path(s) of the policy are backed up per the frequency of the policy. Customers can deactivate backup policies at any time.

Backups are held in secure storage for the duration of the retention setting within the policy. Further, each backup creates a restore point. Customers can initiate a restore of their data to their server by choosing the desired restore point and indicating the folder on their server to put the data. The agent will then retrieve the necessary data from storage, and place it in the specified folder. Sufficient space on the drive must be available for the restore to be successful.

Removing a policy from the Control Portal also dis-associates the policy from any servers, meaning backups cease to occur at that point (though any existing backups will be retained according to the policy configuration.

### Where will the Simple Backup Service be available? Where are the backups stored?

The Simple Backup Service will be available for virtual machines and bare metal servers in all CenturyLink Cloud nodes, public and private. The availability will be introduced according to the timeline above. The storage targets for the backups will be located in regions around the world. These locations are in enterprise data centers that meet CenturyLink standards for availability, durability, security, and access. Customers can choose the target which make sense for the business needs and governance. Backup target regions tentatively include:

* US East
* US West
* Canada
* EU-West (Ireland)
* EU-East (Germany)
* APAC (Singapore)

### What is a policy for the Simple Backup Service?

A policy is defined by the user, and includes:

* A unique backup policy name
* The frequency of the backups
* A retention period (in days, months, and years)
* Path(s) and/or folder(s) that contains the data to be backed up.

From there, users associate a policy with a server and then specify the target region for the backup. A user can have multiple policies in their account; policies can have one or more servers. Further servers can have more than one policy.

### My requirements for governance may not be met by the Simple Backup Service. What are my options? Can I continue to use Standard and Premium storage indefinitely?

Standard and Premium Storage will not be available for continued use once they are retired on June 1; if you have questions about options, please refer to [this knowledge article with additional options](../Support/introducing-new-options-for-backups.md), including those from our ecosystem partners.

### I'd like to do snapshots on my VMs. Does Simple Backup Service perform snapshots? What options do I have?

Simple Backup Service does not perform snapshots - it provides file and folder level backups and restores. However, you may continue to use the [snapshot capability in the Control Portal](../Servers/creating-and-managing-server-snapshots.md). If you have questions about options, please contact us at [help@ctl.io](mailto:help@ctl.io).

### With this new service, can I still restore to a remote DC, like with Premium Storage?

Not today - restores will be done on the source VM. However, future improvements to Simple Backup Service may include support for restores to a server at a remote DC. Alternatively, users may first restore the files to the server at the source data center, and then copy/move the files to the server at the remote data center.

### What operating systems does Simple Backup Service support?

The service supports all 64-bit operating systems available on the Platform today. In the future, legacy 32-bit operating systems will be supported as well.

### How does Simple Backup Service differ from the current storage services?

This chart is a helpful comparison:

| Feature | Standard | Premium | Simple Backup Service |
| --- | --- | --- | ---|
| Block Storage | Included | Included | Purchased separately |
| Required with each server | Default option | Optional upgrade | No, users opt-in only |
| Backup Level | Snapshot | Snapshot | File-level |
| Supports user-defined policies | No | No | Yes |
| Retention Period | 5 days | 14 days | User-defined (1 day minimum) |
| Location of Backups | Local DC | Secondary DC | Choose from several options |
| Frequency of backup | Daily | Daily | User definable (minimum 1 hour) |
| Restores | Upon request by CTL Cloud customer care | Upon request by CTL Cloud customer care | Self-service |
