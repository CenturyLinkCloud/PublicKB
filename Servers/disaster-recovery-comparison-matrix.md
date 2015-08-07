{{{
  "title": "Disaster Recovery Comparison Matrix",
  "date": "6-25-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview

Customers frequently request information on the Disaster Recovery and Business Continuity services offered by CenturyLink Cloud. The Matrix below provides a quick, high level guide to the services available as part of our platform or via customization.  **In order to qualify for Platform DR services a customer must deploy their virtual instances on Premium Storage**. Customers should be aware that any combination of these options, per application or per virtual instance, are possible.

|**Feature**   	|**Platform DR**   	|**Build-to Spec DR**
|:-	|:-	|:-	|
|Recovery Time and Point Objectives|24 Hr RPO / 8 Hr RTO<sup>1</sup>|Customizable to Client RPO/RTO requirements by application or data center.
|Disaster Recovery Data Centers|WA1-Seattle <--> UT1-Salt Lake City<p>IL1-Chicago <--> NY1-New York<p>GB1-Portsmouth <--> GB3-Slough<p>CA2-Toronto --> CA1-Vancouver<p>CA3-Toronto <--> CA1-Vancouver<p>VA1-Sterling <--> UC1-Santa Clara|Source and Destination can be any CenturyLink Cloud Federated Data Center.
|Customer Testing|Yes<sup>2</sup>|Yes, customer-initiated, application-level failover
|Data Replication|Premium Storage Virtual Machines on the CenturyLink Cloud platform include a daily backup of the Operating System's running state.  Copies are stored locally and at a secondary regional data center. These backups are not application aware and as such do not ensure transactional consistency, additional replication methodologies are advised for transactional applications or databases|Customers can create data replication services specific to their application platform using various technologies.  These include, but are not limited to, SQL AlwaysOn Availability Groups, SQL Log Shipping, Exchange DAG, DFS, Rsync and others.
|Network Failover|No<sup>3</sup>|Not required, network failover is addressed architecturally as redundant instances deployed in multiple data centers for data replication and rapid activation.
|Declaration of Disaster|CenturyLink Cloud|Customer

1.  **RPO and RTO figures are objectives, not SLA's.  [Review CenturyLink Cloud SLA's](https://www.ctl.io/legal/sla) for more information.**
2.  **Refer to [CenturyLinkCloud.com](http://www.ctl.io) for service task overview and costs for DR Testing of VM Instances on premium storage**
3.  **includes virtual machine failover only**

### Exclusions
* There are a number of services and components that would not be included as part of the premium storage product set. Exclusions include Custom Templates, Archived Virtual Machines, IPSEC VPN Tunnels, Alert Policies, Metadata (server settings, activity history, statistics).
* [Managed Services](//www.ctl.io/managed-services) are delivered from [select CenturyLink Cloud locations](//www.ctl.io/data-centers) and customers should carefully vet the use of premium storage. If Managed Services are required in the event of a DR event, premium storage may not be the optimal choice.
