{{{
  "title": "Network Exchange FAQs",
  "date": "06-28-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Product Overview

[Network Exchange](https://www.ctl.io/network-exchange/) provides secure, high-speed, redundant, automated network connections between disparate IT environments allowing for a true hybrid environment. It is the preferred alternative to using the Internet or IPSec VPN for customers needing to connect two or more environments directly together. Common environments include CenturyLink Cloud (CLC), CenturyLink Private Cloud on VMware Cloud Foundation (VCF), Colocation environments, CenturyLink Managed Hosting, CenturyLink Dedicated Cloud Compute, 3rd party networks and customer owned devices. Network Exchange is ideal for your hybrid environment as well as capacity augmentation or cloud bursting, data migration, and disaster recovery. 

Network Exchange provides the user with near total control of connection setup and management via the Network Exchange Internet portal, combined with automation through software defined networking, and pre-deployed network infrastructure. 

### Frequently Asked questions

**Q: How is Network Exchange secure?**

**A:** Network Exchange uses dedicated, private equipment not accessible to the public and the Internet. Additionally, Network Exchange uses virtual routing to create routing environments specific to each customer. No global routing tables are used within the Network Exchange environment. There are also firewalls within CenturyLink Cloud accounts. In some cases, depending on the opposite endpoint, there may also be other firewalls.

**Q: Can anyone use Network Exchange?**

**A:** Anyone who already has or will create a CenturyLink Cloud account and has at least two valid endpoints (data sources) to connect within the same location. An example would be someone wanting to connect their CenturyLink Cloud VMs to their CenturyLink Dedicated Cloud Compute (DCC) environment.

**Q: Where do I go for support of Network Exchange?**

**A:** For additional information, questions, and support of the Network Exchange UI, please refer to the [Network Exchange Product Page](https://www.ctl.io/network-exchange) for more information and links to resources. Questions and support requests should be emailed to help@ctl.io.

**Q: Does Network Exchange use SDN (Software Defined Networking) technologies?**

**A:** Yes. Network Exchange uses software to deploy network configurations within the network infrastructure. All virtual circuits within Network Exchange can be build and deleted via a software front-end using RESTful based API communication.

**Q: Can customers build and delete their own virtual circuits within Network Exchange? Can Customer Service or someone other than the customer access Network Exchange to add or delete virtual circuits?**

**A:** Customers with a valid CenturyLink Cloud account and with the appropriate permissions can create, modify, or delete an exchange. CenturyLink Customer Service has access to all exchanges by default for the purpose of assisting customers. Customers can request for this access to be blocked.

**Q: Is the provisioning of a Network Exchange circuit completely automated from end-to-end?**

**A:** At the initial launch, Network Exchange provisioning to CenturyLink Cloud, CenturyLink Private Cloud on VCF and in the near future AWS is fully automated. The provisioning of Colocated and Dedicated Access Endpoints require physical implementation of cross connects and potentially some additional configuration. The provisioning to CenturyLink Managed Hosting Network (HAN) requires minimal manual configurations.

**Q: Is Network Exchange Layer 2 or Layer 3?**

**A:** Network Exchange uses a combination of Layer 2 and Layer 3. Within the Network Exchange environment, BGP (and optionally Static routing for Dedicated Access Endpoints) and L3 VPN are used to route traffic on a per customer basis. Each customer has their own virtualized routing table. At the edge, there is a combination of L2 VLANs and L3 routing.

**Q: What is the speed of the network?**

**A:** The speed of each Endpoint connection to the Network Exchange equipment is configured independently with rate limits selected by the customer. Two rate limits exist: 10 Gbps and 1 Gbps. 

**Q: Am I limited to the speed I can use?**

**A:** Currently, the only limit is the slowest point in the network path. Customers are self provisioned with 1Gbps or 10Gbps connections. Since all Exchange Endpoints must be in the same metro area, little latency is present.

**Q: Am I limited to how much data I can pass?**

**A:** There is currently no limit to the overall amount of data that can be passed. The limit is with how much data can be passed at any given time. This is due to the size of the network path.

**Q: How many connections can I create?**

**A:** An Exchange may contain multiple instances of several Endpoint types. Specifically, an Exchange can connect to an unlimited number of Colocated and Managed Hosting environments and customer owned devices in any of the metro areas that Network Exchange is available. The exception to this is that only one CenturyLink Cloud Endpoint is allowed per account at each location Network Exchange is available. Additionally, the customer may create multiple exchanges at each location.

**Q: What is an “Exchange”?**

**A:** An exchange consists of two or more endpoints or data sources, all of which may communicate with each other.

**Q: Can I view the usage/speed/performance of each of my connections?**

**A:** Both ingress and egress traffic measurements are provided per endpoint.

**Q: What kind of workloads or scenarios is Network Exchange designed for?**

**A:** Network Exchange is designed for most common Hybrid IT workloads. For example, applications reliant on data or services in other environments, file transfer of large or small amounts of data, reliably accessing data/resources in another environment, replication, backups, along with being a key element for a business continuity or a disaster recovery strategy. It is not intended for streaming video or voice.

**Q: I'm a Cloud Network Service (CNS) customer. How does Network Exchange affect my CNS service?**

**A:** Network Exchange is a new service, indepdendent of Cloud Network Service. It will be operated in parallel with CNS and eventually replace it. Currently, no time frame exists for a required migration from CNS to Network Exchange. CenturyLink can provide a migration path from CNS to Network Exchange and guide customers through the process. Several CNS customers have self-selected to migrate due to the ability of Network Exchange to allow for the self-management of connections between multiple Endpoints rather than relying on CenturyLink to manage each CNS connection between two data sources. 

**Q: I'm a Cloud Network Service (CNS) customer. Can I use Network Exchange at the same time as CNS?**

**A:** Yes. A customer can use both CNS and Network Exchange at the same time so long as each is operated under it's own subaccount on CLC. Different VLANs must be used for CenturyLink Managed Hosting Network (HAN) endpoints.
