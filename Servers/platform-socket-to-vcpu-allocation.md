{{{
  "title": "Platform Socket to vCPU Allocation",
  "date": "12-14-2016",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview
When creating a virtual machine on **CenturyLink Cloud**, Servers will be created with a 1 to 1 ratio of virtual sockets to vCPUs **and** the cores per socket is equal to one. These are VMware vSphere defaults and enables vNUMA to select and present the best virtual NUMA topology to the guest operating system, which will be optimal on the underlying physical topology.

Number of vCPUs|Virtual Sockets|Cores per Sockets
---------------|---------------|-----------------
1|1|1
2|2|1
3|3|1
4|4|1
5|5|1

*and so on....*

### Licensing Impact
Many vendors license and/or limit their applications and services based on any one of the **3** items above. For example, [Microsoft SQL Server 2016 limits](//msdn.microsoft.com/en-us/library/cc645993.aspx) **Standard Edition** to the lesser of 4 Sockets or 24 cores. Thus customers who want to leverage more than 4 vCPUs on CenturyLink Cloud would need to leverage **Enterprise Edition** which does not impose such limits. Customers should carefully review each vendors licensing terms against the delivery model used on CenturyLink Cloud to make sure they comply with those terms and are not procuring more compute than a product is capable of consuming.

### Custom Configurations
Customers can [Submit a Custom Request](../Support/submitting-custom-requests.md) if they require a unique Socket to vCPU ratio.  It is highly recommended by both VMware and CenturyLink to keep the default delivery model for optimal performance and self-service capabilities.  
