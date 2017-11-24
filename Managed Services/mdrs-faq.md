{{{
"title": "Managed Disaster Recovery Services FAQ",
"date": "08-04-2017",
"author": "Daniel Morton",
"attachments": [],
"contentIsHTML": false
}}}

**What are Managed Disaster Recovery Services?**

The Managed Disaster Recovery Services (MDRS) offer a fully-managed disaster recovery (DR) solution that orchestrates multiple DR technologies for the customer. For customers who lack DR expertise or who are short of staff to maintain a DR solution, MDRS takes the responsibilities of DR and delivers end-to-end services. Unlike other DRaaS solutions, CTL MDRS carries out regular testing, audits, and ATOD failover services to ensure the reliability, accuracy and efficiency of our product. The following services are included in MDRS:
* White-glove implementation
* 24x7 monitoring and maintenance
* Regular testing
* Regular audits
* At-time-of-disaster failover services
* Post-disaster failback services
* Runbook development and maintenance

**What does the installation and configuration service include?**

CenturyLink provides an implementation that includes SafeHaven infrastructure deployment, Local Replication Agent (LRA) installation, recovery server configuration, protection group creation, monitoring of system deployment, initial data seeding, and acceptance testing.

Note: Before the implementation, the customer is required to establish the network infrastructure, open the ports, prepare storage, reserve CPU and memory resources, and set up client servers according to the Managed Disaster Recovery Services Implementation Guide and the Managed Disaster Recovery Services Requirement.

**Which operating systems are supported?**

SafeHaven supports VMware vSphere based virtual Windows and Linux servers. The following OS matrix shows supported server types. For OS managed by CenturyLink, restoring Managed OS components on the recovery server is included in the failover services.

| Supported Server | SafeHaven 4.0.2 Local Cache | SafeHaven 4.0.2 Local Replica |
|-------------------------|:----------------:|:----------------------:|
| Windows 2008 Server R1/R2 (64 bit) | X | X |
| Windows 2012 Server R1/R2 (64 bit) | X | X |
| Ubuntu 12/14/16 |   | X |
| RHEL 5/6/7 |   | X |
| CentOS 5/6/7 |   | X |
| openSUSE 11/13 |   | X |

**What are the supported hosting platforms?**

SafeHaven supports VMware vSphere based cloud platforms including: CenturyLink Cloud, CenturyLink Dedicated Cloud Compute, and customer-provided cloud infrastructure that uses VMware virtualization. The following table show the supported primary and recovery hosting platforms.

| Primary Platform | Recovery Platform |
|------------------------|--------------------------|
| CenturyLink Cloud | CenturyLink Cloud |
| Customer provided VMware Datacenter | CenturyLink Cloud |
| Dedicated Cloud Compute | CenturyLink Cloud |

**What application support is there during a recovery?**

For applications using native replication technologies, CenturyLink coordinates with different parties to recover the applications. For applications native to the Windows OS residing on servers protected by SafeHaven, CenturyLink ensures that the services of the applications are started during a failover or a test failover. However, custom configurations in the applications are the responsibility of the customer. Likewise, services that are unable to start due to configuration issues in the applications are also the responsibility of the customer.

**What configuration services does CenturyLink provide?**

CenturyLink provides configuration of the primary disk replication, WAN sync rate, recovery point interval, periodic disaster recovery report system, and the SafeHaven built-in disaster recovery plan. For detailed information on specific configuration roles and responsibilities, refer to the *Managed Disaster Recovery Services Guide*.

**What administrative access does the customer retain?**

The customer is given administrative control to the SafeHaven solution via the SafeHaven Console. The customer is provided login credentials for the SafeHaven cluster from which the customer is able to view SafeHaven nodes, protected servers, protection groups, storage usage, replication status, recovery servers, etc. The customer can adjust certain settings according to their business needs. The customer can also perform certain administrative tasks. For detailed information on customer administrative tasks, refer to the *Managed Disaster Recovery Services Guide*.

**What types of monitoring take place on servers?**

Servers are monitored 24 X 7 X 365. CenturyLink monitors SafeHaven nodes, protection groups, protected Windows servers, and recovered Windows servers. No monitors are deployed on Linux production servers. The following monitoring probes are in place for SafeHaven servers:
* SafeHaven
* RabbitMQ
* SCST
* Apache
* SSH
* SBD Module
* CPU
* Memory
* Disk space
* RPO
* PG
* CMS service

The following monitoring probes are in place for Windows production servers:
* Replication process
* Replication service CPU usage
* Replication service memory usage
* Local replication completion
* SafeHaven installation folder size
* System event log
* LRA replication status
* Connection to local replication disk

For detailed monitor information and frequency intervals, refer to the *Managed Disaster Recovery Services Guide*.

**What types of audit services are covered?**

Audit services identify new servers, disks, applications, deletions, and network and computing resource alterations to the production environment, and also reflect the modifications at the recovery data center. For detailed information on audit scope, refer to the *Managed Disaster Recovery Services Guide*.

**What types of test services are covered?**

SafeHaven test failover is a bubble test in which the CenturyLink managed recovery servers and the corresponding primary servers are isolated. Tests and alterations on the recovery data center are not routed back to a production data center, thus avoiding any disruptions. Critical applications are also started by CenturyLink on recovery servers during testing.

**How often does CenturyLink conduct failover testing?**

CenturyLink delivers semi-annual failover testing during the term of your service year. A customer who requires additional tests can purchase them separately.

**How often can a customer invoke at-time-of-disaster (ATOD) support?**

CenturyLink offers 24 X 7 X 365 ATOD service support for one disaster declaration every contract year. Customers requiring additional ATOD services can purchase the disaster declaration service separately.

**What types of responsibility does the customer assume?**

Generally speaking, the customer is responsible for the following:
* Designates and maintain customer contact during the service term.
* Agrees to meet implementation requirements and standards for on-going support requirements.
* Ensures that production and disaster recovery environments provisioned with servers, local incremental and replica storage, network connectivity, CPU, memory, other infrastructure components and replication are operational.
* Identifies and provides CenturyLink with access to all relevant customer-controlled information, resources, and locations required.
* Purchases the CenturyLink DR Manager, which coordinates the DR implementation, daily maintenance, test, audit, ATOD, and failback procedures.
* Purchases and uses the CenturyLink Cloud as a recovery data center.

Specific details of customer responsibility can be found in the *Managed Disaster Recovery Services Guide*.
