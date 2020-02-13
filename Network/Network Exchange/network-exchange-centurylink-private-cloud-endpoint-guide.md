{{{
  "title": "Network Exchange CenturyLink Private Cloud on VMware Cloud Foundation Endpoint Guide",
  "date": "06-28-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### CenturyLink Private Cloud on VMware Cloud Foundation (VCF) Endpoint Connections

* Starting in mid July, 2018, Network Exchange will have fully automated setup of connections to CenturyLink's new private cloud - [CenturyLink Private Cloud on VMware Cloud Foundation](https://www.ctl.io/centurylink-private-cloud-on-vmware-cloud-foundation/). The addition of CenturyLink Private Cloud on VCF as a Network Exchange Endpoint allows customers to easily connect to a highly secure, scalable, and powerful environment that can be deployed in less than a day. 

### CenturyLink Private Cloud on VMware Cloud Foundation (VCF) Endpoint Connectivity Prerequisites

* The desired CenturyLink Private Cloud on VCF site must be supported within Network Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network/network-exchange-connectivity-matrix-configuration-guide.md) for supported data centers.

### CenturyLink Private Cloud on VCF Endpoint Capabilities

* Rate limit choices of 1Gbps and 10Gbps through shared, redundant bandwidth to and from CenturyLink Private Cloud on VCF.
* Static routing is currently available for connecting to CenturyLink Private Cloud on VCF. BGP will be available soon.
* Fully automated setup and tear down of connections between CenturyLink Private Cloud on VCF and the dedicated ports on the terminating Network Exchange equipment. 

### Notes

* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account.
* Currently, an End User may only add the CenturyLink Private Cloud on VCF endpoint(s) present in the same metropolitan area as the serving instance of Network Exchange. See the [Network Exchange Availability Matrix and Configuration Guide](../Network/network-exchange-connectivity-matrix-configuration-guide.md) for more information.
