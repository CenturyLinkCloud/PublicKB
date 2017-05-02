{{{
  "title": "Network Exchange CenturyLink Colocation Endpoint Guide",
  "date": "04-27-2017",
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

* The End User must initiate a request with the colocation provider for a cross connect between Network Exchange and the End User’s equipment following the provisioning of Network Exchange.
* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the colocation endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one colocation endpoint is served, all may be included in a given Exchange. See the Network Exchange Availability Matrix and Configuration Guide for more information.
