{{{ "title": "CenturyLink Private Node",
"date": "06-09-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Table of contents

* [Service Description](#service-description)
* [User Experience](#user-experience)
* [Deployment Details](#deployment-details)
* [Expansion Modules](#expansion-modules)
* [Configuration Notes](#configuration-notes)
* [Business Terms](#business-terms)

### Service Description

CenturyLink Private Node (“Private Node”) is a managed, private, and physically isolated deployment of a CenturyLink Cloud data center for a specific Customer. As a result, the Private Node data centers are single tenant and exclusively managed by the Customer. CenturyLink provides the infrastructure including space, power, standard compute resources, storage resources, network switching infrastructure, access to the Internet, cloud automation and orchestration software, virtualization licensing, management and monitoring of the infrastructure, and use of the CenturyLink Cloud Control Portal and API. The Private Node Service is covered by the CenturyLink Cloud Enterprise level SLA.

### User Experience

The Private Node Service operates identically to the CenturyLink Cloud public service where Customers use the Control Portal and/or the API to interact with the Service. When Customers log into the Control Portal, the Private Node data center is visible along with all the CenturyLink Cloud public data centers so customers have total access to both the public and private data centers via a uniform user interface and API. Consistent with the public cloud, customers that want to restrict access to any data center to all or a subset of their users may do so via Control Portal settings. This enables the Customer to limit users to only the Private Node data center(s), should they desire to do so.

### Deployment Details

Private Node is hosted in a CenturyLink data center in a colocation space only accessible by CenturyLink employees. Colocation power is also included as part of the Service. CenturyLink provides full monitoring and maintenance of all the equipment used to deliver the Private Node solution. The Private Node solution is designed for redundancy to achieve the Enterprise level SLA. The CenturyLink Cloud platform software is updated by CenturyLink consistent with the public cloud which is generally done once a month. Private Node Customers get all the updates and new features added to Control portal and the APIs over time. Connectivity to the CenturyLink Internet backbone is provided as part of the solution. Consistent with the CenturyLink Cloud public service, Customers are responsible for the OS and application layer, including licensing, management, and monitoring, of the virtual machines. However, software licensing, Managed Operating System and Application services are available for purchase for Customers as an option.
CenturyLink Private Node includes the following for the Baseline Deployment Spec (1/4 rack):

Baseline Deployment|Features & Capacity
-------------------|--------
1/4 Rack|308 Physical Cores<br>2,816GB of Physical RAM<br>110TB Usable Flash SSD Storage<br>Management infrastructure necessary for CenturyLink to operate, monitor and manage the solution<br>Enterprise support level SLA<br>CenturyLink colocation space, power and physical security

### Expansion Modules

Compute and Storage — Expansion Modules adds more compute and storage capacity to the initial CenturyLink Private Node baseline deployment. Each expansion module provides the following to support your growth of virtual servers:
* 448 Physical CPU Cores
* 4,096 GB of Physical RAM
* 160TB Usable Flash SSD Storage

The table below provides a holistic view of the usable resources based on the baseline and expansion modules:

Deployment Type|Capacity
---------------|--------
Baseline (1/4 rack)|308 Physical CPU Cores<br>2,816 GB of Physical RAM<br>110TB Usable Flash SSD Storage
Baseline +1 Expansion Module (1/2 rack)|756 Physical CPU Cores<br>6,912 GB of Physical RAM<br>270TB Usable Flash SSD Storage
Baseline +2 Expansion Modules (3/4 rack)|1,204 Physical CPU Cores<br>11,008 GB of Physical RAM<br>430TB Usable Flash SSD Storage
Baseline +3 Expansion Modules (full rack)|1,652 Physical CPU Cores<br>15,104 GB of Physical RAM<br>590TB Usable Flash SSD Storage

### Configuration Notes

*	Each Deployment Type (1/4, 1/2, 3/4 & full Rack) reserves 5 physical nodes for management and the control plane.
*	Core counts are based on Two (2) Intel E5-2660v4 CPUs, for a total of 28 CPU Cores per Physical Server
* Private Node can be deployed in CenturyLink data centers across North America, Europe, and Asia Pacific.
* Private Node supports up to 2,000 VLANs and can sustain up to 3 Gbps of Internet connectivity.
* Private Node does not support object storage as a service. Customers needing object storage services may purchase that via the CenturyLink Cloud public service.
* Customers do not have physical access to the Private Node equipment within the Colocation space.
* The Private Node Service may take up to four months to deploy from the date Customer executes the Service Order to Customer acceptance in North America and EMEA. Asia Pacific based deployments may take a longer period of time. CenturyLink selects the equipment used in the delivery of the Service.
* CenturyLink Cloud will provide Private Node Customers feedback with regard to overall capacity management of the Service (e.g., if provisioned capacity exceeds recommended utilization levels). Customers are responsible for adding additional expansion modules so that the necessary capacity is in place based on the Customer’s use of the platform. Storage and Compute availability SLAs are voided, should the storage or compute capacity exceed virtual capacity limits which are:
  *	CenturyLink Private Node baseline deployment: 2,464 vCPUS, 2,816 GB RAM, 110 TB of Storage
  *	Compute and Storage Expansion Module: 3,584 vCPUS, 4,096 GB RAM, 160 TB of Storage

### Business Terms

The Private Node infrastructure elements are charged on a fixed monthly recurring basis. Private Node is available in three to five year term commitments. Private Node expansion modules are available in three through five year term commitments. Internet bandwidth, software licensing, managed operating systems, managed application services and additional Service Engineering time is available on a usage fee basis identical to the public cloud.
