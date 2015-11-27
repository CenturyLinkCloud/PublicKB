{{{
  "title": "About Simple Backup Service and the Retirement of Standard & Premium Storage",
  "date": "UPDATED 11-18-2015, First Posted 10-7-2015",
  "author": "Jared Ruckle",
  "attachments": []
}}}

### Description

CenturyLink will be introducing a new service, Simple Backup Service, and retiring the Standard and Premium storage products. This Frequently Asked Questions document is meant to provide greater context and clarity about this transition.

### Why is this change happening?

Many customers want more features in their backups - either in retention period, location of secondary copies, or the freedom to have no backup at all. The Simple Backup Service offers this flexibility.

CenturyLink Cloud will still offer a block storage service for virtual machines and bare metal - but users will not be required to have a backup option for existing instances or new servers that they create.

### What does this mean for me?

Your backups on Standard and Premium will continue to function until the Simple Backup Service becomes available in your data center. At that point, customers will need to apply a Simple Backup Policy to their servers in order to have data backed up. Your backup will then operate consistent with Standard or Premium backup service definitions, provided that you apply a similar policy to your servers (the one exception: new backups will be for entire drives and their paths, not snapshots). We recommend pre-identifying those servers and important data/apps which need backup ahead of time.

### Will my servers be automatically removed from standard & premium storage? Is there something I need to do to enable Simple Backup Service?

Yes, customer action will be required, but CenturyLink is managing a few items to make things a little easier. The following describes the "default" option:

* CenturyLink engineers will remove Standard & Premium storage from the Platform (primary block storage will continue to function).
* CenturyLink will then populate a few common backup policies to your account.
* You will need to associate a Simple Backup Service policy to each server if desired.
* Customers can also modify a pre-populated policy or create their own.

If you would require additional assistance or an alternative method, please contact us at [help@ctl.io](mailto:help@ctl.io) or reach out to your account manager.

### When is this happening?

The Standard and Premium products will be phased out data center by data center. This phased retirement of Standard and Premium - and phased launch of the Simple Backup Service - is likely to occur in late 2015 or early 2016. We will post more details on this transition in the coming weeks.

### Will my pricing change?

Yes – your price for block storage will drop, since backups are no longer included by default. However, additional backup costs may be incurred via the Simple Backup Service.

### Will I save money with the Simple Backup Service, compared to what I'm paying today?

It depends on several factors, including:

* Backup policies applied to your servers
* The pace of data change on your servers
* The retention period of the backups

We anticipate that the combination of *lower* block storage costs and common Simple Backup Service configurations will be *significantly less expensive* than Premium storage, and *slightly more expensive* than Standard storage. The exact differences of course will depend on your implementation and the final price of block storage and of the Simple Backup Service.

### What is the Simple Backup Service?

The Simple Backup Service is a new product that performs scheduled backups of data from your servers and stores them in secure object storage for customized retention periods. Users can configure and manage backup policies (frequency, retention, and paths) via the Control Portal. The details and reports of the backups can be viewed via the Control Portal as well.

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

Standard and Premium Storage will not be available for continued use once they are retired from a data center; if you have questions about options, please contact us at [help@ctl.io](mailto:help@ctl.io).

### I'd like to do snapshots on my VMs. Does Simple Backup Service perform snapshots? What options do I have?

Simple Backup Service does not perform snapshots - it provides file and folder level backups and restores. However, you may continue to use the [snapshot capability in the Control Portal](../Servers/creating-and-managing-server-snapshots.md). If you have questions about options, please contact us at [help@ctl.io](mailto:help@ctl.io).

### With this new service, can I still restore to a remote DC, like with Premium Storage?

Not at first - restores will be done on the source VM. However, future improvements to Simple Backup Service may include support for restores to a server at a remote DC. Alternatively, users may first restore the files to the server at the source data center, and then copy/move the files to the server at the remote data center.

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
