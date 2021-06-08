{{{
  "title": "SMTP Traffic",
  "date": "XXXXXXXXX",
  "author": "Derek Jansen",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### SMTP Traffic Filtering for Shared Data Center Egress

As of 26 May 2021, we began blocking SMTP traffic traversing the shared egress NAT in every Public Cloud data center. For any servers without a public IP address assigned, SMTP traffic will be filtered at our firewall.

To avoid SMTP traffic filtering, a public IP address must be assigned to the server per the instructions at <https://www.ctl.io/knowledge-base/network/lumen-cloud/how-to-add-public-ip-to-virtual-machine>.
