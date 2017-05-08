{{{
  "title": "Network Exchange FAQs",
  "date": "04-27-2017",
  "author": "Rob Lesieur",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Product Overview

[Network Exchange](https://www.ctl.io/network-exchange/) provides a secure, high speed, redundant, private network to connect compute islands together to support hybrid IT. It is the preferred alternative to using the Internet or IPSec VPN for customers needing to connect their CenturyLink Cloud (CLC) environments to other, non-CLC environments. Network Exchange is ideal for your hybrid environment and applications as well as storage and backups. Network Exchange includes ease of setup and management via the CLC Control Portal, coupled with CLC network automation, and pre-deployed network infrastructure. All with usage based, pay as you go billing.

### Frequently Asked questions

**Q: How is Network Exchange secure?**

**A:** Network Exchange uses virtual routing to create routing environments specific to each customer. No global routing tables are used within the Network Exchange environment. There are also firewalls within CenturyLink Cloud accounts. In some cases, depending on the opposite endpoint, there may also be other firewalls.

**Q: Can anyone use Network Exchange?**

**A:** Anyone who already has or will create a CenturyLink Cloud account and has a valid endpoint to connect to. An example would be someone wanting to connect their CenturyLink Cloud VMs to their CenturyLink Dedicated Cloud Compute (DCC) environment.

**Q: Where do I go for support of Network Exchange?**

**A:** For additional information, questions, and support of the CLC Network Exchange UI, please refer to the Network Exchange product page for more information and links to resources. Questions and support requests should be emailed to help@ctl.io.

**Q: Is Network Exchange using SDN (Software Defined Network) technologies?**

**A:** Yes. Network Exchange uses software to deploy network configurations within the network infrastructure. All virtual circuits within Network Exchange can be build and deleted via a software front-end using RESTful based API communication.

**Q: Can customers build and delete their own virtual circuits within Network Exchange? Can Customer Service or someone other than the customer access Network Exchange to add or delete virtual circuits?**

**A:** Customers with a valid CenturyLink Cloud account and with the appropriate permissions can create, modify, or delete an exchange. CenturyLink Customer Service has access to all exchanges by default if customers wish for them to perform an action on their behalf. Customer may request for this access to be blocked.

**Q: Is the provisioning of a Network Exchange circuit completely automated from end-to-end?**

**A:** At the initial launch, Network Exchange provisioning to CLC is automated, but the provisioning to the other end-point is a combination of automation and manual provisioning for CenturyLink Managed Services and in the case of colocation, requires a cross connect be established for final connectivity.

**Q: Is Network Exchange Layer 2 or Layer 3?**

**A:** Network Exchange uses a combination of Layer 2 and Layer 3. Within the Network Exchange environment, BGP and L3 VPN are used to route traffic on a per customer basis. Each customer has their own virtualized routing table. At the edge, there is a combination of L2 VLANs and L3 routing.

**Q: What is the speed of the network?**

**A:** The speed of the network is dependent on distance and latency, but the capabilities can reach close to 10Gbps. Generally 1Gbps physical links and 10Gbps physical links are provisioned per customer in the case of colocation. The network core will be managed to meet demand.

**Q: Am I limited to the speed I can use?**

**A:** Currently the only limit is the slowest point in the network path. Generally customers will be provisioned with 1Gbps or 10Gbps in the case of colocation. Distance and latency also play into the overall speed.

**Q: Am I limited to how much data I can pass?**

**A:** There is currently no limit to the overall amount of data that can be passed. The limit is with how much data can be passed at any given time. This is due to the size of the network path.

**Q: How many connections can I create?**

**A:** An exchange may contain as many endpoints as are available at that location. The customer may create multiple exchanges, within the availability of endpoints for the location.

**Q: What is an “Exchange”?**

**A:** An exchange consists of two or more endpoints, all of which may communicate with each other.

**Q: Can I view the usage/speed/performance of each of my connections?**

**A:** Both ingress and egress traffic measurements are provided per endpoint.

**Q: What kind of workloads or scenarios is Network Exchange designed for?**

**A:** Network Exchange is designed for most common Hybrid IT workloads. For example, applications reliant on data or services in other environments, file transfer of large or small amounts of data, reliably accessing data/resources in another environment, replication, backups, along with being a key element for a business continuity or a disaster recovery strategy. It is not intended for streaming video or voice.

**Q: I'm a Cloud Network Service (CNS) customer. How does Network Exchange affect my CNS service?**

**A:** Network Exchange is a new service, indepdendent of Cloud Network Service. It will be operated in parallel with CNS and eventually replace it. CenturyLink will provide a migration path from CNS to Network Exchange and guide customers through the process. CNS customers will be provided ample notice prior to beginning the migration process. 

**Q: I'm a Cloud Network Service (CNS) customer. Can I use Network Exchange at the same time as CNS?**

**A:** Yes. A customer can use both CNS and Network Exchange at the same time so long as each is operated under it's own subaccount on CLC. Different VLANs must be used for CTL Managed Hosting endpoints.
