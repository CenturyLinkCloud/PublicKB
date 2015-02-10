{{{
  "title": "Managed Backup - Frequently Asked Questions",
  "date": "01-22-2015",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Q: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What is included in the Managed Backup service?</strong></p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp;Managed Backup makes&nbsp;CenturyLink's backup&nbsp;solution available in the CenturyLink Cloud. Customers can deploy the new managed backup service on existing virtual machines in the CenturyLink Cloud, as well as on new VMs. By default, all servers with Managed Backup enabled have their volumes backed up nightly.&nbsp; The backup data is stored for two weeks in the same data center as the virtual machine&nbsp;<em>and</em> in a remote data center – this offers geographic redundancy. Customers also get 24x7 support from managed backup engineers to help troubleshoot any backup issues or change configurations such as schedules or retention policies. This support staff is available by contacting the&nbsp;CenturyLink Client Service Center at 1-888-638-6771.&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How do I create a VM that uses Managed Backup?</strong></p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp; From the Control Portal menu, select “Create Server.” You will then be prompted to select the data center, group membership, and other VM properties.&nbsp; Select a data center that supports Managed Backup (an updated list is&nbsp;<a href="http://www.centurylinkcloud.com/managed-services" target="_blank">available here</a>), and then click the “managed server” element to “Yes.” Once this is selected, you will see the option for "managed backup" appear. Set this to yes, and the operating system drop-down menu will then automatically refresh to show available options. Choose your version, and then proceed with the remainder of the server creation process. You may also&nbsp;<a href="https://t3n.zendesk.com/entries/62585140-Enabling-and-Disabling-Managed-Backup" target="_blank">review a more detailed walkthrough of enabling (and disabling) Managed Backup on a server</a>.</p>
<p>&nbsp;</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What if I don’t see an option for Managed Backup in the CenturyLink Cloud Control Panel?</strong></p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There could be a few causes:&nbsp;</p>
<ul>
<li>Be sure you are creating the server in a data center that supports the managed backup service (an updated list is&nbsp;<a href="http://www.centurylinkcloud.com/managed-services" target="_blank">available here</a>).</li>
<li>It is possible your company has not yet executed a Master Services Agreement (MSA) with CenturyLink Technology Solutions. To obtain a MSA – or if you believe you should already have one in place – please contact a CenturyLink Sales Representative toll free at:</li>
<li>United States:&nbsp; 1-855-287-2541</li>
<li>Canada:&nbsp; 1-877-387-3764</li>
<li>Europe, Middle East &amp; Africa:&nbsp; +44 (0) 207 400 5600</li>
<li>Japan:&nbsp; +81 3 5214 0180</li>
<li>Hong Kong:&nbsp; +852 3079 4461</li>
<li>Singapore:&nbsp; +65 6591 8824</li>
</ul>
</ul>
<p>&nbsp;</p>
<p><strong>Q: &nbsp; &nbsp; &nbsp; What's the difference between Managed Backup and Premium Storage?</strong></p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp;Both options provide a two-week retention period and offsite backups.&nbsp; But Managed Backup also offers the ability for customers to work with the managed backup support team to customize retention policies and backup schedules.&nbsp; There are options for including – or excluding - specific files/folders from a backup policy. Premium Storage simply provides nightly VM snapshots, making it difficult to restore selected files or folders, while Managed Backup performs full and incremental backups on a nightly basis and can be turned on and off as needed. Managed Backup also encrypts the backup data at rest.</p>
<p>Users are likely best served by choosing <em>either</em> Managed Backup <em>or</em> Premium Storage.&nbsp;For Hyperscale servers, Managed Backup is recommended.&nbsp;</p>
<p>&nbsp;</p>
<p><strong><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How much does the Managed Backup service cost? Why is the cost not included in the estimates shown in Control Portal?</strong></strong></p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp;Managed Backup uses a tiered pricing model and will cost anywhere from $0.87 to $1.10 depending on how much protected storage is being used. Existing customers using Data Protect Backup for other hosted solutions may also have different pricing based on term commit agreements. Though the costs for Managed Backup does not currently show up as part of the estimates in Control Portal, they will appear on your monthly invoice from CenturyLink as a separate line item. If you have detailed questions regarding billing, please contact your&nbsp;CenturyLink Sales Representative using one of the numbers above.</p>
<p class="p1">&nbsp;</p>
<p class="p1"><strong>Q: &nbsp; &nbsp; &nbsp; &nbsp;When do my scheduled backups run? What if I want my backups to run more frequently or on a different schedule?</strong></p>
<p class="p1">A: &nbsp; &nbsp; &nbsp; &nbsp;Managed backups are scheduled to run daily.&nbsp; The time of the backup will be within 12 hours from the time of server creation (if a server was created at 8:05am, backup will run sometime before 8:05pm each day).&nbsp;If you would like to change this schedule, you may contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771 and enter a request to customize the scheduled backup time for a particular server or set of servers.</p>
<p>&nbsp;</p>
<p class="p1"><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How can I see the status of my recent backups?</strong></p>
<p class="p1">A: &nbsp; &nbsp; &nbsp; &nbsp;Status for recent backups can be seen from the Netbackup Client agent on the server itself. For details, see <a href="https://t3n.zendesk.com/entries/62585180-Using-Managed-Backup-Client" target="_blank">instructions on using the Netbackup Client</a>.&nbsp;The CenturyLink Technology Solutions Client Service Center is also available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.</p>
<p class="p1">&nbsp;</p>
<p class="p1"><strong>Q:&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;If I delete my VM, what happens to the backups?</strong></p>
<p class="p1">A:<strong>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</strong>The backups will eventually be expired off the storage. Backups are managed in storage per a data retention policy which is 14 days, after which, the backups will expiration off the storage.</p>
<p>&nbsp;</p>
<p class="p1"><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What if I only want to backup <em>some</em> of the data on my server? Can I target a specific set of files or folders?</strong></p>
<p class="p1">A: &nbsp; &nbsp; &nbsp; &nbsp; In order to make sure you are using only the amount of backup storage that you need, you can configure an exclusions list to prevent certain paths on the server from being sent to backup. You can configure this list from the&nbsp;Netbackup Client agent on the server itself. For details, see&nbsp;<a href="https://t3n.zendesk.com/entries/62585180-Using-Managed-Backup-Client" target="_blank">instructions on using the Netbackup Client</a>.<strong>&nbsp;</strong>The CenturyLink Technology Solutions Client Service Center is also available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.</p>
<p class="p1"><strong>&nbsp;</strong></p>
<p class="p1"><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What if I want my backups to be kept for longer than two weeks?</strong></p>
<p class="p1">A: &nbsp; &nbsp; &nbsp; &nbsp; If you would like to change the default two-week retention schedule for your backups, you may contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771 and enter a request to customize the retention period&nbsp;for a particular server or set of servers.&nbsp;A few different retention periods are available to choose from.</p>
<p class="p1">&nbsp;</p>
<p><strong>Q: &nbsp; &nbsp; &nbsp; &nbsp;What should I do if I need a restore?</strong></p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp;Contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771.</p>
<p>&nbsp;</p>
<p class="p1"><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How can I remove Managed Backup from a VM? Can I add Managed Backup to an existing VM?</strong></p>
<p class="p1">A: &nbsp; &nbsp; &nbsp; <em>&nbsp;&nbsp;&nbsp;</em>From the Control Portal you can enable and disable managed backup on existing managed servers. On the Server Details page,&nbsp;you will see the option for managed backup on the right side under Server Info. Just click the disable (or enable) button and you will be presented with a switch to allow you to turn managed backup on or off. You may also&nbsp;<a href="https://t3n.zendesk.com/entries/62585140-Enabling-and-Disabling-Managed-Backup" target="_blank">review a more detailed walkthrough of enabling (and disabling) Managed Backup on a server</a>.</p>
<p class="p1">&nbsp;</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Who do I contact if I have trouble with or questions about Managed Backup on my VM?</strong></p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The CenturyLink Technology Solutions Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year.&nbsp; Simply call us at 1-888-638-6771.</p>
