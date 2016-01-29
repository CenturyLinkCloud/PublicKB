{{{
  "title": "Load Balancing Comparison Matrix",
  "date": "8-18-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Overview

CenturyLink Cloud offers customers a choice of shared or dedicated load balancing services delivered using Citrix Netscaler VPX devices. The matrix below provides a high level comparison of the two offerings allowing customers to make informed decisions on their **Layer 4** load balancing solution.

### Comparison Matrix

**Feature**|**Shared**|**Dedicated**
-----------|----------|-------------
Control Self-Service|Yes|No
Availability|Highly Available Pair|Single Instance or Highly Available pair options available<sup>1</sup>
Load Balancing VIP Ports|TCP/80 & TCP/443|Any
Load Balancing Algorithms|Round Robin<br>Least Connection|[Citrix Complete Listing](http://support.citrix.com/proddocs/topic/netscaler-load-balancing-93/ns-lb-customizing-lbalgorithms-wrapper-con.html)
Costing Model|per VIP (NLB Group)|Per Device: VPX-200 or VPX-1000 available in Standard, Enterprise or Platinum Edition<sup>2</sup>
Responsibility for Support and Management|CenturyLink Cloud|Customer via CLI or Web based UI
Performance|HTTP throughput: up to 400 Mbps<br>**Performance is shared among all clients**|HTTP throughput: Up to 400 Mbps<br>SSL encrypted throughput: Up to 400 Mbps<br>HTTP compression throughput: Up to 350 Mbps<br>SSL VPN/ICA Proxy Concurrent Users: Up to 1500<br>New SSL requests/second: Up to 750
SSL Offloading|No|Yes, Customer Configured
Health Checks|Yes, TCP and PING|Yes, Customer Configured

1. **Customers can optionally pay for an upgrade from a single VPX to an HA pair using a service task**
2. **Customers can optionally pay for in place upgrades of VPX-200 Devices to a higher performance VPX-1000, including the edition, using a service task**

### Additional Details
The links below provide additional details on the capabilities and features of the Citrix Netscaler VPX Platform.

* [Deploy a Dedicated Citrix VPX Appliance using Service Task](../Service Tasks/deploy-a-dedicated-citrix-vpx-appliance.md)
* [Shared vs Dedicated Network Load Balancing Architecture Considerations](../Network/load-balancing-dedicated-vs-shared.md)
* [Netscaler VPX Overview](//www.citrix.com/products/netscaler-application-delivery-controller/features/platforms/vpx.html)
* [Netscaler Editions](//www.citrix.com/products/netscaler-application-delivery-controller/features/editions.html)
* [Netscaler Load Balancing Algorithms](//docs.citrix.com/en-us/netscaler/10-5/ns-tmg-wrapper-10-con/ns-lb-wrapper-con-10/ns-lb-customizing-lbalgorithms-wrapper-con.html)
* [How To: Configure Shared Load Balancing Services via Self-Service](../Network/creating-a-self-service-load-balancing-configuration.md)
* [Dedicated Load Balancing Management](../Network/dedicated-load-balancer-basic-management.md)
* [Deploying a Dedicated Citrix VPX Environment in a Multi-tenant Fashion](../Network/deploying-a-dedicated-citrix-vpx-environment-in-a-multi-tenant-fashion.md)
* [System Limits for a NetScaler Appliance](http://support.citrix.com/article/ctx118716)
