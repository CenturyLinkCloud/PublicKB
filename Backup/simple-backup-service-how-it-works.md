{{{
  "title": "Simple Backup How It Works",
  "date": "02-24-2016",
  "author": "John Gerger",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

**Simple Backup Service (SBS)**

[Simple Backup Service](https://www.ctl.io/simple-backup-service/) provides file and folder level backups and restores. The service is integrated with the [Control Portal](https://control.ctl.io/) and is API accessible. That gives you flexibility and ease of use to configure and customize backup policies.

For example, you can specify the backup frequency, retention, location, self-service restores, or path(s)/folder(s) to be backed up. The policies you define can then be applied to VMs and [Bare Metal](https://www.ctl.io/bare-metal/) cloud servers. You can add or remove servers to policies at any time or indicate the storage region as your business needs change.

**How it Works**
Define and apply a policy to the server. A backup agent is then installed on the server. Backups of designated files and folders occur per the frequency defined in the backup policy. The server connects to the Internet through which the backup agent communicates directly with the backup infrastructure. No external server talks to the customer’s server.

SBS leverages [Object Storage](https://www.ctl.io/object-storage/). Backups are securely transferred into Object Storage and reside in storage for the duration of the retention period. Restores are initiated by the customer, at which point the files are brought back to the server within a matter of minutes for customer use. All information pertaining to the backup or restore is available to the customer.

**Backup Policies**
Backup Policies are user-defined configurations that you specify through the [Control Portal](https://control.ctl.io/). Servers are added to policies and start backing up based on the policy details. There is no limit on the number of servers you can add to a policy. Likewise, a server can be added to multiple policies. Backup Policy details include:

* *Name* – A quick, user-friendly name to assist with identifying policies
* *Operating System* – Linux or Windows. All 64-bit Managed OS versions are currently supported.
* *Frequency* – Measured in hours, the frequency establishes the duration between backups. Following a completed backup, the frequency timer restarts and the next backup begins upon frequency expiration.
* *Retention (days)* – The number of days that each data point is stored in secure object storage.
* *Paths to Include* – Define what directories should be included in your backups. Multiple paths may be indicated by clicking the ‘add path’ button.
* *Paths to Exclude* – Define what directories should be excluded from your backups. Multiple paths may be indicated by clicking the ‘add path’ button. Exclusions override inclusions. Certain OS files/folders are automatically excluded from backup.

**Backup Agent**
When a server is added to a backup policy the backup agent is automatically installed on the server as a continuously running service. The agent executes backups of designated files/folders, per the frequency, retention period, and storage location specified in the backup policy. Agent communication transmits over a secure, TLS (transport layer security) connection to the cloud component of the SBS service to sync policy changes and determine when to execute a backup.

Upon installation the agent initially conducts a full backup as indicated by the backup policy. For each consecutive backup, the agent handles files on the server the status of the file as indicate below:

* *Added files* – The new files are backed up and do not expire based on the retention until the file on the server is changed on the server and a new version is backed up, or the file is deleted from the server.
* *Changed files* – The new file is backed up and the prior file version is set to expire after the policy retention period lapses.
* *Deleted files* – Files deleted from a server are retained in storage until the policy retention period lapses.
* *Unchanged files* – No additional files are added to storage. The original files do not expire based on the retention until the file on the server is changed and a new version is backed up, or the file is deleted from the server.

**Full vs. Incremental Backups**
As mentioned above, all data is transferred to Objected Storage when the backup agent gets installed on the server. Incremental backups occur according to the frequency defined in the backup policy and cover the added, changed, or deleted files and folders specifically. This model has the same level of customer data protection as a constant full backup. It offers the benefits of reduced backup speed, minimized data transfer cost, and minimized storage cost. The bottom line is a fast, reliable, and affordable backup solution. In addition, there are also tactics you can use to help [reduce restore costs](https://www.ctl.io/knowledge-base/backup/minimizing-restore-costs/) as well.

**Backup Duration**
The length of time needed to complete the backup varies. Several factors come into play such as whether it's the initial backup, a subsequent incremental backup, the number of files and folders, files sizes, other processes running on the server, bandwidth, ingest rates into Object Storage, or region and distance to the target storage, etc. In any case, the frequency timer does not restart until the previous backup has completed.

**Active/Inactive Policy vs. Active/Inactive Server**
You can enable or disable a server or policy as needed. An inactive policy essentially disables all servers associated with the policy, while the server status only refers to the specified server. An inactive policy status overrides an active server status. Here are the state definitions:

* *Policy Active* – This status indicates that all active servers execute scheduled backups according to the policy configurations. A policy remains in an active state upon until the user chooses to disable the policy.
* *Policy Inactive* – This status indicates prevents the servers under the policy from executing scheduled backups, regardless of the server status. Once disabled, the retention period starts for all data backed up under the policy and it expires after the retention period lapses.
* *Server Active* – This status indicates that the server executes scheduled backups according to policy details for the duration that the policy status is active. Server status is automatically set to active when the server is added to a policy.
* *Server Inactive* – This status indicates that the server does not execute scheduled backups, regardless of the policy status. Once disabled, the retention period starts for all data backed up under this policy and expires after the retention period has lapses.

If the backup agent is unable to communicate with the SBS infrastructure, data will not be set to expire. The feature ensures that data is safe and restorable in the case of server failure or Internet connectivity issues. Servers removed from a policy are treated as if the server status is set to inactive and the retention period starts.

**Restoration**
A new restoration point is created at the completion of every backup, full or incremental. The restore point contains a backup date and time stamp which is actually the point-in-time that the backup job completed. Executing a restore is easy. You manage restoration points through the Control Portal or via API calls. Select the "point-in-time" backup event, specify a destination directory, and click the *restore* button. That's it! Your data is restored automatically within minutes. You can also delete restoration points that are no longer needed.

In order to prevent the accidental overwriting of data, a new directory is created under the restoration path you provide. The directory uses the restoration point ID as the name and contains all of the restored data.

**Security**
Backup are transferred from your server over the public Internet to Object Storage using TLSv1.2. The data is then encrypted at rest in the object store with 256-bit AES encryption server side. A unique key that is also encrypted with a master key when it is stored is used to secure your data. Keys are stored in separate locations from your data for extra protection. At this time user supplied keys are not supported.

**Related Topics**
* [Getting Started with Simple Backup](https://www.ctl.io/knowledge-base/backup/getting-started-with-simple-backup/)
* [Simple Backup FAQs](https://www.ctl.io/knowledge-base/backup/simple-backup-service-faqs/)
* [Minimizing Restore Costs](https://www.ctl.io/knowledge-base/backup/minimizing-restore-costs/)
* [About Simple Backup Services](https://www.ctl.io/knowledge-base/support/backup-service-changes-faq/)
