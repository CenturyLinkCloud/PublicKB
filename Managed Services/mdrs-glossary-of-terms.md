{{{
"title": "Managed Disaster Recovery Services Glossary of Terms",
"date": "08-04-2017",
"author": "Daniel Morton",
"attachments": [],
"contentIsHTML": false
}}}

**Business Continuity** -  Ensures that an organization can continue to deliver products or services at acceptable predefined levels in the event of a serious incident or disaster and is able to recover to an operational state within a reasonably short period. There are three key elements involved: resilience, recovery, and contingency.

**Central Managed Server** - SafeHaven Central Managed Server is part of SafeHaven cluster. It gathers information about the status of SafeHaven Replication Nodes (SRN), protection groups, recovery point history, job history, WAN sync speed, un-synced data, and presents the information via SafeHaven Console. The Central Managed Server receives commands from the SafeHaven Console and distributes the commands to SRNs to execute the commands.

**CenturyLink Cloud** - CenturyLink Cloud is a single cloud platform offering secure enterprise cloud services ideal for business apps, IaaS, PaaS, SaaS, DBaaS, and cloud management via an intuitive Control Portal.


**Client Server** - A Client Server is server used to launch the SafeHaven Console, which is a Graphical User Interface. It must be a Windows machine with the proper Java version installed.

**Disaster Recovery Plan** - The Disaster Recovery Plan is a SafeHaven built-in plan which maps production servers to recovery servers and defines the boot up and power off sequence of the servers in each protection group.

**Failback** - Failback is the process of restoring operations to the primary site. SafeHaven Failback is protection group based. There is no data loss for SafeHaven Failback. After SafeHaven Failback, the DR solution is restored to the same status as before disaster. During failback Managed Disaster Recovery Services coordinate with different CenturyLink teams MS SQL, AD, SAP, etc., to restore applications.

**Failover** - Failover switches the workloads from the production site to the recovery site. SafeHaven Failover is protection group based so that applications and servers in the same group are consistent. SafeHaven Failover stops the WAN sync from the primary site to the recovery site and brings up the recovery servers based on the selected checkpoints. During failover Managed Disaster Recovery Services coordinate with different CenturyLink teams MS SQL, AD, SAP, etc., to restore applications.

**In-Band-to-Out-of-Band Conversion** - In-Band-to-Out-of-Band Conversion is a procedure, which boots up recovery servers from local disks instead of the network disks.

**Local Cache** - Local Cache is a type of protection group, which adopts a small amount of storage acting as a WAN sync cache to transmit data from the production site to the recovery site.

**Local Replica** - Local Replica is a type of protection group. It keeps a copy of the server image on the primary site for WAN sync and recovery purposes.

**Local Replication** - Local Replication means copying data from the primary disks to the SafeHaven managed disks.

**Local Replication Agent** - Local Replication Agent is an agent installed on the primary Windows servers to perform replication from primary disks to the SafeHaven managed disks.

**Major Release** - Major Releases (X.y.z) are vehicles for delivering major and minor feature developments and enhancements to existing features. They incorporate all applicable error corrections made in prior Major Releases, Minor Releases, and Patch Releases.

**Minor Release** - Minor Releases (x.Y.z) are vehicles for delivering minor feature developments, enhancements to existing features, and defect corrections. They incorporate all applicable error corrections made in prior Minor Releases.

**Periodic DR Report** - Periodic DR Report is sent to the customer by email to demonstrate the SafeHaven cluster information, protection group status, WAN sync speed, RPO, and un-synced data. The customer can obtain a general idea of the DR solution through the Report.

**Primary Server** - The primary server bears the customer workloads.

**Protection Group** - A SafeHaven Protection Group contains one or more application servers with a single recovery policy. We recommend grouping multiple interdependent servers into one protection group to maintain application consistency during failover and failback.

**Recovery Point** - SafeHaven Recovery Point is used to perform test-failover and failover. It offers the ability to fail over a protection group to a specific point in time. The Recovery Point is used to determine the RPO.

**Recovery Point Interval** - Recovery Point Interval is a time span in which to achieve a recovery point. RPO is decided by the Recovery Point Interval.

**Recovery Point Objective (RPO)** - Recovery Point Objective is the maximum targeted period in which data might be lost from an IT service due to a major incident.

**Recovery Server** - A recovery server is a stand-by server of the primary server. In the SafeHaven solution, the Recovery Server is only powered on during test-failover or failover.

**Recovery Time Objective (RTO)** - Recovery Time Objective is the targeted duration of time and a service level within which IT Infrastructure or business process must be restored after a disaster to avoid unacceptable consequences associated with a break in business continuity.

**SafeHaven Cluster** - The SafeHaven Cluster is the fundamental infrastructure. It consists of one SafeHaven CMS and multiple pairs of SafeHaven SRNs. Protection groups reside under the cluster.

**SafeHaven Console** - SafeHaven Console is a Graphical User Interface (GUI) used to manage SafeHaven solutions. It displays such information as data centers, SafeHaven nodes, and protection groups. Users can change the WAN sync speed, checkpoint interval, configure the periodical report, and configure the built-in disaster recovery plan via the SafeHaven Console.

**SafeHaven Replication Node** - SafeHaven Replication Node is an Ubuntu server controlling protection group WAN sync. The node also executes the test-failover, failover, and failback commands. A protection group is built between a pair of SafeHaven Replication Nodes.

**Test-failover** - SafeHaven test-failover is the test of the solution without interruption to the primary server workloads.

**WAN Sync** - WAN sync copies data from the SafeHaven cache or replica disk to the recovery site.
