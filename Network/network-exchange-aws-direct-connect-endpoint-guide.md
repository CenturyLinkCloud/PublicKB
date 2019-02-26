{{{
  "title": "Network Exchange AWS Direct Connect Endpoint Guide",
  "date": "02-25-2019",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### AWS Direct Connect Endpoint Prerequisites

* End Users must have an AWS account and an [AWS Direct Connect](https://aws.amazon.com/directconnect/) subscription.
* The desired AWS region must be available at a data center in which Network Exchange  is available and can connect to AWS Direct Connect. See the *[Network Exchange Availability Matrix and Configuration Guide](../Network/network-exchange-connectivity-matrix-configuration-guide.md)* for supported data centers.

### AWS Direct Connect Endpoint Capabilities

* Rate limit choices of 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, and 3 Gbps.
* Fully automated setup and tear down of connections between AWS Direct Connect and the dedicated ports on the terminating Network Exchange equipment. 

### Notes

* The Network Exchange fabric leverages the economics of shared networking while logically isolating network traffic between Exchanges, even within the same End User account.

