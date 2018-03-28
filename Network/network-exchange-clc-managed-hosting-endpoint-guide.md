{{{
  "title": "Network Exchange CenturyLink Managed Hosting Endpoint Guide",
  "date": "03-28-2018",
  "author": "Marco Paolillo",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Managed Hosting Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* For any existing CLC accounts that wish to use Network Exchange, it is necessary to migrate them to a Dedicated VR.  Having a dedicated virtual routing table allows each customer to have their own set of IPs’ from a cloud connectivity standpoint.  A Dedicated VR is also required for automation to work when creating connectivity to the cloud.  
To create a dedicated virtual routing table (Dedicated VR), the VR will need to be created and all existing IP blocks the customer is using will need to converge to the new VR.  To initiate this process, create a ticket with the CenturyLink Cloud help desk.  

* The desired Managed Hosting site must be supported within Network Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](https://www.ctl.io/knowledge-base/network/network-exchange-connectivity-matrix-configuration-guide/) for supported data centers.
* The End User must separately order two instances of HAN VLAN Access in advance of provisioning Network Exchange. The VLAN IDs supplied by CenturyLink will be used in the provisioning process.

### Managed Hosting Endpoint Capabilities

* Up to 10Gb/s of shared bandwidth to and from the Managed Hosting site. Network performance is offered as “best effort”. 
* BGP is used for dynamically managing routes between Network Exchange and the End User’s network.
* Fully automated provisioning of Exchanges once HAN VLAN Access has been obtained.

### Notes

* This endpoint guide applies to Managed Hosting endpoints connected to other endpoints over the shared network capability of HAN. Managed Hosting End Users wishing to connect to Managed Hosting using direct connections should refer to the CenturyLink Dedicated Access Endpoint Guide.
* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the Managed Hosting endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. Where more than one Managed Hosting endpoint is served, all may be included in a given Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](https://www.ctl.io/knowledge-base/network/network-exchange-connectivity-matrix-configuration-guide/) for available endpoints per metro area.
* An order for two instances of HAN VLAN Access must be placed and the order completed before provisioning the Managed Hosting endpoint.
* For additional information regarding the Network Exchange architecture and use cases, please consult the [Network Exchange Architecture and Technical Guide](https://cloudhelp.ctl.io/knowledge-base/network-exchange-technical-guide/)
