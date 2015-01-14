{{{
  "title": "CenturyLink Cloud Backup and Recovery Services",
  "date": "1-5-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description:</h3>
<p>The CenturyLink Cloud Platform provides clients with various integrated and custom solutions to protect and rapidly recovery data. &nbsp;</p>
<h3>Standard Virtual Machine Backup &amp; Recovery Services</h3>
<p>All <em><strong>Standard</strong> </em>Virtual Machines in the CenturyLink Cloud platform include a nightly file system backup of the Operating System's running state. These nightly backups start around 8pm (local server time) but are staggered to minimize
  impact on load. The backups will be retained based on choice during VM provisioning.&nbsp;<em><strong>These backups are&nbsp;not application aware and as such do not provide transactional consistency. Refer to the Database and Exchange portions of this KB for options to meet this need.</strong></em>
</p>
<ul>
  <li>5 Days of rolling backups, retained within the local data center</li>
  <li>14 Days of rolling backups, with copies stored locally and at a secondary regional data center. &nbsp;Data Center pairings can be found in the <a href="https://t3n.zendesk.com/entries/22023314-Disaster-Recovery-Comparison-Matrix" target="_blank">DR Matrix</a>.&nbsp;</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/WfLAlIfI5SnFrTHRjUgXD6teQ/?name=backup-levels.png" alt="backup-levels.png" />
</p>
<p><em><strong>exhibit (backup user experience)</strong></em>
</p>
<h3>File Server Backup &amp; Recovery Services</h3>
<p>CenturyLink Cloud clients can perform file server backup and recovery using various methodologies. &nbsp;</p>
<h4>Self-Service Volume Shadow Copy Service (VSS) File Backup</h4>
<p>Implementing VSS on a file server provides IT administrators a simple way to restore previous versions of files in a self-service manner. &nbsp;VSS Shadow copies can be scheduled and are stored locally on the virtual machine. &nbsp;See&nbsp;<a href="http://help.tier3.com/entries/21687584-Configuring-Windows-File-level-Backup-VSS-">http://help.tier3.com/entries/21687584-Configuring-Windows-File-level-Backup-VSS-</a>&nbsp;for
  details on enabling VSS file backups.</p>
<h4>Virtual Machine Backup</h4>
<p>As file systems are part of the daily Virtual Machine backup process no additional steps are required to leverage daily backups of file server data. &nbsp;These backups are point in time backups on a daily basis. &nbsp;Clients who are looking for self-service,
  more frequent file server backups or customized retention policies can leverage Object Storage.</p>
<h4>Object Storage&nbsp;</h4>
<p>For clients who are interested in custom data retention policies (length, frequency) over and above the included platform features customers can implement backup services powered by Object Storage. &nbsp;Using 3rd party backup software customers can store
  data on the CenturyLink Cloud Geo-redundant Object Storage platform. &nbsp;Refer to <a href="https://t3n.zendesk.com/entries/23372615-Using-Object-Storage-for-Backup-as-a-Service" target="_blank">https://t3n.zendesk.com/entries/23372615-Using-Object-Storage-for-Backup-as-a-Service</a>&nbsp;</p>
<h3>Database Backup &amp; Recovery Services</h3>
<p>Virtual Machine backups included in the platform do not allow for a crash consistent database backups due to the nature of their design (in flight transactions etc). &nbsp;CenturyLink Cloud clients can implement two methods to achieve crash consistent
  database backups on the platform. &nbsp; &nbsp;</p>
<ul>
  <li>Leverage integrated database backup tool kits that ship with database software such as Oracle RMAN or SQL Maintenance. &nbsp;These tools create backups of logs and databases to localized or remote volumes in a scheduled manner. &nbsp;Typically, localized
    database volume backups are acceptable for smaller environments. &nbsp;Larger database environments may benefit from implementing a storage server, accessible via CIFS or NFS, to centrally house all database backups. There are numerous 3rd party database
    backup products available that can also be leveraged in this fashion. &nbsp;</li>
  <li>For Microsoft SQL environments clients can elect to implement 3rd party backup software backed by Object Storage. &nbsp;These tools typically allow for hot backups using VSS of SQL server transaction logs and databases to a centralized repository. &nbsp;Clients
    can control the frequency of database backups (including logs) and can achieve very aggressive recovery point objectives (RPO) and recovery time objectives (RTO) for their mission critical SQL database services. &nbsp;Refer to&nbsp;<a href="https://t3n.zendesk.com/entries/23372615-Using-Object-Storage-for-Backup-as-a-Service"
    target="_blank">https://t3n.zendesk.com/entries/23372615-Using-Object-Storage-for-Backup-as-a-Service</a>
  </li>
</ul>
<h3>Microsoft Exchange Backup &amp; Recovery Services</h3>
<p>To safely backup and restore Microsoft Exchange mailbox data CenturyLink Cloud recommends implementation of an Object Storage solution. &nbsp;Using 3rd party backup clients allows for complete recovery of message/mailbox (Exchange) data. &nbsp;Clients
  are free to determine their retention periods and frequency for Microsoft application data. &nbsp;Refer to&nbsp;<a href="https://t3n.zendesk.com/entries/23372615-Using-Object-Storage-for-Backup-as-a-Service" target="_blank">https://t3n.zendesk.com/entries/23372615-Using-Object-Storage-for-Backup-as-a-Service</a>
</p>
<p><em>* The use of Object Storage is not meant to replace application high availability features such as Exchange DAG</em>
</p>
<h3>Recovery Options</h3>
<h4>Complete VM Restoration</h4>
<p>A complete VM restoration can be performed based on the retention period chosen. &nbsp;This type of restore is typically used to recover from operating system or other OS related failures (i.e. BSOD). &nbsp; &nbsp;&nbsp;</p>
<h4>File or Directory Restoration</h4>
<p>Specific files and/or directories can be restored upon request based on retention period selected. &nbsp;The CenturyLink Cloud NOC will attach the entire volume on which the data resides to the virtual machine, allowing clients to selectively retrieve/restore
  the files/directories required. &nbsp;By attaching volumes customers can be assured their data is not accessed by support personnel for security reasons. &nbsp;</p>
<p>Clients who implement Object Storage for File Services can leverage the 3rd Party software GUI to restore files/directories on-demand.&nbsp;&nbsp;</p>
<h4>Application Restoration</h4>
<p>Clients who implement application backup services using Object Storage can perform very granular data recovery. &nbsp;The 3rd party client interface permits SQL DBAs and Exchange administrators to restore messages, mailboxes, logs, databases and various
  other data components on-demand. &nbsp; &nbsp; &nbsp;&nbsp;</p>
<h3>How to Request Data Restoration</h3>
<p>To request service please submit a ticket to the CenturyLink Cloud NOC via&nbsp;<a href="http://help.tier3.com/">http://help.tier3.com</a>. &nbsp;Include the following information:</p>
<ul>
  <li>Customer Name</li>
  <li>Server Name</li>
  <li>Type of Recovery (VM, Volume)</li>
  <li>Desired restore point</li>
  <li>Any specific recovery specification or instructions (i.e. restore location)</li>
</ul>
<h3>Frequently Asked Questions</h3>
<p><strong>Q:&nbsp; How long will it take to restore my data?</strong>
</p>
<p>Data restoration times are a variable component. &nbsp;The volume of data to be restored affects the time to restore. &nbsp;Clients are encouraged to request a time estimate based on the restore request from the NOC. &nbsp;</p>
<p><strong>Q:&nbsp;</strong><strong>&nbsp;How far back can data be restored?&nbsp;</strong>
</p>
<p>Virtual Machine Data restoration is based on the retention chosen for the server (5 or 14 Days). &nbsp;Data is restored from scheduled nightly backups. &nbsp;Clients who implement object storage services may have unique retention periods. &nbsp;</p>
<p>Clients can invoke snapshots via the self-service interface for point-in-time recovery from environment changes or upgrades. &nbsp;Details can be found @ <a href="http://help.tier3.com/entries/21381762-Creating-and-Managing-Server-Snapshots">http://help.tier3.com/entries/21381762-Creating-and-Managing-Server-Snapshots</a>.</p>
<p><strong>Q: &nbsp;Are copies stored in the secondary regional data center secure?</strong>
</p>
<p>Virtual Machine backups are encrypted using AES-128 or higher during transfer between CenturyLink Cloud federated regional data centers. &nbsp;These transfers take place over IPSEC Tunnels. &nbsp;</p>
<p><strong>Q: &nbsp;How long until a deleted VM is fully removed from the system?<br /></strong>
</p>
<p>The virtual machine will be removed from the system based on what type of retention period is selected. Data will be removed from the system on the 6th or 15th day depending on retention chosen.</p>
<p><strong>Q: &nbsp;Do daily backups occur regardless of the VM's operating state? &nbsp;(running, stopped, paused, archived)<br /></strong>
</p>
<p>VMs in running, stopped or paused states receive daily backups. VMs in the archived state do not receive daily backups.&nbsp;</p>
