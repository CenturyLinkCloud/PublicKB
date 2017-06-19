{{{
  "title": "Network Exchange CenturyLink Colocation Endpoint Guide",
  "date": "06-15-2017",
  "author": "Rob Lesieur",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Colocation Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* The desired colocation site must be supported within Network Exchange. See the Network Exchange Availability Matrix and Configuration Guide for supported data centers.

### Colocation Endpoint Capabilities

* Up to 10Gb/s of shared bandwidth to and from the colocation site. Network performance is offered as “best effort”. 
* Choices of 1Gb/s and 10Gb/s dedicated connectivity between the End User’s equipment and Network Exchange equipment.
* Fully automated setup and tear down of connections to the End User’s dedicated ports on the terminating Network Exchange equipment.
* BGP is used for dynamically managing routes between Network Exchange and the End User’s network.

### Notes

* The End User must initiate a request for two instances of "HAE" (HAN Access Extension) - a cross connect - between Network Exchange and the End User’s equipment following the provisioning of Network Exchange. Network Exchange will provide the equipment location and ports to be connected to in order to complete the connections.
* The user will have a choice between a 1Gbps and 10Gbps connection. The optics used to connect to Network Exchange are one of:
  * QFX-SFP-1GE-LX SFP 1000BASE-LX Gigabit Ethernet Optics, 1,310 nm for 10 km transmission on single mode fiber-optic (SMF)
  * QFX-SFP-10GE-LR SFP+ 10GBASE-LR 10 Gigabit Ethernet Optics, 1,310 nm for 10 km transmission on single mode fiber-optic (SMF)
* The user will obtain the proper optics for their end of the cross connect, matching speed and type (SMF). 
* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the colocation endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one colocation endpoint is served, all may be included in a given Exchange. See the Network Exchange Availability Matrix and Configuration Guide for more information.
