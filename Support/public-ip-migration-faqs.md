{{{
  "title": "Public IP Migration FAQs",
  "date": "11-23-2020",
  "author": "Brandy Smith",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

**Important Update** 
11-23-2020
Lumen Public Cloud (formerly CenturyLink Public Cloud – CLC) has made the decision to not move forward with the IP Migration initiative outlined below. 
Instead, Lumen is pivoting to an internal platform change that will allow for better governance and security over our networks and the platform while not impacting our customers. 
A formal communication will be sent via email to all Lumen Public Cloud customers with more information. 
At this time there is no action required by customers. 

### Description

This communication is an important announcement regarding the migration from Lumen Public Cloud public IPs. This document is to provide Lumen Public Cloud customers with information how to identify if a public IP is impacted and how to migrate.

###  What IPs Require Migration?

Any Lumen Public Cloud public IP that is not within the following range is an impacted IP and will require migration: 65.151.128.0/17 (65.151.128.0 - 65.151.255.255).

### Why Is Migration Happening?

* Better governance over our networks.
* Increased security by adding DDoS mitigation in the new IP range. This is not possible with some of the existing ranges. 


### Frequently Asked Questions

**Q: What products will be impacted?**

* Servers using public IP addresses 
* Existing IPSec (Site-to-Site) VPN tunnels 

**Q: How do I migrate a public IP assigned to a server?**

Simply remove and assign a new public IP via the Control Portal and a new IP within the range 65.151.128.0/17 will be assigned. Our [Public IP Article](../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) provides detailed instructions.

One migration method is to [assign a second internal IP](../Servers/how-to-associate-additional-private-ips-with-a-cloud-server.md) to your server, then add a corresponding new public IP. Next update DNS records to point to the new public IP. Once satisfied with the migration, release the original public IP via the Control Portal. Note, release of the initial internal IP in the Control Portal will require a support request to help@ctl.io.

**Q: How do I migrate an existing IPSec VPN**

Our [March 31 Release Notes](../Release Notes/2020/2020-03-31-cloud-platform-release-notes.md) recently announced that any changes to an existing self-service IPSec VPN will automatically update the CLC peer IP with the new IP range. 

Custom IPSec VPNs that are not displayed in the Control Portal will require manual configuration changes to complete migration. Please contact our Customer Care Team via help@ctl.io for assistance.

**Q: When is migration required?**

A final migration date is not yet available, more information will be provided regarding final deadlines. Our intent is to provide as much advanced notice as possible. Migration is encouraged at the earliest possible customer convenience.

**Q: My Public IP is in the range 65.151.128.0 - 65.151.255.255, is there anything I need to do?**

Nothing is required, your Public IP is already in the correct range.


**Q: How Can I Migrate Existing Public IP Configuration To a New IP?**

Use our API to effeciently gather existing public IP configuration and assign a new public IP with the same configuration:

1. [Authenticate to the API](https://www.ctl.io/api-docs/v2/#authentication)
2. [Get current public IP configuration](https://www.ctl.io/api-docs/v2/#firewall-get-public-ip-address)
3. [Delete the current IP](https://www.ctl.io/api-docs/v2/#firewall-remove-public-ip-address)
4. [Assign a new IP](https://www.ctl.io/api-docs/v2/#firewall-add-public-ip-address) using the configuration parameters gathered in step 2.
**NOTE**, include the current internal IP in the API call to ensure the new public IP is configured with the existing internal IP rather than a new internal IP being assigned with the request. Here is a PUT call Body example:

```
{
	"internalIPAddress": "10.91.172.12",
	"ports": [
		{
            "protocol": "ICMP",
            "port": 0
        },
        {
            "protocol": "TCP",
            "port": 802,
            "portTo": 810
        },
        {
            "protocol": "TCP",
            "port": 9841
        }
    ],
    "sourceRestrictions": [
        {
            "cidr": "8.8.8.8/32"
        }
    ]
}
```
If you wish to add an additional internal IP in the migration process, review our ["How to Associate Additional Private IPs"](../Servers/how-to-associate-additional-private-ips-with-a-cloud-server.md) article. A blueprint can be deployed in the Control Portal or following this [APIv1 documentation](https://www.ctl.io/api-docs/v1/#blueprint-deploy-blueprint).
