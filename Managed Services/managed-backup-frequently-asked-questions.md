{{{
  "title": "Managed Backup - Frequently Asked Questions",
  "date": "7-8-2015",
  "author": "Bryan Friedman",
  "attachments": [
    {
      "file_name": "Average Amount of Protected Data Example",
      "url": "../attachments/Avg Amount of Protected Data Example.xlsx",
      "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    }
  ],
  "contentIsHTML": false,
  "sticky": false
}}}

**Q: What is included in the Managed Backup service?**

A: Managed Backup makes CenturyLink's backup solution available in the CenturyLink Cloud. Customers can deploy the new managed backup service on existing virtual machines in the CenturyLink Cloud, as well as on new VMs. By default, all servers with Managed Backup enabled have their volumes backed up nightly. The backup data is stored for two weeks in the same data center as the virtual machine **and** in a remote data center – this offers geographic redundancy. Customers also get 24x7 support from managed backup engineers to help troubleshoot any backup issues or change configurations such as schedules or retention policies. This support staff is available by contacting the CenturyLink Client Service Center at 1-888-638-6771.

**Q: How do I create a VM that uses Managed Backup?**

A: From the Control Portal menu, select “Create Server.” You will then be prompted to select the data center, group membership, and other VM properties. Select a data center that supports Managed Backup (an updated list is [available here](//www.ctl.io/managed-services/backup/)), and then click the “managed server” element to “Yes.” Once this is selected, you will see the option for "managed backup" appear. Set this to yes, and the operating system drop-down menu will then automatically refresh to show available options. Choose your version, and then proceed with the remainder of the server creation process. You may also [review a more detailed walkthrough of enabling (and disabling) Managed Backup on a server](../Managed Services/enabling-and-disabling-managed-backup.md).

**Q: What if I don’t see an option for Managed Backup in the CenturyLink Cloud Control Panel?**

A: There could be a few causes:
* Be sure you are creating the server in a data center that supports the managed backup service (an updated list is [available here](//www.ctl.io/managed-services/backup/)).
* It is possible your company has not yet executed a Master Services Agreement (MSA) with CenturyLink Technology Solutions. To obtain a MSA – or if you believe you should already have one in place – please contact a CenturyLink Sales Representative toll free at:
    * United States: 1-855-287-2541
    * Canada: 1-877-387-3764
    * Europe, Middle East and Africa: +44 (0) 207 400 5600
    * Japan: +81 3 5214 0180
    * Hong Kong: +852 3079 4461
    * Singapore: +65 6591 8824

**Q: What's the difference between Managed Backup and Premium Storage?**

A: Both options provide a two-week retention period and offsite backups. But Managed Backup also offers the ability for customers to work with the managed backup support team to customize retention policies and backup schedules. There are options for including – or excluding - specific files/folders from a backup policy. Premium Storage simply provides nightly VM backups, making it difficult to restore selected files or folders, while Managed Backup performs full and incremental backups on a nightly basis and can be turned on and off as needed. Managed Backup also encrypts the backup data at rest.

Users are likely best served by choosing *either* Managed Backup *or* Premium Storage. For Hyperscale servers, Managed Backup is recommended.

**Q: How much does the Managed Backup service cost? Why is the cost not included in the estimates shown in Control Portal?**

A: Managed Backup uses a tiered pricing model and will cost anywhere from $0.87 to $1.10 per GB per month,and depending on how much average protected storage is being used (see table below). *Note: Existing managed hosting customers using Data Protect Backup will have cloud usage contribute to overall protected data utilization and also may have different pricing based on existing term commit agreements.* Though the costs for Managed Backup does not currently show up as part of the estimates in Control Portal, they will appear on your monthly invoice from CenturyLink as a separate line item. If you have detailed questions regarding billing, please contact your CenturyLink Sales Representative using one of the numbers above.

**Avg Protected Data Utilization**|**Monthly Price per GB**
----------------------------------|------------------------
0-1|$1.10
1-5|$1.08
5-10|$1.05
10-15|$1.03
15-20|$1.01
20-25|$0.98
25-30|$0.96
30-40|$0.94
40-50|$0.91
50-75|$0.89
75-100|$0.87

*For information on how "average protected data utilization" is calculated, review the attachment at the end of this KB.*

**Q: When do my scheduled backups run? What if I want my backups to run more frequently or on a different schedule?**

A: Managed backups are scheduled to run daily. The time of the backup will be within 12 hours from the time of server creation (if a server was created at 8:05am, backup will run sometime before 8:05pm each day). If you would like to change this schedule, you may contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771 and enter a request to customize the scheduled backup time for a particular server or set of servers.

**Q: How can I see the status of my recent backups?**

A: Status for recent backups can be seen from the Netbackup Client agent on the server itself. For details, see [instructions on using the Netbackup Client](../Managed Services/using-managed-backup-client.md). The CenturyLink Technology Solutions Client Service Center is also available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.

**Q:   If I delete my VM, what happens to the backups?**

A: The backups will eventually be expired off the storage. Backups are managed in storage per a data retention policy which is 14 days, after which, the backups will expiration off the storage.

**Q: What if I only want to backup *some* of the data on my server? Can I target a specific set of files or folders?**

A:  In order to make sure you are using only the amount of backup storage that you need, you can configure an exclusions list to prevent certain paths on the server from being sent to backup. You can configure this list from the Netbackup Client agent on the server itself. For details, see [instructions on using the Netbackup Client](../Managed Services/using-managed-backup-client.md).

The CenturyLink Technology Solutions Client Service Center is also available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.

**Q: What if I want my backups to be kept for longer than two weeks?**

A:  If you would like to change the default two-week retention schedule for your backups, you may contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771 and enter a request to customize the retention period for a particular server or set of servers. A few different retention periods are available to choose from.

**Q: What should I do if I need a restore?**

A: Contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771.

**Q: How can I remove Managed Backup from a VM? Can I add Managed Backup to an existing VM?**

A: From the Control Portal you can enable and disable managed backup on existing managed servers. On the Server Details page,you will see the option for managed backup on the right side under Server Info. Just click the disable (or enable) button and you will be presented with a switch to allow you to turn managed backup on or off. You may also [review a more detailed walk through of enabling (and disabling) Managed Backup on a server](../Managed Services/enabling-and-disabling-managed-backup.md).

**Q: Who do I contact if I have trouble with or questions about Managed Backup on my VM?**

A: The CenturyLink Technology Solutions Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.

**Q: Is there a customer accessible API which allows for turning on/off backups, configuring backups, and triggering restores?**

A: This feature is not available currently.

**Q: As a customer can I leverage Microsoft Volume Shadow Copy Service (VSS)?**

A: The Master server in the DPB infrastructure is already configured to support this. There is no need to configure the backup agent on the VM. However, VSS must be configured appropriately on the Operating System.

**Q: As a customer can I request on-demand backups out of the normal scheduled jobs?**

A: This is possible via a request to Support.  The backup will have the standard product feature of 2 weeks retention at the local data center and a simultaneous copy at the secondary data center.

**Q: Is hot backup offered in Managed Backup for (a) databases and for (b) Exchange? What options/suggestions are available?**

A: Hot backup is not offered in Managed Backup.  Managed Backup is for file/folder level backups and restores.

For SQL, Mysql , Oracle and other databases, a suggested method is to put the data to a file/folder for inclusion in the backups.

To safely backup and restore Microsoft Exchange mailbox data CenturyLink Cloud customers must implementation and operate their own solution.  Using 3rd party backup clients allows customers to perform recovery of message/mailbox (Exchange) data, define retention periods and backup frequency.  Customers can speak to a CenturyLink Cloud sales representative for guidance.

**Q: Where are my offsite vault copies stored?**

A: The table below provides the offsite vault locations:

**CenturyLink Cloud Location**|**Offsite Vault Location**
------------------------------|--------------------------
US West (Santa Clara) - UC1|[CenturyLink CH3](//www.centurylink.com/business/enterprise/colocation/data-centers/united-states/illinois/chicago.html)
US East (Sterling) - VA1|[CenturyLink DL2](//www.centurylink.com/business/enterprise/colocation/data-centers/united-states/texas/dallas.html)
Great Britain (Slough) - GB3|[CenturyLink LO6](//www.centurylink.com/business/enterprise/colocation/data-centers/united-kingdom/london.html)
APAC (Singapore) - SG1|[CenturyLink SG8](//www.centurylink.com/business/enterprise/colocation/data-centers/singapore.html)
