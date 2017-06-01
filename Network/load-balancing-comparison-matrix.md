{{{
  "title": "Load Balancing Comparison Matrix",
  "date": "5-23-2017",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Overview

CenturyLink Cloud offers customers a wide range of load balancing solutions in our product catalog.  Customers who wish to quickly review the choices along with features and capabilities can use the comparison matrix below.

### Comparison Matrix

**Feature**|**LBaaS<br>(Legacy)**|**LBaaS**|**Citrix VPX<sup>4</sup><br>(Dedicated)**|**[Marketplace](../Ecosystem Partners/Partner Integration Resources/ecosystem-program-resources.md)**
-----------|---------------------|---------|-----------------------------------------|-------------
Control Integration<sup>1</sup>|Yes|Yes|No|No
High Availability|Yes|Yes|Optional|Optional
Mode/Port|TCP/80<br>TCP/443|HTTP<br>TCP/Any|Any|Any
Method|Round Robin<br>Least Connection|Round Robin<br>Least Connection<br>SourceIP<br>URL Hash|[Listing](http://docs.citrix.com/en-us/netscaler/11-1/load-balancing/load-balancing-customizing-algorithms.html)|Varies by<br>Vendor
Persistence|SourceIP|SourceIP|[Listing](http://docs.citrix.com/en-us/netscaler/11-1/load-balancing/load-balancing-persistence/persistence.html)|Varies by<br>Vendor
Health Checks|No|[Yes](../LBaaS/getting-started-with-load-balancer-as-a-service.md)|Yes|Yes
SSL Offloading|No|No|Yes|Yes
WAF|No|No|Optional|Optional
Global Server Load Balancing|No|No|Optional|Optional
[SLA](//www.ctl.io/legal/sla/)<sup>2</sup>|Yes|Yes|Limited|Limited
[Support](../Support/how-do-i-report-a-support-issue.md)<sup>3</sup>|Yes|Yes|Limited|Limited
Lifecycle Management<sup>6</sup>|Day 0<br>Day 2<br>Day N|Day 0<br>Day 2<br>Day N|Day 0|Day 0
[Locations](../General/centurylink-cloud-data-center-locations.md)|Any|VA1<br>UC1<br>CA3<br>GB3<br>SG1|Any|Any
OSI Model<sup>5</sup>|Layer 4|Layer 4|Layer 4<br>Layer 7|Layer 4<br>Layer 7

<sup>1: Control Integration at a minimum allows a customer to implement the service on-demand, operate it via self-service in the UX (or using API) with a pay as you go model.</sup>

<sup>2: [SLA](//www.ctl.io/legal/sla/) is defined as an agreement between CenturyLink and the customer to honor service availability for load balancing specific services via a master service agreement. [Limited SLA's include Virtual Machine availability only.](//www.ctl.io/legal/sla/)</sup>

<sup>3: [Support](//www.ctl.io/support/) is defined as an agreement between CenturyLink and the customer to provide technical support and incident management for the load balancing service. Tracking a Dedicated Load Balancer license expiration date is performed by the customer, please reference our [License Management Article](../Network/dedicated-load-balancer-license-management.md). **Limited Support provides customer service engineers to confirm the infrastructure state and virtual machine state.  Customers are responsible for all Day 1, 2 and N operational support.**</sup>

<sup>4: [CenturyLink offers](//www.ctl.io/pricing/) various pricing models for the Citrix VPX virtual appliance based on performance and availability needs.  Customers can elect to upgrade **[edition](//www.citrix.com/products/netscaler-adc/platforms.html#editions)** and **availability** configurations at any time.

<sup>5: Layer 4 is related to fourth layer of the OSI model: transport level. For example: TCP and UDP protocols are transport level. Layer 7 is related to seventh layer of the OSI model: application level. For example: HTTP, FTP, SMTP, DNS protocols are application level.</sup>

<sup>6: CenturyLink provides lifecycle management based on Day 0 (Install: Import, IP Device), 1 (Configure, Operate), 2 (Optimize, Compliance) and N (Upgrade, Patching) methodologies.  Customers are responsible for any operational support that is not included in the base offering.

  ![Lifecycle Management](../images/lifecycle-management.png)

### Additional Details
The links below provide supporting material that can assist a customer with further evaluating the proper load balancing service for their needs.

* [Citrix Netscaler VPX Documentation](http://docs.citrix.com/en-us/netscaler/11-1.html)
* [Citrix Netscaler VPX Editions](//www.citrix.com/products/netscaler-adc/platforms.html#editions)
* [CenturyLink Ecosystem Partners](../Ecosystem Partners/General/ecosystem-partner-list.md)
* [CenturyLink Pricing Catalog](//www.ctl.io/pricing/)
* [CenturyLink Cloud Legal Documentation (SLA, Service Guide etc)](//www.ctl.io/legal/)
