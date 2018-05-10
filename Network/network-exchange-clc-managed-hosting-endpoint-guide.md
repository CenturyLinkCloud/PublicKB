{{{
  "title": "Network Exchange CenturyLink Managed Hosting via HAN Endpoint Guide",
  "date": "05-09-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Managed Hosting via HAN Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* The desired Managed Hosting site must be supported within Network Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network/network-exchange-connectivity-matrix-configuration-guide.md) for supported data centers.
* Two instances of Managed Hosting Network (HAN) VLAN Access are required and will be automatically ordered with this Endpoint.

### Managed Hosting via HAN Endpoint Capabilities

* Rate limit choices of 1Gb/s and 10Gb/s through shared bandwidth to and from the [Managed Hosting Network (HAN)](https://www.ctl.io/architecture/cns-architecture/), which is a CenturyLink network infrastructure used to provide connectivity for Managed Server customers, NAS Customers, and other CenturyLink managed services.
* BGP is used for dynamically managing routes between Network Exchange and the End User’s network.
* Near fully automated setup and tear down of connections between the Managed Hosting Network (HAN) and the dedicated ports on the terminating Network Exchange equipment. HAN requires additional configurations performed outside of the Network Exchange portal.

### Notes

* Managed Hosting End Users wishing to connect to Managed Hosting using direct connections should refer to the Network Exchange CenturyLink Managed Hosting Dedicated Access Endpoint Guide.
* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the Managed Hosting endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one Managed Hosting endpoint is served, all may be included in a given Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network/network-exchange-connectivity-matrix-configuration-guide.md) for more information.
