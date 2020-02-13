{{{
  "title": "Network Exchange Dedicated Access Endpoint Guide",
  "date": "06-28-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Dedicated Access Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* The desired site must be supported within Network Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network Exchange/network-exchange-connectivity-matrix-configuration-guide.md) for supported data centers.

### Dedicated Access Endpoint Capabilities

* Choices of 1Gbps and 10Gbps dedicated connectivity between the End User’s equipment and Network Exchange equipment.
* Options of a single line connection or a redundant connection (two physical connections) to increase gauranteed uptime.
* Partially automated setup and tear down of connections between the End User’s equipment and the End User’s dedicated ports on the terminating Network Exchange equipment. The Dedicated Access Endpoint requires that one or two cross connects, with number based on redundancy, be implemented.  
* Routing Types of both BGP and Static are available.

### Notes

* Dedicated Access may be used for connecting directly to CenturyLink Managed Hosting and third party networks and devices.
* This document does not apply to CenturyLink endpoints reached through the Managed Area Network (HAN). For HAN-connected endpoints, please refer to the [Network Exchange CenturyLink Managed Hosting via HAN Endpoint Guide](../Network Exchange/network-exchange-clc-managed-hosting-endpoint-guide.md).
* Additional purchase(s) required includes Hosting Access Extension (HAE) - a cross connect - with number of orders matching the number of connections, one for a single line or two for redundant connections. The cross connects will connect Network Exchange and the End User’s equipment following the provisioning of Network Exchange. Network Exchange will provide the equipment location and ports on the Network Exchange switches to be connected to, so the connections can be completed.
* The user will have a choice between a 1Gbps and 10Gbps connection. The optics used to connect to Network Exchange are one of:
  * QFX-SFP-1GE-LX SFP 1000BASE-LX Gigabit Ethernet Optics, 1,310 nm for 10 km transmission on single mode fiber-optic (SMF)
  * QFX-SFP-10GE-LR SFP+ 10GBASE-LR 10 Gigabit Ethernet Optics, 1,310 nm for 10 km transmission on single mode fiber-optic (SMF)
  * QFX-SFP-1GE-T 1000BASE-T SFP Copper SFP, Up to 100M (328 ft.) on Cat 5 unshielded twisted-pair copper cabling
* Service Delivery will obtain the proper optics for the other end of the cross connect, matching speed and type (SMF).
* Currently, an End User may only add Dedicated Access Endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one Dedicated Access endpoint is served, all may be included in a given Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network Exchange/network-exchange-connectivity-matrix-configuration-guide.md) for more information.
