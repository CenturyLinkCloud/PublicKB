{{{
  "title": "Public IP Migration FAQs",
  "date": "05-20-2020",
  "author": "Ben Heisel",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Description

This communication is an important announcement regarding the migration from CenturyLink Cloud public IPs. This document is to provide CenturyLink Cloud customers with information how to identify if a public IP is impacted and how to migrate.

###  What IPs Are Legacy And Require Migration

Any CenturyLink Cloud public IP that is not within the following range is an impacted IP and will require migration: 65.151.128.0/17 (65.151.128.0 - 65.151.255.255).

### Why Is Migration Happening?

* Better governance over our networks 
* Increased security by adding DDoS mitigation in the new IP ranges (something we were unable to do before) 


### Frequently Asked Questions

**Q: What products will be impacted?**

* Servers using public IP addresses 
* Existing IPSec (Site-to-Site) VPN tunnels 

**Q: How do I migrate a public IP assigned to a server?**

Simply remove and assign a new public IP via the Control Portal and a new IP within the range 65.151.128.0/17 will be assigned. Our [Public IP Article](../network/centurylink-cloud/how-to-add-public-ip-to-virtual-machine.md) provides detailed instructions.

**Q: How do I migrate an existing IPSec VPN**

Our [March 31 Release Notes](../release-notes/2020/2020-03-31-cloud-platform-release-notes/.md) recently announced that any changes to an existing self-service IPSec VPN will automatically update the CLC peer IP using the new IP range. 

Custom IPSec VPNs that are not displayed in the Control Portal will require manual configuration changes to complete migration. Please contact our Customer Care Team via help@ctl.io for assistance.

**Q: When is migration required?**

A final migration date is not yet available, more information will be provided regarding final deadlines. Our desire was to publish information and provide as much advanced notice as possible. Migration is encouraged at the earliest possible customer convenience.
