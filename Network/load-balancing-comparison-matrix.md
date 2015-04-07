{{{
  "title": "Load Balancing Comparison Matrix",
  "date": "4-7-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

CenturyLink Cloud offers customers a choice of shared or dedicated load balancing services delivered using Citrix Netscaler VPX devices. The matrix below provides a high level comparison of the two offerings allowing customers to make informed decisions on their **Layer 4** load balancing solution.

### Comparison Matrix

|**Feature**   	|**Shared**   	|**Dedicated**
|:-	|:-	|:-	|
|Control Self-Service|Yes|No
|Availability|Highly Available Pair|Single Instance or Highly Available pair options available
|Load Balancing VIP Ports|TCP/80 & TCP/443|Any
|Load Balancing Algorithms|Round Robin<p>Least Connection|[Citrix Complete Listing](http://support.citrix.com/proddocs/topic/netscaler-load-balancing-93/ns-lb-customizing-lbalgorithms-wrapper-con.html)
|Costing Model|per VIP (NLB Group)|Per Device: VPX-200 or VPX-1000 available in both Standard or Enterprise Edition
|Responsibility for Support and Management|CenturyLink Cloud|Customer via CLI or Web based UI
|Performance|HTTP throughput: 1 Gbps<p>HTTP compression throughput: Up to .75 Gbps<p>**Performance is shared among all clients**|HTTP throughput: 200 Mbps or 1 Gbps<p>SSL encrypted throughput: Up to 1 Gbps<p>HTTP compression throughput: Up to .75 Gbps<p>SSL VPN/ICA Proxy Concurrent Users: Up to 1500<p>New SSL requests/second: Up to 750
|SSL Offloading|No|Yes, Customer Configured
|Health Checks|Yes, TCP & PING|Yes, Customer Configured

### Additional Details
The links below provide additional details on the capabilities and features of the Citrix Netscaler VPX Platform.

* [Shared vs Dedicated Network Load Balancing Architecture Considerations](../Network/load-balancing-dedicated-vs-shared.md)
* [Netscaler VPX Overview](http://www.citrix.com/products/netscaler-application-delivery-controller/features/platforms/vpx.html)
* [Netscaler Editions](http://www.citrix.com/products/netscaler-application-delivery-controller/features/editions.html)
* [Netscaler Load Balancing Algorithms](http://support.citrix.com/proddocs/topic/netscaler-load-balancing-93/ns-lb-customizing-lbalgorithms-wrapper-con.html)
* [How To: Configure Shared Load Balancing Services via Self-Service](../Network/creating-a-self-service-load-balancing-configuration.md)
* [Dedicated Load Balancing Management](../Network/dedicated-load-balancer-basic-management.md)
* [Deploying a Dedicated Citrix VPX Environment in a Multi-tenant Fashion](../Network/deploying-a-dedicated-citrix-vpx-environment-in-a-multi-tenant-fashion.md)
* [System Limits for a NetScaler Appliance](http://support.citrix.com/article/ctx118716)
