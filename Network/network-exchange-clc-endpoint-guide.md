{{{
  "title": "Network Exchange CenturyLink Cloud Endpoint Guide",
  "date": "04-27-2017",
  "author": "Rob Lesieur",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### CLC Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* The desired CenturyLink Cloud must be supported within Network Exchange. See the Network Exchange Availability Matrix and Configuration Guide for supported data centers.

### CLC Endpoint Capabilities

* Up to 10Gb/s of shared bandwidth to and from CenturyLink Cloud. Network performance is offered as “best effort”. [reference SLA]
* Fully automated setup and tear down of CenturyLink Cloud connections to the End User’s VLANs.
* CLC firewall rules are automatically updated as CLC endpoints are added or deleted.
* BGP is used for dynamically managing routes between Network Exchange and CenturyLink Cloud.

### Notes

* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the CenturyLink Cloud endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one CLC endpoint is served, all may be included in a given Exchange. See the Network Exchange Availability Matrix and Configuration Guide for more information.
* No CLC service ticket is required to add or delete a CenturyLink Cloud endpoint.
