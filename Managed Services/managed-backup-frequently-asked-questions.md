{{{
  "title": "Managed Backup - Frequently Asked Questions",
  "date": "01-22-2015",
  "author": "Bryan Friedman",
  "attachments": [
    {
      "file_name": "Average Amount of Protected Data Example",
      "url": "/knowledge-base/attachments/Avg Amount of Protected Data Example.xlsx",
      "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    }
  ],
  "contentIsHTML": true
}}}

<p><strong>Q: What is included in the Managed Backup service?</strong></p>
<p>A: Managed Backup makesCenturyLink's backupsolution available in the CenturyLink Cloud. Customers can deploy the new managed backup service on existing virtual machines in the CenturyLink Cloud, as well as on new VMs. By default, all servers with Managed Backup enabled have their volumes backed up nightly. The backup data is stored for two weeks in the same data center as the virtual machine<em>and</em> in a remote data center – this offers geographic redundancy. Customers also get 24x7 support from managed backup engineers to help troubleshoot any backup issues or change configurations such as schedules or retention policies. This support staff is available by contacting theCenturyLink Client Service Center at 1-888-638-6771.</p>

<p><strong>Q: How do I create a VM that uses Managed Backup?</strong></p>
<p>A: From the Control Portal menu, select “Create Server.” You will then be prompted to select the data center, group membership, and other VM properties. Select a data center that supports Managed Backup (an updated list is<a href="http://www.centurylinkcloud.com/managed-services" target="_blank">available here</a>), and then click the “managed server” element to “Yes.” Once this is selected, you will see the option for "managed backup" appear. Set this to yes, and the operating system drop-down menu will then automatically refresh to show available options. Choose your version, and then proceed with the remainder of the server creation process. You may also<a href="/knowledge-base/managed-services/enabling-and-disabling-managed-backup">review a more detailed walkthrough of enabling (and disabling) Managed Backup on a server</a>.</p>

<p><strong>Q: What if I don’t see an option for Managed Backup in the CenturyLink Cloud Control Panel?</strong></p>
<p>A: There could be a few causes:</p>
<ul>
    <li>Be sure you are creating the server in a data center that supports the managed backup service (an updated list is<a href="http://www.centurylinkcloud.com/managed-services" target="_blank">available here</a>).</li>
    <li>It is possible your company has not yet executed a Master Services Agreement (MSA) with CenturyLink Technology Solutions. To obtain a MSA – or if you believe you should already have one in place – please contact a CenturyLink Sales Representative toll free at:</li>
    <li>United States: 1-855-287-2541</li>
    <li>Canada: 1-877-387-3764</li>
    <li>Europe, Middle East &amp; Africa: +44 (0) 207 400 5600</li>
    <li>Japan: +81 3 5214 0180</li>
    <li>Hong Kong: +852 3079 4461</li>
    <li>Singapore: +65 6591 8824</li>
</ul>

<p><strong>Q: What's the difference between Managed Backup and Premium Storage?</strong></p>
<p>A: Both options provide a two-week retention period and offsite backups. But Managed Backup also offers the ability for customers to work with the managed backup support team to customize retention policies and backup schedules. There are options for including – or excluding - specific files/folders from a backup policy. Premium Storage simply provides nightly VM snapshots, making it difficult to restore selected files or folders, while Managed Backup performs full and incremental backups on a nightly basis and can be turned on and off as needed. Managed Backup also encrypts the backup data at rest.</p>
<p>Users are likely best served by choosing <em>either</em> Managed Backup <em>or</em> Premium Storage.For Hyperscale servers, Managed Backup is recommended.</p>

<p><strong><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How much does the Managed Backup service cost? Why is the cost not included in the estimates shown in Control Portal?</strong></strong></p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp;Managed Backup uses a tiered pricing model and will cost anywhere from $0.87 to $1.10 per GB per month,&nbsp;depending on how much average protected storage is being used (see table below). <em style="font-size: 1em; line-height: 1.45em;">Note:&nbsp;</em><span style="font-size: 1em; line-height: 1.45em;"><em>Existing managed hosting customers using Data Protect Backup will have cloud usage contribute to overall protected data utilization and also may have different pricing based on existing term commit agreements.&nbsp;</em></span><span style="font-size: 1em; line-height: 1.45em;">Though the costs for Managed Backup does not currently show up as part of the estimates in Control Portal, they will appear on your monthly invoice from CenturyLink as a separate line item. If you have detailed questions regarding billing, please contact your&nbsp;CenturyLink Sales Representative using one of the numbers above.</span></p>
<table>
<tbody>
<tr>
<th>
Avg Protected<br />Data Utilization*
</th>
<th>
Monthly<br />Price per GB
</th>
</tr>
<tr>
<td>0-1</td>
<td>$1.10</td>
</tr>
<tr>
<td>1-5</td>
<td>$1.08</td>
</tr>
<tr>
<td>5-10</td>
<td>$1.05</td>
</tr>
<tr>
<td>10-15</td>
<td>$1.03</td>
</tr>
<tr>
<td>15-20</td>
<td>$1.01</p>
</td>
</tr>
<tr>
<td>20-25</td>
<td>$0.98</td>
</tr>
<tr>
<td>25-30</td>
<td>$0.96</td>
</tr>
<tr>
<td>30-40</td>
<td>$0.94</td>
</tr>
<tr>
<td>40-50</td>
<td>$0.91</td>
</tr>
<tr>
<td>50-75</td>
<td>$0.89</td>
</tr>
<tr>
<td>75-100</td>
<td>$0.87</td>
</tr>
</tbody>
</table>
<p>* For information on how "average protected data utilization" is calculated, take a look at this [example of a two-month period](/knowledge-base/attachments/Avg Amount of Protected Data Example.xlsx).</p>

<p><strong>Q: When do my scheduled backups run? What if I want my backups to run more frequently or on a different schedule?</strong></p>
<p>A: Managed backups are scheduled to run daily. The time of the backup will be within 12 hours from the time of server creation (if a server was created at 8:05am, backup will run sometime before 8:05pm each day).If you would like to change this schedule, you may contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771 and enter a request to customize the scheduled backup time for a particular server or set of servers.</p>

<p><strong>Q: How can I see the status of my recent backups?</strong></p>
<p>A: Status for recent backups can be seen from the Netbackup Client agent on the server itself. For details, see <a href="/knowledge-base/managed-services/using-managed-backup-client">instructions on using the Netbackup Client</a>.The CenturyLink Technology Solutions Client Service Center is also available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.</p>

<p><strong>Q:   If I delete my VM, what happens to the backups?</strong></p>
<p>A: The backups will eventually be expired off the storage. Backups are managed in storage per a data retention policy which is 14 days, after which, the backups will expiration off the storage.</p>

<p><strong>Q: What if I only want to backup <em>some</em> of the data on my server? Can I target a specific set of files or folders?</strong></p>
<p>A:  In order to make sure you are using only the amount of backup storage that you need, you can configure an exclusions list to prevent certain paths on the server from being sent to backup. You can configure this list from theNetbackup Client agent on the server itself. For details, see<a href="/knowledge-base/managed-services/using-managed-backup-client">instructions on using the Netbackup Client</a>.<strong></strong>The CenturyLink Technology Solutions Client Service Center is also available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.</p>

<p><strong>Q: What if I want my backups to be kept for longer than two weeks?</strong></p>
<p>A:  If you would like to change the default two-week retention schedule for your backups, you may contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771 and enter a request to customize the retention periodfor a particular server or set of servers.A few different retention periods are available to choose from.</p>

<p><strong>Q: What should I do if I need a restore?</strong></p>
<p>A: Contact the CenturyLink Technology Solutions Client Service Center at 1-888-638-6771.</p>

<p><strong>Q: How can I remove Managed Backup from a VM? Can I add Managed Backup to an existing VM?</strong></p>
<p>A: <em></em>From the Control Portal you can enable and disable managed backup on existing managed servers. On the Server Details page,you will see the option for managed backup on the right side under Server Info. Just click the disable (or enable) button and you will be presented with a switch to allow you to turn managed backup on or off. You may also<a href="/knowledge-base/managed-services/enabling-and-disabling-managed-backup">review a more detailed walkthrough of enabling (and disabling) Managed Backup on a server</a>.</p>

<p><strong>Q: Who do I contact if I have trouble with or questions about Managed Backup on my VM?</strong></p>
<p>A: The CenturyLink Technology Solutions Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771.</p>
