{{{
  "title": "Network Exchange CenturyLink Cloud Endpoint Guide",
  "date": "06-28-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### CLC Endpoint Connectivity Prerequisites

* End Users must establish a CenturyLink Cloud (CLC) master account and sub-accounts, the latter to create isolation between the networking resources of the business units of their enterprise. The Exchanges created under each sub-account will be logically isolated from one another.
* For any existing CLC accounts that wish to use Network Exchange, it is necessary to migrate them to a Dedicated VR.  Having a dedicated virtual routing table allows each customer to have their own set of IPs’ from a cloud connectivity standpoint.  A Dedicated VR is also required for automation to work when creating connectivity to the cloud.  
To create a dedicated virtual routing table (Dedicated VR), the VR will need to be created and all existing IP blocks the customer is using will need to converge to the new VR.  To initiate this process, create a ticket with the CenturyLink Cloud help desk.  
* The desired CenturyLink Cloud must be supported within Network Exchange. See the *[Network Exchange Availability Matrix and Configuration Guide](../Network Exchange/network-exchange-connectivity-matrix-configuration-guide.md)* for supported data centers.

### CLC Endpoint Capabilities

* 2 connection speeds (up to) 1Gbps and 10Gbps of shared bandwidth.  
* Fully automated setup and tear down of CenturyLink Cloud connections to the End User’s VLANs.
* CLC firewall rules are automatically updated as CLC endpoints are added or deleted.
* BGP is used for dynamically managing routes between Network Exchange and CenturyLink Cloud.

### Notes

* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account. Dedicated access to CenturyLink Cloud is not supported with Network Exchange.
* Currently, an End User may only add the CenturyLink Cloud Endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. See the *[Network Exchange Availability Matrix and Configuration Guide](../Network Exchange/network-exchange-connectivity-matrix-configuration-guide.md)* for more information.
* A CLC service ticket is not required to add or delete a CenturyLink Cloud endpoint.
* For additional information regarding the Network Exchange architecture and use cases, please see the *[Network Exchange Product Page](https://www.ctl.io/network-exchange/)*.
