{{{
  "title": "Lumen Cloud Use Case: Extending Customer Active Directory Infrastructure",
  "date": "9-24-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Customers of Lumen Cloud often already have their own Active Directory (AD) infrastructure with DNS for user logins, name resolution along with other services that AD offers. This article will explain how to extend current AD infrastructure to their cloud servers using an IPSEC VPN tunnel and/or MPLS.

### Audience

Active Directory (AD) Domain Administrators

### Prerequisites

Setup an IPSEC VPN tunnel that allows communication between the VLAN your new AD servers will live on and your current AD servers. The new VM must be able to reach the existing domain controllers or these steps will not work.  Please see below links for creating VLANs and creating an IPSEC VPN tunnel on CLC.

* [Creating and Deleting VLANs](creating-and-deleting-vlans.md)
* [Creating a Self-Service IPsec (Site-to-Site) VPN Tunnel](creating-a-self-service-ipsec-site-to-site-vpn-tunnel.md)

### Description

1. Create a VM or two (recommended for HA, best practices is to have two domain controllers per site) that will be used as the domain controllers. Set the DNS setting to resolve to the current AD/DNS servers (ideally, the FSMO role holder which can be quieried using ntdsutil). When creating the server, set the primary and secondary DNS entries to the current onsite AD/DNS server(s).
2. Log into the newly created VM. Ping the AD/DNS server to ensure it can be reached. This step is vital- ensure your VM can reach your current AD infrastructure before continuing.
3. [Set up AD sites based on Sites and vlan subnets](https://technet.microsoft.com/en-us/library/cc732761.aspx) in "AD Sites and Services" to ensure that new VMs created and added to the domain use the newly created AD servers for authentication. Ensure that all sites and subnets have been added- adding sites/subnets will result in the new DCs being automatically placed in the correct location.
4. Run dcpromo on the server to promote the VM to a new domain controller in the current domain; repeat for the second VM if applicable.  If the server(s) are 2012, [install the Active Directory Directory Services (ADDS) role](https://technet.microsoft.com/en-us/library/hh472162.aspx). After reboot, follow the dcpromo wizard. Adprep may need to be run prior to successful DC promotion depending on your forest functional level and your Domain Controller's OS.
5. Verify that the new domain controllers are members of the new sites and subnets.
6. Create forward and reverse lookup zones for all subnets/vLANs in DNS. Verify that the zones/records are being replicated.
7. Verify replication topology by examining "NTDS settings" for each Domain Controller in "Active Directory Sites and Services". Optionally, one can run "dcdiag.exe /v" for a verbose report on Domain Controller configuration, replication and any other issues that may require additional troubleshooting.

Options: Leverage MPLS connections or direct connects to connect your cloud environment to the location of your current AD infrastructure. Customers will often leave the IPSEC VPN tunnel in place for redundancy (or a secondary tunnel for redudancy should the endpoint device support it). Environments with high levels of security restrictions may need to leverage Read-Only-Domain-Controllers (RODC) or varying levels of trusts/configurations depending on what directory information may reside in a Public Cloud.
