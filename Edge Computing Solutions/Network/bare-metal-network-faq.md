{{{
  "title": "Bare Metal Network FAQ",
  "date": "2-21-2021",
  "author": "Brent Smith",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}


### Description

Lumen Bare Metal servers are built with connectivity to either the Internet or an MPLS IPVPN (coming soon).
This FAQ addresses how the access to these networks are setup for servers.


### How are IP addresses assigned?

 Each server is assigned its own IPv4 /29 subnet.
 The first three IP addresses are assigned to the upstream routers, with the fourth address assigned to the server.
 The 5th and 6th IP addresses are unassigned and may be utilized by the customer on their server.


**1st IP** – router default gateway

**2nd IP** – reserved for router1

**3rd IP** – reserved for router2

**4th IP** – assigned to server

**5th IP** – unused/available

**6th IP** – unused/available


### How can more IP addresses be assigned to my server?

At this time, additional IP space is not supported. Only the /29 subnet that is assigned to the server can be used.

### How is the network protected against failure?

 Each Edge Bare Metal size server has four 25 Gigabit Ethernet interfaces, with two interfaces on each of two separate NIC cards.
 By default all four interfaces are placed into a single Link Access Group (LAG) or bond utilizing LACP for individual link monitoring.

 Each server connects to two switches: 2x 25GE to switch A and 2x 25GE to switch B.
 These switches are located in the same physical rack as the server.
 Each of these switches have multiple 100GE fiber connections to multiple other switches in the datacenter that create an ethernet switching fabric.
 This switching fabric can sustain full traffic capacity with any single switch or link failure.
 **Note** This switch redundancy means that a server can always expect up to 50 Gbps of throughput, even if one of its directly connected switches were to fail.
 While a server does have 100 Gbps of total bandwidth capacity, half of that is redundant.

Egress from the datacenter’s switch fabric to either the Internet (AS3356) or the MPLS IPVPN network (AS3549) is provided by two diverse Provider Edge (PE) routers – one pair per each network. These PE pairs connect to a corresponding pair of switches in the fabric. Traffic can be forwarded through both PEs and will switchover automatically upon failure of a PE, switch or the link between them. This dual routing path is important to remember when utilizing traceroutes or other reporting. PE1 may be active today but PE2 become the active path tomorrow.

You can learn more about how you are billed for Egress for Edge Bare Metal [here](.../edge-computing-solutions/getting-started/edge-bare-metal-billing/).
