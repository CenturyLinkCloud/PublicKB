{{{
  "title": "Network Exchange FAQs",
  "date": "09-06-2016",
  "author": "Mark Lee",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Product Overview

[Network Exchange](https://www.ctl.io/network-exchange/) provides a secure, high speed, redundant, private network to connect your CenturyLink Cloud environment to other environments.  It is the preferred alternative to using the Internet or IPSec for customers needing to connect their CLC environments to other, non-CLC environments. Network Exchange is ideal for your hybrid environment and applications as well as storage and backups. Network Exchange includes ease of setup and management via the CLC Portal, coupled with CLC network automation, and pre-deployed network infrastructure. All with usage based, pay as you go billing.

**Q: How is Network Exchange secure?**

**A:** Network Exchange uses virtual routing to create routing environments specific to each customer. No global routing tables are used within the Network Exchange environment. There are also firewalls within CenturyLink Cloud accounts. In some cases, depending on the opposite endpoint, there may also be firewalls.

**Q: Can anyone use Network Exchange?**

**A:** Anyone who already has or will create a CenturyLink Cloud account and has a valid endpoint to connect to.  An example would be someone wanting to connect their CenturyLink Cloud VM’s to their CenturyLink Dedicated Cloud Compute (DCC) environment or their COLO environment in the same data center.

**Q: Where do I go for support of Network Exchange?**

**A:** For additional information, questions, and support of the CLC Network Exchange UI, please refer to the [Network Exchange](//www.ctl.io/network-exchange/) product page for more information and links to resources. Questions and support requests should be emailed to [help@ctl.io](mailto:help@ctl.io).

**Q: Is Network Exchange using SDN (Software Defined Network) technologies?**

**A:** Yes. Network Exchange uses software to deploy network configurations within the network infrastructure.  All virtual circuits within Network Exchange can be build and deleted via a software front-end using RESTful based API communication.

**Q: Can customers build and delete their own virtual circuits within Network Exchange? Can Customer Service or someone other than the customer access Network Exchange to add or delete virtual circuits?**

**A:** Customers with a valid CenturyLink Cloud account and with the appropriate permissions can create, modify, or delete a virtual circuit.  The administrator of the CenturyLink Cloud account will need to grant access to anyone who may need to perform an add, modify, or delete function.

**Q: Is the provisioning of a Network Exchange circuit completely automated from end-to-end?**

**A:** At the initial launch, Network Exchange provisioning to CLC is automated, but the provisioning to the other end-point is a combination of automation and manual provisioning.

**Q: Is Network Exchange Layer 2 or Layer 3?**

**A:** Network Exchange uses a combination of Layer 2 and Layer 3. Within the Network Exchange environment, BGP and L3 VPN are used to route traffic on a per customer basis. Each customer has their own virtualized routing table. At the edge, there is a combination of L2 VLANs and L3 routing. 

**Q: What is the speed of the network?**

**A:** The speed of the network is dependent on distance and latency, but the capabilities can reach close to 10Gbps. Generally 1Gbps physical links and 10Gbps physical links are provisioned per customer.

**Q:  Am I limited to the speed I can use?**

**A:** Currently the only limit is the slowest point in the network path.  Generally customers will be provisioned with 1Gbps or 10Gbps. Distance and latency also play into the overall speed.

**Q:  Am I limited to how much data I can pass?**

**A:** There is currently no limit to the overall amount of data that can be passed. The limit is with how much data can be passed at any given time.  This is due to the size of the network path. Generally, customers will be able to push 1Gbps or 10Gbps.

**Q: How many connections can I create?**

**A:** Only one virtual circuit per product type can be created at initial launch.  For example, one virtual circuit can be created between your CLC environment and your DCC environment.

**Q: What is a “virtual circuit”?  Is it different than a “connection”?**

**A:** Yes, a virtual circuit is the same as a connection. A virtual circuit is a logically isolated network path that may share physical connectivity with other virtual circuits, but is completely private. 

**Q: Can I view the speed/performance of each of my connections?**

**A:** There are no tools available to view the speed and performance of a virtual circuit at this time.

**Q: Where can I view usage information about my Network Exchange virtual circuits?**

**A:** This is not currently provided, but can be obtained via a request to Support, [help@ctl.io](mailto:help@ctl.io).

**Q: Can I use Network Exchange to create a connection to my other locations/environments that are connected to my IQ network?**

**A:** Currently, only connectivity between CenturyLink Cloud servers and Dedicated Cloud Compute is available via Network Exchange and the HAN. Connecting to locations/servers on your IQ network via Network Exchange is not currently available. Please consult your account manager for options for connecting other locations/environments.

**Q: How do I use Network Exchange to create a connection to my other clouds?**

**A:** This functionality is currently not available.

**Q: What APIs are available for Network Exchange?**

**A:** APIs are not currently available/published for use outside the portal.

**Q: What should I expect with regards to usage and billing?**

**A:** Network Exchange is usage based. Usage and billing is calculated on the quantity of GBs that have passed the Network Exchange switches for the customer’s unique virtual circuits for the month. This includes both ingress and egress traffic. Meaning, both the inbound and outbound traffic to/from a customer’s CLC environment.

**Q: What kind of workloads or scenarios is Network Exchange designed for?**

**A:** Network Exchange is designed for most common Hybrid IT workloads.  For example, applications reliant on data or services in other environments, file transfer of large or small amounts of data, reliably accessing data/resources in another environment, replication, backups, along with being a key element for a business continuity or a disaster recovery strategy. It is not intended for streaming video or voice.

**Q: Where is Network Exchange available?**

**A:** At time of launch, Network Exchange will be available at Santa Clara, which is CenturyLink Cloud UC1 and CenturyLink SC8 and SC9. It will be available for customers who have CenturyLink Cloud (CLC) and Dedicated Cloud Compute (DCC) at the data center.

**Q: Do I need to add routes to my CLC servers or DCC servers?**

**A:** No. This is not needed because of BGP.
