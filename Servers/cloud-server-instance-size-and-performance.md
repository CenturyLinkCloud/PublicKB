{{{
  "title": "Cloud Virtual Server Instance Size and Performance",
  "date": "7-8-2015",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

The CenturyLink Cloud Platform does not offer predefined virtual "instance types" but rather, lets users provision virtual servers with any combination of resources they want. The platform is designed to deliver predictable performance for each machine regardless of size and data center. Costs are incurred hourly and based on the amount of CPU, memory and storage resources allocated.

### Maximum Resources (Standard)

* 16 vCPU, with at least 2 GHz per vCPU
* 128 GB memory
* Up to 4 TB storage
    * up to 4 disks of 1 TB apiece
    * up to 15 disks, not exceeding 4 TB

The max configuration for a given Standard virtual machine is 16 vCPU, 128 GB of memory and 4 TB of storage. Refer to [Operating System Root Drive Size](operating-system-root-drive-size.md) for OS Drive Sizes.

### Maximum Resources (Hyperscale)

* 16 vCPU, with at least 2 GHz per vCPU
* 128 GB memory
* Up to 1 TB Storage (SSD)
    * single disk up to 1 TB
    * up to 15 disks, not exceeding 1 TB

The max configuration for a given Hyperscale virtual machine is 16 vCPU, 128 GB of memory and 1 TB of storage. Refer to [Operating System Root Drive Size](operating-system-root-drive-size.md) for OS Drive Sizes.

### Maximum Throughput

Virtual Machine vNIC			  | 10 Gbps
----------------------------|-----------------
Firewall (between VLANs)  	| up to 6 Gbps
Firewall (external) 		  	| up to 2 Gbps
Load Balancer						   	| 100 Mbps to 400 Mbps (based on unit size purchased)<br>SSL Offload: up to 750 new SSL requests/second
VPN (client)							  | up to 20 Mbps<br>19 max concurrent connections (higher volumes available)
VPN (IPSEC)                 | up to 1 Gbps
Standard VM-based Storage   | 5ms latency<br>Minimum IOPS (2500), Maximum IOPS (20,000) with 4KB block size
Hyperscale VM-based Storage | Minimum of 15,000 IOPS

### How Compute Resources are Allocated

For organizations that are used to working with their own data centers, the term "compute resources" means how many CPUs and cores that are included in a server. Traditionally, these resources are allocated once when the server is purchased.

With the increasing prevalence of server virtualization, developers and administrators are growing comfortable with compute resources that can easily change over time. Cloud computing takes this paradigm further by not only charging per hour (instead of for the life of the server), but also shielding the user from the underlying infrastructure that hosts the virtual machines. Each vCPU requested by a customer is equivalent to a 2 GHz or faster Intel Xeon processor. These resources are then managed by the hypervisor to ensure that all server instances on the physical host receive predictable performance while maximizing the overall performance of the physical host.

CenturyLink Cloud closely monitors the server clusters and ensures that CPU and RAM utilization never surpass 50-70% to allow enough headroom for spikes and peak traffic.
