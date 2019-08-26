{{{
  "title": "Hairpin NAT",
  "date": "2-26-2016",
  "author": "Chris Little",
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
1. CLC server 10.20.30.x sends a packet to 65.151.148.x 
2. Edge infrastructure notes that 65.151.148.x has a NAT to 10.10.20.x and forwards packet to 10.10.20.x

### Restricting source traffic and Hairpin NAT

|Source|Destination|Value to add to source traffic list|
|-------|-----------|---------|
|CLC Public IP|CLC Public IP|Source public IP|
|CLC Private IP|CLC public IP|Public NAT pool address range*|

\*Due to security concerns with using the public NAT pool in a source traffic restriction list, CenturyLink Cloud recommends that a public IP is assigned to the source server.

\*Note that CLC is performing infrastructure upgrades that change the behavior of the Private IP NAT hairpin.
If you have CLC Private IPs in the source traffic restriction list and traffic is not passing, please contact support for assistance at help@ctl.io.
