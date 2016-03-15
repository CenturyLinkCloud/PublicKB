{{{
  "title": "Simple backup FAQs",
  "date": "02-2-2016",
  "author": "Justin Withington, John Gerger",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

**FAQs: Simple Backup Service**
-------------------------------

#### IMPORTANT NOTE

CenturyLink Cloud’s Simple Backup Service product is currently in a Limited Beta with specific customers by invitation only and is not intended for production usage. During the Limited Beta there is no production Service Level Agreement.

**FREQUENTLY ASKED QUESTIONS**
------------------------------

**Q: Where do I configure backups?**

A: The Control Portal provides backup configuration functionality. Please refer to our [Getting Started Guide](./getting-started-with-simple-backup.md) for more details

**Q: What are the network requirements for SBS, if any?**

A: Simple Backup Service requires outbound internet traffic over port 443. CLC VMs allow outbound traffic by default using NAT.

**Q: If the backup frequency is every 4 hours, what should I expect?**

A: This depends on how long a backup takes to complete. The frequency timer will not start until the previous backup has completed, so in this example the next backup will start 4 hours after the previous one has completed.

**Q: Can I manually initiate a backup outside of my regularly scheduled frequency?**

A: Yes, from the Backup Agent, users can select the “Backup” button from the Home Dashboard or the Policy Details page. This will place a request at the top of the backup queue and will be processed as soon possible.

**Q: Can I schedule backups to execute at a specific time in the day?**

A: No, the policy frequency determines when the next backup will be executed or the user may manually trigger a backup. Once a backup has completed, the frequency will start to countdown and the next backup will occur when the frequency countdown has expired.

**Q: Can I completely delete my backed up files from storage regardless of the retention period?**

A: No, this is a manual process at this time. A support request will need to be opened to have this performed.

**Q: Why do unchanged files not follow retention?**

A: This provides the ability to utilize incremental backups with consistent full backup protection. By not expiring unchanged files, there is no need to retransfer them to object storage, which minimizes data transfer costs and provides quicker backups. Bottom line is that it provides quicker and cheaper backups for our users.

**Q: Is SBS intended to be used for Disaster Recovery?**

A: No, SBS provides file-level backup protection. In fact, SBS does not backup the OS files or provide snapshot capability. Users can still perform [manual snapshots on-demand](https://www.ctl.io/knowledge-base/servers/creating-and-managing-server-snapshots/) and as scheduled tasks within the server settings. For full [Disaster Recovery](https://www.ctl.io/knowledge-base/support/introducing-new-options-for-backups/#how-does-the-simple-backup-service-compare-to-other-options-are-available-on-centurylink-cloud) services, there are a number of options available internally or through Certified Ecosystem partners.

**Q: Which files/folders are automatically excluded from the backups?**

A: Please refer to the list below:

-  **Windows**

  Explicit path exclusions: "C:\$Recycle.Bin", "C:\SystemVolume Information", "C:\Windows", "C:\Program Files\BakDatAgent", "C:\Program Files\SimpleBackupService", "C:\ProgramData\Microsoft", "C:\Recovery", "C:\PerfLogs"

  Explicit files exclusions: "C:\system.sav", "C:\hiberfil.sys", "C:\pagefile.sys", "C:\swapfile.sys"

  Directory names excluded (regardless of path): "\$Recycle.Bin", "System Volume Information"

  fileExtensionsExcluded: None

  Checked at runtime by type: symbolic links, Windows junctions

 

- **Linux**

  Explicit path exclusions: "/tmp", "/temp", "/proc", "/dev", "/devices", "/sys", "/opt/bakdat", "/opt/simplebackupservice", "/run", "/var/run", "/var/lock", "/mnt", "/media", "/lost+found", "/var/spool/cups", "/var/spool/lpd", "/var/spool/postfix"

  Explicit files exclusions: None

  Directory names excluded (regardless of path): "lost+found"

  fileExtensionsExcluded: ".lock", ".lck"

  Checked at runtime by type: symbolic links, devices (block & character), pipes, sockets


**Q: Can I opt to backup the files that are automatically excluded from backups?**

A: Not at this time; currently the exclusion list overrides the inclusion list. The reason these are not included is because SBS is intended to backup the apps and data that are specific and important to your business. SBS is not intended to be a full server restore. Since OS files are not included, the speed and performance of the backups are increased, while also minimizing backup costs.

**Q: If I reboot my server, do I need to restart the agent?**

A: The agent is setup to start on boot at install time.

**Q: If a new version of the the agent is available, what are the steps to update the agent on my server?**

A: No steps required by the user. The agent will automatically update itself, given that the server is powered on, agent is running and the server is connected to the internet.

**Q: What happens when polices are disabled by the user?**

A: When a policy is disabled backups will stop being performed for the associated server and paths tied to the policy . A count down of the retention period will begin based on the policy details. For example, if the retention period is 14 days, then once the policy is disabled, the files will be retained in storage for 14 days, then removed from storage.

**Q: What if an inactive policy is enabled while the current backups are counting down their retention period?**

A: The files in storage will stop their retention period countdown and all servers associated with the policy will resume their regularly scheduled backups.

**Q: What is the difference between an active/inactive server vs. active/inactive policy?**

A: An inactive policy essentially disables all servers while the server status only refers to the specified server. An inactive policy status will override an active server status.

**Q: What happens when my server is paused, which pauses the agent, or losses connectivity?**

A: No further backups occur from the server to storage. If a backup agent is unable to communicate with the SBS infrastructure backed up data will not be set to expire. This is to ensure that data is safe and restorable in the case of server failure or internet connectivity issues.

**Q: Can I select specific files/folders to restore from a restore point?**

A: Currently the only restore option available is a full restore of all files from a specific point in time (based on the retention period); all files that existed at that point in time will be restored. We have selective file restore on the roadmap and understand that it is a very important feature to most people, but we do not have an estimated release date yet.

**Q: Can restores be performed to another server?**

A: Not currently at this time. A self-service feature is on the SBS roadmap.

**Q: How is the “Backup Date” determined for Restore Points?**

A: The Backup Date is the point in time that the Backup Job completed.

**Q: Why does my Restore Point Status show as “Partial_Success”?**

A: A partially successful backup means that at least one new, or changed file was not backed up completely. All other files successfully backed up will be available through this restore point. Note that locked files will not be backed up.

**Q: How can I confirm that my backups were successful?**

A: There are two places in the agent that show the status of your backups. First, in the Backup Jobs section, which shows all backups executed by this particular agent. Second, for additional information, selecting “Restore” from the Policy Details page will drill down into greater detail about backups for the specific Policy. Details include Backup Date, Status, and Protected Data (GBs).

**Q: Can I adjust the storage region of a server?**

A: No, adjusting the region is not supported. In order to allow redundancy, users may configure a server to backup in multiple regions. A server may be added to the same policy multiple times as long as the region is different.

**Q: How do you handle backing up open files?**

A: At this time, open files will not be backed up and a “Partial_Success” will be shown as the Restore Point Status.
