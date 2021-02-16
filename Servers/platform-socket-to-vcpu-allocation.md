{{{
  "title": "Platform Socket to vCPU Allocation",
  "date": "2-20-2018",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview
When creating a virtual machine on **Lumen Cloud**, Servers will be created with a 1 to 1 ratio of virtual sockets to vCPUs **and** the cores per socket is equal to one. These are VMware vSphere defaults and enables vNUMA to select and present the best virtual NUMA topology to the guest operating system, which will be optimal on the underlying physical topology.

Number of vCPUs|Virtual Sockets|Cores per Sockets
---------------|---------------|-----------------
1|1|1
2|2|1
3|3|1
4|4|1
5|5|1

*and so on....*

### Licensing Impact
Many vendors license and/or limit their applications and services based on any one of the **3** items above. For example, [Microsoft SQL Server 2016 limits](//msdn.microsoft.com/en-us/library/cc645993.aspx) **Standard Edition** to the lesser of 4 Sockets or 24 cores. Customers who want to optimize their costs on Lumen Cloud should consider leveraging our [Relational DB for MSSQL service](https://www.ctl.io/relational-database/relational-db-mssql/) for larger compute configurations (> 4 vCPU). This service is designed and implemented in such a way that customers can leverage **Standard or Web Edition** licenses up to 16 vCPU **without** the need to procure **Enterprise Edition**. Customers who wish to deploy and manage their own MS SQL Server virtual machines and database platform will need to purchase **Enterprise Edition** to leverage more than 4 vCPUs on Lumen Cloud due to the socket to vCPU ratios above. Customers should carefully review each vendors licensing terms against the delivery model used on Lumen Cloud to make sure they comply with those terms and are not procuring more compute than a product is capable of consuming.
