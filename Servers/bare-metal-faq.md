{{{
  "title": "Bare Metal FAQ",
  "date": "06-29-2015",
  "author": "Bryan O'Neal",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

CenturyLink Bare Metal servers introduce the ability to provision and manage physical machines from the CenturyLink Cloud platform in a self-service, on-demand, and highly automated fashion.

This FAQ addresses commonly asked questions about the service. For further information on this service and how it compares to virtual servers, see [Server Comparison Matrix](../Servers/server-comparison-matrix.md).


**What are the available configurations for Bare Metal servers?**

* 4 cores (3.6GHz E3), 16 GB RAM, 10Gb NIC
  * Storage is 2x1TB 7200 RAID 1 (0.91TB usable)
* 12 cores (2.4GHz 2x6 E5), 64 GB RAM, dual 10Gb NIC
  * Storage is 4x2TB 7200 RAID 5 (5.46TB usable)
* 20 cores (2.3GHz 2x10 E5), 128 GB RAM, dual 10Gb NIC
  * Storage is 6x2TB 7200 RAID 5 (9.09TB usable)

**Why don't I see the option to provision a Bare Metal server type?**

There are a couple reasons you might not see the option for Bare Metal servers.  First, check your data center and the current [availability for Bare Metal servers](https://www.ctl.io/data-centers/#/filters/Bare%20Metal).  Bare Metal servers are not available in all data centers. If you are in a data center where Bare Metal servers should be available, contact Customer Care to have them check to see if Bare Metal servers need to be enabled for your account.

**Why am I seeing an error saying "limit exceeded" for CPU, memory, or storage when I try to provision a Bare Metal server?**

All accounts start with a pre-defined resource (CPU/memory/storage) limit per data center. Bare Metal server resources are included as part of these limits. If you've reached the limits for your account, you may contact Customer Care to [request an increase on your resource limits](../Control Portal/how-to-increase-resources-on-account.md).

**Can I increase or decrease CPU, memory or storage resources on Bare Metal servers?**

No, the CPU, memory and storage are static resources on each individual Bare Metal server and can not be changed once a particular configuration has been provisioned. The best available path for adjusting the resource configuration is to provision a new server with the desired configuration and plan to migrate any data as necessary.

**What are the self-service actions available to me through the Control portal for Bare Metal servers?**

Through the Control portal you are able to power the Bare Metal server on or off, perform a server reset and add a single public IP.  

**What are the best suited workloads for this new server class?**

Any applications not well-suited to virtualization whether it be performance or licensing restrictions related, database and application workloads where consistent performance is critical, grid or HPC (High Performance Computing), data analytics, caching and indexing.

**How do I connect my Bare Metal servers over the network to my CenturyLink Cloud virtual servers?**

Bare Metal servers share the same network as CenturyLink Cloud virtual servers so it's as easy as creating and connecting networks amongst all your server types.  For more information on Network features of CenturyLink Cloud platform, reference the [Network Section](https://www.ctl.io/knowledge-base/network/#1) of our knowledge base.

**Since these servers use local storage, how do I avoid application failure if underlying hardware fails?**

It is your responsibility to maintain any data recovery or restoration process that may be necessary in the case of a critical hardware failure. An integrated backup solution will be available at some point but is not currently.

**How is hardware support and replacement handled for Bare Metal servers?**

CenturyLink is responsible for all hardware replacement for Bare Metal servers.  We monitor the Bare Metal servers underlying hardware using agentless SNMP monitoring via iLO.  If an incident is detected a ticket for investigation is automatically generated and the customer is notified. In the case where a server becomes completely unavailable the process to replace the server will begin immediately with consent from the customer. For additional service level details please reference the Bare Metal servers SLA on the [SLA page](https://www.ctl.io/legal/sla/).

**What are the security features available for Bare Metal servers?**

Bare Metal servers can be incorporated in the same firewall policies currently available with other CenturyLink Cloud server types. All Bare Metal servers are also provisioned with fully encrypted local storage for the protection of customer data.

**What should I do if I do not see the configuration of CPU/Memory/Storage I want?**

We've initially launched with a limited number of Bare Metal server configuration types and fully expect to expand upon the number of types and quantity available of each based on customer feedback.  The server configuration screen will provide an up to date indication of our available server types.  If you do not see a configuration type there that suits your needs, please submit a [Feature Request](https://www.ctl.io/knowledge-base/support/how-do-i-submit-a-feature-request/) including a brief explanation of your use case and the need for a particular configuration of resources.

**What features do Bare Metal servers share with CenturyLink Cloud virtual servers?**

While there are multiple in common between the two, there are several features available on virtual servers within CenturyLink Cloud that do not apply to Bare Metal servers.  Please see the [Server Comparison Matrix](../Servers/server-comparison-matrix.md) for more detail.

**Is there a term commit option available for Bare Metal servers?**

Yes, customers may work with their respective Sales representative to make use of the existing Cloud Term Commit process for Bare Metal servers in the same way they would for CenturyLink Cloud virtual servers.

**May I have console or iLO access to my Bare Metal server?**

No, there are a select number of management capabilities available through the Control portal including power operations and the ability to reset the server. No additional iLO or console access is included with the service.

**Can I change the administrator/root password of my server through Control or the API?**

No, the password can only be set at the time of server creation. If you would like to change the password on the server, you may do so through the OS, but the “show credentials” link in the Control portal will no longer display accurate credentials.

**Where are Bare Metal servers available geographically?**

Bare Metal servers availability can be viewed on the [CenturyLink Cloud data centers page](https://www.ctl.io/data-centers/#/filters/Bare%20Metal).

**What should I do if my Bare Metal server becomes unresponsive?**

Contact our Customer Care group by submitting a support request using the link at the top right side of this site.  If a ticket has not already been automatically generated, they will respond to your request and begin investigation.

**How is data destruction handled in the cases of hard drive failure/replacement and/or server relinquishment for Bare Metal servers?**

All local storage associated with Bare Metal servers is fully encrypted.  As such, destruction is not necessary to protect sensitive data.  Data is rendered unrecoverable as part of our routine rediscovery and provisioning process for servers that have been decommissioned.

**Do I still get billed for a Bare Metal server that is turned off?**

Yes, Bare Metal servers are dedicated to you once they have been provisioned and will continue to bill the normal hourly rate regardless of the state of the server.  Under certain circumstances, if a server has become unavailable to the point where it has exceeded the SLA for availability, credits may be applicable for the lost server time.

**Can I customize my storage configuration on a Bare Metal server?**

No, the storage configurations provisioned for Bare Metal servers are all either RAID 1 or RAID 5 depending on the server configuration type and tampering with that configuration could result in loss of management access which could disrupt support. Each server is provisioned with two partitions, one 300GB boot partition and a second partition for the remaining storage capacity for that particular configuration type.

**Can I bring my own OS image?**

No, the available Operating Systems include Windows 2012 R2, RHEL6 and CentOS. In the future there will be additional Linux and Windows variations available. If there is a particular OS image you would like to see incorporated please [submit a feature request](https://www.ctl.io/knowledge-base/support/how-do-i-submit-a-feature-request/).

**Can I use my own licensing for the OS?**

No, the licensing is factored into the cost of the Bare Metal server where applicable and can not be separated from the service.  If you would be interested in using your own OS licensing with Bare Metal servers, please let us know in a [feature request](https://www.ctl.io/knowledge-base/support/how-do-i-submit-a-feature-request/).
