{{{
  "title": "Network Filtering",
  "date": "06-14-2021",
  "author": "Derek Jansen",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

This article desribes the network filtering setup for the Public Cloud platform. By default, the platform **does not** filter any network traffic except in the specific cases outlined in this article.

##### SMTP Traffic Filtering for Shared Data Center Egress

As of 26 May 2021, the platform began blocking SMTP traffic traversing the shared egress NAT in every data center. For any servers without a public IP address assigned, SMTP traffic will be filtered at our firewall.

To avoid SMTP traffic filtering, a public IP address must be assigned to the server per the instructions at <https://www.ctl.io/knowledge-base/network/lumen-cloud/how-to-add-public-ip-to-virtual-machine>.
