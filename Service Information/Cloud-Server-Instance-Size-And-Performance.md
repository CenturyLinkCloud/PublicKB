---
title: Cloud Server Instance Size and Performance
author: Joe Smith
tags:
  - four
  - five
date: 7-10-2014
---

##Cloud Server Instance Size and Performance
The CenturyLink Cloud Platform does not offer predefined "instance types" but rather, lets users provision servers with any combination of resources they want. The platform is designed to deliver predictable performance for each machine regardless of size and data center. Costs are incurred hourly and based on the amount of CPU, memory and storage resources allocated.

####Maximum Resources (Standard)

* 16 vCPU, with at least 2 GHz per vCPU
* 128 GB memory
* 17-60 GB root drive
* 4 TB total VM storage (up to 4 drives of 1 TB apiece)
The max configuration for a given Standard virtual machine is 16 vCPU, 128 GB of memory and 4 TB of storage. 
 
####Maximum Resources (Hyperscale)

* 16 vCPU, with at least 2 GHz per vCPU
* 128 GB memory
* Up to 1 TB Storage (SSD)
The max configuration for a given Hyperscale virtual machine is 16 vCPU, 128 GB of memory and 1 TB of storage.

####Maximum Throughput

* **Virtual Machine vNIC**
	* up to 10 Gbps vNIC depending on OS Template
* **Firewall (between VLANs)**
	* up to 6 Gbps
* **Firewall (external)**
	* up to 2 Gbps
* **Load Balancer**
	* 200 Mbps to 1 Gbps (based on unit size purchased)
	* SSL Offload: up to 750 new SSL requests/second
* **VPN (client)**
	* up to 20 Mbps
	* Max Concurrent Connections: 19 (higher volumes available)
* **VPN (IPSEC)**
	* up to 1 Gbps
* **Standard VM-based Storage**
	* Latency: 5ms
	* Performance: Minimum IOPS (2500), Maximum IOPS (20,000) with 4KB block size
* **Hyperscale VM-based Storage**
	* Performance: Minimum of 15,000 IOPS

####How We Allocate Compute Resources

For organizations that are used to working with their own data centers, the term of "compute resources" means how many CPUs and cores that are included in a server. Traditionally, these resources are allocated once when the server is purchased. With the increasing prevalence of server virtualization, developers and administrators are growing comfortable with compute resources that can easily change over time. Cloud computing takes this paradigm further by not only charging per hour (instead of for the life of the server), but also shielding the user from the underlying infrastructure that hosts the virtual machines. Each vCPU requested by a customer is equivalent to a **2 GHz or faster Intel Xeon processor**. These resources are then managed by the hypervisor to ensure that all server instances on the physical host receive predictable performance while maximizing the overall performance of the physical host. CenturyLink Cloud closely monitors the server clusters and ensures that CPU and RAM utilization never surpass 50-70% to allow enough headroom for spikes and peak traffic. 