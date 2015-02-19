{{{
  "title": "CenturyLink Cloud Use Case: Extending Customer Active Directory Infrastructure",
  "date": "1-29-2014",
  "author": "Eric S",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Customers of CenturyLink Cloud often already have their own Active Directory (AD) infrastructure with DNS for user logins, name resolution along with other services that AD offers. This article will explain how to extend current AD infrastructure to their cloud servers using IPSEC VPN tunnel and/or MPLS.

### Audience

Active Directory (AD) Domain Administrators

### Prerequisites

* [Creating and Deleting VLANs](creating-and-deleting-vlans.md)
* [Creating a Self-Service IPsec (Site-to-Site) VPN Tunnel](creating-a-self-service-ipsec-site-to-site-vpn-tunnel.md)

  Setup an IPSEC VPN tunnel that allows communication between the VLAN your new AD servers will live on and your current AD servers. The new VM must be able to reach the existing domain controllers or these steps will not work.

### Description

1. Create a VM or 2 (recommended for HA) that will be used has the domain controllers. Set the DNS setting to resolve to the current AD/DNS servers. When creating the server set the primary and secondary DNS setting to be the current onsite AD/DNS server.
2. Log into the newly created VM. Ping the AD/DNS server to ensure it can be reached. This step is vital. Ensure your VM can reach your current AD servers before continuing.
3. Run dcpromo on the server to make the VM a new domain controller in the current domain. repeat for the other VM if applicable.
4. Set up AD sites based on IP subnets to ensure that new VMs created and added to the domain use the newly created AD servers for authentication. Technet instructions can be found here: https://technet.microsoft.com/en-us/library/cc732761.aspx
5.  Add the new domain controllers to the new site.

Options: Leverage MPLS connections or direct connects to connect your cloud environment to the location of your current AD infrastructure. Often customers will leave the IPSEC VPN tunnel in place for redundancy.
