{{{
  "title": "CenturyLink Cloud Backup and Recovery Services",
  "date": "7-8-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

The CenturyLink Cloud Platform provides clients with various integrated and custom solutions to protect and rapidly recovery data.

### Exclusions
* Managed Backup Customers

### Standard Server Backup &amp; Recovery Services
All **Standard** Servers in the CenturyLink Cloud platform include a nightly file system backup of the Operating System's running state. These nightly backups start around 8pm (local server time) but are staggered to minimize impact on load. The backups will be retained based on choice during VM provisioning. **These backups are not application aware and as such do not provide transactional consistency. Refer to the Database and Exchange portions of this KB for options to meet this need.**

* Standard Backup: 5 Days of rolling backups, retained within the local data center
* Premium Backup: 14 Days of rolling backups, with copies stored locally and the two most recent copies replicated to a secondary data center. Data Center pairings can be found in the [DR Matrix](../Servers/disaster-recovery-comparison-matrix.md).

### File Server Backup &amp; Recovery Services

CenturyLink Cloud clients can perform file server backup and recovery using various methodologies.

#### Self-Service Volume Shadow Copy Service (VSS) File Backup

Implementing VSS on a file server provides IT administrators a simple way to restore previous versions of files in a self-service manner. VSS Shadow copies can be scheduled and are stored locally on the virtual machine. See [Configuring Windows File Level Backups VSS](../Servers/configuring-windows-file-level-backup-vss.md) for details on enabling VSS file backups.

#### Virtual Machine Backup

As file systems are part of the daily Virtual Machine backup process no additional steps are required to leverage daily backups of file server data. These backups are point in time backups on a daily basis. Clients who are looking for self-service, more frequent file server backups or customized retention policies can leverage Object Storage.

#### Object Storage

For clients who are interested in custom data retention policies (length, frequency) over and above the included platform features customers can implement backup services powered by Object Storage. Using 3rd party backup software customers can store data on the CenturyLink Cloud Geo-redundant [Object Storage platform](../Object Storage/using-object-storage-for-backup-as-a-service.md).

### Database Backup &amp; Recovery Services

Virtual Machine backups included in the platform do not allow for a crash consistent database backups due to the nature of their design (in flight transactions etc). CenturyLink Cloud clients can implement two methods to achieve crash consistent database backups on the platform.

* Leverage integrated database backup tool kits that ship with database software such as Oracle RMAN or SQL Maintenance. These tools create backups of logs and databases to localized or remote volumes in a scheduled manner. Typically, localized database volume backups are acceptable for smaller environments. Larger database environments may benefit from implementing a storage server, accessible via CIFS or NFS, to centrally house all database backups. There are numerous 3rd party database backup products available that can also be leveraged in this fashion.
* For Microsoft SQL environments clients can elect to implement 3rd party backup software backed by Object Storage. These tools typically allow for hot backups using VSS of SQL server transaction logs and databases to a centralized repository. Clients can control the frequency of database backups (including logs) and can achieve very aggressive recovery point objectives (RPO) and recovery time objectives (RTO) for their mission critical SQL database services. Refer to [Using Object Storage for Backup as a Service](../Object Storage/using-object-storage-for-backup-as-a-service.md).

### Microsoft Exchange Backup &amp; Recovery Services

To safely backup and restore Microsoft Exchange mailbox data CenturyLink Cloud recommends implementation of an Object Storage solution. Using 3rd party backup clients allows for complete recovery of message/mailbox (Exchange) data. Clients are free to determine their retention periods and frequency for Microsoft application data. Refer to [Using Object Storage for Backup as a Service](../Object Storage/using-object-storage-for-backup-as-a-service.md).

*The use of Object Storage is not meant to replace application high availability features such as Exchange DAG*

### Recovery Options

#### Complete VM Restoration

A complete VM restoration can be performed based on the retention period chosen. This type of restore is typically used to recover from operating system or other OS related failures (i.e. BSOD).

#### File or Directory Restoration

Specific files and/or directories can be restored upon request based on retention period selected. The CenturyLink Cloud NOC will attach the entire volume on which the data resides to the virtual machine, allowing clients to selectively retrieve/restore the files/directories required. By attaching volumes customers can be assured their data is not accessed by support personnel for security reasons.

Clients who implement Object Storage for File Services can leverage the 3rd Party software GUI to restore files/directories on-demand.

#### Application Restoration
Clients who implement application backup services using Object Storage can perform very granular data recovery. The 3rd party client interface permits SQL DBAs and Exchange administrators to restore messages, mailboxes, logs, databases and various other data components on-demand.

### How to Request Data Restoration

To request service please submit a ticket to the CenturyLink Cloud NOC. Include the following information:

  * Customer Name
  * Server Name
  * Type of Recovery (VM, Volume)
  * Desired restore point
  * Any specific recovery specification or instructions (i.e. restore location)

### Frequently Asked Questions

**How long will it take to restore my data?**

Data restoration times are a variable component. The volume of data to be restored affects the time to restore. Clients are encouraged to request a time estimate based on the restore request from the NOC.

**How far back can data be restored?**

Virtual Machine Data restoration is based on the retention chosen for the server (5 or 14 Days). Data is restored from scheduled nightly backups. Clients who implement object storage services may have unique retention periods.

Clients can invoke [snapshots via the Control Portal](../Servers/creating-and-managing-server-snapshots.md) for point-in-time recovery from environment changes or upgrades.

**Are copies stored in the secondary regional data center secure?**

Virtual Machine backups are encrypted using AES-128 or higher during transfer between CenturyLink Cloud federated regional data centers. These transfers take place over IPSEC Tunnels.

**How long until a deleted VM is fully removed from the system?**

The virtual machine will be removed from the system based on what type of retention period is selected. Data will be removed from the system on the 6th or 15th day depending on retention chosen.

**Do daily backups occur regardless of the VM's operating state?  (running, stopped, paused, archived)**

VMs in running, stopped or paused states receive daily backups. VMs in the archived state do not receive daily backups.
