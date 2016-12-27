{{{
  "title": "Migrating Data to and from CenturyLink Cloud",
  "date": "12-22-2016",
  "author": "Mason Elliott",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

There are various ways to migrate data to and from the CenturyLink Cloud. This article lists the most commonly used methods, highlighting factors to consider when making that decision.
CenturyLink Cloud partners may use this resource as a reference when advising their customers on data migration options.

### Physical Media - Service Task

CenturyLink Cloud supports importing and exporting data through portable storage devices into our data centers by shipping removable media directly to CenturyLink. Data imports typically supported by CenturyLink Cloud include, OVFs, OVAs and unstructured data.
This is a relatively cost effective method to unburden the customer from the migration activity.
On the other hand, shipping of data creates delays, as new data continues to be written in the primary location. There is also the possibility of loss or damage of disk during transportation.

### Self-Service VM Import (OVF)

Customers can import OVFs from VMware environments into CenturyLink Cloud when they meet the self-service import requirements [listed here](//www.ctl.io/knowledge-base/servers/self-service-vm-import-ovf-requirements/). This is a low cost method and the customer is in control of the transfer of their data. It is important to note that length of import depends on connection speed /bandwidth at both ends, and the amount of data that needs to be transferred.
There is no cost to OVF since CenturyLink Cloud does not charge for the transfer of data into the CenturyLink Cloud

### VM Import &ndash; Service Task (OVF/OVA)

This is the best option for virtual appliances or other OVF files that do not meet self-service import requirements [listed here](//www.ctl.io/knowledge-base/servers/self-service-vm-import-ovf-requirements/). Take a customer virtual machine and convert to either (a) a running virtual machine or (b) a reusable template. Servers converted. The customer will be asked for details about which account, group, VLAN, and storage type to apply to the imported server.

### SafeHaven Data Migration

CenturyLink [SafeHaven](//www.ctl.io/disaster-recovery/) enables protection of critical applications from unexpected unavailability. Additionally, SafeHaven offers advanced features like Live Failback, Live Test Failover, Custom Check Point Intervals, Protection Groups, and Runbook Automation. While Safehaven is a great tool for enabling turnkey disaster recovery it can also be utilized to help migrate data and workloads from on premises to CenturyLink Cloud and between CenturyLink Cloud locations.

### Native Application Tools

* **Microsoft SQL AlwaysOn** is a preferred method to migrate an existing MS SQL database to CLC. [Click here for more information](//msdn.microsoft.com/en-us/library/ff877884.aspx).

* **AD Replication**: Customers can configure a new Windows Domain Controller in CLC as an addition to their domain controller on-premises via a site-to-site VPN. Replication can automatically be administered to migrate all directory services to CLC.

* **MySQL Replication**: There are many ways to replicate MySQL data natively, including [Binary Log File Replication and utilizing Global Transaction Identifiers](//dev.mysql.com/doc/refman/5.7/en/replication-howto.html).

* **Couchbase Replication**: Couchbase is a popular NoSQL database that is available for deployment within CenturyLink Cloud. Couchbase utilizes clusters for active and replica data and can also replicate data between clusters utilizing XDCR. [Click here for more detail.](//docs.couchbase.com/admin/admin/Tasks/tasks-manage-xdcr.html)


### Third Party Tools

* **Rackware Management Module:** [Find it here](//www.rackwareinc.com/centurylink-migration/).

* **Backup & Restore:** Many 3rd party backup solutions such as [Cloudberry](//www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-cloudberry-lab-backup-enterprise-blueprint/) allow you to back up your on-premise files and restore them into the CenturyLink Cloud via a simple backup and restore procedure. This can be done with a file level backup solution that will allow you to layer the data onto a new CLC VM or utilizing an image level backup solution such as [Double-Take](//www.visionsolutions.com/products/windows/double-take-availability/overview) to restore the entire image.

### File Copy
[Robocopy](//technet.microsoft.com/en-us/magazine/ee851678.aspx) is a popular tool included with Windows that allows for easy file transfer at scale.

### Migration Options Matrix

**Migration Option**|**Description**|**Reference Articles**|**Cost**|**Implementation / Deployment**|**Complexity**
--------------------|---------------|----------------------|--------|-------------------------------|--------------
**Physical Media (Service Task)** |Users can import and export data through portable storage devices into CenturyLink data centers by shipping removable media to CenturyLink.|[Service Task: Data Import-Export](//www.ctl.io/service-tasks/#data-import-export)<br>[Importing and Exporting Data Using a Portable Storage Device](//www.ctl.io/knowledge-base/service-tasks/importing-and-exporting-data-using-a-portable-storage-device/#service-task-prioritization)|$390 initial,<br>$195 each additional hour|Long<br>Days/Weeks|Low
**VM Import (Self-Service)** |Users can import OVFs from VMware environments into CenturyLink Cloud|[Using Self-Service VM Import](//www.ctl.io/knowledge-base/servers/using-self-service-vm-import/)<br>[Self-Service VM Import / OVF Requirements](//www.ctl.io/knowledge-base/servers/self-service-vm-import-ovf-requirements/)|Free to import.<br>Cost for VM resources.|Short<br>Hours|Mild
**VM Import (Service Task)** |Best option for virtual appliances or other OVF files that do not meet self-service import requirements [listed here](//www.ctl.io/knowledge-base/servers/self-service-vm-import-ovf-requirements/). Convert a virtual machine to (a) a running virtual machine or (b) a reusable template. The customer will be asked for details about which account, group, VLAN, and storage type to apply to the imported server.|[Service Task: VM Import](//www.ctl.io/service-tasks/#vm-import)|$195 per hour|Hours/Days|Low
**SafeHaven Data Migration** |Users can leverage SafeHaven DRaaS solution to set up an instance where the customer can migrate data between on-premises and cloud vms. Requires a SafeHaven account and a professional services engagement for onboarding and deployment.|[Disaster Recovery](//www.ctl.io/disaster-recovery/)|$1,850 Quickstart Onboarding<br><br>$45 License per protected VM<br><br>Cost for replication and management nodes (variable)|Days/Weeks|High
**Native Replication Tools** |**Microsoft SQL AlwaysOn:** Preferred method to migrate an existing MS SQL database to CLC.<br>**AD Replication:** Customers can configure a new Windows Domain Controller in CLC as an addition to their domain controller on-premises via a site to site VPN. Replication can automatically be administered to migrate all directory services to CLC.<br>**MySQL Replication:** Native tools for replicating MySQL<br>**NoSQL (Couchbase):** Using XDCR for cluster replication|[Configure AlwaysOn (SQL Server)](//msdn.microsoft.com/en-us/library/ff877884.aspx)<br><br>[Configure MySQL Replication](//dev.mysql.com/doc/refman/5.7/en/replication-howto.html)<br><br>[Cross Data Center Replication](//docs.couchbase.com/admin/admin/Tasks/tasks-manage-xdcr.html)|Free|Hours/Days|Mild
**Rackware Management Module** |RMM is a software product that decouples the application stack from the underlying platform,
allowing it to be ported to any new platform. RMM includes discovery, analysis and automation features, allowing the migration process to be fast, easy and error‐free.|[Rackware for datacenter migration and DR](//www.rackwareinc.com/centurylink-migration/)|Custom Quote Required|Days/Weeks|High
**Backup & Restore** |Many 3rd party backup solutions such as Cloudberry allow you to back up your on-premise data and restore it into the CenturyLink Cloud via a simple backup and restore procedure. This can be done with a file level backup solution that will allow you to layer the data onto a new CLC VM or utilizing an image level backup solution such as Double-Take to restore the entire image.|[Cloudberry Lab Backup Enterprise - Blueprint](//www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-cloudberry-lab-backup-enterprise-blueprint/)<br>[Double-Take](//www.visionsolutions.com/products/windows/double-take-availability/overview)|Varies by Provider|Hours/Days|Mild
**File Copy** |Robocopy is a popular tool included with Windows that allows for easy file transfer at scale.<br><br>Rsync: File Copy for Linux machines|[Robocopy for File Management](//technet.microsoft.com/en-us/magazine/ee851678.aspx)|Free|Hours|Mild
