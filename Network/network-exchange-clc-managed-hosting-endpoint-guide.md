{{{
  "title": "Network Exchange CenturyLink Managed Hosting Endpoint Guide",
  "date": "06-14-2017",
  "author": "Rob Lesieur",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Managed Hosting Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* The desired Managed Hosting site must be supported within Network Exchange. See the Network Exchange Availability Matrix and Configuration Guide for supported data centers.
* The End User must separately order two instances of HAN VLAN Access in advance of provisioning Network Exchange. The VLAN IDs supplied by CenturyLink will be used in the provisioning process.

### Managed Hosting Endpoint Capabilities

* Up to 10Gb/s of shared bandwidth to and from the Managed Hosting site. Network performance is offered as “best effort”. [reference SLA]
* BGP is used for dynamically managing routes between Network Exchange and the End User’s network.
* Fully automated provisioning of Exchanges once HAN VLAN Access has been obtained.

### Notes

* This endpoint guide applies to Managed Hosting endpoints connected to other endpoints over the shared network capability of HAN. Managed Hosting End Users wishing to connect to Managed Hosting using direct connections should refer to the CenturyLink Dedicated Access Endpoint Guide.
* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the Managed Hosting endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one Managed Hosting endpoint is served, all may be included in a given Exchange. See the Network Exchange Availability Matrix and Configuration Guide for more information.
* An order for two instances of HAN VLAN Access must be placed and the order completed before provisioning the Managed Hosting endpoint.
