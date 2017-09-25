{{{
  "title": "Simple Backup Service FAQs",
  "date": "6-27-2017",
  "author": "John Gerger",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Table of Contents

* [Requirements](#requirements)
* [Agent](#agent)
* [Backups](#backups)
* [Restores](#restores)
* [Policies](#policies)
* [Frequency](#frequency)
* [Scheduling](#scheduling)
* [Retention](#retention)
* [Inclusions and Exclusions](#inclusions-and-exclusions)
* [Billing](#billing)

### Requirements

**Q: What are the network requirements for Simple Backup Service (SBS), if any?**

A: SSH for root is required to allow the Blueprint to initially install the Backup Agent on the target server; it may be disabled after the initial instillation as it is not needed for the agent to function. The Simple Backup Service also requires outbound internet traffic over port 443. CenturyLink Cloud VMs allow outbound traffic by default using NAT. Alternatively, firewall rules may be configured utilizing the endpoints listed below.

```
up-va1.backup.ctl.io
up-de1.backup.ctl.io
up-ca3.backup.ctl.io
up-sg1.backup.ctl.io
up-uc1.backup.ctl.io
up-gb3.backup.ctl.io
```
Additional endpoints will need to be configured based on the Storage Region selected as indicated in the [How it Works](./simple-backup-service-how-it-works.md) KB article.

**Q: What OSes are supported?**

A: All Operating Systems that are currently buildable in the CenturyLink Cloud Control Portal are supported. Customer imported OVA/OVF OSes and 32-bit OSes are not supported.

**Q: How can I use Simple Backup Service on a server that doesn't have internet access?**

A: Simple Backup Service requires consistent internet connectivity to install, update, backup, and restore. If consistent internet connectivity is not an option, please review our [Managed Backup](https://www.ctl.io/managed-services/backup/) offering.

**Q: What happens when my server is paused, which pauses the agent, or losses connectivity?**

A: No further backups occur from the server to storage. If a backup agent is unable to communicate with the SBS infrastructure, stored backup data will not be set to expire. This is to ensure that data is safe and restorable in the case of server failure or internet connectivity issues.

**Q: Is SBS intended to be used for Disaster Recovery?**

A: No, SBS provides file-level backup protection. In fact, SBS does not backup certain [OS files](#inclusions-and-exclusions) or provide snapshot capability. Users can still perform [manual snapshots on-demand](https://www.ctl.io/knowledge-base/servers/creating-and-managing-server-snapshots/) and as scheduled tasks within the server settings. For full [Disaster Recovery](https://www.ctl.io/knowledge-base/support/introducing-new-options-for-backups/#how-does-the-simple-backup-service-compare-to-other-options-are-available-on-centurylink-cloud) services, there are a number of options available internally or through Certified Ecosystem partners.

**Q: Does SBS support server cloning?**

A: No, currently SBS does not support cloning. If the agent is installed on a server and the server is cloned there can be data continuity issues between the backups of the source and cloned server. If a server is going to be cloned, the SBS agent must be [uninstalled](./removing-simple-backup-service.md) first, and the agent properly installed on all servers needed after they are cloned.

### Agent

**Q: What are the minimum requirements of a VM for the SBS agent to run?**

A: Although the SBS agent will run on 1 Core, 1GB of RAM VM's, the overall speed and performance might not be optimal. There could be resource contention on the server during a backup as well, depending on the other processes running on the server at that time.

**Q: What are the logon credentials for the backup agent?**

A: Please review the [SBS Agent Security Configurations](./sbs-agent-security.md) KB article for details.

**Q: Can I change the backup agent credentials for all my instances in one place?**

A: Not at this time. Each properties file must be updated individually.

**Q: How can I access my backup agent from a remote machine?**

A: Please review the [SBS Agent Security Configurations](./sbs-agent-security.md) KB article for details.

**Q: Where can I find the backup agent's logs on my machine?**

A: Logs can be viewed at the following locations:
  * Linux: /var/lib/simple-backup-service
  * Windows: C:\Windows\System32\config\systemprofile\appdata\local\simplebackupservice

**Q: What can I find in the backup agent's logs?**

A: The backup agent's logs have details about the backups that have run on the system. This is helpful if you are trying to identify causes of backup failures as the failed files will be listed in the logs.

**Q: If a new version of the the agent is available, what are the steps to update the agent on my server?**

A: No steps required by the user. The agent automatically updates itself, given that the server is powered on, agent is running and the server is connected to the internet.

**Q: If I reboot my server, do I need to restart the agent?**

A: The agent is setup to start on boot at install time.

### Backups

**Q: Where do I configure backups?**

A: The Control Portal provides backup configuration functionality. Please refer to our [Getting Started Guide](./getting-started-with-simple-backup.md) for more details. Additionally, the [Backup API](https://www.ctl.io/api-docs/v2/#simple-backup) may be used for advanced scripting.

**Q: What does an "IN_PROGRESS" status backup mean?**

A: An "IN_PROGRESS" status for a backup job means the data is actively being transferred from the server to the specified storage region associated with the policy.

**Q: How do you handle backing up open files?**

A: At this time, open files will not be backed up and a “Partial_Success” will be shown as the Restore Point Status.

**Q: How can I confirm that my backups were successful?**

A: There are two places in the agent that show the status of your backups. First, in the Backup Jobs section, which shows all backups executed by this particular agent. Second, for additional information, selecting “Restore” from the Policy Details page will drill down into greater detail about backups for the specific Policy. Details include Backup Date, Status, and Protected Data (GBs).

**Q: For a "Failed" or "Partial_Success" backup status, can I see which files failed and why?**

A: Yes, see the sbs-backup-files-failed.csv file located on your system for details.

**Q: Where are my backups actually stored?**

A: The SBS agent on the server transfers backup data to one of six different backup storage regions, each built on top of cloud object storage. CenturyLink sources this object storage from a combination of its own cloud platform, as well as 3rd party cloud providers such as Amazon Web Services. For more information, see our [How It Works](https://www.ctl.io/knowledge-base/backup/simple-backup-service-how-it-works/) KB article.

### Restores

**Q: What does an "IN_PROGRESS" status restore mean?**

A: An "IN_PROGRESS" status for a restore job indicates the data is actively being restored from the storage region associated with the policy to the server.

**Q: Can I select specific files/folders to restore from a restore point?**

A: Yes, in the restore section there is an option to perform a full restore, or selective file restore. Using the selective file restore option allows you to enter the full path to a file or folder and the option to add multiple paths to restore.

**Q: Can restores be performed to another server?**

A: A self-service feature is on the SBS roadmap. If a restore to an alternate server is required, please create a [support request](https://www.ctl.io/knowledge-base/support/how-do-i-report-a-support-issue/#exceptions).

**Q: How is the “Backup Date” determined for Restore Points?**

A: The Backup Date is the point in time that the Backup Job completed.

**Q: What is the "Protected Data" amount for my Restore Point?**

A: Protected Data is not the amount of data backed up for the specified backup instance, but rather the total amount of restorable data for the specified restore point. Essentially, Protected Data is the consolidation of your full backup and any changes per the specified backup instance.

**Q: Why does my Restore Point Status show as “Partial_Success”?**

A: A partially successful backup means that at least one new, or changed file was not backed up completely. All other files successfully backed up will be available through this restore point. Note that locked files will not be backed up.

**Q: Why did my restore fail?**

A: Common causes of restore failure:

  - Server lacks internet connectivity over port 443.
  - Restore Path is not accessible due to permissions.
  - Insufficient disk space (error message will display).

**Q: Why can't I see all of my restored files?**

A: Common causes of obscured restore files:

  - Permissions of the files and folders restored as assigned during backup execution.
  - Invalid path structure provided as a Restore Path. In this case, the files and folders will be restored to the C:Windows\System32 folder for Windows or the SimpleBackupService directory for Linux.

**Q: How do I stop an in-progress restore from completing?**

A: Restarting the Simple Backup Service on the server will stop all running restore task(s). See https://www.ctl.io/knowledge-base/backup/restarting-simple-backup-service/ for steps to restart in Linux and Windows.

### Policies

**Q: Can I adjust the storage region of a server?**

A: No, adjusting the region is not supported. In order to allow redundancy, users may configure a server to backup in multiple regions. A server may be added to the same policy multiple times as long as the region is different.

**Q: Why is my policy status still showing "Pending_Install"**

A: A policy will show its status as "Pending_Install" until the SBS agent checks back in with the SBS servers. This could be delayed if the agent is performing a backup/restore or if a system reboot is required.

**Q: What happens when polices are disabled by the user?**

A: When a policy is disabled, backups will stop being performed for the associated server and paths tied to the policy. A countdown of the retention period will begin based on the policy details. For example, if the retention period is 14 days, then once the policy is disabled, the files will be retained in storage for 14 days, then removed from storage.

**Q: What if an inactive policy is enabled while the current backups are counting down their retention period?**

A: The files in storage will stop their retention period countdown and all servers associated with the policy will resume their regularly scheduled backups.

**Q: What is the difference between an active/inactive server vs. active/inactive policy?**

A: An inactive policy essentially disables all servers while the server status only refers to the specified server. An inactive policy status will override an active server status.

**Q: How can I view the policies applied to a server?**

A: Currently, the most efficient method of viewing all the policies applied to a server is to navigate from Control Portal and drill into the server from the Policy Details page. Steps are detailed below:

  1. From your server within Control Portal, click **manage** in the Simple Backup section to view all policies associated with your account alias.
  2. Click a policy to drill into the policy details to view all associated servers.
  3. Click a server to view all applied policies.

### Frequency

**Q: Where has the frequency setting gone when creating a new policy?**

A: We have replaced the frequency method of backing up with a CRON style scheduling method. Please see below for more details.

**Q: Will my backup policies that were setup with frequency still function?**

A: YES! We have backwards compatibility for all backup policies that use the frequency method of backing up

**Q: How do I change my old frequency based policies over to schedule based policies?**

Simply select the policy you wish to change, click edit, and select the desired schedule for the new policy. Once it has been saved, the new schedule will take effect.

**Q: If the backup frequency is every 4 hours, what should I expect?**

A: This depends on how long a backup takes to complete. The frequency timer will not start until the previous backup has completed, so in this example the next backup will start 4 hours after the previous one has completed.

**Q: Can I manually initiate a backup outside of my regularly scheduled frequency?**

A: Yes. From the Backup Agent, click the **Backup** button from the Home Dashboard or the Policy Details page. This places a request at the top of the backup queue and will be processed as soon possible.

**Q: Can I schedule backups to execute at a specific time in the day?**

A: YES! This is part of our new Scheduling feature; for more details, please see the [getting started guide](./getting-started-with-simple-backup.md)

### Scheduling

**Q: What scheduling configurations are available?**

A: You can configure a backup schedule on an hourly, daily, weekly, monthly or yearly basis.

**Q: Can I set the hour of the day to backup?**

A: Yes, all options except for hourly allow you to specify at what hour you want the backup to start.

**Q: Can I specify a time for backups to NOT happen?**

A: No, you can not currently specify a blackout period for backups.

### Retention

**Q: Can I completely delete my backed up files from storage regardless of the retention period?**

A: No. This is a manual process at this time. A [support request](https://www.ctl.io/knowledge-base/support/how-do-i-report-a-support-issue/#exceptions) will need to be opened to have this performed.

**Q: Why do unchanged files not follow retention?**

A: This provides the ability to utilize incremental backups with consistent full backup protection. By not expiring unchanged files, there is no need to retransfer them to object storage, which minimizes data transfer costs and provides quicker backups. Bottom line is that it provides quicker and cheaper backups for our users.

**Q: What is the maximum retention period for backups?**

A: 18263 days (approximately 50 years)

### Inclusions and Exclusions

**Q: Which files/folders are automatically excluded from the backups?**

A: Please refer to the list below:

-  **Windows**

  Explicit path exclusions: "C:\$Recycle.Bin", "C:\SystemVolume Information", "C:\Windows", "C:\Program Files\BakDatAgent", "C:\Program Files\SimpleBackupService", "C:\ProgramData\Microsoft", "C:\Recovery", "C:\PerfLogs"

  Explicit files exclusions: "C:\system.sav", "C:\hiberfil.sys", "C:\pagefile.sys", "C:\swapfile.sys"

  Folder names excluded (regardless of path): "\$Recycle.Bin", "System Volume Information"

  fileExtensionsExcluded: None

  Checked at runtime by type: symbolic links, Windows junctions

- **Linux**

  Explicit path exclusions: "/tmp", "/temp", "/proc", "/dev", "/devices", "/sys", "/opt/bakdat", "/opt/simplebackupservice", "/run", "/var/run", "/var/lock",  "/media", "/lost+found", "/var/spool/cups", "/var/spool/lpd", "/var/spool/postfix"

  Explicit files exclusions: None

  Directory names excluded (regardless of path): "lost+found"

  fileExtensionsExcluded: ".lock", ".lck"

  Checked at runtime by type: symbolic links, devices (block & character), pipes, sockets

**Q: Can I opt to backup the files that are automatically excluded from backups?**

A: Not at this time. Currently, the exclusion list overrides the inclusion list. The reason these are not included is because SBS is intended to backup the apps and data that are specific and important to your business. SBS is not intended to be a full server restore. Since OS files are not included, the speed and performance of the backups are increased, while also minimizing backup costs.

**Q: Are wildcard characters supported for inclusion/exclusion backup paths when creating a Backup Policy?**

A: Wildcard characters are not directly supported at this time. However, all sub-folders and files of an included path will be backed up unless specifically added to the exclusion list. All sub-folders and files of an exclusion path will be omitted from backup.

### Billing

**Q: How is my bill calculated?**

A: SBS provides a simplified billing model. The cost per GB for backups is calculated on the actual data stored on an hourly basis. The actual data stored varies based on the backup retention, frequency, and your data change rate. After your first initial backup, each subsequent backup will capture and store changes to your data. The restore cost is a flat rate based on the restored amount of data in GBs.

* Backup Cost Calculation Example:

  10 GB of data backed up starting on the 15th of the month assuming no changes throughout the reamining duration of the month.

  Hourly GB Usage = (10 GB of backup x 15 days x 24 hours) = 3,600 GB

  Billable GB amount based on the monthly rate = 3,600 GB usage / 720 hours in a month = 5 GB

**Q: Are there any additional costs or hidden fees associated with SBS?**

A: No, there are no hidden fees or additional costs (data transfer, storage, licenses, etc.).
