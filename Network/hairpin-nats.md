{{{
  "title": "Hairpin NAT",
  "date": "8-29-2019",
  "author": "Stephen Akers",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This article discusses what a Hairpin NAT is and its support within CenturyLink Cloud

### What is a Hairpin NAT?
Also referred to as "hairpinning", [hairpinning](//en.wikipedia.org/wiki/Hairpinning) describes a communication between two hosts behind the same NAT device using their mapped endpoint.

### Hairpinning/Hairpin NAT support
CenturyLink Cloud supports Hairpinning/Hairpin NAT services at a platform level globally. Any **new or existing** public IP addresses are provided this functionality.

### How Hairpin NAT works within CenturyLink Cloud
Hairpin NAT optimizes the path that traffic takes between servers within CenturyLink Cloud.  When a cloud server initiates traffic to a public IP address that is hosted in the same datacenter, the hairpin functionality keeps the traffic internal to the datacenter edge network infrastructure as it does not need to be forwarded to the internet.  Therefore a cloud server can communicate with another cloud server in the same datacenter using the private or public IP.

Hairpin flow example - Destination server 10.10.20.x with public IP 65.151.148.x
1. CLC server 10.20.30.x sends a packet to 65.x.x.x 
2. Edge infrastructure notes that 65.x.x.x has a NAT to 10.10.20.x and forwards packet to 10.10.20.x

### Restricting source traffic and Hairpin NAT

|Source|Destination|Value to add to source traffic list|
|-------|-----------|---------|
|CLC Public IP|CLC Public IP|Source public IP|
|CLC Private IP|CLC public IP|Public NAT pool address range*|

\*Due to security concerns with using the public NAT pool in a source traffic restriction list, CenturyLink Cloud recommends that a public IP is assigned to the source server.

\*Note that CLC is performing infrastructure upgrades that change the behavior of the Private IP NAT hairpin.
If you have CLC Private IPs in the source traffic restriction list and traffic is not passing, please contact support for assistance at help@ctl.io.

### FAQ

#### Question: Am I using Hairpin NAT?

Answer: A typical scenario for Hairpin NAT would be when a DNS name is referenced by a CLC server that does not have a public IP address.  The server would access xyz.com which resolves to a CLC hosted public address.  CenturyLink Cloud recommends that a private DNS be used for CLC servers which can be used to provide the internal IP which does not need to traverse the edge.

#### Question: Should I use Hairpin NAT?
Answer: CenturyLink Cloud recommends that the internal IP address should be used as it will take a more optimal path and not need to be processed by the edge network infrastructure.  Typically a DNS server internal to your account can be used to reference the internal CLC address.

#### Question: Do I need to include IPs from my Site to Site IPSec VPN, CNS or NetX link in the public IPs source traffic restriction list?

Answer: No. There is no path/route on those links to a server's public IP.  All communications over these types of links is to the private address of the VM. 

#### Question: I have CLC private IPs in my source traffic restriction list to allow for Hairpin NAT and I cannot reach the public IP anymore.

Answer: This is due to a CLC infrastructure upgrade to the edge routing infrastructure that changed the behavior of the Hairpin NAT.  You will need to either add a public IP to the source CLC server and include the newly added public IP in the source traffic restriction list or you can bypass Hairpin Nat by using the private IP of the destination instead of the public IP.
