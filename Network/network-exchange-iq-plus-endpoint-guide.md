{{{
  "title": "Network Exchange IQ+ Endpoint Guide",
  "date": "10-31-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### IQ+ Endpoint Guide

The Network Exchange IQ+ Endpoint allows for automated, self-managed connectivity to Cyxtera data centers in which a serving instance of Network Exchange exists.

### IQ+ Endpoint Prerequisites

* An IQ+ connection into the existing shared edge switch (CPE) in a Cyxtera data center must be present.
* The desired site must be supported within Network Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network/network-exchange-connectivity-matrix-configuration-guide.md) for supported data centers.

### IQ+ Endpoint Capabilities

* Choices of 1Gbps and 10Gbps dedicated connectivity between the IQ+ termination point (shared CPE) in the Cyxtera data center and Network Exchange equipment.
* Connections are redundant (two physical connections) to increase gauranteed uptime.
* Automated setup and tear down of connections between the IQ+ equipment (shared CPE) and the End User’s dedicated ports on the terminating Network Exchange equipment. The connection requires 1 VLAN be configured manually.  
* Only the Static routing types is available.

### Notes

* Additional purchase(s) required includes 1 HAN VLAN 1.0 order.
* CenturyLink Technical Implimentation (HSIE) in coordination with CenturyLink Service Delivery Coordinators (SDCs) will configure the VLAN.
* The allocated VLAN will be provided and must be used in the Network Exchange UI.  
* Network Exchange IQ+ Endpoints are available to connect to the shared CPE in Cyxtera data centers only.
* The IQ+ Endpoint must be in a Cyxtera data center in which a serving instance of Network Exchange exists. 